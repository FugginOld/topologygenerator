# tests/ — assert-based, no framework

Plain scripts run directly: `python tests/<file>.py` (exit 0 = pass). No pytest, no framework, no
fixtures beyond `tests/fixtures/`. New non-trivial logic gets ONE runnable check — an `assert`-based
selftest or a small `test_*.py` — matching the existing style. Trivial one-liners need no test.

- `test_pipeline.py` — collectors → normalize → enrich over fixtures, fully offline.
- `test_cards.py` — the `Card` contract + the `network_cards` adapter.

Some modules ship their own selftest instead of a file here (`make_linux_topology.py --selftest`,
`renderers/html/store.py`). CI runs every one of them — see the root `CLAUDE.md` for the full list.
