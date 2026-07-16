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


def _pihole_base(url: str) -> str:
    base = (url or "").rstrip("/")
    return base[: -len("/admin")] if base.endswith("/admin") else base


def _v6_stats(summary: dict, blocking: dict | None) -> dict:
    """Pure map of Pi-hole v6 /stats/summary (+ /dns/blocking) -> panel stats."""
    q = (summary or {}).get("queries") or {}
    if "total" not in q:
        return {}
    g = (summary or {}).get("gravity") or {}
    out = {}
    if blocking and blocking.get("blocking"):
        out["status"] = blocking["blocking"]
    out.update({
        "queries": int(_num(q.get("total"))),
        "blocked": int(_num(q.get("blocked"))),
        "block_pct": round(_num(q.get("percent_blocked")), 1),
        "blocklist": int(_num(g.get("domains_being_blocked"))),
    })
    return out


def _v5_stats(d: dict) -> dict:
    if not isinstance(d, dict) or "dns_queries_today" not in d:
        return {}
    return {
        "status": d.get("status", "unknown"),
        "queries": int(_num(d.get("dns_queries_today"))),
        "blocked": int(_num(d.get("ads_blocked_today"))),
        "block_pct": round(_num(d.get("ads_percentage_today")), 1),
        "blocklist": int(_num(d.get("domains_being_blocked"))),
    }


def _pihole_v6(base: str, token: str) -> dict:
    """Pi-hole v6 REST API: POST /api/auth -> SID, GET /api/stats/summary, then
    release the session (v6 caps concurrent sessions, so we must log out)."""
    api, sid = base + "/api", None
    try:
        body = json.dumps({"password": token or ""}).encode()
        req = urllib.request.Request(api + "/auth", data=body,
                                     headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=8) as r:
            sess = (json.load(r) or {}).get("session") or {}
        if sess.get("valid"):
            sid = sess.get("sid")
    except Exception:
        pass                                             # unprotected instance -> try unauthenticated
    hdr = {"X-FTL-SID": sid} if sid else {}
    try:
        with urllib.request.urlopen(urllib.request.Request(api + "/stats/summary", headers=hdr), timeout=8) as r:
            summary = json.load(r)
        blocking = None
        try:
            with urllib.request.urlopen(urllib.request.Request(api + "/dns/blocking", headers=hdr), timeout=6) as r:
                blocking = json.load(r)
        except Exception:
            pass
        return _v6_stats(summary, blocking)
    except Exception:
        return {}
    finally:
        if sid:                                          # log out so we don't leak sessions each poll
            try:
                urllib.request.urlopen(urllib.request.Request(
                    api + "/auth", headers={"X-FTL-SID": sid}, method="DELETE"), timeout=5)
            except Exception:
                pass


def _pihole_v5(base: str, token: str) -> dict:
    q = urllib.parse.urlencode({"summaryRaw": "", "auth": token or ""})
    try:
        with urllib.request.urlopen(f"{base}/admin/api.php?{q}", timeout=8) as r:
            return _v5_stats(json.load(r))
    except Exception:
        return {}


def pihole(cfg: dict) -> dict:
    """Pi-hole stats — v6 REST API (/api) first, falling back to the v5 api.php."""
    base = _pihole_base(cfg.get("url"))
    if not base:
        return {}
    token = cfg.get("token", "")
    return _pihole_v6(base, token) or _pihole_v5(base, token)


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


if __name__ == "__main__":   # ponytail: pure response->stats mapping, offline
    v6 = _v6_stats({"queries": {"total": 10000, "blocked": 3100, "percent_blocked": 31.0},
                    "gravity": {"domains_being_blocked": 120000}}, {"blocking": "enabled"})
    assert v6 == {"status": "enabled", "queries": 10000, "blocked": 3100,
                  "block_pct": 31.0, "blocklist": 120000}, v6
    assert _v6_stats({}, None) == {}                      # no queries -> empty
    assert _v5_stats({"dns_queries_today": 5, "ads_blocked_today": 1,
                      "ads_percentage_today": 20.0, "domains_being_blocked": 9,
                      "status": "enabled"})["queries"] == 5
    assert _pihole_base("http://10.0.10.5/admin") == "http://10.0.10.5"
    print("widgets/fetchers pihole self-check ok")
