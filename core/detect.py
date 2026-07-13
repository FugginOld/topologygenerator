"""Credential-free gateway fingerprint: identify the router so a fresh install
knows which collector to configure.

We can *identify* a UniFi/OPNsense/pfSense gateway without auth, but we can't
*pull data* from it without credentials — so this only guides config, it never
activates anything. Collectors already no-op when their source is absent, so the
user just enables the one this points at.

Signal: an HTTP GET of the gateway's web UI. The login page names the product
(works for DIY installs on generic hardware, which have no telltale MAC OUI).
"""
from __future__ import annotations

import ipaddress
import re
import socket
import ssl
import subprocess
import urllib.error
import urllib.request

_HINTS = {
    "unifi":    "add a `unifi` API key",
    "opnsense": "add `opnsense` API key + secret",
    "pfsense":  "install pfSense-pkg-API, then a `pfsense` collector (not built yet)",
}


def _classify(blob: str) -> str | None:
    """Router kind from lowercased page body + headers."""
    b = blob.lower()
    if "opnsense" in b:
        return "opnsense"
    if "pfsense" in b:
        return "pfsense"
    if "unifi" in b or "ubnt" in b or "ubiquiti" in b:
        return "unifi"
    return None


def _local_ip() -> str | None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return None
    finally:
        s.close()


def default_gateway() -> str | None:
    """Default-route gateway IP, cross-platform; falls back to the local /24's .1."""
    try:  # linux: /proc/net/route (hex, little-endian)
        with open("/proc/net/route") as fh:
            for line in fh.read().splitlines()[1:]:
                f = line.split()
                if len(f) > 3 and f[1] == "00000000" and int(f[3], 16) & 2:
                    return socket.inet_ntoa(bytes.fromhex(f[2])[::-1])
    except OSError:
        pass
    for cmd in (["route", "print", "0.0.0.0"], ["netstat", "-rn"]):  # windows / bsd/mac
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=8).stdout
        except (OSError, subprocess.SubprocessError):
            continue
        m = re.search(r"0\.0\.0\.0\s+0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)", out) \
            or re.search(r"(?m)^default\s+(\d+\.\d+\.\d+\.\d+)", out)
        if m:
            return m.group(1)
    ip = _local_ip()                      # ponytail: last resort, assumes .1 gateway
    if ip:
        try:
            return str(next(ipaddress.ip_network(ip + "/24", strict=False).hosts()))
        except (ValueError, StopIteration):
            pass
    return None


def _fingerprint(ip: str) -> str | None:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for url in (f"https://{ip}/", f"http://{ip}/"):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "topo-detect"})
            with urllib.request.urlopen(req, timeout=6, context=ctx) as r:
                kind = _classify(r.read(8192).decode("utf-8", "replace") + str(r.headers))
                if kind:
                    return kind
        except urllib.error.HTTPError as e:      # a login page is still a fingerprint
            kind = _classify(str(e.headers))
            if kind:
                return kind
        except (urllib.error.URLError, OSError, ValueError):
            continue
    try:  # UniFi OS proxies its Network app here even when the root page is generic
        urllib.request.urlopen(f"https://{ip}/proxy/network/", timeout=6, context=ctx)
        return "unifi"
    except urllib.error.HTTPError:
        return "unifi"                            # exists but needs auth -> still UniFi
    except (urllib.error.URLError, OSError):
        return None


def detect_gateway() -> dict | None:
    """{'ip','kind','hint'} for the default gateway, or None if none found."""
    ip = default_gateway()
    if not ip:
        return None
    kind = _fingerprint(ip)
    if not kind:
        return {"ip": ip, "kind": "generic",
                "hint": f"gateway {ip}: unrecognized — pingsweep still maps the LAN"}
    return {"ip": ip, "kind": kind,
            "hint": f"gateway {ip} looks like {kind.upper()} — {_HINTS[kind]} "
                    f"in config.yaml for VLAN + client detail"}


if __name__ == "__main__":  # ponytail: pure-logic selftest + live probe
    assert _classify("<title>OPNsense</title>") == "opnsense"
    assert _classify("Login to pfSense") == "pfsense"
    assert _classify("UniFi OS") == "unifi"
    assert _classify("<html>generic router</html>") is None
    print("classify ok")
    g = detect_gateway()
    print("live detect:", g)
