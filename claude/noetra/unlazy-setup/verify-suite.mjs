// G2 oracle: the skill's own regression suite passes on this machine.
// The suite list is read from the repo's package.json rather than hardcoded,
// so a suite added upstream is covered instead of silently skipped.
import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { homedir } from "node:os";
import { join } from "node:path";

const SKILL = join(homedir(), ".claude", "skills", "unlazy");
const fail = (m) => { console.error("FAIL: " + m); process.exit(1); };

const pkg = JSON.parse(readFileSync(join(SKILL, "package.json"), "utf8"));
const script = pkg?.scripts?.test;
if (typeof script !== "string" || !script.trim()) fail("package.json defines no test script");

const cmds = script.split("&&").map((s) => s.trim()).filter(Boolean);
if (cmds.length < 3) fail(`unexpected test script shape (${cmds.length} commands): ${script}`);

let ran = 0;
for (const cmd of cmds) {
  const parts = cmd.split(/\s+/);
  if (parts[0] !== "node") fail("unsupported non-node test command: " + cmd);
  const r = spawnSync(process.execPath, parts.slice(1), {
    cwd: SKILL, encoding: "utf8", timeout: 300000,
  });
  if (r.error) fail(`${cmd} failed to start: ${r.error.message}`);
  if (r.status !== 0) {
    const tail = ((r.stdout || "") + (r.stderr || "")).slice(-1500);
    fail(`${cmd} exited ${r.status}\n${tail}`);
  }
  ran++;
}

if (ran !== cmds.length) fail(`ran ${ran} of ${cmds.length} declared suites`);
console.log(`ran ${ran} suites declared in package.json scripts.test, every one exit 0`);
console.log("suite verification passed");
