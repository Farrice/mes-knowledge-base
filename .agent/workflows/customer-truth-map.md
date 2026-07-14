---
description: "End-to-end Voice-of-Customer conductor — gather real customer language, clean to signal, build the six-category map, find the deeper job + the widest gaps, put it to work in copy/content/offers, and keep it fresh — by orchestrating all 12 /ctm-* subroutines under a verbatim-integrity gate"
---

# /customer-truth-map

The front-door conductor (alias `/ctm`) for the Customer Truth Map. Point it at a customer + problem and it walks the six phases in order, orchestrating the 12 granular workflows — it sequences, grounds, and gates; it does not reimplement them.

## Trigger
`/customer-truth-map` (alias `/ctm`)

## Workflow
`skills/customer-truth-map/workflows/customer-truth-map.md`

## Quick Use
Provide:
1. One customer + one problem cluster (narrow — the "solo bookkeeper who just lost a big client" test)
2. Real sources (communities/threads/own-data), if known
3. Which output it feeds (copy / content / positioning / offer) and whether a map already exists

## Modes
- **BUILD** — no usable map yet: Layer-0 ground → Phases 1–4 → finished map
- **APPLY** — a map exists, you need deliverables: Phase 5 only (`/ctm-to-*`)
- **REFRESH** — a map may be stale: Phase 6 (`/ctm-refresh`, optional `/ctm-triangulate`)

Cold start that also wants outputs runs BUILD → APPLY. Default for an unspecified ask is BUILD.

## Pipeline
0 Ground (memory_facade + Recall) → 1 Scope → Gather → 2 Clean → 3 Map → 4 Jobs → Gaps → (Deepen) → 5 to-Copy/Content/Offer → 6 Refresh/Triangulate

## Output
Finished six-category map (Say/Think/Feel/Do + Pains/Gains, source-tagged) + JTBD reframes + ranked gap shortlist; or the grounded apply payload; or the refreshed map + dated change-log. Plus a run receipt and the 9-criterion quality gate (Verbatim-Integrity veto).

## Stacks With
→ all 12 subroutines: `/ctm-scope` `/ctm-gather` `/ctm-clean` `/ctm-map` `/ctm-jobs` `/ctm-gaps` `/ctm-to-copy` `/ctm-to-content` `/ctm-to-offer` `/ctm-triangulate` `/ctm-refresh` `/ctm-deepen`
→ hand-offs: `/copy-engine`, `/ghostwrite`, master-copywriter · `/novelty-forge`, `/parallax`, `/diandra-*` · `/build-bos`, positioning skills
→ `/buyer-sourcer`, `/mcraney-deep-canvass`, consumer-posture, fact-verifier
