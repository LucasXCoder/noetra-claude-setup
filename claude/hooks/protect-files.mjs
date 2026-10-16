// ~/.claude/hooks/protect-files.mjs : PreToolUse(Edit|Write) blocks edits to rule files and secrets
const PROTECTED = [
  /\/PAPER_ORB\/RULES\.md$/i,              // permanent trading rules: human-edited only
  /(^|\/)\.env(?!\.example$)(\.[\w-]+)?$/i, // .env, .env.local (not .env.example)
  /\.(pem|key|p12|pfx)$/i,
  /\/\.claude\/\.credentials\.json$/i,
  /\/\.git\//,
  /\/\.ssh\//,
];
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const p = String(JSON.parse(raw || '{}').tool_input?.file_path ?? '').split('\\').join('/');
  const hit = PROTECTED.find((re) => re.test(p));
  if (!hit) process.exit(0);
  process.stderr.write(`Blocked: ${p} is protected (${hit}). Propose the change in chat; Lucas edits it by hand.\n`);
  process.exit(2);
});
