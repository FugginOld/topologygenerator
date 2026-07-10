# topologygenerator

Generate system and network topologies of a homelab — auto-discovered from live
sources, normalized into one canonical model, and rendered as an animated HTML
dashboard, a Graphviz SVG, or git-diffable Mermaid.

The repo is the **tooling**. Your actual topology (IPs, MACs, hostnames, VLAN
policy) is a *build artifact* and is gitignored — see [Security](#security).

## How it works

```
sources ──▶ collectors ──▶ topology.json ──▶ renderers
(live)      (read-only)     (canonical)       (html / svg / mermaid)
```

Every collector is read-only and emits raw dicts. `core/normalize.py` merges
them into one `Topology` (deduped by MAC, then reconciled by IP and hostname),
`core/enrich.py` adds vendor/kind, and renderers consume only the canonical
model — so you can add outputs without touching collection.

## Quick start

```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml     # edit — this file is gitignored
python make_topology.py --config config.yaml
python renderers/html/serve.py         # http://localhost:8770
```

With nothing configured but `arpscan` (the default), you already get a live host
map. Enable more collectors in `config.yaml` as you go.

## Collectors

| Collector    | Source                          | Adds                                    | Needs                |
|--------------|---------------------------------|-----------------------------------------|----------------------|
| `arpscan`    | `arp-scan` / `nmap -sn`         | live hosts, MAC, vendor                 | arp-scan or nmap     |
| `opnsense`   | OPNsense REST API               | **VLAN zones**, DHCP names, ARP         | API key/secret       |
| `unifi_snmp` | SNMP LLDP + FDB                 | **physical switch-port edges**, uplinks | net-snmp, SNMP on sw |
| `tailscale`  | `tailscale status --json`       | overlay mesh (tagged `ts`)              | tailscale            |
| `docker`     | `docker ps` over SSH            | containers nested under hosts           | key-based SSH        |
| `dns`        | Pi-hole / hosts file            | friendly names                          | —                    |

MAC is the primary join key; nodes are then reconciled by IP and hostname so a
host seen by three collectors collapses into one.

## Renderers

- **`renderers/html/`** — animated dashboard (VLAN zones, firewall hub, Tailscale
  overlay toggle, click-to-isolate). Reads `topology.json`; refreshes every 30s.
- **`renderers/static_svg.py`** — Graphviz `dot` → SVG/PNG for README/wiki.
- **`renderers/mermaid.py`** — `topology.mmd`, renders on GitHub, diffs cleanly.

## Automation

Runs on a homelab host, not GitHub Actions (Actions can't reach your LAN). See
`systemd/` for a timer that regenerates the map every 10 minutes. If you want
history/diffing, snapshot each `topology.json` into SQLite and diff runs.

## Security

Your generated topology is a map of your network. **Keep it out of git.**
`.gitignore` already excludes `config.yaml`, `out/`, `*.raw.json`, and
`topology.json`. Recommended: keep this repo **private**. If public, only ever
commit the tooling and `config.example.yaml` (dummy values). One accidental
`git add -A` of a build artifact leaks the whole layout.

## Layout

```
collectors/   read-only source adapters (one file per source)
core/         schema.py · normalize.py · enrich.py · oui.csv
renderers/    html/ · static_svg.py · mermaid.py
systemd/      timer + service units
tests/        fixtures + end-to-end pipeline test
make_topology.py   orchestrator
```

## Tests

```bash
python tests/test_pipeline.py      # no live network; uses fixtures
```

## License

MIT
