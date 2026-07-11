#!/usr/bin/env python3
"""Generate a detailed hardware topology of THIS Windows PC.

Reads the real PnP device tree + CIM (the same data msinfo32 shows under
Components / Hardware Resources) and reconstructs the actual bus fabric:

    root complex -> root ports / bridges -> endpoints
    + RAM (DIMMs), displays, and plugged-in USB devices as leaf cards

Bus links carry REAL negotiated labels: PCIe "x4 G4", memory "DDR5", etc.
Software Environment (drivers, services, startup) is excluded — hardware only.
msinfo32.exe is GUI-only and won't produce a report non-interactively, so we
read its underlying source (the Win32 PnP/CIM device tree) directly.

    {name, generated, nodes:[{id,label,sub,cls,parent,cap,kind,grp,up?,link?}, ...]}

    cls  gen5 | gen4 | gen3       (from real PCIe gen where available)
    kind cpu | hub | leaf
    grp  gpu | disk | net | usb | mem | display   (telemetry / colour bucket)
    up   link state, network ports only
    link bus label drawn on the edge from the parent ("x4 G4", "DDR5", "USB")

    python make_pc_topology.py [--out out/topology_pc.json] [--name "my pc"]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

PS = r"""
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
Write-Output ('CPU|' + $cpu.Name.Trim() + '|' + $cpu.NumberOfCores + '|' + $cpu.NumberOfLogicalProcessors)
Get-NetAdapter -Physical | ForEach-Object { Write-Output ('LINK|' + $_.InterfaceDescription + '|' + $_.MediaConnectionState) }
try { Get-PhysicalDisk | ForEach-Object { Write-Output ('SIZE|' + $_.FriendlyName + '|' + $_.BusType + '|' + [math]::Round($_.Size/1GB) + 'GB') } } catch {}
try { Get-Disk -ErrorAction SilentlyContinue | ForEach-Object {
  $dn=$_.Number; $fn=$_.FriendlyName; $used=0; $tot=0
  Get-Partition -DiskNumber $dn -ErrorAction SilentlyContinue | Where-Object DriveLetter | ForEach-Object {
    $v=Get-Volume -DriveLetter $_.DriveLetter -ErrorAction SilentlyContinue
    if ($v -and $v.Size) { $tot += $v.Size; $used += ($v.Size - $v.SizeRemaining) }
  }
  if ($tot -gt 0) { Write-Output ('FILL|' + $fn + '|' + [math]::Round($used/$tot,4) + '|' + [math]::Round($used/1GB) + '|' + [math]::Round($tot/1GB)) }
} } catch {}
Get-CimInstance Win32_PhysicalMemory | ForEach-Object { Write-Output ('RAM|' + $_.DeviceLocator + '|' + [math]::Round($_.Capacity/1GB) + '|' + $_.ConfiguredClockSpeed + '|' + $_.SMBIOSMemoryType) }
try { Get-CimInstance -Namespace root\wmi WmiMonitorID -ErrorAction SilentlyContinue | ForEach-Object {
  $m=($_.ManufacturerName | Where-Object {$_ -gt 0} | ForEach-Object {[char]$_}) -join ''
  $n=($_.UserFriendlyName | Where-Object {$_ -gt 0} | ForEach-Object {[char]$_}) -join ''
  Write-Output ('MON|' + $m + ' ' + $n) } } catch {}
# Pipelined property lookups (one cmdlet call each) — per-device calls are ~50x
# slower. PAR = parent for every device (climb map); META/PROP = detail for the
# devices we render (PCI fabric, disks, named USB devices).
$all = Get-PnpDevice -PresentOnly
$all | Get-PnpDeviceProperty -KeyName 'DEVPKEY_Device_Parent' -ErrorAction SilentlyContinue | ForEach-Object { Write-Output ('PAR|' + $_.InstanceId + '|' + $_.Data) }
$kept = $all | Where-Object { $_.InstanceId -like 'PCI\*' -or $_.Class -eq 'DiskDrive' -or `
  (($_.InstanceId -like 'USB\*') -and $_.FriendlyName -and ($_.FriendlyName -notmatch 'Composite|Root Hub|Generic USB Hub|Unknown|Host Controller')) }
$kept | ForEach-Object { Write-Output ('META|' + $_.InstanceId + '|' + $_.Class + '|' + $_.FriendlyName) }
$kept | Get-PnpDeviceProperty -KeyName 'DEVPKEY_Device_LocationInfo','DEVPKEY_PciDevice_CurrentLinkWidth','DEVPKEY_PciDevice_CurrentLinkSpeed' -ErrorAction SilentlyContinue | ForEach-Object { Write-Output ('PROP|' + $_.InstanceId + '|' + $_.KeyName + '|' + $_.Data) }
"""

HEX_TAIL = re.compile(r"\s*-\s*[0-9A-Fa-f]{3,4}$")
DDR = {"34": "DDR5", "35": "LPDDR5", "26": "DDR4", "27": "LPDDR4", "24": "DDR3"}


def clean(name: str) -> str:
    name = name.replace("(R)", "").replace("(TM)", "").replace("(Microsoft)", "").strip()
    return re.sub(r"\s+", " ", HEX_TAIL.sub("", name)).strip()


def short_loc(loc: str) -> str:
    m = re.search(r"bus (\d+), device (\d+), function (\d+)", loc or "")
    return f"bus{m.group(1)}·dev{m.group(2)}·fn{m.group(3)}" if m else (loc or "")


def short_cpu(name: str) -> str:
    for g in ("12th Gen ", "13th Gen ", "14th Gen "):
        name = name.replace(g, "")
    return clean(name)


def pcie(cw: str, cs: str) -> tuple[str | None, str | None]:
    """(link label, cls) from negotiated width + speed code. gen == speed code."""
    try:
        w, gen = int(cw), int(cs)
    except (TypeError, ValueError):
        return None, None
    if not w:
        return None, None
    cls = "gen5" if gen >= 5 else "gen4" if gen == 4 else "gen3"
    return f"x{w} G{gen}", cls


def is_hub(name: str, cls: str = "") -> bool:
    low = name.lower()
    if cls == "USBHub" or ("usb" in low and "hub" in low):
        return True
    return any(k in low for k in ("root port", "peg", "root complex", "bridge",
                                  "upstream", "downstream", " dmi"))


def classify(name: str, cls: str) -> dict:
    low = name.lower()
    if cls == "Net":
        if "x710" in low or "10g" in low or "sfp" in low:
            return {"cls": "gen4", "cap": 20, "grp": "net"}
        if "i226" in low or "i225" in low or "2.5g" in low:
            return {"cls": "gen3", "cap": 2.5, "grp": "net"}
        if any(s in low for s in ("wi-fi", "wifi", "wireless", "rz6", "ax2", "be2")):
            return {"cls": "gen3", "cap": 2.4, "grp": "net"}
        return {"cls": "gen3", "cap": 1, "grp": "net"}
    if cls == "Display":
        return {"cls": "gen4", "cap": 4, "grp": "gpu"}
    if cls in ("SCSIAdapter", "HDC") or "nvm express" in low:
        return {"cls": "gen4", "cap": 0, "grp": None}   # controller structural; disk carries load
    if cls == "DiskDrive":
        return {"cls": "gen4", "cap": 7, "grp": "disk"}
    if cls == "USB" or "usb" in low or "thunderbolt" in low:
        return {"cls": ("gen4" if "usb4" in low or "3.2" in low else "gen3"),
                "cap": (40 if "usb4" in low else 10), "grp": "usb"}
    return {"cls": "gen3", "cap": 0, "grp": None}       # structural PCH/CPU function


def probe() -> list[str]:
    r = subprocess.run(["powershell.exe", "-NoProfile", "-Command", PS],
                       capture_output=True, text=True)
    lines = [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
    if not any(ln.startswith("META|") for ln in lines):
        raise RuntimeError((r.stderr or "no PnP device data from PowerShell").strip()[-600:])
    return lines


def build(lines: list[str]) -> list[dict]:
    cpu_name, cores, threads = "CPU", "", ""
    link, size, fill, rams, mons, pmap = {}, {}, {}, [], [], {}
    meta = {}   # iid -> (class, name)
    prop = {}   # iid -> {loc, cw, cs}
    for ln in lines:
        p = ln.split("|")
        if p[0] == "CPU":
            cpu_name, cores, threads = short_cpu(p[1]), p[2], p[3]
        elif p[0] == "LINK":
            link[clean(p[1])] = (p[2].strip().lower() == "connected")
        elif p[0] == "SIZE":
            size[clean(p[1])] = f"{p[2]} · {p[3]}"
        elif p[0] == "FILL" and len(p) >= 5:
            fill[clean(p[1])] = (float(p[2]), p[3], p[4])   # (fraction, usedGB, totalGB)
        elif p[0] == "RAM" and len(p) >= 5:
            rams.append((p[1], p[2], p[3], p[4]))
        elif p[0] == "MON":
            mons.append(clean(p[1]))
        elif p[0] == "PAR" and len(p) >= 2:
            pmap[p[1]] = p[2] if len(p) > 2 else ""
        elif p[0] == "META" and len(p) >= 4:
            meta[p[1]] = (p[2], "|".join(p[3:]))
        elif p[0] == "PROP" and len(p) >= 4:
            key, data = p[2], "|".join(p[3:])
            slot = prop.setdefault(p[1], {})
            if "LocationInfo" in key:
                slot["loc"] = data
            elif "CurrentLinkWidth" in key:
                slot["cw"] = data
            elif "CurrentLinkSpeed" in key:
                slot["cs"] = data

    # (iid, parent, cls, loc, cw, cs, name)
    devs = [(iid, pmap.get(iid, ""), cls, prop.get(iid, {}).get("loc", ""),
             prop.get(iid, {}).get("cw", ""), prop.get(iid, {}).get("cs", ""), name)
            for iid, (cls, name) in meta.items()]
    kept = set(meta)
    ctrl_iid = next((iid for iid, par, cls, loc, cw, cs, name in devs
                     if cls in ("SCSIAdapter", "HDC") or "nvm express" in name.lower()), None)
    root_iid = next((iid for iid, par, cls, loc, cw, cs, name in devs
                     if "host bridge" in name.lower() or "bus 0, device 0, function 0" in (loc or "")),
                    "__root__")

    def nearest_kept(iid: str) -> str | None:
        """Climb the real PnP parent chain to the closest ancestor we render,
        stepping through intermediate hubs (USB root hubs, ACPI nodes)."""
        cur, hops = pmap.get(iid, ""), 0
        while cur and hops < 40:
            if cur in kept:
                return cur
            cur, hops = pmap.get(cur, ""), hops + 1
        return None

    nodes, idmap, n = {}, {}, 0

    def nid(iid):
        nonlocal n
        if iid not in idmap:
            idmap[iid] = f"n{n}"; n += 1
        return idmap[iid]

    nodes[root_iid] = {"id": nid(root_iid), "label": cpu_name, "kind": "cpu", "cls": "gen5",
                       "parent": None, "sub": f"{threads} threads · {cores} cores · root complex"}

    for iid, par, cls, loc, cw, cs, name in devs:
        if iid == root_iid:
            continue
        label = clean(name)
        node = {"id": nid(iid), "label": label, "sub": short_loc(loc), "parent": None}
        blabel, bcls = pcie(cw, cs)
        if is_hub(name, cls):
            node.update(kind="hub", cls=(bcls or ("gen5" if "peg" in name.lower() else "gen3")), cap=0)
        else:
            c = classify(name, cls)
            node.update(kind="leaf", cls=(bcls or c["cls"]), cap=c["cap"])
            if c["grp"]:
                node["grp"] = c["grp"]
            if blabel:
                node["link"] = blabel
            if c["grp"] == "net":
                up = link.get(label)
                if up is not None:
                    node["up"] = up
                    node["sub"] += " · " + ("link up" if up else "no link")
            if cls == "DiskDrive" and label in size:
                node["sub"] = size[label]
            if cls == "DiskDrive" and label in fill:
                frac, used, tot = fill[label]
                node["fill"] = frac
                node["sub"] = f"{used}/{tot}GB used"
        if cls == "DiskDrive" and ctrl_iid:
            node["_parent_iid"] = ctrl_iid
        else:
            node["_parent_iid"] = nearest_kept(iid) or root_iid
        nodes[iid] = node

    for iid, node in nodes.items():
        if iid != root_iid:
            node["parent"] = nodes[node.pop("_parent_iid")]["id"]

    out = list(nodes.values())

    # prune empty bridges (root ports with nothing downstream)
    changed = True
    while changed:
        parents = {x["parent"] for x in out}
        before = len(out)
        out = [x for x in out if not (x["kind"] == "hub" and x["id"] not in parents)]
        changed = len(out) < before

    # ---- append synthetic cards WMI has no PnP node for (won't be pruned) ----
    # USB devices are already nested by the real parent-climb above.
    root_id = nodes[root_iid]["id"]
    gpu_id = next((x["id"] for x in out if x.get("grp") == "gpu"), root_id)

    def add(node):
        nonlocal n
        node["id"] = f"n{n}"; n += 1
        out.append(node)
        return node["id"]

    # RAM nests under a synthesized memory controller: CPU -> IMC -> channel -> DIMM
    if rams:
        imc_id = add({"label": "Integrated Memory Controller", "sub": "IMC",
                      "cls": "gen5", "parent": root_id, "kind": "hub", "cap": 0})
        chan_ids = {}
        for loc, gb, cfg, mtype in rams:
            m = re.search(r"Channel\s*([A-Z0-9]+)", loc)
            chan = m.group(1) if m else "?"
            if chan not in chan_ids:
                chan_ids[chan] = add({"label": f"Channel {chan}", "sub": "memory channel",
                                      "cls": "gen5", "parent": imc_id, "kind": "hub", "cap": 0})
            ddr = DDR.get(str(mtype), "DDR")
            add({"label": f"{gb}GB {ddr}-{cfg}", "sub": loc, "cls": "gen5",
                 "parent": chan_ids[chan], "kind": "leaf", "cap": 38, "grp": "mem", "link": ddr})

    for mon in mons:
        add({"label": mon or "Display", "sub": "monitor", "cls": "gen4",
             "parent": gpu_id, "kind": "leaf", "cap": 6, "grp": "display", "link": "video"})

    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join("out", "topology_pc.json"))
    ap.add_argument("--name", default="my desktop pc")
    args = ap.parse_args()
    if not sys.platform.startswith("win"):
        sys.exit("make_pc_topology.py reads Windows hardware via PowerShell/CIM — run it on the PC.")

    nodes = build(probe())
    topo = {"name": args.name,
            "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "nodes": nodes}
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(topo, fh, indent=2)
    print(f"wrote {args.out}  ({len(nodes)} modules)")


if __name__ == "__main__":
    main()
