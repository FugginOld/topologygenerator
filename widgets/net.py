"""Shared HTTP for widget fetchers, with two guards a widget URL needs because it
is user-supplied and the *server* makes the request:

- SSRF guard: only private / loopback / link-local targets are fetched (homelab
  services live on the LAN). A hostname must resolve entirely to private
  addresses, which also blocks DNS-rebinding to a public host.
- TLS: unverified by default (self-signed Proxmox/UniFi/services), but callers can
  pass verify=True to opt into certificate validation.

Collector contract: never raises, returns None on any failure (incl. a blocked
target).
"""
from __future__ import annotations

import ipaddress
import json
import socket
import ssl
import urllib.parse
import urllib.request

_VERIFY = ssl.create_default_context()
_NOVERIFY = ssl.create_default_context()
_NOVERIFY.check_hostname = False
_NOVERIFY.verify_mode = ssl.CERT_NONE


def _private(ip_str: str) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str)
    except ValueError:
        return False
    return ip.is_private or ip.is_loopback or ip.is_link_local


def allowed(url: str) -> bool:
    """True only if `url`'s host is (or resolves entirely to) a private address."""
    try:
        host = urllib.parse.urlparse(url).hostname or ""
    except ValueError:
        return False
    if not host:
        return False
    if _private(host):                                   # IP literal
        return True
    try:                                                 # hostname: every A/AAAA must be private
        addrs = {info[4][0] for info in socket.getaddrinfo(host, None)}
    except OSError:
        return False
    return bool(addrs) and all(_private(a) for a in addrs)


def get_json(url, headers=None, data=None, method=None, timeout=8, verify=False):
    if not allowed(url):
        return None                                      # SSRF guard: non-private target refused
    ctx = _VERIFY if verify else _NOVERIFY
    try:
        req = urllib.request.Request(url, headers=headers or {}, data=data, method=method)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return json.load(r)
    except Exception:
        return None


if __name__ == "__main__":   # ponytail: the SSRF host check, offline
    assert allowed("http://192.168.1.5:8989")
    assert allowed("http://10.0.0.1/x") and allowed("http://127.0.0.1:61208")
    assert allowed("http://[::1]:8080")
    assert not allowed("http://8.8.8.8")           # public IP
    assert not allowed("https://example.com")      # resolves public
    assert not allowed("") and not allowed("not a url")
    print("widgets/net self-check ok")
