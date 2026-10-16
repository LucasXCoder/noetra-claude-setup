# Phase 4 — Autonomous Mode (Chapter 1 finale)

> The income engine that makes Noetra fund its own $350/mo. Claude runs self-directed across
> the offices, researches and proposes opportunities, and leaves a morning brief.
> **HARD RULE — Claude researches, builds, and proposes fully autonomously, but a human
> approves before ANY real money is risked.** Autonomous spend ceiling = **$0**.

Everything runs on **Claude via the Max plan only** (no external providers — see CLAUDE.md).
This doc is the build spec; it's dormant until we start Phase 4.

---

## 1. The Morning Standup Loop (core)
A **CEO / Head-Office agent** runs every morning before Lucas wakes:

```
  ┌─ trigger (≈6:00am, pre-wake) ───────────────────────────────────────────┐
  │ 1. WAKE      CEO loads MASTER TODO (~/.claude/noetra/master-todo.md)     │
  │              + claude-mem + yesterday's plan/results + goals             │
  │ 2. REVIEW    Reconcile yesterday: planned vs done, per lane/office       │
  │ 3. PLAN      Allocate today per MASTER TODO priority (#1 LL, #2 Vault    │
  │              Loader …); update each item's next-step/status              │
  │ 4. DISPATCH  Spawn office workers (RuFlow swarm, Max plan)              │
  │      ├─ Trading Office     → LL/MQL rebuild, backtests, MC (NO live trades)
  │      ├─ Scholarship Office → Vault Loader, find/draft submissions       │
  │      ├─ School/Deadlines   → Citrus deadlines, transfer (USC/Col/UCLA)   │
  │      ├─ Research/Opp Office→ hunt + evaluate opportunities, write proposals  │
  │      └─ Brain Hygiene (wkly)→ noetra-librarian health-check: distill new raw-sources,
  │                               flag wiki contradictions/stale notes                       
  │ 5. RESEARCH  Overnight/morning hunt: Polymarket, Kalshi, new tools,      │
  │              income ideas → score (EV · effort · risk · goal-fit)        │
  │ 6. AGGREGATE CEO compiles results + proposals + decisions-pending        │
  │ 7. BRIEF     Write morning brief + push to phone                         │
  │ 8. PERSIST   Write all results/learnings to claude-mem (compounds)       │
  └─ wait for human → approvals processed on wake; money-actions gated ──────┘
```

Each cycle **reads from and writes to claude-mem shared memory**, so allocation and opportunity
scoring get smarter every day.

## 2. Architecture
| Layer | What | Where |
|---|---|---|
| **CEO / Head Office** | Orchestrator agent: review → plan → dispatch → brief | RuFlow "queen" in `~/noetra-offices`, Max plan |
| **Office workers** | Trading, Scholarship, School/Deadlines, Research/Opportunity | RuFlow swarm workers (Task tool: haiku for scans, sonnet/opus for evaluation) |
| **Shared memory** | Compounding context + structured state | claude-mem + `~/noetra-offices/state/` files |
| **Scheduler** | Fires the standup pre-wake | Primary: Claude Code scheduled routine (cron). Fallback: Startup-folder launcher + "is-it-morning" guard (Task Scheduler needs elevation we don't have) |
| **Approval gate** | Money/decisions queue → human | `state/decisions-pending.md` surfaced in brief; phone push |
| **Brief delivery** | The morning output | `state/brief-YYYY-MM-DD.md` + PushNotification / Odysseus phone-approval |

## 3. State files (`~/noetra-offices/state/`)
- `daily-plan.md` — today's allocation per office (CEO writes)
- `standup-log.md` — append-only log of each morning cycle
- `proposals/` — one md per opportunity (thesis, EV, risk, cost, recommendation)
- `decisions-pending.md` — queue of items awaiting human approval (esp. anything costing money)
- `brief-YYYY-MM-DD.md` — the morning brief
- claude-mem holds the durable cross-session memory; state files are the working surface.

## 4. Opportunity hunting — a STANDALONE, AI-OPERATED side project
**Mission:** Noetra builds and runs its OWN side project, by itself with minimal human help, that
throws off a realistic **~$350/mo** to fund Noetra. **Self-funding or it dies.** Simple.

**OUT OF SCOPE (do NOT propose):** LL, MQL, and Noetra itself are Lucas's separate things — not the
product, not for sale here. The Scholarship Office and underwear brand are also separate efforts.
This hunt is its own clean side project, unattached to those.

**TOP criterion: operational autonomy** — can the AI build AND operate it nearly solo (generate,
schedule, publish, maintain on its own), so Lucas's involvement is approval + the few things only a
human can do (own a domain, hold the payout account)? Favor projects that run on autopilot.

**Scope (any legitimate, AI-operable method):** programmatic-SEO / affiliate / ad-supported content
sites the AI auto-builds and updates · faceless automated content channels or newsletters · automated
data/alert products (collect public data → publish/sell access) · AI-generated digital products on
autopilot · tiny self-serve utilities · anything new it discovers. The `data-scraper-agent` skill is
a ready engine for the autonomous collect→enrich→publish loop.

**Process:** research broadly (WebSearch/WebFetch + public APIs, all read-only) → score EVERY
candidate on the rubric → **rank them** → for each top opportunity write a proposal to
`proposals/` with a **short build/execution plan** (steps, time-to-first-dollar, what's needed) →
surface the BEST ranked in the brief.

**Scoring rubric (unchanged):** expected value · capital required · effort · risk · time-to-cash ·
goal-fit (esp. $350/mo mandate & transfer narrative) · reversibility. Rank by fastest realistic
path to $350/mo, weighting low capital + low effort + high goal-fit.

**Safety (unchanged):** no funds/wallets/exchange/broker execution credentials are connected;
markets are analyzed, never traded; everything is a **proposal only** (§5).

## 5. Money safety — how the HARD RULE is enforced
1. **No execution credentials** for any broker/exchange/payment processor exist on the machine; agents physically cannot move money.
2. **Autonomous spend = $0.** Anything costing money is a **proposal only** → `decisions-pending.md`.
3. **Human approves, human executes** (or explicitly authorizes within a pre-agreed limit) — never the agent unilaterally.
4. Trading offices run **backtests / Monte Carlo / paper only**; LL/MQL stay simulation until a human flips them live.
5. Kill switch: a `state/PAUSE` file halts all autonomous cycles.

## 6. Morning brief format
```
# Noetra Morning Brief — <date>
## Done yesterday   (per office: ✅/⚠️/❌ + one line)
## Today's plan     (per office: top 1-3 tasks)
## Opportunities    (each: name · EV · cost · risk · recommendation)
## ⚠️ Awaiting your approval   (money/decisions — nothing acted on yet)
## Notes / blockers
```

## 7. Build milestones
- **M1** State scaffolding (`state/` dir + file schemas + claude-mem conventions)
- **M2** CEO standup agent (review→plan→brief) run manually end-to-end
- **M3** Wire the 4 office workers on RuFlow (Max plan)
- **M4** Opportunity research + scoring rubric + `proposals/` + `decisions-pending`
- **M5** Scheduler (cron routine) + morning phone notification
- **M6** Approval workflow + verify the $0 money-gate
- **M7** Feedback loop (results → claude-mem → smarter next allocation)

## 8. Guardrails / risks
- **Money:** §5 hard gate. · **Token/rate budget (Max):** time-box cycles, cap iterations, haiku for routine scans, opus only for evaluation; stagger office runs.
- **Runaway loops:** max-iteration + wall-clock limits, `PAUSE` kill switch.
- **Web research:** read-only, never authenticate or transact, treat links cautiously.
- **Privacy:** all local (claude-mem + state files); no external providers.

## 9. Decisions to confirm when Phase 4 starts
- Wake/standup time + cadence (daily? weekdays?).
- Scheduler: Claude Code cloud routine vs local launcher (confirm Max-plan cost model for cloud routines).
- Brief delivery channel (file only / phone push / email).
- Opportunity scope + risk appetite (which domains, max proposed capital per idea).
- Whether *approved* trades ever auto-execute within a preset limit, or always stay manual.
