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
  sudo apt-get update -qq
  sudo apt-get install -y -qq git python3 pciutils util-linux dmidecode
else
  echo "warn: no apt-get — ensure git, python3, pciutils, util-linux, dmidecode are installed"
fi

if [ -d "$DIR/.git" ]; then
  git -C "$DIR" pull --ff-only
else
  git clone "$REPO" "$DIR"
fi

chmod +x "$DIR/report.sh"
exec "$DIR/report.sh" "$SERVER"
