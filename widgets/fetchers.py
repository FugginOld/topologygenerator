"""Widget fetchers: a service's API -> a compact stats dict for its panel.

Collector contract: stdlib-only, NEVER raise, return {} on any source failure.
Reuse a `collectors/` client for transport/auth where one exists; otherwise a few
lines of urllib. Keep the returned keys small and display-agnostic — the client
decides layout.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request


def _num(x) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def pihole(cfg: dict) -> dict:
    """Pi-hole v5 summary API (summaryRaw). token optional for public stats."""
    base = (cfg.get("url") or "").rstrip("/")
    if base.endswith("/admin"):
        base = base[: -len("/admin")]
    if not base:
        return {}
    q = urllib.parse.urlencode({"summaryRaw": "", "auth": cfg.get("token", "")})
    try:
        with urllib.request.urlopen(f"{base}/admin/api.php?{q}", timeout=8) as r:
            d = json.load(r)
    except Exception:
        return {}
    if not isinstance(d, dict) or "dns_queries_today" not in d:
        return {}                                        # wrong endpoint / Pi-hole v6 / auth needed
    return {
        "status": d.get("status", "unknown"),
        "queries": int(_num(d.get("dns_queries_today"))),
        "blocked": int(_num(d.get("ads_blocked_today"))),
        "block_pct": round(_num(d.get("ads_percentage_today")), 1),
        "blocklist": int(_num(d.get("domains_being_blocked"))),
    }


def proxmox(cfg: dict) -> dict:
    """Cluster resource summary via the PVE collector's authenticated transport."""
    try:
        from collectors.proxmox import ProxmoxCollector
        res = ProxmoxCollector(cfg)._get("/cluster/resources") or []   # reuse token+TLS transport
    except Exception:
        return {}
    if not res:
        return {}
    run = lambda t: sum(1 for r in res if r.get("type") == t and r.get("status") == "running")
    tot = lambda t: sum(1 for r in res if r.get("type") == t)
    nodes = [r for r in res if r.get("type") == "node"]
    maxcpu = sum(_num(n.get("maxcpu")) for n in nodes) or 1
    maxmem = sum(_num(n.get("maxmem")) for n in nodes) or 1
    return {
        "nodes": sum(1 for n in nodes if n.get("status") == "online"),
        "vms": run("qemu"), "vms_total": tot("qemu"),
        "lxc": run("lxc"), "lxc_total": tot("lxc"),
        "cpu_pct": round(sum(_num(n.get("cpu")) for n in nodes) / maxcpu * 100, 1),
        "mem_pct": round(sum(_num(n.get("mem")) for n in nodes) / maxmem * 100, 1),
    }


def unifi(cfg: dict) -> dict:
    """WAN + client + gateway summary via the UniFi collector's dashboard()."""
    try:
        from collectors.unifi import UnifiCollector
        d = UnifiCollector(cfg).dashboard() or {}
    except Exception:
        return {}
    if not d:
        return {}
    gw, wan, tp, cl = d.get("gateway", {}), d.get("wan", {}), d.get("throughput", {}), d.get("clients", {})
    return {
        "wan_up": bool(wan.get("up")),
        "wan_status": wan.get("status") or "?",
        "clients": cl.get("total"),
        "rx_bps": tp.get("rx_bps"), "tx_bps": tp.get("tx_bps"),
        "gw_cpu": gw.get("cpu"), "gw_mem": gw.get("mem"),
    }
