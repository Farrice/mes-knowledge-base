# Integration Guide — Riley's Stack vs. Ours

**Read this first:** Riley demonstrates a **paid third-party stack**. We hold none of those keys and don't replicate his spend. Every Riley capability maps onto infrastructure Antigravity already owns — mostly **$0**, with a small metered Apify budget for social scraping. This document is the *mapping*, not an API reference for tools we don't hold.

> Earlier drafts of this file invented pricing tables, REST endpoints (`api.foreplay.co/v1/ads`, `api.scrapecreators.com`), Python clients, and monthly budget estimates for services we have no account with. All of that is removed. The only dollar figures Riley states on record are **"$250 for nine [frontier] prompts"** and **"the $20/month plan"** — both about model spend. See `source-quotes.md` § "What the Source Does NOT Establish."

---

## The Mapping

| Riley capability | His tool (paid) | **Our route** | Cost | Live workflow / script |
|---|---|---|---|---|
| Scrape a creator (video, transcript, metrics) → DB | ScrapeCreators | Apify `sc-*` actors + free yt-dlp captions → Social Intelligence Notion DB | ~$0.005–0.25/run (Apify $29/mo plan, budget-guarded); yt-dlp captions **$0** | `/scrape-creator` · `execution/social_intel.py` |
| Competitor ad-spy by longest-running ad | Foreplay ($59–149/mo) | Meta Ad Library via **read-only Playwright** | **$0** | `/ad-spy` · `execution/ad_spy.py` |
| Winning ad → on-brand creative | Paper.design | Dara static engine / Fantastic Studio / Canva MCP / Higgsfield | $0 unless a generator credit applies (cost-gated) | `/creative-from-winners` |
| Scrape a brand's site → asset sheet | Firecrawl | Tavily (crawl/extract) + Playwright (screenshots) | **$0** | `/brand-asset-scrape` |
| Email drafts at scale | Gmail | Gmail MCP — **drafts only, never send** | **$0** | `/inbox-drafts` |
| Stage/schedule social posts | Buffer/Typefully | Typefully `POST /v1/drafts` | **$0** (free tier); key pending | `/post-scheduler` |
| Constraint-encoded booking links | Cal.com | Cal.com API v2 (`event-types`/`availability`) | **$0** (free tier); key pending | `/scheduling-links` |
| Data warehouse / staging | Notion | Social Intelligence DB (`3a749875-a897-8104-a867-fc9aeb53f52c`) | included | `execution/notion_api.py` (pins `2022-06-28`) |
| Pattern analysis / voice generation | Codex + GPT-5.6 | Claude (this harness) + `/extract` | model cost only | Chain / `/extract` |
| Board / canvas MCP | Paper MCP | Canva MCP / Pencil (`.pen`) | included/gated | — |

---

## Per-Route Notes

### `/scrape-creator` (Apify + yt-dlp + Notion)
- Budget: `.agent/apify-usage.json`, $29/mo plan, soft-warn 70%, hard-stop 90%. `python3 execution/social_intel.py status` shows state.
- Per-run ceilings live in `apify_client.py`: pay-per-event TikTok actors default to a **$0.25/run** ceiling; YouTube metrics ~**$0.005/video** (per_result); YouTube transcript **free via yt-dlp**, falling back to `sc-youtube-transcripts` (~$0.10/run cap) only if captions are missing.
- Instagram has no dedicated transcript actor in the current contract — caption stands in for Hook/Analysis.
- Riley's authenticity filter is honored downstream: scrape, then exclude sponsored in the analysis pass and note the exclusion.

### `/ad-spy` (Meta Ad Library, $0)
- Read-only Playwright, Tier 1 per `directives/browser-automation-safety.md` (navigate/snapshot/evaluate; no login, no state change).
- **Ad Library exposes no likes/views/spend/ROI for commercial ads.** Runtime is the only free performance proxy. Leave `Views`/`Likes`/`Comments` blank in Notion — never fabricate. This is the one honest gap vs. Foreplay.
- No Apify meta-ads actor is wired in `ACTORS` yet — do not run an untested one without Farrice's go-ahead (the cost-gate only guards registered actors).

### `/inbox-drafts`, `/post-scheduler`, `/scheduling-links` (human-gate terminus)
- All three encode Riley's #9 draft-terminus doctrine: **the agent stages, the human ships.** `/inbox-drafts` creates Gmail drafts and never calls send, even if asked mid-batch.
- `/post-scheduler` and `/scheduling-links` need one-time free key setup (`TYPEFULLY_API_KEY`, `CALCOM_API_KEY` in root `.env`). Missing key → deliver the platform-ready artifact + the activation note; never fake a staged post/link.

### Notion — Social Intelligence DB
- Single shared DB (`3a749875-a897-8104-a867-fc9aeb53f52c`), not a new DB per scrape. Schema in `references/notion-schema-templates.md` and `directives/notion-databases.md`.
- Riley's "Notion DB = disposable staging" instinct maps to our `Batch` tagging + `Extract Candidate` checkbox: the DB is a staging/querying surface; the durable asset is the extracted skill.
- Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`) — never the JS client (silently breaks schema updates).

---

## The Three-Path Integration Ladder (Riley's own logic, generalized)

When wiring any new tool, choose in this order (Hidden Knowledge #6):
1. **MCP** — richest, when a connector exists (Gmail, Canva, Notion, Playwright, Higgsfield here).
2. **Raw REST** — API key → "create a skill that fully controls it" (Riley's Cal.com bootstrap; our `/scheduling-links`, `/post-scheduler`).
3. **Computer-use / record-and-replay** — GUI automation when neither exists (Playwright drive; Riley's Typefully record-and-replay).

The integration surface is "does it have an API," not "does it have a plugin."
