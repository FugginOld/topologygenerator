"""Widget Type catalog — the declarative list the store UI browses and the server
validates against. Each Type binds a config-field schema to a fetcher.

field: {name, label, type: text|url|password|number|bool, required?, secret?}
Adding a Type = one CATALOG entry + one fetcher (docs/prd/widget-store.md, Phase 2).
"""
from __future__ import annotations

from . import fetchers

# shared field set for the url + API-key services (Servarr, SABnzbd, Tautulli, …)
_ARR_FIELDS = [
    {"name": "url", "label": "URL (http://host:port)", "type": "url", "required": True},
    {"name": "key", "label": "API key", "type": "password", "required": True, "secret": True},
]

CATALOG = [
    {
        "id": "pihole", "label": "Pi-hole", "category": "Network", "icon": "pihole",
        "desc": "DNS queries + blocked (Pi-hole v5 and v6).",
        "fields": [
            {"name": "url", "label": "Pi-hole URL", "type": "url", "required": True},
            {"name": "token", "label": "App password (v6) / API token (v5)", "type": "password", "secret": True},
        ],
        "fetch": fetchers.pihole,
    },
    {
        "id": "proxmox", "label": "Proxmox VE", "category": "System", "icon": "proxmox",
        "desc": "Node health, running VMs / LXC, CPU + memory.",
        "config_key": "proxmox",     # inherit config.yaml's proxmox block when the form is blank
        "fields": [
            {"name": "url", "label": "PVE URL", "type": "url"},
            {"name": "token", "label": "API token (user@realm!id=secret)", "type": "password", "secret": True},
            {"name": "verify_tls", "label": "Verify TLS", "type": "bool"},
            {"name": "node", "label": "Node (optional)", "type": "text"},
        ],
        "fetch": fetchers.proxmox,
    },
    {
        "id": "unifi", "label": "UniFi", "category": "Network", "icon": "unifi",
        "desc": "WAN status, client count, live throughput.",
        "config_key": "unifi",       # inherit config.yaml's unifi block when the form is blank
        "fields": [
            {"name": "url", "label": "Gateway URL", "type": "url"},
            {"name": "api_key", "label": "API key", "type": "password", "secret": True},
            {"name": "site", "label": "Site", "type": "text"},
            {"name": "verify_tls", "label": "Verify TLS", "type": "bool"},
        ],
        "fetch": fetchers.unifi,
    },
    # ── media stack: url + API key each (Settings -> General/Security in the app) ──
    {
        "id": "sonarr", "label": "Sonarr", "category": "Media", "icon": "sonarr",
        "desc": "Series, queue, missing episodes.", "fields": _ARR_FIELDS, "fetch": fetchers.sonarr,
    },
    {
        "id": "radarr", "label": "Radarr", "category": "Media", "icon": "radarr",
        "desc": "Movies, queue, missing.", "fields": _ARR_FIELDS, "fetch": fetchers.radarr,
    },
    {
        "id": "prowlarr", "label": "Prowlarr", "category": "Downloads", "icon": "prowlarr",
        "desc": "Indexers, grabs, queries.", "fields": _ARR_FIELDS, "fetch": fetchers.prowlarr,
    },
    {
        "id": "bazarr", "label": "Bazarr", "category": "Media", "icon": "bazarr",
        "desc": "Missing subtitles (episodes + movies).", "fields": _ARR_FIELDS, "fetch": fetchers.bazarr,
    },
    {
        "id": "sabnzbd", "label": "SABnzbd", "category": "Downloads", "icon": "sabnzbd",
        "desc": "Queue size, speed, time left.", "fields": _ARR_FIELDS, "fetch": fetchers.sabnzbd,
    },
    {
        "id": "tautulli", "label": "Tautulli", "category": "Media", "icon": "tautulli",
        "desc": "Active Plex streams + bandwidth.", "fields": _ARR_FIELDS, "fetch": fetchers.tautulli,
    },
    {
        "id": "seerr", "label": "Seerr / Overseerr", "category": "Media", "icon": "overseerr",
        "desc": "Pending / approved / available requests.", "fields": _ARR_FIELDS, "fetch": fetchers.seerr,
    },
]

_BY_ID = {t["id"]: t for t in CATALOG}


def get(type_id: str) -> dict | None:
    return _BY_ID.get(type_id)


def field_names(type_id: str) -> list[str]:
    return [f["name"] for f in (_BY_ID.get(type_id) or {}).get("fields", [])]


def secret_fields(type_id: str) -> list[str]:
    return [f["name"] for f in (_BY_ID.get(type_id) or {}).get("fields", []) if f.get("secret")]


def catalog_public() -> list[dict]:
    """Catalog minus the fetch callables — JSON-safe for the browser."""
    return [{k: v for k, v in t.items() if k != "fetch"} for t in CATALOG]


def fetch(type_id: str, config: dict) -> dict:
    """Live stats for one configured widget. Never raises — a bad fetcher must not
    500 the dashboard (defence-in-depth on top of the fetchers' own guards)."""
    t = _BY_ID.get(type_id)
    if not t:
        return {}
    try:
        return t["fetch"](config or {}) or {}
    except Exception:
        return {}


if __name__ == "__main__":   # ponytail: catalog integrity + JSON-safety, offline
    import json as _json
    ids = [t["id"] for t in CATALOG]
    assert len(ids) == len(set(ids)), "duplicate widget id"
    for t in CATALOG:
        assert t["fields"] and callable(t["fetch"]), t["id"]
        assert fetch(t["id"], {}) == {}, f"{t['id']} not graceful on empty config"   # no url -> {}
    assert secret_fields("proxmox") == ["token"]
    assert field_names("unifi")[0] == "url"
    _json.dumps(catalog_public())            # must be serialisable (no callables)
    assert fetch("nope", {}) == {}
    print(f"widgets/registry self-check ok ({len(CATALOG)} types)")
