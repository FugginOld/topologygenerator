# Run on a WINDOWS reporting machine. Pushes this host's topology + live
# telemetry to the dashboard server. Self-updates from git on each start.
#
#   .\report.ps1 -Server http://host:8770          # server (name = hostname)
#   .\report.ps1 -Server http://host:8770 -Name node-a
#   $env:TOPO_SERVER="http://host:8770"; .\report.ps1   # server via env
#   $env:TOPO_TOKEN="secret"; .\report.ps1         # if the server sets a shared token
#
# The server URL is required (-Server or $env:TOPO_SERVER) — ./install.sh prints
# it. The dashboard keeps ONE card per name (defaults to this host's hostname), so
# give machines that share a hostname distinct names or one overwrites the other.
#
# Requires Python 3 on PATH. If PowerShell blocks the script, run once:
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
param(
  [string]$Server = $env:TOPO_SERVER,
  [string]$Name = $env:TOPO_NAME
)
if (-not $Server) { Write-Error "set -Server http://<dashboard-ip>:8770 (or `$env:TOPO_SERVER)"; exit 1 }
Set-Location $PSScriptRoot

git pull --ff-only 2>$null

$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if (-not $py) { Write-Error "Python 3 not found on PATH - install it and re-run."; exit 1 }

$argv = @("topology_agent.py", "--server", $Server, "--report")
$suffix = ""
if ($Name) { $argv += @("--name", $Name); $suffix = " as '$Name'" }
Write-Host "reporting to $Server$suffix  (Ctrl-C to stop)"
& $py.Source @argv
