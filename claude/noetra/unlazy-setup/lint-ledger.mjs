// G0 oracle: pass through the skill's own ledger linter and require its real
// verdict. This wrapper adds no judgement of its own; it fails unless
// gate-lint.mjs exits 0 and emits its own LINT OK marker.
import { spawnSync } from "node:child_process";
import { homedir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const LINTER = join(homedir(), ".claude", "skills", "unlazy", "scripts", "gate-lint.mjs");
const fail = (m) => { console.error("FAIL: " + m); process.exit(1); };

const r = spawnSync(process.execPath, [LINTER, "GATES.md"], {
  cwd: here, encoding: "utf8", timeout: 120000,
});
if (r.error) fail("gate-lint failed to start: " + r.error.message);
const out = (r.stdout || "") + (r.stderr || "");
process.stdout.write(out);
if (r.status !== 0) fail(`gate-lint exited ${r.status}`);
if (!out.includes("LINT OK")) fail("gate-lint emitted no LINT OK marker");

console.log("ledger lint passed");
