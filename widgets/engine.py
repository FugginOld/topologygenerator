"""Data-driven widget engine.

A *definition* declares auth + endpoints + field mappings; the engine does the
HTTP and extraction, so most Homepage-style widgets become ~data instead of a
hand-written fetcher. Collector contract: stdlib-only, never raises, {} on any
source failure. Auth-weird services (cookie login, CSRF) still need a custom
fetcher in fetchers.py — the engine covers the api-key / basic / bearer majority.

Definition shape:
  {
    "id","label","category","icon","desc",
    "auth": "none"|"apikey-header"|"apikey-query"|"bearer"|"token"|"basic",
    "header": "X-Api-Key",       # apikey-header only (default X-Api-Key)
    "param":  "apikey",          # apikey-query only (default apikey)
    "params": [{"name","label","required"}],   # extra config/path params (env, slug)
    "calls":  {name: "/path/{env}?x=1"},        # {url}-relative; {cfg-key} templated
    "show":   [{"key","call","path","op","fmt","num","den"}],
  }
show ops:  none -> value at path · "len" -> list/dict length ·
  "count_where:F=V" -> count list items where item[F]==V ·
  "ratio" (num/den paths) -> 100*num/den.   fmt: "pct" | "round".
"""
from __future__ import annotations

import base64
import json
import ssl
import urllib.parse
import urllib.request

_TLS = ssl.create_default_context()
_TLS.check_hostname = False
_TLS.verify_mode = ssl.CERT_NONE


def _get(url, headers, timeout=8):
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout, context=_TLS) as r:
            return json.load(r)
    except Exception:
        return None


def form_fields(defn: dict) -> list[dict]:
    """Config-form fields implied by the auth style + any extra path params."""
    fields = [{"name": "url", "label": "URL (http://host:port)", "type": "url", "required": True}]
    for p in defn.get("params", []):
        fields.append({"name": p["name"], "label": p.get("label", p["name"]),
                       "type": "text", "required": bool(p.get("required"))})
    auth = defn.get("auth", "none")
    if auth in ("apikey-header", "apikey-query", "bearer", "token"):
        fields.append({"name": "key", "label": "API key", "type": "password",
                       "required": True, "secret": True})
    elif auth == "basic":
        fields.append({"name": "username", "label": "Username", "type": "text"})
        fields.append({"name": "password", "label": "Password", "type": "password", "secret": True})
    return fields


def _auth(defn: dict, cfg: dict):
    """(headers, query_params) for the definition's auth style."""
    a, key = defn.get("auth", "none"), cfg.get("key", "")
    h, q = {}, []
    if a == "apikey-header":
        h[defn.get("header", "X-Api-Key")] = key
    elif a == "bearer":
        h["Authorization"] = "Bearer " + key
    elif a == "token":
        h["Authorization"] = "Token " + key
    elif a == "apikey-query":
        q.append((defn.get("param", "apikey"), key))
    elif a == "basic":
        raw = f"{cfg.get('username','')}:{cfg.get('password','')}".encode()
        h["Authorization"] = "Basic " + base64.b64encode(raw).decode()
    return h, q


def _fmt_url(base: str, path: str, cfg: dict, qextra) -> str:
    for k, v in cfg.items():                              # {env}/{slug} path templating
        path = path.replace("{" + k + "}", urllib.parse.quote(str(v), safe=""))
    url = base + path
    if qextra:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(qextra)
    return url


def _resolve(data, path):
    """Dotted path into JSON; `len`/`length` gives a list/dict size, ints index lists."""
    cur = data
    for part in (path or "").split("."):
        if part == "":
            continue
        if part in ("len", "length"):
            return len(cur) if isinstance(cur, (list, dict, str)) else None
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None
        elif isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
        if cur is None:
            return None
    return cur


def _apply(data, f):
    op = f.get("op")
    if op == "len":
        v = _resolve(data, f["path"]) if f.get("path") else data
        return len(v) if isinstance(v, (list, dict, str)) else None
    if op and op.startswith("count_where:"):
        fld, _, val = op.split(":", 1)[1].partition("=")
        lst = _resolve(data, f["path"]) if f.get("path") else data
        return sum(1 for x in lst if isinstance(x, dict) and str(x.get(fld)) == val) if isinstance(lst, list) else None
    if op == "ratio":
        num, den = _resolve(data, f.get("num", "")), _resolve(data, f.get("den", ""))
        if isinstance(num, (int, float)) and isinstance(den, (int, float)) and den:
            v = 100.0 * num / den
            return round(v, 1) if f.get("fmt") == "pct" else v
        return None
    v = _resolve(data, f.get("path", ""))
    if isinstance(v, (int, float)):
        if f.get("fmt") == "pct":
            return round(v, 1)
        if f.get("fmt") == "round":
            return round(v)
    return v


def fetch(defn: dict, cfg: dict) -> dict:
    base = (cfg.get("url") or "").rstrip("/")
    if not base:
        return {}
    headers, q = _auth(defn, cfg)
    calls = {name: _get(_fmt_url(base, path, cfg, q), headers)
             for name, path in (defn.get("calls") or {}).items()}
    out = {}
    for f in defn.get("show") or []:
        src = calls.get(f["call"]) if f.get("call") else next(iter(calls.values()), None)
        if src is None:
            continue
        val = _apply(src, f)
        if val is not None:
            out[f["key"]] = val
    return out if out else {}


def entry(defn: dict) -> dict:
    """A registry CATALOG entry backed by the engine (bound fetch, derived fields)."""
    return {"id": defn["id"], "label": defn["label"], "category": defn.get("category", "Other"),
            "icon": defn.get("icon", defn["id"]), "desc": defn.get("desc", ""),
            "fields": form_fields(defn), "config_key": defn.get("config_key"),
            "fetch": (lambda cfg, d=defn: fetch(d, cfg))}


if __name__ == "__main__":   # ponytail: pure logic + a stubbed end-to-end fetch, offline
    assert _resolve({"a": {"b": 5}}, "a.b") == 5
    assert _resolve({"a": [1, 2, 3]}, "a.len") == 3
    assert _resolve({"a": [{"x": 9}]}, "a.0.x") == 9
    assert _resolve({"a": 1}, "a.b.c") is None
    assert _apply([1, 2, 3], {"op": "len"}) == 3
    assert _apply({"r": [{"s": "running"}, {"s": "exited"}]},
                  {"op": "count_where:s=running", "path": "r"}) == 1
    assert _apply({"b": 30, "t": 100}, {"op": "ratio", "num": "b", "den": "t", "fmt": "pct"}) == 30.0
    h, q = _auth({"auth": "apikey-header", "header": "X-Gotify-Key"}, {"key": "K"})
    assert h == {"X-Gotify-Key": "K"} and q == []
    h, q = _auth({"auth": "basic"}, {"username": "u", "password": "p"})
    assert h["Authorization"].startswith("Basic ")
    assert _fmt_url("http://h", "/e/{env}/x", {"env": "2"}, [("apikey", "K")]) == "http://h/e/2/x?apikey=K"
    assert [f["name"] for f in form_fields({"auth": "basic"})] == ["url", "username", "password"]

    # stub the HTTP layer and drive a full fetch (sonarr-shaped)
    _stub = {"series": [1, 2, 3], "queue": {"totalRecords": 2}, "missing": {"totalRecords": 5}}
    _orig = _get
    _get = lambda url, headers, timeout=8: _stub[url.split("/")[-1].split("?")[0]]   # noqa: E731
    d = {"auth": "apikey-query", "param": "apikey",
         "calls": {"series": "/series", "queue": "/queue", "missing": "/missing"},
         "show": [{"key": "series", "call": "series", "op": "len"},
                  {"key": "queue", "call": "queue", "path": "totalRecords"},
                  {"key": "missing", "call": "missing", "path": "totalRecords"}]}
    assert fetch(d, {"url": "http://h", "key": "K"}) == {"series": 3, "queue": 2, "missing": 5}
    _get = _orig
    assert fetch(d, {"url": ""}) == {}
    print("widgets/engine self-check ok")
