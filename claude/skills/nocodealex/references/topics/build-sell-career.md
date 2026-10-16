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

---

## Atom index

<!-- AUTO:atoms BEGIN -- regenerated by build_topics.py, do not edit below -->

*1237 atoms.*

### analogy

- `g12-0158` *STATED* — Claude Marketplace opening to developers is the iPhone App Store in 2008 again.
  > “It's the iPhone App Store in 2008 again.”
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *analogy-for* `g12-0155`

### bio

- `g01-0046` *CORE* — career-ops was built by santifer with Claude Code as its brain.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0044`

- `g02-0100` *STATED* — career-ops was built by santifer with Claude Code as its brain.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0098`
  ↳ *evidence-for* `g01-0046`

- `g03-0061` *STATED* — career-ops was built by santifer with Claude Code as its brain.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0059`
  ↳ *evidence-for* `g01-0046`

### caveat

- `g01-0055` *CORE* — career-ops never sends the LinkedIn note it drafts; you send it yourself.
  > “It never sends it.”
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *qualifies* `g01-0054`
  ↳ *example-of* `g01-0194`
  ↳ *example-of* `g02-0237`

- `g02-0093` *STATED* — GoLive's payments provider is Stripe, live-tested only in test mode.
  > “Stripe (test mode)”
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *qualifies* `g02-0080`

- `g04-0041` *INFERRED* — Sending Harvey's cold email from a separate domain keeps any deliverability or spam-reputation damage off your main business domain.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *qualifies* `g04-0040`

- `g04-0053` *STATED* — Although Harvey is free software, Alex's guide has a 'What it costs' section and a 'The catch' section about running it (bodies locked).
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *qualifies* `g04-0029`
  ↳ *example-of* `g04-0242`

- `g05-0140` *INFERRED* — Mortiflix is AGPL-3.0, unlike the MIT tools in Alex's guides: building a hosted service on modified Mortiflix code carries copyleft source-sharing obligations.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *qualifies* `g05-0128`
  ↳ *qualifies* `g05-0322`
  ↳ *example-of* `g18-0288`

- `g05-0248` *STATED* — The Founder guide has a catch qualifying simulated business validation.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *qualifies* `g05-0238`
  ↳ *qualifies* `g09-0197` — simulated validation has a catch; fake customers are not real ones

- `g06-0172` *STATED* — The Anthropic Startup Stack is made of offers from independent partner companies, not from Anthropic itself.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *qualifies* `g06-0170`

- `g07-0268` *STATED* — Alex's /linkedin-roast guide includes 'Worth knowing before you rely on it' and 'Where the numbers come from' sections (email-gated).
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`

- `g10-0008` *STATED* — Alex Chen's Reddit AI search guide has a section 'Before you rely on it: the honest part' with caveats on trusting Reddit's AI answers (body locked).
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *qualifies* `g10-0002`
  ↳ *example-of* `g10-0270`
  ↳ *example-of* `g17-0306`

- `g12-0065` *INFERRED* — Because the go-live skill configures Stripe only in test mode, switching to live payments that take real money remains a separate step you do yourself.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *qualifies* `g12-0061`
  ↳ *qualifies* `g02-0093`

- `g12-0260` *STATED* — Anthropic's speed numbers are measurements of its own apps; they show what the fixes did there, not what the same changes will do to a different codebase.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *qualifies* `g12-0257`
  ↳ *qualifies* `g12-0258`
  ↳ *qualifies* `g12-0259`

- `g13-0060` *STATED* — Alex's Higgsfield guide ends with a 'Before you spend' section of checks before putting money into the API.
  — [g-higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy](https://chen.media/guides/higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy)
  ↳ *qualifies* `g13-0045`
  ↳ *example-of* `g12-0303`

- `g13-0066` *STATED* — A scraped lead is only useful with evidence that the business fits your criteria and a contact route you can verify.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *qualifies* `g13-0064`
  ↳ *qualifies* `g19-0115` — a scraped lead is only useful with evidence it fits and a verifiable contact route

- `g13-0067` *STATED* — The SCRAPE reel's 'unlimited leads' and 'zero detection' are shorthand, not guarantees.
  > “The reel uses shorthand such as “unlimited leads” and “zero detection.” Those are not guarantees.”
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *qualifies* `g13-0061`
  ↳ *qualifies* `g19-0111` — 'unlimited leads' is shorthand, not a guarantee

- `g13-0160` *STATED* — Treat a Public APIs entry as a starting point: the provider's current documentation and pricing determine what you can build.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *qualifies* `g13-0156`
  ↳ *evidence-for* `g17-0314`
  ↳ *qualifies* `y04-0081` — provider docs and pricing decide what you can build

- `g13-0161` *STATED* — A free API tier may require an account or key, cap your requests, or exclude commercial use.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *example-of* `g13-0160`
  ↳ *evidence-for* `g17-0194`
  ↳ *qualifies* `y04-0086` — free tiers may need a key, cap requests or exclude commercial use

- `g13-0162` *STATED* — The Public APIs directory does not grant permission to use every listed service without restrictions.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *qualifies* `g13-0160`

- `g13-0195` *STATED* — HackingTool is a toolkit, not an automatic guarantee that an application is secure.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *qualifies* `g13-0189`
  ↳ *qualifies* `r02-0119` — a check toolkit is not an automatic guarantee an app is secure

- `g13-0210` *STATED* — Runable's credit costs, available models and plan limits can change.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *qualifies* `g13-0208`
  ↳ *evidence-for* `g17-0314`

- `g14-0343` *STATED* — The three-services guide has 'honest notes' on what none of the tools removes (the real work still remains).
  > “the honest note on what none of them removes”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0329`
  ↳ *example-of* `g14-0348`
  ↳ *evidence-for* `g15-0101`
  ↳ *example-of* `g17-0306`

- `g15-0143` *STATED* — 3D scroll websites have real costs, stated honestly in the guide, which closes with a checklist (locked).
  — [g-how-3d-scroll-websites-actually-work-and-how-to-get-one-from-one-prompt](https://chen.media/guides/how-3d-scroll-websites-actually-work-and-how-to-get-one-from-one-prompt)
  ↳ *qualifies* `g15-0140`
  ↳ *example-of* `g15-0177`
  ↳ *example-of* `g17-0306`

- `g17-0172` *STATED* — The swap prices were checked the week the guide went out: the links do not move, the prices do.
  > “The links do not move; the prices do.”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0168`
  ↳ *example-of* `g17-0307`
  ↳ *evidence-for* `g17-0314`

- `g17-0189` *STATED* — Ghost's managed hosting is paid, but the Ghost software itself is free.
  > “Their managed hosting is paid. The software is not”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0185`

- `g17-0194` *CORE* — Free usually means a free tier, not unlimited.
  > “Free usually means a free tier, not unlimited.”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0193`
  ↳ *example-of* `g17-0306`
  ↳ *qualifies* `g17-0314`

- `g17-0295` *STATED* — career-ops does not log into job boards for you, does not fill in application forms and does not send anything.
  > “It does not log into job boards for you, it does not fill in application forms, and it does not send anything.”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0294`
  ↳ *qualifies* `g01-0053` — career-ops drafts field answers but does not itself fill in or submit forms
  ↳ *evidence-for* `r02-0053`
  ↳ *contrast* `r02-0025` — career-ops does not fill application forms; /hunter prepares an answer for every field and opens the page for you

- `g17-0302` *STATED* — Alex Chen lists the honest limits of his career-ops guide.
  > “Honest limits of this guide”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0297`
  ↳ *example-of* `g17-0306`

- `g17-0314` *CORE* — Free tiers and prices change constantly, so treat any free-tier claim as dated and re-check the vendor page before relying on it.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each) [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts) [g-three-open-source-coding-agents-out-of-china](https://chen.media/guides/three-open-source-coding-agents-out-of-china) [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *qualifies* `g17-0313`

- `g18-0045` *STATED* — Keep paying for DeepL if the translated output is going in front of customers.
  > “Keep DeepL if the output is going in front of customers”
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0044`
  ↳ *example-of* `g18-0028`
  ↳ *evidence-for* `g17-0196`

- `g18-0266` *STATED* — Alex says six of the seven repos are MIT and Open Montage is AGPL-3.0, which is a different commitment.
  > “Six are MIT. Open Montage is AGPL-3.0, which is a different commitment.”
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0265`
  ↳ *qualifies* `g18-0274`
  ↳ *evidence-for* `g05-0140`

- `g19-0059` *STATED* — The six-site guide closes with 'Read this before you trust it', a caveat section on the sweep's results.
  > “Read this before you trust it”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *part-of* `g19-0047`
  ↳ *example-of* `g17-0306`

- `g19-0260` *STATED* — Read the expiry warning in PROMPT 4 before building anything on Capterra access.
  > “see the expiry warning in PROMPT 4 before you build anything on it”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0259`

- `g19-0289` *STATED* — The carousel guide ends with 'Read This Before you Start' and 'The honest part'.
  > “The honest part”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0274`
  ↳ *example-of* `g17-0306`

- `g21-0028` *STATED* — The three-AI-services guide ends with a section titled 'The honest part'.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *part-of* `g21-0019`
  ↳ *qualifies* `g21-0020`
  ↳ *example-of* `g17-0306`

- `g22-0095` *STATED* — Bookkeeping guide section 'Check it before you trust it' covers verifying Claude's books before relying on them.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`
  ↳ *example-of* `g22-0275`
  ↳ *example-of* `g17-0306`

- `g22-0148` *STATED* — Meta Ads guide section 'Read this before you trust it' covers checks before trusting the connector's actions and numbers.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0145`
  ↳ *example-of* `g22-0275`
  ↳ *example-of* `g17-0306`

- `g22-0235` *STATED* — For exact search volumes in the keyword-gap workflow you can connect a keyword tool.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *contrast* `g22-0236`

- `g23-0125` *INFERRED* — Letting Claude post listings and reply to buyers requires giving it agentic browser or computer access to your resale accounts, so review what it sends.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *qualifies* `g23-0119`

- `g23-0167` *STATED* — The resume keyword rewrite must stay truthful: hit every keyword, truthfully.
  > “Rewrite to hit every keyword, truthfully”
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *qualifies* `g23-0170`

- `r01-0058` *STATED* — /agency live call coaching needs a transcription app that writes the call to a text file as you talk.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0045`

- `r01-0154` *CORE* — /hiring-panel does not guarantee an interview or a job, and it is not career or legal advice.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0018`
  ↳ *qualifies* `r01-0116`

- `r01-0260` *INFERRED* — The candle trial is inconsistent on break-even: the prosecution opening says 58 sales a month while the rebuttal, Statistician and judge say about 57 ($1,600 / $28 = 57.1, so 58 whole sales).
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0259`
  ↳ *qualifies* `r01-0242`

- `r02-0040` *STATED* — Your resume still goes to Claude like anything else you give it, even though /hunter's files stay local.
  > “Your resume goes to Claude like anything else you give it.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0039`
  ↳ *evidence-for* `g01-0058`

- `r02-0043` *STATED* — Many application forms are built with scripts and can't be read ahead of time; when that happens, paste the questions into /hunter and it answers them.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0012`

- `r02-0044` *STATED* — /hunter is made by language models: a high score and a tailored resume don't guarantee an interview or a job.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0315`
  ↳ *evidence-for* `r01-0154`

- `r02-0261` *STATED* — DATABASE watch: migration 002 drops users.bio with no copy and no way back, no migration can be undone, and DROP COLUMN needs SQLite 3.35+ (VPS version unchecked; the Mac had 3.54).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0258`
  ↳ *qualifies* `r02-0239`

- `r03-0163` *STATED* — /linkedin-roast cannot post to LinkedIn for you: you paste everything in yourself.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0170`
  ↳ *qualifies* `r03-0135`

- `r03-0164` *STATED* — LinkedIn does not publish how it ranks profiles; keywords make your profile match what recruiters type, but they do not promise a rank, interviews or connection requests.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0170`
  ↳ *qualifies* `g04-0163`

- `r03-0187` *STATED* — Saving a LinkedIn profile as a PDF works on desktop only (Me, View profile, then More or Resources, then Save to PDF) and for English profiles only.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0182`
  ↳ *qualifies* `r03-0144`

- `r03-0266` *STATED* — Nothing /linkedin-roast produces guarantees interviews, connection requests or a job.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *generalizes* `r03-0164`
  ↳ *evidence-for* `r01-0154`
  ↳ *qualifies* `r03-0135`

- `r04-0232` *STATED* — /shark is not connected to the TV show; the sharks are language models and the offers are practice numbers, not real money and not financial advice.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0213`
  ↳ *qualifies* `y02-0184` — /shark offers are practice numbers from language models, not real investors

- `r04-0266` *STATED* — /shark host rule: the offers are practice numbers from language models, not real money and not financial advice; say so once if the user treats an offer as a valuation.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0242`
  ↳ *qualifies* `r04-0232`

### claim

- `g01-0004` *STATED* — When a company rejects you it almost never says why, so job seekers send the same resume to the next dozen jobs and hope.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *because* `g01-0005`

- `g01-0041` *STATED* — Claude Resume Kit outputs LaTeX that you compile on your own machine.
  — [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything)
  ↳ *part-of* `g01-0034`
  ↳ *example-of* `g01-0196`

- `g01-0057` *CORE* — career-ops keeps everything on your machine: no telemetry, no backend.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *qualifies* `g01-0044`
  ↳ *example-of* `g01-0196`
  ↳ *example-of* `g02-0240`

- `g01-0058` *CORE* — With career-ops your CV only goes to the AI you use.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0057`

- `g01-0062` *STATED* — career-ops pans a large pile of job posts (740 in santifer's case) down to your shortlist.
  — [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud)
  ↳ *part-of* `g01-0044`

- `g01-0064` *STATED* — career-ops is the open-source Claude job hunter that sorts jobs for you.
  — [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j)
  ↳ *example-of* `g01-0045`
  ↳ *part-of* `g01-0044`

- `g01-0158` *STATED* — ReelMimic learns how the reference was made but never reuses the original footage, characters, logos or assets.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *qualifies* `g01-0155`

- `g02-0002` *STATED* — Most people spend hours filling out job applications and never hear back.
  > “Most people spend hours filling out applications and never hear back.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *because* `g21-0172`
  ↳ *evidence-for* `r02-0002`

- `g02-0008` *STATED* — Job hunting is the same chore on repeat: find the posting, work out if you fit, edit the resume, write a cover letter, type your details into a form, and then nothing comes back.
  > “Job hunting is the same chore on repeat”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *evidence-for* `g02-0002`
  ↳ *evidence-for* `r02-0002`

- `g02-0081` *STATED* — Claude can build an app in minutes, but getting it in front of real users still means accounts, hosting, a database, a domain and secrets.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)

- `g02-0096` *STATED* — Guide headline: know if a job is worth applying to before you start, because career-ops scores it out of 5 against your CV.
  > “Know If a Job Is Worth Applying Before You Start”
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a)
  ↳ *contrast* `g02-0097` — same guide body, two different hooks
  ↳ *example-of* `g02-0242`
  ↳ *part-of* `g01-0044`

- `g02-0097` *STATED* — Guide headline asks '200 applications, zero replies?' and pitches career-ops as showing which of those jobs were never worth sending.
  > “200 Applications, Zero Replies? career-ops Shows Which Jobs Were Never Worth Sending”
  — [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *example-of* `g02-0242`
  ↳ *part-of* `g01-0044`

- `g02-0112` *STATED* — career-ops keeps everything on your machine: no telemetry, no backend.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0098`
  ↳ *example-of* `g02-0240`
  ↳ *evidence-for* `g01-0057`

- `g02-0113` *STATED* — With career-ops your CV only goes to the AI you use.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *qualifies* `g02-0112`
  ↳ *evidence-for* `g01-0058`

- `g02-0209` *STATED* — Editing talking-head videos is mostly cutting: the ums, the false starts, the dead air between takes.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *leads-to* `g02-0211`

- `g02-0243` *CORE* — Both job tools Alex features gate effort behind a fit score: /hunter scores out of 100 with a default threshold of 80, career-ops scores out of 5 and won't push below 4.0, so both cut at roughly 80% fit.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill) [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *generalizes* `g01-0052`
  ↳ *generalizes* `r02-0014`

- `g03-0065` *STATED* — career-ops checks a posting is still live before you write a word.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0060`
  ↳ *evidence-for* `g01-0050`

- `g03-0066` *STATED* — career-ops scores the role against your real CV and will not push you to apply below 4.0/5 (you can override it).
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0060`
  ↳ *because* `g03-0063` — the 4.0/5 bar explains why few posts become applications
  ↳ *evidence-for* `g01-0052`

- `g03-0067` *STATED* — career-ops tailors an ATS-readable CV PDF for roles worth applying to.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0060`
  ↳ *evidence-for* `g01-0053`

- `g03-0068` *STATED* — career-ops drafts a cover letter and the answer to every application field.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0060`
  ↳ *evidence-for* `g01-0053`

- `g03-0069` *STATED* — career-ops finds the hiring manager or recruiter and drafts a short LinkedIn note, but never sends it.
  > “It never sends it.”
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *example-of* `g03-0011`
  ↳ *part-of* `g03-0060`
  ↳ *evidence-for* `g01-0054`

- `g03-0070` *STATED* — career-ops scan mode checks 100+ pre-configured company job boards (Anthropic, OpenAI, ElevenLabs, Retool, n8n and more) for new roles.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0060`
  ↳ *evidence-for* `g01-0056`

- `g03-0071` *STATED* — career-ops keeps everything on your machine: no telemetry, no backend, and your CV only goes to the AI you use.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *example-of* `g03-0012`
  ↳ *qualifies* `g03-0059`
  ↳ *evidence-for* `g01-0057`

- `g04-0031` *STATED* — Harvey finds businesses that fit your ideal customer, such as local businesses.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0032`
  ↳ *part-of* `g04-0029`

- `g04-0032` *STATED* — Harvey reads each prospect's website and learns something specific about that business.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0033`

- `g04-0034` *STATED* — Harvey reads the replies to its cold emails and works each conversation toward a meeting.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *contrast* `r01-0052` — Harvey answers replies itself; /agency support only drafts and you send

- `g04-0040` *STATED* — Harvey needs a mailbox to send from, and its README recommends Gmail or Google Workspace on a separate sending domain.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)

- `g04-0097` *STATED* — When a company rejects a job applicant it almost never says why, so people send the same resume to the next dozen jobs and hope.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *leads-to* `g04-0098`
  ↳ *evidence-for* `g01-0004`

- `g04-0147` *STATED* — Nobody tells you why a recruiter scrolled past your LinkedIn profile.
  > “Nobody tells you why a recruiter scrolled past your LinkedIn profile.”
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)

- `g05-0225` *STATED* — 3D Asset Server downloads are ready to drop into a game or a website.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`

- `g06-0171` *STATED* — Anthropic's startup program is open to bootstrapped, pre-seed and venture-backed startups.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *qualifies* `g06-0170`

- `g07-0051` *STATED* — Alex says an AI agency used to mean a team on payroll.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *contrast* `g07-0052` — payroll team vs agents
  ↳ *evidence-for* `r01-0039`

- `g07-0055` *STATED* — Most people trying to run an AI automation agency are stuck doing all five jobs alone.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *because* `g07-0052`

- `g07-0059` *STATED* — The outbound agent also produces a file you can send all the emails from with your own email.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — outbound agent
  ↳ *evidence-for* `r01-0086`

- `g07-0244` *STATED* — Nobody tells you why a recruiter scrolled past your LinkedIn profile.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *because* `g07-0246`
  ↳ *evidence-for* `g04-0147`

- `g07-0248` *STATED* — /linkedin-roast rewrites your headline, your About section and every job, and makes a banner file and a headshot prompt.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *evidence-for* `r03-0135`

- `g07-0251` *STATED* — /linkedin-roast gives you five reviews for free, then fixes the profile.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *evidence-for* `g04-0149`

- `g07-0264` *STATED* — /linkedin-roast makes a banner file at LinkedIn's size.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0248`
  ↳ *evidence-for* `r03-0150`

- `g07-0265` *STATED* — /linkedin-roast writes a prompt for your headshot to paste into your own image tool.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0248`
  ↳ *evidence-for* `r03-0151`

- `g07-0272` *STATED* — Most AI video tools give you a loose clip you still have to cut, voice and score yourself.
  — [g-syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent](https://chen.media/guides/syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent)
  ↳ *contrast* `g07-0273`

- `g08-0030` *STATED* — After the panel, /hiring-panel rebuilds your resume with every mistake fixed.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0028`
  ↳ *evidence-for* `r01-0137`

- `g08-0033` *STATED* — Job seekers apply to dozens of jobs and never find out why companies say no.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *because* `g08-0034`
  ↳ *leads-to* `g08-0035`
  ↳ *evidence-for* `r01-0117`

- `g08-0034` *STATED* — When a company rejects you it almost never says why, so you send the same resume to the next dozen and hope.
  > “When a company rejects you it almost never says why, so you send the same resume to the next dozen and hope.”
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *evidence-for* `g01-0004`

- `g08-0162` *STATED* — You pay every month for apps that do a handful of things you actually use; Replica rebuilds an app like that as your own version.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *leads-to* `g08-0156`
  ↳ *evidence-for* `g08-0262`

- `g08-0224` *STATED* — /rival answers who will beat you before a real competitor does.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *qualifies* `g08-0220`
  ↳ *example-of* `g09-0254`

- `g09-0176` *STATED* — Logo sites charge you every year for a template.
  > “Logo sites charge you every year for a template.”
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *contrast* `g09-0177`

- `g09-0178` *STATED* — On most logo sites you type your business name, pick a template and pay every year; the result looks like a thousand other logos and the files are never really yours.
  > “What you end up with looks like a thousand other logos, and the files are never really yours.”
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *qualifies* `g09-0176`
  ↳ *example-of* `y02-0188`

- `g09-0194` *STATED* — Most launches find out whether anyone cares on launch day, when it's too late to change the page, the price or the ad.
  > “Most launches find out whether anyone cares on launch day, when it's too late to change the page, the price or the ad.”
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)

- `g09-0197` *STATED* — MiroFish lets you run the launch first, on people who don't exist.
  > “MiroFish lets you run the launch first, on people who don't exist.”
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *contrast* `g09-0194`
  ↳ *example-of* `g09-0254`

- `g09-0212` *STATED* — Your app sits still for eight hours every night.
  > “Your app sits still for eight hours every night.”
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)

- `g10-0009` *STATED* — Reddit is where people describe their problems in their own words, before anyone has sold them a solution.
  > “Reddit is where people describe their problems in their own words, before anyone has sold them a solution.”
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *because* `g10-0002`

- `g10-0010` *STATED* — The old problem with Reddit research was reading enough of it: ten threads, three hundred comments, half of them jokes.
  > “ten threads, three hundred comments, half of them jokes”
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *contrast* `g10-0013`

- `g10-0013` *STATED* — Tapping Ask on Reddit gives you one answer summed up from real posts and comments, with a link to every source it used, instead of a list of threads.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *defines* `g10-0001`

- `g10-0015` *STATED* — Asking Reddit's AI what people in your niche keep struggling with returns a list of real pain points, each one traceable to the threads where people said it.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *evidence-for* `g10-0014`
  ↳ *example-of* `g10-0005`

- `g10-0017` *STATED* — Building content and products from real Reddit pain points means you never have to guess what to make.
  > “so you never have to guess what to make”
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *because* `g10-0016`
  ↳ *evidence-for* `g19-0239`

- `g10-0018` *STATED* — Reddit's Ask button sits right next to the search field, in both the Reddit app and on reddit.com.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0001`

- `g10-0019` *STATED* — On Reddit, pressing Enter in search gives the usual list of posts; tapping Ask gives an AI answer instead.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *qualifies* `g10-0018`

- `g10-0020` *STATED* — Reddit's AI search reads real posts and comments across many communities and sums them up into one answer.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0001`

- `g10-0021` *STATED* — Every Reddit Ask answer links to the posts and comments it came from, plus the communities where you'll find more.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *enables* `g10-0006`
  ↳ *part-of* `g10-0013`

- `g10-0235` *STATED* — When Lovable credits run out, you wait or you pay more.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *because* `g10-0234`
  ↳ *qualifies* `g17-0212` — Lovable credits run out; then you wait or pay more

- `g10-0244` *STATED* — Every Dyad file sits on your computer: open it in VS Code, push it to GitHub, deploy it to Vercel or your own server, with no lock-in.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *enables* `g10-0230`

- `g12-0052` *STATED* — Claude Code can build you an app in an afternoon; getting it in front of real users is where most people stall.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *because* `g12-0053`
  ↳ *leads-to* `g12-0051` — problem the skill solves
  ↳ *evidence-for* `g02-0081`

- `g12-0053` *STATED* — Taking an app live needs hosting, a database, a web address, email that actually arrives, and payments, each with its own account, keys and dashboard.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *evidence-for* `g02-0081`

- `g12-0057` *STATED* — Go-live skill hosting: Vercel or Netlify; it creates the project, moves your app's settings over and deploys it.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`
  ↳ *evidence-for* `g02-0089`

- `g12-0058` *STATED* — Go-live skill database: Supabase or Neon; it creates the database and connects your app to it.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`
  ↳ *evidence-for* `g02-0090`

- `g12-0059` *STATED* — Go-live skill web address: Porkbun or GoDaddy; it points your own domain at the app and checks it serves over HTTPS.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`
  ↳ *evidence-for* `g02-0091`

- `g12-0060` *STATED* — Go-live skill email: Resend; it sets up your sending domain so your app's emails can go out.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`
  ↳ *evidence-for* `g02-0092`

- `g12-0061` *STATED* — Go-live skill payments: Stripe, in test mode; it adds the test keys and the webhook, and checks a test-card payment.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`
  ↳ *evidence-for* `g02-0093`

- `g12-0062` *STATED* — Go-live skill sign-in: Supabase Auth; it configures signup, email confirmation and password-recovery settings.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`
  ↳ *depends-on* `g12-0058` — both on Supabase
  ↳ *evidence-for* `g02-0094`

- `g12-0063` *STATED* — Everything the go-live skill sets up lands on your own accounts: you own the hosting, the database and the domain, not the skill.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *qualifies* `g12-0051`
  ↳ *evidence-for* `g02-0080`

- `g12-0130` *STATED* — SEO agencies charge hundreds of dollars, often thousands, to audit a website.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *contrast* `g12-0131`
  ↳ *example-of* `g22-0276`

- `g12-0136` *STATED* — Slow pages lose visitors, and Google measures all three Core Web Vitals.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)

- `g12-0137` *STATED* — SEO skill indexing check: pages Google can't crawl or index, including blocked pages, broken sitemaps, canonical mistakes and redirect chains.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0133`

- `g12-0138` *STATED* — A page Google can't find can't rank, so indexing problems come out as Critical in the SEO skill's report.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *qualifies* `g12-0137`

- `g12-0139` *STATED* — SEO skill local-search check: your Google Business Profile (categories, hours, photos, reviews) and whether your name, address and phone match everywhere.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0133`
  ↳ *because* `g12-0140`

- `g12-0140` *STATED* — Missing Google Business Profile info keeps a business out of the map results for 'near me' searches.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)

- `g12-0141` *STATED* — SEO skill AI-answers check: whether your pages give short, self-contained answers Google's AI Overviews and AI Mode can quote, using question-style headings, clear sources and structured data.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0133`
  ↳ *example-of* `y01-0112`

- `g12-0142` *STATED* — Google's own guidance is that optimizing for AI search is still SEO.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *evidence-for* `g12-0141`
  ↳ *qualifies* `y01-0112` — Google: optimizing for AI search is still SEO
  ↳ *qualifies* `y01-0111` — Google says AI search optimization is still SEO, so Google search still matters

- `g12-0144` *STATED* — SEO skill content, on-page and schema check: E-E-A-T signals, titles and headings, internal links, images, and Schema.org markup it can validate or write for you.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0133`

- `g12-0145` *STATED* — Content, on-page and schema checks carry most of the SEO skill's health score.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *qualifies* `g12-0144`
  ↳ *qualifies* `g12-0134`

- `g12-0157` *STATED* — Alex's plugin guide offers five weekend-sized plugin ideas and the exact steps from an empty folder to a live Claude Marketplace listing.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`

- `g12-0160` *STATED* — Developers who were on the App Store shelf early got found without fighting a million other apps for attention.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *leads-to* `g12-0161`
  ↳ *part-of* `g12-0158`

- `g12-0185` *STATED* — SupoClip takes one long video in and puts scored vertical clips out, with face tracking and word-synced captions.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0184`

- `g12-0191` *STATED* — SupoClip renders vertical 9:16 clips with the speaker kept in frame and subtitles synced word by word.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0185`

- `g12-0255` *STATED* — Most of what Anthropic found slowing claude.ai are ordinary web-app bugs, which is why they're worth checking for in your own code.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *leads-to* `g12-0251`
  ↳ *evidence-for* `r02-0127`

- `g12-0270` *STATED* — Polsia sets up the pieces a company needs: a live app, a payments account, an email inbox and a code repo.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0267`
  ↳ *contrast* `g12-0053` — Polsia sets up the company stack itself; the go-live skill sets it up on your own accounts after approval

- `g12-0273` *STATED* — Polsia is free to start, with no credit card.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *qualifies* `g12-0267`

- `g13-0152` *STATED* — The fastest way to make a prototype useful is often to connect it to real data.
  > “The fastest way to make a prototype useful is often to connect it to real data.”
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *contrast* `g13-0063` — API data vs scraped page data

- `g13-0207` *STATED* — The goal of the Runable workflow is a consistent set of brand assets you can inspect before publishing.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *part-of* `g13-0204`

- `g13-0209` *STATED* — Runable's model list includes GPT and Claude options.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *part-of* `g13-0204`

- `g14-0288` *STATED* — A solo business still has marketing, social media, design, finance and legal work.
  > “A solo business still has marketing, social media, design, finance and legal work.”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`

- `g14-0331` *STATED* — Of Alex's three sellable services, two are built on free repos and one runs on a tool that is not a repo and cannot be downloaded.
  > “the honest note on which of the three you cannot download”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0329`

- `g14-0332` *STATED* — Three AI tools already exist that a person will pay you to run for them.
  > “Three things already exist that a person will pay you to run for them.”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0329`
  ↳ *enables* `g14-0334`

- `g14-0333` *STATED* — None of Alex's three services asks you to write an app or be technical enough to build one from nothing.
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *qualifies* `g14-0332`

- `g15-0005` *STATED* — The motion gap is what a design agency bills you for, and Skiper UI, Vengeance UI, Animmaster Lib and React Bits close that gap with copy-and-paste code.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *because* `g15-0001`

- `g15-0049` *STATED* — The LinkedIn-skills guide explains all eleven skills in plain words, getting it running, and how to get value from it (22 numbered steps, bodies locked).
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *part-of* `g15-0041`

- `g15-0097` *STATED* — Three free open-source projects each turn one small input into a finished product a business already pays a freelancer for, and all three install in minutes.
  — [g-three-free-ai-tools-you-can-sell-as-a-service](https://chen.media/guides/three-free-ai-tools-you-can-sell-as-a-service)
  ↳ *evidence-for* `g14-0332`

- `g16-0229` *STATED* — There is a reason AI subscriptions pile up in the first place.
  > “Why the subscriptions pile up in the first place”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *qualifies* `g16-0218`

- `g16-0242` *STATED* — There is a software cost nobody is actually counting.
  > “The cost nobody is actually counting”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *qualifies* `g16-0234`

- `g17-0171` *STATED* — Swapping the six KEEP tools costs more in time than it saves in money.
  > “swapping them costs more in time than it saves in money”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)

- `g17-0193` *STATED* — Every paid AI tool in Alex Chen's ten-tools guide has a free alternative that does the same job for most people.
  > “Every paid tool below has a free alternative that does the same job for most people.”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0313`

- `g17-0294` *STATED* — career-ops runs locally inside an AI coding tool you already have open.
  > “It runs locally inside an AI coding tool you already have open.”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0291`
  ↳ *evidence-for* `g01-0057`

- `g17-0296` *STATED* — career-ops reads, judges, drafts, and hands the result back to you.
  > “It reads, judges, drafts, and hands the result back to you.”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *contrast* `g17-0295`
  ↳ *evidence-for* `g01-0055`

- `g17-0299` *STATED* — Alex Chen's career-ops guide explains why your application file never got read, the part the video has no room for.
  > “why your file never got read”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0298`
  ↳ *example-of* `g17-0305`

- `g18-0026` *STATED* — Alex uses top-tier prices deliberately, because the people who feel a tool bill are the ones on the upper plans.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *evidence-for* `g17-0168`

- `g18-0095` *STATED* — Open Generative AI replaces a monthly video subscription with your own API key.
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *part-of* `g18-0092`

- `g19-0049` *STATED* — All six sites in Alex's unclaimed-money sweep are real government or NAUPA-endorsed sites.
  > “These are real government and NAUPA-endorsed sites.”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *part-of* `g19-0047`
  ↳ *enables* `g19-0050`

- `g19-0050` *STATED* — In the six-site sweep you search your own name for free, and no site on the list charges a fee to search or to claim.
  > “You are searching your own name, for free. No site on this list charges a fee to search or to claim.”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *part-of* `g19-0047`

- `g19-0052` *STATED* — There is no single national unclaimed-money database in the US.
  > “There is no single national unclaimed-money database.”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *because* `g19-0053`

- `g19-0053` *STATED* — Different kinds of holders report unclaimed money to different systems: states, the federal pension insurer, the FDIC, a private retirement registry, and the IRS.
  > “states, the federal pension insurer, the FDIC, a private retirement registry, and the IRS”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *because* `g19-0056` — holders report to different systems

- `g19-0056` *STATED* — Checking one unclaimed-money site and stopping is why most searches come back empty.
  > “Checking one site and stopping is why most searches come back empty.”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *leads-to* `g19-0058`

- `g19-0114` *STATED* — Agencies, Clay and Apollo all do the same job: you name a niche and a city, something finds the businesses, pulls a name, a phone and an email, and hands you a list.
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *qualifies* `g19-0115`

- `g19-0115` *STATED* — Claude Code does the lead-list job for free, and you keep what comes out.
  > “Claude Code does that job for free, and you keep what comes out.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0111`

- `g19-0129` *STATED* — Pointing a scraper at the wrong sources gets you fifty junk rows and a blocked address.
  > “Point a scraper at the wrong sources and you get fifty junk rows and a blocked address.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *because* `g19-0130`

- `g19-0130` *STATED* — Ten minutes of source planning is the whole difference between a scrape and a clean lead list.
  > “Ten minutes of planning is the whole difference between a scrape and a clean list.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *evidence-for* `g19-0122`

- `g19-0221` *STATED* — One missed call is a customer already dialing your competitor.
  > “One missed call is a customer already dialing your competitor”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`

- `g19-0223` *STATED* — Every missed plumbing call is someone with a broken pipe who calls the next plumber ten seconds later.
  > “someone with a broken pipe who calls the next plumber ten seconds later”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *defines* `g19-0221`

- `g19-0224` *STATED* — The shop owner who misses calls is not lazy; he is under a sink with both hands full and cannot reach the phone, and that gap is the entire business.
  > “He is under a sink with both hands full and cannot reach the phone. That gap is the entire business.”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *because* `g19-0225`

- `g19-0226` *STATED* — The shop owner pays you to keep the voice line running.
  > “The owner pays you to keep it running.”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`
  ↳ *evidence-for* `g19-0220`
  ↳ *evidence-for* `g14-0337`

- `g19-0228` *STATED* — Claude writes the voice line's brain; a voice platform and a phone number give that brain a mouth and ears.
  > “Claude writes the brain. You need a voice platform and a phone number to give that brain a mouth and ears”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *enables* `g19-0225`

- `g19-0229` *STATED* — Most voice platforms have a free tier to build the missed-call line on.
  > “most of them have a free tier to build on”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *qualifies* `g19-0228`

- `g19-0243` *STATED* — The core idea of the complaint play is sound; only the mechanics in the video need fixing.
  > “The core idea in the video is sound. ... The mechanics just need fixing.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0239`

- `g19-0245` *STATED* — The pricing math decides whether the price you pick for the undercut product actually makes money.
  > “the arithmetic that decides whether the price you pick makes money”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0242`

- `g19-0258` *STATED* — G2 and Capterra, named in the same breath in the video, behave completely differently for Claude today.
  > “They behave completely differently today.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *contradicts* `g19-0248` — video named G2 and Capterra together

- `g19-0259` *STATED* — Capterra genuinely works with Claude and is the best automatable source in the whole complaint play.
  > “Capterra genuinely works and is the best automatable source in this whole play”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *because* `g19-0257`
  ↳ *enables* `g19-0240`
  ↳ *qualifies* `g08-0167` — Capterra works with Claude; G2 behaves differently

- `g19-0261` *STATED* — One-star reviews are the wrong place to look for a pricing complaint.
  > “One star reviews are the wrong place to look.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0240`

- `g19-0264` *STATED* — One-star reviews are rage about downtime.
  > “One star reviews are rage about downtime.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *because* `g19-0261`

- `g19-0266` *STATED* — Three- and four-star reviewers basically like the product and think the price is off.
  > “written by people who basically like the product and think the price is off”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *because* `g19-0265`

- `g19-0277` *STATED* — The step everyone gets wrong is taking whoever says yes first and ending up running four different businesses at once, with four styles and four learning curves.
  > “end up running four different businesses at once, with four different styles and four different learning curves”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *because* `g19-0276`

- `g19-0279` *STATED* — One industry means one style, one set of words, and one workflow you reuse forever.
  > “One industry means one style, one set of words, and one workflow you reuse forever.”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *because* `g19-0276`

- `g19-0281` *STATED* — By the fifth client in the same industry, you are barely thinking.
  > “By the fifth, you are barely thinking.”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *leads-to* `g19-0280`

- `g19-0282` *STATED* — Good starter industries for a carousel service all need posts, rarely make their own, and are used to paying for services.
  > “they all need posts, rarely make their own, and are used to paying for services”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *defines* `g19-0283`

- `g19-0284` *STATED* — With a carousel service you are not selling design; you are selling the fact that clients never have to think about their feed again.
  > “You are not selling design. You are selling the fact that they never have to think about their feed again.”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *depends-on* `g19-0285`

- `g19-0285` *STATED* — Selling 'never think about your feed again' only works if you know the client's world cold, and you only know it cold by staying in one lane long enough to learn it.
  > “you only know it cold if you stay in one lane long enough to learn it”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *because* `g19-0276`

- `g20-0057` *STATED* — The mass-produced rule is written into the YouTube Partner Program monetization policies, under 'Inauthentic content'; it is not a rumour or a prediction.
  > “That is not a rumour or a prediction. It is written into the YouTube Partner Program monetization policies, under Inauthentic content.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *evidence-for* `g20-0055`

- `g20-0059` *STATED* — YouTube's policy lists as not monetizable: 'AI-generated content made with generic or unoriginal templates giving the impression of mass production without adding the creator's original, authentic insights or perspective.'
  > “AI-generated content made with generic or unoriginal templates giving the impression of mass production without adding the creator's original, authentic insights or perspective.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0057`
  ↳ *evidence-for* `g20-0063` — policy targets templates, not AI per se
  ↳ *qualifies* `g15-0098` — YouTube does not monetize templated mass-produced AI video

- `g20-0060` *STATED* — YouTube's policy also lists as not monetizable: 'Image slideshows, templated storylines, or scrolling text with minimal or no narrative, commentary, or educational value.'
  > “Image slideshows, templated storylines, or scrolling text with minimal or no narrative, commentary, or educational value.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0057`

- `g20-0063` *STATED* — AI is not banned on YouTube; templates are.
  > “AI is not banned. Templates are”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`
  ↳ *qualifies* `g20-0055`

- `g20-0069` *STATED* — The faceless YouTube guide compares 'Doing it by hand vs this' system.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`
  ↳ *example-of* `g20-0282`

- `g20-0088` *STATED* — The carousel guide compares 'Doing it by hand vs this' prompt-driven system.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0070`
  ↳ *example-of* `g20-0282`

- `g21-0020` *STATED* — Alex claims a non-coder can build 3 AI services with Claude and sell them for about $5,000 each.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *part-of* `g21-0019`
  ↳ *contrast* `g19-0220` — sell an AI service for about $5,000 each vs a voice line at $300 a month recurring

- `g21-0024` *STATED* — You do not need to code to sell AI services: each of the three is a real, sellable service.
  > “You do not need to code. Each of these is a real, sellable service.”
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *part-of* `g21-0019`
  ↳ *evidence-for* `g14-0333`

- `g21-0026` *STATED* — Claude does the heavy lifting on these AI services so you can deliver one in a weekend.
  > “Claude does the heavy lifting so you can deliver it in a weekend.”
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *because* `g21-0024`

- `g21-0098` *STATED* — People are using Claude to build premium websites for real clients right now and getting paid.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0094`
  ↳ *qualifies* `g21-0095`

- `g21-0105` *STATED* — On-brand visuals like social posts, ad creatives and pitch slides are what agencies charge thousands for.
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)
  ↳ *part-of* `g21-0104`

- `g21-0172` *STATED* — If the ATS parse fails or the match is weak, a person may never open your resume file.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *qualifies* `g21-0171`

- `g21-0173` *STATED* — Job seekers are not being ignored; they are being filtered by ATS software.
  > “You are not being ignored. You are being filtered.”
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *generalizes* `g21-0172`

- `g21-0184` *STATED* — Most resume rejections are structural: a two column layout, a skills table, or a date format the parser cannot read.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *because* `g21-0185`

- `g22-0082` *STATED* — The $0 bookkeeping setup makes Claude reconcile a year of transactions and hand you a clean profit and loss.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`

- `g22-0083` *STATED* — The Claude bookkeeping setup does what a bookkeeper charges a few hundred a month for, in one chat.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *qualifies* `g22-0082`
  ↳ *example-of* `g22-0276`

- `g22-0085` *STATED* — Pointed at the folder, Claude reads every line, categorizes each transaction the way an accountant would, and gives you a profit and loss you can actually use.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0082`

- `g22-0086` *STATED* — The Claude bookkeeping setup lives or dies on two things: your folder setup and your categorization rules.
  > “The whole thing lives or dies on two things: your folder setup and your categorization rules.”
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`

- `g22-0127` *STATED* — Describe what you are building in one sentence and Claude hands back a whole brand kit: a logo in 5 styles, the exact color codes, a matching font pairing, and social banners ready to post.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *part-of* `g22-0126`

- `g22-0128` *STATED* — The Claude brand studio replaces an agency: no $4,000 and no 3 weeks of revisions.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *qualifies* `g22-0127`
  ↳ *example-of* `g22-0276`

- `g22-0146` *STATED* — Connect Meta's official Ads connector to Claude and run your whole Facebook ad account by typing.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0145`
  ↳ *example-of* `g22-0277`

- `g22-0226` *STATED* — The keyword-gap setup makes Claude find the keywords your competitors rank for and write the articles to outrank them.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`

- `g22-0227` *STATED* — The Claude keyword-gap workflow is what SEO agencies charge $3,000 a month for, in one chat, with no agency and no SEO degree.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *qualifies* `g22-0226`
  ↳ *evidence-for* `g22-0237`
  ↳ *example-of* `g22-0276`

- `g22-0236` *STATED* — The keyword-gap winnability ranking works from on-page signals alone, without a keyword tool.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *qualifies* `g22-0229`

- `g23-0074` *STATED* — Why Gamma wins Presentations in his tier list: Gamma makes a finished, on brand deck from a one paragraph brief.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick)

- `g23-0115` *STATED* — The closet method's summary line is 'One photo in, cash out'.
  > “One photo in, cash out”
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *defines* `g23-0114`

- `g23-0117` *STATED* — Claude estimates what each item would sell for from recent listings.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0121`

- `g23-0118` *STATED* — Claude writes the full resale listing: title, description, price, and which app to post it on.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0122`

- `g23-0119` *STATED* — Claude can then post the listings and answer buyers on your behalf.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0123`
  ↳ *contrast* `g02-0237` — closet flow lets Claude post listings and reply to buyers itself, unlike the usual draft-and-approve gate

- `g23-0163` *STATED* — The four resume prompts stop you getting auto-rejected before a person ever sees your resume.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *because* `g23-0164`

- `g23-0164` *STATED* — Most companies run your resume through an ATS screener before a human reads it.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *evidence-for* `g21-0172`

- `g23-0165` *STATED* — The ATS screener scores your resume on keywords.
  > “It scores you on keywords.”
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *qualifies* `g23-0164`
  ↳ *evidence-for* `g21-0171`

- `g23-0168` *STATED* — A resume must pass two readers in sequence, the keyword-scoring bot and then the human, so the prompts optimise for the bot first and the human last.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *generalizes* `g21-0170`

- `g23-0173` *STATED* — The AI tool you reach for says everything about your level.
  > “The AI tool you reach for says everything about your level.”
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)

- `g23-0174` *STATED* — Beginners default to whatever AI tool is popular.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *part-of* `g23-0173`
  ↳ *analogy-for* `g23-0185` — popular tool vs the one doing the job

- `g23-0175` *STATED* — Pros quietly upgrade to the tool that actually does the job, then move about 10x faster and get paid for it.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *part-of* `g23-0173`

- `g23-0176` *STATED* — Same task, totally different results, depending on the tool.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *qualifies* `g23-0173`

- `r01-0052` *STATED* — The /agency support agent drafts replies; you send them.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0050`
  ↳ *qualifies* `r01-0104`

- `r01-0117` *STATED* — You apply to dozens of jobs and never find out why companies say no; /hiring-panel tells you first.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *because* `r01-0116`

- `r02-0002` *STATED* — The problem /hunter targets: applying to jobs is hours of filling out the same forms for companies that never reply.
  > “Applying to jobs is hours of filling out the same forms for companies that never reply.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *because* `r02-0001` — the pain /hunter solves

- `r02-0039` *STATED* — Everything /hunter makes (profile, resume, packets, log) is saved in `.hunter/` in the folder where you run it and stays on your computer.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0313`
  ↳ *example-of* `g02-0240`

- `r02-0041` *STATED* — /hunter reads public postings only and does not log in to job sites.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0007`
  ↳ *evidence-for* `g19-0128`

- `r03-0147` *STATED* — Everything /linkedin-roast makes goes into one folder, linkedin-roast-output/, in the folder where you ran it.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)

- `r03-0152` *STATED* — /linkedin-roast ends with a five-line checklist of what to paste into LinkedIn.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0147`

- `r03-0233` *STATED* — Harvard College's Mignone Center for Career Success (MCS) does not publish a bullet formula by name; /linkedin-roast uses what the MCS resume guide and its sample resume teach (careerservices.fas.harvard.edu/resources/create-a-strong-resume/).
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *evidence-for* `r03-0159`
  ↳ *part-of* `r03-0232`

- `r03-0235` *STATED* — MCS groups its action verbs by type: leadership, communication, research, technical, teaching, quantitative, creative, helping, organizational.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0234`

- `r03-0237` *STATED* — MCS lists 'not demonstrating results' among the top resume mistakes.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *because* `r03-0236`
  ↳ *evidence-for* `g21-0179`

- `r03-0317` *STATED* — All five roasters agreed (5 of 5) that no experience bullet had a number or a result and most described duties.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0316`
  ↳ *evidence-for* `r03-0236`
  ↳ *evidence-for* `g21-0179`
  ↳ *evidence-for* `r01-0133`

- `y01-0081` *STATED* — Alex pitches ai-agency-claude as doing work that normally needs an entire team, installed with one command.
  > “This is work that you normally need an entire team to do, and somehow this takes one command to install.”
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *evidence-for* `g07-0051`
  ↳ *evidence-for* `y04-0139`
  ↳ *qualifies* `y01-0079`

- `y01-0111` *STATED* — Alex claims most people aren't searching Google anymore - they're asking Claude, ChatGPT and Perplexity.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)

- `y01-0113` *STATED* — Because businesses care whether people can find them through AI tools, ai-agency-claude includes a GEO and SEO team.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *because* `y01-0111`

- `y02-0005` *STATED* — The Harvey agent reads every reply and keeps the conversation going 24/7 until it books you a meeting.
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *contrast* `r01-0050` — Harvey reads replies and keeps conversations going 24/7 on its own; /agency sends nothing without your yes
  ↳ *evidence-for* `g04-0034`
  ↳ *part-of* `y02-0001`

- `y02-0074` *STATED* — The board report prevents the mistakes you would have made, saving you tons of money and time.
  — [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs)
  ↳ *qualifies* `g09-0019`

- `y02-0084` *STATED* — Alex Chen claims the rebuild means you get Duolingo for free and 'can sell a perfect copycat of their app and make money too'.
  > “you get Duolingo for completely free and you can sell a perfect copycat of their app and make money too”
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *evidence-for* `g08-0262`

- `y03-0121` *STATED* — Instead of paying Lovable every month, every line of code from Dyad is yours to take anywhere.
  — [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4)
  ↳ *evidence-for* `g10-0244`
  ↳ *part-of* `y03-0116`
  ↳ *evidence-for* `y03-0208`

- `y03-0126` *STATED* — You own every page Instatic publishes.
  — [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY)
  ↳ *leads-to* `y03-0127`
  ↳ *evidence-for* `y03-0208`

- `y03-0133` *STATED* — With FluidVoice you stop paying Wispr Flow every single month.
  — [OtRSHXUQxAQ](https://youtu.be/OtRSHXUQxAQ) [4xBCskEhIfE](https://youtu.be/4xBCskEhIfE)
  ↳ *example-of* `g16-0235`

- `y03-0144` *STATED* — SupoClip takes one long video and cuts it into ready-to-post shorts so you don't edit everything by hand.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *enables* `g14-0341`
  ↳ *evidence-for* `g12-0185`
  ↳ *part-of* `y03-0143`

- `y03-0150` *STATED* — Out of a one-hour video, SupoClip only gives you back the clips most likely to go viral.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *evidence-for* `g12-0190`

- `y03-0154` *STATED* — Since SupoClip is open source, you run it completely yourself instead of paying every month.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *example-of* `g16-0235`
  ↳ *qualifies* `y03-0143`

- `y03-0157` *STATED* — Runnable writes the copy, generates the ads and builds a website people buy from.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *part-of* `y03-0156`

- `y03-0158` *STATED* — Runnable gives you GPT, Claude, image generation and video generation in one site.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *evidence-for* `g13-0209`
  ↳ *part-of* `y03-0156`

- `y03-0162` *STATED* — Runnable supports a built-in database for signups and Stripe payments.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *evidence-for* `g13-0220`
  ↳ *enables* `y03-0161`

- `y03-0163` *STATED* — Runnable can be tried for free (comment 'Run').
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *example-of* `y02-0194`
  ↳ *evidence-for* `g13-0208`
  ↳ *qualifies* `y03-0156`

- `y03-0164` *STATED* — Reddit's new built-in AI is a gold mine for content research and new business ideas.
  — [Ab_9hEiq6NI](https://youtu.be/Ab_9hEiq6NI)
  ↳ *evidence-for* `g10-0014`

- `y03-0166` *STATED* — Reddit Ask reads real Reddit posts and comments, then sums up the answer with a link to every source.
  — [Ab_9hEiq6NI](https://youtu.be/Ab_9hEiq6NI)
  ↳ *evidence-for* `g10-0001`
  ↳ *part-of* `y03-0165`

- `y03-0169` *STATED* — With Reddit pain-point research you never have to guess what to make, because real people already told you what they need.
  — [Ab_9hEiq6NI](https://youtu.be/Ab_9hEiq6NI)
  ↳ *evidence-for* `g10-0017`
  ↳ *evidence-for* `y03-0164`

- `y04-0032` *STATED* — Runnable bundles GPT, Claude, image generation and video generation in one site.
  > “You get GPT, Claude, image generation and video generation in one site.”
  — [TKrtaLRIHBg](https://youtu.be/TKrtaLRIHBg)
  ↳ *evidence-for* `y03-0158`
  ↳ *part-of* `y04-0031`

- `y04-0036` *STATED* — Runnable supports a built-in database for the signups and Stripe payments (transcribed 'striver payments').
  > “It even supports a built-in database for the signups and Stripe payments.”
  — [TKrtaLRIHBg](https://youtu.be/TKrtaLRIHBg)
  ↳ *evidence-for* `y03-0162`
  ↳ *part-of* `y04-0031`

- `y04-0037` *STATED* — Runnable is free to try, and he pitches it as building 'a whole brand in minutes'.
  > “To try for free, comment Run.”
  — [TKrtaLRIHBg](https://youtu.be/TKrtaLRIHBg)
  ↳ *evidence-for* `y03-0163`
  ↳ *qualifies* `y04-0031`

- `y04-0081` *STATED* — People are turning free APIs into full platforms with real paying users.
  > “People are turning these free APIs into full platforms with real paying users.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *evidence-for* `g13-0168`
  ↳ *evidence-for* `y04-0139`

- `y04-0139` *STATED* — Ironically AI makes owning things easier, because one person can suddenly create far more economic value without needing a massive team.
  > “AI makes this much easier because one person can suddenly create way more economic value without needing a massive team”
  — [HAKXPtoRXh8](https://youtu.be/HAKXPtoRXh8)
  ↳ *evidence-for* `y04-0031` — one person running a whole agency's output
  ↳ *qualifies* `y04-0137`

### concept

- `g07-0054` *STATED* — An AI automation agency is five jobs: finding clients, selling on the call, writing the proposal, building the automation, and keeping clients happy.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *defines* `g07-0052`
  ↳ *leads-to* `g07-0055`
  ↳ *evidence-for* `r01-0041`

- `g12-0149` *STATED* — Guide section 'How the score works' explains how the SEO skill's 100-point health score is built (body email-gated).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *defines* `g12-0134`

- `g12-0194` *STATED* — Guide section 'How it picks the clips' explains SupoClip's clip-scoring logic (body email-gated).
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0184`
  ↳ *qualifies* `g12-0190`
  ↳ *example-of* `g02-0234`

- `g13-0058` *STATED* — Alex's Higgsfield guide has a section 'The cashback, exactly' detailing the $1-for-$1 API cashback terms.
  — [g-higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy](https://chen.media/guides/higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy)
  ↳ *part-of* `g13-0045`

- `g16-0234` *STATED* — Each of the five repos removes a specific meter rather than lowering a price.
  > “each one removes a specific meter rather than lowering a price”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *example-of* `g16-0008`

- `g17-0169` *STATED* — Alex Chen's free-swaps series: part 1 covered creative tools, part 2 covered utilities, part 3 covers the software you pay for to actually run something (hosting, CRM, storefronts, invoicing).
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0167`

- `g18-0288` *CORE* — Alex reports each open source tool's licence (MIT, Apache 2.0, AGPL-3.0) because the licence decides whether you can build a business on it.
  — [g-the-open-source-agent-tool-two-yc-founders-gave-away](https://chen.media/guides/the-open-source-agent-tool-two-yc-founders-gave-away) [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools) [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install) [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)

- `g21-0211` *STATED* — A real content team is five jobs: someone who finds what is trending, someone who writes the hooks, someone who plans the month, an editor who kills the weak posts before they go out, and someone who squeezes a week of content out of every good idea.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0210`
  ↳ *leads-to* `g21-0212`

- `r01-0039` *STATED* — An AI agency used to mean a team on payroll: one person for outreach, one for sales calls, one to build, one to answer clients.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *contrast* `r01-0040` — payroll team vs agents

- `r02-0008` *STATED* — /hunter can source jobs from company career pages, Greenhouse, Lever and Ashby job boards, RSS feeds, or postings you paste in.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0007`

### definition

- `g01-0012` *STATED* — The five parallel /hiring-panel readers are the hiring manager, another applicant for the same job, the CEO, the recruiter with 30 seconds, and the teammate you would sit next to.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *defines* `g01-0011`

- `g17-0293` *STATED* — MIT is the permissive licence: you can use the code, change it and use it commercially, as long as you keep the licence notice.
  > “MIT is the permissive one”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *defines* `g17-0292`
  ↳ *generalizes* `g17-0259` — MIT = commercial use
  ↳ *contrast* `g17-0241` — MIT vs CC0
  ↳ *example-of* `g17-0310`
  ↳ *example-of* `g18-0288`

- `g18-0017` *STATED* — Rowboat is on GitHub under Apache 2.0, 'the permissive one': you can use it commercially, modify it and ship it inside your own product as long as you keep the licence and the notices.
  > “the permissive one”
  — [g-the-open-source-agent-tool-two-yc-founders-gave-away](https://chen.media/guides/the-open-source-agent-tool-two-yc-founders-gave-away)
  ↳ *part-of* `g18-0015`
  ↳ *example-of* `g18-0288`

- `g21-0171` *CORE* — An applicant tracking system (ATS) is software that reads almost every online application before a human sees it: it parses your resume into fields, matches it against the job description, and ranks you.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0170`

- `r01-0079` *STATED* — An /agency leads file is a CSV or a list with name, business, email, and a website or one line about them.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *defines* `r01-0043`

- `r01-0120` *STATED* — The /hiring-panel automated screen decides if a human even sees your resume: can it be read, are titles and dates clear, which of the job's key terms are missing.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0119`
  ↳ *example-of* `g21-0171`

- `r01-0131` *STATED* — /hiring-panel reader 1, the hiring manager, reads for one thing: can this person do the job on day one?
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0128`
  ↳ *contrast* `r01-0127` — two hiring-manager reads: interview decision vs day-one ability

- `r01-0132` *STATED* — /hiring-panel reader 2 is another applicant for the same job, reading as a rival: where is this resume weaker than mine?
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0128`

- `r01-0133` *STATED* — /hiring-panel reader 3, the CEO, reads for impact: what did this person change, and by how much?
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0128`

- `r01-0134` *STATED* — /hiring-panel reader 4, the recruiter, has 30 seconds and 100 resumes today and reads the top third only.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0128`
  ↳ *evidence-for* `g01-0012`

- `r01-0135` *STATED* — /hiring-panel reader 5, the teammate, would work next to this person and reads for how they work with others.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0128`

- `r02-0092` *STATED* — /hunter's `PACKET.md` is everything the user needs to send the application in a few minutes.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0088`

- `r02-0124` *STATED* — /launch TESTS station: runs your tests, type check and build, and finds the parts nothing tests.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0125` *STATED* — /launch SECURITY station: hunts for security holes: leaked keys and passwords, routes anyone can reach, input that reaches your database.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0126` *STATED* — /launch DATABASE station: migrations that destroy data, users who can read other users' rows, missing backups.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0127` *STATED* — /launch SPEED station: heavy pages, queries in loops, lists with no limit, slow calls in every request.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0128` *STATED* — /launch COST station: every paid service your code calls, what it costs at 100 and 1,000 users, and whether a stranger can run up your bill.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0129` *STATED* — /launch USERS station: walks sign up, sign in, the main thing your app does and payment, looking for steps that break.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0130` *STATED* — /launch RECOVERY station: settings nobody wrote down, seeing errors in production, rolling back.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0131` *STATED* — /launch RULES station: a privacy policy and terms when you collect data, deleting a user's data, licences, and promises your code doesn't keep.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0123`

- `r02-0165` *STATED* — The /launch description summarises its 8 checks as tests, security holes, the database, speed, the actual cost, the user's path, recovery, and privacy and rules.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *generalizes* `r02-0123`
  ↳ *evidence-for* `r01-0032`

- `r03-0148` *STATED* — linkedin-roast-output/roasts.md holds the five roasts and what all five agree on.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0147`

- `r03-0149` *STATED* — linkedin-roast-output/new-profile.md holds the new headline (with two alternates), the new About with the keywords it chose and why, and every experience entry before and after.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0147`

- `r03-0150` *STATED* — /linkedin-roast outputs banner.png (and banner.svg): a plain banner at LinkedIn's size, 1584 x 396.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0147`

- `r03-0151` *STATED* — linkedin-roast-output/headshot-prompt.md is a prompt to paste into the image tool of your choice, with your own photo attached.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0147`

- `y01-0112` *STATED* — GEO / AI visibility in Alex's usage: whether a business can be found by people asking AI assistants (Claude, ChatGPT, Perplexity), alongside traditional SEO.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *defines* `y01-0113`

- `y03-0165` *STATED* — Reddit's AI is called Ask, and it is the button right next to the search bar.
  — [Ab_9hEiq6NI](https://youtu.be/Ab_9hEiq6NI)
  ↳ *evidence-for* `g10-0018`
  ↳ *defines* `y03-0164`

- `y04-0138` *STATED* — Things you can own: equity, a business, an audience, products - anything where AI can increase your net worth without all the upside going to somebody else.
  > “this is equity, a business, an audience, products, or anything where AI can increase your net worth without all of that upside going to somebody else”
  — [HAKXPtoRXh8](https://youtu.be/HAKXPtoRXh8)
  ↳ *defines* `y04-0137`

### example

- `g01-0069` *STATED* — khan-explainer blackboard lesson: a diagram drawn stroke by stroke while the voice explains it.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *example-of* `g01-0066`

- `g01-0070` *STATED* — khan-explainer draw-over-UI tutorial: arrows, circles and numbered steps drawn over your own product screenshots.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *example-of* `g01-0066`

- `g01-0071` *STATED* — khan-explainer real-audio clip: a YouTube video or podcast goes in, vertical shorts come out, with the board drawn to the speaker's words.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *example-of* `g01-0066`
  ↳ *contrast* `g01-0152` — repurpose real audio into shorts vs mimic a reference style

- `g05-0247` *STATED* — The Founder guide shows what a real run looks like ('What a real run looks like').
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`

- `g08-0051` *STATED* — Brandon Thomas says he built the PhotoCraft, FilmCraft and EffectCraft suite with Claude, an example of one developer cloning major paid software with Claude.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0050`
  ↳ *evidence-for* `g08-0262`

- `g08-0227` *STATED* — /rival enemy 1: the big company that adds your idea as a feature.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0226`

- `g08-0228` *STATED* — /rival enemy 2: the cheap copycat that clones your idea for a fraction of the price.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0226`

- `g08-0229` *STATED* — /rival enemy 3: the fast startup that ships twice as fast.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0226`

- `g08-0230` *STATED* — /rival enemy 4: the free tool that is good enough to make you pointless.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0226`

- `g08-0231` *STATED* — /rival enemy 5: the customer stealer that goes straight for your first hundred customers.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0226`

- `g12-0261` *STATED* — Guide section 'The em dash that froze the page' covers an em dash that froze claude.ai (body email-gated).
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *part-of* `g12-0250`
  ↳ *example-of* `g12-0255`

- `g12-0262` *STATED* — Guide section 'The reload nobody could see' covers an invisible reload slowing claude.ai (body email-gated).
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *part-of* `g12-0250`
  ↳ *example-of* `g12-0255`

- `g12-0263` *STATED* — Guide section 'The rest of the list' covers the other performance fixes from Anthropic's sprint (body email-gated).
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *part-of* `g12-0250`
  ↳ *part-of* `g12-0255`

- `g13-0155` *STATED* — Alex's PUB guide includes a small verified weather request and copyable Claude Code prompts reusable with other APIs.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *example-of* `g13-0154`

- `g13-0205` *STATED* — Alex's Runable guide walks a fictional headphone launch called Onda through the workflow.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *example-of* `g13-0204`

- `g14-0070` *STATED* — The SETUP guide's test workload is a small competitor-research brief run with the three tools.
  > “Run a small competitor-research brief”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`

- `g14-0108` *STATED* — Agent Reach workflow 1: build a job shortlist you can inspect.
  > “Workflow 1: a job shortlist you can inspect”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`
  ↳ *example-of* `g14-0112`
  ↳ *example-of* `g14-0027`

- `g14-0109` *STATED* — Agent Reach workflow 2: video research with evidence.
  > “Workflow 2: video research with evidence”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`
  ↳ *example-of* `g14-0112`

- `g14-0110` *STATED* — Agent Reach workflow 3: find a useful content pattern.
  > “Workflow 3: find a useful content pattern”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`
  ↳ *example-of* `g14-0112`

- `g17-0173` *STATED* — Free swap 01 of 15 (Ecommerce): Shopify $399/month at top tier, free alternative WooCommerce $0.
  > “Shopify $399 → WooCommerce $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0174` *STATED* — Free swap 02 of 15 (Video Calls): Zoom $22/month at top tier, free alternative Jitsi $0. Marked KEEP: the paid tool genuinely wins.
  > “Zoom $22 → Jitsi $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`
  ↳ *example-of* `g17-0170`

- `g17-0175` *STATED* — Free swap 03 of 15 (Documents): Google Workspace $22/month at top tier, free alternative LibreOffice $0. Marked KEEP: the paid tool genuinely wins.
  > “Google Workspace $22 → LibreOffice $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`
  ↳ *example-of* `g17-0170`

- `g17-0176` *STATED* — Free swap 04 of 15 (Project Management): Asana $30/month at top tier, free alternative Trello $0.
  > “Asana $30 → Trello $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0177` *STATED* — Free swap 05 of 15 (Websites): Webflow $39/month at top tier, free alternative WordPress $0.
  > “Webflow $39 → WordPress $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0178` *STATED* — Free swap 06 of 15 (Hosting): Kinsta $100/month at top tier, free alternative Cloudflare Pages $0.
  > “Kinsta $100 → Cloudflare Pages $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0179` *STATED* — Free swap 07 of 15 (Dashboards): Looker $60/month at top tier, free alternative Metabase $0.
  > “Looker $60 → Metabase $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0180` *STATED* — Free swap 08 of 15 (Heatmaps): Hotjar $80/month at top tier, free alternative Matomo $0.
  > “Hotjar $80 → Matomo $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0181` *STATED* — Free swap 09 of 15 (Remote Access): TeamViewer $50/month at top tier, free alternative RustDesk $0.
  > “TeamViewer $50 → RustDesk $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0182` *STATED* — Free swap 10 of 15 (Screen Recording): Loom $24/month at top tier, free alternative ShareX $0. Marked KEEP: the paid tool genuinely wins.
  > “Loom $24 → ShareX $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`
  ↳ *example-of* `g17-0170`

- `g17-0183` *STATED* — Free swap 11 of 15 (Invoicing): QuickBooks $60/month at top tier, free alternative Invoice Ninja $0.
  > “QuickBooks $60 → Invoice Ninja $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0184` *STATED* — Free swap 12 of 15 (CRM): HubSpot $100/month at top tier, free alternative Twenty $0. Marked KEEP: the paid tool genuinely wins.
  > “HubSpot $100 → Twenty $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`
  ↳ *example-of* `g17-0170`

- `g17-0185` *STATED* — Free swap 13 of 15 (Blogging): Squarespace $52/month at top tier, free alternative Ghost $0.
  > “Squarespace $52 → Ghost $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`

- `g17-0186` *STATED* — Free swap 14 of 15 (Image Editing): Adobe Firefly $10/month at top tier, free alternative GIMP $0. Marked KEEP: the paid tool genuinely wins.
  > “Adobe Firefly $10 → GIMP $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`
  ↳ *example-of* `g17-0170`

- `g17-0187` *STATED* — Free swap 15 of 15 (Video Editing): CapCut $9/month at top tier, free alternative Kdenlive $0. Marked KEEP: the paid tool genuinely wins.
  > “CapCut $9 → Kdenlive $0”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *part-of* `g17-0167`
  ↳ *example-of* `g17-0170`
  ↳ *contradicts* `g17-0214` — CapCut verdict: KEEP, the paid tool genuinely wins (15-swaps) vs swap CapCut Pro to free Edits (ten-tools)

- `g17-0198` *STATED* — IMAGE CREATION: Midjourney Standard $30/month (Basic is $10) swaps to Nano Banana at gemini.google.com.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`

- `g17-0200` *STATED* — AI RESEARCH: Perplexity Max $200/month (Pro is $20) swaps to Consensus at consensus.app.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`
  ↳ *contradicts* `g23-0182` — Perplexity: replace Perplexity Max $200/month with Consensus (ten-tools) vs pros switch to Perplexity for research (pro stack)

- `g17-0202` *STATED* — AVATAR CREATION: HeyGen Pro $99/month (Creator is $29) swaps to Hedra at hedra.com.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`

- `g17-0204` *STATED* — CODE GENERATION: GitHub Copilot Pro+ $39/month (Pro is $10) swaps to Cursor at cursor.com.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`
  ↳ *evidence-for* `g23-0202`

- `g17-0206` *STATED* — VIDEO GENERATION: Higgsfield Plus $39/month (Starter is $15) swaps to Hailuo at hailuoai.video.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`
  ↳ *contradicts* `g23-0179` — Higgsfield: replace Higgsfield Plus $39/month with free Hailuo (ten-tools) vs pros switch to Higgsfield for video (pro stack)

- `g17-0208` *STATED* — IMAGE EDITING: Adobe Firefly Pro $30/month (Standard is $10) swaps to Photoroom at photoroom.com.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`
  ↳ *contradicts* `g17-0186` — Firefly Pro $30 second tier vs Firefly $10 listed as 'highest self serve plan'
  ↳ *contradicts* `g17-0170` — ten-tools swaps Firefly to Photoroom; 15-swaps marks Firefly KEEP

- `g17-0210` *STATED* — SOCIAL SCHEDULING: Buffer Team $12/month per channel (Essentials is $6) swaps to Publer at publer.com.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`

- `g17-0212` *STATED* — WEBSITE BUILDER: Framer Pro $30/month (Basic is $10) swaps to Lovable at lovable.dev.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`

- `g17-0214` *STATED* — VIDEO EDITING: CapCut Pro $20/month swaps to Edits at instagram.com/edits.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`
  ↳ *contradicts* `g17-0170` — ten-tools swaps CapCut to Edits; 15-swaps marks CapCut KEEP

- `g17-0217` *STATED* — VOICE GENERATION: ElevenLabs Creator $22/month (Starter is $5) swaps to MiniMax at minimaxi.com.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *example-of* `g17-0193`

- `g17-0221` *STATED* — Alex Chen's ten-tools guide adds five more paid-to-free AI swaps that did not fit in the video.
  > “Five more that did not fit”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *part-of* `g17-0193`

- `g19-0283` *STATED* — Starter industries for the carousel service: dentists, gyms and studios, real estate agents, restaurants and cafes, med spas, law firms, dental and vet clinics.
  > “dentists, gyms and studios, real estate agents, restaurants and cafes, med spas, law firms, dental and vet clinics”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *example-of* `g19-0276`

- `g21-0109` *STATED* — On-brand asset 1: a week of social posts, 7 on-brand graphics in one go (quote, tip, feature, testimonial, teaser...).
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)
  ↳ *example-of* `g21-0107`

- `g21-0110` *STATED* — On-brand asset 2: ad creatives, with the graphic laid out and the headline + copy written for you.
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)
  ↳ *example-of* `g21-0107`

- `g21-0112` *STATED* — On-brand asset 4: one-pagers & pitch slides: clean sell-sheets and decks in your exact style.
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)
  ↳ *example-of* `g21-0107`

- `r01-0147` *STATED* — Example run: '/hiring-panel ~/Documents/resume.pdf  Senior product designer at a fintech startup'.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0149`

- `r01-0196` *STATED* — /court prompt for a business idea: '/court I want to start [business] for [customer]. I have [money/time], [what I've done so far], and I'd charge [price].'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0194`

- `r01-0197` *STATED* — /court prompt for quitting your job: '/court Quit my job as [job] to do [plan] full time. I have [savings], [income so far], and my monthly costs are [costs].'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0194`
  ↳ *generalizes* `r01-0237`

- `r01-0198` *STATED* — /court prompt for a post before you publish it: '/court This post will get more engagement than my usual posts: [paste the post]. My usual posts get [numbers].'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0194`

- `r01-0199` *STATED* — /court prompt for a big purchase: '/court Buy [thing] for [price]. I'd use it for [reason]. The alternative is [alternative].'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0194`

- `r01-0237` *STATED* — The /court example case: 'Quit my job as a nurse to sell handmade candles on Etsy full time.'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0186`
  ↳ *example-of* `r01-0218`
  ↳ *example-of* `r01-0157`
  ↳ *example-of* `g09-0254`

- `r01-0238` *STATED* — Candle case facts: $8,000 saved; 40 sales in the last 3 months at $28 each; rent $1,600 a month; candles made at home in spare time.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0237`

- `r01-0241` *STATED* — The Statistician juror voted GUILTY: no base rate, and the plan stakes a job and all savings on a more-than-fourfold jump in sales extrapolated from one 40-sale, three-month total with no trend and no stopping point.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0240`

- `r01-0243` *STATED* — Statistician would flip if the case had a month-by-month sales record showing sales rising fast enough to reach about 57 a month inside the five months the savings cover.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0241`

- `r01-0244` *STATED* — The Parent juror voted GUILTY: wouldn't let anyone they love quit nursing and stake $8,000 on candles grossing about $373 a month against $1,600 rent, with no stop point and no way back.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0240`

- `r01-0246` *STATED* — Parent would flip if the record showed a firm way back to nursing, such as an approved leave or a promised re-hire.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0244`

- `r01-0247` *STATED* — The Lawyer juror voted GUILTY: home-made candles carry fire, burn and lease exposure, and the record shows no liability insurance, lease permission, tax plan, health coverage or license upkeep.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0240`

- `r01-0248` *STATED* — Lawyer would flip if the home business were already papered: the landlord's written consent and a product-liability insurance policy.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0247`

- `r01-0249` *STATED* — Defense opening ('go ahead as described'): the plan is a bet on a product that already sells, with five months of rent in savings.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0163`

- `r01-0252` *STATED* — Defense point 1, demand is proven in money: 40 sales at $28; low volume at a proven price is a better starting point than an untested idea.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0249`
  ↳ *example-of* `r01-0251`
  ↳ *contrast* `r01-0259`

- `r01-0253` *STATED* — Defense point 2, the runway is measurable: $8,000 against $1,600 is five months, longer than the three that produced the sales record.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0249`
  ↳ *example-of* `r01-0251`
  ↳ *contrast* `r01-0261` — same runway, read two ways

- `r01-0254` *STATED* — Defense point 3, hours are the variable the plan changes: the record doesn't say whether time or demand caps sales, so full-time hours are the direct test.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0249`
  ↳ *example-of* `r01-0251`
  ↳ *contrast* `r01-0262` — hours vs demand

- `r01-0255` *STATED* — Defense point 4, no new fixed cost: candles are made at home, so the business adds no workshop lease on top of rent already owed.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0249`
  ↳ *example-of* `r01-0251`
  ↳ *contrast* `r01-0263`

- `r01-0257` *STATED* — Prosecution opening: as written, the plan quits a nurse's income on the strength of about $373 a month in gross sales.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0162`

- `r01-0262` *STATED* — Prosecution point 3: nothing shows spare-time sales scale to full time; if demand is the limit, more hours make more stock, not more sales.
  > “If demand is the limit, more hours make more stock, not more sales.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0257`
  ↳ *example-of* `r01-0258`

- `r01-0263` *STATED* — Prosecution point 4: the plan spends the job first and tests demand second — no income target, sales milestone, stop point or reduced-hours step, so the $8,000 is both the test budget and the safety net.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0257`
  ↳ *example-of* `r01-0258`

- `r01-0267` *STATED* — Defense rebuttal: the prosecution's cost line 'sales stay near $373 a month' states only one branch of an admitted unknown.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0262`

- `r01-0269` *STATED* — Prosecution rebuttal: 'spare time' shows hours are scarce, not that hours limit sales.
  > “"Spare time" shows hours are scarce, not that hours limit sales”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0254`

- `r01-0277` *STATED* — Lawyer's deciding fact: a wax-and-flame business sits in a presumably leased home, yet the record is silent on the lease, any insurance and which country's rules apply.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r01-0247`

- `r01-0280` *STATED* — Defense rebuttal of point 1 — 'survives as arithmetic, not as a verdict': $373 a month is what spare-time work produced and says nothing about the full-time rate.
  > “Survives as arithmetic, not as a verdict.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0259`

- `r01-0281` *STATED* — Defense rebuttal of point 2: survives if sales stay flat, but the record is silent on other income and on whether nursing work can be resumed, which decides how final the loss is.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0261`
  ↳ *leads-to* `r01-0246` — way back to nursing becomes the Parent's flip condition

- `r01-0282` *STATED* — Defense rebuttal of point 4: the missing stop point is a real gap, but 40 sales in three months is already a demand test at spare-time scale, so 'tests demand second' overstates it.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0263`

- `r01-0284` *STATED* — Prosecution rebuttal of defense point 1 — survives in part: someone paid, but the plan needs volume, the very thing the defense sets aside.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0252`

- `r01-0285` *STATED* — Prosecution rebuttal of defense point 2 — survives as arithmetic only: five months counts rent alone while sales are gross, with candle cost, fees and other living costs unrecorded.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0253`

- `r01-0286` *STATED* — Prosecution rebuttal of defense point 4 — survives, but beside the point: no lease is added, yet quitting ends the nursing income, whose amount the record never states.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0264`
  ↳ *qualifies* `r01-0255`

- `r02-0013` *STATED* — /hunter gives each job one fit score written like `94/100 (recruiter 96, hiring manager 92)`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0080`

- `r02-0089` *STATED* — /hunter run step 7 (Show the list) prints every continued job as one line, best first, like `94/100  Company, Role (remote)  ready` or `needs you: 2 answers`, then the below-threshold jobs one line each.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`

- `r02-0153` *STATED* — The repo's `examples/captionpal` demo app (an AI caption writer) looks finished and passes its own tests, yet its real launch poll came back HOLD: 8 of 8 stations say NO-GO.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0122` — looks finished, passes own tests, 8/8 NO-GO
  ↳ *example-of* `r02-0118`
  ↳ *example-of* `g09-0254`

- `r02-0154` *STATED* — CaptionPal's poll caught an admin page that hands anyone every user's email and password hash, a paid AI endpoint a stranger could call forever, and a migration that stops the site starting again after its first restart.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0153`

- `r02-0202` *STATED* — CaptionPal is /launch's tiny demo app: an AI caption writer for Instagram posts where you sign up, paste a photo description and get three captions.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *defines* `r02-0153`

- `r02-0205` *STATED* — CaptionPal's mission: people sign up with email and password, paste a photo description, get three AI-written captions saved to find again; the landing page says "Three scroll-stopping captions in one click. Your photos are never stored."
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0178`
  ↳ *example-of* `r02-0179`

- `r02-0207` *STATED* — CaptionPal's stack is Python standard library only (http.server, sqlite3, urllib): app/server.py, app/db.py with SQL migrations in app/migrations/, app/ai.py, app/config.py, running on one small VPS behind a domain.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0178`
  ↳ *example-of* `r02-0180`

- `r02-0208` *STATED* — CaptionPal's mission states the test command and that there is no type check, lint or build step.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0178`
  ↳ *example-of* `r02-0181`

- `r02-0209` *STATED* — CaptionPal's mission says the launch changes everything (first launch), including the three migrations in app/migrations/.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0178`
  ↳ *example-of* `r02-0182`

- `r03-0153` *STATED* — linkedin-roast-skill's examples/jordan-sample/ shows a made-up profile and what the skill did with it.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0134`

- `r03-0269` *STATED* — Example headshot prompt: 'Create a clean, professional LinkedIn headshot of the person in the attached photo. Keep their real face, features, skin tone and hairstyle exactly as they are: it must look like them. Shoulders up, facing the camera with a relaxed, friendly expression. Plain neutral light-grey background, soft even light, no harsh shadows. Smart-casual clothes that suit a marketing job. Square crop with the face in the middle.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0256`

- `r03-0270` *STATED* — The example's 'Before you upload' notes: do not let a tool change your face (if it looks like someone else, do not use it); square image at least 400 x 400 (LinkedIn accepts up to 7680 x 4320), JPG or PNG, under 8 MB; read the image tool's privacy terms first.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0257`

- `r03-0272` *STATED* — Jordan Sample's before-headline: 'Passionate Team Player | Open to New Opportunities'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0224` — mood words

- `r03-0273` *STATED* — Rewritten headline (88 characters, limit 220): 'Marketing Coordinator | Social media, email and events | Outdoor gear | Mailchimp, Canva'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *contrast* `r03-0272`
  ↳ *example-of* `r03-0223`

- `r03-0274` *STATED* — Alternate headline 1 (115 characters): 'Marketing Coordinator at Bluebird Outdoor Gear | Social media, email newsletters and trade shows | Mailchimp, Canva'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0222`

- `r03-0275` *STATED* — Alternate headline 2 (129 characters), for once you have a real result: 'Marketing Coordinator | Social media and email marketing | [ADD YOUR BEST RESULT, for example email open rate or follower growth]'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0220`

- `r03-0276` *STATED* — Before-About example of self-praise: 'I am a passionate and hard-working marketing professional who loves working with people. [...] I am a team player with great communication skills and I am looking for a role where I can grow and make an impact. Open to new opportunities!'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *evidence-for* `r03-0299`

- `r03-0277` *STATED* — Rewritten About (655 characters, limit 2,600) in three short paragraphs: current role and duties plus an [ADD YOUR NUMBER] best result; prior internship and B.A. in Communications; the role sought and tools (Mailchimp, Canva).
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *contrast* `r03-0276`
  ↳ *example-of* `r03-0226`

- `r03-0279` *STATED* — Keyword-table row: 'marketing coordinator' went in the headline and About because it is the job title recruiters search for and matches the current title.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0229`

- `r03-0280` *STATED* — Keyword-table row: the profile said 'email newsletter', but 'Email marketing' is the term people search, so both were used.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0229`

- `r03-0281` *STATED* — Keyword-table row: Mailchimp and Canva went in the headline and About because tools are searched for by name and both were already in the skills.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0229`

- `r03-0282` *STATED* — Keyword-table rows: 'social media' and 'events, trade shows' were backed by the current job and internship; 'Instagram, Facebook' were platforms named in the internship; 'outdoor gear' is the current employer's industry.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0229`

- `r03-0284` *STATED* — Jordan's top skills (Microsoft Office, Teamwork, Communication) read as self-grading to two of the five roasters; the fix is to replace them with specific skills you can prove.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *evidence-for* `r03-0313`

- `r03-0285` *STATED* — Bullet rewrite: 'Responsible for the company's social media accounts' became 'Manage the company's social media accounts, posting [ADD YOUR NUMBER: posts per week] a week and growing followers from [ADD YOUR NUMBER] to [ADD YOUR NUMBER].'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`
  ↳ *qualifies* `r03-0307` — duty rewritten as result

- `r03-0286` *STATED* — Bullet rewrite: 'Helped with the monthly email newsletter' became 'Co-produce the monthly email newsletter ([ADD: your part]) for [ADD YOUR NUMBER: subscribers] subscribers, with an average open rate of [ADD YOUR NUMBER]%.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`

- `r03-0287` *STATED* — Bullet rewrite: 'Worked with the team on marketing campaigns' became 'Collaborate with the marketing team on [ADD YOUR NUMBER: how many] campaigns, owning [ADD: your part], which brought in [ADD YOUR NUMBER: leads, sales or reach].'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`

- `r03-0288` *STATED* — Bullet rewrite: 'Attended trade shows and helped at the booth' became 'Staff the company booth at [ADD YOUR NUMBER: how many] trade shows, [ADD: what you did there], collecting [ADD YOUR NUMBER] leads.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`

- `r03-0289` *STATED* — 'Assisted with various marketing tasks as needed' was Removed because 'It says nothing. If it covers real work, name the work and add a result.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0242`

- `r03-0290` *STATED* — Verb upgrades in the example rewrite: 'Responsible for' -> 'Manage', 'Helped with' -> 'Co-produce', 'Worked with the team' -> 'Collaborate', 'Attended' -> 'Staff', 'Assisted' -> 'Supported', 'Helped create' -> 'Co-created'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0234`
  ↳ *generalizes* `r03-0285`

- `r03-0291` *STATED* — Internship rewrite: 'Posted on Instagram and Facebook' became 'Posted to Summit Street Coffee's Instagram and Facebook accounts [ADD YOUR NUMBER: posts per week] a week, reaching [ADD YOUR NUMBER] followers.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`
  ↳ *example-of* `r03-0240`

- `r03-0292` *STATED* — Even a barista role gets rewritten: 'Served customers in a fast-paced environment' became 'Served about [ADD YOUR NUMBER: customers per shift] customers a shift in a fast-paced shop.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`
  ↳ *example-of* `r03-0232`

- `r03-0293` *STATED* — The example experience section is labelled 'Rewritten with the Harvard MCS bullet format: an action verb, what you did, a result', current role in present tense, finished roles in past tense, titles, employers and dates unchanged.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0158`

- `r03-0294` *STATED* — The example ends with 'Questions for you' ('Answer these and the skill updates this file'): six questions such as which platforms, posting frequency and follower counts, newsletter size and open rate, campaign roles, trade-show leads.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0261`

- `r03-0296` *STATED* — Example 'Assumed:' line: field is marketing (social media, email and events); level is early career; the job they seem to want is a marketing role built around social media and email.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0192`

- `r03-0298` *STATED* — Recruiter roast: the headline has no job title and no search keyword, so a search for 'Marketing Coordinator' or 'Social Media' will not surface the profile; 'Open to new opportunities' doesn't say which opportunity.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0197`
  ↳ *evidence-for* `r03-0223`

- `r03-0300` *STATED* — Recruiter's first 6 seconds: reads the headline, finds no title, scans the bullets for a number, finds none, doesn't message: 'Nothing separates this person from the other 99 profiles today', and 'Assisted'/'Helped' verbs suggest low ownership.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0197`
  ↳ *example-of* `r03-0211`
  ↳ *evidence-for* `r01-0134`
  ↳ *example-of* `g04-0158`

- `r03-0301` *STATED* — Recruiter's first fix: rewrite the headline as 'Marketing Coordinator | Social Media & Email | Outdoor Retail' to get into searches, then add one metric to each Bluebird bullet.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0197`
  ↳ *example-of* `r03-0213`

- `r03-0302` *STATED* — Hiring manager roast: 'Passionate' and 'team player' are claims anyone can make, and 'Open to New Opportunities' just says you want a job; no one searching 'email marketing' or 'social media coordinator' will find it.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0198`

- `r03-0303` *STATED* — Hiring manager's first 6 seconds: looks for one number or named result, finds none, closes the tab 'because I can't tell what you could do on day one'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0198`
  ↳ *evidence-for* `r03-0198`
  ↳ *evidence-for* `r01-0131`
  ↳ *example-of* `g04-0158`

- `r03-0304` *STATED* — Hiring manager on 'Assisted the marketing manager with day-to-day tasks': the same filler again, making the internship 'sound like errands'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0198`

- `r03-0305` *STATED* — Hiring manager's first fix: replace 'Responsible for the company's social media accounts' with proof: platforms, posting pace and one result, e.g. 'Run Bluebird's Instagram and Facebook, [X] posts a week; grew followers from [A] to [B] in [time].'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0198`

- `r03-0307` *STATED* — Founder roast: 'Being responsible is a duty, not a result.'
  > “Being responsible is a duty, not a result”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0199`

- `r03-0308` *STATED* — Founder roast: "'Where I can grow' is about what the writer wants, not what I get."
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0199`

- `r03-0309` *STATED* — Founder's first fix: rewrite the Bluebird bullets so each has a real number from Instagram and Mailchimp (followers gained, newsletter open rate, leads from the trade show booth), and only use numbers you can show.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0199`

- `r03-0310` *STATED* — Expert roast: 'Attending is not marketing'; the trade-show bullet names no show, lead count or follow-up, yet it is the entire evidence for the 'events' claim in the About.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0200`
  ↳ *example-of* `r03-0205`

- `r03-0311` *STATED* — Expert's first 6 seconds: no links, portfolio, Featured work or campaign names to make them stay, so 'I have no proof to forward to a hiring manager'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0200`
  ↳ *example-of* `g04-0158`

- `r03-0312` *STATED* — Expert's first fix: rewrite the headline as role, channel and one real number pulled from the Mailchimp or social analytics; finding that number shows you how to fix every bullet.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0200`

- `r03-0313` *STATED* — Peer's first 6 seconds: can't tell the specialty, finds no number or campaign name, no link to work samples, and 'Microsoft Office' and 'Teamwork' in Top Skills make them roll their eyes; the one thing they'd copy is naming Mailchimp and Canva, because tools are concrete.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0201`
  ↳ *example-of* `g04-0158`

- `r03-0314` *STATED* — Peer roast: "'Open to new opportunities' is a banner, not a headline."
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0201`

- `r03-0315` *STATED* — Peer's first fix: rewrite the headline as the real job, e.g. 'Marketing Coordinator | Social, Email and Events | Outdoor Retail': quick, searchable, and it tells readers what to look for.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0201`

- `r03-0319` *STATED* — Recruiter bullet roast: 'Helped with the monthly email newsletter' gives no open rate, list size, or what 'helped' meant, and Mailchimp is in the skills list but nothing shows what was done with it.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0210`
  ↳ *evidence-for* `r03-0321`

- `r03-0321` *STATED* — Hiring manager: the skills list names Mailchimp and Canva, but nothing shows work made with them, so listing a tool is not evidence of using it well.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0198`

- `r03-0322` *STATED* — Founder headline roast: 'The word "marketing" is missing from a marketer's headline'; 'Passionate' and 'team player' cost nothing to claim.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0199`
  ↳ *evidence-for* `r03-0223`

- `r03-0324` *STATED* — Founder's first 6 seconds: reads the headline and current bullets looking for one number, finds none, sees more self-grading in the skills ('Teamwork', 'Communication'), and closes the tab: 'Nothing here shows I would get results for my money.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0199`
  ↳ *evidence-for* `r03-0284`
  ↳ *example-of* `g04-0158`

- `r03-0325` *STATED* — Expert headline roast: 'Passionate Team Player' is 'a free adjective every applicant claims', and 'Open to New Opportunities' tells the reader 'you will take anything'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0200`
  ↳ *evidence-for* `r03-0224`

- `r03-0327` *STATED* — Expert bullet roast: 'Helped with the monthly email newsletter': 'Helped how, for how many subscribers, and with what open or click rate?'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *leads-to* `r03-0286` — the questions become the rewrite's placeholders
  ↳ *example-of* `r03-0210`

- `r03-0329` *STATED* — Peer verdict: 'I would not trust it yet, because I can't tell if this person is good or just present.'
  > “I can't tell if this person is good or just present.”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0201`

- `r03-0330` *STATED* — Peer bullet roast: 'Responsible for the company's social media accounts' gives no platform, posting pace or growth number, 'so it is a duty and not a result'; 'showing up is not marketing'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0201`
  ↳ *evidence-for* `r03-0307`

- `r03-0332` *STATED* — The example keyword note: recruiters search by words like these and LinkedIn Recruiter's search highlights matches in Summary, Experience and Skills; LinkedIn does not publish how it ranks profiles, so the rewrite 'cannot promise a rank, interviews or connection requests'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0231`
  ↳ *part-of* `r03-0229`

- `r03-0333` *STATED* — Internship rewrites: 'Assisted the marketing manager with day-to-day tasks' became 'Supported the marketing manager with [ADD: the real tasks, for example scheduling posts, writing copy or updating the website]'; 'Helped create flyers for events' became 'Co-created flyers for [ADD YOUR NUMBER: how many] events, [ADD: a result, for example attendance]'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0293`
  ↳ *qualifies* `r03-0304` — fix for the 'errands' internship

- `r03-0334` *STATED* — Barista rewrite: 'Handled cash and card payments' became 'Handled cash and card payments, with [ADD: a result if you have one, for example a balanced till or no errors]'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0292`

- `r04-0118` *STATED* — Groomly (example app): an online booking app for independent dog groomers, so their clients can book and pay a deposit without texting back and forth.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0167`

- `r04-0124` *STATED* — Groomly 'Who pays': independent dog groomers and small grooming salons (1 to 5 groomers).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0169`

- `r04-0125` *STATED* — Groomly 'Where they talk online': r/doggrooming, r/smallbusiness, and grooming forums (public pages only).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0169`

- `r04-0126` *STATED* — Groomly 'Marketing to draft': a week of Instagram posts (7, one a day) for groomers; a 30-second launch video script with a shot list.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0170`

- `r04-0234` *STATED* — /shark product-idea template: /shark [product] for [customer], priced at [price]. It costs me [cost] to make. [how many] people have bought it so far.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0233`

- `r04-0235` *STATED* — /shark side-hustle template: /shark I want to turn [side hustle] into a business. I make [income] a month from it today, working [hours] a week.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0233`

- `r04-0236` *STATED* — /shark app/SaaS template: /shark [app] helps [customer] do [job]. [users] people use it, [paying] pay [price] a month. I need [amount] for [use].
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0233`

- `r04-0237` *STATED* — /shark service/agency template: /shark I want to sell [service] to [customer] for [price]. I have [clients] clients so far.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0233`

- `r04-0238` *STATED* — /shark creator-business template: /shark I have [followers] followers on [platform] and I want to sell [product] to them for [price].
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0233`

- `r04-0239` *STATED* — /shark before a real investor meeting: /shark [paste your actual pitch deck text or one-pager].
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0233`

- `r04-0268` *STATED* — Hot-sauce example pitch: a subscription box of hot sauces from small local makers, $35 a month.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0226`
  ↳ *example-of* `r04-0250`
  ↳ *example-of* `r04-0221`

- `r04-0270` *STATED* — Hot-sauce example traction: 12 paying subscribers so far, all from posting on Instagram.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0226`

- `r04-0272` *STATED* — Hot-sauce example goal and ask: reach 500 subscribers in a year, asking for $50,000 to buy stock in bulk and run ads.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0226`

- `r04-0274` *STATED* — Operator Shark's biggest worry: 'You're asking for money to go from 12 to 500 subscribers, but nothing shows who packs, whether small makers can supply that many boxes, or whether anyone stays.'
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0273`
  ↳ *depends-on* `r04-0272`

- `r04-0275` *STATED* — Operator Shark question 1: who packs and ships today, is their time in the $19, and what does 500 boxes a month do to that cost?
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0274`

- `r04-0276` *STATED* — Operator Shark question 2: which small makers will commit to 500 boxes' worth a month at today's prices, and how much of the $50,000 goes on bulk stock that sits if growth stalls?
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0274`

- `r04-0277` *STATED* — Operator Shark question 3: with about $16 left per box, what can an ad-won subscriber cost before ads lose money, and how many of your 12 have stayed?
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0274`

- `r04-0278` *STATED* — Customer Shark's biggest worry: 'A bottle of hot sauce lasts me weeks, so I would cancel once my shelf is full, and your pitch never says how long any of your 12 have stayed.'
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0273`
  ↳ *depends-on* `r04-0270`

- `r04-0279` *STATED* — Customer Shark question 1: how many months has your longest-paying subscriber stayed, and how many of the 12 have already cancelled?
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0278`

- `r04-0280` *STATED* — Customer Shark question 2: why wouldn't I buy straight from the makers, and what did your 12 stop buying to make room for $35 a month?
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0278`

- `r04-0281` *STATED* — Customer Shark question 3: your 12 came from posting on Instagram; what do they say made them subscribe, and would a cold stranger from an ad say the same?
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0278`

- `r04-0284` *STATED* — Founder homework: find out who packs and ships today, whether anyone's time is inside the $19, what the $19 splits into (sauce, packaging, postage), and what each part costs at 500 boxes a month.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0275`
  ↳ *example-of* `r04-0282`

- `r04-0285` *STATED* — Founder homework: find out which makers will supply 500 boxes' worth a month and at what price per bottle; the pitch names no maker.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0276`

- `r04-0286` *STATED* — Founder homework: the pitch gives no split of the $50,000 beyond 'to buy stock in bulk and run ads'; find out the dollar split between stock and ads, and what happens to unsold stock if growth stalls.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0276`

- `r04-0288` *STATED* — Founder homework: find out how many of the 12 still pay, how many months each has stayed, and what one ad-won subscriber costs; all 12 came from Instagram posting, so the pitch shows no ad-won subscriber.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0277`
  ↳ *qualifies* `r04-0287`

- `r04-0289` *STATED* — Founder homework: '12 paying subscribers so far' doesn't say whether that means 12 now or 12 ever; find out each one's sign-up date, how many people have ever subscribed, and how many cancelled.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0279`
  ↳ *qualifies* `r04-0270`

- `r04-0290` *STATED* — Founder homework: the pitch gives no reason to choose the box over buying direct; find out what each maker charges for the same bottles direct and what the box offers that going direct does not.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0280`

- `r04-0291` *STATED* — Founder homework: ask each of the 12 subscribers what they spent less on to afford $35 a month.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0280`

- `r04-0292` *STATED* — Founder homework: find out why each of the 12 says they subscribed and whether they knew the founder before buying; with no ad results, nothing shows whether a stranger reached by an ad would subscribe or stay.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0281`

- `r04-0294` *STATED* — Operator Shark: OUT, no offer: 'I won't put $50,000 into bulk stock and ads for a business I can't see inside', since the answers gave nothing on who packs, maker supply for 500 boxes, or retention.
  > “I won't put $50,000 into bulk stock and ads for a business I can't see inside.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0293`
  ↳ *because* `r04-0274`
  ↳ *evidence-for* `r04-0226`

- `r04-0295` *STATED* — What would change the Operator Shark's mind: a one-page costing of a 500-box month with a written quote behind every line (bottles from named makers who agree to that volume, packaging, postage, the packer's time), ending in a cost per box to hold against the $19.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0294`
  ↳ *depends-on* `r04-0284`

- `r04-0296` *STATED* — Customer Shark: OUT, no offer: a bottle lasts weeks so it would cancel once its shelf is full, and the founder could not say how long any of the 12 stayed or how many quit, so nothing shows anyone keeps paying $35 a month.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0293`
  ↳ *because* `r04-0278`
  ↳ *evidence-for* `r04-0226`

- `r04-0297` *STATED* — What would change the Customer Shark's mind: a dated list of everyone who has ever subscribed, including anyone who cancelled, showing most of them still paying after their third box.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0296`
  ↳ *depends-on* `r04-0289`

- `y01-0091` *STATED* — Agency demo scenario: a med spa hires you as a client - normally you'd need someone writing the content, planning the ads and planning the social posts.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *example-of* `y01-0101`

- `y02-0003` *STATED* — Example of the Harvey agent: if you build websites, it finds local businesses near you, reads every one of their websites, and picks the ones that need you most.
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *evidence-for* `g04-0032`
  ↳ *part-of* `y02-0001`
  ↳ *example-of* `y02-0002`

- `y03-0146` *STATED* — SupoClip clip question 1: does the opening hook you?
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `y03-0145`

- `y03-0147` *STATED* — SupoClip clip question 2: will people keep watching?
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `y03-0145`

- `y03-0148` *STATED* — SupoClip clip question 3: is it actually useful?
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `y03-0145`

- `y03-0149` *STATED* — SupoClip clip question 4: would somebody send it to a friend?
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `y03-0145`

- `y03-0159` *STATED* — Launching a new brand in Runnable, you can generate the product shots and a video for the ad.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *example-of* `y03-0157`

- `y04-0033` *STATED* — Brand-launch example in Runnable: when launching a new product brand (transcribed 'head foot brand'), generate the product shots and a video for the ad.
  > “You can generate the product shots and a video for the ad.”
  — [TKrtaLRIHBg](https://youtu.be/TKrtaLRIHBg)
  ↳ *evidence-for* `y03-0159`
  ↳ *example-of* `y04-0031`
  ↳ *leads-to* `y04-0035`

- `y04-0063` *STATED* — Jev use case 2 (sorting incoming work): when 100 lead emails come in, Jev labels each one a warm lead, a cold lead, or not even a lead at all.
  > “Imagine 100 lead emails come in. Jev labels them as warm leads, cold leads, or not even leads at all.”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *evidence-for* `g13-0187`
  ↳ *example-of* `y04-0060`

- `y04-0087` *STATED* — Free-API build example: a food app with real nutrition data.
  > “a food app with real nutrition data”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *example-of* `g13-0152`
  ↳ *example-of* `y04-0086`

- `y04-0088` *STATED* — Free-API build example: a crypto platform with real prices.
  > “a crypto platform with real prices”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *example-of* `g13-0152`
  ↳ *example-of* `y04-0086`

- `y04-0089` *STATED* — Free-API build example: a news site with real headlines.
  > “a news site with real headlines”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *example-of* `g13-0152`
  ↳ *example-of* `y04-0086`

### idea

- `g05-0055` *INFERRED* — A one-sentence promo video lets a builder give a product or GitHub repo a 4K launch trailer without editing skills.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)

- `g07-0102` *STATED* — Alex lists three cheap things to build with Haiku 5.5 this week ('Three cheap things to build this week'; email-gated).
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`

- `g08-0262` *INFERRED* — Two guides in this batch share one thesis: paid software you subscribe to can now be cloned with Claude (the Craft apps for Adobe, Replica for any app).
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft) [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *evidence-for* `y02-0188`

- `g12-0152` *INFERRED* — Because the free SEO skill does what agencies charge hundreds to thousands for and works on a client's site, it can underpin a low-cost SEO-audit service.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *depends-on* `g12-0130`
  ↳ *depends-on* `g12-0131`
  ↳ *evidence-for* `y01-0119`

- `g12-0166` *STATED* — Guide section '5 plugins you could build this weekend' lists five weekend-sized plugin ideas (body email-gated; 5 prompts to copy).
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`
  ↳ *part-of* `g12-0157`
  ↳ *depends-on* `g12-0165`

- `g13-0056` *STATED* — Alex's Higgsfield guide pairs the API setup with a distribution strategy: a plan for turning the generated video output into distribution so what you make gets seen.
  — [g-higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy](https://chen.media/guides/higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy)
  ↳ *depends-on* `g13-0044`

- `g14-0330` *STATED* — Three AI services you can sell: a CRM agent, a short-form editing package and a phone agent.
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0329`

- `g14-0340` *STATED* — Service method one: an AI sales assistant (CRM agent) for one industry.
  > “Method one, an AI sales assistant for one industry”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0330`
  ↳ *example-of* `g14-0334`

- `g14-0341` *STATED* — Service method two: short-form video editing sold as a monthly package.
  > “Method two, short-form editing as a monthly package”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0330`
  ↳ *example-of* `g14-0334`
  ↳ *enables* `g14-0044` — OpenCut as editing tool

- `g14-0342` *STATED* — Service method three: an AI agent that can use a phone.
  > “Method three, an agent that can use a phone”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0330`
  ↳ *example-of* `g14-0334`

- `g16-0140` *STATED* — A million token window changes what is worth building; his guide lists what to actually build with it.
  > “What to actually build with a million token window”
  — [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)
  ↳ *depends-on* `g16-0130`

- `g17-0190` *STATED* — Alex Chen picks the three business-tool swaps to make if you only do three.
  > “If you only do three”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0167`

- `g22-0096` *STATED* — Bookkeeping guide section 'Do more with the same folder' reuses the transaction folder for further analyses.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`

- `r01-0290` *INFERRED* — The candle trial's core lesson generalises: before a risky bet, pre-commit a stop date and stop level, and keep a way back.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *generalizes* `r01-0273`
  ↳ *generalizes* `r01-0263`
  ↳ *evidence-for* `g08-0188`

- `r02-0292` *STATED* — SPEED watch: asking for the 3 captions in one AI request, or making the 3 calls at once, would cut the wait to about a third.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0241`

- `y01-0119` *STATED* — AI visibility (GEO audit plus fixes) becomes an entire separate service you can offer through the agency.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *depends-on* `y01-0113`
  ↳ *example-of* `y01-0120`

### method

- `g01-0006` *STATED* — Step 1 of /hiring-panel: type /hiring-panel plus your resume (a file or pasted text), plus the job posting if you have one.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0001`
  ↳ *leads-to* `g01-0007`
  ↳ *evidence-for* `r01-0149`

- `g01-0008` *STATED* — The /hiring-panel automated-screen Claude checks that the resume text can be read in order, that titles and dates are clear, and, if given a job posting, which of the job's key skills are missing.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0007`
  ↳ *contrast* `g01-0053` — ATS-readability check vs ATS-readable CV generation
  ↳ *evidence-for* `r01-0120`

- `g01-0009` *STATED* — The /hiring-panel automated-screen Claude answers PASS or REJECT, with the resume lines that decided it.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0007`

- `g01-0035` *STATED* — Instead of rewriting a pasted resume, Claude Resume Kit draws on a knowledge base you build once from your own papers, reports and projects.
  — [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything)
  ↳ *part-of* `g01-0034`
  ↳ *enables* `g01-0036`

- `g01-0045` *CORE* — With career-ops you paste a job and Claude checks it is still open, scores it against your real CV out of 5, tells you to skip a weak fit, and drafts the CV and answers for the ones worth it.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *defines* `g01-0044`

- `g01-0050` *CORE* — career-ops 'Still open?' step: it checks the posting is live before you write a word.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0045`
  ↳ *leads-to* `g01-0051`

- `g01-0051` *CORE* — career-ops 'Not you?' step: it scores the role against your real CV and tells you to skip a weak fit.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0045`
  ↳ *leads-to* `g01-0053`
  ↳ *contrast* `g01-0005` — score fit before applying vs learn rejection reasons before applying
  ↳ *example-of* `g01-0193`

- `g01-0053` *CORE* — career-ops 'Worth it?' step: it tailors an ATS-readable CV PDF and drafts a cover letter and the answer to every application field.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0045`
  ↳ *leads-to* `g01-0054`
  ↳ *evidence-for* `r02-0083`

- `g01-0054` *CORE* — career-ops 'Who to talk to?' step: it finds the hiring manager or recruiter and drafts a short LinkedIn note.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0045`

- `g01-0056` *CORE* — career-ops scan mode checks 100+ pre-configured company job boards (Anthropic, OpenAI, ElevenLabs, Retool, n8n and more) for new roles.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *part-of* `g01-0045`

- `g01-0063` *STATED* — Use career-ops to score one job post against your CV before you apply.
  — [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s)
  ↳ *example-of* `g01-0051`
  ↳ *part-of* `g01-0044`

- `g01-0067` *STATED* — With khan-explainer you describe the video, Claude writes a scene file, and one command renders an MP4 where a pen draws on a blackboard or whiteboard while a voice explains it.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *defines* `g01-0066`

- `g01-0154` *STATED* — ReelMimic accepts a reference as a file, a phone recording or a YouTube link.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g01-0153`
  ↳ *leads-to* `g01-0155`

- `g01-0155` *STATED* — ReelMimic breaks the reference down into shot count, shot lengths, BPM, transitions, colours, framing and camera moves.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *leads-to* `g01-0156`

- `g02-0083` *STATED* — GoLive first detects what your app needs, then writes a plan of the exact changes.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *leads-to* `g02-0084`
  ↳ *part-of* `g02-0080`

- `g02-0085` *STATED* — GoLive applies the approved plan with your own logins and verifies what actually works.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *leads-to* `g02-0086`
  ↳ *example-of* `g02-0239`

- `g02-0086` *STATED* — GoLive records what it created.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)

- `g02-0087` *STATED* — GoLive re-checks what it created for drift on demand.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *depends-on* `g02-0086`

- `g02-0088` *STATED* — GoLive can tear down what it created again.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *depends-on* `g02-0086`

- `g02-0099` *STATED* — With career-ops you paste a job and Claude checks it is still open, scores it against your real CV out of 5, tells you to skip a weak fit, and drafts the CV and answers for the ones worth it.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *defines* `g02-0098`
  ↳ *evidence-for* `g01-0045`

- `g02-0104` *STATED* — career-ops checks that a posting is still live before you write a word.
  > “It checks the posting is live before you write a word.”
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0099`
  ↳ *evidence-for* `g01-0050`

- `g02-0105` *STATED* — career-ops scores the role against your real CV and tells you to skip a weak fit.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0099`
  ↳ *evidence-for* `g02-0096`
  ↳ *evidence-for* `g01-0051`

- `g02-0107` *STATED* — For roles worth applying to, career-ops tailors an ATS-readable CV PDF.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0099`
  ↳ *evidence-for* `g01-0053`

- `g02-0108` *STATED* — career-ops drafts a cover letter and the answer to every application field.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0099`
  ↳ *evidence-for* `g01-0053`

- `g02-0109` *STATED* — career-ops finds the hiring manager or recruiter and drafts a short LinkedIn note.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0098`
  ↳ *evidence-for* `g01-0054`

- `g02-0111` *STATED* — career-ops scan mode checks 100+ pre-configured company job boards (Anthropic, OpenAI, ElevenLabs, Retool, n8n and more) for new roles.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0098`
  ↳ *evidence-for* `g01-0056`

- `g02-0152` *STATED* — With claude-seo you type /seo audit and your web address to start a site audit.
  > “You type /seo audit and your web address”
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *enables* `g02-0151`

- `g02-0155` *STATED* — claude-seo audits content quality, technical SEO, schema, local SEO, backlinks and more.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *part-of* `g02-0153`

- `g02-0156` *STATED* — claude-seo checks AI search readiness: whether ChatGPT-style answers and Google's AI results can find and cite you (GEO/AEO, llms.txt).
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *part-of* `g02-0153`
  ↳ *example-of* `y01-0112`

- `g02-0157` *STATED* — claude-seo writes a prioritized action plan as Markdown, with a PDF option, so you know what to fix first.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *part-of* `g02-0151`

- `g02-0208` *STATED* — With Video Use you point Claude at a folder of raw takes, agree on a plan, and get final.mp4 back with fillers cut, colour graded, captions burned in and every cut checked.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *defines* `g02-0207`
  ↳ *example-of* `g02-0237`

- `g02-0210` *STATED* — You drop raw footage in a folder, ask for the edit in plain words, and Video Use produces edit/final.mp4 next to your files.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0208`

- `g02-0211` *STATED* — Video Use cuts out filler words (um, uh, false starts) and the dead space between takes.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`

- `g02-0212` *STATED* — Video Use colour grades every segment: warm cinematic, neutral punch, or any custom ffmpeg look.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`

- `g02-0214` *STATED* — Video Use burns in subtitles in your style, two-word UPPERCASE chunks by default.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`

- `g03-0060` *STATED* — career-ops flow: paste a job, Claude checks it is still open, scores it against your real CV out of 5, tells you to skip a weak fit, and drafts the CV and answers for the ones worth it.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *defines* `g03-0059`
  ↳ *evidence-for* `g01-0045`

- `g03-0072` *STATED* — The career-ops guide's locked sections are "Set it up", "The catch" and "Sources" (1 prompt to copy, 5 numbered steps).
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *example-of* `g03-0005`
  ↳ *part-of* `g03-0059`

- `g04-0030` *STATED* — To use Harvey you tell it what you sell and who your ideal customer is.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0031`

- `g04-0033` *STATED* — Harvey writes each prospect a cold email that mentions the specific real thing it found about them.
  > “writes each a cold email about something real it found”
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0034`

- `g04-0047` *STATED* — Start Harvey's dashboard with: harvey dashboard (it opens at http://localhost:5555).
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0048`
  ↳ *enables* `g04-0036`

- `g04-0048` *STATED* — Start the Harvey agent itself with: harvey run
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *depends-on* `g04-0037`
  ↳ *depends-on* `g04-0039`
  ↳ *depends-on* `g04-0040`

- `g04-0051` *STATED* — Alex's Harvey guide also covers doing the same outreach process by hand, without the agent (section 'Doing it by hand', body locked).
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *contrast* `g04-0035`
  ↳ *example-of* `g02-0234`

- `g04-0052` *STATED* — Alex's Harvey guide breaks down what Harvey does in each loop cycle and what its dashboard shows (sections 'What it does each cycle' and 'The dashboard', bodies locked).
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *qualifies* `g04-0035`
  ↳ *example-of* `g02-0234`

- `g04-0103` *STATED* — Run the skill by typing /hiring-panel with your resume (a file or pasted text), plus the job posting if you have one.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0099`
  ↳ *evidence-for* `r01-0149`

- `g04-0105` *STATED* — The /hiring-panel automated-screen Claude checks that the resume text can be read in order and that titles and dates are clear.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0104`
  ↳ *evidence-for* `r01-0120`

- `g04-0106` *STATED* — Given a job posting, the /hiring-panel automated-screen Claude reports which of the job's key skills are missing from your resume.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0104`
  ↳ *evidence-for* `r01-0125`

- `g04-0107` *STATED* — The /hiring-panel automated-screen Claude answers PASS or REJECT, with the lines that decided it.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0104`
  ↳ *example-of* `g04-0246`
  ↳ *evidence-for* `g01-0009`

- `g04-0113` *STATED* — /hiring-panel then rebuilds your resume with every mistake fixed.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *leads-to* `g04-0114`
  ↳ *example-of* `g04-0249`
  ↳ *evidence-for* `r01-0137`

- `g04-0152` *STATED* — To run /linkedin-roast, save your LinkedIn profile as a PDF, then type /linkedin-roast and the file name.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *leads-to* `g04-0153`
  ↳ *evidence-for* `r03-0144`

- `g04-0156` *STATED* — Each /linkedin-roast persona roasts your headline and your About section.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0153`

- `g04-0157` *STATED* — Each /linkedin-roast persona picks your three weakest bullets.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0153`

- `g04-0158` *STATED* — Each /linkedin-roast persona says what it would do in the first six seconds of seeing your profile.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0153`

- `g04-0159` *STATED* — Each /linkedin-roast persona gives a score out of 10 and names the one fix it would make first.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0153`

- `g04-0162` *STATED* — /linkedin-roast then fixes the profile, starting with a new headline.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *example-of* `g04-0249`
  ↳ *evidence-for* `r03-0222`

- `g04-0163` *STATED* — /linkedin-roast writes an About section that uses the words people search for.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0162`
  ↳ *evidence-for* `r03-0227`

- `g04-0164` *STATED* — /linkedin-roast rewrites every experience entry in the style Harvard's career center teaches for resumes.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0162`
  ↳ *evidence-for* `r03-0158`

- `g04-0167` *STATED* — /linkedin-roast makes a banner file at LinkedIn's banner size.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0149`
  ↳ *evidence-for* `r03-0150`

- `g04-0168` *STATED* — /linkedin-roast writes a headshot prompt for you to paste into your own image tool.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0149`
  ↳ *evidence-for* `r03-0151`

- `g05-0246` *STATED* — The Founder skills are meant to run in a set order ('Run it in this order'; 9 numbered steps).
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`
  ↳ *because* `g05-0241` — each skill reads the previous one's output

- `g06-0184` *STATED* — Using the Anthropic startup program takes two steps: apply, then redeem the partner codes (details in the gated part of the guide).
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0170`

- `g07-0058` *STATED* — The outbound agent writes a short, personal first email to each business in your voice.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — outbound agent
  ↳ *leads-to* `g07-0059`
  ↳ *evidence-for* `r01-0043`

- `g07-0060` *STATED* — The agency skill's sales agent preps every call: who they are, the questions to ask, the objections and your answers, and the price.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — sales agent
  ↳ *leads-to* `g07-0061`
  ↳ *evidence-for* `r01-0091`

- `g07-0062` *STATED* — The agency skill's workflow agent turns your call notes into a proposal.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — workflow agent
  ↳ *leads-to* `g07-0063` — after your approval
  ↳ *evidence-for* `r01-0097`

- `g07-0218` *STATED* — Step 3: build something with the API credits; Alex's guide includes 1 prompt for it (email-gated).
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`

- `g07-0250` *STATED* — To run /linkedin-roast, save your LinkedIn profile as a PDF, then type /linkedin-roast and the file name.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *leads-to* `g07-0252`
  ↳ *evidence-for* `r03-0144`

- `g07-0255` *STATED* — Each /linkedin-roast reviewer says what it would do in the first six seconds of seeing your profile.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0254`
  ↳ *evidence-for* `g04-0158`

- `g07-0259` *STATED* — /linkedin-roast's fix step writes you a new LinkedIn headline.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0248`
  ↳ *evidence-for* `r03-0222`

- `g07-0260` *STATED* — /linkedin-roast writes an About section that uses the words people search for.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0248`
  ↳ *evidence-for* `r03-0227`

- `g07-0261` *STATED* — /linkedin-roast rewrites every experience entry in the style Harvard's career center teaches for resumes.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0248`
  ↳ *evidence-for* `r03-0158`

- `g07-0277` *STATED* — Describe the Syren video in your own words; you can also add docs, images, videos, PowerPoints or YouTube links, or start from a preset use case.
  — [g-syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent](https://chen.media/guides/syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent)
  ↳ *part-of* `g07-0270`
  ↳ *leads-to* `g07-0278`

- `g07-0279` *STATED* — Refine a Syren video in the chat: change the script, swap the avatar or the voice, or restyle one scene.
  — [g-syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent](https://chen.media/guides/syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent)
  ↳ *part-of* `g07-0270`
  ↳ *leads-to* `g07-0280`

- `g07-0280` *STATED* — In Syren, choose landscape for websites and slides or portrait for phones and social.
  — [g-syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent](https://chen.media/guides/syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent)
  ↳ *part-of* `g07-0270`

- `g07-0284` *STATED* — Syren's Brand Kit teaches it your style ('Brand Kit: teaching it your style'; email-gated).
  — [g-syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent](https://chen.media/guides/syren-make-a-whole-video-from-one-prompt-synthesia-ai-video-agent)
  ↳ *part-of* `g07-0270`

- `g08-0038` *STATED* — The /hiring-panel automated screen checks that the resume text can be read in order, that titles and dates are clear and, if you gave a job posting, which of the job's key skills are missing.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0037`
  ↳ *evidence-for* `r01-0120`

- `g08-0161` *STATED* — Alex's suggested first run: try Replica on one app tonight (section 'Try it on one app tonight').
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`

- `g08-0167` *STATED* — Replica's entrepreneur skill reads real reviews on the App Store, G2, Capterra and Reddit and turns what users hate into a fix plan for your version.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`
  ↳ *evidence-for* `g08-0157` — reviews are how the clone skips what users hate
  ↳ *evidence-for* `g19-0240`

- `g08-0188` *STATED* — /jester step 4: the cheapest test you can run this week, with what result means keep going and what result means stop.
  — [g-give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes](https://chen.media/guides/give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes)
  ↳ *part-of* `g08-0177`

- `g08-0233` *STATED* — /rival step 4: you get the weakness the winning plan goes after, and three things to do this week to fix it before a real competitor finds it.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0220`

- `g09-0202` *STATED* — Give MiroFish your product page saved as a PDF or text, and it builds a crowd from the people and groups in your material, each with a profile of its own.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *example-of* `g09-0198`

- `g09-0203` *STATED* — Give MiroFish your price and your ad, and you get two simulated social feeds where the crowd talks about it: posts, replies, likes, reposts.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *example-of* `g09-0199`

- `g09-0204` *STATED* — Ask MiroFish one question in plain words (will people love it or ignore it?) and it returns a written report: who's in, who's out, and the reasons that keep coming up.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *example-of* `g09-0200`

- `g09-0205` *STATED* — MiroFish follow-up questions open a chat with any single simulated customer: why didn't you buy?
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *qualifies* `g09-0200`

- `g09-0206` *STATED* — Change one thing (the headline, the price, the ad) and run MiroFish again to see which version the crowd takes better before a real customer sees either.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *depends-on* `g09-0200`

- `g09-0208` *STATED* — After reading the MiroFish report, interview the simulated customers who swam away ('Step 5: read the report, then ask the ones who swam away').
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *depends-on* `g09-0205`

- `g09-0219` *STATED* — Night-crew scout: looks for people who need what you make, finding real posts and threads where they ask for it, with links, and drafting replies.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0216`
  ↳ *evidence-for* `r04-0091`

- `g09-0220` *STATED* — The night-crew scout also writes the marketing you asked for, like a week of social posts or a launch video script.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0219`
  ↳ *evidence-for* `r04-0091`

- `g09-0254` *CORE* — Alex's recurring advice: rehearse a decision or launch against simulated critics or customers (board, sharks, jury, flight controllers, MiroFish crowd) before spending real money or time.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives) [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill) [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill) [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers) [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *because* `g09-0245`

- `g10-0002` *STATED* — Alex Chen's Reddit research method: use Reddit's Ask AI search to find what your niche audience actually struggles with, then paste those pain points into Claude to turn them into video ideas and digital products.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)

- `g10-0004` *STATED* — Step 1 of the Reddit pain-point research method: open Reddit's Ask (the AI search button).
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0002`
  ↳ *leads-to* `g10-0005`

- `g10-0005` *STATED* — Step 2 of the Reddit pain-point research method: ask Reddit's AI for the pain points of your niche (the guide's question prompts are locked).
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0002`
  ↳ *leads-to* `g10-0006`
  ↳ *example-of* `g02-0234`

- `g10-0006` *STATED* — Step 3 of the Reddit pain-point research method: open the sources (the threads and comments) that Reddit's Ask answer links to.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0002`
  ↳ *leads-to* `g10-0007`

- `g10-0007` *STATED* — Step 4 of the Reddit pain-point research method: paste the pain points and sources into Claude (with the guide's locked Claude prompt).
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0002`

- `g10-0016` *STATED* — Paste the Reddit pain-point list into Claude and it becomes video ideas and digital products that solve those exact problems.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *defines* `g10-0007`
  ↳ *depends-on* `g10-0015`

- `g10-0230` *STATED* — Dyad step 5: put the app on the internet.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`

- `g12-0068` *STATED* — Guide section 'Step 2: take your app live' runs the go-live skill on your app (body email-gated).
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0050`

- `g12-0148` *STATED* — Guide section 'Run your first audit' runs the SEO skill on a site (body email-gated; 3 prompts to copy).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *example-of* `g02-0234`

- `g12-0150` *STATED* — Guide section 'Read the action plan' covers reading the SEO skill's ranked fix list (body email-gated).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *depends-on* `g12-0134`

- `g12-0169` *STATED* — Guide section 'Get it into the store' covers submitting a plugin to Claude Marketplace (body email-gated).
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`

- `g12-0190` *STATED* — SupoClip takes a long video (a podcast, a talk, a stream) as a YouTube link or an upload, finds the most clip-worthy moments and scores them.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0185`

- `g12-0195` *STATED* — Guide section 'What it does to every clip' covers SupoClip's per-clip processing (body email-gated).
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0184`
  ↳ *qualifies* `g12-0191`

- `g13-0059` *STATED* — Alex's Higgsfield guide has a 'Set it up' section with 1 copyable prompt for getting the Higgsfield API running.
  — [g-higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy](https://chen.media/guides/higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy)
  ↳ *part-of* `g13-0043`

- `g13-0064` *STATED* — Before scraping, start with a defined output: a table of businesses, an inventory of product information, or a set of page summaries.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063` — first decide the output

- `g13-0075` *STATED* — Alex's Scrapling guide has a step 'Turn business pages into a reviewable lead sheet'.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`
  ↳ *depends-on* `g13-0066`

- `g13-0076` *STATED* — Alex's Scrapling guide has a step 'Turn a website into useful research notes'.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0163` *STATED* — Alex's PUB guide step: 'Start with one useful feature' before wiring many APIs.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *leads-to* `g13-0164`
  ↳ *part-of* `g13-0152`

- `g13-0165` *STATED* — Alex's PUB guide step: 'Try a small weather request' as the first verified API call.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *leads-to* `g13-0166`
  ↳ *part-of* `g13-0155`

- `g13-0166` *STATED* — Alex's PUB guide step: 'Reuse the workflow with an API key' for providers that need authentication.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *leads-to* `g13-0167`

- `g13-0167` *STATED* — Alex's PUB guide step: 'Test the failure paths before sharing' an API-backed prototype.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *leads-to* `g13-0168`
  ↳ *evidence-for* `r02-0129`

- `g13-0168` *STATED* — Alex's PUB guide step: 'Turn the prototype into a useful product'.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)

- `g13-0187` *STATED* — Workflow 2 from Alex's JEV video: triage incoming leads with Jev.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0184`
  ↳ *depends-on* `g13-0075` — scraped lead sheet feeds Jev lead triage

- `g13-0190` *STATED* — Use HackingTool to choose a small review of an app you own, collect evidence, and turn a finding into a code change.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *part-of* `g13-0189`

- `g13-0202` *STATED* — HackingTool guide step 4: define the test before selecting tools.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *leads-to* `g13-0203`
  ↳ *evidence-for* `g13-0064`

- `g13-0203` *STATED* — HackingTool guide step 5: turn one finding into a verified repair.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *part-of* `g13-0190`
  ↳ *contrast* `g13-0279` — verified repair vs inspected build
  ↳ *evidence-for* `r02-0200`

- `g13-0206` *STATED* — When adapting the Runable guide, replace the invented Onda identity with your own product and verified facts.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *qualifies* `g13-0205`

- `g13-0216` *STATED* — Runable guide step 1: lock the brand brief before generating assets.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *leads-to* `g13-0217`
  ↳ *part-of* `g13-0204`
  ↳ *evidence-for* `g14-0011`

- `g13-0217` *STATED* — Runable guide step 2: approve one product image, then reuse it.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *leads-to* `g13-0218`
  ↳ *part-of* `g13-0221`

- `g13-0218` *STATED* — Runable guide step 3: build a short ad around the approved hero image.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *leads-to* `g13-0219`

- `g13-0219` *STATED* — Runable guide step 4: turn the same assets into a landing page.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *leads-to* `g13-0220`

- `g13-0220` *STATED* — Runable guide step 5: verify the complete launch, including checks for signups and checkout.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *contrast* `g13-0167` — launch verification vs failure-path testing
  ↳ *evidence-for* `r02-0129`

- `g13-0221` *STATED* — Alex's Runable workflow keeps one visual direction across product shots, ads and the website, with 4 copyable prompts.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *enables* `g13-0207`

- `g14-0009` *STATED* — Begin an AI marketing workflow with one campaign, one audience and one useful action you want the reader to take.
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0003`
  ↳ *example-of* `g14-0349`
  ↳ *evidence-for* `g19-0276`

- `g14-0011` *STATED* — Write the brand brief once and reuse it across every stage of the marketing workflow.
  > “Write the brand brief once”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`
  ↳ *enables* `g14-0002` — brand check needs a brief

- `g14-0014` *STATED* — Use audience evidence (how readers actually responded) to improve the next run of the marketing workflow.
  > “Use audience evidence to improve the next run”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`
  ↳ *qualifies* `g14-0002`

- `g14-0026` *STATED* — Make a task map for your own work to think through how AI could change your job.
  > “Make a task map for your own work”
  — [g-anthropic-2030-economic-scenarios-explained](https://chen.media/guides/anthropic-2030-economic-scenarios-explained)
  ↳ *part-of* `g14-0015`
  ↳ *leads-to* `g14-0027`

- `g14-0027` *STATED* — Compare evidence before changing your career plans in response to AI-economy scenarios.
  > “Compare evidence before changing your plans”
  — [g-anthropic-2030-economic-scenarios-explained](https://chen.media/guides/anthropic-2030-economic-scenarios-explained)
  ↳ *part-of* `g14-0015`

- `g14-0126` *STATED* — Test Jev by running a small useful trial and a practical first project before building on it.
  > “Run a small useful trial”
  — [g-jev-typesafe-ai-explained](https://chen.media/guides/jev-typesafe-ai-explained)
  ↳ *part-of* `g14-0113`
  ↳ *example-of* `g14-0349`

- `g14-0334` *CORE* — Alex's service method: pick one trade, point the tool at the one job that trade hates doing, and charge a monthly fee to keep doing it.
  > “picking one trade, pointing the tool at the one job that trade hates doing, and charging a monthly fee to keep doing it”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)

- `g14-0335` *STATED* — Service method step 1: pick one trade (one industry niche).
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0334`
  ↳ *leads-to* `g14-0336`

- `g14-0336` *STATED* — Service method step 2: point the AI tool at the one job that trade hates doing.
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0334`
  ↳ *leads-to* `g14-0337`

- `g14-0337` *STATED* — Service method step 3: charge a monthly fee to keep doing that job.
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0334`

- `g14-0344` *STATED* — The three-services guide ends with what to do if you try only one thing.
  > “If you try only one thing”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0329`

- `g15-0047` *STATED* — Every linkedin-skills skill follows the same three-step pattern: it drafts, shows you the draft, and waits; nothing is published until you approve it.
  > “Every skill shows you a draft first and waits for your OK before doing anything. Nothing gets posted without your approval.”
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *part-of* `g15-0041`
  ↳ *example-of* `g15-0182`

- `g15-0102` *STATED* — The guide's plan for charging for these tools runs Build, Market, Sell (sections locked).
  — [g-three-free-ai-tools-you-can-sell-as-a-service](https://chen.media/guides/three-free-ai-tools-you-can-sell-as-a-service)

- `g16-0186` *STATED* — Tip 11 (expert): build working software from the Code tab, in plain English.
  > “11. Build working software from the Code tab, in plain English”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *qualifies* `g16-0253`

- `g16-0202` *STATED* — Build prompt 1: write a full PRD.
  > “Write a Full PRD”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0196`

- `g17-0168` *STATED* — In the 15-swaps guide every price is the highest self-serve plan on that tool's pricing page, not the entry one.
  > “Every price is the highest self serve plan on that tool's pricing page, not the entry one.”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0167`

- `g17-0195` *STATED* — Before cancelling a paid tool, run the free alternative for a full week on real work.
  > “Run the free tool for a full week on real work first.”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *because* `g17-0194`
  ↳ *qualifies* `g17-0191`
  ↳ *example-of* `g17-0307`

- `g17-0197` *STATED* — In the ten-tools guide each paid tool is priced on its SECOND paid tier (the plan you move to when the entry plan stops being enough), with the entry price in brackets.
  > “Each paid tool below is priced on its SECOND paid tier”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0193`
  ↳ *contrast* `g17-0168` — second paid tier vs highest self-serve tier

- `g17-0222` *STATED* — Alex Chen's ten-tools guide explains how to actually do the paid-to-free swap without breaking anything.
  > “How to actually do the swap”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0195`

- `g17-0297` *STATED* — In Alex Chen's career-ops guide, anything that could not be confirmed from a primary source is marked as unconfirmed instead of repeated.
  > “Anything that could not be confirmed from a primary source is marked as such instead of repeated.”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0292`

- `g17-0298` *STATED* — career-ops' four jobs (read postings, flag fakes, find the human, write the negotiation) are covered in the order you will actually use them.
  > “The four things, in the order you will actually use them”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *part-of* `g17-0291`

- `g17-0300` *STATED* — Alex Chen's career-ops guide covers running it yourself.
  > “Running it yourself”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0294`

- `g19-0048` *STATED* — The six-site sweep runs on two Claude prompts, an intake prompt and a sweep prompt, while one field is deliberately left for you to type yourself.
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *part-of* `g19-0047`

- `g19-0058` *STATED* — The six-site guide has a 'How to run it' section and a 'Checking one site vs. checking all six' comparison.
  > “Checking one site vs. checking all six”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *part-of* `g19-0047`

- `g19-0116` *STATED* — The lead machine needs Claude Code, a terminal, and about ten minutes.
  > “You need Claude Code, a terminal, and about ten minutes.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0111`

- `g19-0117` *STATED* — Run the four lead-machine prompts in order: The Target, The Scraper, The Verifier, The Writer.
  > “Run the four prompts in order.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0111`

- `g19-0119` *STATED* — Swap the niche and city on step one and the whole lead machine re-runs for a brand new market.
  > “Swap the niche and city on step one and the whole thing re-runs for a brand new market.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *depends-on* `g19-0120`
  ↳ *evidence-for* `g19-0227`

- `g19-0120` *STATED* — Lead step 1, The Target: one line in (a niche and a city); out comes a plan for where those businesses actually live online, so the scraper is not guessing.
  > “One line in: a niche and a city. Out: a plan for where those businesses actually live online, so the scraper is not guessing.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0117`
  ↳ *leads-to* `g19-0131`

- `g19-0122` *STATED* — The Target prompt asks Claude to 'Build me a source plan, not the list yet.'
  > “Build me a source plan, not the list yet.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`

- `g19-0123` *STATED* — The source plan's first return item: the public places the business type is listed, namely directories, association sites, map listings and their own websites.
  > “directories, association sites, map listings, and their own websites”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`

- `g19-0124` *STATED* — The Target prompt has Claude rank each lead source by how complete it is and how easy it is to pull from.
  > “Rank each by how complete it is and how easy it is to pull from.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`

- `g19-0125` *STATED* — The source plan lists, for each source, the fields to expect: business name, website, phone, email, contact name.
  > “business name, website, phone, email, contact name”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`

- `g19-0126` *STATED* — The Target prompt asks for a realistic total count of businesses to expect in the city.
  > “A realistic total count I should expect in this city.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`

- `g19-0127` *STATED* — The Target prompt asks for one search you can run to reach each source.
  > “One search I can run to reach each source.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`

- `g19-0131` *STATED* — Lead step 2 is The Scraper, which pulls the businesses from the planned sources.
  > “The Scraper”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0117`
  ↳ *leads-to* `g19-0132`

- `g19-0132` *STATED* — Lead step 3 is The Verifier, the stage that makes the leads 'verified'.
  > “The Verifier”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0117`
  ↳ *leads-to* `g19-0133`
  ↳ *evidence-for* `g13-0066`

- `g19-0133` *STATED* — Lead step 4 is The Writer.
  > “The Writer”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0117`

- `g19-0219` *STATED* — The design-tools guide closes with 'Which one to actually use' and 'Last thing'.
  > “Which one to actually use”
  — [g-five-hyped-ai-design-tools-judged-the-way-a-client-would](https://chen.media/guides/five-hyped-ai-design-tools-judged-the-way-a-client-would)
  ↳ *part-of* `g19-0212`

- `g19-0225` *STATED* — Build the shop one phone line that always gets answered: an AI voice picks up, talks to the customer, and books the job into the calendar.
  > “An AI voice picks up, talks to the customer, and books the job into the calendar.”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`
  ↳ *example-of* `g14-0342`

- `g19-0227` *CORE* — Build the voice line one time, then reskin the same setup for the next shop with different words.
  > “You build it one time, then reskin the same setup for the next shop with different words.”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`

- `g19-0230` *STATED* — Voice-line step: pick one type of business, then paste a prompt to scope that trade and find what would make an owner in it stop and listen.
  > “that would make an owner in this trade stop and listen”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`
  ↳ *analogy-for* `g19-0276` — pick one trade / one industry
  ↳ *evidence-for* `g14-0335`

- `g19-0231` *STATED* — Voice-line step 'What the voice says, asks, and does' uses a Paste-This-to-Build-the-Brain prompt that keeps those things clearly separated.
  > “things, clearly separated:”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`

- `g19-0232` *STATED* — Voice-line step 'Give the brain a phone number' includes a prompt to get unstuck on setup that flags the one step people get wrong.
  > “Flag the one step people get wrong”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`

- `g19-0233` *STATED* — To reskin the voice line per client, paste the prompt with your working build attached ('[paste your Part 2 Output]') and have Claude give it back ready to paste in.
  > “[paste your Part 2 Output]”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`
  ↳ *part-of* `g19-0227`

- `g19-0234` *STATED* — The one question that closes the voice-line sale: 'Quick question. How many calls did you miss last week?'
  > “Quick question. How many calls did you miss last week?”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`

- `g19-0235` *STATED* — After the owner thinks about the calls that walked away, offer to put the voice line on their number for a week so they can hear it work.
  > “number for a week so you can hear it work?”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *leads-to* `g19-0234`

- `g19-0239` *CORE* — The three-step play: find a complaint that repeats, build the one feature people actually use, and charge less.
  > “Find a complaint that repeats, build the one feature people actually use, charge less.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0238`

- `g19-0240` *STATED* — Step 1 of the play: find a complaint about an existing product that repeats across reviewers.
  > “Find a complaint that repeats”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0239`

- `g19-0241` *STATED* — Step 2 of the play: build only the one feature people actually use.
  > “build the one feature people actually use”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0239`

- `g19-0242` *STATED* — Step 3 of the play: charge less than the incumbent.
  > “charge less”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0239`

- `g19-0254` *STATED* — The fix for Claude not reading Reddit is a reversal: you collect the Reddit posts, Claude finds the pattern.
  > “The fix is a reversal: you collect, Claude finds the pattern.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0249` — workaround
  ↳ *evidence-for* `g10-0002`

- `g19-0265` *STATED* — The pricing complaint you want lives in the Cons field of three- and four-star reviews.
  > “The complaint you want lives in the Cons field of three and four star reviews”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *contrast* `g19-0261`
  ↳ *part-of* `g19-0240`

- `g19-0275` *STATED* — Build the carousel workflow (Section 2) before sending the pitch (Section 4), so when a shop says yes you can turn their idea into a finished post the same day.
  > “build the workflow first so that when a shop says yes, you can turn their idea into a finished post the same day”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0274`

- `g19-0276` *CORE* — Carousel-service step 1: pick one industry and stay there.
  > “Pick one industry and stay there”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0274`
  ↳ *evidence-for* `g14-0335`

- `g19-0278` *STATED* — Pick ONE industry and refuse the rest until you are full.
  > “Pick ONE and refuse the rest until you are full.”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0276`

- `g19-0286` *STATED* — Carousel-service step 2: build the workflow once.
  > “Build the workflow once”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0274`
  ↳ *part-of* `g19-0275`
  ↳ *depends-on* `g19-0279`
  ↳ *evidence-for* `g19-0227`

- `g19-0287` *STATED* — Carousel-service step 3: price it so it is an easy yes.
  > “Price it so it is an easy yes”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0274`

- `g19-0288` *STATED* — Carousel-service step 4: send the exact pitch that gets the yes.
  > “The exact pitch that gets the yes”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *part-of* `g19-0274`
  ↳ *part-of* `g19-0275`

- `g20-0065` *STATED* — Faceless YouTube Step One is 'The brain'.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`
  ↳ *leads-to* `g20-0066`
  ↳ *analogy-for* `g20-0023` — brain step

- `g20-0066` *STATED* — Faceless YouTube Step Two is 'The voice, and what actually has to be built'.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`
  ↳ *leads-to* `g20-0067`
  ↳ *analogy-for* `g20-0028`

- `g20-0067` *STATED* — Faceless YouTube Step Three is 'The loop, and its real limits'.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`

- `g20-0076` *STATED* — Carousel setup 1: go to claude.ai/projects, click New Project and name it Carousels.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0071`
  ↳ *leads-to* `g20-0077`

- `g20-0077` *STATED* — Carousel setup 2: on the project page, find the panel on the right and click 'Set project instructions'.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0071`
  ↳ *leads-to* `g20-0078`

- `g20-0078` *STATED* — Carousel setup 3: paste the carousel prompt into the project instructions panel, not in the chat box.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0071`
  ↳ *leads-to* `g20-0079`
  ↳ *example-of* `g20-0289`

- `g20-0079` *STATED* — Carousel setup 4: click 'Save instructions'.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0071`
  ↳ *leads-to* `g20-0080`

- `g20-0080` *STATED* — Carousel setup 5: open a New chat inside the Carousels project and type only your topic.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0071`
  ↳ *example-of* `g20-0085`

- `g20-0085` *STATED* — The carousel guide's prompts are 'The prompt' (saved once), 'The topic line' (what you type per chat) and 'The fix line' (for corrections).
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0070`
  ↳ *leads-to* `g20-0087`

- `g20-0086` *STATED* — The carousel guide has a 'Your brand' section for adapting the decks to your brand.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0070`

- `g20-0087` *STATED* — Carousel finishing steps: 'Getting it out of Claude', then 'Into Canva'.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0070`

- `g21-0097` *STATED* — To build a premium site, open one chat and hand Claude the business, your brand, and a site you like the look of; it builds the whole thing.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0094`

- `g21-0099` *STATED* — Website step 1, the brief: tell Claude the business, paste your logo + photos, and drop a link to a site you love.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0097`
  ↳ *leads-to* `g21-0100`

- `g21-0100` *STATED* — Website step 2, the build: one prompt builds every page as a real site, not a template.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0097`
  ↳ *leads-to* `g21-0101`

- `g21-0102` *STATED* — Website step 4, put it live: preview it, then deploy it free or hand it to the client.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0097`

- `g21-0175` *STATED* — Paste your resume into the agents as text (not a screenshot) so it can be read cleanly, and keep the real job description handy for agent two (the Recruiter).
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0170`
  ↳ *enables* `g21-0186`

- `g21-0178` *STATED* — Diagnoser output 1, PARSE ERRORS: anything the parser would drop, garble, or misfile (tables, columns, headers, footers, graphics, text in images, unusual section names, dates it cannot read).
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0177`
  ↳ *evidence-for* `g21-0184`

- `g21-0179` *STATED* — Diagnoser output 2, SCREEN OUT LINES: quote every bullet verbatim that would hurt, each with one reason code: NO METRIC / PASSIVE / VAGUE / NO PROOF / DUPLICATE / DATED.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0177`

- `g21-0180` *STATED* — Diagnoser output 3, MISSING SECTIONS: the sections a recruiter expects and cannot find.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0177`

- `g21-0181` *STATED* — Diagnoser output 4: a 0 to 100 parse-and-match score, plus the single change that would raise it the most.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0177`

- `g21-0185` *STATED* — Resume rule: fix the parse before the prose.
  > “Fix the parse before the prose.”
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *generalizes* `g21-0183`

- `g21-0222` *STATED* — repurpose.md body opens 'You are my repurposer. Source material: $ARGUMENTS' and asks for outputs ready to be copy-pasted.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0221`

- `g21-0223` *STATED* — repurpose.md outputs include one X thread of 7 to 10 posts, one LinkedIn post, five short captions, and one short email to your list.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0222`

- `g21-0224` *STATED* — repurpose.md ends by picking the single best piece to post first and saying why.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *qualifies* `g21-0223`

- `g21-0231` *STATED* — trends.md body opens 'You are my trend scout. Niche: $ARGUMENTS' and finds what is overperforming in this niche right now.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0230`
  ↳ *example-of* `g21-0211`

- `g21-0232` *STATED* — For each trend, trends.md returns the trend in one line, why it is working, a specific content angle for your brand, and a ready-to-use hook, then names one to jump on today.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0231`

- `g21-0235` *STATED* — Each calendar.md entry gives the day, the platform and format, the pillar it serves, and a working hook.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0234`

- `g22-0084` *STATED* — Drop your bank statements, receipts and exports into one folder and point Claude at it.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *leads-to* `g22-0085`
  ↳ *defines* `g22-0087`

- `g22-0087` *STATED* — Bookkeeping step 1: one folder; drop your statements, receipts and exports in.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`
  ↳ *leads-to* `g22-0088`

- `g22-0088` *STATED* — Bookkeeping step 2: one prompt; point Claude at the folder and tell it to categorize everything using your rules.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`
  ↳ *leads-to* `g22-0089`

- `g22-0092` *STATED* — Bookkeeping guide section 'Set up the folder' gives the exact folder structure (body email-gated).
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0086`
  ↳ *part-of* `g22-0087`
  ↳ *example-of* `g02-0234`

- `g22-0093` *STATED* — Bookkeeping guide section 'Your categorization rules' gives copy-ready rules for categorizing transactions.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0086`
  ↳ *enables* `g22-0088`

- `g22-0094` *STATED* — Bookkeeping guide section 'The prompt' holds the reconcile-and-categorize prompt.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0088`

- `g22-0137` *STATED* — Save your brand brief so you can spin up a fresh brand for every new idea in minutes.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *part-of* `g22-0143`
  ↳ *evidence-for* `g14-0011`

- `g22-0143` *STATED* — Brand setup step 5: save the brief; for the next idea paste it back, change one line and regenerate for a fresh brand in minutes.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *part-of* `g22-0138`

- `g22-0147` *STATED* — Meta Ads guide section 'The first 5 prompts' gives the first five prompts to run once connected.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0145`

- `g22-0151` *STATED* — Once the Meta Ads connector is live you manage campaigns by chatting: pull numbers, pause the losers, feed the winners, and launch new campaigns, all inside your real account.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *contrast* `g12-0303` — Meta Ads connector pauses and launches campaigns in your real account by chat

- `g22-0224` *STATED* — Screen-record the Claude Wrapped artifact and it is your Story.
  — [g-build-your-own-claude-wrapped-from-your-real-stats](https://chen.media/guides/build-your-own-claude-wrapped-from-your-real-stats)
  ↳ *leads-to* `g22-0217`

- `g22-0228` *STATED* — Give Claude your site and a few competitors; it finds the topics they get free Google traffic from that you are missing.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`
  ↳ *leads-to* `g22-0229`

- `g22-0229` *STATED* — Claude ranks the missing keyword topics by how easy each is to win.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *leads-to* `g22-0230`
  ↳ *part-of* `g22-0232`

- `g22-0230` *STATED* — Claude then writes the article to take each keyword: title, headings, meta, even the schema Google looks for.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0233`

- `g22-0231` *STATED* — Keyword-gap step 1: point Claude at the targets, your site plus 2-3 competitors.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`
  ↳ *leads-to* `g22-0232`

- `g22-0232` *STATED* — Keyword-gap step 2 ('Find the gap'): find the keywords competitors win on that you do not, sorted easiest-to-win first.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`
  ↳ *leads-to* `g22-0233`

- `g22-0233` *STATED* — Keyword-gap step 3 ('Write the article that takes it'): Claude writes each article built to rank, ready to paste into your site.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`

- `g22-0234` *STATED* — Keyword-gap tip: turn on web search (or paste competitors' top pages or their sitemap URL) so Claude is reading their real content, not guessing.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *qualifies* `g22-0231`
  ↳ *example-of* `g22-0280`

- `g22-0238` *STATED* — Keyword-gap guide closes with 'Pro tips'.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`

- `g23-0114` *STATED* — The closet-flip method is three word-for-word prompts: price every item from a single photo, write the listing that actually sells, and let Claude post and reply to buyers for you.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)

- `g23-0116` *STATED* — You take one photo of the pile and Claude reads every item in it.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0121`

- `g23-0120` *STATED* — Run the three closet prompts in order.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *qualifies* `g23-0114`

- `g23-0121` *STATED* — Closet Prompt 1 of 3 'Price the Pile': every item priced from one photo.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0114`

- `g23-0122` *STATED* — Closet Prompt 2 of 3 'the Sell-this-week Listing': the listing that actually sells.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0114`

- `g23-0123` *STATED* — Closet Prompt 3 of 3 'Let Claude Do It': post it and reply to buyers for you.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0114`

- `g23-0162` *STATED* — Four resume prompts: read the job posting, rewrite your resume to match what the screener scans for, check it back line by line, and make it sound human.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *leads-to* `g23-0163`
  ↳ *because* `g23-0168`

- `g23-0166` *STATED* — Run the four resume prompts in order: they match the screener truthfully and in your voice, then make the resume read like a person wrote it.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *qualifies* `g23-0162`

- `g23-0169` *STATED* — Resume Prompt 1 of 4 'Read the Posting': see exactly what the bot scans for.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *part-of* `g23-0162`
  ↳ *depends-on* `g23-0165`

- `g23-0170` *STATED* — Resume Prompt 2 of 4 'Rewrite to Match': rewrite to hit every keyword, truthfully.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *part-of* `g23-0162`

- `g23-0171` *STATED* — Resume Prompt 3 of 4 'Re-check Line by Line': score it back against the posting.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *part-of* `g23-0162`
  ↳ *analogy-for* `g23-0030` — score-back is a self-grade against a rubric
  ↳ *example-of* `g23-0200`

- `g23-0172` *STATED* — Resume Prompt 4 of 4 'Make It Human': so it passes the human too.
  — [g-four-prompts-that-rewrite-your-resume-for-the-posting](https://chen.media/guides/four-prompts-that-rewrite-your-resume-for-the-posting)
  ↳ *part-of* `g23-0162`

- `r01-0042` *STATED* — '/agency setup' interviews you once: your offer, who you sell to, your price, your voice.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0043` *STATED* — '/agency outbound leads.csv' (outbound agent) writes a personal first email for every business on your list, ready to send from your own email.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0044` *STATED* — '/agency sales prep acme' (sales agent) writes a one-page call plan: questions, objections, price, the next step.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0045` *STATED* — '/agency sales live call.txt' (sales agent) coaches you during the call, one line at a time, from any live transcript file.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0046` *STATED* — '/agency build acme' (workflow agent) writes the proposal, then builds the automation with a README and a test.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0047` *STATED* — '/agency support' (customer service agent) sorts client emails and drafts every reply in your voice.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0049` *STATED* — '/agency status' shows what's waiting on you.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`

- `r01-0051` *STATED* — The /agency outbound agent writes the emails and a mail-merge file; you send them from your own email at a pace your provider allows.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0050`

- `r01-0063` *STATED* — Every /agency outbound email says who it's from and how to opt out.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0043`
  ↳ *analogy-for* `g19-0236`

- `r01-0064` *STATED* — /agency keeps opt-outs in .agency/DO-NOT-CONTACT.md, and the outbound agent always checks it before anything is written.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0043`

- `r01-0071` *STATED* — /agency setup question 1: What do you build for clients? (for example: AI receptionists, lead follow-up, booking automations)
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`
  ↳ *leads-to* `r01-0077` — Offer

- `r01-0072` *STATED* — /agency setup question 2: Who do you sell to? (one kind of business, one city or country if it matters)
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`
  ↳ *leads-to* `r01-0077` — Customer
  ↳ *evidence-for* `g14-0335`

- `r01-0073` *STATED* — /agency setup question 3: What does a client pay, and what do they get for it?
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`
  ↳ *leads-to* `r01-0077` — Price

- `r01-0074` *STATED* — /agency setup question 4: What do you need to get on a call? (the one result that makes a business owner reply)
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`
  ↳ *leads-to* `r01-0077` — Promise

- `r01-0076` *STATED* — /agency setup question 6: your name, your business name, and the link people book a call with.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`
  ↳ *leads-to* `r01-0077` — Sign-off

- `r01-0082` *STATED* — /agency cold email structure, in the user's voice: the specific detail, the one problem the offer fixes for a business like theirs, the promise, and one clear ask (a 15-minute call, with the booking link).
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0043`
  ↳ *evidence-for* `g04-0033`

- `r01-0085` *STATED* — /agency saves each cold email as .agency/outbox/<business>.md with To, Subject and Body at the top.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0043`

- `r01-0086` *STATED* — /agency writes .agency/outbox/SEND.csv (email, subject, body) so all emails can be sent from your own email tool's mail merge.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0043`
  ↳ *enables* `r01-0051`

- `r01-0090` *STATED* — Before a call, /agency sales prep reads everything in .agency/clients/<client>/ plus the client's website.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0044`

- `r01-0091` *STATED* — /agency writes .agency/clients/<client>/CALL.md: who they are in three lines, the three questions to ask first, likely objections with a one-line answer each, the price to quote, and the one next step to close on.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0044`
  ↳ *enables* `r01-0093` — live lines move to the next step from CALL.md

- `r01-0093` *STATED* — Each time the client says something new, /agency sales live prints ONE short line the user can say next: answer the question, handle the objection, or move to the next step from CALL.md.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0045`

- `r01-0095` *STATED* — When the user types stop, /agency sales live writes .agency/clients/<client>/NOTES.md: what they want, objections, what was promised, next step.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0045`
  ↳ *leads-to* `r01-0097` — NOTES.md feeds PROPOSAL.md

- `r01-0097` *STATED* — /agency writes PROPOSAL.md from NOTES.md (asking what's missing): their problem in their words, what you will build, what it will do for them (one number if you have one), the timeline, the price, and what you need from them.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0096`
  ↳ *leads-to* `r01-0098`

- `r01-0099` *STATED* — /agency builds in .agency/clients/<client>/build/: working code or an importable workflow file for the tool the client uses, a README on how to run it, and a test that proves the main path works.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0096`

- `r01-0103` *STATED* — /agency support sorts each client email into question, problem, change request, billing, or happy.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0047`

- `r01-0105` *STATED* — /agency support puts anything that needs a decision or money at the top.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0047`

- `r01-0110` *STATED* — /agency status shows leads written to, emails waiting to send, calls prepped, proposals waiting for approval, builds and their tests, replies waiting, and what is left in the queue.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *defines* `r01-0049`

- `r01-0123` *STATED* — The automated screen first checks the resume can be read top to bottom: columns, tables, text in images and odd section names all break it.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0122`
  ↳ *leads-to* `r01-0124` — checks run in order
  ↳ *evidence-for* `g21-0184`
  ↳ *evidence-for* `g21-0178`
  ↳ *evidence-for* `g21-0185`

- `r01-0124` *STATED* — The automated screen's second check: are the job titles, employers and dates clear?
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0122`
  ↳ *leads-to* `r01-0125`

- `r01-0125` *STATED* — With a job posting, the automated screen checks which of the posting's key skills and terms appear in the resume and which are missing.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0122`
  ↳ *leads-to* `r01-0126`

- `r01-0126` *STATED* — The automated screen's last check: contact details present, length sensible, no filler.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0122`

- `r01-0137` *STATED* — /hiring-panel rewrites the resume with the same facts and every numbered mistake fixed, adding nothing that is not in the original or in what the user said.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *leads-to* `r01-0139`

- `r01-0149` *STATED* — Everything after /hiring-panel is the resume: a file path (PDF is fine) or pasted text, optionally followed by a job posting or role.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0116`

- `r01-0288` *STATED* — The candle judge notes a granted leave would also let the user test full-time hours with a way back — test the risky variable without burning the fallback.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0273`
  ↳ *depends-on* `r01-0246`
  ↳ *leads-to* `r01-0290`

- `r02-0015` *STATED* — Jobs below the /hunter threshold are listed with the reason and nothing is written for them.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0082`

- `r02-0025` *STATED* — /hunter prepares the resume, the cover letter and an answer for every field; you say yes, it opens the page, and you paste and press submit.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0312`

- `r02-0026` *STATED* — When you tell /hunter you sent an application, the job goes into `.hunter/applications.md`, your list of everywhere you applied.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0025`

- `r02-0028` *STATED* — Questions only you can answer (work authorization, salary, demographics, legal) are left for you in the /hunter packet marked `YOU`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0025`

- `r02-0042` *STATED* — If a /hunter source can't be read it says so and moves on.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0072`

- `r02-0058` *STATED* — Setup question 1: your resume as a file path (PDF is fine) or pasted text, saved as `.hunter/RESUME.md`, the master copy that is never edited afterwards.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`

- `r02-0059` *STATED* — Setup question 2: target roles (up to five titles) and titles you do not want.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`

- `r02-0060` *STATED* — Setup question 3: locations (cities, remote only, or hybrid) and any work authorization limit, for example "need visa sponsorship".
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`

- `r02-0061` *STATED* — Setup question 4: a salary floor if any, and anything that rules a company out (industries, sizes).
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`

- `r02-0062` *STATED* — Setup question 5: contact details for forms: name, email, phone, links (LinkedIn, portfolio, GitHub) and earliest start date.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`

- `r02-0063` *STATED* — Setup question 6: where to look: a company career page URL, a Greenhouse/Lever/Ashby job-board URL (for example `boards.greenhouse.io/<company>`), an RSS feed of jobs, or "I'll paste postings"; saved to `.hunter/SOURCES.md`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`
  ↳ *depends-on* `r02-0008`

- `r02-0064` *STATED* — Setup question 7: the score needed to continue, default 80.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0057`
  ↳ *defines* `r02-0014`

- `r02-0067` *STATED* — After setup /hunter tells the user each command in one line and says that the profile and resume stay on this computer.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0016`
  ↳ *qualifies* `r02-0039`

- `r02-0071` *STATED* — /hunter run step 1 (Find, headhunter): fetch every source in `.hunter/SOURCES.md`; career pages and RSS are fetched and read.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`

- `r02-0073` *STATED* — /hunter run step 2 (Filter): drop postings already in `.hunter/seen.md`, postings that break a Dealbreaker or a Not-these title, and clear mismatches of location or level.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`

- `r02-0074` *STATED* — /hunter adds every posting it looked at to `.hunter/seen.md` (one line: date, company, role, link) so later runs only see new jobs.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0073`
  ↳ *example-of* `r02-0313`

- `r02-0080` *STATED* — A /hunter job's fit score is the average of the recruiter's and hiring manager's scores.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`

- `r02-0082` *STATED* — /hunter run step 4 (Keep only the high ones): everything below the threshold is listed one line each with its score and gap and gets no resume, cover letter or application.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`
  ↳ *depends-on* `r02-0014`

- `r02-0083` *STATED* — /hunter run step 5 (Tailor, resume writer) writes `.hunter/jobs/<date>-<company>-<role>/RESUME.md` and `COVER-LETTER.md` for each job that continues.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`
  ↳ *part-of* `r02-0011`

- `r02-0088` *STATED* — /hunter run step 6 (Fill out, form filler) writes `PACKET.md` in the same job folder.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`
  ↳ *part-of* `r02-0012`

- `r02-0090` *STATED* — /hunter ends the list by asking: "Tap yes for the ones to send: give me numbers, or 'all ready'."
  > “Tap yes for the ones to send: give me numbers, or 'all ready'.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0089`
  ↳ *example-of* `r02-0003`

- `r02-0091` *STATED* — /hunter saves a short `.hunter/TODAY.md` with the same list, ending with the credit line.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0089`

- `r02-0093` *STATED* — The top of a /hunter PACKET.md holds the company, role, posting link, the score line, the reason from each scorer, and GAPS.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0092`

- `r02-0096` *STATED* — If an application form cannot be read (most are built with scripts), /hunter says so and asks the user to paste the questions, then answers them.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0094`
  ↳ *generalizes* `r02-0043`

- `r02-0100` *STATED* — A /hunter packet ends with a final check line asking whether every `[ADD:]` and `YOU` is answered; until then the status is `needs you`, not `ready`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0092`
  ↳ *depends-on* `r02-0085`

- `r02-0102` *STATED* — During review /hunter says "Paste these answers in, attach the files, and press submit yourself." and waits for "done" or "skip".
  > “Paste these answers in, attach the files, and press submit yourself.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0101`

- `r02-0103` *STATED* — On "done" /hunter sets the job's status to `applied` in `.hunter/applications.md` with today's date, and never marks `applied` on its own.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0101`
  ↳ *enables* `r02-0026`

- `r02-0104` *STATED* — `/hunter applied <number or all>` marks sent jobs as `applied`, and adds a new row if the user sent one without /hunter.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0020`

- `r02-0105` *STATED* — `/hunter job` runs steps 3 to 7 on one posting, skipping the filter because the user picked it; if it scores below threshold it says so and asks whether to continue anyway.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0018`

- `r02-0106` *STATED* — `/hunter log` shows `.hunter/applications.md` newest first, then what is `ready` or `needs you`, adding new rows above the credit line so it stays last.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0021`

- `r02-0108` *STATED* — The /hunter morning message is "N new jobs fit you, M are ready for your yes."
  > “N new jobs fit you, M are ready for your yes.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0107`

- `r02-0114` *STATED* — /hunter rule: respect each site's rules, read only public postings, and keep going if one source fails.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *generalizes* `r02-0041`
  ↳ *evidence-for* `g19-0128`

- `r02-0200` *STATED* — Do not start fixing during the /launch poll; when it is over, offer to work through "Fix before launch" in order, then `/launch --recheck` to poll only the stations that held.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *leads-to* `r02-0147`

- `r02-0203` *STATED* — CaptionPal was written to look finished and to have the kind of problems a launch check should catch; do not deploy it, and its key in `app/config.py` is fake.
  > “It was written to look finished and to have the kind of problems a launch check should catch. **Do not deploy it.**”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0202`

- `r02-0204` *STATED* — CaptionPal runs with `python3 -m app.server` at http://localhost:8000; its tests run with `python3 -m unittest discover -s tests`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0202`

- `r02-0212` *STATED* — The /launch board is a table of Station, Call and Why, with each Why written in plain words a non-engineer understands.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0135`

- `r02-0214` *STATED* — The flight director's write-up has four sections: The holds, Fix before launch, Watch list, and Then.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *defines* `r02-0134`

- `r02-0215` *STATED* — The flight director's holds merge findings across stations under shared tags, e.g. hold 1 "SECURITY, DATABASE: Anyone can download every email and password hash from /admin/users, or sign in as anyone and read their captions."
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`

- `r02-0221` *STATED* — CaptionPal fix 1 [SECURITY]: delete /admin/users.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0286`

- `r02-0222` *STATED* — CaptionPal fix 2 [SECURITY]: parameterise find_user, make users.email UNIQUE, and hash passwords with salted scrypt.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0286`

- `r02-0223` *STATED* — CaptionPal fix 3 [SECURITY]: on login set a `secrets.token_urlsafe` session in an HttpOnly, Secure cookie and require it on /captions and /api/captions.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0286`

- `r02-0224` *STATED* — CaptionPal fix 4 [COST]: enforce FREE_CAPTIONS_PER_DAY per user, cap description length, drop `Access-Control-Allow-Origin: *`, and set a provider spending cap.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0257`

- `r02-0225` *STATED* — CaptionPal fix 5 [DATABASE]: make migrate() skip applied migrations.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0264`

- `r02-0226` *STATED* — CaptionPal fix 6 [USERS]: add a /login page and a signed-in form that saves three captions and lists them, escaped, on /captions.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0308`

- `r02-0227` *STATED* — CaptionPal fix 7 [SPEED]: captions_for becomes one indexed `WHERE user_id = ? LIMIT 50` query, plus a urlopen timeout and ThreadingHTTPServer.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0294`

- `r02-0228` *STATED* — CaptionPal fix 8 [RECOVERY]: read AI_KEY and BILLING_ACCOUNT from the environment, add logging, /health and a friendly AI error, and commit and tag in git.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0271`
  ↳ *depends-on* `r02-0266`

- `r02-0229` *STATED* — CaptionPal fix 9 [RULES]: link a privacy policy and terms from sign-up, and remove "Check your inbox".
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0278`

- `r02-0230` *STATED* — CaptionPal fix 10 [TESTS]: add server tests for fixes 1-9.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *part-of* `r02-0301`

- `r02-0231` *INFERRED* — The flight director orders fixes security first, then cost, data, user journey, speed, recovery, rules and finally tests that lock all prior fixes in.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *generalizes* `r02-0221`
  ↳ *generalizes* `r02-0230`
  ↳ *qualifies* `r02-0134`

- `r02-0232` *STATED* — CaptionPal watch list: a nightly database backup (DATABASE) and confirming the AI price fits $100/month (COST).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *depends-on* `r02-0260`
  ↳ *depends-on* `r02-0251`

- `r02-0233` *STATED* — CaptionPal watch list: HTTPS on the VPS (SECURITY, unchecked), account deletion (RULES), and restarts signing everyone out (RECOVERY).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *depends-on* `r02-0245`

- `r02-0234` *STATED* — CaptionPal's Then step: start the server twice, then `/launch --recheck` all eight stations, and launch only on eight GOs.
  > “Start the server twice, then `/launch --recheck` all eight stations. Launch only on eight GOs.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0214`
  ↳ *example-of* `r02-0200`

- `r02-0251` *STATED* — COST could not check the budget because no price per generation was given, so it wrote its assumptions: 3 generations per click, and 20 per person per day is 600 a month per user.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0252`
  ↳ *example-of* `r02-0245` — explicit assumptions when price unknown

- `r02-0257` *STATED* — COST fix: require a signed-in session on `/api/captions`, enforce `FREE_CAPTIONS_PER_DAY` per user, and set a monthly spending cap at the AI provider.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0246`

- `r02-0264` *STATED* — DATABASE fix: make user rows reachable only by their owner (remove or guard /admin/users, random session tokens, parameterized find_user) and have migrate() skip migrations already applied.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0258`

- `r02-0271` *STATED* — RECOVERY fix, where no single change suffices: record applied migrations so restarts work, document BILLING_ACCOUNT, add logging plus a /health route, put a timeout and friendly error on the AI call, and commit a tagged release to git before going live.
  > “No single change suffices”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0265`

- `r02-0278` *STATED* — RULES fix: on the sign-up page link a privacy policy and terms (what is collected, that descriptions go to the AI provider, how to delete an account), and remove the "check your inbox" line until an email is really sent.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0272`

- `r02-0282` *STATED* — SECURITY watch: passwords are unsalted MD5 (db.py:24, 34); use salted scrypt or pbkdf2.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0279`
  ↳ *leads-to* `r02-0222`

- `r02-0283` *STATED* — SECURITY watch: the AI key is hard-coded in app/config.py:5 (commented as fake), so a real key would have to go into source code; read it from an environment variable.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *leads-to* `r02-0228`

- `r02-0286` *STATED* — SECURITY fix: rebuild sign-in with random session tokens in an HttpOnly cookie checked on every route, a parameterised query in find_user, and /admin/users removed or locked.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0279`

- `r02-0294` *STATED* — SPEED fix: make `captions_for` one `SELECT ... WHERE user_id = ? ORDER BY id DESC LIMIT 50` with an index on `user_id`, add a timeout to the AI calls, and switch to `ThreadingHTTPServer`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0287`

- `r02-0308` *STATED* — USERS fix: build the missing journey: a sign-in page that sets a session cookie, and a signed-in caption form that calls the AI, saves the three captions and shows them on /captions with an empty state.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0302`

- `r03-0144` *STATED* — Save your LinkedIn profile as a PDF (desktop only): Me, View profile, More or Resources, Save to PDF.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *leads-to* `r03-0145`

- `r03-0157` *STATED* — /linkedin-roast step 4: it rewrites the headline (220 characters or fewer), the About (2,600 or fewer) and every experience entry.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0134`
  ↳ *leads-to* `r03-0160`

- `r03-0158` *CORE* — /linkedin-roast bullets follow Harvard College's Mignone Center for Career Success resume guide: start with an action verb, say specifically what you did, and end on a result with a number.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0157`
  ↳ *evidence-for* `g21-0179`

- `r03-0160` *STATED* — /linkedin-roast step 5: it makes the banner with code, and writes the headshot prompt (or uses an image tool if you already have one connected).
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0134`

- `r03-0190` *STATED* — /linkedin-roast pulls out the headline, About, every experience (title, employer, dates, bullets), education, skills, and any notes about the banner and photo; if a saved PDF doesn't show them it writes 'not in the file' and moves on.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0154`

- `r03-0222` *STATED* — Headline fix: write one new headline of 220 characters or fewer (count them and say the count), then two alternates.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0157`
  ↳ *depends-on* `r03-0183`

- `r03-0223` *STATED* — Headline order: the job and the strongest search words first, then what you do and for whom, or the result.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0222`

- `r03-0225` *STATED* — About fix: rewrite it in 2,600 characters or fewer (count them), in one to three short paragraphs.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0157`
  ↳ *depends-on* `r03-0184`

- `r03-0226` *STATED* — The About's first sentence says what the person does and for whom, the best proof comes early, and first person is fine there.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0225`

- `r03-0227` *STATED* — Choose 8 to 12 keywords (job titles, tools, methods and industries) that (a) the profile already backs up and (b) the five roasters say people in this field search for.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0225`
  ↳ *evidence-for* `g23-0167`

- `r03-0229` *STATED* — Under the new About, print a table of keyword, where it went, why it helps; the reason given is that recruiters search by these words and LinkedIn Recruiter's search highlights matches in the Summary, Experience and Skills sections.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0227`

- `r03-0232` *STATED* — Rewrite EVERY experience entry, including the ones the roasters liked.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0157`

- `r03-0234` *STATED* — Start each bullet with an action verb, and use a different verb each time.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0232`
  ↳ *part-of* `r03-0158`

- `r03-0236` *STATED* — Say what you did, specifically, and end on the result; make it fact-based: quantify and qualify.
  > “quantify and qualify”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0232`
  ↳ *part-of* `r03-0158`

- `r03-0239` *STATED* — Bullets use no 'I', no slang, no unnecessary abbreviations and no story-telling, and stay easy to skim at one or two lines a bullet.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0232`

- `r03-0240` *STATED* — Use present tense for the current role and past tense for finished ones, as in the MCS sample resume, and write numbers as numerals the same way each time.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0232`

- `r03-0241` *STATED* — Keep each entry's title, employer and dates exactly as they are, with two to five bullets a role, strongest first.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0232`

- `r03-0242` *STATED* — A bullet with no information in it ('various tasks as needed') can be removed, shown as 'Removed' with the reason.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0232`

- `r03-0245` *STATED* — Banner: write linkedin-roast-output/banner.svg with width="1584" height="396" viewBox="0 0 1584 396": a solid or two-colour background, and in large type the new job title plus one short line that is true in the profile.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0160`
  ↳ *depends-on* `r03-0185`
  ↳ *leads-to* `r03-0249`

- `r03-0247` *STATED* — Put banner text in the middle or on the right, away from the lower left where the profile photo overlaps.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0245`
  ↳ *because* `r03-0185` — banner sits behind the profile photo

- `r03-0253` *STATED* — If no converter works, keep only the SVG and tell the user LinkedIn takes JPG or PNG, so they must convert it (open it in a browser and screenshot it, or use any free converter).
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0249`

- `r03-0254` *STATED* — Headshot: ONLY if a connected image tool can generate or edit an image from a reference photo, ask the user for their own photo (a file path), run it, save the result in the output folder, and say which tool made it.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0160`

- `r03-0256` *STATED* — Without an image tool, write headshot-prompt.md: a ready-to-paste prompt asking for a clean, shoulders-up professional headshot of the person in the attached photo, keeping their real face and features, plain neutral background, soft even light, clothes that suit their field, plus 'attach your own photo'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0160`
  ↳ *contrast* `r03-0254`

- `r03-0257` *STATED* — headshot-prompt.md adds three notes: LinkedIn says the photo must reflect your likeness, so do not let a tool change your face; use a square crop of at least 400 x 400 pixels, JPG or PNG, under 8 MB; the photo goes to whichever image tool you use, so read its privacy terms.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0256`
  ↳ *depends-on* `r03-0186`

- `r03-0258` *STATED* — Create ONE folder, linkedin-roast-output/, in the user's working directory holding roasts.md, new-profile.md (headline + 2 alternates, About, keyword table, 'Add only if true' list, every entry before/after, every [ADD YOUR NUMBER] question), banner.png/.svg and headshot-prompt.md or the generated image.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *defines* `r03-0147`

- `r03-0261` *STATED* — /linkedin-roast finishes in chat with the folder path, then the [ADD YOUR NUMBER] questions as one list ('answer these and I will update new-profile.md'), then the paste checklist.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *defines* `r03-0152`

- `r03-0262` *STATED* — Paste checklist items 1-3: Headline, paste the new one (220 characters or fewer); About, paste it in; Experience, replace each role's text, filling in the [ADD YOUR NUMBER] gaps first.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0261`

- `r03-0263` *STATED* — Paste checklist items 4-5: Banner, upload banner.png (1584 x 396); Photo, upload your new photo (at least 400 x 400, and it must look like you).
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0261`
  ↳ *depends-on* `r03-0185`

- `r04-0091` *STATED* — The night crew scout goes looking for people who need what you make (real posts and threads with links), writes draft replies, and drafts the marketing you asked for (a week of social posts, a launch video script); drafts only, it never posts.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0087`

- `r04-0144` *STATED* — Scout step 1: read 'The app' and 'Customers', then search the listed places (and find better ones if they're thin) for real people asking for what the app does, complaining about the problem it solves, or comparing tools for it; public pages only, never sign up for or log in to anything.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0091`
  ↳ *depends-on* `r04-0125`
  ↳ *evidence-for* `g19-0128`

- `r04-0145` *STATED* — Scout report night-crew/reports/<date>-scout.md lists the 10 best leads: who, where, a link, what they said, and why they fit.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0091`

- `r04-0146` *STATED* — The scout writes draft replies for the best 3 leads (helpful first, the app mentioned only where it fits); drafts only, never posted.
  > “helpful first, the app mentioned only where it fits”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0091`
  ↳ *qualifies* `r04-0134`
  ↳ *example-of* `g02-0237`

- `r04-0147` *STATED* — The scout report includes 'What people keep asking for' that isn't in the Backlog yet.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0091`
  ↳ *contrast* `r04-0153` — scout's demand signals vs tracker's build-next
  ↳ *evidence-for* `g10-0015`

- `r04-0148` *STATED* — Scout step 3: write the requested marketing into night-crew/marketing/<date>/ (for example posts.md with one post per day, or launch-video-script.md with a shot list).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0091`
  ↳ *depends-on* `r04-0126`

- `r04-0149` *STATED* — Scout step 4: open a draft pull request titled 'Night crew (scout): leads and drafts for <date>', with the top 3 leads in its description.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0091`

- `r04-0167` *STATED* — Night crew interview question 1: the app in one sentence, and who it is for ('a booking app for dog groomers').
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0166`

- `r04-0169` *STATED* — Night crew interview question 3: the customers, who would pay and where they talk online (subreddits, forums, communities); if they don't know, the scout will find out.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0166`

- `r04-0170` *STATED* — Night crew interview question 4: marketing to draft, e.g. a week of social posts or a launch video script.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0166`

- `y01-0082` *STATED* — Alex's agency walkthrough: install the agency inside Claude, set up the teams, run it on a real business, then sell what it creates to other businesses or run it yourself.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *depends-on* `y01-0079`

- `y01-0120` *STATED* — Starting an AI agency from zero, don't sell all the tools at once - pick one service, for example AI visibility.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *evidence-for* `g14-0335`
  ↳ *part-of* `y01-0127`

- `y01-0121` *STATED* — Agency step 1: use the sales team to find businesses that are a good fit.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0127`
  ↳ *leads-to* `y01-0122`
  ↳ *depends-on* `y01-0103`

- `y01-0122` *STATED* — Agency step 2: use the GEO team to figure out exactly what those businesses are missing.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0127`
  ↳ *leads-to* `y01-0123`
  ↳ *depends-on* `y01-0114`

- `y01-0123` *STATED* — Agency step 3: use the sales team again to write personalized outbound pitches that solve their problems.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0127`
  ↳ *leads-to* `y01-0124`
  ↳ *depends-on* `y01-0106`

- `y01-0124` *STATED* — Agency step 4: once you close someone, deliver the real work with the systems already installed from the repo.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0127`

- `y01-0125` *STATED* — Later, upsell the agency client to other services such as marketing, SEO and content.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *leads-to* `y01-0124`

- `y01-0127` *STATED* — Alex's agency formula: find the client, pinpoint the problem, sell them the solution, then deliver the outcome through the repo.
  > “all you have to do is just find the client, pinpoint the problem, and sell them the solution, and then you can deliver the outcome through this repo.”
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0082`

- `y02-0002` *STATED* — To use the Harvey customer-hunting agent you just tell it what you sell and who your dream customer is, and it goes hunting for prospects for you.
  > “you just tell it what you sell and who your dream customer is and it goes hunting for you”
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *evidence-for* `g04-0030`
  ↳ *part-of* `y02-0001`

- `y02-0004` *STATED* — The Harvey agent writes each prospect a cold email about something real it found on their site, so it never sounds like spam.
  > “it writes each one a cold email about something real it found on their site, so it never sounds like spam”
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *evidence-for* `g04-0033`
  ↳ *part-of* `y02-0001`
  ↳ *leads-to* `y02-0005` — personalised email -> replies handled -> meeting

- `y02-0150` *STATED* — MiroFish method: give it your product page, price or ad and ask 'will people love it or ignore it?'.
  > “you give it your product page, price, or ad, and ask, will people love it or ignore it?”
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *evidence-for* `g09-0204`
  ↳ *part-of* `y02-0148`

- `y02-0154` *STATED* — After a MiroFish run you can ask any of the simulated customers why they didn't buy your product.
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *evidence-for* `g09-0205`
  ↳ *part-of* `y02-0148`

- `y03-0145` *STATED* — SupoClip doesn't edit randomly: it asks four questions about every single clip.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *example-of* `g12-0194`
  ↳ *part-of* `y03-0143`
  ↳ *leads-to* `y03-0150`
  ↳ *generalizes* `y03-0155`

- `y03-0155` *INFERRED* — SupoClip's four questions double as a checklist for any short you make: hook, retention, usefulness and shareability.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)

- `y03-0160` *STATED* — Runnable keeps the same visual direction across assets so everything looks like it belongs to the same brand.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *evidence-for* `g13-0221`
  ↳ *qualifies* `y03-0159`

- `y03-0161` *STATED* — You can ask Runnable to build the landing page, product details, email signup and checkout.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *evidence-for* `g13-0219`
  ↳ *part-of* `y03-0157`

- `y03-0167` *STATED* — Ask Reddit's Ask for the most common problems in your niche and you get a real list of pain points.
  — [Ab_9hEiq6NI](https://youtu.be/Ab_9hEiq6NI)
  ↳ *evidence-for* `g10-0015`
  ↳ *depends-on* `y03-0166`
  ↳ *leads-to* `y03-0168`

- `y03-0168` *STATED* — Paste the Reddit pain points into Claude and Claude turns them into real video ideas and digital products that solve those problems.
  — [Ab_9hEiq6NI](https://youtu.be/Ab_9hEiq6NI)
  ↳ *evidence-for* `g10-0016`
  ↳ *leads-to* `y03-0169`

- `y04-0035` *STATED* — After the assets, ask Runnable to build the landing page, product details, email signup and checkout.
  > “ask it to build the landing page, product details, email signup, and checkout”
  — [TKrtaLRIHBg](https://youtu.be/TKrtaLRIHBg)
  ↳ *evidence-for* `y03-0161`
  ↳ *leads-to* `y04-0036`

- `y04-0137` *STATED* — Instead of asking what skill to learn for 2030, ask what you can actually own.
  > “instead of asking what skill you should be learning for 2030, you should be asking what you can actually own”
  — [HAKXPtoRXh8](https://youtu.be/HAKXPtoRXh8)
  ↳ *contrast* `g14-0026` — ask what you can own vs map how AI changes your tasks

### number

- `g01-0042` *STATED* — Claude Resume Kit setup takes about 10 minutes per paper, done once.
  — [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything)
  ↳ *qualifies* `g01-0035`

- `g01-0048` *CORE* — After santifer open-sourced career-ops it passed 74,000 stars on GitHub.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *evidence-for* `g01-0044`

- `g01-0049` *INFERRED* — career-ops' published funnel means about 1 in 11 evaluated posts became an application (68/740 = 9.2%) and about 1 in 6 applications became an interview process (12/68 = 17.6%).
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *qualifies* `g01-0047`

- `g01-0052` *CORE* — career-ops will not push you to apply below 4.0/5, though you can override it.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *qualifies* `g01-0051`

- `g02-0103` *INFERRED* — santifer's career-ops funnel works out to about 9% of evaluated posts applied to (68/740), about 18% of applications reaching interviews (12/68), and 1 offer from 12 interview processes.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *qualifies* `g02-0101`
  ↳ *evidence-for* `g02-0106` — selectivity: only ~9% of evaluated posts got an application
  ↳ *evidence-for* `g01-0049`

- `g02-0106` *STATED* — career-ops will not push you to apply to a role scored below 4.0/5, though you can override it.
  > “It will not push you to apply below 4.0/5 (you can override it).”
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *qualifies* `g02-0105`
  ↳ *example-of* `g02-0243`
  ↳ *evidence-for* `g01-0052`

- `g02-0213` *STATED* — Video Use adds a 30 ms audio fade at every cut, so you never hear a pop.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`
  ↳ *evidence-for* `g02-0218` — one visible reason the cuts land cleanly

- `g03-0063` *INFERRED* — santifer's career-ops funnel works out to roughly 9% of evaluated posts applied to (68/740) and about 18% of applications reaching interviews (12/68).
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *generalizes* `g03-0062`
  ↳ *evidence-for* `g01-0049`

- `g04-0148` *STATED* — On Fiverr, basic LinkedIn audits were listed at $5 to $50 and full LinkedIn rewrites at $300 or more (listings seen on October 10, 2026).
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *evidence-for* `g04-0150`
  ↳ *evidence-for* `r03-0136`
  ↳ *example-of* `g22-0276`

- `g06-0191` *STATED* — LTX 2.5 commercial use is free only under $10M a year in annual revenue (whole company, including affiliates); above that you need a paid Commercial Use Agreement.
  — [g-run-ltx-2-5-the-open-weights-ai-video-model-on-your-own-computer](https://chen.media/guides/run-ltx-2-5-the-open-weights-ai-video-model-on-your-own-computer)
  ↳ *part-of* `g06-0190`
  ↳ *example-of* `g18-0288`

- `g07-0245` *STATED* — On Fiverr, basic LinkedIn audits were listed at $5 to $50 and full rewrites at $300 or more (listings seen on October 10, 2026).
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *contrast* `g07-0251` — paid audits vs free reviews
  ↳ *example-of* `g07-0292`
  ↳ *example-of* `g07-0301`
  ↳ *evidence-for* `g04-0148`

- `g10-0003` *STATED* — Alex Chen's Reddit AI search guide (chen.media) contains 7 prompts to copy and 3 numbered steps.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0002`

- `g10-0011` *STATED* — Since May 2026 Reddit's AI does the reading of threads and comments for you.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *part-of* `g10-0012`

- `g10-0022` *STATED* — Reddit's AI search works in six languages: English, Spanish, Brazilian Portuguese, Italian, French and German.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *qualifies* `g10-0001`

- `g10-0023` *STATED* — Reddit's AI search (Reddit Answers) already had 15 million weekly users before it moved into the main search bar.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *evidence-for* `g10-0014`

- `g10-0234` *STATED* — Lovable Pro costs $25 a month for 100 credits, and every prompt spends some.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *evidence-for* `g10-0224`
  ↳ *evidence-for* `g10-0267`

- `g10-0241` *STATED* — Lovable Pro is $300 a year, and Lovable's free plan gives you 5 build credits a day.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *contrast* `g10-0240`

- `g12-0135` *STATED* — SEO skill speed check, Core Web Vitals: the main content loads in under 2.5 seconds (LCP), the page reacts in under 200 ms (INP), and nothing jumps around (CLS under 0.1).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0133`
  ↳ *because* `g12-0136`

- `g12-0159` *STATED* — Apple's App Store opened with a few hundred apps, more than 800 by its first weekend, when people downloaded 10 million of them in three days.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *evidence-for* `g12-0158`

- `g12-0186` *STATED* — OpusClip turns one long video into short clips, and its Pro plan is $29 a month.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *contrast* `g12-0187`

- `g12-0197` *STATED* — Guide section 'What it costs' covers SupoClip's running costs (body email-gated).
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0184`
  ↳ *contrast* `g12-0186`

- `g12-0254` *STATED* — Anthropic's team merged more than three thousand changes in the speed sprint without a customer-facing incident or rollback.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *evidence-for* `g12-0252`

- `g12-0257` *STATED* — At the 75th percentile, a fresh claude.ai load until the page is typeable went from 3.1 s to 0.55 s.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *evidence-for* `g12-0252`

- `g12-0259` *STATED* — At the 75th percentile, loading a Claude Cowork cloud session went from 2.6 s to 0.73 s.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *evidence-for* `g12-0252`

- `g13-0045` *STATED* — Until September 30, 2026, Higgsfield gives every verified business $1 of cashback for every $1 spent on its API, up to $100,000.
  — [g-higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy](https://chen.media/guides/higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy)
  ↳ *part-of* `g13-0043`

- `g13-0046` *STATED* — Higgsfield's API cashback is paid from a $20 million pool.
  — [g-higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy](https://chen.media/guides/higgsfield-s-api-cashback-how-to-set-it-up-and-a-distribution-strategy)
  ↳ *qualifies* `g13-0045`

- `g13-0208` *STATED* — At the September 22, 2026 check, Runable listed a free plan with daily credits and access to website, image and video creation.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *qualifies* `g13-0204`
  ↳ *example-of* `g17-0314`

- `g17-0167` *STATED* — All 15 business tools in Alex Chen's 'free swaps' part 3 cost $1057 a month at their top tier; the switchable ones cost $870.
  > “All 15 at their top tier is $1057 a month. Switchable: $870.”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)

- `g17-0220` *STATED* — Alex Chen's ten-tools guide totals what the ten paid AI tools add up to.
  > “What that adds up to”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)

- `g19-0054` *STATED* — About $70 billion in unclaimed money sits across the six-site systems combined.
  > “About $70 billion sits across all of them combined”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *qualifies* `g19-0052`
  ↳ *evidence-for* `g19-0047`

- `g19-0055` *STATED* — Roughly 1 in 7 Americans has unclaimed money in at least one of the systems.
  > “roughly 1 in 7 Americans has something in at least one”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *evidence-for* `g19-0056` — odds justify checking all six

- `g19-0112` *STATED* — Agencies sell a lead list for $2,000.
  > “Agencies sell a lead list for $2,000.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *contrast* `g19-0115`
  ↳ *part-of* `g19-0114`
  ↳ *example-of* `g22-0276`

- `g19-0113` *STATED* — Clay and Apollo, the tools that build lead lists, run about $600 a month between them.
  > “Clay and Apollo, run about $600 a month between them”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *contrast* `g19-0115`
  ↳ *part-of* `g19-0114`
  ↳ *example-of* `g22-0276`

- `g19-0222` *STATED* — A plumber misses about a dozen calls a week.
  > “A plumber misses about a dozen calls a week.”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *evidence-for* `g19-0221`
  ↳ *part-of* `g19-0224`

- `g19-0255` *STATED* — Collecting Reddit posts by hand for Claude to analyse takes about 30 minutes (Section 2 of the complaint guide).
  > “it takes about 30 minutes”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0254`

- `g19-0280` *STATED* — The second dentist takes half the time the first one did, because you already know what a dentist's feed is supposed to look like.
  > “The second dentist takes half the time the first one did”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *evidence-for* `g19-0279`

- `g20-0068` *STATED* — The faceless YouTube guide has a 'The Numbers: What it costs, and what it pays' section.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`

- `g21-0025` *STATED* — A local business or founder pays 4 to 5 figures for an AI service like a support agent, content engine or lead engine.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *evidence-for* `g21-0020`

- `g21-0095` *STATED* — Alex says a premium website the old way took two weeks and thousands of dollars; with Claude it is one afternoon.
  > “The old way took two weeks and thousands of dollars. This is one afternoon.”
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0094`
  ↳ *example-of* `g22-0276`

- `g21-0106` *STATED* — Designers charge hundreds for a single graphic and take a week.
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)
  ↳ *evidence-for* `g21-0105`
  ↳ *example-of* `g22-0276`

- `g22-0138` *STATED* — The brand studio's one-time setup is done once per brand and takes about 5 minutes.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *part-of* `g22-0126`

- `r01-0094` *STATED* — /agency live coaching never prints more than two lines at once.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0093`

- `r01-0242` *STATED* — Statistician's deciding fact: covering $1,600 rent from gross sales takes about 57 sales a month at $28, over four times the roughly 13 a month in the record.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r01-0241`

- `r01-0245` *STATED* — Parent's deciding fact: 40 sales at $28 over three months is about $373 a month, under a quarter of the $1,600 rent, so the $8,000 is gone in under seven months even if every sales dollar were profit.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r01-0244`

- `r01-0259` *STATED* — Prosecution point 1: sales cover under a quarter of rent; at least $1,227 a month drawn from savings on rent alone; covering rent needs 58 sales a month, more than four times today's 13.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0257`
  ↳ *example-of* `r01-0258`
  ↳ *contradicts* `r01-0242` — 58 vs about 57 sales a month

- `r01-0261` *STATED* — Prosecution point 2: $8,000 is five months of rent with no income, about 6.5 months counting gross sales as pure profit, and the record lists no materials, Etsy fees, shipping, food, utilities or insurance.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0257`
  ↳ *example-of* `r01-0258`

- `r01-0278` *STATED* — Prosecution point 2's cost line: the whole $8,000 gone in under seven months, with the job already given up.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0261`
  ↳ *contrast* `r01-0245` — same under-seven-months runway reached by prosecution and Parent

- `r02-0014` *STATED* — Only jobs at or above your /hunter threshold continue to tailoring; the default threshold is 80.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *leads-to* `r02-0015`

- `r02-0206` *STATED* — CaptionPal's owner expects about 1,000 sign-ups in the first month from a launch video, with 20 free captions per person per day planned.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0178`
  ↳ *example-of* `r02-0183`

- `r02-0210` *STATED* — CaptionPal's owner wants running costs under $100 a month at launch, and the AI provider charges per generation.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0178`
  ↳ *example-of* `r02-0183`

- `r02-0249` *STATED* — COST finding: each CaptionPal request costs 3 paid generations, so a script sending one request a second costs 259,200 generations a day.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0246`
  ↳ *depends-on* `r02-0247`

- `r02-0252` *STATED* — COST break-even: $100/month holds only if a generation costs under $0.00167 (100 users, 60,000/month) or $0.000167 (1,000 users, 600,000/month).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *depends-on* `r02-0210`
  ↳ *depends-on* `r02-0206`

- `r02-0289` *STATED* — SPEED measured on a scratch database: at 20,000 rows captions_for ran 20,001 queries in 122 ms.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0287`
  ↳ *evidence-for* `r02-0288`
  ↳ *example-of* `r02-0244`

- `r02-0290` *STATED* — SPEED measured: at 600,000 rows (1,000 users × 20 captions a day × 30 days) captions_for ran 600,001 queries in 6.1 s for every `/captions` view.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0287`
  ↳ *evidence-for* `r02-0288`
  ↳ *depends-on* `r02-0206`

- `r03-0183` *STATED* — LinkedIn headline: 220 characters at most; LinkedIn's help pages do not print this number (it is the widely reported limit), so trust the editor's counter if it differs.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0182`

- `r03-0184` *STATED* — LinkedIn About: 2,600 characters at most (LinkedIn's Talent Blog); LinkedIn Help suggests one or two short paragraphs about mission, motivation and skills.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0182`

- `r03-0185` *STATED* — LinkedIn banner: 1584 x 396 pixels, JPG or PNG, under 8 MB; it sits behind the profile photo, and the crop shifts with the browser window.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0182`

- `r03-0186` *STATED* — LinkedIn profile photo: JPG or PNG, from 400 x 400 up to 7680 x 4320 pixels, under 8 MB, and LinkedIn says it must reflect the user's likeness.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0182`

- `r03-0246` *STATED* — Banner text: at most two lines, each about 40 characters or fewer at 56 px.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0245`

- `r04-0271` *STATED* — Hot-sauce example unit cost: each box costs about $19 to fill and ship.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0226`
  ↳ *evidence-for* `r04-0287`

- `r04-0283` *STATED* — Founder answer: at about $19 a box, 500 boxes a month cost about $9,500 ($19 x 500).
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *depends-on* `r04-0271`
  ↳ *qualifies* `r04-0275`

- `r04-0287` *STATED* — Founder answer: $35 minus $19 leaves $16 per box per month before ads, so the most an ad can cost per subscriber is $16 times the months that person stays.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0277`
  ↳ *example-of* `g19-0245`

- `y02-0156` *STATED* — The MiroFish video title frames it as 'Test your launch on 1,000 fake customers' while the script says 'thousands of fake users'.
  — [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *qualifies* `y02-0148`

- `y02-0173` *STATED* — The Logo Design Skill replaces paying a logo site $96 a year.
  — [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20)
  ↳ *evidence-for* `g09-0176`
  ↳ *part-of* `y02-0172`

- `y03-0127` *STATED* — Framer costs up to $45 a month for each site; with Instatic you host your site anywhere you want instead.
  — [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY)
  ↳ *contradicts* `g17-0212` — Framer price: 'up to $45 a month for each site' vs Framer Pro $30/month (Basic $10)
  ↳ *evidence-for* `y03-0122`

### opinion

- `g01-0005` *STATED* — What a job seeker needs is the rejection reasons before applying; the /hiring-panel skill gives seven of them.
  > “What you need is the rejection reasons before you apply. This skill gives you seven of them.”
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *leads-to* `g01-0001`

- `g01-0065` *STATED* — Stop applying to every job: career-ops scores each job against your CV first.
  — [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *because* `g01-0052`
  ↳ *part-of* `g01-0044`

- `g04-0098` *STATED* — Alex's premise for /hiring-panel: a job seeker needs the rejection reasons before applying, and the skill gives seven of them.
  > “What you need is the rejection reasons before you apply.”
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *evidence-for* `g01-0005`

- `g04-0119` *STATED* — Alex frames /hiring-panel as the way to get a resume past the 'robot screen' by letting 7 Claudes try to reject it first.
  > “Get Your Resume Past the Robot Screen”
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri)
  ↳ *part-of* `g04-0117`
  ↳ *contrast* `g04-0120` — two headlines, same guide body
  ↳ *depends-on* `g04-0104`
  ↳ *example-of* `g04-0244`
  ↳ *example-of* `g02-0242`

- `g04-0120` *STATED* — Alex frames /hiring-panel as rejection practice: get rejected by seven Claudes before a real rejection counts.
  > “Practice Rejection Before It Counts”
  — [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0118`
  ↳ *example-of* `g04-0244`
  ↳ *example-of* `g02-0242`

- `g04-0150` *STATED* — Alex positions /linkedin-roast as the free alternative to a paid Fiverr LinkedIn review.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *qualifies* `g04-0149`
  ↳ *evidence-for* `r03-0136`

- `g08-0035` *STATED* — What a job seeker needs is the rejection reasons before applying, and /hiring-panel gives you seven of them.
  > “What you need is the rejection reasons before you apply. This skill gives you seven of them.”
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *leads-to* `g08-0028`
  ↳ *evidence-for* `g01-0005`

- `g08-0223` *STATED* — What you actually need to know about an idea is who will try to beat you, and how.
  > “What you actually need to know is who will try to beat you, and how.”
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *leads-to* `g08-0220`

- `g09-0019` *STATED* — The most expensive mistake a founder makes is six months spent building something nobody wants.
  > “The most expensive mistake a founder makes is six months spent building something nobody wants.”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *generalizes* `g09-0149`

- `g09-0149` *STATED* — Claude's helpful yes is the opposite of what you need before you spend money on an idea.
  > “That's the opposite of what you need before you spend money on an idea.”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *qualifies* `g09-0148`
  ↳ *evidence-for* `r04-0206`
  ↳ *evidence-for* `g08-0250`

- `g09-0157` *STATED* — The list of questions you couldn't answer is the useful part of the shark session: it's your to-do list before you pitch anyone real.
  > “That last list is the useful part. It's your to-do list before you pitch anyone real.”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *qualifies* `g09-0156`
  ↳ *evidence-for* `r04-0226`

- `g10-0014` *STATED* — For anyone who makes content or sells online, Alex Chen calls Reddit's Ask AI search the fastest research tool there is.
  > “that's the fastest research tool there is”
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *qualifies* `g10-0001`

- `g12-0143` *STATED* — For Google's AI answers: if your pages are not quotable, you're not mentioned.
  > “If you're not quotable, you're not mentioned.”
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *qualifies* `g12-0141`

- `g12-0161` *STATED* — Right now the Claude Marketplace shelf is as empty as it will ever be.
  > “Right now the shelf is as empty as it will ever be.”
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *depends-on* `g12-0158`

- `g14-0010` *STATED* — A smaller marketing campaign is easier to check than a month of unreviewed AI-generated posts.
  > “A smaller campaign is easier to check than a month of unreviewed posts.”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *because* `g14-0009`

- `g14-0338` *STATED* — Alex's three sellable services are the same method three times over, which is why he calls them methods rather than tools.
  > “That is the same method three times over, which is why they are methods rather than tools.”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *because* `g14-0334`

- `g14-0339` *CORE* — The tools are replaceable; the order of the method is not.
  > “The tools are replaceable. The order is not.”
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *generalizes* `g14-0338`
  ↳ *evidence-for* `g15-0101`

- `g15-0101` *CORE* — The tools are the easy half of selling an AI service, which is the part nobody puts in a video.
  — [g-three-free-ai-tools-you-can-sell-as-a-service](https://chen.media/guides/three-free-ai-tools-you-can-sell-as-a-service)
  ↳ *qualifies* `g15-0097`
  ↳ *leads-to* `g15-0102`
  ↳ *example-of* `g15-0175`
  ↳ *example-of* `g15-0177`

- `g16-0235` *STATED* — A cheaper subscription is still a subscription, while a removed meter is a line item that never comes back.
  > “a cheaper subscription is still a subscription and a removed meter is a line item that never comes back”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *qualifies* `g16-0234`

- `g17-0170` *STATED* — Six of the fifteen paid business tools are marked KEEP: Zoom, Google Workspace, Loom, HubSpot, Firefly and CapCut genuinely win.
  > “Zoom, Google Workspace, Loom, HubSpot, Firefly and CapCut genuinely win”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *because* `g17-0171`

- `g17-0188` *STATED* — Hotjar is easier to set up; Matomo is the one you own.
  > “Hotjar is easier to set up. Matomo is the one you own”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0180`

- `g17-0196` *CORE* — A tool you genuinely use is worth paying for.
  > “A tool you genuinely use is worth paying for.”
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0195`
  ↳ *generalizes* `g17-0171`

- `g18-0128` *STATED* — A tool you genuinely use is worth paying for.
  > “A tool you genuinely use is worth paying for.”
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0125`
  ↳ *evidence-for* `g17-0196`

- `g19-0271` *STATED* — The screenshot-the-pricing-page rule is the single cheapest thing in the complaint guide and converts its riskiest advice into defensible advice.
  > “it converts the riskiest advice in it into defensible advice”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *qualifies* `g19-0267`

- `g20-0056` *STATED* — The no-pay-for-mass-production rule is the thing almost nobody selling the faceless YouTube workflow will tell you.
  > “the thing almost nobody selling this workflow will tell you.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *qualifies* `g20-0055`

- `g20-0058` *STATED* — The YouTube inauthentic-content wording describes a lot of what gets sold as a faceless channel business, so read it slowly.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *qualifies* `g20-0059`

- `g22-0237` *STATED* — Keyword-gap guide section 'Why this beats the agency' argues the workflow beats paying an SEO agency.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)
  ↳ *part-of* `g22-0225`

- `g23-0073` *STATED* — 2026 tier list, Presentations: bad PowerPoint, mid Canva, great pick Gamma.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick)
  ↳ *part-of* `g23-0051`
  ↳ *because* `g23-0074`

- `g23-0177` *STATED* — Pro AI stack, Writing: beginners use ChatGPT; pros switch to Claude because it gives longer, more natural drafts and far better at following detailed instructions.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *evidence-for* `g23-0204`
  ↳ *example-of* `g23-0175`

- `g23-0178` *STATED* — Pro AI stack, Coding: beginners use ChatGPT, Lovable; pros switch to Cursor because it gives a real AI code editor that works across your whole project, not just snippets.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *evidence-for* `g23-0202`
  ↳ *example-of* `g23-0175`
  ↳ *contrast* `g23-0067` — Lovable: beginner tool vs mid
  ↳ *contrast* `g17-0212` — Lovable is a beginner tool pros leave for Cursor (pro stack) vs recommended free website-builder swap (ten-tools)

- `g23-0179` *STATED* — Pro AI stack, Video: beginners use InVideo, CapCut; pros switch to Higgsfield because it gives cinematic AI video and motion, instead of stitching templates together.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *evidence-for* `g23-0201`
  ↳ *example-of* `g23-0175`

- `g23-0180` *STATED* — Pro AI stack, Automation: beginners use Make; pros switch to Zapier because it gives the widest app ecosystem, so your workflows can connect to almost anything.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *example-of* `g23-0175`

- `g23-0181` *STATED* — Pro AI stack, Websites: beginners use Shopify, Replit; pros switch to Emergent because it gives describe the app and it builds and ships the whole thing for you.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *example-of* `g23-0175`
  ↳ *contrast* `g23-0067` — Emergent vs Claude Code for building whole apps

- `g23-0182` *STATED* — Pro AI stack, Research: beginners use Gemini, ChatGPT; pros switch to Perplexity because it gives sourced, cited answers you can actually trust and link back to.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *evidence-for* `g23-0203`
  ↳ *example-of* `g23-0175`

- `r03-0136` *STATED* — Alex positions /linkedin-roast as a free alternative to paying someone on Fiverr to review your profile.
  > “It is a free alternative to paying someone on Fiverr to review your profile.”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0134`

- `y01-0102` *STATED* — Alex calls the sales department possibly his favourite part of ai-agency-claude because it builds an entire sales pipeline to get new clients, not just do the work.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *qualifies* `y01-0103`

- `y02-0038` *STATED* — Alex Chen's framing: with The Agency 'you just became an AI agency owner for free'.
  > “You just became an AI agency owner for free.”
  — [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *part-of* `y02-0033`

- `y02-0149` *STATED* — Your friends won't tell you your launch will flop (video title) — which is why you test on simulated customers.
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk)
  ↳ *example-of* `g09-0254`
  ↳ *evidence-for* `g09-0194`
  ↳ *because* `y02-0148`

- `y02-0188` *CORE* — A recurring theme: free and open-source tools replace paid subscriptions — Adobe at $68.97/month, a logo site at $96/year, any app you pay for (rebuild), per-message AI fees (local MiniCPM), and a whole agency for $0.
  — [lhx8M2JPLPE](https://youtu.be/lhx8M2JPLPE) [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20) [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0) [nJLWbwhr13o](https://youtu.be/nJLWbwhr13o) [_O69QaBeuVU](https://youtu.be/_O69QaBeuVU) [pibEuNPl9NU](https://youtu.be/pibEuNPl9NU) [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *evidence-for* `g12-0301`
  ↳ *generalizes* `y02-0052`
  ↳ *generalizes* `y02-0173`
  ↳ *generalizes* `y02-0075`
  ↳ *generalizes* `y02-0016`
  ↳ *generalizes* `y02-0033`

- `y04-0086` *STATED* — Think about what you can build when every feature you need already exists for free.
  > “Think about what you can build when every feature you need already exists for free.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *because* `y04-0080`

- `y04-0136` *STATED* — The most important takeaway isn't whether AI takes your job, it's what you own if the value of your own work starts falling.
  > “the most important thing in this entire report isn't whether AI takes your job, it's what you own if the value of your own work starts falling”
  — [HAKXPtoRXh8](https://youtu.be/HAKXPtoRXh8)
  ↳ *leads-to* `y04-0137`

### prediction

- `y01-0110` *STATED* — Alex: showing up inside AI is something most businesses aren't thinking about yet but has huge potential over the next 1 to 2 years.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *because* `y01-0111`

### product

- `g01-0001` *STATED* — The free /hiring-panel Claude Code skill puts your resume in front of a hiring panel of seven Claudes that try to reject it, then rebuilds the resume with every mistake fixed.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *evidence-for* `r01-0116`

- `g01-0034` *STATED* — Claude Resume Kit is a free, open-source (MIT) set of Claude Code commands that writes a tailored resume, CV and cover letter for each job post.
  — [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything)
  ↳ *contrast* `g01-0044` — knowledge-base tailoring vs job-scoring agent
  ↳ *evidence-for* `r02-0083`

- `g01-0044` *CORE* — career-ops is a free, open-source job search agent that runs inside Claude Code.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)

- `g02-0080` *CORE* — GoLive is an open-source skill that takes an app Claude built live: hosting, database, domain, email and payments, on your own accounts.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *because* `g02-0081`

- `g02-0098` *STATED* — career-ops is a free, open-source job search agent that runs inside Claude Code.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *evidence-for* `g01-0044`

- `g02-0151` *STATED* — claude-seo is a free, open-source (MIT) plugin for Claude Code: one command, a team of agents, a fix list.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)

- `g02-0207` *STATED* — Video Use is a free, open-source skill for Claude Code from the Browser Use team that edits a folder of raw clips into a finished video.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *because* `g02-0209`

- `g03-0059` *STATED* — career-ops is a free, open-source job search agent that runs inside Claude Code.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *evidence-for* `g01-0044`

- `g04-0029` *CORE* — Harvey (https://github.com/ethanplusai/harvey) is a free, open-source AI sales agent under the MIT licence, made by ethanplusai.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *part-of* `g04-0054`
  ↳ *example-of* `g04-0252`
  ↳ *example-of* `g18-0288`

- `g04-0036` *STATED* — Harvey shows you everything it does on a local dashboard.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *part-of* `g04-0029`

- `g04-0099` *STATED* — /hiring-panel is a free Claude Code skill that puts your resume in front of a hiring panel of seven Claudes that try to reject it, then rebuilds the resume with every mistake fixed.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *because* `g04-0098`
  ↳ *evidence-for* `r01-0116`

- `g04-0149` *STATED* — /linkedin-roast is a free Claude Code skill that gives you five LinkedIn profile reviews for free, then fixes the profile.
  > “This skill gives you five reviews for free, then fixes the profile.”
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *because* `g04-0147`
  ↳ *part-of* `g04-0172`
  ↳ *part-of* `g04-0173`
  ↳ *evidence-for* `r03-0134`

- `g05-0238` *STATED* — Founder is a free, MIT-licensed set of eleven Claude skills that test a business idea before you launch it — before you spend a dollar.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *example-of* `g09-0254`
  ↳ *because* `g09-0019`

- `g06-0170` *STATED* — Anthropic's startup program lists up to $45,000 in discounts and credits from companies building with Claude, and you don't need investors to join.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)

- `g10-0001` *CORE* — Reddit built its AI into search: the Ask button next to the search bar reads real posts and comments and sums up the answer, with a link to every source.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)

- `g10-0012` *STATED* — Reddit's AI search started as Reddit Answers and now lives in the normal Reddit search bar.
  — [g-reddit-ai-search-content-research-goldmine](https://chen.media/guides/reddit-ai-search-content-research-goldmine)
  ↳ *defines* `g10-0001`

- `g13-0204` *CORE* — Runable is an app that can take one small brand brief through product imagery, an ad and a landing page.
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)

- `g15-0098` *STATED* — MoneyPrinterTurbo turns a topic into a short video.
  — [g-three-free-ai-tools-you-can-sell-as-a-service](https://chen.media/guides/three-free-ai-tools-you-can-sell-as-a-service)
  ↳ *example-of* `g15-0097`

- `g15-0099` *STATED* — GPT-SoVITS turns a minute of your voice into a cloned voice.
  — [g-three-free-ai-tools-you-can-sell-as-a-service](https://chen.media/guides/three-free-ai-tools-you-can-sell-as-a-service)
  ↳ *example-of* `g15-0097`

- `g15-0100` *STATED* — Hunyuan3D turns a single photo into a 3D model.
  — [g-three-free-ai-tools-you-can-sell-as-a-service](https://chen.media/guides/three-free-ai-tools-you-can-sell-as-a-service)
  ↳ *example-of* `g15-0097`

- `g15-0158` *STATED* — Google Opal turns plain English into a working mini app.
  — [g-the-four-google-ai-tools-worth-your-time](https://chen.media/guides/the-four-google-ai-tools-worth-your-time)
  ↳ *part-of* `g15-0156`

- `g15-0160` *STATED* — Google Pomelli reads your site instead of your brief.
  — [g-the-four-google-ai-tools-worth-your-time](https://chen.media/guides/the-four-google-ai-tools-worth-your-time)
  ↳ *part-of* `g15-0156`

- `g17-0199` *STATED* — Nano Banana is Google's image model, free inside the Gemini app, with no card and no queue.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0198`
  ↳ *qualifies* `g17-0072` — Nano Banana free in both Gemini app and Google AI Studio

- `g17-0201` *STATED* — Consensus searches actual peer-reviewed papers instead of the open web and shows how many studies support the answer; it has a free tier.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0200`

- `g17-0203` *STATED* — Hedra makes talking avatars from one photo plus a script, and its free credits refresh monthly.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0202`

- `g17-0205` *STATED* — Cursor's Hobby plan is $0 with no card and no time limit, but has limited agent requests and tab completions.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0204`

- `g17-0207` *STATED* — Hailuo gives free credits every day, roughly 3 to 5 clips, topped up on sign-in.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0206`

- `g17-0209` *STATED* — Photoroom does background removal and product shots; its free plan exports up to 250 images a month with a watermark.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0208`

- `g17-0211` *STATED* — Publer's free plan covers 3 accounts with 10 scheduled posts each.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0210`

- `g17-0213` *STATED* — Lovable's free plan gives 5 credits a day up to 30 a month, publishes live to a lovable.app subdomain, and needs no card.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0212`

- `g17-0215` *STATED* — Edits is Instagram's own video editor: genuinely free, no watermark.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0214`

- `g17-0216` *STATED* — CapCut has only one paid tier for individuals ($20/month CapCut Pro), so its row is the same at entry and second tier.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0214`
  ↳ *contradicts* `g17-0187` — CapCut Pro $20 only paid tier vs CapCut $9 as top tier

- `g17-0218` *STATED* — MiniMax gives free text-to-speech credits across many languages.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *qualifies* `g17-0217`

- `g17-0291` *STATED* — career-ops is an open-source job-search setup that reads every posting for you, flags the fake ones, finds the human behind the portal and writes your negotiation.
  > “reads every posting for you, flags the fake ones, finds the human behind the portal, and writes your negotiation”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *evidence-for* `g01-0044`

- `g21-0021` *STATED* — Sellable AI service #1: the 24/7 AI Support Agent.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *example-of* `g21-0020`

- `g21-0022` *STATED* — Sellable AI service #2: the AI Content Engine.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *example-of* `g21-0020`

- `g21-0023` *STATED* — Sellable AI service #3: the AI Lead Engine.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *example-of* `g21-0020`

- `g21-0176` *STATED* — Resume agent 1 of 4, the Diagnoser, reads your resume the way the machine does, not the way your friend does, to show the exact lines that get you screened out.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0174`
  ↳ *leads-to* `g21-0186`

- `g21-0186` *STATED* — Resume agent 2 of 4: the Recruiter (uses the real job description).
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0174`
  ↳ *leads-to* `g21-0187`

- `g21-0187` *STATED* — Resume agent 3 of 4: the Rewriter.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0174`
  ↳ *leads-to* `g21-0188`

- `g21-0188` *STATED* — Resume agent 4 of 4: the Hiring Manager.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0174`

- `r01-0037` *STATED* — The /agency skill (github.com/alexyc9381/agency-skill) is an AI automation agency that runs inside Claude Code: five agents, one command.
  > “Five agents, one command.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0001`

- `r01-0116` *STATED* — The /hiring-panel skill (github.com/alexyc9381/hiring-panel-skill) has seven Claudes try to reject your resume, then rebuilds the resume with every mistake fixed.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0001`

- `r02-0001` *STATED* — /hunter (github.com/alexyc9381/hunter-skill) is a free Claude Code skill: a headhunter made of five Claudes that finds new jobs that fit you, scores each one out of 100, rewrites your resume and cover letter for the high scorers, and fills out the whole application.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)

- `r03-0135` *STATED* — After the roast, /linkedin-roast fixes the profile: a new headline, an About section with the keywords people search for, every experience entry rewritten, a banner file and a headshot prompt.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *leads-to* `r03-0134`

- `y02-0001` *STATED* — Someone built a free Claude agent (Alex Chen's CTA keyword 'Harvey') whose only job is to get you customers.
  > “Someone built a Claude agent whose only job is to get you customers”
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *evidence-for* `g04-0029`
  ↳ *example-of* `y02-0194`

- `y02-0007` *STATED* — You watch everything the Harvey customer agent does on a live dashboard.
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *evidence-for* `g04-0036`
  ↳ *part-of* `y02-0001`

- `y02-0148` *STATED* — MiroFish is an open-sourced way to test your launch on thousands of fake users, and it just hit 75,000 stars (CTA keyword 'fish').
  > “It's called Mirofish and it shows how people will really react before you launch.”
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *evidence-for* `g09-0195`
  ↳ *example-of* `y02-0194`

- `y03-0156` *STATED* — Runnable puts an entire AI agency inside one app.
  — [3ZXrp-OQeGM](https://youtu.be/3ZXrp-OQeGM)
  ↳ *evidence-for* `g13-0204`

- `y04-0031` *STATED* — Runnable puts 'an entire AI agency inside one app': it writes the copy, generates the ads, and builds a website people buy from.
  > “Someone put an entire AI agency inside one app.”
  — [TKrtaLRIHBg](https://youtu.be/TKrtaLRIHBg)
  ↳ *evidence-for* `y03-0156`

### resource

- `g02-0012` *STATED* — /hunter can read career pages, job boards on Greenhouse, Lever or Ashby, an RSS feed, or postings you paste.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0011`
  ↳ *evidence-for* `r02-0008`

- `g02-0089` *STATED* — GoLive's live-tested hosting providers are Vercel and Netlify.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *part-of* `g02-0080`

- `g02-0090` *STATED* — GoLive's live-tested database providers are Supabase and Neon.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *part-of* `g02-0080`

- `g02-0091` *STATED* — GoLive's live-tested domain DNS providers are Porkbun and GoDaddy.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *part-of* `g02-0080`

- `g02-0092` *STATED* — GoLive's live-tested email provider is Resend.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *part-of* `g02-0080`

- `g02-0094` *STATED* — GoLive's live-tested sign-in provider is Supabase authentication.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *part-of* `g02-0090` — both Supabase

- `g02-0114` *STATED* — One career-ops guide has an email-gated worked example titled 'How the score works (an example)'.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a)
  ↳ *example-of* `g02-0105`
  ↳ *example-of* `g02-0234`

- `g02-0115` *STATED* — The other career-ops guide swaps that section for 'Why you hear nothing back (an example)', framing the same scoring as the reason mass applications get no replies.
  — [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *example-of* `g02-0097`

- `g02-0116` *STATED* — Both career-ops guides have 1 prompt and 5 numbered steps, plus email-gated 'Set it up' and 'The catch' sections.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *part-of* `g02-0098`
  ↳ *example-of* `g02-0232`

- `g02-0145` *STATED* — /awwwards builds the site in Next.js by default and in Astro for content-only showcases.
  — [g-have-claude-build-an-award-level-website-from-one-line](https://chen.media/guides/have-claude-build-an-award-level-website-from-one-line)
  ↳ *leads-to* `g02-0146`

- `g02-0159` *STATED* — claude-seo can optionally use Google credentials for Search Console, PageSpeed and GA4 as extras.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *qualifies* `g02-0158`

- `g02-0160` *STATED* — The claude-seo guide has 1 prompt and 4 numbered steps, with email-gated 'Step 1: set it up' and 'The catch' sections.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *part-of* `g02-0151`
  ↳ *example-of* `g02-0232`

- `g02-0218` *STATED* — The Video Use guide has 2 prompts and 4 numbered steps, with an email-gated 'Why the cuts land cleanly' section plus 'Set it up' and 'The catch'.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`
  ↳ *example-of* `g02-0232`

- `g04-0054` *STATED* — Guide: 'Harvey: a Free Claude Sales Agent That Finds Customers, Emails Them and Answers the Replies' at https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies (1 prompt, 11 numbered steps).
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *example-of* `g04-0243`

- `g04-0116` *STATED* — Alex's /hiring-panel guide has 8 ready-made prompts and 5 numbered steps; its locked sections are 'Get the skill', 'Run it on your resume', 'Ready-made ones to paste', 'What an answer looks like' and 'Good to know'.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0117`
  ↳ *part-of* `g04-0118`

- `g04-0117` *STATED* — Guide (headline A): 'Get Your Resume Past the Robot Screen: 7 Claudes Try to Reject It First (Free /hiring-panel Skill)' at https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri)
  ↳ *example-of* `g04-0243`

- `g04-0118` *STATED* — Guide (headline B): 'Practice Rejection Before It Counts: Run Your Resume Past 7 Claudes With the Free /hiring-panel Skill' at https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free
  — [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *example-of* `g04-0243`

- `g04-0171` *STATED* — Alex's /linkedin-roast guide has 8 prompts and 9 numbered steps; locked sections include 'Save your profile as a PDF', 'Get the skill', 'What you get', 'What an answer looks like', 'Worth knowing before you rely on it' and 'Where the numbers come from'.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0172`
  ↳ *part-of* `g04-0173`

- `g04-0172` *STATED* — Guide (headline A): '5 Claudes Roast Your LinkedIn Profile, Then Rewrite Every Line: Set Up the Free /linkedin-roast Skill' at https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li)
  ↳ *example-of* `g04-0243`
  ↳ *example-of* `g04-0244`
  ↳ *example-of* `g02-0242`

- `g04-0173` *STATED* — Guide (headline B): 'Roast Night for Your LinkedIn: 5 Claudes Tear It Apart and Rebuild It (Free /linkedin-roast Skill)' at https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked
  — [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *example-of* `g04-0243`
  ↳ *example-of* `g04-0244`
  ↳ *example-of* `g02-0242`

- `g06-0173` *STATED* — Anthropic Startup Stack offer: ElevenLabs, 12 months free plus 33M characters.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0174` *STATED* — Anthropic Startup Stack offer: ClickHouse, $5K in ClickHouse Cloud credits.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0175` *STATED* — Anthropic Startup Stack offer: Hex, 6 months free on the Enterprise plan.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0176` *STATED* — Anthropic Startup Stack offer: Granola, 3 months of Business free, up to 10 seats.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0177` *STATED* — Anthropic Startup Stack offer: Gamma, 25% off the first year of Gamma Pro annual.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0178` *STATED* — Anthropic Startup Stack offer: Firecrawl, 2.5x your plan's monthly credits for a year.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0179` *STATED* — Anthropic Startup Stack offer: Attention, 20% off the first year (7-day free trial).
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0180` *STATED* — Anthropic Startup Stack offer: Emergent, 20% off for the first 6 months.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0181` *STATED* — Anthropic Startup Stack offer: Augment Code, $100 in Cosmos credits.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0182` *STATED* — More Anthropic Startup Stack offers sit under "View more" on the startup program page.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0172`

- `g06-0183` *STATED* — Accepted Anthropic startup program members get Applied AI office hours with Anthropic: 45-minute live sessions, every other week.
  — [g-apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity](https://chen.media/guides/apply-to-anthropic-s-startup-program-and-what-anthropic-says-about-capacity)
  ↳ *part-of* `g06-0170`

- `g09-0193` *STATED* — chen.media guide 'Test Your Launch on a Crowd of Fake Customers Before Real Ones See It: How to Run MiroFish With Claude' (https://chen.media/guides/mirofish-test-your-launch-on-fake-customers) has 7 prompts to copy and 9 numbered steps; sections: What you get; How it works; What you need; Step 1: get it running; Step 2: make Claude play everyone; Step 3: give it your launch; Step 4: run it, small first; Step 5: read the report, then ask the ones who swam away; Three tests worth running; The honest part.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *example-of* `g09-0253`

- `g09-0209` *STATED* — The MiroFish guide lists three tests worth running.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *part-of* `g09-0193`

- `g11-0133` *STATED* — Alex's Ultrafast guide has a separate section for people building an app on the API.
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)
  ↳ *depends-on* `g11-0122`

- `g12-0066` *STATED* — Guide section 'What you need' lists the accounts and prerequisites for running the go-live skill (body email-gated).
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0050`
  ↳ *depends-on* `g12-0053`
  ↳ *example-of* `g02-0234`

- `g12-0256` *STATED* — Anthropic's post 'How we made claude.ai 3x faster in two weeks': https://claude.dev/blog/how-we-made-claude-ai-faster/
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *evidence-for* `g12-0252`
  ↳ *example-of* `g12-0300`

- `g13-0087` *STATED* — animos.app makes a launch video without an editor.
  — [g-4-free-sites-that-stop-your-app-looking-vibe-coded](https://chen.media/guides/4-free-sites-that-stop-your-app-looking-vibe-coded)
  ↳ *example-of* `g13-0084`

- `g13-0088` *STATED* — deck.gallery is a gallery of pitch decks to borrow from.
  — [g-4-free-sites-that-stop-your-app-looking-vibe-coded](https://chen.media/guides/4-free-sites-that-stop-your-app-looking-vibe-coded)
  ↳ *example-of* `g13-0084`

- `g14-0329` *STATED* — Alex's guide 'Three Services You Can Sell: a CRM Agent, an Editing Package and a Phone Agent' gives the two free repos, the one tool that is not a repo, the exact service to sell with each, and the honest note on what none of them removes.
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)

- `g14-0345` *STATED* — The three-services guide covers what each tool really does, how each installs, and the exact service you would sell with it.
  — [g-three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent](https://chen.media/guides/three-services-you-can-sell-a-crm-agent-an-editing-package-and-a-phone-agent)
  ↳ *part-of* `g14-0329`

- `g17-0256` *STATED* — Course 3 (turns it into money): Nate Herk's build and sell with Claude Code course.
  > “3. Nate Herk, build and sell with Claude Code”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *part-of* `g17-0253`

- `g17-0292` *STATED* — career-ops is by Santiago Fernandez de Valderrama Aparicio, published on GitHub under the MIT licence.
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *evidence-for* `g17-0291`
  ↳ *evidence-for* `g01-0046`
  ↳ *example-of* `g18-0288`

- `g19-0047` *STATED* — Alex's chen.media guide 'The Six-Site Sweep for Money You Are Already Owed' (category: Build & sell) gives all six official unclaimed-money links, the intake prompt, the sweep prompt, and the one field you type yourself.
  > “All six official links, the intake prompt, the sweep prompt, and the one field you type yourself.”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)

- `g19-0057` *STATED* — The six-site guide lists the exact page to search on each of the six unclaimed-money sites.
  > “Here are all six, with the exact page to search on each.”
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *part-of* `g19-0047`

- `g19-0111` *STATED* — Alex's chen.media guide 'Turn One Line Into Hundreds of Verified Leads for Nothing' (category: Build & sell) is the Claude Code build that turns one line into hundreds of verified leads for zero dollars.
  > “The Claude Code build that turns one line into hundreds of verified leads, for zero dollars”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *example-of* `g21-0023`

- `g19-0134` *STATED* — A bonus not in the video is the deliverability cheat sheet for sending to the leads.
  > “The deliverability cheat sheet”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0111`

- `g19-0135` *STATED* — The leads guide ends with 'What This Replaces', 'The math' and Honest Notes.
  > “What This Replaces”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0111`

- `g19-0212` *STATED* — Alex's chen.media guide 'Five Hyped AI Design Tools, Judged the Way a Client Would' (category: Build & sell) ranks the 5 most-hyped AI design tools head-to-head and gives the prompt that makes the winner hand you something real.
  > “Here is the full ranking, plus the prompt that makes the winner hand you something real.”
  — [g-five-hyped-ai-design-tools-judged-the-way-a-client-would](https://chen.media/guides/five-hyped-ai-design-tools-judged-the-way-a-client-would)

- `g19-0220` *STATED* — Alex's chen.media guide 'Build the Voice Line That Answers a Local Shop's Missed Calls' (category: Build & sell) gives the whole build and the exact words to sell it for 300 dollars a month.
  > “the whole build, and the exact words to sell it for 300 dollars a month”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)

- `g19-0238` *STATED* — Alex's chen.media guide 'Find the Complaint, Build the One Feature, Undercut the Price' (category: Build & sell) gives the exact prompts, the subreddits and the pricing math, including the parts of the video that do not work.
  > “Including the parts of the video that do not work, and what to do instead.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)

- `g19-0244` *STATED* — The complaint guide contains copy-paste prompts, the actual subreddit list with each sub's promotion rule, and the pricing arithmetic.
  > “the actual subreddit list with each sub's promotion rule”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0238`
  ↳ *enables* `g19-0254`

- `g19-0272` *STATED* — The complaint guide's Honest Notes list everything that does not work as described plus every claim Alex could not verify to a primary source; read them before you build.
  > “every claim in here I could not verify to a primary source”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0238`
  ↳ *example-of* `g17-0306`

- `g19-0273` *STATED* — The complaint guide's sections: The Exact Prompts, The Subreddits, The Pricing Math, and The Slow Way vs This Way.
  > “The Slow Way vs This Way”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0238`

- `g19-0274` *STATED* — Alex's chen.media guide 'One Idea to a Finished Carousel in a Minute, and the Pitch' (category: Build & sell) gives the workflow that turns one idea into a finished carousel in a minute and the exact pitch that gets a local business to say yes.
  > “The workflow that turns one idea into a finished carousel in a minute”
  — [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch)
  ↳ *example-of* `g21-0022`

- `g20-0054` *STATED* — Alex Chen's chen.media guide 'The Faceless YouTube System: What Works and What It Costs' (category: Build & sell) covers the faceless YouTube system built with Claude, what it really costs, and the one policy that decides whether you get paid at all; it has 3 prompts to copy.
  > “What actually works, what it really costs, and the one policy that decides whether you get paid at all.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)

- `g20-0061` *STATED* — The YouTube monetization policy Alex quotes is at support.google.com/youtube/answer/1311392.
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *evidence-for* `g20-0057`

- `g20-0070` *STATED* — Alex Chen's chen.media guide 'The One Prompt That Makes Claude Design Real Carousels' (category: Build & sell): one prompt saved once, after which every new chat is just your topic and Claude builds the deck in front of you; 3 prompts to copy.
  > “One prompt, saved once. After that, every new chat is just your topic, and Claude builds the deck in front of you.”
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *enables* `g19-0286`

- `g21-0019` *STATED* — Alex's chen.media guide 'Three AI Services a Non-Coder Can Build and Sell' (section: Tools & repos) is powered by sponsor Matchtern and uses funnel keyword SKILLS.
  > “Powered by Matchtern · keyword: SKILLS”
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *part-of* `g21-0243`

- `g21-0027` *STATED* — For each AI service, the guide covers what it is, why people pay, how to build it with Claude, and the line that lands the client.
  — [g-three-ai-services-a-non-coder-can-build-and-sell](https://chen.media/guides/three-ai-services-a-non-coder-can-build-and-sell)
  ↳ *part-of* `g21-0019`

- `g21-0094` *STATED* — Alex's chen.media guide 'The Workflow That Makes Claude Build a Premium Website' (section: Build & sell, dated 2026-07-07) gives a no-code workflow for Claude to build a real premium site: clean layout, smooth animations, perfect on mobile.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)

- `g21-0103` *STATED* — The premium-website guide's locked sections include 'The build prompt', 'Make it premium', 'Put it live' and 'Selling it'.
  — [g-the-workflow-that-makes-claude-build-a-premium-website](https://chen.media/guides/the-workflow-that-makes-claude-build-a-premium-website)
  ↳ *part-of* `g21-0094`

- `g21-0104` *STATED* — Alex's chen.media guide 'The Setup That Makes Claude Design On-Brand Visuals' (section: Build & sell, dated 2026-07-07) sets Claude up to make social posts, ad creatives, thumbnails, one-pagers and pitch slides in your style, in one chat.
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)

- `g21-0116` *STATED* — The on-brand visuals guide's locked sections include 'The asset prompts (copy-paste)', 'Getting the finished image out' and 'Pro tips'.
  — [g-the-setup-that-makes-claude-design-on-brand-visuals](https://chen.media/guides/the-setup-that-makes-claude-design-on-brand-visuals)
  ↳ *part-of* `g21-0104`

- `g21-0170` *STATED* — Alex's chen.media guide 'Four Claude Agents That Get Your Resume Past the Bot' (section: Build & sell) chains four Claude agents (Diagnoser, Recruiter, Rewriter, Hiring Manager) to beat auto-rejection.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)

- `g21-0177` *STATED* — The Diagnoser prompt opens: 'You are an applicant tracking system, not a career coach. Parse the resume below exactly as ATS software would.'
  > “You are an applicant tracking system, not a career coach. Parse the resume below exactly as ATS software would.”
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0176`

- `g21-0189` *STATED* — The resume guide's bonus (not in the video) is 'The screen out cheat sheet', followed by sections 'What This Replaces', 'The math' and 'Honest Notes'.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0170`

- `g22-0081` *STATED* — Alex Chen's chen.media guide 'The $0 Bookkeeping Setup: Folder, Rules and Prompt' (section: Build & sell) gives 3 prompts plus the folder setup and categorization rules.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)

- `g22-0126` *STATED* — Alex Chen's chen.media guide 'Turn Claude Into a Full Brand Studio, Free' (section: Build & sell; comment keyword Brand) is fully free with no locked sections.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *example-of* `g22-0283`

- `g22-0225` *STATED* — Alex Chen's chen.media guide 'Find the Keywords Your Competitor Ranks For and You Do Not' (section: Build & sell) gives 2 prompts for a Claude SEO keyword-gap workflow.
  — [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not)

- `g23-0124` *STATED* — The closet guide ends with a cheat sheet, 'Where to post what'.
  — [g-price-and-list-everything-in-your-closet-in-three-prompts](https://chen.media/guides/price-and-list-everything-in-your-closet-in-three-prompts)
  ↳ *part-of* `g23-0114`

- `g23-0183` *STATED* — The pro-stack guide has a locked section 'The pro loadout (your business AI stack)'.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *part-of* `g23-0173`

- `g23-0184` *STATED* — The pro-stack guide has a locked section 'How to actually turn this into money'.
  — [g-the-pro-ai-stack-what-separates-playing-from-shipping](https://chen.media/guides/the-pro-ai-stack-what-separates-playing-from-shipping)
  ↳ *leads-to* `g23-0175`

- `r01-0038` *STATED* — The full /agency guide is at chen.media/guides/run-an-ai-agency-inside-claude-five-agents.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0024`

- `r01-0118` *STATED* — The /hiring-panel guide is at chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0024`

- `r02-0065` *STATED* — /hunter writes `.hunter/PROFILE.md` under the headings Roles, Not these, Locations, Salary, Dealbreakers, Contact, Start date, Threshold.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0016`

- `r02-0066` *STATED* — /hunter creates `.hunter/applications.md` as a table (date, company, role, score, status, link) whose last line is the credit line.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0016`
  ↳ *enables* `r02-0026`

- `r02-0135` *STATED* — /launch returns `LAUNCH-REPORT.md`: the call (GO for launch, or HOLD), the board, and the fix list.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0118`

- `r02-0235` *STATED* — The /launch run folder keeps the full poll: the mission and every station's report, alongside LAUNCH-REPORT.md.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0135`

- `r03-0172` *STATED* — Harvard College Guide to Creating a Strong Resume (Mignone Center for Career Success): https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0158`

- `r03-0173` *STATED* — LinkedIn Help, Save a profile as a PDF: https://www.linkedin.com/help/linkedin/answer/a541960
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0144`

- `r03-0174` *STATED* — LinkedIn Help, background photo: https://www.linkedin.com/help/linkedin/answer/a568217/add-or-change-the-background-photo-on-your-profile
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0185`

- `r03-0175` *STATED* — LinkedIn Help, photo won't upload (profile photo and background specs): https://www.linkedin.com/help/linkedin/answer/a549049
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0186`

- `r03-0176` *STATED* — LinkedIn Help, profile photo guidelines: https://www.linkedin.com/help/billing/answer/430
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0186`

- `r03-0177` *STATED* — LinkedIn Talent Blog, About section limit: https://www.linkedin.com/business/talent/blog/product-tips/linkedin-profile-summaries-that-we-love-and-how-to-boost-your-own
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0184`

- `r03-0178` *STATED* — LinkedIn Recruiter Help, keyword search: https://www.linkedin.com/help/recruiter/answer/a415295
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0171`
  ↳ *evidence-for* `r03-0229`

### result

- `g01-0047` *CORE* — santifer ran his own job search through career-ops: 740 job posts evaluated, 68 applications, 12 interview processes, 1 offer (Head of Applied AI).
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t)
  ↳ *evidence-for* `g01-0044`
  ↳ *evidence-for* `g01-0061`
  ↳ *evidence-for* `g01-0062`

- `g02-0101` *STATED* — santifer ran his own job search through career-ops: 740 job posts evaluated, 68 applications, 12 interview processes, 1 offer (Head of Applied AI).
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *evidence-for* `g02-0098`
  ↳ *evidence-for* `g02-0097` — selective applying produced interviews and an offer
  ↳ *evidence-for* `g01-0047`

- `g03-0062` *STATED* — santifer ran his own job search through career-ops: 740 job posts evaluated, 68 applications, 12 interview processes, 1 offer (Head of Applied AI).
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *evidence-for* `g03-0059`
  ↳ *evidence-for* `g01-0047`

- `g17-0192` *INFERRED* — The $870 switchable figure equals $1057 minus the six KEEP tools' $187 (Zoom $22 + Google Workspace $22 + Loom $24 + HubSpot $100 + Firefly $10 + CapCut $9); the arithmetic checks out.
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *evidence-for* `g17-0167`
  ↳ *depends-on* `g17-0170`

- `g17-0219` *INFERRED* — The ten paid AI tools in Alex Chen's list total $521 a month at their second paid tier ($135 a month at entry tier), all swappable to free alternatives.
  — [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)
  ↳ *depends-on* `g17-0197`
  ↳ *evidence-for* `g17-0220`

- `g19-0262` *STATED* — Measured on 19 July 2026: monday.com had 23 one-star reviews on Capterra out of 6,073.
  > “monday.com has 23 one star reviews on Capterra out of 6,073”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0263`

- `g19-0263` *STATED* — Word-scanning monday.com's one-star Capterra reviews for 'expensive', 'pricing', 'cost' or 'overpriced' gave zero hits, against 10 hits for bugs, outages and support.
  > “I got zero hits against 10 hits for bugs, outages and support”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *evidence-for* `g19-0261`
  ↳ *evidence-for* `g19-0264`

- `g20-0062` *STATED* — In January 2026 YouTube terminated 16 automated faceless channels holding roughly 35 million subscribers between them: not demonetized, removed.
  > “Not demonetized. Removed.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *evidence-for* `g20-0055`

- `g22-0089` *STATED* — Bookkeeping step 3 output: one clean P&L.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0081`

- `g22-0090` *STATED* — The bookkeeping run also produces a categorized ledger you can export to CSV.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt)
  ↳ *part-of* `g22-0089`

- `r01-0266` *STATED* — In the candle trial both the defense and prosecution rebuttals named point 3 — whether hours or demand limits sales — as the deciding question.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0265`
  ↳ *depends-on* `r01-0254`

- `r01-0270` *STATED* — Candle charges that stuck: gives up the paycheck first with savings worth five months of rent (3 jurors); about 13 sales a month vs about 57 needed (2 jurors); nothing says when to stop (2 jurors).
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0274`
  ↳ *evidence-for* `r01-0168`
  ↳ *contrast* `r01-0136` — both report how many reviewers flagged each problem

- `r01-0271` *STATED* — What the candle defense got right: people paid (40 sales at $28 in spare time), and the plan is unproven, not doomed.
  > “The plan is unproven, not doomed”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0274`
  ↳ *evidence-for* `r01-0268` — unproven, not doomed

- `r01-0272` *STATED* — Candle conditions for acquittal, each answering one juror, to do this week: Statistician — list sales month by month; Parent — ask the employer in writing for an approved leave or promised re-hire; Lawyer — get landlord written consent and product-liability insurance.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0169`
  ↳ *depends-on* `r01-0243`
  ↳ *depends-on* `r01-0246`
  ↳ *depends-on* `r01-0248`

- `r01-0273` *STATED* — The candle sentence: do not hand in your notice yet; keep the paycheck while gathering the three items; before resigning, write down the date and sales level at which you stop; then bring the plan back.
  > “My order: do not hand in your notice yet.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0274`
  ↳ *leads-to* `r01-0236` — bring the plan back

- `r02-0211` *STATED* — CaptionPal's LAUNCH-REPORT.md headline reads `# HOLD: 8 of 8 stations say NO-GO`.
  > “HOLD: 8 of 8 stations say NO-GO”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0153`
  ↳ *example-of* `r02-0157`

- `r02-0216` *STATED* — CaptionPal hold 2 (COST): anyone can call the paid AI without signing in or any limit, running up your bill.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0215`
  ↳ *generalizes* `r02-0246`

- `r02-0217` *STATED* — CaptionPal hold 3 (RECOVERY, DATABASE): the first restart crashes on a migration, with no error log and nothing to roll back to.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0215`
  ↳ *generalizes* `r02-0265`

- `r02-0218` *STATED* — CaptionPal hold 4 (USERS): no sign-in page, no caption form, captions never saved.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0215`
  ↳ *generalizes* `r02-0302`

- `r02-0219` *STATED* — CaptionPal hold 5 (SPEED): "Your captions" reads every caption one by one, and one slow AI reply freezes the site.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0215`
  ↳ *generalizes* `r02-0287`

- `r02-0220` *STATED* — CaptionPal hold 6 (RULES): no privacy policy or terms, and a promised verification email never comes; hold 7 (TESTS): none of this is tested.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0215`
  ↳ *generalizes* `r02-0272`
  ↳ *generalizes* `r02-0295`

- `r02-0237` *STATED* — CaptionPal's /admin/users route has no sign-in check: a local GET with no cookie returned 200 with every user's id, email and unsalted MD5 password hash (server.py:43-45, db.py:53-54); SECURITY, DATABASE, RULES, TESTS and USERS all flagged it.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0215`
  ↳ *evidence-for* `r02-0279`
  ↳ *evidence-for* `r02-0258`
  ↳ *evidence-for* `r02-0242`

- `r02-0238` *STATED* — CaptionPal's session cookie is just the email address (server.py:30, 57): the probe `Cookie: session=victim@x.com` showed the victim's private captions.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0279`
  ↳ *evidence-for* `r02-0258`
  ↳ *evidence-for* `r02-0242`

- `r02-0239` *STATED* — CaptionPal's db.migrate() re-runs every migration on each start without tracking which ran, so on a scratch database the second start failed with `OperationalError no such column: "bio"` and any restart, deploy or reboot leaves the site down; DATABASE, RECOVERY, TESTS and USERS all caught it.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0265`
  ↳ *evidence-for* `r02-0258`
  ↳ *evidence-for* `r02-0298`
  ↳ *evidence-for* `r02-0242`

- `r02-0240` *STATED* — CaptionPal's db.save_caption is called only by tests/test_app.py:23 and never by /api/captions, so "Your captions" stays empty despite the mission's promise; COST, DATABASE, RULES, TESTS and USERS all reported it.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0302`
  ↳ *evidence-for* `r02-0297`
  ↳ *leads-to* `r02-0254`
  ↳ *evidence-for* `r02-0242`

- `r02-0241` *STATED* — CaptionPal's AI calls have no timeout (`urlopen(req)`, default socket timeout None), make 3 calls in a row per request, and run on the single-threaded `HTTPServer`, so a slow provider freezes the site for every user; SPEED and RECOVERY both flagged it.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0287`
  ↳ *evidence-for* `r02-0265`
  ↳ *evidence-for* `r02-0242`

- `r02-0246` *STATED* — CaptionPal COST station NO-GO: anyone on the internet, signed in or not, can make the app call the paid AI as often as they like, so a stranger could run up the owner's bill with no limit.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0128`

- `r02-0247` *STATED* — COST finding: `/api/captions` calls the paid AI with no sign-in check, no rate limit and no cap (app/server.py:61-62 never calls `self.user()`).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0246`

- `r02-0248` *STATED* — COST finding: `FREE_CAPTIONS_PER_DAY = 20` (app/config.py:6) is never used anywhere; grep finds only its definition.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0246`
  ↳ *leads-to* `r02-0224`

- `r02-0250` *STATED* — COST finding: `Access-Control-Allow-Origin: *` on every response (app/server.py:20) lets any other website make its visitors' browsers call `/api/captions` too.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0246`
  ↳ *contrast* `r02-0281` — same CORS * finding from two stations

- `r02-0254` *STATED* — COST watch: because captions are never saved, users have to pay again to see them.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0246`

- `r02-0256` *STATED* — COST checked: the only paid outbound call is app/ai.py:17; there are no email, SMS, maps or storage services, SQLite costs nothing, the VPS price was not given, and tests pass (2/2).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0246`

- `r02-0258` *STATED* — CaptionPal DATABASE station NO-GO: anyone can download every user's email and scrambled password, open another user's saved captions, and the app cannot start again after a restart.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0126`

- `r02-0259` *STATED* — DATABASE finding: find_user pastes the email into SQL (db.py:30), and on a scratch database a UNION login signed in as user 1 and listed user 1's caption.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0258`
  ↳ *evidence-for* `r02-0280` — DATABASE reproduces SECURITY's injection

- `r02-0260` *STATED* — DATABASE watch: there is no backup or restore anywhere, and the whole database is one SQLite file at a relative path (config.py:3), so starting from another folder opens an empty database.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0258`

- `r02-0262` *STATED* — DATABASE watch: no indexes exist, captions_for loads every caption one query each (db.py:46-48), and users.email is not UNIQUE, so a second signup with the same email was accepted.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0258`
  ↳ *evidence-for* `r02-0288`

- `r02-0263` *STATED* — DATABASE checked: no seed or reset scripts, tests use a temp database (tests/test_app.py:10-12) and pass, and captions_for does filter by owner.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0258`

- `r02-0265` *STATED* — CaptionPal RECOVERY station NO-GO: the site will not start a second time, needs a setting nobody wrote down, records no errors anywhere, and has no saved earlier version to go back to.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0130`

- `r02-0266` *STATED* — RECOVERY finding: `BILLING_ACCOUNT` is read at app/ai.py:15 but documented nowhere (no README mention, no .env.example or host config), so if unset every caption request raises KeyError and the user gets a dropped connection.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0265`
  ↳ *evidence-for* `r02-0304` — unset BILLING_ACCOUNT is the KeyError USERS hit

- `r02-0267` *STATED* — RECOVERY finding: no logging, error tracker, alerts or health check (grep for logging/sentry/health finds nothing); only http.server's stderr tracebacks.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0265`

- `r02-0268` *STATED* — RECOVERY finding: nothing to roll back to: the folder is not under version control (`git log`: "fatal: not a git repository"), with no tagged release and no feature flags.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0265`

- `r02-0269` *STATED* — RECOVERY watch: sessions live in memory (server.py:9) so each restart logs everyone out, and settings are hardcoded in app/config.py, not read from the environment.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0265`

- `r02-0270` *STATED* — RECOVERY checked: tests pass (2 tests, OK) and all three migrations apply once on a fresh database (SQLite 3.54.0).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0265`
  ↳ *contrast* `r02-0239` — migrations apply once, fail twice

- `r02-0272` *STATED* — CaptionPal RULES station NO-GO: people will hand over their email and password with no privacy policy or terms anywhere, and the app promises a verification email it never sends.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0131`

- `r02-0273` *STATED* — RULES finding: sign-up collects email and password and every photo description goes to an outside AI company, but `grep -rniE "privacy|terms|policy" app` finds nothing, leaving the owner with the legal risk (GDPR/CCPA) for about 1,000 creators.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0272`
  ↳ *depends-on* `r02-0206`

- `r02-0274` *STATED* — RULES finding: after sign-up the app says "Check your inbox to verify your email." (app/server.py:53) but no code sends email (`grep -rniE "smtp|mail"`), so every new user waits for an email that never comes.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0272`
  ↳ *example-of* `r02-0131` — promise the code doesn't keep

- `r02-0275` *STATED* — RULES watch: there is no way to delete an account or its captions: no delete route in server.py and no delete function in db.py.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0272`

- `r02-0276` *STATED* — RULES watch: "Your photos are never stored" holds (no photo is uploaded), but the description is sent to the AI provider, so the privacy policy should say so.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0272`
  ↳ *qualifies* `r02-0205` — landing-page promise checked against code

- `r02-0277` *STATED* — RULES checked: no payments, no marketing emails so no unsubscribe needed, no analytics or tracking cookies so no consent banner, and standard library only so no licence conflicts.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0272`

- `r02-0279` *STATED* — CaptionPal SECURITY station NO-GO: anyone on the internet can download every user's email and password fingerprint, log in as any user without their password, and read their saved captions.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0125`

- `r02-0280` *STATED* — SECURITY finding: SQL injection in login, because find_user puts the typed email into the query with an f-string (app/db.py:30); the email `nobody' UNION SELECT 1,'z','<md5>' --` logged in as user 1.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0279`
  ↳ *example-of* `r02-0244`

- `r02-0281` *STATED* — SECURITY finding: /api/captions needs no sign-in and has no limit, and every response sends CORS `*` (server.py:20, 61-63), so any visitor or website can spend the owner's AI bill.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0246` — SECURITY and COST both flag the open paid endpoint
  ↳ *evidence-for* `r02-0279`

- `r02-0284` *STATED* — SECURITY watch: /captions without a cookie crashes (TypeError), login never sends Set-Cookie, captions are printed unescaped (stored XSS once save_caption is wired in), email is not UNIQUE, and DEBUG = True.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0279`

- `r02-0285` *STATED* — SECURITY checked: no shell commands, user-controlled file paths, .env files, private keys or public env vars, and no dependency audit applies (standard library only); HTTPS was unverifiable because the server speaks plain HTTP on port 8000.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0279`
  ↳ *evidence-for* `r02-0245`

- `r02-0287` *STATED* — CaptionPal SPEED station NO-GO: "Your captions" reads every caption from every user one at a time, slowing with every caption anyone saves, and one stuck AI request can freeze the whole site.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0127`

- `r02-0288` *STATED* — SPEED finding: an N+1 query with no limit in `captions_for` (app/db.py:43-50) selects every caption id in the table, runs one query per id and filters by user in Python.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0287`

- `r02-0291` *STATED* — SPEED watch: captions.user_id has no index, /admin/users returns every user with no limit, and every DB call opens a new connection and never closes it (db.py:7-10).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0288`

- `r02-0293` *STATED* — SPEED checked: no JavaScript, images or build step, and the landing page is 170 bytes.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0287`

- `r02-0296` *STATED* — TESTS finding: no test touches app/server.py or app/ai.py; on a throwaway copy /login sent no cookie, a hand-typed `session=a@b.com` cookie opened that person's captions, and /captions without one crashed with TypeError.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0295`
  ↳ *evidence-for* `r02-0238`

- `r02-0298` *STATED* — TESTS finding: migrations are tested only on a fresh database (test_app.py:10-12), so the restart failure on an existing database went untested.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0295`

- `r02-0299` *STATED* — TESTS watch: the paid AI call, the 20-a-day limit, the SQL built from the email, and the non-UNIQUE email (a@b.com stored twice in a probe) have no tests.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0295`

- `r02-0300` *STATED* — TESTS checked: `python3 -m unittest discover -s tests` gives "Ran 2 tests in 0.013s OK" (Python 3.9.6), with no type check, lint or build and no skipped, commented-out or empty tests or snapshots.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0295`
  ↳ *contrast* `r02-0295` — 2 OK yet NO-GO

- `r02-0302` *STATED* — CaptionPal USERS station NO-GO: a new user can sign up but cannot sign in, has no button that writes captions, and never gets captions saved, so the app's main promise does not work.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0129`

- `r02-0303` *STATED* — USERS finding: sign-in is unreachable: GET /login returns 404 and only POST /login exists (app/server.py:54), which sends no Set-Cookie, so nobody is ever signed in.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0302`
  ↳ *evidence-for* `r02-0284` — no Set-Cookie seen by both

- `r02-0304` *STATED* — USERS finding: the core action has no page: nothing links or posts to /api/captions, and when called it crashed on KeyError 'BILLING_ACCOUNT' (app/ai.py:15), dropping the connection.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0302`

- `r02-0305` *STATED* — USERS finding: "Your captions" (server.py:42) is always blank with no empty-state text, and crashes without a session.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0302`
  ↳ *depends-on* `r02-0240`

- `r02-0306` *STATED* — USERS watch: sign-up promises verification but there is no verify or sign-out route (both 404), and no form validation: a blank password drops the connection (KeyError; parse_qs drops blanks) and the same email registers twice.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0274`
  ↳ *qualifies* `r02-0302`

- `r02-0307` *STATED* — USERS checked: landing and sign-up pages load, sign-up stores the user, a wrong password gets a clear 401 message, and there is no payment step, as the mission says.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0302`

- `r04-0226` *STATED* — In the real 2-investor example session, 'A subscription box of hot sauces from small local makers, $35 a month' got no deal from either shark, and six pieces of homework.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0215`
  ↳ *example-of* `g09-0254`
  ↳ *example-of* `r04-0206`

- `y01-0101` *STATED* — From the marketing department alone you go from basically nothing to website copy, emails, ads and the first 30 days of content for a business.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)

- `y02-0073` *STATED* — The boardroom gives you a professional report you can paste into Claude.
  — [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs)
  ↳ *example-of* `g09-0254`
  ↳ *part-of* `y02-0069`
  ↳ *leads-to* `y02-0074`

- `y02-0153` *STATED* — MiroFish lets you see who loves it, who ignores it, and why — before launch.
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *evidence-for* `g09-0204`
  ↳ *part-of* `y02-0148`

- `y02-0184` *STATED* — The Shark panel means you find out what investors hate about your idea before you pitch a real one.
  — [O-ngH7V3_U0](https://youtu.be/O-ngH7V3_U0)
  ↳ *example-of* `g09-0254`
  ↳ *evidence-for* `r04-0206`
  ↳ *part-of* `y02-0179`

### style

- `g02-0234` *INFERRED* — chen.media guides give away the lede, the first section and the full table of contents, and gate the rest (install steps, catches, prompts) behind an email signup.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill) [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode) [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read) [g-run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl](https://chen.media/guides/run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl) [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive) [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi) [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code) [g-run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr](https://chen.media/guides/run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr) [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude) [g-have-claude-build-an-award-level-website-from-one-line](https://chen.media/guides/have-claude-build-an-award-level-website-from-one-line) [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google) [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say) [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code) [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background) [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit) [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video) [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *part-of* `g02-0232`

- `g02-0242` *INFERRED* — Alex republishes the same guide body under different hook headlines: AirLLM as '235 billion parameters on a 3GB card' and '2.8 trillion parameters on your gaming card'; career-ops as 'know if a job is worth applying' and '200 applications, zero replies?'.
  — [g-run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl](https://chen.media/guides/run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl) [g-run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr](https://chen.media/guides/run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr) [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *qualifies* `g02-0232`

- `g12-0301` *CORE* — A recurring Alex Chen angle is a free or open-source tool priced against a paid incumbent: SEO agencies charging hundreds to thousands, OpusClip Pro at $29/month, NVIDIA's models for $0, Polsia free with no credit card.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments) [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code) [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative) [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business) [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *generalizes* `g12-0130`
  ↳ *generalizes* `g12-0187`
  ↳ *generalizes* `g12-0290`
  ↳ *generalizes* `g12-0273`
  ↳ *generalizes* `g12-0051`

- `g22-0217` *STATED* — Claude Wrapped section 'Post yours' invites sharing the result.
  — [g-build-your-own-claude-wrapped-from-your-real-stats](https://chen.media/guides/build-your-own-claude-wrapped-from-your-real-stats)
  ↳ *part-of* `g22-0211`

- `g22-0276` *CORE* — Alex Chen frames each Claude workflow against the price of the human service it replaces: a bookkeeper at a few hundred a month, an SEO agency at $3,000 a month, a $4,000 brand agency, a $10k design, a lawyer.
  — [g-the-0-bookkeeping-setup-folder-rules-and-prompt](https://chen.media/guides/the-0-bookkeeping-setup-folder-rules-and-prompt) [g-find-the-keywords-your-competitor-ranks-for-and-you-do-not](https://chen.media/guides/find-the-keywords-your-competitor-ranks-for-and-you-do-not) [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free) [g-five-claude-skills-that-feel-like-cheating](https://chen.media/guides/five-claude-skills-that-feel-like-cheating)
  ↳ *evidence-for* `g12-0301`

### warning

- `g02-0084` *STATED* — GoLive asks for your approval: nothing is written to a real account without a plan you have seen and approved.
  > “Nothing is written to a real account without a plan you have seen and approved.”
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *leads-to* `g02-0085`
  ↳ *evidence-for* `g02-0082`
  ↳ *example-of* `g02-0237`
  ↳ *evidence-for* `g12-0303`

- `g02-0110` *STATED* — career-ops never sends the LinkedIn note it drafts.
  > “It never sends it.”
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *qualifies* `g02-0109`
  ↳ *example-of* `g02-0237`
  ↳ *evidence-for* `g01-0055`

- `g13-0197` *STATED* — Alex frames HackingTool strictly as a way to check your own apps before launch.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *qualifies* `g13-0190`
  ↳ *evidence-for* `r02-0118`

- `g13-0211` *STATED* — Check your Runable account before generating several video variants; a free starting plan is not unlimited production.
  > “a free starting plan is not unlimited production”
  — [g-runable-headphone-brand-launch-guide](https://chen.media/guides/runable-headphone-brand-launch-guide)
  ↳ *qualifies* `g13-0208`
  ↳ *evidence-for* `g17-0194`
  ↳ *qualifies* `y03-0163` — a free starting plan is not unlimited production
  ↳ *qualifies* `y04-0037` — 'a whole brand in minutes' is bounded by credits

- `g17-0191` *STATED* — Read Alex Chen's honest notes before you cancel any paid business tool.
  > “Before you cancel anything”
  — [g-15-more-free-swaps-hosting-crm-and-storefronts](https://chen.media/guides/15-more-free-swaps-hosting-crm-and-storefronts)
  ↳ *qualifies* `g17-0171`
  ↳ *example-of* `g17-0306`

- `g17-0301` *STATED* — career-ops comes with one rule that is not optional.
  > “One rule, and it is not optional”
  — [g-the-setup-that-reads-every-job-posting-and-flags-the-fake-ones](https://chen.media/guides/the-setup-that-reads-every-job-posting-and-flags-the-fake-ones)
  ↳ *qualifies* `g17-0295`

- `g18-0265` *STATED* — Read the licence before you build a business on an open source repo.
  > “Read the licence before you build a business on one of these.”
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *qualifies* `g18-0262`
  ↳ *example-of* `g18-0288`

- `g19-0051` *INFERRED* — A service that charges a fee to search for or claim unclaimed money is not one of the six official sites in Alex's sweep.
  — [g-the-six-site-sweep-for-money-you-are-already-owed](https://chen.media/guides/the-six-site-sweep-for-money-you-are-already-owed)
  ↳ *leads-to* `g19-0050`

- `g19-0128` *CORE* — The Target prompt restricts Claude to publicly available sources and has it flag any source whose terms forbid scraping so you skip it.
  > “Use only publicly available sources. If a source's terms forbid scraping, flag it so I skip it.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *part-of* `g19-0121`
  ↳ *qualifies* `g19-0129`

- `g19-0236` *CORE* — The one rule you never break with an AI voice line: have it say it is an assistant, not pretend to be a person.
  > “Have it say it is an assistant”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0220`
  ↳ *qualifies* `g19-0231`

- `g19-0237` *STATED* — An AI voice line must hand real emergencies to a human.
  > “hand real emergencies to a human”
  — [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls)
  ↳ *part-of* `g19-0236`

- `g19-0267` *CORE* — Before publishing any price comparison, quote or competitor number in public, open the competitor's own pricing page yourself, screenshot it and date the screenshot.
  > “open the competitor's own pricing page yourself, screenshot it, and date the screenshot”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *because* `g19-0270`
  ↳ *qualifies* `g19-0242` — undercut claims must be verified
  ↳ *evidence-for* `g17-0314`

- `g19-0270` *STATED* — An inaccurate public claim about a competitor's price is litigable, not just rude.
  > “an inaccurate claim about a competitor's price is litigable and not just rude”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *evidence-for* `g19-0271`

- `g20-0055` *CORE* — YouTube does not pay for content that reads as mass-produced.
  > “YouTube does not pay for content that reads as mass-produced.”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`

- `g20-0064` *STATED* — Be careful which niche you automate on a faceless YouTube channel.
  > “Be careful which niche you automate”
  — [g-the-faceless-youtube-system-what-works-and-what-it-costs](https://chen.media/guides/the-faceless-youtube-system-what-works-and-what-it-costs)
  ↳ *part-of* `g20-0054`

- `r01-0062` *STATED* — Cold email has rules: CAN-SPAM in the US, GDPR in Europe.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *because* `r01-0063`
  ↳ *leads-to* `r01-0064`
  ↳ *qualifies* `g04-0033` — cold email must follow CAN-SPAM / GDPR

- `r01-0101` *STATED* — /agency never uses the client's real passwords or keys: it leaves placeholders and lists what to fill in.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0099`

- `r01-0289` *STATED* — /agency applies the email law of where the user's leads are (for example CAN-SPAM, GDPR), not just where the user is.
  > “Respect email law where the user's leads are”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0062`
  ↳ *part-of* `r01-0043`

- `r02-0027` *STATED* — /hunter never creates accounts, never types passwords and never gets past a CAPTCHA.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0025`
  ↳ *evidence-for* `r01-0101`

- `r02-0053` *STATED* — /hunter never submits an application through any channel: not through a form, a browser tool or an email.
  > “You never submit an application. Not through a form, a browser tool or an email.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *generalizes* `r02-0027`
  ↳ *evidence-for* `r02-0312`
  ↳ *example-of* `g02-0237`

- `r02-0098` *STATED* — Answers that stay `YOU` and are never guessed by /hunter: work authorization and sponsorship, salary if the profile has none, disability, veteran, gender, race and any other self-identification, criminal record, references, anything legal, or a signature.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0028`

- `r02-0112` *STATED* — /hunter rule: never submit, send, post, pay for or sign anything, and never contact a company or a person for the user.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *generalizes* `r02-0053`
  ↳ *example-of* `g02-0237`

- `r02-0255` *STATED* — COST watch: a live-looking AI key hard-coded in app/config.py:5 means anyone with the code can spend on the account.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0283` — COST reads key as live-looking; SECURITY notes it is commented fake

- `r03-0224` *STATED* — No mood words like 'passionate' or 'driven' in the headline; facts from the profile only.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0222`

- `r03-0228` *STATED* — Use each keyword in a real sentence about real work, once or twice at most: no keyword lists, no stuffing.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0227`
  ↳ *qualifies* `g23-0170` — hit every keyword, but each once or twice in a real sentence: no keyword lists, no stuffing

- `r03-0248` *STATED* — The banner has no logos, no photos, no faces and no invented claims.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0245`

- `y02-0085` *INFERRED* — Selling a 'perfect copycat' of a commercial app carries trademark, copyright and terms-of-service risk; the safer use of the rebuild pipeline is cloning functionality for personal use or building a differentiated competitor.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *qualifies* `g08-0262` — selling a perfect copycat carries trademark/copyright/ToS risk
  ↳ *qualifies* `y02-0084`

<!-- AUTO:atoms END -->
