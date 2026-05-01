---
description: Scan for rising trends and "Shadow Market" opportunities
---

> **Browser tools**: For live community signals (Reddit threads, niche forums, Twitter conversations) when Apify is rate-limited or you need to verify a specific thread's current state, use Playwright (`mcp__playwright__browser_*`) per `directives/browser-automation-routing.md`. Apify remains primary for scaled scraping; Playwright is the targeted-investigation alternative.

# ⚠️ CRITICAL: This workflow requires LIVE RESEARCH. Do NOT use mocked or simulated data.

## Overview
This workflow replaces the deprecated `trend_scanner.py`. The Agent (you) performs the intelligence work.

## Phase 1: Entity Understanding
Before research, classify the niche:
-   **Product/Service**: Target keywords like "[niche] review", "[niche] price", "best [niche]".
-   **Demographic**: Target keywords for PROGRAMS/ASSISTANCE that serve them.
-   **Program**: Target eligibility, requirements, comparison keywords.

## Phase 2: Trend Research (REQUIRED)

This phase has two parallel tracks: **macro trend signals** (Perplexity/web search — synthesis tasks) and **live community signals** (Apify — raw extraction). Run both.

### Track A: Macro Trends (Perplexity / search_web)

Use `search_web` or `perplexity_ask` for these — they need synthesis, not raw extraction:

1.  **Query**: `"[Niche] trends 2026 rising"`
    -   **Extract**: What topics are rising? What influencers are talking about?
2.  **Query**: `"[Niche] exploding topics" OR "[Niche] Google Trends data"`
    -   **Extract**: Is the trend rising, stable, or falling?

### Track B: Live Community Signals (Apify-First)

For the "what are people actually complaining about RIGHT NOW" signal — Apify Reddit scraper returns raw threads instead of fragmented SERP snippets:

```bash
# Search Reddit-wide for the niche
python execution/apify_client.py reddit "[Niche]" --limit 50 --comments

# Pull from specific niche subreddits if you know them
python execution/apify_client.py reddit --subreddit [SubredditName] --limit 30 --comments
```

**Extract from the raw threads**:
- Recurring complaints (signals supply gaps)
- "I wish I had..." moments (signals demand)
- Brand mentions or generic-product names (signals branding opportunities)
- Comment counts + upvote ratios (signals heat)

**Optional — TikTok hashtag scan** (medium cost ~$0.20, only if TikTok is a major signal source for this niche):

```bash
python execution/apify_client.py tiktok [niche_hashtag] --limit 50
```

**Fallback Contract**: If any Apify call returns `{"fallback": true}`, the monthly cap is hit. Reroute to:
- `search_web`: `site:reddit.com "[Niche]"`
- OR `perplexity_ask`: "What are the top community complaints and 'I wish I had' moments in [Niche] right now? Cite Reddit threads with URLs."

## Phase 3: Shadow Market Assessment (Samuel Thompson Logic)
**Definition**: A "Shadow Market" = High Desperation + Low Competition Quality.
-   **Query**: `"[Niche Topic]" SERP analysis` (or just search the topic directly)
    -   **Assess**: Are the top 3 results from major players (Zillow, Amazon, NYT)? Or from small blogs/outdated sites?
    -   If **small/outdated competitors** dominate AND search interest is high = **Shadow Market FOUND**.

## Phase 4: Synthesis
Output a report with:
-   **Top 3 Rising Trends** (with sources)
-   **Shadow Market Verdict** (Yes/No, with justification)
-   **Suggested Attack Angle** (What content to create)

## Output Location
Write the report to `strategy_briefs/Trend_Report_[Niche].md`.
