"""Post-normalize enrichment: vendor from MAC OUI, kind inference, aging.

oui.csv is a minimal starter table. Replace with the full IEEE registry
(http://standards-oui.ieee.org/oui/oui.csv) for real coverage; loader tolerates
either the trimmed 2-column form used here or the full IEEE CSV.
"""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone, timedelta

from .schema import Topology, Node

_OUI_PATH = os.path.join(os.path.dirname(__file__), "oui.csv")
_oui_cache: dict[str, str] | None = None


def _load_oui() -> dict[str, str]:
    global _oui_cache
    if _oui_cache is not None:
        return _oui_cache
    table: dict[str, str] = {}
    if os.path.exists(_OUI_PATH):
        with open(_OUI_PATH, newline="") as fh:
            for row in csv.reader(fh):
                if not row or row[0].startswith("#"):
                    continue
                # trimmed form: "AABBCC,Vendor"  |  IEEE form has assignment in col 1
                if len(row) >= 2 and len(row[0].replace(":", "").replace("-", "")) == 6:
                    prefix = row[0].replace(":", "").replace("-", "").upper()
                    table[prefix] = row[1].strip()
                elif len(row) >= 3:  # IEEE "MA-L,AABBCC,Company"
                    table[row[1].strip().upper()] = row[2].strip()
    _oui_cache = table
    return table


def vendor_for_mac(mac: str | None) -> str | None:
    if not mac:
        return None
    prefix = mac.replace(":", "").upper()[:6]
    return _load_oui().get(prefix)


# crude kind inference from vendor/name hints; real topology gets kind from
# collectors (a switch reported over SNMP is already kind=switch).
_HINTS = [
    ("firewall", ("opnsense", "pfsense", "fortigate", "firewall")),
    ("switch", ("unifi", "switch", "cisco", "netgear", "mikrotik")),
    ("ap", ("ap ", "access point", "u6", "u7", "uap")),
    ("iot", ("tuya", "espressif", "shelly", "sonoff", "tasmota", "camera", "cam-")),
]


def infer_kind(node: Node) -> str:
    if node.kind and node.kind != "unknown":
        return node.kind
    hay = f"{(node.name or '').lower()} {(node.vendor or '').lower()}"
    for kind, needles in _HINTS:
        if any(nd in hay for nd in needles):
            return kind
    return "host"


def enrich(topo: Topology, offline_after_minutes: int = 30) -> Topology:
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=offline_after_minutes)
    for n in topo.nodes:
        if not n.vendor:
            n.vendor = vendor_for_mac(n.mac)
        n.kind = infer_kind(n)
        # age out hosts not seen recently
        if n.last_seen:
            try:
                seen = datetime.fromisoformat(n.last_seen)
                if seen < cutoff:
                    n.online = False
            except ValueError:
                pass
    return topo
