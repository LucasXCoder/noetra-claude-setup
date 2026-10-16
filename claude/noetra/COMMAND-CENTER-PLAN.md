# Noetra Command Center — Master Plan (noetra.group)

**Status:** v2 — **LOCKED & approved 2026-06-11.** Code gated on Lucas's explicit "build."
**First build:** Head Office vertical slice (Phase A). `noetra.group` domain is registered.
**What it is:** the visual command center for the entire Noetra system — one pane of glass over the
local engine (memory, offices, money, roadmap), in the **Noetra design system** (Apple-level polish ·
3D depth · glassmorphism · cinematic dark · physics motion · awwwards-tier). A living, premium OS you
run from your phone.

---

## 0. North-star & principles
- **The website is glass, not the engine.** Real work runs locally (Claude Code, claude-mem, the agent
  framework/offices, the standup). The site **reads** state and **routes approvals** — never executes
  money, never controls agent behavior.
- **Truth first, game second.** Every visual/score is downstream of **honest agent reporting.** Failures
  are shown, never hidden; concealment is penalized (Honesty Ledger, §2.4).
- **One Noetra aesthetic** (`~/.claude/noetra/DESIGN.md`): **near-pure-black canvas, vibrant accents that
  pop, low-poly 3D with subtle idle motion ("vibration"),** glass material, spring physics. Vibrant + dark.
- **Claude / Max plan only.** Local-first, private, tunneled. **$0 autonomous spend; human approves before
  anything goes live.**

---

## 1. Architecture
```
 Phone / browser ──▶ noetra.group  (the GLASS: React app, read + approve)
        │  Cloudflare Tunnel (auth: passkey)
        ▼
 LOCAL ENGINE (your machine, always-on)
   ├─ Gateway API + WebSocket   (aggregates state, streams live events)
   ├─ AGENT FRAMEWORK           (§2: registry + message bus + honesty ledger)
   ├─ claude-mem worker :37777  ·  capture bridge  ·  Graphify graphs
   ├─ state files (master-todo, standup, self-fund, decisions)
   └─ Claude Code  (does the actual work)
```
- **Gateway API** (new): one local service (Node/Fastify or FastAPI) exposing clean REST + **WebSocket**
  (live office activity, new memories, task progress, approvals). The app never touches files directly.
- **Tunnel:** Cloudflare Tunnel → `noetra.group`, passkey-gated (the site can approve things).
- **Frontend:** Vite · React · TS · Tailwind (DESIGN.md tokens) · React-Three-Fiber/drei · Framer Motion ·
  GSAP · shadcn/ui (`ui-styling`).
- **Graceful "awaiting data":** panels needing not-yet-real data render a beautiful standby, never break.

---

## 2. THE AGENT FRAMEWORK (the engine the Living Offices mirrors)
Decision: **full framework + live mirror.** The offices are the glass over a REAL multi-agent system.
- **2.1 An "agent" = any unit that does a job — script OR AI.** No LLM required; a script that does its
  job is a valid agent. Each declares a **role**.
- **2.2 Agent registry:** every agent registers `{id, office, role, capabilities, inputs/outputs, owner,
  kind: script|ai}`. The registry is the source of truth for who exists and what they do.
- **2.3 Inter-agent message bus:** agents **communicate and hand off work** via typed messages; every
  handoff is logged and auditable. Agents must talk to each other — handoffs are the backbone.
- **2.4 Honesty Ledger (rides the bus):** logs **predicted-vs-actual** per agent/office. Concealing or
  misreporting failure is the **one thing that costs Spark.** Truthful reporting is the only way to score.
  This makes the hard rule a mechanic, not just policy.
- **2.5 Role schema → visual:** each role carries a baseline costume (suit/tie/hat/tool) so the org is
  readable at a glance. The Living Offices (§3.2) renders the registry + bus live.

---

## 3. SECTIONS

### 3.1 Command Center Dashboard — HOME  ·  (Phase A, first)
- **$350 Survival/Vitality meter (hero):** real self-generated revenue vs the $350 target, "Noetra is
  N% self-funded." Drives global **vitality theming** — under target the UI cools/dims; over target it
  warms and the offices/constellation brighten. The stakes ("fund itself or it dies"), made felt.
- **Now strip (live):** what every agent/office is executing this second (WebSocket), read-only.
- **Office status row:** each office tile → state (idle/working/blocked) + headline metric + voxel peek.
- **Today's brief** (full cinematic version §4.2) · **Trading** (LL/MQL paper P&L, awaiting-data until
  rebuild) · **Scholarship progress** · **Token economy** (memory/graph savings) · **System vitals**
  (worker · capture bridge · graph · Max-plan usage · uptime).

### 3.2 The Living Offices — CENTERPIECE  ·  (Phase C, vertical slices)
A 3D **voxel world**; each office is a glowing room/biome with a **team of cute blocky voxel entities**
(the agents) living and working in it — the **live mirror of the Agent Framework (§2).**
- **Core 6 offices (modular — add Financial Advisor / Ops / School later):**
  **Head Office (CEO)** · **Trading (LL/MQL)** · **Scholarship** · **Coding** · **Research/Opportunity** ·
  **Income/Self-Funding.** Each a distinct biome with its own accent (Head=gold/white, Trading=plasma/amber,
  Scholarship=mint, Coding=iris, Research=aurora, Income=green/gold).
- **Entities = one per registered agent; many per office; each visually distinct BY ROLE** so you can
  *look and instantly know each agent's job.* Costumes/suits/ties/hats/tools signal the role.
  - **Example — Scholarship chain:** Research agent (suit+tie, finds scholarships) → Writing agent (essays)
    → Form-filler/Deploy agent (applications) → Submission agent → Manager. Each hands off to the next over
    the message bus; the office shows handoffs as **light-streams**.
- **Living behavior (reflects REAL activity, visual only):** entities animate when their agent is working
  (move to desks, "type," carry results, confer); idle otherwise. Never controls behavior — pure mirror.
- **Game layer (honest):** entities earn **Spark ⚡** from their office's **real output**; real awards/
  badges; **Spark buys cosmetics only** (colors/outfits/hats/ties). Offices **grow** as they perform,
  **dim/flag** when underperforming. Framed as a **living neural network** — cross-office collaboration
  shown as light flowing between rooms. Scores are downstream of the Honesty Ledger (§2.4).
- **Phased:** C1 static rooms + real status; C2 live activity; C3 full game layer + customization studio.

### 3.3 Memory / Second Brain  ·  (Phase B)
3D neural constellation of claude-mem + the Graphify graph, growing live (new captures pop in, clusters
bloom). **People-network cluster** (relationships thicken on recurrence). **Vault browser** (raw-sources →
wiki, citations + backlinks). **Memory health** (contradictions/stale/gaps from the librarian).

### 3.4 Master To-Do / Roadmap  ·  (Phase B)
All lanes from `master-todo.md`: my projects · school · self-funding hunt — each card with name, next
step, status. **Lane board** + a **cinematic chapter-journey map** (Ch.1→4) + **dependency view**. School
lane: courses/deadlines/transfer goals (needs your input).

### 3.5 Self-Funding Engine  ·  (Phase B, tied to Ch.1 Phase 4)
`~/noetra-selffund/` — separate lane. **Ranked opportunity board** (rubric: EV · capital · effort · risk ·
time-to-cash · goal-fit · reversibility). **Approval inbox** (approve queues; never spends). **Revenue
tracker** → feeds the $350 meter. **Safety banner + PAUSE kill-switch** always visible.

---

## 4. Added ideas (locked in)
- **4.1 Vitality theming** — the $350 meter is Noetra's life-force; the whole UI warms/cools with it.
- **4.2 Cinematic morning briefing** — the CEO entity "presents" the overnight standup on open.
- **4.3 Unified Approval Inbox + phone push** — one place, one tap, for everything awaiting you.
- **4.4 Voice layer (Phase A priority)** — "brief me," "approve D1," "MQL status." Routes to Claude locally.
- **4.5 ⌘K ask-the-brain** — global semantic search across memory/wiki/graph.
- **4.6 Time-rewind/replay · 4.7 office channels (read-only) · 4.8 achievements wall · 4.9 alerts engine ·
  4.10 mobile glance mode · 4.11 customization studio · 4.12 cinematic onboarding.**

---

## 5. Design application
- DESIGN.md tokens; **glass over the 3D worlds**; spring-physics motion; `prefers-reduced-motion` honored.
- **Aesthetic lock:** near-pure-black background, **vibrant accents that pop**, **low-poly models with a
  subtle idle vibration/animation.** Cinematic depth, colors forward. Restraint at rest, alive on interaction.

---

## 6. Build order (all Chapter 2) — VERTICAL SLICE
Build ONE office end-to-end, prove the loop, then replicate.

- **Phase A — Shell + Home + Framework + first slice (FIRST):**
  app scaffold + Noetra design kit · Gateway API + WebSocket · Cloudflare tunnel to `noetra.group` + auth ·
  **Home cockpit** ($350 vitality meter, live now-feed, system vitals) · **Approval Inbox** · **⌘K
  ask-the-brain** · **voice layer** · **Agent Framework foundation** (registry + message bus + role schema
  + Honesty Ledger) · **Head Office vertical slice** — the **CEO orchestrator + morning standup/delegation
  loop** (reads master-todo → plans the day → delegates → leaves the brief), mirrored in its voxel room.
  *This delivers Ch.1 Phase 4's core AND the first Command-Center slice in one.*
- **Phase B — Knowledge & control:** Memory/Second Brain (§3.3), Roadmap (§3.4), Self-Funding (§3.5).
- **Phase C — Living Offices, replicate the slice** to the worker offices in order:
  **Income/Self-Funding → Research → Coding → Trading → Scholarship** (mandate priority + readiness).
  Each: real agents + bus + voxel room + Spark + Honesty Ledger. C1 static → C2 live → C3 game layer.
- **Phase D — Delight:** cinematic briefing, time-rewind, achievements, office channels, alerts/push,
  mobile glance, onboarding.

---

## 7. Tech stack
Frontend: Vite · React · TS · Tailwind (tokens) · R3F + drei · Framer Motion · GSAP · shadcn/ui.
Gateway: Node + Fastify + ws (or FastAPI) — local; reads claude-mem DB/API, state files, Graphify json;
REST + WebSocket. Remote: Cloudflare Tunnel + passkey. Voxels: R3F instanced meshes; Spline for hero art.
All local, Claude/Max-only.

---

## 8. Hard rules (enshrined)
1. Glass-only: reads + approves; never runs the engine or moves money.
2. $0 autonomous spend; no execution credentials; human approves before live; PAUSE kill-switch.
3. Game reflects **real** metrics; failures shown; concealment penalized (Honesty Ledger). Never rewards hiding.
4. Claude / Max plan only. Local-first, private, tunneled.
5. Noetra design system, awwwards quality, every surface.

---

## 9. Resolved decisions (v2)
Offices = **Core 6** (+ modular). Currency = **Spark ⚡**. **Vitality theming** = yes. **noetra.group** =
registered. **Voice** = Phase A. **Entities** = one per agent, role-differentiated. **Agent layer** = full
framework + live mirror. **Build** = vertical slice, **Head Office (CEO) first**.

---

## 10. v3 ADDENDUM — merged ideas + AUTONOMOUS BUILD directive (2026-06-21)
Lucas: "reinvent + reimplement — keep the plan AND add the IG-video ideas; loop-build the command center on your own; I'll review/audit when back." Most video ideas were ALREADY in v2 (dashboard · phone access · message bus §2.3 · approval inbox · offices · voice). NEW additions merged in:

- **10.1 Telegram control channel** (new) — a Telegram bot = the fast TEXT channel to the office from the phone (send tasks, get the brief, approve, spin up/manage agents) — complements the visual noetra.group dashboard. Buildable as code; needs Lucas's bot token + the local Gateway running. The dashboard = glass to LOOK; Telegram = the line to TALK.
- **10.2 24/7 daemon + schedulable workflows** (from "Cortex OS") — a persistent local supervisor that keeps the offices running with scheduled workflows (crons that fire agent tasks through the day) + a shared task Kanban agents push through. **HONEST CAVEAT (the wall we keep hitting):** runs only while the machine is ON; the safety system blocks an AI from auto-starting unsupervised agents, so **Lucas enables/runs the daemon; the office builds the code.** True always-on-while-PC-off = a hosted backend later (his accounts).
- **10.3 Auto-research / self-improvement loop** (Karpathy-style) — agents periodically critique + improve their own deliverables before sending; ties to the Honesty Ledger (§2.4). Build as a recurring "review-and-improve" pass in the agent framework.
- **10.4 Skill packs** — bundled skills (research · content · outreach · custom) the offices invoke; ties to skill-creator + the Anthropic Skills Marketplace work. Custom-skill + automation slots.
- **10.5 Productize + sell** (his agency angle / Ch.4) — package the whole command center so it can be given to team members OR sold to clients. The **offices** are the differentiator vs everyone's one-click dashboards. Build modular/white-labelable from the start.
- **Borrow, don't bolt:** pull specific ideas/components from GitHub agent-OS repos, but keep OUR design + offices as the core (avoid foreign-system integration mess + the install-external-code wall).

### 10.6 AUTONOMOUS BUILD BACKLOG (the loop works through this; Lucas audits when back)
Build to `~/noetra-selffund/build/command-center/`. Code is fine to write autonomously; **deploy / tokens / running daemons / spend = Lucas's gated taps.** Glass-only: reads + approves, never executes money/agents.
1. ✅/🔨 **Home cockpit dashboard MVP** (static, reads state, Noetra design, phone-viewable) — in progress.
2. **Gateway API** (local Node/Fastify or FastAPI: REST + WebSocket; reads claude-mem DB + state files + Graphify; serves the app). 
3. **Dashboard sections**: Approval Inbox · Self-Funding engine (ranked board + revenue→$350 meter) · Roadmap (master-todo lanes) · Memory/second-brain view.
4. **Agent Framework foundation**: registry + typed message bus + Honesty Ledger + role schema (the engine the Living Offices mirrors).
5. **Telegram bot** (control channel; token = Lucas's).
6. **Auto-research/self-improve loop** in the framework.
7. **Living Offices** voxel slice (Head Office first) — heavy, later.
8. **Package/white-label** pass for selling.
**Cadence:** advance 1 component per loop (paced ≤2 build agents/tick, rate-limit aware); keep PermitPulse monitoring alive in parallel; update office/state/command-center-build progress + the DASHBOARD each tick.
