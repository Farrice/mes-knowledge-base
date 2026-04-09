# Apify Usage Policy

> **Monthly Budget Limit: $29.00 (Apify Starter plan)**
> This directive applies to ALL agents, workflows, and research tasks that use Apify.
> **Last Updated: 2026-04-06**

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

## The 7 Approved Actors

These are the only actors loaded in `.mcp.json` and `execution/apify_client.py`. Adding new actors requires editing both files.

| Actor key | Apify ID | Purpose | Cost class |
|---|---|---|---|
| `reddit` | `trudax/reddit-scraper-lite` | Reddit posts/comments/subreddits | Cheap (~$0.001/result) |
| `instagram` | `apify/instagram-scraper` | IG profiles, posts, hashtags | Cheap (~$0.0005/result) |
| `tiktok` | `clockworks/free-tiktok-scraper` | TikTok hashtags, profiles | Medium (~$0.004/result) |
| `youtube` | `apidojo/youtube-scraper` | YouTube videos + transcripts | Medium (~$0.005/result) |
| `amazon` | `junglee/amazon-scraper` | Amazon products, reviews | Cheap-Medium (~$0.0015/result) |
| `maps` | `compass/crawler-google-places` | Google Maps places, reviews | Medium (~$0.007/result) |
| `web` | `apify/rag-web-browser` | JS-rendered page fetch | Cheap (~$0.003/result) |

**Why these specific actors**: Best cost/quality ratio in their category as of 2026-04-06. Reddit-scraper-lite is the cheapest reliable Reddit option. Instagram-scraper is the cheapest at $0.50/1k. No expensive enterprise actors are loaded — even if an agent tries to call something else, the MCP server simply doesn't have it.

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
