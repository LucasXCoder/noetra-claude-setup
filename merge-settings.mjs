#!/usr/bin/env node
// merge-settings.mjs <existing.json> <incoming.json>  → merged JSON on stdout.
// Incoming (the Noetra template) wins for every key it defines, except that permission rules,
// enabled plugins, marketplaces and env vars are unioned so Mac-only additions survive.
import { readFileSync } from 'node:fs';

const [existing, incoming] = process.argv.slice(2).map((p) => JSON.parse(readFileSync(p, 'utf8')));
const merged = { ...existing, ...incoming };
const union = (a = [], b = []) => [...new Set([...a, ...b])];

if (existing.permissions || incoming.permissions) {
  const e = existing.permissions || {};
  const i = incoming.permissions || {};
  merged.permissions = { ...e, ...i };
  for (const k of ['allow', 'deny', 'ask', 'additionalDirectories']) {
    if (e[k] || i[k]) merged.permissions[k] = union(e[k], i[k]);
  }
}
for (const k of ['enabledPlugins', 'extraKnownMarketplaces', 'env']) {
  if (existing[k] || incoming[k]) merged[k] = { ...(existing[k] || {}), ...(incoming[k] || {}) };
}
process.stdout.write(JSON.stringify(merged, null, 2) + '\n');
