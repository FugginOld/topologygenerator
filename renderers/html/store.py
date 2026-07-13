"""Topology store — persistence over a guarded directory (`out/topologies/*.json`).

Deep and narrow: bytes in/out, plus the single path-injection barrier every
user-supplied id passes through. No presentation (the sidebar row shaping lives
with the Handler), so this imports nothing server-specific and is testable with
no HTTP — see the __main__ self-check.
"""
from __future__ import annotations

import json
import os
import re
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.abspath(os.path.join(_HERE, "..", "..", "out", "topologies"))


def path(tid: str) -> str:
    """Resolve <tid>.json inside STORE, refusing any id that escapes it.

    The single barrier for every user-supplied id: strip directory parts,
    allowlist the charset, then confirm the resolved file really sits directly
    in STORE (blocks '..', absolute paths, separators, symlink tricks).
    """
    name = os.path.basename(tid)
    if not re.fullmatch(r"[A-Za-z0-9._-]+", name):
        raise ValueError("bad topology id")
    fp = os.path.realpath(os.path.join(STORE, name + ".json"))
    if os.path.dirname(fp) != os.path.realpath(STORE):
        raise ValueError("bad topology id")
    return fp


def slug(name: str) -> str:
    """Timestamped id — keeps generated topologies unique."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "topology"
    return f"{s}-{int(time.time())}"


def stable_slug(name: str) -> str:
    """No timestamp — one stable entry per host, so re-pushes overwrite."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "host"


def save(topo: dict, source: str | None = None) -> dict:
    """Persist a topology keyed by its (slugged) name. `source` records the push
    origin for reported hosts. Returns {id, name}."""
    name = (topo.get("name") or "host").strip()
    tid = stable_slug(name)
    topo["name"] = name
    if source is not None:
        topo["source"] = source
    os.makedirs(STORE, exist_ok=True)
    with open(path(tid), "w", encoding="utf-8") as fh:
        json.dump(topo, fh, indent=2)
    return {"id": tid, "name": name}


def load(tid: str) -> dict:
    with open(path(tid), encoding="utf-8") as fh:
        return json.load(fh)


def ids() -> list[str]:
    """Every stored topology id (no order guarantee)."""
    if not os.path.isdir(STORE):
        return []
    return [f[:-5] for f in os.listdir(STORE) if f.endswith(".json")]


def delete(tid: str) -> None:
    """Remove a topology; a bad/absent id is a no-op."""
    try:
        fp = path(tid)
    except ValueError:
        return
    if os.path.isfile(fp):
        os.remove(fp)


if __name__ == "__main__":  # ponytail: the barrier is the whole reason to test in isolation
    for safe in ("network", "../etc/passwd", "a/b", "..", "/abs/x"):   # basename-reduced -> inside STORE
        assert os.path.dirname(path(safe)) == os.path.realpath(STORE), safe
    for reject in ("", "a b", "a;b", "a$b"):                            # invalid charset -> rejected
        try:
            path(reject); raise AssertionError(f"accepted {reject!r}")
        except ValueError:
            pass
    assert stable_slug("PVE Host!") == "pve-host"
    assert slug("x").startswith("x-") and slug("x")[2:].isdigit()
    print("store self-check ok")
