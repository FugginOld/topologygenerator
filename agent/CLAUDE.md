# agent/ — reporting agent

`topology_agent.py` runs the right scanner for the host OS and pushes the map + live telemetry to the
dashboard. `report.sh` (Linux) and `report.ps1` (Windows) wrap it, each with `-Install` / `-Uninstall`
persistence (systemd unit / scheduled task, with no-admin fallbacks: Unraid boot `go` hook, Windows
Startup-folder `.vbs`).

- **`TOPO_SERVER` (or the first positional arg) is required** — there is no hardcoded dashboard IP.
  The server auto-detects its own IP for locally generated cards.
- A bootstrap agent install is a **minimal file set** (`agent/` + `scanners/make_linux_topology.py` +
  `core/local_telemetry.py`), not the whole repo. `report.sh` self-updates via git only when run from
  a full checkout; a minimal install updates by re-running bootstrap.
- The dashboard keeps **one card per name** (defaults to hostname) — distinct hosts sharing a hostname
  need distinct `--name`, or they overwrite each other.
- `.ps1` must be ASCII (PS 5.1). Bind PowerShell named params with a **hashtable splat**, not an array
  (an array splat binds positionally).
