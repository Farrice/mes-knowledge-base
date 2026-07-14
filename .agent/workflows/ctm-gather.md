---
description: "Phase 1 Step 3 of the Customer Truth Map — the WIRED collection step. Pull raw, unedited verbatim customer language down the full fallback chain (Apify Reddit → NotebookLM → Playwright → WebFetch → research.py → manual paste) plus own-data ingest, keep every source tag and permalink, honor the cost gate, output one raw corpus"
---

# /ctm-gather

Collect the raw language (wired). Takes the source map from `/ctm-scope` and collects raw, unedited customer language — typos and all — down a real, budgeted fallback chain. It collects only; it does not clean, sort, or paraphrase.

## Trigger
`/ctm-gather`

## Workflow
`skills/customer-truth-map/workflows/ctm-gather.md`

## Quick Use
Provide the `/ctm-scope` source map. Own-data ingest FIRST (free, richest), then down the chain. Surface projected cost before any paid call; never retry a denied call.

## Pipeline
Step 0 Own-data ingest (free) → 1 Apify Reddit (budget-gated) → 2 NotebookLM → 3 Playwright (read-only) → 4 WebFetch → 5 research.py → 6 manual paste (the floor)

## Output
One raw corpus of verbatim, source-tagged blocks (`> "raw text" — [source, permalink]`) + an honest gather receipt (which tools fired, fell through, source counts, total spend) + a coverage note. Hands to `/ctm-clean`.

## Stacks With
→ hands off to `/ctm-clean`
→ `/buyer-sourcer` (luke-iha-avatar-machine) for the scaled mine
→ cost gate (Apify), browser-automation-safety (Tier-1 Playwright)
