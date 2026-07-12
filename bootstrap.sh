#!/usr/bin/env bash
# One-shot provision for a FRESH Debian/Ubuntu reporting machine: install deps,
# clone the repo, and start reporting to the dashboard server.
#
#   curl -fsSL https://raw.githubusercontent.com/FugginOld/topologygenerator/main/bootstrap.sh | bash
#   # or, to point at a different server / dir:
#   TOPO_SERVER=http://192.168.1.225:8770 TOPO_DIR=~/topo bash bootstrap.sh
set -euo pipefail

REPO="${TOPO_REPO:-https://github.com/FugginOld/topologygenerator.git}"
DIR="${TOPO_DIR:-$HOME/topologygenerator}"
SERVER="${TOPO_SERVER:-http://192.168.1.225:8770}"

if command -v apt-get >/dev/null 2>&1; then
  apt-get update -qq \
    && apt-get install -y -qq git python3 pciutils util-linux dmidecode \
    || echo "warn: dependency install failed — run as root, or install: git python3 pciutils util-linux dmidecode"
else
  # ponytail: no apt-get (e.g. Unraid/Slackware) — check what's actually present instead of a blanket warning
  missing=""
  for bin in git python3 lspci lsblk dmidecode; do
    command -v "$bin" >/dev/null 2>&1 || missing="$missing $bin"
  done
  [ -n "$missing" ] && echo "warn: no apt-get and missing:$missing — install these manually"
fi

if [ -d "$DIR/.git" ]; then
  git -C "$DIR" pull --ff-only
else
  git clone "$REPO" "$DIR"
fi

chmod +x "$DIR/report.sh"
exec "$DIR/report.sh" "$SERVER"
