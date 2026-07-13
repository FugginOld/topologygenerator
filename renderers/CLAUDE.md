# renderers/ — topology -> visuals

- `card.py` — **the dashboard view-model** (`Card`). One place defines the node contract
  `{id, parent, label, sub, cls, kind, meta, grp, cap, up, fill, link, iface}`; `to_dict()` drops
  `None`. Both `make_pc_topology.py` and the server build through this.
- `network_cards.py` — `from_topology(topo)` adapts a normalized network topology into cards.
- `mermaid.py`, `static_svg.py` — static exports.
- `html/` — the live dashboard (see its own `CLAUDE.md`).

`Card` is the seam every renderer and scanner passes through: change the node contract *here*, not in
the individual scanners. `make_linux_topology.py` is the one exception — it stays self-contained and
mirrors the shape by hand. Covered by `tests/test_cards.py`.
