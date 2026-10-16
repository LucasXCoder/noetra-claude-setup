// G1 oracle: unlazy is installed where Claude Code discovers skills, with an
// intact file set, routable frontmatter, and sources that parse on this runtime.
import { existsSync, readFileSync, statSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { homedir } from "node:os";
import { join } from "node:path";

const SKILL = join(homedir(), ".claude", "skills", "unlazy");
const fail = (m) => { console.error("FAIL: " + m); process.exit(1); };

if (!existsSync(SKILL)) fail("skill directory missing: " + SKILL);

const required = [
  "SKILL.md", "SECURITY.md", "README.md", "package.json",
  "scripts/gate-check.mjs", "scripts/gate-lint.mjs", "scripts/stop-hook.mjs",
  "scripts/install-hooks.mjs", "scripts/dispatch-check.mjs",
  "scripts/lib/gates.mjs", "scripts/lib/dispatch.mjs",
  "scripts/lib/process-tree.mjs", "scripts/lib/regex-worker.mjs",
  "references/gates.md", "references/method.md", "references/orchestration.md",
  "references/dispatch.md", "references/parallel.md", "references/token-economy.md",
  "templates/gates-leaf.md", "templates/gates-node.md", "templates/PLAN.md",
];

for (const rel of required) {
  const p = join(SKILL, rel);
  if (!existsSync(p)) fail("missing required file: " + rel);
  if (statSync(p).size === 0) fail("required file is empty: " + rel);
}

const skillMd = readFileSync(join(SKILL, "SKILL.md"), "utf8");
const fm = /^---\r?\n([\s\S]*?)\r?\n---/.exec(skillMd);
if (!fm) fail("SKILL.md has no YAML frontmatter block; Claude Code cannot route it");
const name = /^name:\s*(.+)$/m.exec(fm[1]);
const desc = /^description:\s*(.+)$/m.exec(fm[1]);
if (!name || name[1].trim() !== "unlazy") fail("frontmatter name is not 'unlazy'");
if (!desc || desc[1].trim().length < 40) fail("frontmatter description missing or too short to route on");

const sources = required.filter((r) => r.endsWith(".mjs"));
for (const rel of sources) {
  try {
    execFileSync(process.execPath, ["--check", join(SKILL, rel)], { stdio: "pipe" });
  } catch {
    fail("source does not parse on " + process.version + ": " + rel);
  }
}

console.log(`verified ${required.length} required paths present and non-empty`);
console.log(`parsed ${sources.length} sources on ${process.version}`);
console.log("install verification passed");
