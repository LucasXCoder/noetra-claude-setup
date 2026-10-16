---
description: Hackathon speed mode - demo-first, thin vertical slices, always-runnable main
---
Hackathon mode for: $ARGUMENTS

This overrides the slower parts of the usual workflow for the rest of the session (brainstorming ceremony, formal plans, unlazy ledgers). Quality bar stays: it must run, and the demo must not break.

1. **Frame (5 min, ask me at most 3 questions):** the one-sentence pitch, the judging criteria, the demo audience and time limit, required tech or sponsor APIs. Write them to `HACKATHON.md` in the repo, plus a `CLAUDE.md` with stack, run command and conventions.
2. **Scope for the demo, not the product:** list the 3 moments the demo must show. Everything else is cut. Pick boring, fast tech I already know (Vite + React + Tailwind + shadcn, or Next.js; FastAPI for Python). Fake or hardcode anything the judges cannot see.
3. **Vertical slice first:** get an end-to-end happy path running and deployed or runnable within the first hour, then widen it. `main` always runs. Commit every working step.
4. **Parallelize:** independent pieces (UI, API, data, pitch assets) go to separate subagents or `claude --worktree` sessions with disjoint files. Never two sessions on the same file.
5. **Verify by running:** start the app, drive it with Playwright, take a screenshot, fix what differs. No claiming done without having run it. Use the Chrome DevTools MCP for slow or broken pages.
6. **Polish last 20%:** the Noetra DESIGN.md look, empty/loading/error states on the demo path, a seeded demo dataset, a one-command start (`make demo` or `npm run demo`).
7. **Demo kit:** README with screenshots, a 60-second script in `DEMO.md`, a fallback recording or screenshots in case the live demo fails, a 3-slide pitch.

Rules: do not spend money or create accounts without asking me. Use only Claude for any AI feature in the product unless I say otherwise and give a key. Keep secrets in `.env`, never committed.
