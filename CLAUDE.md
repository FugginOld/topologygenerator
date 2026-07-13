# CLAUDE.md

Homelab **network + hardware topology generator**. Scanners and collectors gather a
machine's or a network's real topology; a pipeline normalizes + enriches it; renderers
draw it (Mermaid, static SVG, and a live web dashboard). Reporting agents push each
host's map + live telemetry to the dashboard server.

## Pipeline (the spine)

```
collectors/*.py + scanners/*.py        gather raw node/link/zone dicts
        -> core/normalize.py           dedup by MAC, reconcile by IP/hostname, VLAN by subnet
        -> core/enrich.py              vendor (core/oui.csv), device kind, online/aging
        -> renderers/card.py           dashboard view-model (Card)
        -> renderers/{mermaid,static_svg,html}
```

Data degrades gracefully: a dead source returns `[]`, never raises. A partial map beats no map.

## Layout

- `scanners/` — top-level generators: `make_pc_topology.py` (Windows PC), `make_linux_topology.py`
  (Linux host), `make_network_topology.py` (whole network; drives the collectors).
- `collectors/` — one read-only source each (unifi, proxmox, docker, pingsweep, …), subclassing `Collector`.
- `core/` — the pipeline: `normalize.py`, `enrich.py`, `schema.py`, `detect.py` (credential-free
  gateway fingerprint), `local_telemetry.py`, `oui.csv`.
- `renderers/` — `card.py` (view-model), `network_cards.py` (topology→cards adapter),
  `mermaid.py`, `static_svg.py`, `html/` (the dashboard).
- `agent/` — reporting agent (`topology_agent.py`) + installers (`report.sh`, `report.ps1`).
- `bootstrap.sh` / `bootstrap.ps1` — one-shot provision for a fresh reporting host.
- `install.sh` / `uninstall.sh` — dashboard-server systemd install.
- `tests/` — assert-based, no framework.

## Commands

Install: `pip install -r requirements.txt`

- Dashboard server: `python renderers/html/topology_server.py [--port 8770]`
- Map this machine: `python scanners/make_pc_topology.py` (Windows) · `python scanners/make_linux_topology.py` (Linux)
- Map the network: `python scanners/make_network_topology.py`
- Report to a dashboard: `agent/report.sh http://<dashboard-ip>:8770` (or `.\agent\report.ps1 -Server …`)

Tests — exactly what CI runs, all offline:
```
python -m compileall -q .
python tests/test_pipeline.py
python tests/test_cards.py
python renderers/html/store.py               # store path-injection barrier selftest
python scanners/make_linux_topology.py --selftest
```
Also checked in CI: `bash -n *.sh`; `.ps1` must be ASCII; dashboard JS via `node --check` on the
extracted `<script>` block.

## Hard rules

1. **Never commit `config.yaml`** — it is gitignored and holds secrets (API keys, tokens). Keep real
   IPs / users / hostnames out of the tracked `config.example.yaml`; use generic placeholders.
2. **`scanners/make_linux_topology.py` must import nothing from this repo.** The dashboard's remote
   scan pipes it alone over SSH, so it has to be fully self-contained (stdlib only). No
   `from core / renderers / collectors / scanners …`.
3. **Collectors are stdlib-only** (`urllib`, not `requests`), subclass `Collector`, return `list[dict]`
   from `collect()`, and never raise on a dead source (return `[]`). Register a new one in
   `scanners/make_network_topology.py`.
4. **`.ps1` files must be ASCII** — Windows PowerShell 5.1 reads BOM-less files as ANSI, so a stray
   non-ASCII byte corrupts them. CI enforces this.
5. **Dashboard `index.html` is served from disk per request** — HTML/CSS/JS edits need only a browser
   hard-refresh, no restart. Only Python changes need `systemctl restart topology-server`.
6. The dashboard's SVG builder (`el()` in `index.html`) sets `textContent`, never `innerHTML`, for
   device-supplied strings — labels come from scanned hosts and are untrusted. Keep it that way.

## Conventions

- Python: stdlib-first, type hints, `from __future__ import annotations`. `requirements.txt` is
  intentionally tiny — don't add a dependency for what a few lines of stdlib can do.
- Match the terseness and comment density of the file you're editing.
- Commit only when asked. This repo pushes straight to `main`; end commit messages with the
  `Co-Authored-By` trailer.
- Domain vocabulary lives in `CONTEXT.md` (Topology, Collector, Card, Store) — use those names.
