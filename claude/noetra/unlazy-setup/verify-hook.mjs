// G5 oracle: the Stop hook is installed globally AND actually blocks.
// Presence in settings.json proves nothing about behaviour, so this drives the
// real hook over its documented stdin contract across three states, including
// two negative controls that must NOT block.
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { tmpdir, homedir } from "node:os";
import { join } from "node:path";

const SETTINGS = join(homedir(), ".claude", "settings.json");
const fail = (m) => { console.error("FAIL: " + m); process.exit(1); };

if (!existsSync(SETTINGS)) fail("global settings.json not found: " + SETTINGS);
const settings = JSON.parse(readFileSync(SETTINGS, "utf8"));
const groups = settings?.hooks?.Stop;
if (!Array.isArray(groups) || groups.length === 0) fail("no hooks.Stop entries in global settings");

let hookCmd = null;
for (const g of groups) for (const h of (g.hooks || [])) {
  if (typeof h.command === "string" && h.command.includes("stop-hook.mjs")) hookCmd = h.command;
}
if (!hookCmd) fail("no unlazy stop-hook.mjs handler registered in hooks.Stop");

const m = /"([^"]*stop-hook\.mjs)"/.exec(hookCmd);
if (!m) fail("could not extract hook script path from: " + hookCmd);
const HOOK = m[1];
if (!existsSync(HOOK)) fail("registered hook script does not exist: " + HOOK);

const root = mkdtempSync(join(tmpdir(), "unlazy-hook-"));

const UNMET = `# Gates: fixture

Scope: a pipeline with work still outstanding

- [ ] H1: outstanding outcome
  EVIDENCE: pending
`;
const MET = `# Gates: fixture

Scope: a pipeline whose single outcome is met

- [x] H1: satisfied outcome
  EVIDENCE: manual: fixture recorded a decisive result
`;

const cases = [
  { id: "unmet",   ledger: UNMET, block: true,  why: "unmet gate must block the stop" },
  { id: "allmet",  ledger: MET,   block: false, why: "fully met ledger must not block" },
  { id: "noledger", ledger: null, block: false, why: "no ledger at all must not block" },
];

let checked = 0;
for (const c of cases) {
  const dir = join(root, c.id);
  mkdirSync(dir);
  if (c.ledger) writeFileSync(join(dir, "GATES.md"), c.ledger);

  const payload = JSON.stringify({ cwd: dir, session_id: "sess-" + c.id });
  const r = spawnSync(process.execPath, [HOOK, "--unlazy"], {
    input: payload, encoding: "utf8", timeout: 60000,
  });
  if (r.error) fail(`${c.id}: hook failed to start: ${r.error.message}`);

  let decision = null;
  const out = (r.stdout || "").trim();
  if (out) {
    for (const line of out.split(/\r?\n/)) {
      try { const parsed = JSON.parse(line); if (parsed && parsed.decision) decision = parsed.decision; }
      catch { /* non-JSON diagnostic line */ }
    }
  }
  const blocked = decision === "block";
  if (blocked !== c.block) {
    fail(`${c.id} (${c.why}): expected block=${c.block}, hook produced decision=${JSON.stringify(decision)} exit=${r.status} out=${out.slice(0, 300)}`);
  }
  checked++;
}

const negatives = cases.filter((c) => !c.block).length;
if (checked !== cases.length) fail(`drove ${checked} of ${cases.length} hook states`);
if (negatives < 2) fail("hook negative-control coverage regressed");

console.log(`registered hook: ${HOOK}`);
console.log(`drove ${checked} states: 1 blocked on unmet gates, ${negatives} correctly allowed the stop`);
console.log("hook verification passed");
