"""Live host discovery via arp-scan (preferred) or nmap -sn fallback.

Requires one of:
  - arp-scan  (sudo apt install arp-scan)   -- gives IP+MAC+vendor in one shot
  - nmap      (sudo apt install nmap)        -- IP+MAC, no vendor

Config (config.yaml):
  arpscan:
    enabled: true
    interfaces: [eth0.10, eth0.30]     # optional; arp-scan --localnet per if
    subnets: [10.0.30.0/24]            # optional; explicit targets
    use_sudo: true
"""
from __future__ import annotations

import logging
import re
import shutil
import subprocess

from .base import Collector
from core.schema import now_iso

log = logging.getLogger("collector.arpscan")

# arp-scan line: "10.0.30.10\taa:bb:cc:dd:ee:ff\tVendor string"
_ARP_RE = re.compile(
    r"^(\d{1,3}(?:\.\d{1,3}){3})\s+([0-9a-fA-F:]{17})\s*(.*)$"
)
# nmap -sn "Nmap scan report for host (10.0.30.10)" + "MAC Address: AA:.. (Vendor)"
_NMAP_IP = re.compile(r"Nmap scan report for (?:(\S+) )?\(?(\d{1,3}(?:\.\d{1,3}){3})\)?")
_NMAP_MAC = re.compile(r"MAC Address: ([0-9A-Fa-f:]{17}) \((.*)\)")


class ArpScanCollector(Collector):
    name = "arpscan"

    def collect(self) -> list[dict]:
        if shutil.which("arp-scan"):
            return self._tag(self._arpscan())
        if shutil.which("nmap"):
            return self._tag(self._nmap())
        log.warning("neither arp-scan nor nmap found on PATH")
        return []

    def _run(self, cmd: list[str]) -> str:
        if self.cfg.get("use_sudo"):
            cmd = ["sudo", "-n", *cmd]
        try:
            out = subprocess.run(
                cmd, capture_output=True, text=True, timeout=120, check=False
            )
            if out.returncode != 0:
                log.warning("%s exited %s: %s", cmd[0], out.returncode, out.stderr.strip())
            return out.stdout
        except (subprocess.TimeoutExpired, OSError) as e:
            log.warning("failed to run %s: %s", cmd, e)
            return ""

    def _targets(self) -> list[list[str]]:
        cmds = []
        for iface in self.cfg.get("interfaces", []):
            cmds.append(["arp-scan", "--localnet", f"--interface={iface}"])
        for subnet in self.cfg.get("subnets", []):
            cmds.append(["arp-scan", subnet])
        if not cmds:  # default: whole local net on default iface
            cmds.append(["arp-scan", "--localnet"])
        return cmds

    def _arpscan(self) -> list[dict]:
        seen: dict[str, dict] = {}
        ts = now_iso()
        for cmd in self._targets():
            for line in self._run(cmd).splitlines():
                m = _ARP_RE.match(line.strip())
                if not m:
                    continue
                ip, mac, vendor = m.group(1), m.group(2), (m.group(3) or "").strip()
                seen[mac.lower()] = {
                    "ip": ip,
                    "mac": mac,
                    "name": ip,
                    "vendor": vendor or None,
                    "online": True,
                    "last_seen": ts,
                }
        return list(seen.values())

    def _nmap(self) -> list[dict]:
        subnets = self.cfg.get("subnets") or ["--localnet"]
        nodes, ts = [], now_iso()
        for subnet in subnets:
            text = self._run(["nmap", "-sn", subnet])
            cur = None
            for line in text.splitlines():
                ipm = _NMAP_IP.search(line)
                if ipm:
                    cur = {"ip": ipm.group(2), "name": ipm.group(1) or ipm.group(2),
                           "online": True, "last_seen": ts}
                    nodes.append(cur)
                macm = _NMAP_MAC.search(line)
                if macm and cur is not None:
                    cur["mac"] = macm.group(1)
                    cur["vendor"] = macm.group(2)
        return nodes
