# core/ — the normalize -> enrich pipeline

- `normalize.py` — merge raw dicts from every source: dedup by MAC, reconcile by IP / hostname,
  assign VLAN by subnet. Deterministic; no network I/O.
- `enrich.py` — vendor lookup via `oui.csv`, device kind, online / aging.
- `schema.py` — the node / link / zone shapes the pipeline speaks.
- `detect.py` — credential-free gateway fingerprint (UniFi / OPNsense / pfSense) that suggests which
  collector to enable.
- `local_telemetry.py` — live CPU / net / disk sampler (stdlib, cross-platform). Imported by both the
  agent and the server, so keep it dependency-free and self-contained.
- `oui.csv` — MAC prefix → vendor. A committed data file; keep it sorted.

Prefer pure functions here — the pipeline is covered offline by `tests/test_pipeline.py` (fixtures).
Run it after any change to `normalize.py` / `enrich.py`.
