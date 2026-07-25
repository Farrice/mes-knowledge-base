---
date: 2026-07-25
session: riley-brown-os
tier: operator-guide
status: enriched
---

# Riley Brown OS — What We Built 2026-07-25 and How to Use It

> One session turned Riley Brown's video "Codex Is Basically Running My Company Now" into two assets: a forge-grade expert skill (`/riley-brown`, composite 8.33, blind pass EVAL-055) and a live replication of his ~$175-250/mo paid tool stack at $0 on infrastructure we already own — scrape-any-creator→Notion, Foreplay-free ad-spy, creative/brand/inbox/scheduling workflows. Companions: `skills/riley-brown-marketing-automation/SKILL.md` (skill manual), `docs/solutions/2026-07-24-replicate-creator-tool-stack-at-zero-cost.md` (the banked rule), `.agent/handoffs/2026-07-25-riley-brown-os.md` (thread state).

## ⚡ If you only read 10 lines

- Scrape any creator into Notion: `python3 execution/social_intel.py scrape @handle --platform youtube --limit 5 --batch <tag>` — proven at $0.01; transcripts free via yt-dlp captions.
- Competitor ad intel at $0: `/ad-spy <brand>` — Meta Ad Library via Playwright, ranked by "Started running on" (longest-running = winning). Raw HTTP 403s; only a real browser works.
- Everything lands in the **Social Intelligence** Notion DB `3a749875-a897-8104-a867-fc9aeb53f52c` (env `NOTION_DB_SOCIAL_INTEL`).
- The doctrine line: *provide really good examples — retrieval beats prompt tricks; taste is the input the agent can't supply.*
- Winning ad → on-brand variants: `/creative-from-winners` (never carry the source ad's real people/names — the "Dr. Fahim Hussain" rule).
- Site → brand sheet without Firecrawl: `/brand-asset-scrape <domain>` (Tavily + Playwright screenshots).
- Inbox at scale, zero sends: `/inbox-drafts "<intent>"` — Gmail MCP drafts + links, corrections written back into the workflow file.
- Inert until keys land in `.env`: `/post-scheduler` (`TYPEFULLY_API_KEY`) and `/scheduling-links` (`CALCOM_API_KEY`) — both free tiers, ~3 min each.
- Expert front door: `/riley-brown`. A-tier pending Farrice's blind pass (`.tmp/blind-pass-riley/` vs `extractions/riley-brown-marketing-automation/reference-corpus/`).
- Budget guardrails stand: Apify $29/mo wallet ($2.93 spent), $0.25 per-run ceiling, hard-stop at 90%.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/scrape-creator <handle>` (`social_intel.py scrape`) | Notion pages: video, transcript, metrics, hook + analysis | You want a creator's corpus banked and analyzed |
| `/ad-spy <brand>` (+ `execution/ad_spy.py`) | Longest-running-ad ranking → Notion, inference-labeled | Before pitching/serving any brand — esp. the $2,500 sprint ICP |
| `/creative-from-winners <ad ref> --brand X` | 3+ divergent on-brand executions of a proven structure | A winning competitor ad exists and you need volume |
| `/brand-asset-scrape <domain>` | `BRAND-ASSETS.md`: colors, type, logos, voice samples | New client/brand, no DESIGN.md yet |
| `/inbox-drafts "<intent>"` | Gmail drafts + review links, zero sends | Any batch-reply job (declines, outreach, follow-ups) |
| `/post-scheduler`, `/scheduling-links` | Typefully draft / shaped Cal.com link + email | After keys land; staging posts or booking guests |
| `/riley-brown` | Expert persona + full 12-workflow arsenal | Agentic-marketing-ops thinking, skill design, stack decisions |
| `/riley-scrape-to-skill` | A named voice-skill from any creator (his flagship) | You want to write in a scraped creator's voice permanently |
| `python3 execution/social_intel.py status` | Apify budget + last batch | Before any batch scrape |

## The mental model

1. **Capability, not tool.** Every paid tool in a creator's stack maps to a capability, and the harness already held an equivalent for all nine — some literally the same vendor through a cheaper door (ScrapeCreators publishes its actors on Apify inside the existing $29/mo). Inventory before buying; PoC the free route with a ceiling first.
2. **Examples are the engine.** Riley's whole system is example-supply-chain engineering: scrape verified winners (sponsored posts excluded, with an audit trail) → structure them → freeze as named skills → generate in learned voice. Our `/extract` family is the industrial version of his "turn it into a skill."
3. **The terminus is human.** Nothing auto-sends, auto-posts, or auto-schedules. Drafts and links, always — the human supplies taste and the send.
4. **Watch the frames.** The transcript said "just ask"; the frames showed multi-file Python pipelines, AGENTS.md memory commands, and seven API keys. The setup a creator doesn't narrate is where the real system lives.

## Per-capability sections

### Social Intelligence pipeline (`social_intel.py` + `/scrape-creator`)
**What it is:** platform → Apify sc-* actor (or free yt-dlp captions for YouTube) → normalized post records → one Notion page each (metrics, hook, media URL, full transcript chunked into the body).
**When:** banking a creator's corpus for analysis, voice extraction, B-roll hunting, caption borrowing.
**When NOT:** one-off "what did X post today" — just open the profile; a scrape run costs cents and a minute.
**Invoke:** `python3 execution/social_intel.py scrape "<handle_or_url>" --platform auto|instagram|tiktok|youtube --limit N --batch "<tag>" [--dry-run]`
**Worked example:** `scrape @rileybrownai --platform youtube --limit 2 --batch poc-2026-07-24` → 2 verified pages, $0.01, transcripts free.
**Honest edges:** Instagram/TikTok paths written defensively but never live-run; IG has no transcript actor (caption stands in).

### Ad-spy (`ad_spy.py` + `/ad-spy`)
**What it is:** read-only Playwright over the public Meta Ad Library; extracts "Started running on", copy, CTA, platforms; ranks by runtime; ingests top N to Notion with analysis labeled as inference (never claimed as ROAS).
**When:** before pitching any supplement/performance brand; quarterly competitor sweeps.
**When NOT:** you need actual spend/ROI numbers — no public source has them; don't let anyone fabricate them.
**Worked example:** AG1 → 23k raw keyword hits filtered to 9 genuine drinkAG1 ads → top 5 ingested; longest-running: two 176-day Hugh Jackman video variants.
**Honest edges:** keyword search interleaves unrelated advertisers (filter by advertiser page link, not keyword); Apify fallback documented but not wired (no Meta actor in ACTORS dict).

### Creative + brand + ops layer
**What:** `/creative-from-winners` (structure transfer through Dara/Fantastic Studio/Canva/Higgsfield — options, never a pipeline), `/brand-asset-scrape` (Tavily crawl + Playwright screenshots → traceable asset sheet), `/inbox-drafts` (Gmail MCP; batch >3 confirms the thread list first; Standing Corrections section makes it self-improving), `/post-scheduler` + `/scheduling-links` (activation notes at the top of each file).
**Honest edges:** scheduler shells are inert until Farrice pastes the two free API keys; Buffer's public API is closed — Typefully is the X route.

### The expert skill (`/riley-brown`)
**What:** 16 patterns with verbatim anchors, 12 `riley-*` workflows, 9 execution prompts, recognition-test gate, claims ledger including "what the source does NOT establish."
**Honest edges:** A-tier awaits Farrice's blind pass; the Knowledge Vault carries 2 duplicate Riley pages from the earlier Codex half-source session (decide keep/delete).

## Composition table

| Stack | When it earns its cost |
|---|---|
| `/scrape-creator` → `/extract` | A scraped creator proves pattern-rich — corpus is already banked, extraction starts warm |
| `/ad-spy` → `/creative-from-winners` → `/dara-static-engine` | Sprint-offer deliverable: intel → variants → test plan |
| `/scrape-creator` → `/inbox-drafts` | Personalized outreach grounded in what the recipient actually makes |
| `/brand-asset-scrape` → `/design-md-extract` | Client engagement needs a real DESIGN.md, not a moodboard |
