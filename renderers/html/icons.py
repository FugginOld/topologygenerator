"""Service-icon cache: match a container name/image to a dashboard-icons logo,
fetch it once from the CDN, and cache it to disk so the dashboard serves it
locally (offline-warm). A '.miss' marker negative-caches unknowns.

Lifted out of topo_server.py's Handler — the slug-candidate logic has real
branching that deserves a tested home. The server keeps a one-line route.
"""
from __future__ import annotations

import os
import re

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))

ICON_DIR = os.path.join(_ROOT, "out", "icons")      # gitignored cache
ICON_CDN = "https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons"
_ICON_FMTS = (("svg", "image/svg+xml"), ("png", "image/png"), ("webp", "image/webp"))
_VENDORS = {"binhex", "linuxserver", "lscr", "ghcr", "hotio", "ls"}   # prefixes to drop


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def _icon_slugs(name: str, image: str) -> list:
    """dashboard-icons slug candidates from a container name / image, best first."""
    out = []
    img_base = _slug((image or "").split("/")[-1].split(":")[0])   # jellyfin <- lscr.io/.../jellyfin:latest
    for s in (_slug(name), img_base):
        if not s:
            continue
        parts = s.split("-")
        out.append(s)
        if len(parts) > 1 and parts[0] in _VENDORS:
            out.append("-".join(parts[1:]))          # binhex-plex -> plex
        out.append(parts[-1])                        # last token as a final guess
    seen, uniq = set(), []
    for s in out:
        if s and s not in seen:
            seen.add(s); uniq.append(s)
    return uniq


def icon_bytes(name: str, image: str):
    """(content_type, bytes) for a service icon, cached on disk; None if unavailable.
    A '.miss' marker negative-caches unknowns so we don't re-hit the CDN each render."""
    import urllib.request
    os.makedirs(ICON_DIR, exist_ok=True)
    key = _slug(name) or _slug(image) or "x"
    for ext, ctype in _ICON_FMTS + (("miss", ""),):
        p = os.path.join(ICON_DIR, f"{key}.{ext}")
        if os.path.exists(p):
            if ext == "miss":
                return None
            with open(p, "rb") as fh:
                return ctype, fh.read()
    for slug in _icon_slugs(name, image):
        for ext, ctype in _ICON_FMTS:
            try:
                with urllib.request.urlopen(f"{ICON_CDN}/{ext}/{slug}.{ext}", timeout=4) as r:
                    if r.status == 200:
                        data = r.read()
                        with open(os.path.join(ICON_DIR, f"{key}.{ext}"), "wb") as fh:
                            fh.write(data)
                        return ctype, data
            except Exception:
                continue                             # 404 / offline -> try next candidate
    try:
        open(os.path.join(ICON_DIR, f"{key}.miss"), "wb").close()   # ponytail: permanent until out/icons cleared
    except OSError:
        pass
    return None


if __name__ == "__main__":   # ponytail: slug-candidate logic, offline (no CDN)
    assert _slug("Pi-Hole!") == "pi-hole"
    assert _slug("  ") == ""
    # image tag stripped to its bare name, deduped, ordered best-first
    assert _icon_slugs("Jellyfin", "lscr.io/linuxserver/jellyfin:latest") == ["jellyfin"]
    # vendor prefix dropped as a fallback candidate; original kept first
    assert _icon_slugs("binhex-plex", "") == ["binhex-plex", "plex"]
    assert _icon_slugs("", "") == []
    print("renderers/html/icons slug self-check ok")
