# Noetra context — projects, goals, roadmap, offices, parked tools

Moved out of `~/.claude/CLAUDE.md` on 2026-10-16 so it is not re-sent with every message.
Read this when planning, prioritising, running the standup, or when a request names a project.

## Active projects (one line each — deep context in claude-mem)
- **BirdQuant** — algo trading platform (decompiled); `~/Downloads/BirdQuant_Source`, launch `start.bat`.
- **Odysseus** — self-hosted AI desktop app fork (Electron, Council mode, phone approval); `~/odysseus`.
- **Liquidity Lizard (LL)** — Python dual-regime futures bot, TopstepX/ProjectX API (EMA mean-rev + trend pullback). **Rebuild after file loss.**
- **Master Quant Lab (MQL)** — Tauri/React/Python companion to LL: Monte Carlo, prop-firm barrier sim, `.llstrat` JSON. **Rebuild.**
- **Scholarship Office** — multi-agent → $50K+/yr auto scholarship submissions; React UI, Postgres "Vault" (32 tables done), Playwright. **Next: Vault Loader.**
- **404 Protocol** — Y2K hacker pager; Pi Zero 2W, ST7789 1.9" TFT + SSD1306 OLED, 5 buttons, SSH dev.
- **Underwear brand** — glow-in-dark waistband stitching; Alibaba manufacturing research.
- **Noetra** — this AI OS; foundation = Phase 1 (memory/agents/design). Offices + self-building agents roadmap.
- **PermitPulse** (self-funding lane, `~/noetra-selffund/`) — **FIRST business graduated from the Self-Funding Office.** Weekly permit-alert service: every new pool/solar/roofing permit in a metro → sold to contractors at **$99/mo**. **LIVE in Austin** (Chicago built/dormant); first warm lead = **the first warm lead**. HQ → `~/noetra-selffund/business/permitpulse/HQ.md`. The office runs it autonomously (leads · copy · weekly lists · CRM); **Lucas's only manual step = tap Send in the phone Gmail app** (outbound email is human-gated by Claude Code safety — by design). Mon = auto-generate the first lead's first list.

## Yearly goals
- **Noetra self-funds: $350/mo from its own output — NON-NEGOTIABLE** (Income Office: trading, Scholarship Office, SaaS, storefronts). Never out of pocket.
- **Transfer to USC / Columbia / UCLA, Fall 2027** — strong GPA at Citrus; narrative around LL, Noetra, Scholarship Office.
- **Scholarship Office live & filing** — $50K+/yr, funds everything else.
- **Rebuild LL + MQL** → live profit on TopstepX, then SaaS (founding-member pricing).
- **Launch underwear brand** — first product made & selling. **Ship 404 Protocol** — finished hardware.
- **Be the greatest** — build because it's the mission.

## Roadmap — CHAPTERS (the real shape — locked)
**CHAPTER 1 — THE BEST CLAUDE** (current)
- Phase 1 Foundation (memory + graph) ✅ · Phase 2 Agent offices ✅ · Phase 3 Design system ✅
- **Phase 4 — AUTONOMOUS MODE (Ch.1 finale, NEXT):** the income engine that funds the $350/mo.
  **Morning Standup Loop:** a CEO/Head-Office agent runs each morning pre-wake → reviews
  yesterday across offices → checks projects/deadlines/focus → allocates the day to each office
  (Trading LL/MQL · Scholarship · School/deadlines · Research) → does autonomous opportunity
  research overnight across ANY legitimate money-making method fitting my skills/assets (trading,
  micro-SaaS, selling to Claude Code users, products, content, services — see Phase 4 spec),
  scores + ranks them, writes proposals w/ build plans →
  reads/writes claude-mem so it compounds → leaves a **morning brief** (done / planned today /
  decisions awaiting approval). **HARD RULE: researches, builds, proposes fully autonomously,
  but a human approves before ANY real money is risked (autonomous spend = $0).**
  Full build spec → **`~/.claude/noetra/PHASE4-AUTONOMOUS-MODE.md`**.

**CHAPTER 2 — THE COMMAND CENTER** — the `noetra.group` dashboard, phone-accessible, real-time
view of every office, task, and system. **Plan (v2 locked) → `~/.claude/noetra/COMMAND-CENTER-PLAN.md`.**
Build = vertical slice, **Head Office (CEO) first** (its standup/delegation loop = Phase 4 core).
Living Offices = live mirror of a real agent framework (registry + message bus + Honesty Ledger);
agents = script or AI; Spark ⚡ cosmetics; near-black + vibrant low-poly aesthetic.

**CHAPTER 3 — THE REAL WORLD** — scheduling + receptionist agent: calls, calendar, physical-world actions.

**CHAPTER 4 — NOETRA AS A PRODUCT** — founding-member pricing, public brand, others can use it.

**Current focus (update weekly):** Chapter 1 complete through Phase 3 ✅. **Next = Phase 4 (Autonomous Mode).**

## Noetra Offices (RuFlow) — scoped, not global
Multi-agent "office" swarm lives in `~/noetra-offices` ONLY (project-scoped MCP+hooks; runs on Max plan, no paid keys). Global sessions stay lean.

## Parked tools — NOT active (dormant, zero context cost)
Saved in `~/noetra-vault/later-tools/` — NOT installed as skills. Activate only at their chapter (audit first). See that folder's README.
- **Open Design** (cloned) — design canvas → **Ch.2**. · **Omma by Spline** (ref, SaaS `omma.build`) — AI 3D scenes → **Ch.2**. · **Embora** (ref, no repo) — storefront builder → **Ch.4**.
