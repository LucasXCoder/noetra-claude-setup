# GATES - memory-system repair (2026-09-25)

Owner: "is the memory thing that we did to lower usage working with the brain and links"; "FIX ALLL THAT"; "ADD everything that supposed to be in there".
Found: the Noetra capture bridge never auto-started (unquoted spaced path) and crashed on large transcripts; the vault graph refresh never ran
(same bug); claude-mem's AI observer kept capturing on the Max allowance until it ran out; the vault wiki and project notes were empty.

- [x] G1: the streaming v2 capture bridge is running and completing full passes.
    CHECK: python memory_check.py --bridge
    EXPECT: BRIDGE OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=BRIDGE OK  1 process(es) | last full pass 57s ago | 1191 transcripts tracked
- [x] G2: the bridge has written the backlog into the one global memory with no LLM.
    CHECK: python memory_check.py --captured
    EXPECT: CAPTURED OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=CAPTURED OK  97 no-LLM memories in the global 'noetra' memory since the fix, latest 2026-09-26T01:30:05.339Z
- [x] G3: both startup launchers quote their paths, so the bridge and the graph refresh start at logon.
    CHECK: python memory_check.py --launchers
    EXPECT: LAUNCHERS OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=LAUNCHERS OK  both startup scripts quote their spaced paths; both startup shortcuts present
- [x] G4: claude-mem's AI note-taker is switched off in every hooks copy and recall is served without an LLM.
    CHECK: python memory_check.py --observer
    EXPECT: OBSERVER OFF OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=OBSERVER OFF OK  no AI-feeding claude-mem hooks in any copy; recall served by noetra-recall-hook.py (no LLM)
- [x] G5: recall returns real past memories through the new hook.
    CHECK: python memory_check.py --recall
    EXPECT: RECALL OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=RECALL OK  recall hook injected 9000 chars with no LLM; search returned 20 memories
- [x] G6: the vault holds every project note, cited wiki topics, the month-goal briefing, and the master note links them.
    CHECK: python memory_check.py --vault
    EXPECT: VAULT OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=VAULT OK  10 project notes | 21 cited wiki topics | month-goal briefing | master note links every project
- [x] G7: the graph covers the filled vault.
    CHECK: python memory_check.py --graph
    EXPECT: GRAPH OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=GRAPH OK  52 vault files in the graph, 21 wiki topics
- [x] G8: CLAUDE.md describes the repaired memory system so every session knows it.
    CHECK: python memory_check.py --docs
    EXPECT: DOCS OK
  EVIDENCE: exit=0; shell=C:\WINDOWS\system32\cmd.exe; cwd=~\.claude\noetra\memory-fix; path=16240b19625f/53 entries; output=DOCS OK  CLAUDE.md describes the repaired memory system
