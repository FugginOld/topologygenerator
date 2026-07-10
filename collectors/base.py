"""Collector base. Each collector is read-only and returns a list of raw dicts.

Raw dict conventions (all optional unless noted):
  node: {"source": str(req), "name", "ip", "mac", "nodekind", "vendor",
         "host", "tags": [..], "online": bool, "last_seen": iso}
  link: {"source": str(req), "kind": "link", "src": node_id, "dst": node_id,
         "linkkind": "uplink|l2|l3|overlay|host", "port": str}
  zone: emitted via .zones() -> [{"vid","name","subnet","policy","cls"}]

Collectors never raise on a down source: log and return []. A partial map beats
no map.
"""
from __future__ import annotations

import json
import logging
import os
from abc import ABC, abstractmethod

log = logging.getLogger("collector")


class Collector(ABC):
    name: str = "base"

    def __init__(self, cfg: dict):
        self.cfg = cfg or {}

    @property
    def enabled(self) -> bool:
        return bool(self.cfg.get("enabled", False))

    @abstractmethod
    def collect(self) -> list[dict]:
        """Return raw node/link dicts. Must not raise on source failure."""
        ...

    def zones(self) -> list[dict]:
        """Optional: collectors that know VLAN definitions override this."""
        return []

    def _tag(self, items: list[dict]) -> list[dict]:
        for it in items:
            it.setdefault("source", self.name)
        return items

    def dump_raw(self, items: list[dict], outdir: str) -> None:
        path = os.path.join(outdir, f"{self.name}.raw.json")
        try:
            with open(path, "w") as fh:
                json.dump(items, fh, indent=2)
        except OSError as e:
            log.warning("could not write raw for %s: %s", self.name, e)
