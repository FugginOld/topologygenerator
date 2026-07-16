"""Engine-driven widget definitions — data, not code.

Each entry is a declarative spec the generic engine (engine.py) executes: auth
style + endpoints + field mappings, mirrored from Homepage's widget.js `api`
template + `mappings`. Adding a widget here = it becomes installable, no fetcher.
Only api-key / basic / bearer / token services fit; cookie-login ones (qBittorrent
etc.) still need a custom fetcher in fetchers.py.

Verify a new one against a live instance before trusting the field paths (the
endpoints come from the source; the JSON paths from the service's API).
"""
from __future__ import annotations

DEFS = [
    {
        "id": "adguard", "label": "AdGuard Home", "category": "Network", "icon": "adguard-home",
        "desc": "DNS queries, blocked, protection status.",
        "auth": "basic",   # username/password optional
        "calls": {"stats": "/control/stats", "status": "/control/status"},
        "show": [
            {"key": "queries", "call": "stats", "path": "num_dns_queries"},
            {"key": "blocked", "call": "stats", "path": "num_blocked_filtering"},
            {"key": "block_pct", "call": "stats", "op": "ratio",
             "num": "num_blocked_filtering", "den": "num_dns_queries", "fmt": "pct"},
            {"key": "protection", "call": "status", "path": "protection_enabled"},
        ],
    },
    {
        "id": "gotify", "label": "Gotify", "category": "Comms & Requests", "icon": "gotify",
        "desc": "Registered applications and clients.",
        "auth": "apikey-header", "header": "X-Gotify-Key",
        "calls": {"apps": "/application", "clients": "/client"},
        "show": [
            {"key": "apps", "call": "apps", "op": "len"},
            {"key": "clients", "call": "clients", "op": "len"},
        ],
    },
    {
        "id": "portainer", "label": "Portainer", "category": "Infrastructure", "icon": "portainer",
        "desc": "Containers total + running (per environment).",
        "auth": "apikey-header", "header": "X-API-Key",
        "params": [{"name": "env", "label": "Environment ID", "required": True}],
        "calls": {"containers": "/api/endpoints/{env}/docker/containers/json?all=1"},
        "show": [
            {"key": "containers", "call": "containers", "op": "len"},
            {"key": "running", "call": "containers", "op": "count_where:State=running"},
        ],
    },
    {
        "id": "jellyfin", "label": "Jellyfin", "category": "Media", "icon": "jellyfin",
        "desc": "Library counts + active sessions.",
        "auth": "apikey-query", "param": "api_key",
        "calls": {"counts": "/emby/Items/Counts", "sessions": "/emby/Sessions"},
        "show": [
            {"key": "movies", "call": "counts", "path": "MovieCount"},
            {"key": "series", "call": "counts", "path": "SeriesCount"},
            {"key": "episodes", "call": "counts", "path": "EpisodeCount"},
            {"key": "sessions", "call": "sessions", "op": "len"},
        ],
    },
    {
        "id": "emby", "label": "Emby", "category": "Media", "icon": "emby",
        "desc": "Library counts + active sessions.",
        "auth": "apikey-query", "param": "api_key",
        "calls": {"counts": "/emby/Items/Counts", "sessions": "/emby/Sessions"},
        "show": [
            {"key": "movies", "call": "counts", "path": "MovieCount"},
            {"key": "series", "call": "counts", "path": "SeriesCount"},
            {"key": "episodes", "call": "counts", "path": "EpisodeCount"},
            {"key": "sessions", "call": "sessions", "op": "len"},
        ],
    },
    {
        "id": "paperlessngx", "label": "Paperless-ngx", "category": "Files & Docs", "icon": "paperless-ngx",
        "desc": "Document totals + inbox.",
        "auth": "token",
        "calls": {"stats": "/api/statistics/"},
        "show": [
            {"key": "documents", "call": "stats", "path": "documents_total"},
            {"key": "inbox", "call": "stats", "path": "documents_inbox"},
        ],
    },
    # ── media stack (Servarr + friends): url + API key, all pure engine shape.
    # beta=False — these are proven (were hand-fetchers), not built-from-spec.
    {
        "id": "sonarr", "label": "Sonarr", "category": "Media", "icon": "sonarr", "beta": False,
        "desc": "Series, queue, missing episodes.",
        "auth": "apikey-header",   # X-Api-Key
        "calls": {"series": "/api/v3/series", "queue": "/api/v3/queue?page=1&pageSize=1",
                  "missing": "/api/v3/wanted/missing?page=1&pageSize=1"},
        "show": [
            {"key": "series", "call": "series", "op": "len"},
            {"key": "queue", "call": "queue", "path": "totalRecords"},
            {"key": "missing", "call": "missing", "path": "totalRecords"},
        ],
    },
    {
        "id": "radarr", "label": "Radarr", "category": "Media", "icon": "radarr", "beta": False,
        "desc": "Movies, queue, missing.",
        "auth": "apikey-header",
        "calls": {"movie": "/api/v3/movie", "queue": "/api/v3/queue?page=1&pageSize=1",
                  "missing": "/api/v3/wanted/missing?page=1&pageSize=1"},
        "show": [
            {"key": "movies", "call": "movie", "op": "len"},
            {"key": "queue", "call": "queue", "path": "totalRecords"},
            {"key": "missing", "call": "missing", "path": "totalRecords"},
        ],
    },
    {
        "id": "bazarr", "label": "Bazarr", "category": "Media", "icon": "bazarr", "beta": False,
        "desc": "Missing subtitles (episodes + movies).",
        "auth": "apikey-header", "header": "X-API-KEY",
        "calls": {"ep": "/api/episodes/wanted?length=1", "mv": "/api/movies/wanted?length=1"},
        "show": [
            {"key": "missing_episodes", "call": "ep", "path": "total"},
            {"key": "missing_movies", "call": "mv", "path": "total"},
        ],
    },
    {
        "id": "seerr", "label": "Seerr / Overseerr", "category": "Media", "icon": "overseerr", "beta": False,
        "desc": "Pending / approved / available requests.",
        "auth": "apikey-header",
        "calls": {"count": "/api/v1/request/count"},
        "show": [
            {"key": "pending", "call": "count", "path": "pending"},
            {"key": "approved", "call": "count", "path": "approved"},
            {"key": "available", "call": "count", "path": "available"},
            {"key": "total", "call": "count", "path": "total"},
        ],
    },
]


if __name__ == "__main__":   # ponytail: every def is engine-shaped + graceful on empty
    from . import engine
    ids = [d["id"] for d in DEFS]
    assert len(ids) == len(set(ids)), "duplicate definition id"
    for d in DEFS:
        assert d.get("calls") and d.get("show"), d["id"]
        assert engine.form_fields(d)[0]["name"] == "url"
        assert engine.fetch(d, {"url": ""}) == {}          # no url -> {}
    print(f"widgets/definitions self-check ok ({len(DEFS)} defs)")
