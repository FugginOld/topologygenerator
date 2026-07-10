"""OPNsense collector -- the authoritative source for VLAN zones + DHCP names.

Uses the OPNsense REST API (key/secret as basic auth). Create a key under
System > Access > Users > (user) > API keys.

Config:
  opnsense:
    enabled: true
    url: https://10.0.10.1
    key: "..."          # keep in config.yaml (gitignored), never commit
    secret: "..."
    verify_tls: false   # true if the firewall has a trusted cert
    zone_map:           # map interface/description -> zone class + policy
      SERVERS: {cls: srv, policy: "selective"}
      IOT:     {cls: iot, policy: "no lateral"}

Endpoints used (stable across recent OPNsense):
  /api/interfaces/vlan_settings/searchItem      VLAN tag definitions
  /api/dhcpv4/leases/searchLease                DHCP leases (names + MAC + IP)
  /api/diagnostics/interface/getArp             ARP table (live presence)
"""
from __future__ import annotations

import ipaddress
import logging

from .base import Collector
from core.schema import now_iso

log = logging.getLogger("collector.opnsense")

try:
    import requests
except ImportError:  # requests listed in requirements.txt
    requests = None


class OPNsenseCollector(Collector):
    name = "opnsense"

    def _get(self, path: str):
        base = self.cfg["url"].rstrip("/")
        try:
            r = requests.get(
                f"{base}{path}",
                auth=(self.cfg["key"], self.cfg["secret"]),
                verify=self.cfg.get("verify_tls", False),
                timeout=15,
            )
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001 - never raise out of a collector
            log.warning("GET %s failed: %s", path, e)
            return None

    def _post(self, path: str, payload: dict | None = None):
        base = self.cfg["url"].rstrip("/")
        try:
            r = requests.post(
                f"{base}{path}",
                json=payload or {},
                auth=(self.cfg["key"], self.cfg["secret"]),
                verify=self.cfg.get("verify_tls", False),
                timeout=15,
            )
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001
            log.warning("POST %s failed: %s", path, e)
            return None

    # ---- zones from VLAN settings ----
    def zones(self) -> list[dict]:
        if requests is None:
            return []
        data = self._post("/api/interfaces/vlan_settings/searchItem", {"current": 1, "rowCount": 500})
        rows = (data or {}).get("rows", [])
        zmap = self.cfg.get("zone_map", {})
        zones = []
        for row in rows:
            # row has vlan tag + parent + description
            try:
                vid = int(row.get("tag") or 0)
            except (TypeError, ValueError):
                continue
            desc = (row.get("descr") or row.get("description") or f"VLAN{vid}").strip()
            key = desc.upper()
            meta = zmap.get(key, zmap.get(desc, {}))
            zones.append({
                "vid": vid,
                "name": desc,
                "subnet": row.get("subnet", ""),   # often filled from iface cfg
                "policy": meta.get("policy", ""),
                "cls": meta.get("cls", "unknown"),
            })
        return zones

    def collect(self) -> list[dict]:
        if requests is None:
            log.warning("requests not installed; skipping opnsense")
            return []
        nodes: dict[str, dict] = {}
        ts = now_iso()

        # DHCP leases -> names + mac + ip
        leases = self._post("/api/dhcpv4/leases/searchLease", {"current": 1, "rowCount": 2000})
        for row in (leases or {}).get("rows", []):
            mac = (row.get("mac") or "").lower()
            ip = row.get("address") or row.get("ip")
            name = row.get("hostname") or row.get("descr") or ip
            if not (mac or ip):
                continue
            nodes[mac or ip] = {
                "ip": ip, "mac": mac or None, "name": name,
                "online": row.get("status", "").lower() == "online",
                "last_seen": ts,
            }

        # ARP table -> live presence, fills gaps
        arp = self._get("/api/diagnostics/interface/getArp") or []
        for entry in arp if isinstance(arp, list) else arp.get("rows", []):
            mac = (entry.get("mac") or "").lower()
            ip = entry.get("ip")
            if not (mac or ip):
                continue
            key = mac or ip
            node = nodes.setdefault(key, {"ip": ip, "mac": mac or None,
                                          "name": entry.get("hostname") or ip})
            node["online"] = True
            node["last_seen"] = ts
            node.setdefault("vendor", entry.get("manufacturer"))

        return self._tag(list(nodes.values()))
