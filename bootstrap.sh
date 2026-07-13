#!/usr/bin/env bash
# One-shot provision for a FRESH Debian/Ubuntu reporting machine: install deps,
# clone the repo, and install a background systemd service that reports to the
# dashboard server (no terminal left occupied; survives logout + reboot).
#
#   curl -fsSL https://raw.githubusercontent.com/FugginOld/topologygenerator/main/bootstrap.sh | bash
#   # or, to point at a different server / dir:
#   TOPO_SERVER=http://192.168.1.225:8770 TOPO_DIR=~/topo bash bootstrap.sh
#   # one-time snapshot (laptop/PC), no persistent service:
#   TOPO_SERVER=http://192.168.1.225:8770 TOPO_ONCE=1 bash bootstrap.sh
set -euo pipefail

REPO="${TOPO_REPO:-https://github.com/FugginOld/topologygenerator.git}"
DIR="${TOPO_DIR:-$HOME/topologygenerator}"
SERVER="${TOPO_SERVER:-http://192.168.1.225:8770}"

# Privilege: already root -> no sudo needed; otherwise use sudo if present.
# CAN_ROOT is true when we can write system files (install pkgs + the unit).
RUN_USER="$(id -un)"
SUDO=""
if [ "$(id -u)" -ne 0 ] && command -v sudo >/dev/null 2>&1; then SUDO="sudo"; fi
if [ "$(id -u)" -eq 0 ] || [ -n "$SUDO" ]; then CAN_ROOT=true; else CAN_ROOT=false; fi

# Only touch the package manager for tools that are actually MISSING *and*
# relevant to this machine. A re-run on a provisioned host — or one with a wedged
# dpkg but the tools already present (e.g. a Pi) — then never invokes apt at all.
have() { command -v "$1" >/dev/null 2>&1; }
need=""
have git     || need="$need git"
have python3 || need="$need python3"
have lsblk   || need="$need util-linux"                        # storage enumeration
[ -n "$(ls -A /sys/bus/pci/devices 2>/dev/null)" ] && ! have lspci && need="$need pciutils"  # PCI names; skip on a Pi
case "$(uname -m)" in x86_64|i?86) have dmidecode || need="$need dmidecode";; esac  # SMBIOS is x86-only

if [ -n "$need" ]; then
  if command -v apt-get >/dev/null 2>&1; then
    echo "installing:$need"
    $SUDO apt-get update -qq && $SUDO apt-get install -y -qq $need \
      || echo "warn: could not install:$need — fix dpkg, or install manually; devices needing them may be missing"
  else
    echo "warn: missing and no apt-get:$need — install these manually"
  fi
fi

if [ -d "$DIR/.git" ]; then
  git -C "$DIR" pull --ff-only
else
  git clone "$REPO" "$DIR"
fi

chmod +x "$DIR/report.sh"

# TOPO_ONCE: one-time snapshot (laptops / PCs) — push this machine's topology
# once and exit. No service, no lingering process.
if [ -n "${TOPO_ONCE:-}" ]; then
  echo "one-time snapshot -> pushing this machine's topology to $SERVER…"
  exec python3 "$DIR/topology_agent.py" --server "$SERVER"
fi

# Otherwise install a systemd service so reporting runs in the background
# (survives logout + reboot) instead of occupying this terminal. Falls back to
# foreground where systemd/root isn't available.
if command -v systemctl >/dev/null 2>&1 && [ "$CAN_ROOT" = true ]; then
  echo "installing systemd service 'topology-agent' (may prompt for sudo)…"
  $SUDO tee /etc/systemd/system/topology-agent.service >/dev/null <<EOF
[Unit]
Description=Topology reporting agent (pushes hardware map + live telemetry)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$RUN_USER
WorkingDirectory=$DIR
ExecStart=$DIR/report.sh $SERVER
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
  $SUDO systemctl daemon-reload
  $SUDO systemctl enable topology-agent
  $SUDO systemctl restart topology-agent   # restart so a re-run picks up config changes
  echo
  echo "✓ topology-agent is running as a service (starts on boot)."
  echo "  status:  systemctl status topology-agent"
  echo "  logs:    journalctl -u topology-agent -f"
  echo "  stop:    $SUDO systemctl disable --now topology-agent"
else
  echo "no systemd/root — running in the foreground instead (Ctrl-C to stop):"
  exec "$DIR/report.sh" "$SERVER"
fi
