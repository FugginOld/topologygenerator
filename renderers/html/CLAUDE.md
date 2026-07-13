# renderers/html/ — the live dashboard

- `topology_server.py` — stdlib `http.server`. Serves this directory from disk
  (`SimpleHTTPRequestHandler`, `directory=HERE`) plus a small JSON API (`/api/list`,
  `/api/telemetry`, ingest, remote scan). No framework — stdlib only.
- `index.html` — the single-file dashboard (SVG topology + sidebar + skins). All app logic lives in
  the final `<script>` block.
- `store.py` — persistence + a `path()` **path-injection barrier** (basename → `[A-Za-z0-9._-]`
  allowlist → realpath containment). Selftest: `python renderers/html/store.py`.

**Serving:** HTML / CSS / JS edits need no restart — the server reads from disk per request and sends
`Cache-Control: no-store`, so just hard-refresh the browser. Only Python edits need
`systemctl restart topology-server`.

**Security:** `el()` sets `textContent` / `setAttribute` only — never `innerHTML` with scanned or
host-supplied strings (labels are untrusted). Keep it that way. The remote-scan endpoint validates the
host with `ipaddress.ip_address()` and stamps identity server-side — never interpolate a name into the
SSH command.

**Dashboard model notes:** skins are pure CSS vars on `body[data-theme]`, mirrored into JS via
`refreshColors()` because SVG can't use `var()`; the current skins are neutral + unraid, light/dark
(flat, no glass). A node's `n.x` is the card's **left edge** — columns are left-aligned and spaced by
their widest card, and links attach parent-right-edge → child-left-edge. After JS edits, `node --check`
the extracted `<script>` (CI does this too).
