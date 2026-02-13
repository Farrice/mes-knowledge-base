---
description: Scan for rising trends and "Shadow Market" opportunities in a niche using Agentic Research.
---

# ⚠️ CRITICAL: This workflow requires LIVE RESEARCH. Do NOT use mocked or simulated data.

## Overview
This workflow replaces the deprecated `trend_scanner.py`. The Agent (you) performs the intelligence work.

## Phase 1: Entity Understanding
Before research, classify the niche:
-   **Product/Service**: Target keywords like "[niche] review", "[niche] price", "best [niche]".
-   **Demographic**: Target keywords for PROGRAMS/ASSISTANCE that serve them.
-   **Program**: Target eligibility, requirements, comparison keywords.

## Phase 2: Trend Research (REQUIRED)
Use `search_web` to find real data. Execute ALL of these queries:

1.  **Query**: `"[Niche] trends 2026 rising"`
    -   **Extract**: What topics are rising? What influencers are talking about?
2.  **Query**: `"[Niche] subreddit activity" OR site:reddit.com "[Niche]"`
    -   **Extract**: What are people complaining about? What's hot?
3.  **Query**: `"[Niche] exploding topics" OR "[Niche] Google Trends data"`
    -   **Extract**: Is the trend rising, stable, or falling?

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
