// ~/.claude/statusline.mjs : zero-dependency status line, same file on Windows and macOS
let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (c) => (raw += c));
process.stdin.on('end', () => {
  let d = {};
  try { d = JSON.parse(raw.trim() || '{}'); } catch {}
  const R = '\x1b[0m';
  const dim = (s) => `\x1b[2m${s}${R}`;
  const tint = (p) => `\x1b[${p >= 85 ? 31 : p >= 60 ? 33 : 32}m`;
  const num = (v) => (typeof v === 'number' ? Math.round(v) : null);
  const clock = (s) => new Date(s * 1000).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  const parts = [`${d.model?.display_name ?? '?'}${d.effort?.level ? '·' + d.effort.level : ''}`];
  const ctx = num(d.context_window?.used_percentage);
  if (ctx !== null) {
    const n = Math.min(10, Math.round(ctx / 10));
    parts.push(`${tint(ctx)}${'█'.repeat(n)}${'░'.repeat(10 - n)} ${ctx}%${R}`);
  }
  for (const [key, label] of [['five_hour', '5h'], ['seven_day', '7d']]) {
    const w = d.rate_limits?.[key];
    const p = num(w?.used_percentage);
    if (p !== null) parts.push(`${label} ${tint(p)}${p}%${R}${w.resets_at ? dim(' ↻' + clock(w.resets_at)) : ''}`);
  }
  const pc = d.prompt_cache;
  if (pc?.warm && pc.expires_at) parts.push(dim(`cache ${Math.max(0, Math.round((pc.expires_at - Date.now() / 1000) / 60))}m`));
  else if (pc?.caching_observed) parts.push('\x1b[33mcache cold\x1b[0m');
  if (typeof d.cost?.total_cost_usd === 'number') parts.push(dim(`≈$${d.cost.total_cost_usd.toFixed(2)} API-eq`));
  process.stdout.write(parts.join(dim(' │ ')) + '\n');
});
