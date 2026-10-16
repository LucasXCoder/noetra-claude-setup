// G3 oracle: the checker refuses to certify a failing oracle on this machine.
// A negative control alone is not enough -- a checker that failed EVERYTHING
// would pass it. So this exercises one positive control plus three distinct
// failure modes, and requires the checkbox and the exit code to agree.
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { tmpdir, homedir } from "node:os";
import { join } from "node:path";

const SKILL = join(homedir(), ".claude", "skills", "unlazy");
const CHECKER = join(SKILL, "scripts", "gate-check.mjs");
const fail = (m) => { console.error("FAIL: " + m); process.exit(1); };

const MARK = "control marker present";
const root = mkdtempSync(join(tmpdir(), "unlazy-negctl-"));
const approvals = join(root, "approvals");
mkdirSync(approvals);

const cases = [
  { id: "positive",  why: "exit 0 and EXPECT matches",
    check: `node -e "console.log('${MARK}')"`,                         met: true },
  { id: "nonzero",   why: "nonzero exit, no marker",
    check: `node -e "process.exit(3)"`,                                met: false },
  { id: "mismatch",  why: "exit 0 but EXPECT does not match",
    check: `node -e "console.log('unrelated output')"`,                met: false },
  { id: "tokenliar", why: "marker printed but process exits nonzero",
    check: `node -e "console.log('${MARK}'); process.exit(4)"`,        met: false },
];

let verified = 0;
for (const c of cases) {
  const dir = join(root, c.id);
  mkdirSync(dir);
  const ledger = join(dir, "GATES.md");
  writeFileSync(ledger, `# Gates: ${c.id}

Scope: negative control fixture -- ${c.why}

- [ ] N1: fixture is certified only when the checker contract is satisfied
  CHECK: ${c.check}
  EXPECT: ${MARK}
  EVIDENCE: pending
`);

  const r = spawnSync(process.execPath, [CHECKER, "--approve", ledger], {
    encoding: "utf8", timeout: 120000,
    env: { ...process.env, UNLAZY_APPROVAL_DIR: approvals },
  });
  if (r.error) fail(`${c.id}: checker failed to start: ${r.error.message}`);

  const after = readFileSync(ledger, "utf8");
  const boxMet = /^- \[x\] N1:/m.test(after);
  const exitMet = r.status === 0;

  if (boxMet !== exitMet) {
    fail(`${c.id}: checkbox (met=${boxMet}) disagrees with exit code ${r.status}`);
  }
  if (boxMet !== c.met) {
    fail(`${c.id} (${c.why}): expected met=${c.met}, checker reported met=${boxMet} exit=${r.status}`);
  }
  if (c.met && !/EVIDENCE: exit=0;/.test(after)) {
    fail(`${c.id}: passing gate did not record exit-status evidence`);
  }
  if (!c.met && /^- \[x\]/m.test(after)) {
    fail(`${c.id}: failing oracle left a checked box in the ledger`);
  }
  verified++;
}

const negatives = cases.filter((c) => !c.met).length;
if (verified !== cases.length) fail(`exercised ${verified} of ${cases.length} fixtures`);
if (negatives < 3) fail("negative control coverage regressed below three failure modes");

console.log(`exercised ${verified} fixtures: 1 positive control certified, ${negatives} failure modes refused`);
console.log("enforcement verification passed");
