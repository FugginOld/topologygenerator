# scanners/ — top-level topology generators

- `make_pc_topology.py` — **Windows only** (PnP / CIM / WMI). Owns the PCI `VENDORS` table and
  builds cards through `renderers.card.Card`.
- `make_linux_topology.py` — Linux host. **Must import nothing from this repo** — the dashboard's
  `topology_server.scan_host` pipes this file *alone* over SSH, so it has to be fully self-contained,
  stdlib only. Reads `lspci` / `lsblk` / sysfs (+ `dmidecode` as root). Has `--selftest` and `--stdout`.
- `make_network_topology.py` — whole network; the `COLLECTORS` list lives here, driven through the
  `core` pipeline.

**Self-containment check** — if this returns anything, remote SSH scans are broken:
```
grep -nE '^(from|import) (core|renderers|collectors|scanners|make_)' scanners/make_linux_topology.py
```

`make_linux` cannot import `Card` (it must stay self-contained), so it emits the same card dict shape
by hand — keep the two generators in sync on the *schema*, never by importing. Run
`python scanners/make_linux_topology.py --selftest` after editing it.
