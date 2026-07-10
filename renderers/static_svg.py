"""Render a Topology to a static SVG/PNG via Graphviz `dot`.

Good for embedding in README/wiki. Requires graphviz (`apt install graphviz`).
Falls back to writing just the .dot file if `dot` isn't on PATH.
"""
from __future__ import annotations

import logging
import shutil
import subprocess

from core.schema import Topology

log = logging.getLogger("renderer.svg")

_CLS_COLOR = {
    "mgmt": "#63d0ff", "lan": "#46e0a4", "srv": "#ffc451",
    "adsb": "#ff9d5c", "iot": "#ff5f6d", "guest": "#8b7bff",
    "dmz": "#ff9d5c", "unknown": "#8899aa",
}


def _q(s: str) -> str:
    return '"' + (s or "").replace('"', "'") + '"'


def to_dot(topo: Topology) -> str:
    out = [
        "digraph homelab {",
        '  bgcolor="#04070f"; rankdir=TB; splines=true;',
        '  node [style=filled fontname="monospace" fontsize=10 '
        'fontcolor="#cdeaf7" color="#173553" fillcolor="#0a1d33"];',
        '  edge [color="#2d5f7e"];',
        '  WAN [shape=ellipse fillcolor="#0a1d33" label="WAN"];',
        '  FW [shape=box label="firewall\\nL3 core" color="#63d0ff"];',
        "  WAN -> FW;",
    ]
    zone_of = {z.vid: z for z in topo.zones}
    by_vlan: dict[int | None, list] = {}
    for n in topo.nodes:
        by_vlan.setdefault(n.vlan, []).append(n)

    for vid, nodes in by_vlan.items():
        z = zone_of.get(vid)
        color = _CLS_COLOR.get(z.cls if z else "unknown", "#8899aa")
        title = f"VLAN {vid} {z.name}" if z else "unassigned"
        out.append(f"  subgraph cluster_{vid or 'na'} {{")
        out.append(f'    label={_q(title)}; fontcolor="{color}"; color="{color}"; style=dashed;')
        for n in nodes:
            fc = color if n.online else "#33404d"
            out.append(f"    {_q(n.id)} [label={_q(n.name)} color=\"{fc}\"];")
        out.append("  }")
        if z:
            out.append(f"  FW -> {_q(nodes[0].id)} [style=invis];")

    for l in topo.links:
        style = "dashed" if l.kind == "overlay" else "solid"
        out.append(f"  {_q(l.src)} -> {_q(l.dst)} [style={style}];")
    out.append("}")
    return "\n".join(out)


def write(topo: Topology, dot_path: str, svg_path: str | None = None) -> None:
    dot = to_dot(topo)
    with open(dot_path, "w") as fh:
        fh.write(dot)
    if svg_path:
        if not shutil.which("dot"):
            log.warning("graphviz `dot` not found; wrote %s only", dot_path)
            return
        try:
            subprocess.run(["dot", "-Tsvg", dot_path, "-o", svg_path],
                           check=False, timeout=30)
        except (subprocess.TimeoutExpired, OSError) as e:
            log.warning("dot render failed: %s", e)
