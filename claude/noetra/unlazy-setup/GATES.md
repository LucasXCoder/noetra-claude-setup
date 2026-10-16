# Gates: unlazy self-setup

Scope: unlazy is installed, its enforcement provably works on this Windows machine, the Stop hook actually blocks, and the fan-out guidance is recorded where every session reads it

- [x] G0: this ledger states outcomes that can fail
  CHECK: node lint-ledger.mjs
  EXPECT: ledger lint passed
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\unlazy-setup; path=34b20a9bc5da/53 entries; output=LINT OK (1 warning(s)) | ledger lint passed

- [x] G1: the skill is installed with an intact file set and sources that parse on this runtime
  CHECK: node verify-install.mjs
  EXPECT: install verification passed
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\unlazy-setup; path=34b20a9bc5da/53 entries; output=parsed 9 sources on v24.14.1 | install verification passed

- [x] G2: the skill's own regression suite passes on this machine
  CHECK: node verify-suite.mjs
  EXPECT: suite verification passed
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\unlazy-setup; path=34b20a9bc5da/53 entries; output=ran 7 suites declared in package.json scripts.test, every one exit 0 | suite verification passed

- [x] G3: the checker refuses to certify a failing oracle
  CHECK: node verify-enforcement.mjs
  EXPECT: enforcement verification passed
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\unlazy-setup; path=34b20a9bc5da/53 entries; output=exercised 4 fixtures: 1 positive control certified, 3 failure modes refused | enforcement verification passed

- [x] G4: Claude Code routes the unlazy skill from its registry
  EVIDENCE: manual: after clone the session skill registry listed unlazy with its frontmatter description; Skill tool invocation returned the SKILL.md body and base directory ~/.claude/skills/unlazy

- [x] G5: the installed Stop hook blocks a stop while gates are unmet and releases otherwise
  CHECK: node verify-hook.mjs
  EXPECT: hook verification passed
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\unlazy-setup; path=34b20a9bc5da/53 entries; output=drove 3 states: 1 blocked on unmet gates, 2 correctly allowed the stop | hook verification passed

- [x] G6: fan-out guidance is recorded where every session reads it
  CHECK: node verify-guidance.mjs
  EXPECT: guidance verification passed
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\unlazy-setup; path=34b20a9bc5da/53 entries; output=all 10 required directives found | guidance verification passed
