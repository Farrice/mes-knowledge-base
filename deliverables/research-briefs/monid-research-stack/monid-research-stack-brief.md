# the stack that gives claude hands

> RESEARCH BRIEF · PILOT 001 · window: aug 5, 2026 · single-day · lens: research infra · content zeitgeist · sources: 1 video (37 frames) + 4 web + 2 local trackers · compiled: aug 5, 2026

What we verified about Monid AI, our own Apify usage, and the research-to-brief workflow from Eddy Ballesteros's demo — and what we decided to wire. This pilot brief is itself the first artifact of the system it describes.

## the big picture
_WHAT'S FORMING_
Research is moving from 'read what the model remembers' to 'render what the tools just fetched.' Eddy Ballesteros's workflow closes the loop on screen: one sentence in, live data pulled through Monid's pay-per-call router, and a designed decision-document out — for three cents. Our system already has the governance layer (budget trackers, cost gate) and the missing piece was exactly this consumption layer: briefs you can scan, verify, and deploy from.

## what we verified
- **monid is a pay-per-call tool router — one wallet, agent discovers and pays per tool** [VERIFIED] — Demonstrated live: Claude discovers tools, pulls Semrush/Reddit/X/YouTube, renders report. Homepage claims 'Live · 1500+ tools'; script doc says 13+ providers, calls from ~a tenth of a cent. (https://monid.ai/)
- **a full research report cost him $0.03** [VERIFIED] — Cost shown on screen with the tool stack that produced it (Semrush keyword metrics, Reddit top posts + community sizes, X, YouTube last-30-days). (https://www.youtube.com/watch?v=PmvqIaLC6AY)
- **our apify plan is 98% unused this month** [VERIFIED] — $0.59 of $29.00 spent as of today (29 runs). The scraping capacity Farrice wants largely already exists and sits idle. (.agent/apify-usage.json · 2026-08)
- **we have zero linkedin scraping coverage** [VERIFIED] — No LinkedIn actor in apify_client.py ACTORS (17 registered: Reddit, IG, TikTok, YouTube, Amazon, Maps, web, Scrape Creators). LinkedIn is the primary content platform in the current campaign. (execution/apify_client.py ACTORS)
- **monid's catalog covers linkedin, x, tiktok, instagram, amazon, google reviews** [LIKELY] — Listed in Monid's public catalog descriptions. Not yet exercised by us — needs a funded wallet and one smoke call per endpoint before we rely on it. (https://moge.ai/product/monid)
- **ai search converts at 10–40% vs 1–2% for traditional seo** [UNCONFIRMED] — Claim by Greg Eisenberg surfaced in Eddy's report; Eddy himself flags it for fact-checking on camera. Included here as a live example of an UNCONFIRMED chip doing its job. (https://www.youtube.com/watch?v=PmvqIaLC6AY)

## where our apify runs actually went
- reddit: 15 (15 runs — the workhorse)
- youtube: 6 (6 runs)
- tiktok (sc): 6 (6 runs across sc-tiktok + hashtag)
- instagram + web: 2 (2 runs)
- linkedin: 0 (0 runs — no actor exists)
_same scale · runs this month by actor · reddit dominates, linkedin impossible_

## what we're wiring, in order
decisions locked with farrice on aug 5 — each line carries the number that justifies it.
1. **wire monid on all three surfaces, hard-capped** — Claude Code + Codex via config, claude.ai via connector card. $1 free credit covers smoke tests; cost gate denies unknown services by default, so registration is deliberate. $5/run default cap ≈ 150+ reports at Eddy's demonstrated $0.03.
2. **expand apify actors — linkedin first** — 98% of the $29/mo plan is unused and the priority platform has zero coverage. Verify actor pricing and maintenance on the store before registering; smoke-test under $0.25 total.
3. **render every research run as a brief on the asset board** — Markdown blobs are the stated failure ('gets a little wearing on me'). This document is the template proving the alternative: trust header, sourced claims, ranked decisions, one CTA.
4. **keep $25 runs as deliberate deep-dives only** — A $25 default cap exceeds the entire $29/mo Apify budget in two runs. Above $5, the existing 15-minute approval token is the unlock — friction exactly where spend gets real.

## deploy blocks
**one-sentence research prompt (adapted from eddy, t=04:54)**
```
Using Monid, research [TOPIC] in depth. Identify the tools available for this research — Reddit, subreddits, X, web search, and any social platforms that make sense — pull the live data, and render the result as a research brief JSON per templates/research-brief/ (trust header, sourced evidence rows with VERIFIED/LIKELY/UNCONFIRMED confidence, ranked decision section, source ledger), then run: python3 execution/render_brief.py <brief.json> --open
```
**claude.ai connector setup (2 minutes)**
```
1. claude.ai → Settings → Connectors → Add custom connector
2. Name: Monid — URL: https://mcp.monid.ai/v1 → Add
3. Log in / authorize when prompted (new accounts get $1 free credit)
4. Test: "Find the latest posts about AI consulting for supplement brands using Monid MCP"
```
**render this brief**
```
python3 execution/render_brief.py deliverables/research-briefs/monid-research-stack/monid-research-stack-brief.json --open
```

## what this isn't
_CAVEATS WORTH KEEPING_
This is a single-day snapshot built from one creator's demo plus our local trackers. The Apify numbers and the missing-LinkedIn fact are ours and fully reliable. Monid's costs are Eddy's receipts from one report on one day — treat the $0.03 as an order of magnitude, not a quote. The catalog-coverage claim is the vendor's own copy and stays LIKELY until we run one paid call per endpoint we care about. Nothing here has revenue attached yet; the decision section is infrastructure, not income.

## Source ledger
1. Eddy Ballesteros — I Connected Claude to Monid AI (video, watched via /watch, 37 frames) — https://www.youtube.com/watch?v=PmvqIaLC6AY (retrieved 2026-08-05, VERIFIED; used for: workflow, brief anatomy, cost receipts, connector steps)
2. monid.ai homepage — https://monid.ai/ (retrieved 2026-08-05, VERIFIED; used for: router mechanics, 1500+ tools claim, SKILL.md setup path)
3. Monid docs — https://docs.monid.ai/ (retrieved 2026-08-05, VERIFIED; used for: skill quickstart existence)
4. MOGE product listing — Monid — https://moge.ai/product/monid (retrieved 2026-08-05, LIKELY; used for: catalog platform coverage (LinkedIn, X, TikTok, IG, Amazon))
5. .agent/apify-usage.json (local tracker) (retrieved 2026-08-05, VERIFIED; used for: spend $0.59/$29.00, 29 runs, per-actor counts)
6. execution/apify_client.py ACTORS registry (local) (retrieved 2026-08-05, VERIFIED; used for: 17 registered actors, no LinkedIn coverage)

## Context pack (agent feed)
- https://monid.ai/ — monid.ai + video t=01:52–06:24
- https://www.youtube.com/watch?v=PmvqIaLC6AY — video t=06:04
- https://moge.ai/product/monid — moge.ai listing + monid docs
- https://docs.monid.ai/ — Monid docs

_run cost $0.00 — stack: /watch frames · yt-dlp captions · web search · local trackers_
