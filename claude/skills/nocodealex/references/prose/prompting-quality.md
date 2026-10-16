# Prompting patterns and output quality

## What he believes (CORE first)

- **A single Claude is a yes-man** `g08-0249` `g20-0168` `y02-0185`. It grades its own app as amazing, issues and all `y02-0132` `r02-0122`. Asking the same Claude "is this good?" is theater `g20-0171`, and telling it to double-check its writing barely helps `g21-0070`. His fix is structural: blind independent judges, forced quotes, calibrated scales, no rounding up `g07-0296` `g06-0159`.
- **Never soften, never invent.** His panel skills forbid flattery, softened verdicts and praise the reviewers did not give `r01-0019` `r02-0199`. Use only what the user said, label guesses "assumed", or leave a placeholder `r01-0015` `r02-0111`, such as `[ADD YOUR NUMBER: what to count]` `r03-0220` `r03-0335`. Put "Mark missing evidence instead of inventing it" in the prompt `g13-0250`.
- **Ask or flag, never guess** `g20-0293`: ask for missing numbers `g20-0022`, ONE question at a time `r01-0020`, say when unsure `g20-0249`.
- **Don't trust "done"** `g15-0091` `y03-0054`: verification loop with a stop condition `g02-0239`, before/after evidence `g01-0195` `r03-0336`.
- **Structure beats phrasing.** Of 50 tips he tested, 46 were forgettable and 4 changed his defaults `g19-0035` `g19-0036`. All four are about structure `g19-0037`: who reviews the work, what can physically stop a bad action, where the work runs, and how many versions you keep `g19-0038`.
- **Show, don't describe.** Claude matches well and invents taste badly `g13-0083`. Give it a REFERENCE instead of a wish `g20-0120`. Generic design is not a prompting problem `g13-0082` `g20-0119`.
- **Save, don't re-paste:** project instructions cover every chat `g20-0074` `g20-0289`; "the difference between a trick and a system" `g20-0075`.

## Frameworks and methods

**Opus 5.5 / Fable 5 checklist.**
1. Delete "think carefully" lines and control depth with effort (low to max) instead `g05-0059` `g05-0317`.
2. Hand over the whole task in one message `g05-0060`.
3. Name the finish line, e.g. "the tests pass" `g05-0061`.
4. Say when it should stop and ask you `g05-0062`.
5. Then don't interrupt `g05-0063`.

For Fable 5 the three fixes are: give it an example, make it lead with the answer, and give it a goal rather than a script `g23-0004` `g23-0009`.

**Prompt Audit (CLAUDE.md cleanup).** Remove "double-check your work", ALL CAPS and step scripts `y03-0068` `y03-0069` `y03-0070`: capitals over-fire `g12-0102`, scripts override better plans `g12-0104`. Cleanup gave ~2 points accuracy on the same model `g12-0097`; one audit found ~70 fixes `y03-0072`.

**Verification loop**, from the Claude Code team `y03-0053`. Claude tests its own work (clicks the new button, screenshots it), fixes and re-tests until it works `y03-0057` `y03-0058`. Instructions raise effort but miss wrong self-reported numbers and stalls `g16-0149` `g16-0150`, so unlazy moves enforcement into files and checks `g16-0151` `g16-0010`.

**Darwin Loop.** Make three candidates, pick the winner and evolve it into three more. Repeat `g13-0222` `y04-0042`.

**Swarm Loop.** Three critics each hunt a different weakness; the writer fixes, they re-check `g13-0242` `y04-0050` `y04-0052`. Darwin explores, Swarm verifies `y04-0056`; neither is official `g13-0223` `g13-0244`.

**Best-of-five.** Never ask once `g20-0093`. "Treat each one as if it is the only version that ships" `g20-0098`, then end with `THE JOB:` and the task `g20-0100`.

**Interview first.** Grill Me walks a design tree until nothing is silently assumed `g01-0170` `g01-0175`. Family-tree rules: one question at a time, smaller question on "don't know", flag contradictions, mark UNCONFIRMED `g22-0033` `g22-0036` `g22-0037` `g22-0038`.

**Evidence-anchored critique.** Every critique quotes the exact line `g04-0246` `r03-0205`. /launch GO/NO-GO verdicts cite a file and line, or a command and its output `r02-0132`.

**Karpathy's four formats** make errors visible `g09-0014`: ASD-STE100 controlled English `g09-0006`, a diagram `g09-0008`, a slider web page `g09-0010`, an animated explainer `g09-0012`.

## Exact prompts, tools, numbers

- **Brutal mode:** "Be brutally honest with me on this. No compliments, no softening, no 'this is great, but.' Tell me the real problems and what you would fix first." `g23-0042`. The other codes (Eli5, steelman it, pre-mortem, receipts) are toc-only `g23-0044` `g23-0047`.
- **Opus 5.5 design ban:** no cream background, italic headline accents, 01/02/03 labels, mono labels or pill buttons. Ban whatever style it switches to next `g13-0025` `g13-0031`.
- **Starter CLAUDE.md:** "Lead with the answer, then the reasoning. No preamble." `g20-0248`.
- **Scope creep:** "Do only what was asked. Suggest the extra change in one line and wait." `r03-0128`.
- **/learn rule shape:** one line, under 25 words, names a command or file `r03-0093` `r03-0094`.
- **Numbers:** /awwwards re-scores to 8/10 `g02-0147`. Opus 5.5 writing: 10 of 12 measures better, em dashes 15.2 to 0.8 per 1k, hedges +97% `g12-0219` `g12-0221` `g12-0230`; type `/straight-talk` first `y03-0085`. I Have ADHD: 94 words to 35 `g01-0119`. Humanizer: 16/16 blind wins `g01-0150`.
- **Anthropic study** (52 engineers): AI group 50% vs 67%, 17% lower, ~2 minutes faster `g04-0182` `g04-0183` `g04-0185`. Explainers scored 65%+, full delegators under 40% `g08-0016` `g08-0020`.
- **Injection:** Claude may obey hidden lines in pasted text; mark which words are yours `g11-0164` `g11-0167`.

## Contradictions and caveats

- **Self-check:** "double-checking barely helps" `g21-0070` vs the Forge Loop self-grading `g23-0030`. Self-checks count only with tests or evidence behind them.
- **Ban lists:** "prohibition list" and "hard length caps" are toc-only mistakes `g15-0035` `g15-0036`, yet he gives a named design ban list `g13-0024`.
- **Experts:** "act like an expert" is a mistake, yet ORACLE invokes "the single most qualified expert" `g23-0092`.
- **Thinking:** "always thinks" `g05-0059` vs adaptive thinking `g15-0025`.
- **One prompt:** the video says Darwin/Swarm build whole apps `y04-0038`; the guide calls it illustrative `g13-0235`.
- **Questions:** Grill Me numbers every question at once `g01-0171` vs one at a time `r01-0020`.
- **INFERRED:** /iq as an honest-judge recipe `g06-0030`; real-environment verification `g06-0263`.

## What to load next

`topics/agent-teams.md` (panels), `topics/claude-code-mastery.md` (hooks, unlazy, CLAUDE.md), `topics/skills-mcp-ecosystem.md` (installs), `topics/prompting-quality.md` (every atom).
