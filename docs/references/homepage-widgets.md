# Homepage widget catalog (cached reference)

Local snapshot of the 155 service widgets Homepage documents, so we can keep
building integrations even if the site is unavailable. Each is a mechanical port:
one fetcher + one registry entry (see `docs/prd/widget-store.md`, `widgets/`).

- Source: https://github.com/gethomepage/homepage/tree/main/docs/widgets/services
- Per-widget API detail: https://gethomepage.dev/widgets/services/<slug>/
- Cached: 2026-07-15 · ✓ = already shipped in our store

| ✓ | Widget | type | config fields | docs |
|---|--------|------|---------------|------|
|  | Adguard Home | `adguard` | url, username, password | [↗](https://gethomepage.dev/widgets/services/adguard-home/) |
|  | APC UPS Monitoring | `apcups` | url | [↗](https://gethomepage.dev/widgets/services/apcups/) |
|  | Arcane | `arcane` | url, env, key, fields | [↗](https://gethomepage.dev/widgets/services/arcane/) |
|  | ArgoCD | `argocd` | url, key | [↗](https://gethomepage.dev/widgets/services/argocd/) |
|  | Atsumeru | `atsumeru` | url, username, password | [↗](https://gethomepage.dev/widgets/services/atsumeru/) |
|  | Audiobookshelf | `audiobookshelf` | url, key | [↗](https://gethomepage.dev/widgets/services/audiobookshelf/) |
|  | Authentik | `authentik` | url, key, version | [↗](https://gethomepage.dev/widgets/services/authentik/) |
|  | Autobrr | `autobrr` | url, key | [↗](https://gethomepage.dev/widgets/services/autobrr/) |
|  | Azure DevOps | `azuredevops` | organization, project, definitionId, branchName, userEmail, repositoryId, key | [↗](https://gethomepage.dev/widgets/services/azuredevops/) |
|  | Backrest | `backrest` | url, username, password | [↗](https://gethomepage.dev/widgets/services/backrest/) |
| ✓ | Bazarr | `bazarr` | url, key | [↗](https://gethomepage.dev/widgets/services/bazarr/) |
|  | Beszel | `beszel` | url, username, password, systemId, version | [↗](https://gethomepage.dev/widgets/services/beszel/) |
|  | Booklore | `booklore` | url, username, password | [↗](https://gethomepage.dev/widgets/services/booklore/) |
|  | Caddy | `caddy` | url | [↗](https://gethomepage.dev/widgets/services/caddy/) |
|  | Calendar | `calendar` | firstDayInWeek, view, maxEvents, showTime, timezone, integrations, service_group, service_name, color, baseUrl, params, unmonitored, url, name, showName | [↗](https://gethomepage.dev/widgets/services/calendar/) |
|  | Calibre-web | `calibreweb` | url, username, password | [↗](https://gethomepage.dev/widgets/services/calibre-web/) |
|  | Changedetection.io | `changedetectionio` | url, key | [↗](https://gethomepage.dev/widgets/services/changedetectionio/) |
|  | Channels DVR Server | `channelsdvrserver` | url | [↗](https://gethomepage.dev/widgets/services/channelsdvrserver/) |
|  | Checkmk | `checkmk` | url, site, username, password | [↗](https://gethomepage.dev/widgets/services/checkmk/) |
|  | Cloudflare Tunnels | `cloudflared` | accountid, tunnelid, key | [↗](https://gethomepage.dev/widgets/services/cloudflared/) |
|  | Coin Market Cap | `coinmarketcap` | currency, symbols, key, defaultinterval | [↗](https://gethomepage.dev/widgets/services/coin-market-cap/) |
|  | Crowdsec | `crowdsec` | url, username, password | [↗](https://gethomepage.dev/widgets/services/crowdsec/) |
|  | Custom API | `customapi` | url, refreshInterval, username, password, method, headers, requestBody, display, mappings, label, format, locale, dateStyle, timeStyle, style, numeric, additionalField, field, color | [↗](https://gethomepage.dev/widgets/services/customapi/) |
|  | Deluge | `deluge` | url, password, enableLeechProgress | [↗](https://gethomepage.dev/widgets/services/deluge/) |
|  | DeveLanCacheUI | `develancacheui` | url | [↗](https://gethomepage.dev/widgets/services/develancacheui/) |
|  | Dispatcharr | `dispatcharr` | url, username, password, enableActiveStreams | [↗](https://gethomepage.dev/widgets/services/dispatcharr/) |
|  | Dockhand | `dockhand` | url, environment, username, password | [↗](https://gethomepage.dev/widgets/services/dockhand/) |
|  | Emby | `emby` | url, key, enableBlocks, enableNowPlaying, enableUser, enableMediaControl, showEpisodeNumber, expandOneStreamToTwoRows | [↗](https://gethomepage.dev/widgets/services/emby/) |
|  | ESPHome | `esphome` | url, username, password | [↗](https://gethomepage.dev/widgets/services/esphome/) |
|  | EVCC | `evcc` | url | [↗](https://gethomepage.dev/widgets/services/evcc/) |
|  | Filebrowser | `filebrowser` | url, username, password, authHeader | [↗](https://gethomepage.dev/widgets/services/filebrowser/) |
|  | Fileflows | `fileflows` | url | [↗](https://gethomepage.dev/widgets/services/fileflows/) |
|  | Firefly III | `firefly` | url, key | [↗](https://gethomepage.dev/widgets/services/firefly/) |
|  | Flood | `flood` | url, username, password | [↗](https://gethomepage.dev/widgets/services/flood/) |
|  | FreshRSS | `freshrss` | url, username, password | [↗](https://gethomepage.dev/widgets/services/freshrss/) |
|  | Frigate | `frigate` | url, enableRecentEvents, username, password | [↗](https://gethomepage.dev/widgets/services/frigate/) |
|  | FRITZ!Box | `fritzbox` | url | [↗](https://gethomepage.dev/widgets/services/fritzbox/) |
|  | GameDig | `gamedig` | serverType, url, gameToken | [↗](https://gethomepage.dev/widgets/services/gamedig/) |
|  | Gatus | `gatus` | url | [↗](https://gethomepage.dev/widgets/services/gatus/) |
|  | Ghostfolio | `ghostfolio` | url, key | [↗](https://gethomepage.dev/widgets/services/ghostfolio/) |
|  | Gitea | `gitea` | url, key | [↗](https://gethomepage.dev/widgets/services/gitea/) |
|  | Gitlab | `gitlab` | url, key, user_id | [↗](https://gethomepage.dev/widgets/services/gitlab/) |
|  | Glances | `glances` | url, username, password, version, metric, diskUnits, refreshInterval, pointsLimit | [↗](https://gethomepage.dev/widgets/services/glances/) |
|  | Gluetun | `gluetun` | url, key, version | [↗](https://gethomepage.dev/widgets/services/gluetun/) |
|  | Gotify | `gotify` | url, key | [↗](https://gethomepage.dev/widgets/services/gotify/) |
|  | Grafana | `grafana` | version, alerts, url, username, password | [↗](https://gethomepage.dev/widgets/services/grafana/) |
|  | HDHomerun | `hdhomerun` | url, tuner, fields | [↗](https://gethomepage.dev/widgets/services/hdhomerun/) |
|  | Headscale | `headscale` | url, nodeId, key | [↗](https://gethomepage.dev/widgets/services/headscale/) |
|  | Health checks | `healthchecks` | url, key, uuid | [↗](https://gethomepage.dev/widgets/services/healthchecks/) |
|  | Home Assistant | `homeassistant` | url, key, custom, label, value | [↗](https://gethomepage.dev/widgets/services/homeassistant/) |
|  | Homebox | `homebox` | url, username, password, fields | [↗](https://gethomepage.dev/widgets/services/homebox/) |
|  | Homebridge | `homebridge` | url, username, password | [↗](https://gethomepage.dev/widgets/services/homebridge/) |
|  | iFrame | `iframe` | name, src | [↗](https://gethomepage.dev/widgets/services/iframe/) |
|  | Immich | `immich` | url, key, version | [↗](https://gethomepage.dev/widgets/services/immich/) |
|  | Jackett | `jackett` | url, password | [↗](https://gethomepage.dev/widgets/services/jackett/) |
|  | JDownloader | `jdownloader` | username, password, client | [↗](https://gethomepage.dev/widgets/services/jdownloader/) |
|  | Jellyfin | `jellyfin` | url, key, version, enableBlocks, enableNowPlaying, enableUser, enableMediaControl, showEpisodeNumber, expandOneStreamToTwoRows | [↗](https://gethomepage.dev/widgets/services/jellyfin/) |
|  | Jellystat | `jellystat` | url, key, days | [↗](https://gethomepage.dev/widgets/services/jellystat/) |
|  | Karakeep | `karakeep` | url, key | [↗](https://gethomepage.dev/widgets/services/karakeep/) |
|  | Kavita | `kavita` | url, username, password, key | [↗](https://gethomepage.dev/widgets/services/kavita/) |
|  | Komga | `komga` | url, username, password, key | [↗](https://gethomepage.dev/widgets/services/komga/) |
|  | Komodo | `komodo` | url, key, secret, showSummary, showStacks | [↗](https://gethomepage.dev/widgets/services/komodo/) |
|  | Kopia | `kopia` | url, username, password, snapshotHost, snapshotPath | [↗](https://gethomepage.dev/widgets/services/kopia/) |
|  | Lidarr | `lidarr` | url, key | [↗](https://gethomepage.dev/widgets/services/lidarr/) |
|  | Linkwarden | `linkwarden` | url, key | [↗](https://gethomepage.dev/widgets/services/linkwarden/) |
|  | LubeLogger | `lubelogger` | url, username, password, vehicleID | [↗](https://gethomepage.dev/widgets/services/lubelogger/) |
|  | Mailcow | `mailcow` | url, key | [↗](https://gethomepage.dev/widgets/services/mailcow/) |
|  | Mastodon | `mastodon` | url | [↗](https://gethomepage.dev/widgets/services/mastodon/) |
|  | Mealie | `mealie` | url, key, version | [↗](https://gethomepage.dev/widgets/services/mealie/) |
|  | Medusa | `medusa` | url, key | [↗](https://gethomepage.dev/widgets/services/medusa/) |
|  | Mikrotik | `mikrotik` | url, username, password | [↗](https://gethomepage.dev/widgets/services/mikrotik/) |
|  | Minecraft | `minecraft` | url | [↗](https://gethomepage.dev/widgets/services/minecraft/) |
|  | Miniflux | `miniflux` | url, key | [↗](https://gethomepage.dev/widgets/services/miniflux/) |
|  | MJPEG | `mjpeg` | stream | [↗](https://gethomepage.dev/widgets/services/mjpeg/) |
|  | Moonraker (Klipper) | `moonraker` | url | [↗](https://gethomepage.dev/widgets/services/moonraker/) |
|  | Mylar3 | `mylar` | url, key | [↗](https://gethomepage.dev/widgets/services/mylar/) |
|  | MySpeed | `myspeed` | url, password | [↗](https://gethomepage.dev/widgets/services/myspeed/) |
|  | Navidrome | `navidrome` | url, user, token, salt | [↗](https://gethomepage.dev/widgets/services/navidrome/) |
|  | NetAlertX | `netalertx` | url, key, version | [↗](https://gethomepage.dev/widgets/services/netalertx/) |
|  | Netdata | `netdata` | url | [↗](https://gethomepage.dev/widgets/services/netdata/) |
|  | Nextcloud | `nextcloud` | url, key | [↗](https://gethomepage.dev/widgets/services/nextcloud/) |
|  | NextDNS | `nextdns` | profile, key | [↗](https://gethomepage.dev/widgets/services/nextdns/) |
|  | Nginx Proxy Manager | `npm` | url, username, password | [↗](https://gethomepage.dev/widgets/services/nginx-proxy-manager/) |
|  | ntfy | `ntfy` | url, topic | [↗](https://gethomepage.dev/widgets/services/ntfy/) |
|  | NZBget | `nzbget` | url, username, password | [↗](https://gethomepage.dev/widgets/services/nzbget/) |
|  | OctoPrint | `octoprint` | url, key | [↗](https://gethomepage.dev/widgets/services/octoprint/) |
|  | Omada | `omada` | url, username, password, site | [↗](https://gethomepage.dev/widgets/services/omada/) |
|  | Ombi | `ombi` | url, key | [↗](https://gethomepage.dev/widgets/services/ombi/) |
|  | OpenDTU | `opendtu` | url | [↗](https://gethomepage.dev/widgets/services/opendtu/) |
|  | OpenMediaVault | `openmediavault` | url, username, password, method | [↗](https://gethomepage.dev/widgets/services/openmediavault/) |
|  | OpenWRT | `openwrt` | url, username, password, interfaceName | [↗](https://gethomepage.dev/widgets/services/openwrt/) |
|  | OPNSense | `opnsense` | url, username, password, wan | [↗](https://gethomepage.dev/widgets/services/opnsense/) |
|  | Pangolin | `pangolin` | url, key, org | [↗](https://gethomepage.dev/widgets/services/pangolin/) |
|  | Paperless-ngx | `paperlessngx` | url, username, password | [↗](https://gethomepage.dev/widgets/services/paperlessngx/) |
|  | PeaNUT | `peanut` | url, key, username, password | [↗](https://gethomepage.dev/widgets/services/peanut/) |
|  | pfSense | `pfsense` | url, username, password, headers, wan, version, fields | [↗](https://gethomepage.dev/widgets/services/pfsense/) |
|  | PhotoPrism | `photoprism` | url, username, password, key | [↗](https://gethomepage.dev/widgets/services/photoprism/) |
| ✓ | PiHole | `pihole` | url, version, key | [↗](https://gethomepage.dev/widgets/services/pihole/) |
|  | Plant-it | `plantit` | url, key | [↗](https://gethomepage.dev/widgets/services/plantit/) |
|  | Plex | `plex` | url, key | [↗](https://gethomepage.dev/widgets/services/plex/) |
|  | Portainer | `portainer` | url, env, kubernetes, key | [↗](https://gethomepage.dev/widgets/services/portainer/) |
|  | Prometheus | `prometheus` | url | [↗](https://gethomepage.dev/widgets/services/prometheus/) |
|  | Prometheus Metric | `prometheusmetric` | url, refreshInterval, metrics, query, format, suffix, options, maximumFractionDigits, scale, timeStyle | [↗](https://gethomepage.dev/widgets/services/prometheusmetric/) |
| ✓ | Prowlarr | `prowlarr` | url, key | [↗](https://gethomepage.dev/widgets/services/prowlarr/) |
| ✓ | Proxmox | `proxmox` | url, username, password, node | [↗](https://gethomepage.dev/widgets/services/proxmox/) |
|  | Proxmox Backup Server | `proxmoxbackupserver` | url, username, password, datastore | [↗](https://gethomepage.dev/widgets/services/proxmoxbackupserver/) |
|  | Pterodactyl | `pterodactyl` | url, key | [↗](https://gethomepage.dev/widgets/services/pterodactyl/) |
|  | Pyload | `pyload` | url, username, password, key | [↗](https://gethomepage.dev/widgets/services/pyload/) |
|  | qBittorrent | `qbittorrent` | url, username, password, enableLeechProgress, enableLeechSize | [↗](https://gethomepage.dev/widgets/services/qbittorrent/) |
|  | QNAP | `qnap` | url, username, password | [↗](https://gethomepage.dev/widgets/services/qnap/) |
| ✓ | Radarr | `radarr` | url, key, enableQueue | [↗](https://gethomepage.dev/widgets/services/radarr/) |
|  | Readarr | `readarr` | url, key | [↗](https://gethomepage.dev/widgets/services/readarr/) |
|  | Romm | `romm` | url, fields | [↗](https://gethomepage.dev/widgets/services/romm/) |
|  | ruTorrent | `rutorrent` | url, username, password | [↗](https://gethomepage.dev/widgets/services/rutorrent/) |
| ✓ | SABnzbd | `sabnzbd` | url, key | [↗](https://gethomepage.dev/widgets/services/sabnzbd/) |
|  | Scrutiny | `scrutiny` | url | [↗](https://gethomepage.dev/widgets/services/scrutiny/) |
| ✓ | Seerr Widget | `seerr` | url, key | [↗](https://gethomepage.dev/widgets/services/seerr/) |
|  | Slskd | `slskd` | url, key | [↗](https://gethomepage.dev/widgets/services/slskd/) |
| ✓ | Sonarr | `sonarr` | url, key, enableQueue | [↗](https://gethomepage.dev/widgets/services/sonarr/) |
|  | SparkyFitness | `sparkyfitness` | url, key | [↗](https://gethomepage.dev/widgets/services/sparkyfitness/) |
|  | Speedtest Tracker | `speedtest` | url, version, key, bitratePrecision | [↗](https://gethomepage.dev/widgets/services/speedtest-tracker/) |
|  | Spoolman | `spoolman` | url, spoolIds | [↗](https://gethomepage.dev/widgets/services/spoolman/) |
|  | Stash | `stash` | url, key, fields | [↗](https://gethomepage.dev/widgets/services/stash/) |
|  | Stocks | `stocks` | provider, showUSMarketStatus, watchlist | [↗](https://gethomepage.dev/widgets/services/stocks/) |
|  | Suwayomi | `suwayomi` | url, username, password, category | [↗](https://gethomepage.dev/widgets/services/suwayomi/) |
|  | SWAG Dashboard | `swagdashboard` | url | [↗](https://gethomepage.dev/widgets/services/swagdashboard/) |
|  | Syncthing Relay Server | `strelaysrv` | url | [↗](https://gethomepage.dev/widgets/services/syncthing-relay-server/) |
|  | Synology Disk Station | `diskstation` | url, username, password, volume | [↗](https://gethomepage.dev/widgets/services/diskstation/) |
|  | Synology Download Station | `downloadstation` | url, username, password | [↗](https://gethomepage.dev/widgets/services/downloadstation/) |
|  | Tailscale | `tailscale` | deviceid, key | [↗](https://gethomepage.dev/widgets/services/tailscale/) |
|  | Tandoor | `tandoor` | url, key | [↗](https://gethomepage.dev/widgets/services/tandoor/) |
| ✓ | Tautulli (Plex) | `tautulli` | url, key, enableUser, showEpisodeNumber, expandOneStreamToTwoRows | [↗](https://gethomepage.dev/widgets/services/plex-tautulli/) |
|  | Tdarr | `tdarr` | url, key | [↗](https://gethomepage.dev/widgets/services/tdarr/) |
|  | Technitium DNS Server | `technitium` | url, key, node, range | [↗](https://gethomepage.dev/widgets/services/technitium/) |
|  | Tracearr | `tracearr` | url, key, view, enableUser, showEpisodeNumber, expandOneStreamToTwoRows | [↗](https://gethomepage.dev/widgets/services/tracearr/) |
|  | Traefik | `traefik` | url, username, password | [↗](https://gethomepage.dev/widgets/services/traefik/) |
|  | Transmission | `transmission` | url, username, password, rpcUrl | [↗](https://gethomepage.dev/widgets/services/transmission/) |
|  | Trilium | `trilium` | url, key | [↗](https://gethomepage.dev/widgets/services/trilium/) |
|  | TrueNas | `truenas` | url, version, username, password, key, enablePools, nasType | [↗](https://gethomepage.dev/widgets/services/truenas/) |
|  | Tube Archivist | `tubearchivist` | url, key | [↗](https://gethomepage.dev/widgets/services/tubearchivist/) |
| ✓ | Unifi Controller | `unifi` | url, site, username, password, key | [↗](https://gethomepage.dev/widgets/services/unifi-controller/) |
|  | UniFi Drive | `unifi_drive` | url, username, password | [↗](https://gethomepage.dev/widgets/services/unifi-drive/) |
|  | Unmanic | `unmanic` | url | [↗](https://gethomepage.dev/widgets/services/unmanic/) |
|  | Unraid | `unraid` | url, key | [↗](https://gethomepage.dev/widgets/services/unraid/) |
|  | Uptime Kuma | `uptimekuma` | url, slug | [↗](https://gethomepage.dev/widgets/services/uptime-kuma/) |
|  | UptimeRobot | `uptimerobot` | url, key | [↗](https://gethomepage.dev/widgets/services/uptimerobot/) |
|  | UrBackup | `urbackup` | username, password, url, maxDays | [↗](https://gethomepage.dev/widgets/services/urbackup/) |
|  | Vikunja | `vikunja` | url, key, enableTaskList, version | [↗](https://gethomepage.dev/widgets/services/vikunja/) |
|  | Wallos | `wallos` | url, key | [↗](https://gethomepage.dev/widgets/services/wallos/) |
|  | Watchtower | `watchtower` | url, key | [↗](https://gethomepage.dev/widgets/services/watchtower/) |
|  | Wg-Easy | `wgeasy` | url, version, username, password, threshold | [↗](https://gethomepage.dev/widgets/services/wgeasy/) |
|  | What's Up Docker | `whatsupdocker` | url, username, password | [↗](https://gethomepage.dev/widgets/services/whatsupdocker/) |
|  | Xteve | `xteve` | url, username, password | [↗](https://gethomepage.dev/widgets/services/xteve/) |
|  | Your Spotify | `yourspotify` | url, key, interval | [↗](https://gethomepage.dev/widgets/services/yourspotify/) |
|  | Zabbix | `zabbix` | url, key | [↗](https://gethomepage.dev/widgets/services/zabbix/) |

