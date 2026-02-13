---
description: Audit a keyword for "Buyer Intent" using linguistic analysis and live SERP validation.
---

# ⚠️ CRITICAL: This workflow requires LIVE SERP VALIDATION.

## Overview
This workflow replaces the deprecated simulated SERP logic in `keyword_auditor.py`. The Agent (you) performs live validation.

## Phase 1: Linguistic Intent Analysis (Keep from Original)
Classify the keyword based on its linguistic structure. This logic is valid:

| Trigger Words | Intent Class | Value |
| :--- | :--- | :--- |
| "buy", "price", "cost", "cheap", "discount", "deal", "coupon" | **Transactional** 💰💰💰 | HIGH |
| "best", "top", "review", "vs", "compare", "alternative" | **Commercial Investigation** 💰💰 | MEDIUM-HIGH |
| "how", "what", "history", "guide", "tutorial", "tip" | **Informational** 🧠 | LOW |
| Brand names, website names | **Navigational** 📍 | ZERO |

## Phase 2: Live SERP Validation (REQUIRED)
Use `search_web "[Keyword]"` to check the actual Search Engine Results Page.

-   **Check for Ads**: Does the search result mention "Ads" or "Sponsored" at the top?
    -   **If Yes**: Confirms high commercial value. Google sees money here.
    -   **If No**: Could be informational or too niche for advertisers.
-   **Check Top 3 Organic Results**:
    -   **If Dominated by Big Players** (Amazon, Zillow, Wikipedia, NYT): **HIGH Difficulty**.
    -   **If Dominated by Small Blogs/Forums**: **LOWER Difficulty** (Opportunity).

## Phase 3: CPC Estimation (Optional but Valuable)
If possible, search for: `"[Keyword]" CPC cost per click Google Ads`
-   **Extract**: Average CPC from industry benchmarks.
-   **Cite the source** (e.g., WordStream, SEMrush blog).

## Phase 4: Synthesis
Output an Intent Report:

```markdown
## Keyword Intent Report: [Keyword]

**Intent Class**: [Transactional/Commercial/Informational/Navigational]
**Value Score**: [0-100]
**Reasoning**: [Why this classification?]

**SERP Validation**:
-   Ads Detected: [Yes/No]
-   Top 3 Competitors: [List them]
-   Difficulty Assessment: [Low/Medium/High]

**Estimated CPC**: $[X.XX] (Source: [..])

**Verdict**: [ATTACK / MONITOR / AVOID]
```
