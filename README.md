# Topographer

<p align="center">
  <img src="docs/branding/topographer-banner.png" alt="Topographer" width="820">
</p>

[![CI](https://github.com/FugginOld/topographer/actions/workflows/ci.yml/badge.svg)](https://github.com/FugginOld/topographer/actions/workflows/ci.yml)

I never could find a dashboard service I liked. So...using AI, I prompted what I wanted to see. I always wanted to build a network topology but I figured there had to be a way to do it automatically instead of manually running all the commands to compile the network information then piece it together. Same thing with every machine on the network that had a topology to generate as well as a dashboard for that machine. I like it..it works for me. I hope you enjoy it for what it is. - FugginOld

Two topology tools in one repo:

1. **Network topology** — auto-discover a homelab network from live sources,
   normalize into one canonical model, render as an animated HTML dashboard,
   Graphviz SVG, or git-diffable Mermaid. *(the original pipeline, below)*
2. **Hardware topology + fleet dashboard** — scan each machine's real hardware
   fabric (CPU, RAM, PCIe lanes, NVMe, NICs with link state, USB, displays) and
   watch every machine on your network from **one live dashboard**, with per-host
   CPU/net/disk telemetry. *See **[HOWTO.md](HOWTO.md)** for the full setup.*

The repo is the **tooling**. Your actual topology (IPs, MACs, hostnames, VLAN
policy) is a *build artifact* and is gitignored — see [Security](#security).

## Hardware topology + fleet dashboard

Map the real hardware of every machine on your network and watch them live:

```text
   Windows PC ─┐  ./agent/report.sh  (or agent\report.ps1)
   Linux box  ─┼──►  topo_server.py on one host  ──►  live dashboard, one card per machine
   Proxmox    ─┘     (POST /api/ingest + telemetry)
```

- One **server** runs `python renderers/html/topo_server.py`; open `http://HOST:8770`.
- Each machine runs an **agent** that scans its own hardware and pushes its
  topology and live telemetry (`agent/report.sh` on Linux, `agent/report.ps1` on Windows, or
  the `bootstrap.sh` one-liner for a fresh Debian box).
- Scanners: `scanners/make_pc_topo.py` (Windows, PnP/CIM) and `scanners/make_linux_topo.py`
  (Linux, sysfs/proc). Live metrics: `core/local_telemetry.py` (real CPU temp on Linux).

Full step-by-step — server firewall, each reporting machine, persistence,
naming, tokens, troubleshooting — is in **[HOWTO.md](HOWTO.md)**.

## How it works

```text
sources ──▶ collectors ──▶ topo.json ──▶ renderers
(live)      (read-only)     (canonical)       (html / svg / mermaid)
```

Every collector is read-only and emits raw dicts. `core/normalize.py` merges
them into one `Topology` (deduped by MAC, then reconciled by IP and hostname),
`core/enrich.py` adds vendor/kind, and renderers consume only the canonical
model — so you can add outputs without touching collection.

## Quick start

```bash
pip install -r requirements.txt            # only PyYAML is required
python renderers/html/topo_server.py   # http://localhost:8770
```

On a Linux host, `./install.sh` sets the dashboard up as a systemd service
(starts on boot, prints its own URL); `./uninstall.sh` removes it. See
[HOWTO.md](HOWTO.md).

Open the dashboard and click **SCAN NETWORK** — with no config at all it
ping-sweeps your subnet and, if it doesn't recognise a gateway collector,
**fingerprints your router** and tells you which one to enable (e.g. *"gateway
192.168.1.1 looks like UNIFI — add a `unifi` API key"*). Then:

```bash
cp config.example.yaml config.yaml         # edit — this file is gitignored
# enable unifi / proxmox / etc. with their API keys, then re-scan
```

Prefer the CLI? `python scanners/make_network_topo.py --config config.yaml` writes
`out/topo.json` + `.svg` + `.mmd` directly.

**Adding a machine to the fleet:** right-click any host in the network map →
*Generate machine topology*. If SSH remote-scan is configured it scans over SSH;
otherwise it hands you the one-line `bootstrap.sh` command to run on that host
(persistent service, or `TOPO_ONCE=1` for a one-off snapshot).

## Collectors

| Collector    | Source                          | Adds                                          | Needs                       |
|--------------|---------------------------------|-----------------------------------------------|-----------------------------|
| `unifi`      | UniFi controller API (UCG/UDM)  | **VLAN zones**, clients, gateway + WAN, uplinks | API key *(stdlib, no deps)* |
| `proxmox`    | Proxmox VE API                  | **VMs + LXC** (incl. NAT'd) nested under host  | API token *(PVEAuditor)*    |
| `pingsweep`  | OS `ping` + ARP cache           | live hosts, MAC, vendor — **zero install**     | — *(Windows-friendly)*      |
| `arpscan`    | `arp-scan` / `nmap -sn`         | live hosts, MAC, vendor                        | arp-scan or nmap (Linux)    |
| `opnsense`   | OPNsense REST API               | VLAN zones, DHCP names, ARP                    | API key/secret              |
| `unifi_snmp` | SNMP LLDP + FDB                 | **physical switch-port edges**, uplinks        | net-snmp, SNMP on switch    |
| `docker`     | `docker ps` over SSH            | containers nested under hosts                  | key-based SSH               |
| `tailscale`  | `tailscale status --json`       | overlay mesh (tagged `ts`)                     | tailscale                   |
| `dns`        | Pi-hole / hosts file            | friendly names                                 | —                           |

MAC is the primary join key; nodes are then reconciled by IP and hostname so a
host seen by three collectors collapses into one. `unifi`/`proxmox`/`pingsweep`
are **stdlib-only** (no `requests`); the gateway/API collectors auto-degrade to
`[]` when their source is absent, so enabling several is safe.

## Renderers

- **`renderers/html/`** — animated dashboard (VLAN zones, firewall hub, Tailscale
  overlay toggle, click-to-isolate). Reads `topo.json`; refreshes every 30s.
- **`renderers/static_svg.py`** — Graphviz `dot` → SVG/PNG for README/wiki.
- **`renderers/mermaid.py`** — `topo.mmd`, renders on GitHub, diffs cleanly.

## Automation

Runs on a homelab host, not GitHub Actions (Actions can't reach your LAN). See
`systemd/` for a timer that regenerates the map every 10 minutes. If you want
history/diffing, snapshot each `topo.json` into SQLite and diff runs.

## Security

Your generated topology is a map of your network. **Keep it out of git.**
`.gitignore` already excludes `config.yaml`, `out/`, `*.raw.json`, and
`topo.json`. Recommended: keep this repo **private**. If public, only ever
commit the tooling and `config.example.yaml` (dummy values). One accidental
`git add -A` of a build artifact leaks the whole layout.

## Layout

```text
collectors/   read-only source adapters (one file per source)
core/         schema · normalize · enrich · detect (gateway fingerprint) · oui.csv
renderers/    html/ (dashboard + topo_server.py) · static_svg.py · mermaid.py
systemd/      units: topo-server (dashboard) · topo-agent · timer
tests/        fixtures + end-to-end pipeline test
scanners/make_network_topo.py   network topology orchestrator (collectors → renderers)

# hardware topology + fleet dashboard (see HOWTO.md)
scanners/make_pc_topo.py      Windows hardware scan (PnP/CIM)
scanners/make_linux_topo.py   Linux hardware scan (sysfs/proc/USB/thermal)
core/local_telemetry.py       shared live CPU/net/disk/temp sampler
agent/topo_agent.py        push topology + telemetry to the server
install.sh · uninstall.sh  set up / remove the dashboard as a Linux service
agent/report.sh · agent/report.ps1   run the agent (self-updating)
server/server.ps1        start the dashboard on Windows (firewall + topo_server.py)
bootstrap.sh             agent one-liner install (Linux/Unraid): systemd / go-script /
                         TOPO_ONCE snapshot — adapts to the host, git-free
bootstrap.ps1            agent one-liner install (Windows): scheduled task, zip-fetch
```

## Tests

```bash
python tests/test_pipeline.py      # no live network; uses fixtures
```

## License

MIT
