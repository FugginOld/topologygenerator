"""Tailscale overlay plane via `tailscale status --json`.

Tags online tailnet peers with "ts" and emits overlay links between them so the
renderer can draw the mesh that cuts across VLANs. Matches peers back to L2 hosts
by hostname during normalize (best-effort; MAC isn't visible over the tailnet).

Config:
  tailscale:
    enabled: true
    binary: tailscale        # or full path
"""
from __future__ import annotations

import json
import logging
import shutil
import subprocess

from .base import Collector
from core.schema import now_iso

log = logging.getLogger("collector.tailscale")


class TailscaleCollector(Collector):
    name = "tailscale"

    def collect(self) -> list[dict]:
        binary = self.cfg.get("binary", "tailscale")
        if not shutil.which(binary):
            log.warning("tailscale binary not found")
            return []
        try:
            out = subprocess.run(
                [binary, "status", "--json"],
                capture_output=True, text=True, timeout=20, check=False,
            )
            data = json.loads(out.stdout or "{}")
        except (subprocess.TimeoutExpired, OSError, json.JSONDecodeError) as e:
            log.warning("tailscale status failed: %s", e)
            return []

        ts = now_iso()
        items: list[dict] = []
        peers = list((data.get("Peer") or {}).values())
        # include self
        self_node = data.get("Self")
        if self_node:
            peers.append(self_node)

        ts_names = []
        for p in peers:
            name = (p.get("HostName") or p.get("DNSName", "").split(".")[0] or "").strip()
            if not name:
                continue
            ips = p.get("TailscaleIPs") or []
            online = bool(p.get("Online"))
            items.append({
                "name": name,
                "ip": ips[0] if ips else None,   # tailnet IP; L2 match is by name
                "tags": ["ts"],
                "online": online,
                "last_seen": ts,
            })
            if online:
                ts_names.append(name)

        # overlay mesh (logical full-mesh among online peers)
        for i in range(len(ts_names)):
            for j in range(i + 1, len(ts_names)):
                items.append({
                    "kind": "link", "src": ts_names[i], "dst": ts_names[j],
                    "linkkind": "overlay",
                })
        return self._tag(items)
