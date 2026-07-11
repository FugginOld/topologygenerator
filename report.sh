#!/usr/bin/env bash
# Run on a LINUX reporting machine. Keeps this host's topology + live telemetry
# flowing to the dashboard server. Self-updates from git on each start.
#
#   ./report.sh                          # -> default server below
#   ./report.sh http://host:8770         # -> override server
#   TOPO_TOKEN=secret ./report.sh        # -> if the server sets a shared token
#
# Uses only Python 3 stdlib; the Linux collector needs lspci/lsblk (+ dmidecode
# as root for per-DIMM detail). Install: apt-get install pciutils util-linux dmidecode
set -euo pipefail

SERVER="${1:-${TOPO_SERVER:-http://192.168.1.225:8770}}"
cd "$(dirname "$(readlink -f "$0")")"

git pull --ff-only >/dev/null 2>&1 || echo "warn: git pull skipped (offline or local changes)"
for t in lspci lsblk; do
  command -v "$t" >/dev/null 2>&1 || echo "warn: '$t' not found — some devices will be missing (apt-get install pciutils util-linux)"
done

echo "reporting to $SERVER  (Ctrl-C to stop)"
exec python3 agent.py --server "$SERVER" --report
