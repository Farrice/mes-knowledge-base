# Apify Usage Policy

> **Monthly Budget Limit: $29.00 (Apify Starter plan)**
> **Per-Run Cost Cap: $5.00 default** (enforced 2026-08-05, override via approval token)
> This directive applies to ALL agents, workflows, and research tasks that use Apify.
> **Last Updated: 2026-08-05**

## Purpose

Apify provides scraping, social listening, and structured data extraction that **Perplexity and generic web search cannot reach**: JS-rendered pages, rate-limited sites, login walls, and structured datasets from Reddit, Instagram, TikTok, YouTube, Amazon, Google Maps, and arbitrary websites.

> [!IMPORTANT]
> **Apify is for raw data extraction. Perplexity is for synthesis. Use them as a pipeline (Apify → Perplexity → deliverable), NOT as competitors.**

---

## When to Use Apify (PRIMARY)

- **Reddit deep dives** — thread mining, comment analysis, sentiment, subreddit scans
- **Social listening** — Instagram, TikTok, YouTube content scraping
- **E-commerce intelligence** — Amazon products, Best Sellers, reviews
- **Local business research** — Google Maps places, contact info, reviews
- **Site-specific extraction** — when `read_url_content` chokes on JS-rendered pages
- **Bulk structured data** — when you need 50+ items from a single source

## When to Use Perplexity Instead

- **Synthesis and Q&A** — combining many sources into an answer
- **Citation-backed research** — when you need fact-checked claims with sources
- **Trend interpretation** — understanding *what* the data means, not gathering it
- **Cross-source reasoning** — multi-step research that doesn't need raw extraction

## When to Use Tavily / Web Search Instead

- **Quick factual lookups** — dates, prices, names
- **General exploration** — directional context where raw data isn't needed
- **Apify budget exhausted** (see Fallback Contract below)

## When NO External Tool Is Needed

- Synthesis of already-gathered data
- Framework application (applying a known methodology)
- Creative copywriting, code generation, persona embodiment

---

## The 22 Approved Actors (as of 2026-08-05)

`execution/apify_client.py` (ACTORS dict) is the source of truth and the live invocation path. **Note (2026-08-05)**: the Apify MCP server is currently NOT registered in `.mcp.json` — the Python wrapper is the only live path; if the MCP server is re-registered, its `--tools` list must be regenerated from `apify_client.py mcp-tools`.

**Per-run cost gate (2026-08-05, Farrice-approved)**: `PER_RUN_CAP_USD = 5.00` in `apify_client.py` — any run with an estimated cost above $5 requires a 15-minute approval token (`python3 execution/cost_gate.py approve apify-deep-dive`). $5 is the default working tier; ~$25 runs are deliberate deep-dives unlocked per-run by Farrice. Actors must be **universal** capabilities (any workflow may call them), never wired exclusively to one project.

### Original 7 Actors (per_result pricing)

| Actor key | Apify ID | Purpose | Cost/result | Model |
|---|---|---|---|---|
| `reddit` | `trudax/reddit-scraper-lite` | Reddit posts/comments/subreddits | ~$0.001 | per_result |
| `instagram` | `apify/instagram-scraper` | IG profiles, posts, hashtags | ~$0.0005 | per_result |
| `tiktok` | `clockworks/free-tiktok-scraper` | TikTok hashtags, profiles | ~$0.004 | per_result |
| `youtube` | `apidojo/youtube-scraper` | YouTube videos + transcripts | ~$0.005 | per_result |
| `amazon` | `junglee/amazon-scraper` | Amazon products, reviews | ~$0.0015 | per_result |
| `maps` | `compass/crawler-google-places` | Google Maps places, reviews | ~$0.007 | per_result |
| `web` | `apify/rag-web-browser` | JS-rendered page fetch | ~$0.003 | per_result |

### New 10 Scrape Creators Actors (pay_per_event pricing, added 2026-07-16)

**Note**: These actors use **pay_per_event pricing** — cost is NOT per result, but per API call / per run. The actual cost is read from the Apify run response (`usageTotalUsd`) by the wrapper. See [Pay-Per-Event Pricing](#pay-per-event-pricing) section below.

| Actor key | Apify ID | Purpose | Ceiling | Model |
|---|---|---|---|---|
| `sc-tiktok` | `scrape-creators/best-tiktok-scraper` | TikTok search/trending/profile/hashtag/video | $0.25 | pay_per_event |
| `sc-tiktok-video` | `scrape-creators/best-tiktok-video-scraper` | TikTok video-specific scrape | $0.25 | pay_per_event |
| `sc-tiktok-profile` | `scrape-creators/best-tiktok-profile-scraper` | TikTok profile data | $0.25 | pay_per_event |
| `sc-tiktok-hashtag` | `scrape-creators/best-tiktok-hashtag-scraper` | TikTok hashtag scrape | $0.25 | pay_per_event |
| `sc-tiktok-transcripts` | `scrape-creators/best-tiktok-transcripts-scraper` | TikTok video transcripts (if available) | $0.25 | pay_per_event |
| `sc-tiktok-followers` | `scrape-creators/best-tiktok-followers-scraper` | TikTok follower data | $0.25 | pay_per_event |
| `sc-tiktok-following` | `scrape-creators/best-tiktok-following-scraper` | TikTok following data | $0.25 | pay_per_event |
| `sc-youtube-transcripts` | `scrape-creators/best-youtube-transcripts-scraper` | YouTube video transcripts (rich source of insight) | $0.25 | pay_per_event |
| `sc-youtube-channels` | `scrape-creators/best-youtube-channels-scraper` | YouTube channel metadata | $0.25 | pay_per_event |
| `sc-youtube-comments` | `scrape-creators/best-youtube-comments-scraper` | YouTube video comments | $0.25 | pay_per_event |

**Why these actors**: Best enrichment option for social listening. Scrape Creators actors are mission-built for consistent structured data from TikTok and YouTube — superior to generic scrapers. Transcripts are especially valuable for research (direct voice, not interpreted). No fallback to cheaper actors — use these for their category or reroute to Perplexity.

### Expansion: Content & Knowledge Work Actors (added 2026-08-05)

**Goal**: Expand research capability for content discovery, competitive intelligence, and knowledge work. All newly registered actors are pay_per_event (actual cost from Apify response) with default $0.25 per-run ceiling. See [Per-Run Cost-Gate](#per-run-cost-gate-default-500-over-requires-approval).

| Actor key | Apify ID | Purpose | Ceiling | Pricing | Notes |
|---|---|---|---|---|---|
| `linkedin-search` | `harvestapi/linkedin-profile-search` | LinkedIn profile search + filtering | $0.25 | pay_per_event | 4.81★ (744 users). Search profiles by title, location, company. Cost: ~$0.10/search page + $0.004–$0.01/profile. Rate limits apply to 300k+ profiles. |
| `linkedin-posts` | `apimaestro/linkedin-profile-posts` | LinkedIn posts + engagement metrics | $0.25 | pay_per_event | 4.81★ (20,929 users). **Observed cost 2026-08-05: $2.00/1k posts** (100 posts → $0.20; 3 posts → $0.006). Real schema is `username` + `limit` (1-100/page) — unknown fields are silently ignored and the actor returns a full $0.20 page, so keep `limit` honest (fixed in `cmd_linkedin_posts`). |
| `twitter` | `kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest` | X/Twitter search + timeline | $0.25 | per_result | 4.58★. **Observed cost 2026-08-05: $0.25/1k tweets** (15 tweets → $0.0037). Registry uses 0.00025/result. Supports search, username, hashtag queries. |
| `facebook-ads` | `curious_coder/facebook-ads-library-scraper` | Facebook Ads Library (current + historical) | $0.25 | pay_per_event | 4.74★ (930 users). ~$0.75/1k ads. **Schema quirks (verified 2026-08-05)**: input is `urls` as `[{"url": ...}]` request objects (Ads Library search URLs, built by the CLI from your query); minimum 10 charged results; needs `memory_mb: 512` (1 URL per 512MB rule). All handled in `cmd_facebook_ads`. |
| `threads-search` | `jungle_synthesizer/threads-search-scraper` | Threads keyword search (posts + engagement) | $0.25 | per_result | ~$0.50/1k posts ($0.0005/post). Schema: `keywords` (array) + `maxItems`. No login. Smoke-verified 2026-08-05 (real posts w/ like/reply/repost counts). |

**When to use these actors**:
- **LinkedIn search**: prospect research, recruiter leads, founder discovery, competitive hiring analysis
- **LinkedIn posts**: content performance benchmarking, competitor publishing cadence, thought leadership validation
- **Twitter**: trend discovery, founder/expert activity monitoring, real-time signal verification, engagement patterns
- **Facebook Ads**: competitive ad spend analysis, creative/copy testing patterns, campaign targeting reverse-engineering
- **Threads search**: zeitgeist listening by keyword, hook/format mining, cross-posting signal for Meta-side audiences

---

## Pay-Per-Event Pricing (NEW — 2026-07-16)

**Scrape Creators actors do NOT charge per result.** Instead, they charge per run (a "pay-per-event" model). The actual cost depends on request complexity, not result count.

### How It Works (for workflows)

1. **Actual cost is read from Apify response**: The wrapper (`execution/apify_client.py`) extracts `usageTotalUsd` from the Apify run object after completion.
2. **Per-run ceiling enforced**: Default $0.25 per run (override with `--max-cost` or `--allow-expensive` flag).
3. **Cost is logged immediately**: Every run is logged to `.agent/apify-usage.json` with actual cost, not estimate.
4. **No estimate, no surprise**: Since cost is unknown beforehand, use the ceiling ($0.25) as a safety limit.

### In Python (execution/apify_client.py)

```python
result = run_actor(
    "sc-tiktok",
    {"searchTerm": "fitness"},
    limit=20,
    max_cost=0.25,           # Per-run ceiling
    allow_expensive=False     # Fail if run exceeds ceiling
)
```

If actual cost > $0.25, the run is rejected and returns `{"status": "cost_ceiling_exceeded", "fallback": true}`. Workflow must reroute to Perplexity or Tavily.

### In Workflows (via `/social-listen` or pulse scripts)

```bash
python execution/apify_client.py sc-tiktok --search "fitness tips" --limit 20 --max-cost 0.50
```

Override the per-run ceiling with `--max-cost` (still respects $29/mo global budget).

---

## Cost Tracking & Budget

| Metric | Value |
|--------|-------|
| **Monthly Budget** | $29.00 |
| **Soft Warn (Yellow)** | $20.30 (70%) — prefer cheap actors |
| **Hard Stop (Red)** | $26.10 (90%) — block, return fallback |
| **Reset Cadence** | Calendar month (1st at 00:00) — auto-reset by wrapper |

### Tracking File

Usage is tracked in: `.agent/apify-usage.json`

The wrapper auto-creates this file on first run, auto-resets on month change, and logs every actor invocation with cost.

### Realistic Monthly Capacity

At $29.00 budget, you can comfortably run all of:

- 20 Reddit deep dives (50 posts each) = ~$1.00
- 10 Instagram audits (20 posts each) = ~$0.10
- 5 TikTok hashtag scans (50 posts each) = ~$1.00
- 5 YouTube transcript runs (5 videos each) = ~$0.13
- 10 Amazon scrapes (30 products each) = ~$0.45
- 5 Google Maps runs (30 places each) = ~$1.05
- 100 generic web fetches = ~$0.30
- **Total: ~$4.03 of $29.00 used (~14%)**

**You have ~7x headroom**. Use Apify freely. The cap exists as a backstop.

---

## The Fallback Contract (CRITICAL)

The wrapper at `execution/apify_client.py` **NEVER raises an exception** on budget exhaustion. It always returns a structured response.

**On budget exhaustion**, the response contains:

```json
{
  "status": "budget_exhausted",
  "fallback": true,
  "message": "...",
  "alternative": "Use Perplexity (perplexity_client.py) or web search instead.",
  "items": []
}
```

**Workflows MUST check `.fallback` and reroute** when true:

1. **First fallback**: Perplexity (`perplexity_client.py` or `perplexity-ask` MCP)
2. **Second fallback**: Tavily search (`tavily-search` skill)
3. **Third fallback**: Generic `read_url_content` / web search

**This is what makes Apify safe**: workflows degrade, they don't break. Never wrap Apify calls in try/except expecting exceptions. Always check the JSON response.

---

## Three Budget States

| State | Range | Behavior |
|---|---|---|
| **Green** | 0–70% ($0–$20.30) | All Apify calls pass normally |
| **Yellow** | 70–90% ($20.30–$26.10) | Calls still go through, but wrapper writes `.agent/apify-budget-warning.flag` and prints stderr warning. Agents should prefer cheap actors (reddit, instagram, web) and avoid expensive ones (maps, youtube, tiktok). |
| **Red** | 90–100% ($26.10–$29.00) | Hard stop. Wrapper refuses new runs and returns `fallback: true`. |

The yellow flag file `.agent/apify-budget-warning.flag` is auto-cleared when budget returns to green (after monthly reset).

---

## Pre-Run Checks (for expensive operations)

Before any single call expected to consume **>0.5 CU (>$0.15)**, check budget:

```bash
python execution/apify_client.py budget-status
```

This is mandatory for:
- TikTok scans >50 posts
- Google Maps runs >30 places
- YouTube runs >10 videos
- Any Amazon scrape >100 products

Cheap actors (reddit, instagram, web) under default limits do NOT need a pre-check.

---

## Loop Protection

To prevent runaway research swarms from burning budget:

| Guard | Rule |
|---|---|
| **Per-call max_results** | Wrapper enforces a hard timeout (180s) and per-call result cap |
| **Per-task cap** | Max 5 Apify calls per task/swarm (orchestrator enforces) |
| **Duplicate detection** | Same query + same actor within same task → skip, reuse |
| **Fallback chain** | After 1 fallback response, switch the entire task to Perplexity for the rest of the run |

---

## Logging

Every actor invocation is auto-logged to `.agent/apify-usage.json` by the wrapper:

```json
{
  "ts": "2026-04-06T22:00:00+00:00",
  "actor": "reddit",
  "results": 50,
  "cost": 0.05
}
```

The list is bounded to the last 200 runs (FIFO).

---

## Override

To temporarily increase the budget (e.g., for a deep research sprint):

1. Edit `PLAN_DOLLARS` in `execution/apify_client.py`
2. OR manually edit `.agent/apify-usage.json` and bump `plan_dollars`
3. Document the override in `.agent/session-state.md`

To reset mid-month (use sparingly):

```bash
python execution/apify_client.py budget-reset
```

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-06 |
| **Activation Count** | 1 (initial install + verification) |
| **30-Day Review Date** | 2026-05-06 |

**Update Rule**: When this protocol fires (Apify call executed), the wrapper auto-updates `.agent/apify-usage.json`. This directive's tracking row is updated only on policy changes.

*Effective: 2026-04-06 | Plan: Apify Starter $29/mo | Soft warn 70%, hard stop 90%*
