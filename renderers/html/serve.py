#!/usr/bin/env python3
"""Serve the HTML dashboard + out/topology.json on http://localhost:8770.

Browsers block fetch() over file://, so the dashboard needs a real HTTP origin.
This serves the renderers/html/ folder and symlinks/copies topology.json in.

    python renderers/html/serve.py [--port 8770] [--topo out/topology.json]
"""
from __future__ import annotations

import argparse
import http.server
import os
import shutil
import socketserver

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8770)
    ap.add_argument("--topo", default=os.path.join(ROOT, "out", "topology.json"))
    args = ap.parse_args()

    # copy latest topology.json next to index.html so fetch() finds it
    if os.path.exists(args.topo):
        shutil.copy(args.topo, os.path.join(HERE, "topology.json"))
    else:
        print(f"! {args.topo} not found -- run make_topology.py first")

    os.chdir(HERE)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", args.port), handler) as httpd:
        print(f"serving dashboard on http://localhost:{args.port}  (Ctrl-C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
