# collectors/ — one read-only source each

Every collector subclasses `Collector` (`base.py`) and returns raw dicts from `collect()`.
See `base.py` for the exact node / link / zone dict shape.

Rules:

- **Stdlib only** — `urllib.request`, not `requests`. Collectors run on minimal hosts.
- **Never raise on a down source.** Wrap the I/O; log and `return []`. A partial map beats no map.
- Optional `zones()` returns VLAN definitions `{vid, name, subnet, policy, cls}` for collectors that
  know them (unifi, opnsense).
- `enabled` gates on `cfg["enabled"]`; config comes from `config.yaml` (gitignored).
- **Register** a new collector in `scanners/make_network_topology.py`'s `COLLECTORS` list — adding the
  file here is not enough.
- `dump_raw()` writes `out/<name>.raw.json` for debugging. An empty file means the collector returned
  `[]` — check credentials / reachability, not the parser.

Secrets: tokens and API keys live only in `config.yaml`. Never hardcode them, and never put real
values in `config.example.yaml`. Config tokens are stored bare (e.g. Proxmox `user@realm!id=secret`);
the collector adds any required prefix.
