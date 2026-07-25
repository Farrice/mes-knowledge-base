---
description: Run Briar's ideation inputs off the Social Intelligence DB — /scrape-creator batches become the inspiration list with deterministic outlier math
---

# Social Intelligence Bridge

Input #1 (inspiration list) and #3 (packaging outliers), mechanized: the Social Intelligence
Notion DB (fed by /scrape-creator) supplies creators, metrics, hooks, and transcripts — so
baseline math is computed, not eyeballed.

## Pre-Flight Gate

Load `../genius.md` → Five-Input table. Confirm: which batches/creators exist in the DB
(`python3 execution/social_intel.py status`, or query the DB), and the target niche + goal mix.
Thin coverage (<10 posts for a creator) = note baselines as provisional.

## Skill Acquisition

- `../genius.md` (Baseline Click, thumbnail attribution)
- `.agent/workflows/scrape-creator.md` (pipeline + DB shape)
- Workflows 07 (outlier math) and 08 (transfer filter) execute the downstream steps

## Execution

1. **Coverage check**: List tracked creators + post counts. Gaps in the 15-20 inspiration list →
   propose /scrape-creator runs (Apify budget-aware — scrape is the only paid step).
2. **Baseline table**: Per creator, compute baseline from banked Views (exclude top outliers
   from the average).
3. **Outlier pass**: Multiples per post; ≥3× → true outliers. Pull each outlier's Hook +
   transcript from the page body for idea harvesting.
4. **Analysis reuse**: Read existing per-post Analysis properties — verdicts already grounded
   there don't get re-derived.
5. **Route**: outliers → /bc-contextualize; pattern-rich creators → mark Extract Candidate
   checkbox (graduation to /extract — corpus already banked in page bodies).
6. **Idea cards**: Output in ideation-hour card format, signal source = "SI-DB: creator/post".

## Content Type Adaptations

| Type | Adaptation |
|------|-----------|
| Weekly ideation | This replaces manual burner-account scrolling for tracked creators |
| Client niches | Batch per client niche; keep baselines per-creator, per-platform |
| Competitive intel | Stack `competitive-intel` agent for positioning-level analysis |
| Extraction pipeline | Extract Candidates flow to /extract with transcripts pre-banked |

## Output Requirements

Coverage report + baseline table + verified outlier list (with multiples) + idea cards +
scrape/extract recommendations.
Execution prompt: references/prompts-v2/outlier-scan-report.md — honor its Output Contract.

## Quality Gate

Baselines computed from banked data (shown). No idea card without a DB-traceable source. Apify
spend surfaced before proposing new scrapes. Extract Candidate flags justified by pattern
density, not view count alone.
