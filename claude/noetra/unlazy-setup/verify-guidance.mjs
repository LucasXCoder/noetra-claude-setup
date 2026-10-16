// G6 oracle: the fan-out guidance is present in the file every session loads,
// and carries the directives that actually make fan-out correct rather than
// merely mentioning parallelism.
import { readFileSync, existsSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";

const MD = process.argv[2] || join(homedir(), ".claude", "CLAUDE.md");
const fail = (m) => { console.error("FAIL: " + m); process.exit(1); };

if (!existsSync(MD)) fail("master CLAUDE.md not found: " + MD);
const text = readFileSync(MD, "utf8");

const heading = /^## Unlazy .* completion discipline/m;
if (!heading.test(text)) fail("no Unlazy section heading in CLAUDE.md");

const section = text.slice(text.search(heading));
if (section.length < 800) fail(`Unlazy section is only ${section.length} chars; too thin to be useful`);

// Each directive is the load-bearing part of the contract, not decoration.
const required = [
  [/seal the wave/i,                      "seal-the-wave barrier"],
  [/only then wait/i,                     "wait-after-seal ordering"],
  [/--reverify/,                          "parent re-verification of returned leaves"],
  [/disjoint\s+`?OWNS:/i,                 "disjoint OWNS ownership claim"],
  [/PLAN\.md/,                            "interfaces fixed in PLAN.md before dispatch"],
  [/inherited\s+\*?\*?`?PATH`?/i,         "approval binds inherited PATH"],
  [/cmd\.exe/i,                           "Windows default shell note"],
  [/exit 0/i,                             "both exit 0 and EXPECT required"],
  [/pending/i,                            "pending evidence counts as unmet"],
  [/ABANDON/,                             "abandonment is terminal handoff"],
];

const missing = required.filter(([re]) => !re.test(section)).map(([, label]) => label);
if (missing.length) fail(`Unlazy section omits ${missing.length} directive(s): ${missing.join("; ")}`);

console.log(`Unlazy section present in CLAUDE.md (${section.length} chars)`);
console.log(`all ${required.length} required directives found`);
console.log("guidance verification passed");
