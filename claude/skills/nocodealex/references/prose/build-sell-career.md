# Building, launching, selling, content and career

## What he believes (CORE first)

- **Rehearse before you spend.** Run a decision or launch past simulated critics first: board, sharks, jury, flight controllers, a MiroFish crowd `g09-0254`. Claude's helpful yes is the opposite of what you need before money goes in `g09-0149`.
- **The method is the product, not the tool.** The tools are replaceable; the order of the method is not `g14-0339`. Tools are the easy half of selling an AI service `g15-0101`.
- **Niche down and charge monthly.** Pick one trade, point the tool at the one job it hates, charge a monthly fee `g14-0334`. Or find a repeating complaint, build the one feature people use, and charge less `g19-0239`.
- **Free and open source beats the paid incumbent**, priced against the human service it replaces: bookkeeper, $3,000/month SEO agency, $4,000 brand agency `y02-0188` `g12-0301` `g22-0276`. But free usually means a capped free tier `g17-0194`, a tool you really use is worth paying for `g17-0196`, and prices go stale, so re-check them `g17-0314`.
- **Read the licence.** He reports MIT / Apache 2.0 / AGPL-3.0 because the licence decides whether you can build a business on a repo `g18-0288` `g17-0293` `g18-0266`.
- **Agents draft, the human sends.** career-ops never sends its LinkedIn note `g01-0055`. /hunter never submits, signs or pays `r02-0112`. /agency drafts and you send `r01-0051`. GoLive writes nothing without an approved plan `g02-0084`.

## Frameworks and methods

**Job fit gate.** career-ops: is it still open, does it fit you (score out of 5 against your real CV), is it worth it (ATS-readable CV PDF, cover letter, every field answered), who to talk to (a LinkedIn note) `g01-0045` `g01-0050`–`g01-0054`. It won't push you below 4.0/5 `g01-0052`. /hunter scores out of 100 as the average of recruiter and hiring manager `r02-0080`, with a default threshold of 80 `r02-0014`. Files stay in `.hunter/` `r02-0039`. Answers only you can give stay marked `YOU` `r02-0098`. INFERRED: both cut at roughly 80% fit `g02-0243`.

**Resume: fix the parse before the prose** `g21-0185`. Most rejections are structural: two columns, skills tables, dates the parser can't read `g21-0184`. Four agents run in order: Diagnoser, Recruiter, Rewriter, Hiring Manager `g21-0170`. The Diagnoser tags lines NO METRIC / PASSIVE / VAGUE / NO PROOF / DUPLICATE / DATED and gives a 0–100 score `g21-0179` `g21-0181`. /hiring-panel is an automated screen plus a hiring manager and five readers `g01-0002` `g01-0012`. It adds nothing not in your original `r01-0137`.

**LinkedIn (/linkedin-roast).** Save your profile as a PDF (desktop only) `r03-0144`. Five roasters each give a score out of 10 and one first fix `g04-0159`. Limits: headline 220 characters, About 2,600, banner 1584x396, photo at least 400x400 and under 8 MB `r03-0183`–`r03-0186`. Bullets follow Harvard MCS: action verb, what you did, a result with a number `r03-0158`. Use 8–12 keywords the profile already backs up `r03-0227`, no stuffing `r03-0228`.

**Rehearsal panels.** `/court` has templates for an idea, quitting a job, a post and a big purchase `r01-0196`–`r01-0199`. In the candle case the sentence was: keep the paycheck and write down a stop date and stop level first `r01-0273`. `/shark` offers are practice numbers, not money `r04-0232`. `/launch` polls 8 stations (tests, security, database, speed, cost, users, recovery, rules) `r02-0165`. Launch only on eight GOs, then `/launch --recheck` `r02-0234`. Its demo CaptionPal came back `HOLD: 8 of 8` `r02-0211`.

**Selling services.** Carousels: one industry, build the workflow once, price it as an easy yes, send the exact pitch `g19-0276` `g19-0286`–`g19-0288`. Voice line: build once and reskin per shop `g19-0227`. It closes with "How many calls did you miss last week?" `g19-0234` and says it is an assistant `g19-0236`. Lead machine: Target, Scraper, Verifier, Writer `g19-0117`. Swap the niche and city to re-run it `g19-0119`. Public sources only, and skip sites that ban scraping `g19-0128`. /agency: `setup`, `outbound leads.csv`, `sales prep`, `sales live`, `build`, `support`, `status` `r01-0042`–`r01-0049`, with a `DO-NOT-CONTACT.md` `r01-0064`. Complaint play: look at the Cons of 3–4 star Capterra reviews, not 1-star ones `g19-0265`. 1-star reviews are about downtime: 0 pricing hits against 10 for bugs `g19-0263`.

**Launch stack.** GoLive: Vercel/Netlify, Supabase/Neon, Porkbun/GoDaddy, Resend, Stripe in test mode `g12-0057`–`g12-0061`. Everything goes on your own accounts `g12-0063`. Runable: lock the brief, approve one hero image, ad, landing page, then verify signups and checkout `g13-0216`–`g13-0220`.

**Content.** Reddit Ask lists pain points, you open the sources, then paste them into Claude `g10-0004`–`g10-0007`. Carousels get a Claude Project with the prompt in its instructions `g20-0076`–`g20-0080`. `repurpose.md` and `trends.md` take `$ARGUMENTS` `g21-0222` `g21-0231`. YouTube doesn't pay for mass-produced templates `g20-0059`. 16 faceless channels were removed in Jan 2026 `g20-0062`.

## Numbers worth quoting

santifer's run: 740 posts evaluated, 68 applications, 12 interview processes, 1 offer `g01-0047`. INFERRED rates: 9.2% applied, 17.6% reached interview `g01-0049`. The 15 business tools total $1,057/month at top tier, $870 switchable `g17-0167`. INFERRED: the ten AI tools total $521 at the second tier `g17-0219`.

## Contradictions and caveats

- Framer: "up to $45/site" `y03-0127` vs Pro $30, Basic $10 `g17-0212`. The free swap is Lovable `g17-0212` or Durable `g18-0138`.
- CapCut: KEEP at $9 `g17-0187` vs swap $20 Pro to Edits `g17-0214` `g17-0216`.
- Higgsfield and Perplexity are both "swap to free" `g17-0206` `g17-0200` and "pros switch to it" `g23-0179` `g23-0182`.
- The candle break-even is 58 vs about 57 `r01-0260` (INFERRED).
- No tool guarantees an interview `r01-0154` `r02-0044` `r03-0266`. Stripe is test-mode only `g02-0093`. Toc-only: many guide bodies are email-gated `g02-0234` `g12-0149`. INFERRED: a "perfect copycat" carries IP risk `y02-0085`.

## What to load next

`topics/build-sell-career.md` for every atom. agent-teams for how the panels are built. skills-mcp-ecosystem for installs. usage-limits, because panels spend your plan.
