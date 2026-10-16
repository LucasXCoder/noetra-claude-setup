#!/usr/bin/env python3
"""merge_settings.py <existing.json> <incoming.json> → merged JSON on stdout.
Python fallback for merge-settings.mjs (same rules) when node is not installed yet."""
import json
import sys

existing, incoming = (json.load(open(p, encoding="utf-8")) for p in sys.argv[1:3])
merged = {**existing, **incoming}
if "permissions" in existing or "permissions" in incoming:
    e, i = existing.get("permissions", {}), incoming.get("permissions", {})
    merged["permissions"] = {**e, **i}
    for k in ("allow", "deny", "ask", "additionalDirectories"):
        if k in e or k in i:
            merged["permissions"][k] = list(dict.fromkeys(e.get(k, []) + i.get(k, [])))
for k in ("enabledPlugins", "extraKnownMarketplaces", "env"):
    if k in existing or k in incoming:
        merged[k] = {**existing.get(k, {}), **incoming.get(k, {})}
json.dump(merged, sys.stdout, indent=2)
sys.stdout.write("\n")
