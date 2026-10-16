// ~/.claude/hooks/guard-shell.mjs : PreToolUse guard for the Bash AND PowerShell tools
const DENY = [
  [/\brm\s+-\w*(?:rf|fr)\w*\s+["']?(?:\/|~|\$HOME|\.\.?|\*|\/[a-z]|[a-z]:)[\\/]?["']?(?:\s|$)/i, 'rm -rf on a root, home, parent or wildcard target'],
  [/\bgit\s+reset\s+--hard\b/i, 'git reset --hard discards uncommitted work'],
  [/\bgit\s+clean\s+-\w*f/i, 'git clean -f deletes untracked files'],
  [/\bgit\s+push\b.*(?:--force(?!-with-lease)|\s-f\b)/i, 'force push (use --force-with-lease)'],
  [/\b(?:Format-Volume|Clear-Disk|diskpart|mkfs)\b/i, 'disk formatting'],
  [/\b(?:drop\s+(?:table|database)|truncate\s+table)\b/i, 'destructive SQL'],
];
const ASK = [
  [/\brm\s+-\w*(?:rf|fr)\w*\b/i, 'recursive force delete'],
  [/\bRemove-Item\b(?=.*-Recurse)(?=.*-Force)/i, 'Remove-Item -Recurse -Force'],
  [/\b(?:del|erase|rd|rmdir)\s+\/s\b/i, 'cmd recursive delete'],
  [/\bgit\s+(?:checkout|restore)\s+(?:--\s+)?\.(?:\s|$)/i, 'discards all working-tree changes'],
  [/\bgit\s+branch\s+-D\b/, 'force-deletes a branch'],
];
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const cmd = String(JSON.parse(raw || '{}').tool_input?.command ?? '');
  const hit = (rules) => rules.find(([re]) => re.test(cmd));
  const deny = hit(DENY);
  const ask = deny ? null : hit(ASK);
  if (!deny && !ask) process.exit(0);
  const [decision, reason] = deny ? ['deny', deny[1]] : ['ask', ask[1]];
  process.stdout.write(JSON.stringify({
    hookSpecificOutput: { hookEventName: 'PreToolUse', permissionDecision: decision, permissionDecisionReason: `guard-shell: ${reason}` },
  }));
});
