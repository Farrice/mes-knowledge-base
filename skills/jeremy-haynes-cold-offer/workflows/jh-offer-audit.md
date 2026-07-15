---
description: Tear down an existing offer against the "not random" standard — component↔narrative traceability audit
---

# /jh-offer-audit — Offer Alignment Audit

Haynes' component challenge run as a formal audit: every component must name the narrative element it neutralizes; every narrative element must have a component answering it.

## Pre-Flight Gate

- Is there a narrative to audit against? If no umbrella narrative exists → run `/jh-umbrella-narrative` first (an audit against an assumed narrative is theater).
- Is the real question "why did growth stall at scale"? → `/jh-plateau-diagnostic` instead; this audit is one input to it.

## Skill Acquisition

- `genius.md` — component challenge, quality rubric, anti-patterns
- The offer's current articulation (sales page, VSL script, pitch deck, call script — as it is actually presented to prospects)

## Execution

1. **Inventory**: list every component the offer currently includes, in the language the prospect hears.
2. **Trace forward**: for each component → which problem/circumstance/desired outcome does it neutralize? Orphans (no narrative element) get marked CUT-CANDIDATE. "This isn't random shit that's included in the offer stack" is the bar.
3. **Trace backward**: for each narrative element → which component answers it? Unanswered elements = GAPS, each with a proposed component.
4. **Scar check**: does any component TYPE collide with the buyer's failure history (done-for-you to the agency-burned, group program to the mastermind-burned)? Mark REFRAME-OR-REPLACE.
5. **Next-problem check**: what happens immediately after purchase, and does the offer absorb it? The deal dies at the adjacent step.
6. **Articulation order check**: does the presentation open with problems/circumstances before the bridge? Value-stack anchoring, fake urgency, front-loaded education to scanner-mode prospects → each flagged.
7. **Cold-read verdict**: 30-second stranger test on the current articulation, PASS/FAIL with the failing sentence quoted.
8. **Score** against the 8-criterion rubric in genius.md (1–10 each, named evidence per score).

Execution prompt: references/prompts-v2/offer-alignment-teardown.md — honor its Output Contract.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Client audit deliverable | ≤2 pages (density rule); receipts in appendix; strip Haynes-reported numbers |
| Own offers (Farrice) | Add PMF Offer Shelf cross-check — surface, don't regenerate |
| Webinar/VSL offers | Audit the pitch-segment articulation separately from the landing page |
| E-com/product | Components = guarantees, bundles, shipping, support; same traceability law |

## Output Requirements

Audit Report: component trace table (component → element → verdict), gap list with proposed components, scar collisions, next-problem finding, articulation-order findings, cold-read verdict, rubric scorecard, top-3 fixes ranked by close-rate impact.

## Quality Gate

- Every verdict cites the specific component and narrative element (no vibes)
- Gaps come with proposed components, not just complaints
- Fixes ranked by conversion impact, not ease
- Rubric scores anchored with evidence
