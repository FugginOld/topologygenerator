# Homepage widget docs — full cached mirror

Complete offline copy of all 155 Homepage service-widget docs (YAML config + selectable API fields + setup notes), so the full spec survives if the upstream site does not. Companion to the compact list in `homepage-widgets.md`.
Source: https://github.com/gethomepage/homepage/tree/main/docs/widgets/services · Cached: 2026-07-15

## Index

- [adguard-home](#widget-adguard-home)
- [apcups](#widget-apcups)
- [arcane](#widget-arcane)
- [argocd](#widget-argocd)
- [atsumeru](#widget-atsumeru)
- [audiobookshelf](#widget-audiobookshelf)
- [authentik](#widget-authentik)
- [autobrr](#widget-autobrr)
- [azuredevops](#widget-azuredevops)
- [backrest](#widget-backrest)
- [bazarr](#widget-bazarr)
- [beszel](#widget-beszel)
- [booklore](#widget-booklore)
- [caddy](#widget-caddy)
- [calendar](#widget-calendar)
- [calibre-web](#widget-calibre-web)
- [changedetectionio](#widget-changedetectionio)
- [channelsdvrserver](#widget-channelsdvrserver)
- [checkmk](#widget-checkmk)
- [cloudflared](#widget-cloudflared)
- [coin-market-cap](#widget-coin-market-cap)
- [crowdsec](#widget-crowdsec)
- [customapi](#widget-customapi)
- [deluge](#widget-deluge)
- [develancacheui](#widget-develancacheui)
- [diskstation](#widget-diskstation)
- [dispatcharr](#widget-dispatcharr)
- [dockhand](#widget-dockhand)
- [downloadstation](#widget-downloadstation)
- [emby](#widget-emby)
- [esphome](#widget-esphome)
- [evcc](#widget-evcc)
- [filebrowser](#widget-filebrowser)
- [fileflows](#widget-fileflows)
- [firefly](#widget-firefly)
- [flood](#widget-flood)
- [freshrss](#widget-freshrss)
- [frigate](#widget-frigate)
- [fritzbox](#widget-fritzbox)
- [gamedig](#widget-gamedig)
- [gatus](#widget-gatus)
- [ghostfolio](#widget-ghostfolio)
- [gitea](#widget-gitea)
- [gitlab](#widget-gitlab)
- [glances](#widget-glances)
- [gluetun](#widget-gluetun)
- [gotify](#widget-gotify)
- [grafana](#widget-grafana)
- [hdhomerun](#widget-hdhomerun)
- [headscale](#widget-headscale)
- [healthchecks](#widget-healthchecks)
- [homeassistant](#widget-homeassistant)
- [homebox](#widget-homebox)
- [homebridge](#widget-homebridge)
- [iframe](#widget-iframe)
- [immich](#widget-immich)
- [jackett](#widget-jackett)
- [jdownloader](#widget-jdownloader)
- [jellyfin](#widget-jellyfin)
- [jellystat](#widget-jellystat)
- [karakeep](#widget-karakeep)
- [kavita](#widget-kavita)
- [komga](#widget-komga)
- [komodo](#widget-komodo)
- [kopia](#widget-kopia)
- [lidarr](#widget-lidarr)
- [linkwarden](#widget-linkwarden)
- [lubelogger](#widget-lubelogger)
- [mailcow](#widget-mailcow)
- [mastodon](#widget-mastodon)
- [mealie](#widget-mealie)
- [medusa](#widget-medusa)
- [mikrotik](#widget-mikrotik)
- [minecraft](#widget-minecraft)
- [miniflux](#widget-miniflux)
- [mjpeg](#widget-mjpeg)
- [moonraker](#widget-moonraker)
- [mylar](#widget-mylar)
- [myspeed](#widget-myspeed)
- [navidrome](#widget-navidrome)
- [netalertx](#widget-netalertx)
- [netdata](#widget-netdata)
- [nextcloud](#widget-nextcloud)
- [nextdns](#widget-nextdns)
- [nginx-proxy-manager](#widget-nginx-proxy-manager)
- [ntfy](#widget-ntfy)
- [nzbget](#widget-nzbget)
- [octoprint](#widget-octoprint)
- [omada](#widget-omada)
- [ombi](#widget-ombi)
- [opendtu](#widget-opendtu)
- [openmediavault](#widget-openmediavault)
- [openwrt](#widget-openwrt)
- [opnsense](#widget-opnsense)
- [pangolin](#widget-pangolin)
- [paperlessngx](#widget-paperlessngx)
- [peanut](#widget-peanut)
- [pfsense](#widget-pfsense)
- [photoprism](#widget-photoprism)
- [pihole](#widget-pihole)
- [plantit](#widget-plantit)
- [plex-tautulli](#widget-plex-tautulli)
- [plex](#widget-plex)
- [portainer](#widget-portainer)
- [prometheus](#widget-prometheus)
- [prometheusmetric](#widget-prometheusmetric)
- [prowlarr](#widget-prowlarr)
- [proxmox](#widget-proxmox)
- [proxmoxbackupserver](#widget-proxmoxbackupserver)
- [pterodactyl](#widget-pterodactyl)
- [pyload](#widget-pyload)
- [qbittorrent](#widget-qbittorrent)
- [qnap](#widget-qnap)
- [radarr](#widget-radarr)
- [readarr](#widget-readarr)
- [romm](#widget-romm)
- [rutorrent](#widget-rutorrent)
- [sabnzbd](#widget-sabnzbd)
- [scrutiny](#widget-scrutiny)
- [seerr](#widget-seerr)
- [slskd](#widget-slskd)
- [sonarr](#widget-sonarr)
- [sparkyfitness](#widget-sparkyfitness)
- [speedtest-tracker](#widget-speedtest-tracker)
- [spoolman](#widget-spoolman)
- [stash](#widget-stash)
- [stocks](#widget-stocks)
- [suwayomi](#widget-suwayomi)
- [swagdashboard](#widget-swagdashboard)
- [syncthing-relay-server](#widget-syncthing-relay-server)
- [tailscale](#widget-tailscale)
- [tandoor](#widget-tandoor)
- [tdarr](#widget-tdarr)
- [technitium](#widget-technitium)
- [tracearr](#widget-tracearr)
- [traefik](#widget-traefik)
- [transmission](#widget-transmission)
- [trilium](#widget-trilium)
- [truenas](#widget-truenas)
- [tubearchivist](#widget-tubearchivist)
- [unifi-controller](#widget-unifi-controller)
- [unifi-drive](#widget-unifi-drive)
- [unmanic](#widget-unmanic)
- [unraid](#widget-unraid)
- [uptime-kuma](#widget-uptime-kuma)
- [uptimerobot](#widget-uptimerobot)
- [urbackup](#widget-urbackup)
- [vikunja](#widget-vikunja)
- [wallos](#widget-wallos)
- [watchtower](#widget-watchtower)
- [wgeasy](#widget-wgeasy)
- [whatsupdocker](#widget-whatsupdocker)
- [xteve](#widget-xteve)
- [yourspotify](#widget-yourspotify)
- [zabbix](#widget-zabbix)


<a id="widget-adguard-home"></a>

---

---
title: Adguard Home
description: Adguard Home Widget Configuration
---

Learn more about [Adguard Home](https://github.com/AdguardTeam/AdGuardHome).

The username and password are the same as used to login to the web interface.

Allowed fields: `["queries", "blocked", "filtered", "latency"]`.

```yaml
widget:
  type: adguard
  url: http://adguard.host.or.ip
  username: admin
  password: password
```


<a id="widget-apcups"></a>

---

---
title: APC UPS Monitoring
description: Lightweight monitoring widget for APC UPSs using apcupsd daemon
---

This widget extracts UPS information from an apcupsd daemon.
Only works for [APC/Schneider](https://www.se.com/us/en/product-range/61915-smartups/#products) UPS products.

[!NOTE]
By default apcupsd daemon is bound to 127.0.0.1. Edit `/etc/apcupsd.conf` and change `NISIP` to an IP accessible from your homepage docker (usually your internal LAN interface).

```yaml
widget:
  type: apcups
  url: tcp://your.acpupsd.host:3551
```


<a id="widget-arcane"></a>

---

---
title: Arcane
description: Arcane Widget Configuration
---

Learn more about [Arcane](https://github.com/getarcaneapp/arcane).

**Allowed fields** (max 4): `running`, `stopped`, `total`, `images`, `images_used`, `images_unused`, `image_updates`.
**Default fields**: `running`, `stopped`, `total`, `image_updates`.

```yaml
widget:
  type: arcane
  url: http://localhost:3552
  env: 0 # required, 0 is Arcane default local environment
  key: your-api-key
  fields: ["running", "stopped", "total", "image_updates"] # optional
```


<a id="widget-argocd"></a>

---

---
title: ArgoCD
description: ArgoCD Widget Configuration
---

Learn more about [ArgoCD](https://argo-cd.readthedocs.io/en/stable/).

Allowed fields (limited to a max of 4): `["apps", "synced", "outOfSync", "healthy", "progressing", "degraded", "suspended", "missing"]`

```yaml
widget:
  type: argocd
  url: http://argocd.host.or.ip:port
  key: argocdapikey
```

You can generate an API key either by creating a bearer token for an existing account, see [Authorization](https://argo-cd.readthedocs.io/en/latest/developer-guide/api-docs/#authorization) (not recommended) or create a new local user account with limited privileges and generate an authentication token for this account. To do this the steps are:

- [Create a new local user](https://argo-cd.readthedocs.io/en/stable/operator-manual/user-management/#create-new-user) and give it the `apiKey` capability
- Setup [RBAC configuration](https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/#rbac-configuration) for your the user and give it readonly access to your ArgoCD resources, e.g. by giving it the `role:readonly` role.
- In your ArgoCD project under _Settings / Accounts_ open the newly created account and in the _Tokens_ section click on _Generate New_ to generate an access token, optionally specifying an expiry date.

If you installed ArgoCD via the official Helm chart, the account creation and rbac config can be achived by overriding these helm values:

```yaml
configs:
  cm:
    accounts.readonly: apiKey
  rbac:
    policy.csv: "g, readonly, role:readonly"
```

This creates a new account called `readonly` and attaches the `role:readonly` role to it.


<a id="widget-atsumeru"></a>

---

---
title: Atsumeru
description: Atsumeru Widget Configuration
---

Learn more about [Atsumeru](https://github.com/AtsumeruDev/Atsumeru).

Define same username and password that is used for login from web or supported apps

Allowed fields: `["series", "archives", "chapters", "categories"]`.

```yaml
widget:
  type: atsumeru
  url: http://atsumeru.host.or.ip:port
  username: username
  password: password
```


<a id="widget-audiobookshelf"></a>

---

---
title: Audiobookshelf
description: Audiobookshelf Widget Configuration
---

Learn more about [Audiobookshelf](https://github.com/advplyr/audiobookshelf).

You can find your API token by logging into the Audiobookshelf web app as an admin, go to the config → users page, and click on your account.

Allowed fields: `["podcasts", "podcastsDuration", "books", "booksDuration"]`

```yaml
widget:
  type: audiobookshelf
  url: http://audiobookshelf.host.or.ip:port
  key: audiobookshelflapikey
```


<a id="widget-authentik"></a>

---

---
title: Authentik
description: Authentik Widget Configuration
---

Learn more about [Authentik](https://github.com/goauthentik/authentik).

This widget reads the number of active users in the system, as well as logins for the last 24 hours.

You will need to generate an API token for an existing user under `Admin Portal` > `Directory` > `Tokens & App passwords`.
Make sure to set Intent to "API Token".

The account you made the API token for also needs the following **Assigned global permissions** in Authentik:

- authentik Core -> Can view User (Model: User)
- authentik Events -> Can view Event (Model: Event)

Allowed fields: `["users", "loginsLast24H", "failedLoginsLast24H"]`.

| Authentik Version | Homepage Widget Version |
| ----------------- | ----------------------- |
| < 2025.8.0        | 1 (default)             |
| >= 2025.8.0       | 2                       |

```yaml
widget:
  type: authentik
  url: http://authentik.host.or.ip:port
  key: api_token
  version: 2 # optional, default is 1
```


<a id="widget-autobrr"></a>

---

---
title: Autobrr
description: Autobrr Widget Configuration
---

Learn more about [Autobrr](https://github.com/autobrr/autobrr).

Find your API key under `Settings > API Keys`.

Allowed fields: `["approvedPushes", "rejectedPushes", "filters", "indexers"]`.

```yaml
widget:
  type: autobrr
  url: http://autobrr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-azuredevops"></a>

---

---
title: Azure DevOps
description: Azure DevOps Widget Configuration
---

Learn more about [Azure DevOps](https://azure.microsoft.com/en-us/products/devops).

This widget has 2 functions:

1. Pipelines: checks if the relevant pipeline is running or not, and if not, reports the last status.<br>
   Allowed fields: `["result", "status"]`.

2. Pull Requests: returns the amount of open PRs, the amount of the PRs you have open, and how many PRs that you open are marked as 'Approved' by at least 1 person and not yet completed.<br>
   Allowed fields: `["totalPrs", "myPrs", "approved"]`.

You will need to generate a personal access token for an existing user, see the [azure documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows#create-a-pat)

```yaml
widget:
  type: azuredevops
  organization: myOrganization
  project: myProject
  definitionId: pipelineDefinitionId # required for pipelines
  branchName: branchName # optional for pipelines, leave empty for all
  userEmail: email # required for pull requests
  repositoryId: prRepositoryId # required for pull requests
  key: personalaccesstoken
```


<a id="widget-backrest"></a>

---

---
title: Backrest
description: Backrest Widget Configuration
---

[Backrest](https://garethgeorge.github.io/backrest/) is a web-based frontend for
the [Restic](https://restic.net/) backup tool.

**Allowed fields:** `["num_success_latest","num_failure_latest","num_success_30","num_plans","num_failure_30","bytes_added_30"]`

```yaml
widget:
  type: backrest
  url: http://backrest.host.or.ip
  username: admin # optional if auth is enabled in Backrest
  password: admin # optional if auth is enabled in Backrest
```


<a id="widget-bazarr"></a>

---

---
title: Bazarr
description: Bazarr Widget Configuration
---

Learn more about [Bazarr](https://github.com/morpheus65535/bazarr).

Find your API key under `Settings > General`.

Allowed fields: `["missingEpisodes", "missingMovies"]`.

```yaml
widget:
  type: bazarr
  url: http://bazarr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-beszel"></a>

---

---
title: Beszel
description: Beszel Widget Configuration
---

Learn more about [Beszel](https://github.com/henrygd/beszel)

The widget has two modes, a single system with detailed info if `systemId` is provided, or an overview of all systems if `systemId` is not provided.

The `systemID` is the `id` field on the collections page of Beszel under the PocketBase admin panel. You can also use the 'nice name' from the Beszel UI.

A "superuser" is currently required to access the data from the Beszel API.

Allowed fields for 'overview' mode: `["systems", "up"]`
Allowed fields for a single system: `["name", "status", "updated", "cpu", "memory", "disk", "network"]`

| Beszel Version | Homepage Widget Version |
| -------------- | ----------------------- |
| < 0.9.0        | 1 (default)             |
| >= 0.9.0       | 2                       |

```yaml
widget:
  type: beszel
  url: http://beszel.host.or.ip
  username: username # email
  password: password
  systemId: systemId # optional
  version: 2 # optional, default is 1
```


<a id="widget-booklore"></a>

---

---
title: Booklore
description: Booklore Widget Configuration
---

Learn more about [Booklore](https://github.com/booklore-app/booklore).

The widget authenticates with your Booklore credentials to surface total libraries, books, and reading progress counts for your account.

```yaml
widget:
  type: booklore
  url: https://booklore.host.or.ip
  username: username
  password: password
```


<a id="widget-caddy"></a>

---

---
title: Caddy
description: Caddy Widget Configuration
---

Learn more about [Caddy](https://github.com/caddyserver/caddy).

Allowed fields: `["upstreams", "requests", "requests_failed"]`.

```yaml
widget:
  type: caddy
  url: http://caddy.host.or.ip:adminport # default admin port is 2019
```


<a id="widget-calendar"></a>

---

---
title: Calendar
description: Calendar widget
---

## Monthly view

<img alt="calendar" src="https://user-images.githubusercontent.com/5442891/271131282-6767a3ea-573e-4005-aeb9-6e14ee01e845.png">

This widget shows monthly calendar, with optional integrations to show events from supported widgets.

```yaml
widget:
  type: calendar
  firstDayInWeek: sunday # optional - defaults to monday
  view: monthly # optional - possible values monthly, agenda
  maxEvents: 10 # optional - defaults to 10
  showTime: true # optional - show time for event happening today - defaults to false
  timezone: America/Los_Angeles # optional and only when timezone is not detected properly (slightly slower performance) - force timezone for ical events (if it's the same - no change, if missing or different in ical - will be converted to this timezone)
  integrations: # optional
    - type: sonarr # active widget type that is currently enabled on homepage - possible values: radarr, sonarr, lidarr, readarr, ical
      service_group: Media # group name where widget exists
      service_name: Sonarr # service name for that widget
      color: teal # optional - defaults to pre-defined color for the service (teal for sonarr)
      baseUrl: https://sonarr.domain.url # optional - adds links to sonarr/radarr pages
      params: # optional - additional params for the service
        unmonitored: true # optional - defaults to false, used with *arr stack
    - type: ical # Show calendar events from another service
      url: https://domain.url/with/link/to.ics # URL with calendar events
      name: My Events # required - name for these calendar events
      color: zinc # optional - defaults to pre-defined color for the service (zinc for ical)
      params: # optional - additional params for the service
        showName: true # optional - show name before event title in event line - defaults to false
```

## Agenda

This view shows only list of events from configured integrations

```yaml
widget:
  type: calendar
  view: agenda
  maxEvents: 10 # optional - defaults to 10
  showTime: true # optional - show time for event happening today - defaults to false
  previousDays: 3 # optional - shows events since three days ago - defaults to 0
  integrations: # same as in Monthly view example
```

## Integrations

Currently integrated widgets are [sonarr](sonarr.md), [radarr](radarr.md), [lidarr](lidarr.md) and [readarr](readarr.md).

Supported colors can be found on [color palette](../../configs/settings.md#color-palette).

### iCal

This custom integration allows you to show events from any calendar that supports iCal format, for example, Google Calendar (go to `Settings`, select specific calendar, go to `Integrate calendar`, copy URL from `Public Address in iCal format`).


<a id="widget-calibre-web"></a>

---

---
title: Calibre-web
description: Calibre-web Widget Configuration
---

Learn more about [Calibre-web](https://github.com/janeczku/calibre-web).

**Note: widget requires calibre-web ≥ v0.6.21.**

Allowed fields: `["books", "authors", "categories", "series"]`.

```yaml
widget:
  type: calibreweb
  url: http://your.calibreweb.host:port
  username: username
  password: password
```


<a id="widget-changedetectionio"></a>

---

---
title: Changedetection.io
description: Changedetection.io Widget Configuration
---

Learn more about [Changedetection.io](https://github.com/dgtlmoon/changedetection.io).

Find your API key under `Settings > API`.

Allowed fields: `["diffsDetected", "totalObserved"]`.

```yaml
widget:
  type: changedetectionio
  url: http://changedetection.host.or.ip:port
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-channelsdvrserver"></a>

---

---
title: Channels DVR Server
description: Channels DVR Server Widget Configuration
---

Learn more about [Channels DVR Server](https://getchannels.com/dvr-server/).

```yaml
widget:
  type: channelsdvrserver
  url: http://server.host.or.ip:port
```


<a id="widget-checkmk"></a>

---

---
title: Checkmk
description: Checkmk Widget Configuration
---

Learn more about [Checkmk](https://github.com/Checkmk/checkmk).

To setup authentication, follow the official [Checkmk API](https://docs.checkmk.com/latest/en/rest_api.html?lquery=api#bearerauth) documentation.

```yaml
widget:
  type: checkmk
  url: http://checkmk.host.or.ip:port
  site: your-site-name-cla-by-default
  username: username
  password: password
```


<a id="widget-cloudflared"></a>

---

---
title: Cloudflare Tunnels
description: Cloudflare Tunnels Widget Configuration
---

Learn more about [Cloudflare Tunnels](https://www.cloudflare.com/products/tunnel/).

_As of v0.6.10 this widget no longer accepts a Cloudflare global API key (or account email) due to security concerns. Instead, you should setup an API token which only requires the permissions `Account.Cloudflare Tunnel:Read`._

Allowed fields: `["status", "origin_ip"]`.

```yaml
widget:
  type: cloudflared
  accountid: accountid # from zero trust dashboard url e.g. https://one.dash.cloudflare.com/<accountid>/home/quick-start
  tunnelid: tunnelid # found in tunnels dashboard under the tunnel name
  key: cloudflareapitoken # api token with `Account.Cloudflare Tunnel:Read` https://dash.cloudflare.com/profile/api-tokens
```


<a id="widget-coin-market-cap"></a>

---

---
title: Coin Market Cap
description: Coin Market Cap Widget Configuration
---

Learn more about [Coin Market Cap](https://coinmarketcap.com/api).

Get your API key from your [CoinMarketCap Pro Dashboard](https://pro.coinmarketcap.com/account).

Allowed fields: no configurable fields for this widget.

```yaml
widget:
  type: coinmarketcap
  currency: GBP # Optional
  symbols: [BTC, LTC, ETH]
  key: apikeyapikeyapikeyapikeyapikey
  defaultinterval: 7d # Optional
```

You can also specify slugs instead of symbols (since symbols aren't guaranteed to be unique). If you supply both, slugs will be used. For example:

```yaml
widget:
  type: coinmarketcap
  slugs: [chia-network, uniswap]
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-crowdsec"></a>

---

---
title: Crowdsec
description: Crowdsec Widget Configuration
---

Learn more about [Crowdsec](https://crowdsec.net).

See the [crowdsec docs](https://docs.crowdsec.net/docs/local_api/intro/#machines) for information about registering a machine,
in most instances you can use the default credentials (`/etc/crowdsec/local_api_credentials.yaml`).

!!! note
Without the `limit24h` option, the widget will fetch all alerts which is limited to 100 by the API to avoid performance issues.

Allowed fields: `["alerts", "bans"]`.

```yaml
widget:
  type: crowdsec
  url: http://crowdsechostorip:port
  username: localhost # machine_id in crowdsec
  password: password
  limit24h: true # optional, limits alerts to last 24h. Default: false
```


<a id="widget-customapi"></a>

---

---
title: Custom API
description: Custom Widget Configuration from the API
---

This widget can show information from custom self-hosted or third party API.

Fields need to be defined in the `mappings` section YAML object to correlate with the value in the APIs JSON object. Final field definition needs to be the key with the desired value information.

```yaml
widget:
  type: customapi
  url: http://custom.api.host.or.ip:port/path/to/exact/api/endpoint
  refreshInterval: 10000 # optional - in milliseconds, defaults to 10s
  username: username # auth - optional
  password: password # auth - optional
  method: GET # optional, e.g. POST
  headers: # optional, must be object, see below
  requestBody: # optional, can be string or object, see below
  display: # optional, default to block, see below
  mappings:
    - field: key
      label: Field 1
      format: text # optional - defaults to text
    - field: path.to.key2
      format: number # optional - defaults to text
      label: Field 2
    - field: path.to.another.key3
      label: Field 3
      format: percent # optional - defaults to text
    - field: key
      label: Field 4
      format: date # optional - defaults to text
      locale: nl # optional
      dateStyle: long # optional - defaults to "long". Allowed values: `["full", "long", "medium", "short"]`.
      timeStyle: medium # optional - Allowed values: `["full", "long", "medium", "short"]`.
    - field: key
      label: Field 5
      format: relativeDate # optional - defaults to text
      locale: nl # optional
      style: short # optional - defaults to "long". Allowed values: `["long", "short", "narrow"]`.
      numeric: auto # optional - defaults to "always". Allowed values `["always", "auto"]`.
    - field: key
      label: Field 6
      format: text
      additionalField: # optional
        field: hourly.time.key
        color: theme # optional - defaults to "". Allowed values: `["theme", "adaptive", "black", "white"]`.
        format: date # optional
    - field: key
      label: Number of things in array
      format: size
    # This (no field) will take the root of the API response, e.g. when APIs return an array:
    - label: Number of items
      format: size
```

Supported formats for the values are `text`, `number`, `float`, `percent`, `duration`, `bytes`, `bitrate`, `size`, `date` and `relativeDate`.

The `dateStyle` and `timeStyle` options of the `date` format are passed directly to [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) and the `style` and `numeric` options of `relativeDate` are passed to [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat).

The `duration` format expects the duration to be specified in seconds. The `scale` transformation tool can be used if a conversion is required.

The `size` format will return the length of the array or string, or the number of keys in an object. This is then formatted as `number`.

## Example

For the following JSON object from the API:

```json
{
  "id": 1,
  "name": "Rick Sanchez",
  "status": "Alive",
  "species": "Human",
  "gender": "Male",
  "origin": {
    "name": "Earth (C-137)"
  },
  "locations": [
    {
      "name": "Earth (C-137)"
    },
    {
      "name": "Citadel of Ricks"
    }
  ]
}
```

Define the `mappings` section as an array, for example:

```yaml
mappings:
  - field: name # Rick Sanchez
    label: Name
  - field: status # Alive
    label: Status
  - field: origin.name # Earth (C-137)
    label: Origin
  - field: locations.1.name # Citadel of Ricks
    label: Location
```

Note that older versions of the widget accepted fields as a yaml object, which is still supported. E.g.:

```yaml
mappings:
  - field:
      locations:
        1: name # Citadel of Ricks
    label: Location
```

## Data Transformation

You can manipulate data with the following tools `remap`, `scale`, `prefix` and `suffix`, for example:

```yaml
- field: key4
  label: Field 4
  format: text
  remap:
    - value: 0
      to: None
    - value: 1
      to: Connected
    - any: true # will map all other values
      to: Unknown
- field: key5
  label: Power
  format: float
  scale: 0.001 # can be number or string e.g. 1/16
  suffix: "kW"
- field: key6
  label: Price
  format: float
  prefix: "$"
```

## Display Options

The widget supports different display modes that can be set using the `display` property.

### Block View (Default)

The default display mode is `block`, which shows fields in a block format.

### List View

You can change the default block view to a list view by setting the `display` option to `list`.

The list view can optionally display an additional field next to the primary field.

`additionalField`: Similar to `field`, but only used in list view. Displays additional information for the mapping object on the right.

`field`: Defined the same way as other custom api widget fields.

`color`: Allowed options: `"theme", "adaptive", "black", "white"`. The option `adaptive` will apply a color using the value of the `additionalField`, green for positive numbers, red for negative numbers.

```yaml
- field: key
  label: Field
  format: text
  remap:
    - value: 0
      to: None
    - value: 1
      to: Connected
    - any: true # will map all other values
      to: Unknown
  additionalField:
    field: hourly.time.key
    color: theme
    format: date
```

### Dynamic List View

To display a list of items from an array in the API response, set the `display` property to `dynamic-list` and configure the `mappings` object with the following properties:

```yaml
widget:
  type: customapi
  url: https://example.com/api/servers
  display: dynamic-list
  mappings:
    items: data # optional, the path to the array in the API response. Omit this option if the array is at the root level
    name: id # required, field in each item to use as the item name (left side)
    label: ip_address # required, field in each item to use as the item label (right side)
    limit: 5 # optional, limit the number of items to display
    format: text # optional - format of the label field
    target: https://example.com/server/{id} # optional, makes items clickable with template support
```

This configuration would work with an API that returns a response like:

```json
{
  "data": [
    { "id": "server1", "name": "Server 1", "ip_address": "192.168.0.1" },
    { "id": "server2", "name": "Server 2", "ip_address": "192.168.0.2" }
  ]
}
```

The widget would display a list with two items:

- "Server 1" on the left and "192.168.0.1" on the right, clickable to "https://example.com/server/server1"
- "Server 2" on the left and "192.168.0.2" on the right, clickable to "https://example.com/server/server2"

For nested fields in the items, you can use dot notation:

```yaml
mappings:
  items: data.results.servers
  name: details.id
  label: details.name
```

## Custom Headers

Pass custom headers using the `headers` option, for example:

```yaml
headers:
  X-API-Token: token
```

## Custom Request Body

Pass custom request body using the `requestBody` option in either a string or object format. Objects will automatically be converted to a JSON string.

```yaml
requestBody:
  foo: bar
# or
requestBody: "{\"foo\":\"bar\"}"
```

Both formats result in `{"foo":"bar"}` being sent as the request body. Don't forget to set your `Content-Type` headers!


<a id="widget-deluge"></a>

---

---
title: Deluge
description: Deluge Widget Configuration
---

Learn more about [Deluge](https://deluge-torrent.org/).

Uses the same password used to login to the webui, see [the deluge FAQ](https://dev.deluge-torrent.org/wiki/Faq#Whatisthedefaultpassword).

Allowed fields: `["leech", "download", "seed", "upload"]`.

```yaml
widget:
  type: deluge
  url: http://deluge.host.or.ip
  password: password # webui password
  enableLeechProgress: true # optional, defaults to false
```


<a id="widget-develancacheui"></a>

---

---
title: DeveLanCacheUI
description: DeveLanCacheUI Widget Configuration
---

Learn more about [DeveLanCacheUI](https://github.com/devedse/DeveLanCacheUI_Backend).

```yaml
widget:
  type: develancacheui
  url: http://your.develancacheui_backend.host:port
```

The url should point to the DeveLanCacheUI Backend (API)


<a id="widget-diskstation"></a>

---

---
title: Synology Disk Station
description: Synology Disk Station Widget Configuration
---

Learn more about [Synology Disk Station](https://www.synology.com/en-global/dsm).

Note: the widget is not compatible with 2FA.

An optional 'volume' parameter can be supplied to specify which volume's free space to display when more than one volume exists. The value of the parameter must be in form of `volume_N`, e.g. to display free space for volume2, `volume_2` should be set as 'volume' value. If omitted, first returned volume's free space will be shown (not guaranteed to be volume1).

Allowed fields: `["uptime", "volumeAvailable", "resources.cpu", "resources.mem"]`.

To access these system metrics you need to connect to the DiskStation (`DSM`) with an account that is a member of the default `Administrators` group. That is because these metrics are requested from the API's `SYNO.Core.System` part that is only available to admin users. In order to keep the security impact as small as possible we can set the account in DSM up to limit the user's permissions inside the Synology system. In DSM 7.x, for instance, follow these steps:

1. Create a new user, i.e. `remote_stats`.
2. Set up a strong password for the new user
3. Under the `User Groups` tab of the user config dialogue check the box for `Administrators`.
4. On the `Permissions` tab check the top box for `No Access`, effectively prohibiting the user from accessing anything in the shared folders.
5. Under `Applications` check the box next to `Deny` in the header to explicitly prohibit login to all applications.
6. Now _only_ allow login to the `DSM` and `Download Station` applications, either by
   - unchecking `Deny` in the respective row, or (if inheriting permission doesn't work because of other group settings)
   - checking `Allow` for this app, or
   - checking `By IP` for this app to limit the source of login attempts to one or more IP addresses/subnets.
7. When the `Preview` column shows `Allow` in the `DSM` row, click `Save`.

Now configure the widget with the correct login information and test it.

If you encounter issues during testing:

1. Make sure to uncheck the option for automatic blocking due to invalid logins under `Control Panel > Security > Protection`.
   - If desired, this setting can be reactivated once the login is established working.
2. Login to your Synology DSM with the newly created account and accept terms and conditions.
3. Reattempt

```yaml
widget:
  type: diskstation
  url: http://diskstation.host.or.ip:port
  username: username
  password: password
  volume: volume_N # optional
```


<a id="widget-dispatcharr"></a>

---

---
title: Dispatcharr
description: Dispatcharr Widget Configuration
---

Learn more about [Dispatcharr](https://github.com/Dispatcharr/Dispatcharr).

Allowed fields: `["channels", "streams"]`.

```yaml
widget:
  type: dispatcharr
  url: http://dispatcharr.host.or.ip
  username: username
  password: password
  enableActiveStreams: true # optional, defaults to false
```


<a id="widget-dockhand"></a>

---

---
title: Dockhand
description: Dockhand Widget Configuration
---

Learn more about [Dockhand](https://dockhand.pro/).

Note: The widget currently supports Dockhand's **local** authentication only.

**Allowed fields:** (max 4): `running`, `stopped`, `paused`, `total`, `cpu`, `memory`, `images`, `volumes`, `events_today`, `pending_updates`, `stacks`.
**Default fields:** `running`, `total`, `cpu`, `memory`.

```yaml
widget:
  type: dockhand
  url: http://localhost:3001
  environment: local # optional: name or id; aggregates all when omitted
  username: your-user # required for local auth
  password: your-pass # required for local auth
```


<a id="widget-downloadstation"></a>

---

---
title: Synology Download Station
description: Synology Download Station Widget Configuration
---

Learn more about [Synology Download Station](https://www.synology.com/en-us/dsm/packages/DownloadStation).

Note: the widget is not compatible with 2FA.

Allowed fields: `["leech", "download", "seed", "upload"]`.

```yaml
widget:
  type: downloadstation
  url: http://downloadstation.host.or.ip:port
  username: username
  password: password
```


<a id="widget-emby"></a>

---

---
title: Emby
description: Emby Widget Configuration
---

Learn more about [Emby](https://github.com/MediaBrowser/Emby).

You can create an API key from inside Emby at `Settings > Advanced > Api Keys`.

As of v0.6.11 the widget supports fields `["movies", "series", "episodes", "songs"]`. These blocks are disabled by default but can be enabled with the `enableBlocks` option, and the "Now Playing" feature (enabled by default) can be disabled with the `enableNowPlaying` option.

```yaml
widget:
  type: emby
  url: http://emby.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
  enableBlocks: true # optional, defaults to false
  enableNowPlaying: true # optional, defaults to true
  enableUser: true # optional, defaults to false
  enableMediaControl: false # optional, defaults to true
  showEpisodeNumber: true # optional, defaults to false
  expandOneStreamToTwoRows: false # optional, defaults to true
```


<a id="widget-esphome"></a>

---

---
title: ESPHome
description: ESPHome Widget Configuration
---

Learn more about [ESPHome](https://esphome.io/).

Show the number of ESPHome devices based on their state.

Allowed fields: `["total", "online", "offline", "offline_alt", "unknown"]` (maximum of 4).

By default ESPHome will only mark devices as `offline` if their address cannot be pinged. If it has an invalid config or its name cannot be resolved (by DNS) its status will be marked as `unknown`.
To group both `offline` and `unknown` devices together, users should use the `offline_alt` field instead. This sums all devices that are _not_ online together.

```yaml
widget:
  type: esphome
  url: http://esphome.host.or.ip:port
  username: myesphomeuser # only if auth enabled
  password: myesphomepass # only if auth enabled
```


<a id="widget-evcc"></a>

---

---
title: EVCC
description: EVCC Widget Configuration
---

Learn more about [EVCC](https://github.com/evcc-io/evcc).

Allowed fields: `["pv_power", "grid_power", "home_power", "charge_power]`.

```yaml
widget:
  type: evcc
  url: http://evcc.host.or.ip:port
```


<a id="widget-filebrowser"></a>

---

---
title: Filebrowser
description: Filebrowser Widget Configuration
---

Learn more about [Filebrowser](https://filebrowser.org).

If you are using [Proxy header authentication](https://filebrowser.org/configuration/authentication-method#proxy-header) you have to set `authHeader` and `username`.

Allowed fields: `["available", "used", "total"]`.

```yaml
widget:
  type: filebrowser
  url: http://filebrowserhostorip:port
  username: username
  password: password
  authHeader: X-My-Header # If using Proxy header authentication
```


<a id="widget-fileflows"></a>

---

---
title: Fileflows
description: Fileflows Widget Configuration
---

Learn more about [FileFlows](https://github.com/revenz/FileFlows).

Allowed fields: `["queue", "processing", "processed", "time"]`.

```yaml
widget:
  type: fileflows
  url: http://your.fileflows.host:port
```


<a id="widget-firefly"></a>

---

---
title: Firefly III
description: Firefly III Widget Configuration
---

Learn more about [Firefly III](https://www.firefly-iii.org/).

Find your API key under `Options > Profile > OAuth > Personal Access Tokens`.

Allowed fields: `["networth" ,"budget"]`.

```yaml
widget:
  type: firefly
  url: https://firefly.host.or.ip
  key: personalaccesstoken.personalaccesstoken.personalaccesstoken
```


<a id="widget-flood"></a>

---

---
title: Flood
description: Flood Widget Configuration
---

Learn more about [Flood](https://github.com/jesec/flood).

Allowed fields: `["leech", "download", "seed", "upload"]`.

```yaml
widget:
  type: flood
  url: http://flood.host.or.ip
  username: username # if set
  password: password # if set
```


<a id="widget-freshrss"></a>

---

---
title: FreshRSS
description: FreshRSS Widget Configuration
---

Learn more about [FreshRSS](https://github.com/FreshRSS/FreshRSS).

Please refer to [Enable the API in FreshRSS](https://freshrss.github.io/FreshRSS/en/users/06_Mobile_access.html#enable-the-api-in-freshrss) for the "API password" to be entered in the password field.

Allowed fields: `["subscriptions", "unread"]`.

```yaml
widget:
  type: freshrss
  url: http://freshrss.host.or.ip:port
  username: username
  password: password
```


<a id="widget-frigate"></a>

---

---
title: Frigate
description: Frigate Widget Configuration
---

Learn more about [Frigate](https://frigate.video/).

Allowed fields: `["cameras", "uptime", "version"]`.

A recent event listing is disabled by default, but can be enabled with the `enableRecentEvents` option.

```yaml
widget:
  type: frigate
  url: http://frigate.host.or.ip:port
  enableRecentEvents: true # Optional, defaults to false
  username: username # optional
  password: password # optional
```


<a id="widget-fritzbox"></a>

---

---
title: FRITZ!Box
description: FRITZ!Box Widget Configuration
---

Application access & UPnP must be activated on your device:

```
Home Network > Network > Network Settings > Access Settings in the Home Network
[x] Allow access for applications
[x] Transmit status information over UPnP
```

Credentials are not needed and, as such, you may want to consider using `http` instead of `https` as those requests are significantly faster.

Allowed fields (limited to a max of 4): `["connectionStatus", "uptime", "maxDown", "maxUp", "down", "up", "received", "sent", "externalIPAddress", "externalIPv6Address", "externalIPv6Prefix"]`.

```yaml
widget:
  type: fritzbox
  url: http://192.168.178.1
```


<a id="widget-gamedig"></a>

---

---
title: GameDig
description: GameDig Widget Configuration
---

Learn more about [GameDig](https://github.com/gamedig/node-gamedig).

Uses the [GameDig](https://www.npmjs.com/package/gamedig) library to get game server information for any supported server type.

Allowed fields (limited to a max of 4): `["status", "name", "map", "currentPlayers", "players", "maxPlayers", "bots", "ping"]`.

```yaml
widget:
  type: gamedig
  serverType: csgo # see https://github.com/gamedig/node-gamedig#games-list
  url: udp://server.host.or.ip:port
  gameToken: # optional, a token used by gamedig with certain games
```


<a id="widget-gatus"></a>

---

---
title: Gatus
description: Gatus Widget Configuration
---

Learn more about [Gatus](https://github.com/TwiN/gatus).

Allowed fields: `["up", "down", "uptime"]`.

```yaml
widget:
  type: gatus
  url: http://gatus.host.or.ip:port
```


<a id="widget-ghostfolio"></a>

---

---
title: Ghostfolio
description: Ghostfolio Widget Configuration
---

Learn more about [Ghostfolio](https://github.com/ghostfolio/ghostfolio).

Authentication requires manually obtaining a Bearer token which can be obtained by make a POST request to the API e.g.

```
curl -X POST http://localhost:3333/api/v1/auth/anonymous -H 'Content-Type: application/json' -d '{ "accessToken": "SECURITY_TOKEN_OF_ACCOUNT" }'
```

See the [official docs](https://github.com/ghostfolio/ghostfolio#authorization-bearer-token).

_Note that the Bearer token is valid for 6 months, after which a new one must be generated._

Allowed fields: `["gross_percent_today", "gross_percent_1y", "gross_percent_max", "net_worth"]`

```yaml
widget:
  type: ghostfolio
  url: http://ghostfoliohost:port
  key: ghostfoliobearertoken
```


<a id="widget-gitea"></a>

---

---
title: Gitea
description: Gitea Widget Configuration
---

Learn more about [Gitea](https://gitea.com).

API token requires `notifications`, `repository` and `issue` permissions. See the [gitea documentation](https://docs.gitea.com/development/api-usage#generating-and-listing-api-tokens) for details on generating tokens.

Allowed fields: `["repositories", "notifications", "issues", "pulls"]`.

```yaml
widget:
  type: gitea
  url: http://gitea.host.or.ip:port
  key: giteaapitoken
```


<a id="widget-gitlab"></a>

---

---
title: Gitlab
description: Gitlab Widget Configuration
---

Learn more about [Gitlab](https://gitlab.com).

API requires a personal access token with either `read_api` or `api` permission. See the [gitlab documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) for details on generating one.

Your Gitlab user ID can be found on [your profile page](https://support.circleci.com/hc/en-us/articles/20761157174043-How-to-find-your-GitLab-User-ID).

Allowed fields: `["events", "issues", "merges", "projects"]`.

```yaml
widget:
  type: gitlab
  url: http://gitlab.host.or.ip:port
  key: personal-access-token
  user_id: 123456
```


<a id="widget-glances"></a>

---

---
title: Glances
description: Glances Widget Configuration
---

Learn more about [Glances](https://github.com/nicolargo/glances).

<img width="1614" alt="glances" src="https://github-production-user-asset-6210df.s3.amazonaws.com/82196/257382012-25648c97-2c1b-4db0-b5a5-f1509806079c.png">

_(Find the Glances information widget [here](../info/glances.md))_

The Glances widget allows you to monitor the resources (cpu, memory, diskio, sensors & processes) of host or another machine. You can have multiple instances by adding another service block.

```yaml
widget:
  type: glances
  url: http://glances.host.or.ip:port
  username: user # optional if auth enabled in Glances
  password: pass # optional if auth enabled in Glances
  version: 4 # required only if running glances v4 or higher, defaults to 3
  metric: cpu
  diskUnits: bytes # optional, bytes (default) or bbytes. Only applies to disk
  refreshInterval: 5000 # optional - in milliseconds, defaults to 1000 or more, depending on the metric
  pointsLimit: 15 # optional, defaults to 15
```

_Please note, this widget does not need an `href`, `icon` or `description` on its parent service. To achieve the same effect as the examples above, see as an example:_

```yaml
- CPU Usage:
    widget:
      type: glances
      url: http://glances.host.or.ip:port
      metric: cpu
- Network Usage:
    widget:
      type: glances
      url: http://glances.host.or.ip:port
      metric: network:enp0s25
```

## Metrics

The metric field in the configuration determines the type of system monitoring data to be displayed. Here are the supported metrics:

`info`: System information. Shows the system's hostname, OS, kernel version, CPU type, CPU usage, RAM usage and SWAP usage.

`cpu`: CPU usage. Shows how much of the system's computational resources are currently being used.

`memory`: Memory usage. Shows how much of the system's RAM is currently being used.

`process`: Top 5 processes based on CPU usage. Gives an overview of which processes are consuming the most resources.

`containers`: Docker or Kubernetes containers list. Shows up to 5 containers running on the system and their resource usage.

`network:<interface_name>`: Network data usage for the specified interface. Replace `<interface_name>` with the name of your network interface, e.g., `network:enp0s25`, as specified in glances.

`sensor:<sensor_id>`: Temperature of the specified sensor, typically used to monitor CPU temperature. Replace `<sensor_id>` with the name of your sensor, e.g., `sensor:Package id 0` as specified in glances.

`disk:<disk_id>`: Disk I/O data for the specified disk. Replace `<disk_id>` with the id of your disk, e.g., `disk:sdb`, as specified in glances.

`gpu:<gpu_id>`: GPU usage for the specified GPU. Replace `<gpu_id>` with the id of your GPU, e.g., `gpu:0`, as specified in glances.

`fs:<mnt_point>`: Disk usage for the specified mount point. Replace `<mnt_point>` with the path of your disk, e.g., `/mnt/storage`, as specified in glances.

## Views

All widgets offer an alternative to the full or "graph" view, which is the compact, or "graphless" view.

<img width="970" alt="Screenshot 2023-09-06 at 1 51 48 PM" src="https://github-production-user-asset-6210df.s3.amazonaws.com/82196/265985295-cc6b9adc-4218-4274-96ca-36c3e64de5d0.png">

To switch to the alternative "graphless" view, simply pass `chart: false` as an option to the widget, like so:

```yaml
- Network Usage:
    widget:
      type: glances
      url: http://glances.host.or.ip:port
      metric: network:enp0s25
      chart: false
```


<a id="widget-gluetun"></a>

---

---
title: Gluetun
description: Gluetun Widget Configuration
---

Learn more about [Gluetun](https://github.com/qdm12/gluetun).

!!! note

    Requires [HTTP control server options](https://github.com/qdm12/gluetun-wiki/blob/main/setup/advanced/control-server.md) to be enabled. By default this runs on port `8000`.

Allowed fields: `["public_ip", "region", "country", "port_forwarded"]`.
Default fields: `["public_ip", "region", "country"]`.

To setup authentication, follow [the official Gluetun documentation](https://github.com/qdm12/gluetun-wiki/blob/main/setup/advanced/control-server.md#authentication). Note that to use the api key method, you must add the route `GET /v1/publicip/ip` to the `routes` array in your Gluetun config.toml. Similarly, if you want to include the `port_forwarded` field, you must add the route `GET /v1/openvpn/portforwarded` (or `/v1/portforward`) to your Gluetun config.toml.

| Gluetun Version | Homepage Widget Version |
| --------------- | ----------------------- |
| < 3.40.1        | 1 (default)             |
| >= 3.40.1       | 2                       |

```yaml
widget:
  type: gluetun
  url: http://gluetun.host.or.ip:port
  key: gluetunkey # Not required if /v1/publicip/ip endpoint is configured with `auth = none`
  version: 2 # optional, default is 1
```


<a id="widget-gotify"></a>

---

---
title: Gotify
description: Gotify Widget Configuration
---

Learn more about [Gotify](https://github.com/gotify/server).

Get a Gotify client token from an existing client or create a new one on your Gotify admin page.

Allowed fields: `["apps", "clients", "messages"]`.

```yaml
widget:
  type: gotify
  url: http://gotify.host.or.ip
  key: clientoken
```


<a id="widget-grafana"></a>

---

---
title: Grafana
description: Grafana Widget Configuration
---

Learn more about [Grafana](https://github.com/grafana/grafana).

| Grafana Version | Homepage Widget Version |
| --------------- | ----------------------- |
| <= v10.4        | 1 (default)             |
| > v10.4         | 2                       |

Allowed fields: `["dashboards", "datasources", "totalalerts", "alertstriggered"]`.

```yaml
widget:
  type: grafana
  version: 2 # optional, default is 1
  alerts: alertmanager # optional, default is grafana
  url: http://grafana.host.or.ip:port
  username: username
  password: password
```


<a id="widget-hdhomerun"></a>

---

---
title: HDHomerun
description: HDHomerun Widget Configuration
---

Learn more about [HDHomerun](https://www.silicondust.com/support/downloads/).

Allowed fields: `["channels", "hd", "tunerCount", "channelNumber", "channelNetwork", "signalStrength", "signalQuality", "symbolQuality", "networkRate", "clientIP" ]`.

If more than 4 fields are provided, only the first 4 are displayed.

```yaml
widget:
  type: hdhomerun
  url: http://hdhomerun.host.or.ip
  tuner: 0 # optional - defaults to 0, used for tuner-specific fields
  fields: ["channels", "hd"] # optional - default fields shown
```


<a id="widget-headscale"></a>

---

---
title: Headscale
description: Headscale Widget Configuration
---

Learn more about [Headscale](https://headscale.net/).

You will need to generate an API access token from the [command line](https://headscale.net/ref/remote-cli/#create-an-api-key) using `headscale apikeys create` command.

To find your node ID, you can use `headscale nodes list` command.

Allowed fields: `["name", "address", "last_seen", "status"]`.

```yaml
widget:
  type: headscale
  url: http://headscale.host.or.ip:port
  nodeId: nodeid
  key: headscaleapiaccesstoken
```


<a id="widget-healthchecks"></a>

---

---
title: Health checks
description: Health checks Widget Configuration
---

Learn more about [Health Checks](https://github.com/healthchecks/healthchecks).

Specify a single check by including the `uuid` field or show the total 'up' and 'down' for all
checks by leaving off the `uuid` field.

To use the Health Checks widget, you first need to generate an API key.

1. In your project, go to project Settings on the navigation bar.
2. Click on API key (read-only) and then click _Create_.
3. Copy the API key that is generated for you.

Allowed fields: `["status", "last_ping"]` for single checks, `["up", "down"]` for total stats.

```yaml
widget:
  type: healthchecks
  url: http://healthchecks.host.or.ip:port
  key: <YOUR_API_KEY>
  uuid: <CHECK_UUID> # optional, if not included total statistics for all checks is shown
```


<a id="widget-homeassistant"></a>

---

---
title: Home Assistant
description: Home Assistant Widget Configuration
---

Learn more about [Home Assistant](https://www.home-assistant.io/).

You will need to generate a long-lived access token for an existing Home Assistant user in its profile.

Allowed fields: `["people_home", "lights_on", "switches_on"]`.

---

Up to a maximum of four custom states and/or templates can be queried via the `custom` property like in the example below.
The `custom` property will have no effect as long as the `fields` property is defined.

- `state` will query the state of the specified `entity_id`
  - state labels and values can be user defined and may reference entity attributes in curly brackets
  - if no state label is defined it will default to `"{attributes.friendly_name}"`
  - if no state value is defined it will default to `"{state} {attributes.unit_of_measurement}"`
- `template` will query the specified template, see [Home Assistant Templating](https://www.home-assistant.io/docs/configuration/templating)
  - if no template label is defined it will be empty

```yaml
widget:
  type: homeassistant
  url: http://homeassistant.host.or.ip:port
  key: access_token
  custom:
    - state: sensor.total_power
    - state: sensor.total_energy_today
      label: energy today
    - template: "{{ states.switch|selectattr('state','equalto','on')|list|length }}"
      label: switches on
    - state: weather.forecast_home
      label: wind speed
      value: "{attributes.wind_speed} {attributes.wind_speed_unit}"
```


<a id="widget-homebox"></a>

---

---
title: Homebox
description: Homebox Widget Configuration
---

Learn more about [Homebox](https://github.com/hay-kot/homebox).

Uses the same username and password used to login from the web.

The `totalValue` field will attempt to format using the currency you have configured in Homebox.

Allowed fields: `["items", "totalWithWarranty", "locations", "labels", "users", "totalValue"]`.

If more than 4 fields are provided, only the first 4 are displayed.

```yaml
widget:
  type: homebox
  url: http://homebox.host.or.ip:port
  username: username
  password: password
  fields: ["items", "locations", "totalValue"] # optional - default fields shown
```


<a id="widget-homebridge"></a>

---

---
title: Homebridge
description: Homebridge
---

Learn more about [Homebridge](https://github.com/homebridge/homebridge).

The Homebridge API is actually provided by the Config UI X plugin that has been included with Homebridge for a while, still it is required to be installed for this widget to work.

Allowed fields: `["updates", "child_bridges"]`.

```yaml
widget:
  type: homebridge
  url: http://homebridge.host.or.ip:port
  username: username
  password: password
```


<a id="widget-iframe"></a>

---

---
title: iFrame
Description: Add a custom iFrame Widget
---

A basic iFrame widget to show external content, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) for more details about some of the options.

!!! warning

    Requests made via the iFrame widget are inherently **not proxied** as they are made from the browser itself.

## Basic Example

```yaml
widget:
  type: iframe
  name: myIframe
  src: http://example.com
```

## Full Example

```yaml
widget:
  type: iframe
  name: myIframe
  src: http://example.com
  classes: h-60 sm:h-60 md:h-60 lg:h-60 xl:h-60 2xl:h-72 # optional, use tailwind height classes, see https://tailwindcss.com/docs/height
  referrerPolicy: same-origin # optional, no default
  allowPolicy: autoplay; fullscreen; gamepad # optional, no default
  allowFullscreen: false # optional, default: true
  loadingStrategy: eager # optional, default: eager
  allowScrolling: no # optional, default: yes
  refreshInterval: 2000 # optional, no default
```


<a id="widget-immich"></a>

---

---
title: Immich
description: Immich Widget Configuration
---

Learn more about [Immich](https://github.com/immich-app/immich).

| Immich Version | Homepage Widget Version |
| -------------- | ----------------------- |
| < v1.118       | 1 (default)             |
| >= v1.118      | 2                       |

Find your API key under `Account Settings > API Keys`. The key should have the
`server.statistics` permission.

Allowed fields: `["users" ,"photos", "videos", "storage"]`.

```yaml
widget:
  type: immich
  url: http://immich.host.or.ip
  key: adminapikeyadminapikeyadminapikey
  version: 2 # optional, default is 1
```


<a id="widget-jackett"></a>

---

---
title: Jackett
description: Jackett Widget Configuration
---

Learn more about [Jackett](https://github.com/Jackett/Jackett).

If Jackett has an admin password set, you must set the `password` field for the widget to work.

Allowed fields: `["configured", "errored"]`.

```yaml
widget:
  type: jackett
  url: http://jackett.host.or.ip
  password: jackettadminpassword # optional
```


<a id="widget-jdownloader"></a>

---

---
title: JDownloader
description: JDownloader Widget Configuration
---

Learn more about [JDownloader](https://jdownloader.org/).

Basic widget to show number of items in download queue, along with the queue size and current download speed.

Allowed fields: `["downloadCount", "downloadTotalBytes","downloadBytesRemaining", "downloadSpeed"]`.

```yaml
widget:
  type: jdownloader
  username: JDownloader Username
  password: JDownloader Password
  client: Name of JDownloader Instance
```


<a id="widget-jellyfin"></a>

---

---
title: Jellyfin
description: Jellyfin Widget Configuration
---

Learn more about [Jellyfin](https://github.com/jellyfin/jellyfin).

You can create an API key from inside the Jellyfin Administration Dashboard under `Advanced > API Keys`.

As of v0.6.11 the widget supports fields `["movies", "series", "episodes", "songs"]`. These blocks are disabled by default but can be enabled with the `enableBlocks` option, and the "Now Playing" feature (enabled by default) can be disabled with the `enableNowPlaying` option.

| Jellyfin Version | Homepage Widget Version |
| ---------------- | ----------------------- |
| < 10.12          | 1 (default)             |
| >= 10.12         | 2                       |

```yaml
widget:
  type: jellyfin
  url: http://jellyfin.host.or.ip:port
  key: apikeyapikeyapikeyapikeyapikey
  version: 2 # optional, default is 1
  enableBlocks: true # optional, defaults to false
  enableNowPlaying: true # optional, defaults to true
  enableUser: true # optional, defaults to false
  enableMediaControl: false # optional, defaults to true
  showEpisodeNumber: true # optional, defaults to false
  expandOneStreamToTwoRows: false # optional, defaults to true
```


<a id="widget-jellystat"></a>

---

---
title: Jellystat
description: Jellystat Widget Configuration
---

Learn more about [Jellystat](https://github.com/CyferShepard/Jellystat). The widget supports (at least) Jellystat version 1.1.6

You can create an API key from inside Jellystat at `Settings > API Key`.

Allowed fields: `["songs", "movies", "episodes", "other"]`.

```yaml
widget:
  type: jellystat
  url: http://jellystat.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
  days: 30 # optional, defaults to 30
```


<a id="widget-karakeep"></a>

---

---
title: Karakeep
description: Karakeep Widget Configuration
---

Learn more about [Karakeep](https://karakeep.app) (formerly known as Hoarder).

Generate an API key for your user at `User Settings > API Keys`.

Allowed fields: `["bookmarks", "favorites", "archived", "highlights", "lists", "tags"]` (maximum of 4).

```yaml
widget:
  type: karakeep
  url: http[s]://karakeep.host.or.ip[:port]
  key: karakeep_api_key
```


<a id="widget-kavita"></a>

---

---
title: Kavita
description: Kavita Widget Configuration
---

Learn more about [Kavita](https://github.com/Kareadita/Kavita).

Uses the same admin role username and password used to login from the web.

Allowed fields: `["seriesCount", "totalFiles"]`.

```yaml
widget:
  type: kavita
  url: http://kavita.host.or.ip:port
  username: username
  password: password
  key: kavitaapikey # Optional, e.g. if not using username and password
```


<a id="widget-komga"></a>

---

---
title: Komga
description: Komga Widget Configuration
---

Learn more about [Komga](https://github.com/gotson/komga).

Uses the same username and password used to login from the web.

Allowed fields: `["libraries", "series", "books"]`.

| Komga API Version | Homepage Widget Version |
| ----------------- | ----------------------- |
| < v2              | 1 (default)             |
| >= v2             | 2                       |

```yaml
widget:
  type: komga
  url: http://komga.host.or.ip:port
  username: username
  password: password
  key: komgaapikey # optional
```


<a id="widget-komodo"></a>

---

---
title: Komodo
description: Komodo Widget Configuration
---

This widget shows either details about all containers or stacks (if `showStacks` is true) managed by [Komodo](https://komo.do/) or the number of running servers, containers and stacks when `showSummary` is enabled.

The api key and secret can be found in the Komodo settings.

Allowed fields (max 4): `["total", "running", "stopped", "unhealthy", "unknown"]`.
Allowed fields with `showStacks` (max 4): `["total", "running", "down", "unhealthy", "unknown"]`.
Allowed fields with `showSummary`: `["servers", "stacks", "containers"]`.

```yaml
widget:
  type: komodo
  url: http://komodo.hostname.or.ip:port
  key: K-xxxxxx...
  secret: S-xxxxxx...
  showSummary: true # optional, default: false. Takes precedence over showStacks
  showStacks: true # optional, default: false
```


<a id="widget-kopia"></a>

---

---
title: Kopia
description: Kopia Widget Configuration
---

Learn more about [Kopia](https://github.com/kopia/kopia).

Allowed fields: `["status", "size", "lastrun", "nextrun"]`.

You may optionally pass values for `snapshotHost` and / or `snapshotPath` to select a specific backup source for the widget.

```yaml
widget:
  type: kopia
  url: http://kopia.host.or.ip:port
  username: username
  password: password
  snapshotHost: hostname # optional
  snapshotPath: path # optional
```


<a id="widget-lidarr"></a>

---

---
title: Lidarr
description: Lidarr Widget Configuration
---

Learn more about [Lidarr](https://github.com/Lidarr/Lidarr).

Find your API key under `Settings > General`.

Allowed fields: `["wanted", "queued", "artists"]`.

```yaml
widget:
  type: lidarr
  url: http://lidarr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-linkwarden"></a>

---

---
title: Linkwarden
description: Linkwarden Widget Configuration
---

Learn more about [Linkwarden](https://linkwarden.app/).

Allowed fields: `["links", "collections", "tags"]`.

```yaml
widget:
  type: linkwarden
  url: http://linkwarden.host.or.ip
  key: myApiKeyHere # On your Linkwarden install, go to Settings > Access Tokens. Generate a token.
```


<a id="widget-lubelogger"></a>

---

---
title: LubeLogger
description: LubeLogger Widget Configuration
---

Learn more about [LubeLogger](https://github.com/hargata/lubelog) (v1.3.7 or higher is required).

The widget comes in two 'flavors', one shows data for all vehicles or for just a specific vehicle with the `vehicleID` parameter.

Allowed fields: `["vehicles", "serviceRecords", "reminders"]`.
For the single-vehicle version: `["vehicle", "serviceRecords", "reminders", "nextReminder"]`.

```yaml
widget:
  type: lubelogger
  url: https://lubelogger.host.or.ip
  username: lubeloggerusername
  password: lubeloggerpassword
  vehicleID: 1 # optional, changes to single-vehicle version
```


<a id="widget-mailcow"></a>

---

---
title: Mailcow
description: Mailcow Widget Configuration
---

Learn more about [Mailcow](https://github.com/mailcow/mailcow-dockerized).

Allowed fields: `["domains", "mailboxes", "mails", "storage"]`.

```yaml
widget:
  type: mailcow
  url: https://mailcow.host.or.ip
  key: mailcowapikey
```


<a id="widget-mastodon"></a>

---

---
title: Mastodon
description: Mastodon Widget Configuration
---

Learn more about [Mastodon](https://github.com/mastodon/mastodon).

Use the base URL of the Mastodon instance you'd like to pull stats for. Does not require authentication as the stats are part of the public API endpoints.

Allowed fields: `["user_count", "status_count", "domain_count"]`.

```yaml
widget:
  type: mastodon
  url: https://mastodon.host.name
```


<a id="widget-mealie"></a>

---

---
title: Mealie
description: Mealie Widget Configuration
---

Learn more about [Mealie](https://github.com/mealie-recipes/mealie).

Generate a user API key under `Profile > Manage Your API Tokens > Generate`.

Allowed fields: `["recipes", "users", "categories", "tags"]`.

```yaml
widget:
  type: mealie
  url: http://mealie-frontend.host.or.ip
  key: mealieapitoken
  version: 2 # only required if version > 1, defaults to 1
```


<a id="widget-medusa"></a>

---

---
title: Medusa
description: Medusa Widget Configuration
---

Learn more about [Medusa](https://github.com/pymedusa/Medusa).

Allowed fields: `["wanted", "queued", "series"]`.

```yaml
widget:
  type: medusa
  url: http://medusa.host.or.ip:port
  key: medusaapikeyapikeyapikeyapikeyapikey
```


<a id="widget-mikrotik"></a>

---

---
title: Mikrotik
description: Mikrotik Widget Configuration
---

HTTPS may be required, [per the documentation](https://help.mikrotik.com/docs/display/ROS/REST+API#RESTAPI-Overview)

Allowed fields: `["uptime", "cpuLoad", "memoryUsed", "numberOfLeases"]`.

```yaml
widget:
  type: mikrotik
  url: https://mikrotik.host.or.ip
  username: username
  password: password
```


<a id="widget-minecraft"></a>

---

---
title: Minecraft
description: Minecraft Widget Configuration
---

Allowed fields: `["players", "version", "status"]`.

```yaml
widget:
  type: minecraft
  url: udp://minecraftserveripordomain:port
```


<a id="widget-miniflux"></a>

---

---
title: Miniflux
description: Miniflux Widget Configuration
---

Learn more about [Miniflux](https://github.com/miniflux/v2).

Api key is found under Settings > API keys

Allowed fields: `["unread", "read"]`.

```yaml
widget:
  type: miniflux
  url: http://miniflux.host.or.ip:port
  key: minifluxapikey
```


<a id="widget-mjpeg"></a>

---

---
title: MJPEG
description: MJPEG Stream Widget Configuration
---

![camera-preview](https://github.com/gethomepage/homepage/assets/4887959/dbc388d7-04a6-482c-8f36-f9534689b062)

Pass the stream URL from a service like [µStreamer](https://github.com/pikvm/ustreamer) or [camera-streamer](https://github.com/ayufan/camera-streamer).

```yaml
widget:
  type: mjpeg
  stream: http://mjpeg.host.or.ip/webcam/stream
```


<a id="widget-moonraker"></a>

---

---
title: Moonraker (Klipper)
description: Moonraker (Klipper) Widget Configuration
---

Learn more about [Moonraker](https://github.com/Arksine/moonraker).

Allowed fields: `["printer_state", "print_status", "print_progress", "layers"]`.

```yaml
widget:
  type: moonraker
  url: http://moonraker.host.or.ip:port
```

If your moonraker instance has an active authorization and your homepage ip isn't whitelisted you need to add your api key ([Authorization Documentation](https://moonraker.readthedocs.io/en/latest/web_api/#authorization)).

```yaml
widget:
  type: moonraker
  url: http://moonraker.host.or.ip:port
  key: api_keymoonraker
```


<a id="widget-mylar"></a>

---

---
title: Mylar3
description: Mylar3 Widget Configuration
---

Learn more about [Mylar3](https://github.com/MylarComics/mylar3).

API must be enabled in Mylar3 settings.

Allowed fields: `["series", "issues", "wanted"]`.

```yaml
widget:
  type: mylar
  url: http://mylar3.host.or.ip:port
  key: yourmylar3apikey
```


<a id="widget-myspeed"></a>

---

---
title: MySpeed
description: MySpeed Widget Configuration
---

Learn more about [MySpeed](https://myspeed.dev/).

Allowed fields: `["ping", "download", "upload"]`.

```yaml
widget:
  type: myspeed
  url: http://myspeed.host.or.ip:port
  password: password # only required if password is set
```


<a id="widget-navidrome"></a>

---

---
title: Navidrome
description: Navidrome Widget Configuration
---

Learn more about [Navidrome](https://github.com/navidrome/navidrome).

For detailed information about how to generate the token see http://www.subsonic.org/pages/api.jsp.

Allowed fields: no configurable fields for this widget.

```yaml
widget:
  type: navidrome
  url: http://navidrome.host.or.ip:port
  user: username
  token: token #md5(password + salt)
  salt: randomsalt
```


<a id="widget-netalertx"></a>

---

---
title: NetAlertX
description: NetAlertX (formerly PiAlert) Widget Configuration
---

Learn more about [NetAlertX](https://github.com/jokob-sk/NetAlertX).

_Note that the project was renamed from PiAlert to NetAlertX._

Allowed fields: `["total", "connected", "new_devices", "down_alerts"]`.

Provide the `API_TOKEN` (f.k.a. `SYNC_api_token`) as the `key` in your config.

| NetAlertX Version | Homepage Widget Version |
| ----------------- | ----------------------- |
| < v26.1.17        | 1 (default)             |
| > v26.1.17        | 2                       |

```yaml
widget:
  type: netalertx
  url: http://ip:port # use backend port for widget version 2+
  key: yournetalertxapitoken
  version: 2 # optional, default is 1
```


<a id="widget-netdata"></a>

---

---
title: Netdata
description: Netdata Widget Configuration
---

Learn more about [Netdata](https://github.com/netdata/netdata).

Allowed fields: `["warnings", "criticals"]`.

```yaml
widget:
  type: netdata
  url: http://netdata.host.or.ip
```


<a id="widget-nextcloud"></a>

---

---
title: Nextcloud
description: Nextcloud Widget Configuration
---

Learn more about [Nextcloud](https://github.com/nextcloud).

Use username & password, or the `NC-Token` key. Information about the token can be found under **Settings** > **System**. If both are provided, NC-Token will be used.

Allowed fields: `["cpuload", "memoryusage", "freespace", "activeusers", "numfiles", "numshares"]`.

Note "cpuload" and "memoryusage" were deprecated in v0.6.18 and a maximum of 4 fields can be displayed.

```yaml
widget:
  type: nextcloud
  url: https://nextcloud.host.or.ip:port
  key: token
```

```yaml
widget:
  type: nextcloud
  url: https://nextcloud.host.or.ip:port
  username: username
  password: password
```


<a id="widget-nextdns"></a>

---

---
title: NextDNS
description: NextDNS Widget Configuration
---

Learn more about [NextDNS](https://nextdns.io/).

Api key is found under Account > API, profile ID is found under Setup > Endpoints > ID

```yaml
widget:
  type: nextdns
  profile: profileid
  key: yourapikeyhere
```


<a id="widget-nginx-proxy-manager"></a>

---

---
title: Nginx Proxy Manager
description: Nginx Proxy Manager Widget Configuration
---

Learn more about [Nginx Proxy Manager](https://nginxproxymanager.com/).

Login with the same admin username and password used to access the web UI.

Allowed fields: `["enabled", "disabled", "total"]`.

```yaml
widget:
  type: npm
  url: http://npm.host.or.ip
  username: admin_username
  password: admin_password
```


<a id="widget-ntfy"></a>

---

---
title: ntfy
description: ntfy Widget Configuration
---

Learn more about [ntfy](https://github.com/binwiederhier/ntfy).

This widget shows the latest notification for a ntfy topic, including the title or body, priority level, and when it was received. Works with both self-hosted ntfy instances and the public [ntfy.sh](https://ntfy.sh) service.

Allowed fields: `["title", "message", "priority", "lastReceived", "tags"]`.

Default fields: `["title", "message", "priority", "lastReceived"]`.

If more than 4 fields are provided, only the first 4 are displayed.

## Authentication

ntfy supports both public and private topics. For private instances or access-controlled topics, you can authenticate using either a **Bearer token** (ntfy access token) or **Basic auth** (username/password).

| Auth Method  | Config Fields                  | Notes                             |
| ------------ | ------------------------------ | --------------------------------- |
| None         | _(omit key/username/password)_ | For public topics                 |
| Bearer token | `key`                          | ntfy access tokens (`tk_` prefix) |
| Basic auth   | `username` + `password`        | Username/password credentials     |

See the [ntfy documentation](https://docs.ntfy.sh/config/#access-control) for details on access control.

```yaml
widget:
  type: ntfy
  url: http://ntfy.host.or.ip:port # required
  topic: mytopic # required
  # key: tk_accesstoken # optional — for token auth
  # username: user # optional — for basic auth
  # password: pass # optional — for basic auth
```


<a id="widget-nzbget"></a>

---

---
title: NZBget
description: NZBget Widget Configuration
---

Learn more about [NZBget](https://github.com/nzbget/nzbget).

This widget uses the same authentication method as your browser when logging in (HTTP Basic Auth), and is often referred to as the ControlUsername and ControlPassword inside of Nzbget documentation.

Allowed fields: `["rate", "remaining", "downloaded"]`.

```yaml
widget:
  type: nzbget
  url: http://nzbget.host.or.ip
  username: controlusername
  password: controlpassword
```


<a id="widget-octoprint"></a>

---

---
title: OctoPrint
description: OctoPrintWidget Configuration
---

Learn more about [OctoPrint](https://octoprint.org/).

Allowed fields: `["printer_state", "temp_tool", "temp_bed", "job_completion"]`.

```yaml
widget:
  type: octoprint
  url: http://octoprint.host.or.ip:port
  key: youroctoprintapikey
```


<a id="widget-omada"></a>

---

---
title: Omada
description: Omada Widget Configuration
---

The widget supports controller versions 3, 4, 5 and 6.

Allowed fields: `["connectedAp", "activeUser", "alerts", "connectedGateways", "connectedSwitches"]`.

```yaml
widget:
  type: omada
  url: http://omada.host.or.ip:port
  username: username
  password: password
  site: sitename
```


<a id="widget-ombi"></a>

---

---
title: Ombi
description: Ombi Widget Configuration
---

Learn more about [Ombi](https://github.com/Ombi-app/Ombi).

Find your API key under `Settings > Configuration > General`.

Allowed fields: `["pending", "approved", "available"]`.

```yaml
widget:
  type: ombi
  url: http://ombi.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-opendtu"></a>

---

---
title: OpenDTU
description: OpenDTU Widget
---

Learn more about [OpenDTU](https://github.com/tbnobody/OpenDTU).

Allowed fields: `["yieldDay", "relativePower", "absolutePower", "limit"]`.

```yaml
widget:
  type: opendtu
  url: http://opendtu.host.or.ip
```


<a id="widget-openmediavault"></a>

---

---
title: OpenMediaVault
description: OpenMediaVault Widget Configuration
---

Learn more about [OpenMediaVault](https://www.openmediavault.org/).

Provides useful information from your OpenMediaVault

```yaml
widget:
  type: openmediavault
  url: http://omv.host.or.ip
  username: admin
  password: pass
  method: services.getStatus # required
```

## Methods

The method field determines the type of data to be displayed and is required. Supported methods:

`services.getStatus`: Shows status of running services. Allowed fields: `["running", "stopped", "total"]`

`smart.getListBg`: Shows S.M.A.R.T. status from disks. Allowed fields: `["passed", "failed"]`

`downloader.getDownloadList`: Displays the number of tasks from the Downloader plugin currently being downloaded and total. Allowed fields: `["downloading", "total"]`


<a id="widget-openwrt"></a>

---

---
title: OpenWRT
description: OpenWRT widget configuration
---

Learn more about [OpenWRT](https://openwrt.org/).

Provides information from OpenWRT

```yaml
widget:
  type: openwrt
  url: http://host.or.ip
  username: homepage
  password: pass
  interfaceName: eth0 # optional
```

## Interface

Setting `interfaceName` (e.g. eth0) will display information for that particular device, otherwise the widget will display general system info.

## Authorization

In order for homepage to access the OpenWRT RPC endpoints you will need to [create an ACL](https://openwrt.org/docs/techref/ubus#acls) and [new user](https://openwrt.org/docs/techref/ubus#authentication) in OpenWRT.

Create an ACL named `homepage.json` in `/usr/share/rpcd/acl.d/`, the following permissions will suffice:

```json
{
  "homepage": {
    "description": "Homepage widget",
    "read": {
      "ubus": {
        "network.interface.wan": ["status"],
        "network.interface.lan": ["status"],
        "network.device": ["status"],
        "system": ["info"]
      }
    }
  }
}
```

Create a `crypt(5)` password hash using the following command in the OpenWRT shell:

```sh
uhttpd -m "<somepassphrase>"
```

Then add a user that will use the ACL and hashed password in `/etc/config/rpcd`:

```
config login
        option username 'homepage'
        option password '<hashedpassword>'
        list read homepage
```

This username and password will be used in Homepage's services.yaml to grant access.


<a id="widget-opnsense"></a>

---

---
title: OPNSense
description: OPNSense Widget Configuration
---

Learn more about [OPNSense](https://opnsense.org/).

The API key & secret can be generated via the webui by creating a new user at _System/Access/Users_. Ensure "Generate a scrambled password to prevent local database logins for this user" is checked and then edit the effective privileges selecting **only**:

- Diagnostics: System Activity
- Status: Traffic Graph / Reporting: Traffic (OPNSENSE 24.7.x)

Finally, create a new API key which will download an `apikey.txt` file with your key and secret in it. Use the values as the username and password fields, respectively, in your homepage config.

Allowed fields: `["cpu", "memory", "wanUpload", "wanDownload"]`.

```yaml
widget:
  type: opnsense
  url: http://opnsense.host.or.ip
  username: key
  password: secret
  wan: opt1 # optional, defaults to wan
```


<a id="widget-pangolin"></a>

---

---
title: Pangolin
description: Pangolin Widget Configuration
---

Learn more about [Pangolin](https://github.com/fosrl/pangolin).

This widget shows sites (online/total), resources (healthy/total), targets (healthy/total), and traffic statistics for a Pangolin organization. A resource is considered healthy if at least one of its targets is healthy, or if it has no targets.

Allowed fields: `["sites", "resources", "targets", "traffic", "in", "out"]` (maximum of 4).

```yaml
widget:
  type: pangolin
  url: https://api.pangolin.net
  key: your-api-key
  org: your-org-id
```

Find your organization ID in the URL when logged in (e.g., `https://app.pangolin.net/{org-id}/...`).

## API Key Setup

Create an API key with the following permissions:

- **List Sites**
- **List Resources**

**Self-Hosted:** Enable the [Integration API](https://docs.pangolin.net/self-host/advanced/integration-api) in your Pangolin configuration before creating the key.


<a id="widget-paperlessngx"></a>

---

---
title: Paperless-ngx
description: Paperless-ngx Widget Configuration
---

Learn more about [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx).

Use username & password, or the token key. Information about the token can be found in the [Paperless-ngx API documentation](https://docs.paperless-ngx.com/api/#authorization). If both are provided, the token will be used.

Allowed fields: `["total", "inbox"]`.

```yaml
widget:
  type: paperlessngx
  url: http://paperlessngx.host.or.ip:port
  username: username
  password: password
```

```yaml
widget:
  type: paperlessngx
  url: http://paperlessngx.host.or.ip:port
  key: token
```


<a id="widget-peanut"></a>

---

---
title: PeaNUT
description: PeaNUT Widget Configuration
---

Learn more about [PeaNUT](https://github.com/Brandawg93/PeaNUT).

This widget adds support for [Network UPS Tools](https://networkupstools.org/) via a third party tool, [PeaNUT](https://github.com/Brandawg93/PeaNUT).

The default ups name is `ups`. To configure more than one ups, you must create multiple peanut services.

Allowed fields: `["battery_charge", "ups_load", "ups_status"]`.

!!! note

    This widget requires an additional tool, [PeaNUT](https://github.com/Brandawg93/PeaNUT), as noted. Other projects exist to achieve similar results using a `customapi` widget, for example [NUTCase](https://github.com/ArthurMitchell42/nutcase#using-nutcase-homepage).

```yaml
widget:
  type: peanut
  url: http://peanut.host.or.ip:port
  key: nameofyourups
  username: username # only needed if set
  password: password # only needed if set
```


<a id="widget-pfsense"></a>

---

---
title: pfSense
description: pfSense Widget Configuration
---

Learn more about [pfSense](https://github.com/pfsense/pfsense).

This widget requires the installation of the [pfsense-api](https://github.com/jaredhendrickson13/pfsense-api) which is a 3rd party package for pfSense routers.

Once pfSense API is installed, you can set the API to be read-only in System > API > Settings.

There are two currently supported authentication modes: 'Local Database' and 'API Key' (v2) / 'API Token' (v1). For 'Local Database', use `username` and `password` with the credentials of an admin user. The specifics of using the API key / token depend on the version of the pfSense API, see the config examples below. Do not use both headers and username / password.

The interface to monitor is defined by updating the `wan` parameter. It should be referenced as it is shown under Interfaces > Assignments in pfSense.

Load is returned instead of cpu utilization. This is a limitation in the pfSense API due to the complexity of this calculation. This may become available in future versions.

Allowed fields: `["load", "memory", "temp", "wanStatus", "wanIP", "disk"]` (maximum of 4)

For version 2:

```yaml
widget:
  type: pfsense
  url: http://pfsense.host.or.ip:port
  username: user # optional, or API key
  password: pass # optional, or API key
  headers: # optional, or username/password
    X-API-Key: key
  wan: igb0
  version: 2 # optional, defaults to 1 for api v1
  fields: ["load", "memory", "temp", "wanStatus"] # optional
```

For version 1:

```yaml
headers: # optional, or username/password
  Authorization: client_id client_token # obtained from pfSense API
version: 1
```


<a id="widget-photoprism"></a>

---

---
title: PhotoPrism
description: PhotoPrism Widget Configuration
---

Learn more about [PhotoPrism](https://github.com/photoprism/photoprism).

Authentication is possible via [app passwords](https://docs.photoprism.app/user-guide/settings/account/#apps-and-devices) or username/password.

Allowed fields: `["albums", "photos", "videos", "people"]`.

```yaml
widget:
  type: photoprism
  url: http://photoprism.host.or.ip:port
  username: admin # required only if using username/password
  password: password # required only if using username/password
  key: # required only if using app passwords
```


<a id="widget-pihole"></a>

---

---
title: PiHole
description: PiHole Widget Configuration
---

Learn more about [PiHole](https://github.com/pi-hole/pi-hole).

Allowed fields: `["queries", "blocked", "blocked_percent", "gravity"]`.

Note: by default the "blocked" and "blocked_percent" fields are merged e.g. "1,234 (15%)" but explicitly including the "blocked_percent" field will change them to display separately.

```yaml
widget:
  type: pihole
  url: http://pi.hole.or.ip
  version: 6 # required if running v6 or higher, defaults to 5
  key: yourpiholeapikey # optional, in v6 can be your password or app password
```


<a id="widget-plantit"></a>

---

---
title: Plant-it
description: Plant-it Widget Configuration
---

Learn more about [Plantit](https://github.com/MDeLuise/plant-it).

API key can be created from the REST API.

Allowed fields: `["events", "plants", "photos", "species"]`.

```yaml
widget:
  type: plantit
  url: http://plant-it.host.or.ip:port # api port
  key: plantit-api-key
```


<a id="widget-plex-tautulli"></a>

---

---
title: Tautulli (Plex)
description: Tautulli Widget Configuration
---

Learn more about [Tautulli](https://github.com/Tautulli/Tautulli).

Provides detailed information about currently active streams. You can find the API key from inside Tautulli at `Settings > Web Interface > API`.

Allowed fields: no configurable fields for this widget.

```yaml
widget:
  type: tautulli
  url: http://tautulli.host.or.ip:port
  key: apikeyapikeyapikeyapikeyapikey
  enableUser: true # optional, defaults to false
  showEpisodeNumber: true # optional, defaults to false
  expandOneStreamToTwoRows: false # optional, defaults to true
```


<a id="widget-plex"></a>

---

---
title: Plex
description: Plex Widget Configuration
---

Learn more about [Plex](https://www.plex.tv/).

The core Plex API is somewhat limited but basic info regarding library sizes and the number of active streams is supported. For more detailed info regarding active streams see the [Plex Tautulli widget](plex-tautulli.md).

Allowed fields: `["streams", "albums", "movies", "tv"]`.

```yaml
widget:
  type: plex
  url: http://plex.host.or.ip:32400
  key: mytokenhere # see https://www.plexopedia.com/plex-media-server/general/plex-token/
```


<a id="widget-portainer"></a>

---

---
title: Portainer
description: Portainer Widget Configuration
---

Learn more about [Portainer](https://github.com/portainer/portainer).

You'll need to make sure you have the correct environment set for the integration to work properly. From the Environments section inside of Portainer, click the one you'd like to connect to and observe the ID at the end of the URL (should be), something like `#!/endpoints/1`, here `1` is the value to set as the `env` value. In order to generate an API key, please follow the steps outlined here https://docs.portainer.io/api/access.

Allowed fields:

- For Docker mode (default): `["running", "stopped", "total"]`
- For Kubernetes mode (`kubernetes: true`): `["applications", "services", "namespaces"]`

```yaml
widget:
  type: portainer
  url: https://portainer.host.or.ip:9443
  env: 1
  kubernetes: true # optional, defaults to false
  key: ptr_accesskeyaccesskeyaccesskeyaccesskey
```


<a id="widget-prometheus"></a>

---

---
title: Prometheus
description: Prometheus Widget Configuration
---

Learn more about [Prometheus](https://github.com/prometheus/prometheus).

Allowed fields: `["targets_up", "targets_down", "targets_total"]`.

```yaml
widget:
  type: prometheus
  url: http://prometheushost:port
```


<a id="widget-prometheusmetric"></a>

---

---
title: Prometheus Metric
description: Prometheus Metric Widget Configuration
---

Learn more about [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/).

This widget can show metrics for your service defined by PromQL queries which are requested from a running Prometheus instance.

Quries can be defined in the `metrics` array of the widget along with a label to be used to present the metric value. You can optionally specify a global `refreshInterval` in milliseconds and/or define the `refreshInterval` per metric. Inside the optional `format` object of a metric various formatting styles and transformations can be applied (see below).

```yaml
widget:
  type: prometheusmetric
  url: https://prometheus.host.or.ip
  refreshInterval: 10000 # optional - in milliseconds, defaults to 10s
  metrics:
    - label: Metric 1
      query: alertmanager_alerts{state="active"}
    - label: Metric 2
      query: apiserver_storage_size_bytes{node="mynode"}
      format:
        type: bytes
    - label: Metric 3
      query: avg(prometheus_notifications_latency_seconds)
      format:
        type: number
        suffix: s
        options:
          maximumFractionDigits: 4
    - label: Metric 4
      query: time()
      refreshInterval: 1000 # will override global refreshInterval
      format:
        type: date
        scale: 1000
        options:
          timeStyle: medium
```

## Formatting

Supported values for `format.type` are `text`, `number`, `percent`, `bytes`, `bits`, `bbytes`, `bbits`, `byterate`, `bibyterate`, `bitrate`, `bibitrate`, `date`, `duration`, `relativeDate`, and `text` which is the default.

The `dateStyle` and `timeStyle` options of the `date` format are passed directly to [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) and the `style` and `numeric` options of `relativeDate` are passed to [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat). For the `number` format, options of [Intl.NumberFormat](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat) can be used, e.g. `maximumFractionDigits` or `minimumFractionDigits`.

### Data Transformation

You can manipulate your metric value with the following tools: `scale`, `prefix` and `suffix`, for example:

```yaml
- query: my_custom_metric{}
  label: Metric 1
  format:
    type: number
    scale: 1000 # multiplies value by a number or fraction string e.g. 1/16
- query: my_custom_metric{}
  label: Metric 2
  format:
    type: number
    prefix: "$" # prefixes value with given string
- query: my_custom_metric{}
  label: Metric 3
  format:
    type: number
    suffix: "€" # suffixes value with given string
```


<a id="widget-prowlarr"></a>

---

---
title: Prowlarr
description: Prowlarr Widget Configuration
---

Learn more about [Prowlarr](https://github.com/Prowlarr/Prowlarr).

Find your API key under `Settings > General`.

Allowed fields: `["numberOfGrabs", "numberOfQueries", "numberOfFailGrabs", "numberOfFailQueries"]`.

```yaml
widget:
  type: prowlarr
  url: http://prowlarr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-proxmox"></a>

---

---
title: Proxmox
description: Proxmox Widget Configuration
---

Learn more about [Proxmox](https://www.proxmox.com/en/).

This widget shows the running and total counts of both QEMU VMs and LX Containers in the Proxmox cluster. It also shows the CPU and memory usage of the first node in the cluster.

See the [Proxmox configuration documentation](../../configs/proxmox.md#create-token) for details on creating API tokens.

Use `username@pam!Token ID` as the `username` (e.g `api@pam!homepage`) setting and `Secret` as the `password` setting.

Allowed fields: `["vms", "lxc", "resources.cpu", "resources.mem"]`.

You can set the optional `node` setting when you want to show metrics for a single node. By default it will show the average for the complete cluster.

```yaml
widget:
  type: proxmox
  url: https://proxmox.host.or.ip:8006
  username: api_token_id
  password: api_token_secret
  node: pve-1 # optional
```


<a id="widget-proxmoxbackupserver"></a>

---

---
title: Proxmox Backup Server
description: Proxmox Backup Server Widget Configuration
---

Learn more about [Proxmox Backup Server](https://www.proxmox.com/en/proxmox-backup-server/overview).

Create a user and an API token similar to the [Proxmox VE description](proxmox.md). The "Audit" role is required for both the user and token (not group).

Allowed fields: `["datastore_usage", "failed_tasks_24h", "cpu_usage", "memory_usage"]`.

```yaml
widget:
  type: proxmoxbackupserver
  url: https://proxmoxbackupserver.host:port
  username: api_token_id
  password: api_token_secret
  datastore: datastore_name #optional; if ommitted, will display a combination of all datastores used / total
```


<a id="widget-pterodactyl"></a>

---

---
title: Pterodactyl
description: Pterodactyl Widget Configuration
---

Learn more about [Pterodactyl](https://github.com/pterodactyl).

Allowed fields: `["nodes", "servers"]`.

```yaml
widget:
  type: pterodactyl
  url: http://pterodactylhost:port
  key: pterodactylapikey
```


<a id="widget-pyload"></a>

---

---
title: Pyload
description: Pyload Widget Configuration
---

Learn more about [Pyload](https://github.com/pyload/pyload).

Allowed fields: `["speed", "active", "queue", "total"]`.

```yaml
widget:
  type: pyload
  url: http://pyload.host.or.ip:port
  username: username
  password: password # only needed if set
  key: pyloadapikey # only needed if set, takes precedence over username/password
```


<a id="widget-qbittorrent"></a>

---

---
title: qBittorrent
description: qBittorrent Widget Configuration
---

Learn more about [qBittorrent](https://github.com/qbittorrent/qBittorrent).

Uses the same username and password used to login from the web.

Allowed fields: `["leech", "download", "seed", "upload"]`.

```yaml
widget:
  type: qbittorrent
  url: http://qbittorrent.host.or.ip
  username: username
  password: password
  enableLeechProgress: true # optional, defaults to false
  enableLeechSize: true # optional, defaults to false
```


<a id="widget-qnap"></a>

---

---
title: QNAP
description: QNAP Widget Configuration
---

Learn more about [QNAP](https://www.qnap.com).

Allowed fields: `["cpuUsage", "memUsage", "systemTempC", "poolUsage", "volumeUsage"]`.

```yaml
widget:
  type: qnap
  url: http://qnap.host.or.ip:port
  username: user
  password: pass
```

If the QNAP device has multiple volumes, the _poolUsage_ will be a sum of all volumes.

If only a single volume needs to be tracked, add the following to your configuration and the Widget will track this as _volumeUsage_:

```yaml
volume: Volume Name From QNAP
```


<a id="widget-radarr"></a>

---

---
title: Radarr
description: Radarr Widget Configuration
---

Learn more about [Radarr](https://github.com/Radarr/Radarr).

Find your API key under `Settings > General`.

Allowed fields: `["wanted", "missing", "queued", "movies"]`.

A detailed queue listing is disabled by default, but can be enabled with the `enableQueue` option.

```yaml
widget:
  type: radarr
  url: http://radarr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
  enableQueue: true # optional, defaults to false
```


<a id="widget-readarr"></a>

---

---
title: Readarr
description: Readarr Widget Configuration
---

Learn more about [Readarr](https://github.com/Readarr/Readarr).

Find your API key under `Settings > General`.

Allowed fields: `["wanted", "queued", "books"]`.

```yaml
widget:
  type: readarr
  url: http://readarr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-romm"></a>

---

---
title: Romm
description: Romm Widget Configuration
---

Allowed fields: `["platforms", "totalRoms", "saves", "states", "screenshots", "totalfilesize"]`.
If more than (4) fields are provided, only the first (4) will be used.

```yaml
widget:
  type: romm
  url: http://romm.host.or.ip
  fields: ["platforms", "totalRoms", "saves", "states"] # optional - default fields shown
```


<a id="widget-rutorrent"></a>

---

---
title: ruTorrent
description: ruTorrent Widget Configuration
---

Learn more about [ruTorrent](https://github.com/Novik/ruTorrent).

This requires the `httprpc` plugin to be installed and enabled, and is part of the default ruTorrent plugins. If you have not explicitly removed or disable this plugin, it should be available.

Allowed fields: `["active", "upload", "download"]`.

```yaml
widget:
  type: rutorrent
  url: http://rutorrent.host.or.ip
  username: username # optional, false if not used
  password: password # optional, false if not used
```


<a id="widget-sabnzbd"></a>

---

---
title: SABnzbd
description: SABnzbd Widget Configuration
---

Learn more about [SABnzbd](https://github.com/sabnzbd/sabnzbd).

Find your API key under `Config > General`.

Allowed fields: `["rate", "queue", "timeleft"]`.

```yaml
widget:
  type: sabnzbd
  url: http://sabnzbd.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-scrutiny"></a>

---

---
title: Scrutiny
description: Scrutiny Widget Configuration
---

Learn more about [Scrutiny](https://github.com/AnalogJ/scrutiny).

Allowed fields: `["passed", "failed", "unknown"]`.

```yaml
widget:
  type: scrutiny
  url: http://scrutiny.host.or.ip
```


<a id="widget-seerr"></a>

---

---
title: Seerr Widget
description: Seerr Widget Configuration
---

Learn more about [Seerr](https://github.com/seerr-team/seerr).

Find your API key under `Settings > General > API Key`.

_Jellyseerr and Overseerr merged into Seerr. Use `type: seerr` (legacy `type: jellyseerr` and `type: overseerr` are aliased)._

Allowed fields: `["pending", "approved", "available", "completed", "processing", "issues"]`.
Default fields: `["pending", "approved", "completed"]`.

```yaml
widget:
  type: seerr
  url: http://seerr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-slskd"></a>

---

---
title: Slskd
description: Slskd Widget Configuration
---

Learn more about [Slskd](https://github.com/slskd/slskd).

Generate an API key for slskd with `openssl rand -base64 48`.
Add it to your `path/to/config/slskd.yml` in `web > authentication > api_keys`:

```yaml
homepage_widget:
  key: <generated key>
  role: readonly
  cidr: <homepage subnet>
```

Allowed fields: `["slskStatus", "updateStatus", "downloads", "uploads", "sharedFiles"]` (maximum of 4).

```yaml
widget:
  type: slskd
  url: http[s]://slskd.host.or.ip[:5030]
  key: generatedapikey
```


<a id="widget-sonarr"></a>

---

---
title: Sonarr
description: Sonarr Widget Configuration
---

Learn more about [Sonarr](https://github.com/Sonarr/Sonarr).

Find your API key under `Settings > General`.

Allowed fields: `["wanted", "queued", "series"]`.

A detailed queue listing is disabled by default, but can be enabled with the `enableQueue` option.

```yaml
widget:
  type: sonarr
  url: http://sonarr.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
  enableQueue: true # optional, defaults to false
```


<a id="widget-sparkyfitness"></a>

---

---
title: SparkyFitness
description: SparkyFitness Widget Configuration
---

Learn more about [SparkyFitness](https://github.com/CodeWithCJ/SparkyFitness).

Allowed fields: `["eaten", "burned", "remaining", "steps"]`.

```yaml
widget:
  type: sparkyfitness
  url: http://sparkyfitness.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-speedtest-tracker"></a>

---

---
title: Speedtest Tracker
description: Speedtest Tracker Widget Configuration
---

Learn more about [Speedtest Tracker](https://github.com/alexjustesen/speedtest-tracker). or
[Speedtest Tracker](https://github.com/henrywhitaker3/Speedtest-Tracker)

No extra configuration is required.

Version 1 of the widget is compatible with both [alexjustesen/speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker) and [henrywhitaker3/Speedtest-Tracker](https://github.com/henrywhitaker3/Speedtest-Tracker), while version 2 is only compatible with [alexjustesen/speedtest-tracker](https://github.com/alexjustesen/speedtest-tracker).

| Speedtest Version (AJ) | Speedtest Version (HW) | Homepage Widget Version |
| ---------------------- | ---------------------- | ----------------------- |
| < 1.2.1                | ≤ 1.12.0               | 1 (default)             |
| >= 1.2.1               | N/A                    | 2                       |

Allowed fields: `["download", "upload", "ping"]`.

```yaml
widget:
  type: speedtest
  url: http://speedtest.host.or.ip
  version: 1 # optional, default is 1
  key: speedtestapikey # required for version 2
  bitratePrecision: 3 # optional, default is 0
```


<a id="widget-spoolman"></a>

---

---
title: Spoolman
description: Spoolman Widget Configuration
---

Learn more about [Spoolman](https://github.com/Donkie/Spoolman).

4 spools are displayed by default. If more than 4 spools are configured in spoolman you can use the spoolIds configuration option to control which are displayed.

```yaml
widget:
  type: spoolman
  url: http://spoolman.host.or.ip
  spoolIds: [1, 2, 3, 4] # optional
```


<a id="widget-stash"></a>

---

---
title: Stash
description: Stash Widget Configuration
---

Learn more about [Stash](https://github.com/stashapp/stash).

Find your API key from inside Stash at `Settings > Security > API Key`. Note that the API key is only required if your Stash instance has login credentials.

Allowed fields: `["scenes", "scenesPlayed", "playCount", "playDuration", "sceneSize", "sceneDuration", "images", "imageSize", "galleries", "performers", "studios", "movies", "tags", "oCount"]`.

If more than 4 fields are provided, only the first 4 are displayed.

```yaml
widget:
  type: stash
  url: http://stash.host.or.ip
  key: stashapikey
  fields: ["scenes", "images"] # optional - default fields shown
```


<a id="widget-stocks"></a>

---

---
title: Stocks
description: Stocks Service Widget Configuration
---

_(Find the Stocks information widget [here](../info/stocks.md))_

The widget includes:

- US stock market status
- Current price of provided stock symbol
- Change in price of stock symbol for the day.

Finnhub.io is currently the only supported provider for the stocks widget.
You can sign up for a free api key at [finnhub.io](https://finnhub.io).
You are encouraged to read finnhub.io's
[terms of service/privacy policy](https://finnhub.io/terms-of-service) before
signing up.

Allowed fields: no configurable fields for this widget.

You must set `finnhub` as a provider in your `settings.yaml`:

```yaml
providers:
  finnhub: yourfinnhubapikeyhere
```

Next, configure the stocks widget in your `services.yaml`:

The service widget allows for up to 28 items in the watchlist. You may get rate
limited if using the information and service widgets together.

```yaml
widget:
  type: stocks
  provider: finnhub
  showUSMarketStatus: true # optional, defaults to true
  watchlist:
    - GME
    - AMC
    - NVDA
    - TSM
    - BRK.A
    - TSLA
    - AAPL
    - MSFT
    - AMZN
    - BRK.B
```


<a id="widget-suwayomi"></a>

---

---
title: Suwayomi
description: Suwayomi Widget Configuration
---

Learn more about [Suwayomi](https://github.com/Suwayomi/Suwayomi-Server).

Allowed fields: ["download", "nondownload", "read", "unread", "downloadedread", "downloadedunread", "nondownloadedread", "nondownloadedunread"]

The widget defaults to the first four above. If more than four fields are provided, only the first 4 are displayed.
Category IDs can be obtained from the url when navigating to it, `?tab={categoryID}`.

```yaml
widget:
  type: suwayomi
  url: http://suwayomi.host.or.ip
  username: username #optional
  password: password #optional
  category: 0 #optional, defaults to all categories
```


<a id="widget-swagdashboard"></a>

---

---
title: SWAG Dashboard
description: SWAG Dashboard Widget Configuration
---

Learn more about [SWAG Dashboard](https://github.com/linuxserver/docker-mods/tree/swag-dashboard).

Allowed fields: `["proxied", "auth", "outdated", "banned"]`.

```yaml
widget:
  type: swagdashboard
  url: http://swagdashboard.host.or.ip:adminport # default port is 81
```


<a id="widget-syncthing-relay-server"></a>

---

---
title: Syncthing Relay Server
description: Syncthing Relay Server Widget Configuration
---

Learn more about [Syncthing Relay Server](https://github.com/syncthing/syncthing).

Pulls stats from the [relay server](https://docs.syncthing.net/users/strelaysrv.html). [See here](https://github.com/gethomepage/homepage/pull/230#issuecomment-1253053472) for more information on configuration.

Allowed fields: `["numActiveSessions", "numConnections", "bytesProxied"]`.

```yaml
widget:
  type: strelaysrv
  url: http://syncthing.host.or.ip:22070
```


<a id="widget-tailscale"></a>

---

---
title: Tailscale
description: Tailscale Widget Configuration
---

Learn more about [Tailscale](https://github.com/tailscale/tailscale).

You will need to generate an API access token from the [keys page](https://login.tailscale.com/admin/settings/keys) on the Tailscale dashboard.

To find your device ID, go to the [machine overview page](https://login.tailscale.com/admin/machines) and select your machine. In the "Machine Details" section, copy your `ID`. It will end with `CNTRL`.

Allowed fields: `[ "address", "last_seen", "expires", "user", "hostname", "name", "client_version", "os", "created", "authorized", "is_external", "update_available", "tags" ]`.

```yaml
widget:
  type: tailscale
  deviceid: deviceid
  key: tailscalekey
```


<a id="widget-tandoor"></a>

---

---
title: Tandoor
description: Tandoor Widget Configuration
---

Generate a user API key under `Settings > API  > Generate`. For the token's scope, use `read`.

Allowed fields: `["users", "recipes", "keywords"]`.

```yaml
widget:
  type: tandoor
  url: http://tandoor-frontend.host.or.ip
  key: tandoor-api-token
```


<a id="widget-tdarr"></a>

---

---
title: Tdarr
description: Tdarr Widget Configuration
---

Learn more about [Tdarr](https://github.com/HaveAGitGat/Tdarr).

Allowed fields: `["queue", "processed", "errored", "saved"]`.

```yaml
widget:
  type: tdarr
  url: http://tdarr.host.or.ip
  key: tdarrapikey # optional
```


<a id="widget-technitium"></a>

---

---
title: Technitium DNS Server
description: Technitium DNS Server Widget Configuration
---

Learn more about [Technitium DNS Server](https://technitium.com/dns/).

Allowed fields (up to 4): `["totalQueries","totalNoError","totalServerFailure","totalNxDomain","totalRefused","totalAuthoritative","totalRecursive","totalCached","totalBlocked","totalDropped","totalClients"]`.

Defaults to: `["totalQueries", "totalAuthoritative", "totalCached", "totalServerFailure"]`

```yaml
widget:
  type: technitium
  url: <url to dns server>
  key: biglongapitoken
  node: <node dns name or cluster> # optional, defaults to current node
  range: LastDay # optional, defaults to LastHour
```

#### API Key

This can be generated via the Technitium DNS Dashboard, and should be generated from a special API specific user.

#### Node

`node` value determines which Technitium cluster node the statistics are returned for. Specifying a value of `cluster` returns aggregrate stats for all nodes in the cluster. Specify a node domain name to return specific node stats, no value returns stats for the node against which the API is executed.

#### Range

`range` value determines how far back of statistics to pull data for. The value comes directly from Technitium API documentation found [here](https://github.com/TechnitiumSoftware/DnsServer/blob/master/APIDOCS.md#dashboard-api-calls), defined as `"type"`. The value can be one of: `LastHour`, `LastDay`, `LastWeek`, `LastMonth`, `LastYear`.


<a id="widget-tracearr"></a>

---

---
title: Tracearr
description: Tracearr Widget Configuration
---

Learn more about [Tracearr](https://www.tracearr.com/).

Provides detailed information about currently active streams across multiple servers.

Allowed fields (for summary view): `["streams", "transcodes", "directplay", "bitrate"]`.

```yaml
widget:
  type: tracearr
  url: http://tracearr.host.or.ip:3000
  key: apikeyapikeyapikeyapikeyapikey
  view: both # optional, "summary", "details", or "both", defaults to "details"
  enableUser: true # optional, defaults to false
  showEpisodeNumber: true # optional, defaults to false
  expandOneStreamToTwoRows: false # optional, defaults to true
```


<a id="widget-traefik"></a>

---

---
title: Traefik
description: Traefik Widget Configuration
---

Learn more about [Traefik](https://github.com/traefik/traefik).

No extra configuration is required.
If your traefik install requires authentication, include the username and password used to login to the web interface.

Allowed fields: `["routers", "services", "middleware"]`.

```yaml
widget:
  type: traefik
  url: http://traefik.host.or.ip
  username: username # optional
  password: password # optional
```


<a id="widget-transmission"></a>

---

---
title: Transmission
description: Transmission Widget Configuration
---

Learn more about [Transmission](https://github.com/transmission/transmission).

Uses the same username and password used to login from the web.

Allowed fields: `["leech", "download", "seed", "upload"]`.

```yaml
widget:
  type: transmission
  url: http://transmission.host.or.ip
  username: username
  password: password
  rpcUrl: /transmission/ # Optional. Matches the value of "rpc-url" in your Transmission's settings.json file
```


<a id="widget-trilium"></a>

---

---
title: Trilium
description: Trilium Widget Configuration
---

Learn more about [Trilium](https://github.com/TriliumNext/Notes).

This widget is compatible with [TriliumNext](https://github.com/TriliumNext/Notes) versions >= [v0.94.0](https://github.com/TriliumNext/Notes/releases/tag/v0.94.0).

Find (or create) your ETAPI key under `Options > ETAPI > Create new ETAPI token`.

Allowed fields: `["version", "notesCount", "dbSize"]`

```yaml
widget:
  type: trilium
  url: https://trilium.host.or.ip
  key: etapi_token
```


<a id="widget-truenas"></a>

---

---
title: TrueNas
description: TrueNas Scale Widget Configuration
---

Learn more about [TrueNas](https://www.truenas.com/).

| TrueNAS Version         | Homepage widget version |
| ----------------------- | ----------------------- |
| < 26.04 (REST API)      | 1 (default)             |
| > 25.04 (Websocket API) | 2                       |

Allowed fields: `["load", "uptime", "alerts"]`.

To create an API Key, follow [the official TrueNAS documentation](https://www.truenas.com/docs/scale/scaletutorials/toptoolbar/managingapikeys/).

A detailed pool listing is disabled by default, but can be enabled with the `enablePools` option.

To use the `enablePools` option with TrueNAS Core, the `nasType` parameter is required.

```yaml
widget:
  type: truenas
  url: http://truenas.host.or.ip
  version: 2 # optional, defaults to 1
  username: user # not required if using api key
  password: pass # not required if using api key
  key: yourtruenasapikey # not required if using username / password
  enablePools: true # optional, defaults to false
  nasType: scale # defaults to scale, must be set to 'core' if using enablePools with TrueNAS Core
```


<a id="widget-tubearchivist"></a>

---

---
title: Tube Archivist
description: Tube Archivist Widget Configuration
---

Learn more about [Tube Archivist](https://github.com/tubearchivist/tubearchivist).

You must be running at least version 0.4.4

Allowed fields: `["downloads", "videos", "channels", "playlists"]`.

```yaml
widget:
  type: tubearchivist
  url: http://tubearchivist.host.or.ip
  key: tubearchivistapikey
```


<a id="widget-unifi-controller"></a>

---

---
title: Unifi Controller
description: Unifi Controller Widget Configuration
---

Learn more about [Unifi Controller](https://ui.com/).

_(Find the Unifi Controller information widget [here](../info/unifi_controller.md))_

You can display general connectivity status from your Unifi (Network) Controller.

!!! warning

    When authenticating you will want to use a local account that has at least read privileges.

An optional 'site' parameter can be supplied, if it is not the widget will use the default site for the controller.

Allowed fields: `["uptime", "wan", "lan", "lan_users", "lan_devices", "wlan", "wlan_users", "wlan_devices"]` (maximum of four). Fields unsupported by the unifi device will not be shown.

!!! tip

    If you enter e.g. incorrect credentials and receive an "API Error", you may need to recreate the container or restart the service to clear the cache.

```yaml
widget:
  type: unifi
  url: https://unifi.host.or.ip:port
  site: Site Name # optional
  username: user
  password: pass
  key: unifiapikey # required if using API key instead of username/password
```


<a id="widget-unifi-drive"></a>

---

---
title: UniFi Drive
description: UniFi Drive Widget Configuration
---

Learn more about [UniFi Drive](https://ui.com/integrations/network-storage).

## Configuration

Displays storage statistics from your UniFi Network Attached Storage (UNAS) device. Requires a local UniFi account with at least read privileges.

Allowed fields: `["total", "used", "available", "status"]`

```yaml
widget:
  type: unifi_drive
  url: https://unifi.host.or.ip
  username: your_username
  password: your_password
```

!!! tip

    If you enter incorrect credentials and receive an "API Error", you may need to recreate the container or restart the service to clear the cache.


<a id="widget-unmanic"></a>

---

---
title: Unmanic
description: Unmanic Widget Configuration
---

Learn more about [Unmanic](https://github.com/Unmanic/unmanic).

Allowed fields: `["active_workers", "total_workers", "records_total"]`.

```yaml
widget:
  type: unmanic
  url: http://unmanic.host.or.ip:port
```


<a id="widget-unraid"></a>

---

---
title: Unraid
description: Unraid Widget Configuration
---

Learn more about [Unraid](https://unraid.net/).

The Unraid widget allows you to monitor the resources of an Unraid server.

**Minimum Requirements:**

- Unraid 7.2 -or- Unraid Connect plugin 2025.08.19.1850
- API key with the **ADMIN** role: [Managing API Keys](https://docs.unraid.net/go/managing-api-keys)

The widget can display metrics for selected Unraid pools. If using one of the "pool" fields, you must also add the pool name to the settings.

**Allowed fields:** `["cpu","memoryPercent","memoryAvailable","memoryUsed","notifications","arrayFree","arrayUsedSpace","arrayUsedPercent","status","pool1UsedSpace","pool1FreeSpace","pool1UsedPercent","pool2UsedSpace","pool2FreeSpace","pool2UsedPercent","pool3UsedSpace","pool3FreeSpace","pool3UsedPercent","pool4UsedSpace","pool4FreeSpace","pool4UsedPercent"]`

```yaml
widget:
  type: unraid
  url: https://unraid.host.or.ip
  key: api-key
  pool1: pool1name # required only if using pool1 fields
  pool2: pool2name # required only if using pool2 fields
  pool3: pool3name # required only if using pool3 fields
  pool4: pool4name # required only if using pool4 fields
```


<a id="widget-uptime-kuma"></a>

---

---
title: Uptime Kuma
description: Uptime Kuma Widget Configuration
---

Learn more about [Uptime Kuma](https://github.com/louislam/uptime-kuma).

As Uptime Kuma does not yet have a full API the widget uses data from a single "status page". As such you will need a status page setup with a group of monitored sites, which is where you get the slug (the url without the `/status/` portion). E.g. if your status page is URL http://uptimekuma.host/status/statuspageslug, insert `slug: statuspageslug`.

Allowed fields: `["up", "down", "uptime", "incident"]`.

```yaml
widget:
  type: uptimekuma
  url: http://uptimekuma.host.or.ip:port
  slug: statuspageslug
```


<a id="widget-uptimerobot"></a>

---

---
title: UptimeRobot
description: UptimeRobot Widget Configuration
---

Learn more about [UptimeRobot](https://uptimerobot.com/).

To generate an API key, select `My Settings`, and either `Monitor-Specific API Key` or `Read-Only API Key`.

A `Monitor-Specific API Key` will provide the following detailed information
for the selected monitor:

- Current status
- Current uptime
- Date/time of last downtime
- Duration of last downtime

Allowed fields: `["status", "uptime", "lastDown", "downDuration"]`.

A `Read-Only API Key` will provide a summary of all monitors in your account:

- Number of 'Up' monitors
- Number of 'Down' monitors

Allowed fields: `["sitesUp", "sitesDown"]`.

```yaml
widget:
  type: uptimerobot
  url: https://api.uptimerobot.com
  key: uptimerobotapitoken
```


<a id="widget-urbackup"></a>

---

---
title: UrBackup
description: UrBackup Widget Configuration
---

Learn more about [UrBackup](https://github.com/uroni/urbackup_backend).

The UrBackup widget retrieves the total number of clients that currently have no errors, have errors, or haven't backed up recently. Clients are considered "Errored" or "Out of Date" if either the file or image backups for that client have errors/are out of date, unless the client does not support image backups.

The default number of days that can elapse before a client is marked Out of Date is 3, but this value can be customized by setting the `maxDays` value in the config.

Optionally, the widget can also report the total amount of disk space consumed by backups. This is disabled by default, because it requires a second API call.

Note: client status is only shown for backups that the specified user has access to. Disk Usage shown is the total for all backups, regardless of permissions.

Allowed fields: `["ok", "errored", "noRecent", "totalUsed"]`. _Note that `totalUsed` will not be shown unless explicitly included in `fields`._

```yaml
widget:
  type: urbackup
  username: urbackupUsername
  password: urbackupPassword
  url: http://urbackupUrl:55414
  maxDays: 5 # optional
```


<a id="widget-vikunja"></a>

---

---
title: Vikunja
description: Vikunja Widget Configuration
---

Learn more about [Vikunja](https://vikunja.io).

Allowed fields: `["projects", "tasks7d", "tasksOverdue", "tasksInProgress"]`.

A list of the next 5 tasks ordered by due date is disabled by default, but can be enabled with the `enableTaskList` option.

| Vikunja Version | Homepage Widget Version |
| --------------- | ----------------------- |
| < v1.0.0-rc4    | 1 (default)             |
| >= v1.0.0-rc4   | 2                       |

```yaml
widget:
  type: vikunja
  url: http[s]://vikunja.host.or.ip[:port]
  key: vikunjaapikey
  enableTaskList: true # optional, defaults to false
  version: 2 # optional, defaults to 1
```


<a id="widget-wallos"></a>

---

---
title: Wallos
description: Wallos Widget Configuration
---

Learn more about [Wallos](https://github.com/ellite/wallos).

If you're using more than one currency to record subscriptions then you should also have your "Fixer API" key set-up (`Settings > Fixer API Key`).

> **Please Note:** The monthly cost displayed is the total cost of subscriptions in that month, **not** the _"monthly"_ average cost.

Get your API key under `Profile > API Key`.

Allowed fields: `["activeSubscriptions", "nextRenewingSubscription", "previousMonthlyCost", "thisMonthlyCost", "nextMonthlyCost"]`.

Default fields: `["activeSubscriptions", "nextRenewingSubscription", "thisMonthlyCost", "nextMonthlyCost"]`.

```yaml
widget:
  type: wallos
  url: http://wallos.host.or.ip
  key: apikeyapikeyapikeyapikeyapikey
```


<a id="widget-watchtower"></a>

---

---
title: Watchtower
description: Watchtower Widget Configuration
---

Learn more about [Watchtower](https://github.com/nicholas-fedor/watchtower).

To use this widget, Watchtower needs to be configured to [enable metrics](https://watchtower.nickfedor.com/dev/advanced-features/metrics-api/).

Allowed fields: `["containers_scanned", "containers_updated", "containers_failed"]`.

```yaml
widget:
  type: watchtower
  url: http://your-ip-address:8080
  key: demotoken
```


<a id="widget-wgeasy"></a>

---

---
title: Wg-Easy
description: Wg-Easy Widget Configuration
---

Learn more about [Wg-Easy](https://github.com/wg-easy/wg-easy).

Allowed fields: `["connected", "enabled", "disabled", "total"]`.

Note: by default `["connected", "enabled", "total"]` are displayed.

To detect if a device is connected the time since the last handshake is queried. `threshold` is the time to wait in minutes since the last handshake to consider a device connected. Default is 2 minutes.

| Wg-Easy API Version | Homepage Widget Version |
| ------------------- | ----------------------- |
| < v15               | 1 (default)             |
| >= v15              | 2                       |

```yaml
widget:
  type: wgeasy
  url: http://wg.easy.or.ip
  version: 2 # optional, default is 1
  username: yourwgusername # required for v15 and above
  password: yourwgeasypassword
  threshold: 2 # optional
```


<a id="widget-whatsupdocker"></a>

---

---
title: What's Up Docker
description: What's Up Docker Widget Configuration
---

Learn more about [What's Up Docker](https://github.com/fmartinou/whats-up-docker).

Allowed fields: `["monitoring", "updates"]`.

```yaml
widget:
  type: whatsupdocker
  url: http://whatsupdocker:port
  username: username # optional
  password: password # optional
```


<a id="widget-xteve"></a>

---

---
title: Xteve
description: Xteve Widget Configuration
---

Learn more about [Xteve](https://github.com/xteve-project/xTeVe).

Allowed fields: `["streams_all", "streams_active", "streams_xepg"]`.

```yaml
widget:
  type: xteve
  url: http://xteve.host.or.ip
  username: username # optional
  password: password # optional
```


<a id="widget-yourspotify"></a>

---

---
title: Your Spotify
description: Your Spotify Widget Configuration
---

Learn more about [Your Spotify](https://github.com/Yooooomi/your_spotify).

Find your API key under `Settings > Account > Public token`, click `Generate` if not yet generated, copy key after
`?token=`.

Allowed fields: `["songs", "time", "artists"]`.

```yaml
widget:
  type: yourspotify
  url: http://your-spotify-server.host.or.ip # if using lsio image, add /api/
  key: apikeyapikeyapikeyapikeyapikey
  interval: month # optional, defaults to week
```

#### Interval

Allowed values for `interval`: `day`, `week`, `month`, `year`, `all`.

!!! note

    `interval` is different from predefined intervals you see in `Your Spotify`'s UI.
    For example, `This week` in UI means _from the start of this week_, here `week` means _past 7 days_.


<a id="widget-zabbix"></a>

---

---
title: Zabbix
description: Zabbix Widget Configuration
---

Learn more about [Zabbix](https://github.com/zabbix/zabbix). The widget supports (at least) Zabbix server version 7.0.

---

Allowed fields: `["unclassified", "information", "warning", "average", "high", "disaster"]`.

Only 4 fields can be shown at a time, with the default being: `["warning", "average", "high", "disaster"]`.

```yaml
widget:
  type: zabbix
  url: http://zabbix.host.or.ip/zabbix
  key: your-api-key
```

See the [Zabbix documentation](https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens) for details on generating API tokens.
