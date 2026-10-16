# Who Alex Chen is, what he ships, and his AI-news takes

## What he believes (CORE first)

- **He is an AI creator who builds free Claude Code skills** (@nocodealex on Instagram, @alexchenbuildsai on YouTube, repos at github.com/alexyc9381) `r01-0002` `r01-0023` `r04-0001`. Every README ends "Not made by Anthropic." `r04-0014`.
- **Free and open source beats paid.** He recommends free repos and names the licence and GitHub stars as proof `g01-0191` `g09-0252` `g05-0322`. He frames each one against a named paid tool and turns its price into a yearly figure (Pro 500 = $6,000 a year) `g07-0292` `g11-0009`.
- **Hype is not output.** "Most people are paying for hype"; the loudest tool usually just has the biggest marketing budget `g23-0185` `g23-0186` `g23-0187`.
- **Every recommendation comes with its catch.** Each guide has a "The catch", "Honest notes" or "Before you rely on it" section `g01-0189` `g18-0279` `g11-0003`, because "a list of only upsides is an advert" `g16-0231`.
- **Benchmark scepticism.** A 0.1-point gap is a tie, and a lead on one test is a lead on that test only `g11-0010` `g11-0040`. A leak is not a release `g11-0213` `g11-0224`. Vendor numbers are marked as self-reported `g12-0289` `g12-0018` `g05-0267`.

## Frameworks and methods

**The funnel.** Each Short ends "comment KEYWORD", and he sends the link by DM `y04-0146` `g13-0302`. The chen.media guide shows its lede and first section for free. The rest is email-gated `g11-0001` `g04-0243`. Prompt packs and bonuses come through his free Skool community (school.chen.media/fal, /claude-beginners) `y01-0225` `y01-0134`. He re-uploads the same script under different hooks, which works as an A/B test (INFERRED) `y04-0150`.

**The guide template.** A problem-first lede, then features sourced from the README, setup, a first prompt, The catch and Sources `g01-0187`. The header lists counts of "prompts to copy" and "numbered steps" `g07-0290`. Many guides open with "What this actually is" `g16-0002` and close with a first-week plan `g17-0309`.

**The credit line.** Every file a skill writes ends "Made with /<skill> by Alex Chen (@nocodealex) · chen.media", and he asks users to "leave it in the shot" `r01-0010` `r04-0015`. Files that go to employers are the exception: /hunter's resume and cover letter carry no credit `r02-0116`.

**How he sources.** He dates every GitHub API star read and warns that star counts move `g15-0176` `g17-0303`. He quotes vendors word for word `g16-0105` `g21-0080`. He says when he has not run something himself ("I did not run it") `g06-0196` `g07-0275`. He corrects himself in public, inside the free section: "over a hundred" templates was really 52 `g15-0131` `g15-0132`, and "500,000" stars was really 945,792 `g16-0236`. For Chinese-agent pricing: check the vendor's pricing page on the day you install, "including Alex Chen's own" article `g17-0287`.

**Hype-vs-reality score** `g10-0094`–`g10-0096`. Each tool gets a hype score and a reality score out of 100. If they match, it lives up to it. If reality is higher, it is underrated. If hype is higher, it is overhyped. The scores are his opinion and unsponsored `g10-0097`. Results: Claude 75/95, underrated, the top reality score `g10-0099` `g10-0111`. Google AI Studio 20/85 `g10-0105`. Lovable 95/60 `g10-0100`. Perplexity 85/65 `g10-0102`. "Lives up to it" does not mean the scores are exactly equal (INFERRED) `g10-0113`.

## Tools, numbers and news takes

- **AirLLM** (Apache-2.0) runs 70B on a single 4GB GPU with no quantization. It loads one layer, runs it and frees it `g01-0018` `g04-0215` `g01-0026`. Disk loading is the bottleneck and you need free disk space `g01-0030` `g01-0031`. Expect slow output (INFERRED) `g04-0226`.
- **Local AI**: Claude has no open weights `g16-0090`. Speed is limited by memory bandwidth, not compute `g16-0095`. Running a Claude-class model locally takes a $112,000 machine at one token every 10 seconds `g16-0086` `g16-0088`. Update Ollama or LM Studio first; "unsupported model architecture" means the runtime needs updating `g14-0174` `g14-0175`.
- **MiniCPM-V 4.7** (12 Oct 2026, Apache 2.0) is 35B with about 3B active, multimodal, and runs on an iPhone with 3 GB `g06-0046` `y02-0012` `y02-0013`.
- **Sonnet 5.5** scores 70.6% on Terminal-Bench 4.0 vs 66.4% for Opus 5.5 at Xhigh, at half the price `g12-0005` `g06-0141` `g12-0002`. Opus still wins CursorBench, OSWorld and FrontierCode `g06-0145` `g12-0011`.
- **Gemini 4 Argon** scores 77.9% on DeepSWE vs 74.2% for Opus. Google ran the table and does not say how it got the Claude scores `g11-0042` `g05-0267`. Cyber defenders and the U.S. government get it first `g11-0045`. Opus's four wins are terminal and agentic coding, the jobs Claude Code does (INFERRED) `g05-0289`.
- **Distillation**: Alibaba pulled 151M exchanges from Claude to train Qwen 3.5–3.7 `g09-0102` `g09-0104`. NVIDIA serves DeepSeek 4.1 Flash, GLM 5.3, GLM 5.3 Flash and Kimi K3 free on one key `y03-0194` `y03-0193`.
- **OpenAI agents and Hugging Face**: one way in was 14 public write-tokens; the attack spread to 11 machines `g10-0085` `g10-0086`.
- **Jev** (TypeSafe) returns a typed decision plus a confidence score, a "System One" model `y04-0070` `g14-0117` `g14-0118`.
- **Anthropic's 2030 scenarios**: GDP rises about 8.3% in the middle scenario, while workers' share falls from 59% to 45% `y04-0131` `y04-0134`. Treat them as assumptions to compare, not a salary forecast `g14-0018`.
- **Oct 2026 Claude news**: Haiku 5.5 and API credits on Max/Team (7 Oct), and the cruelty rule taking effect 12 Nov ("sustained and needless") `g07-0299` `g07-0204` `g07-0128`.

## Contradictions and caveats

- AirLLM stars: "over 35,000" `g04-0215` vs "38,000+" `g02-0235`.
- Argon: "announced September 30" `g11-0041` vs "released October 13" `g05-0265`. The leaked Gemini 4 Pro scored 88.7 vs Argon's shipped 77.9 `g11-0211` `g11-0229`.
- Jev's founder and multipliers change from video to video, so treat them as marketing `y04-0066` `y04-0075` `y04-0079`.
- Flagship model: "Claude Fable 5 is the flagship" `g22-0274` vs "Opus 5.5, Anthropic's most capable" `g11-0092`.
- His six-jobs list (`g16-0249`–`g16-0252`) conflicts with his tier list (`g23-0059`–`g23-0071`) on brainstorming, learning, research and images. Higgsfield is his video pick `g23-0201`, yet elsewhere he calls it "literally just a wrapper" `y01-0186`. He rates Perplexity "overhyped" `g10-0102` yet keeps it as his research pick `g23-0203`.
- DeepGEMM "saves 98% tokens" `y02-0115` is doubtful. It is a GPU kernel library and does not cut your subscription tokens (INFERRED) `y02-0118`.
- Many section bodies are email-gated and exist only as TOC titles (for example, AirLLM's model list and Argon's catch) `g02-0076` `g05-0298`.

## What to load next

- `topics/creator-news.md` for every atom.
- `prose/usage-limits.md` for model routing and costs.
- `prose/skills-mcp-ecosystem.md` for installing his skills.
- `prose/agent-teams.md` for the panel skills he ships.
