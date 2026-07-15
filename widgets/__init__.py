"""Widget Store — the catalog of widget Types and their service fetchers.

A Widget Type is code (label, category, icon, config-field schema, fetcher); a
Widget is a user-configured instance of a Type owned by a host (see
`renderers/html/widget_store.py`). Fetchers follow the Collector contract:
stdlib-only, never raise, return {} on any source failure. See docs/prd/widget-store.md.
"""
from __future__ import annotations
