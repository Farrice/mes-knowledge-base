---
description: "Phase 4 Step 2 engine — build the gap table (Pain/Job → Current Fix → The Gap → Gap-Width 1–5), sourcing Current Fix from competitor products + the map's ⚠ WORKAROUND DIY fixes, then sort descending by gap width. The widest-gap rows are the named shortlist passed to /ctm-to-copy, /ctm-to-content, /ctm-to-offer"
---

# /ctm-gaps

Map the gaps — turn a pile of complaints into a ranked view of where to act. Lay each pain/job against how the customer handles it today (competitors + DIY workarounds), name where that fix falls short, and score the gap width. Widest-gap-first: a better message lands hardest where the current fix frustrates most.

## Trigger
`/ctm-gaps`

## Workflow
`skills/customer-truth-map/workflows/ctm-gaps.md`

## Quick Use
Provide the `/ctm-jobs` list + the `/ctm-map` ⚠ WORKAROUND tags. Runs prompt P6. Any competitor claim must be fact-verified, not asserted from memory.

## Pipeline
1 Assemble Pain/Job rows + run P6 → 2 Fill Current Fix (competitors + ⚠ WORKAROUND DIY) → 3 Name The Gap in the customer's reality → 4 Score Gap Width 1–5, sort descending → 5 Name the widest-gap shortlist + route each

## Output
The 4-column gap table sorted by width + per-row width rationale + the named widest-gap shortlist (top 3–5, each routed to its best-fit `/ctm-to-*`) + honesty confirmation.

## Stacks With
→ upstream `/ctm-jobs` + `/ctm-map`, downstream `/ctm-to-copy` `/ctm-to-content` `/ctm-to-offer`
→ fact-verifier for competitor claims · owns rubric criterion 7 (Gap Ranking)
