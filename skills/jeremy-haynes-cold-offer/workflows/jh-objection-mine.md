---
description: Mine sales-call transcripts into an objection pie chart, converting majority patterns into offer components and fragments into editions
---

# /jh-objection-mine — Objection→Component Pipeline

"An offer is ideally dynamic." AI analysis over all sales conversations → comprehensive purchase-blocker inventory → fragmented-feedback pie chart → core additions vs. reserve editions. The feedback organ of the living stack.

## Pre-Flight Gate

- Minimum ~10 recorded/logged sales conversations (calls, DMs, email threads). Fewer → note the sample-size caveat and treat outputs as provisional.
- Objections vs. delays are **categorically different** — the pipeline must keep them separate.

## Skill Acquisition

- `genius.md` — patterns 5/6/7 (objection conversion, pie-chart triage, offer layers)
- Current offer stack (from `/jh-offer-stack` blueprint or `/jh-offer-audit` inventory)

## Execution

1. **Sweep**: analyze every available transcript/thread. Extract each purchase-blocker verbatim, tagged OBJECTION (won't buy because X) or DELAY (will buy but after/if Y).
2. **Cluster + quantify**: group into named patterns; count frequency; render the pie chart (table with % is fine — the point is proportions, not the graphic). "What seemingly is randomness" becomes clarity only when quantified.
3. **Triage**:
   - **Majority slices** → CORE additions: design the component that dissolves the pattern pre-emptively, articulated inside the offer ("hey, by the way, we've got great capital partners..." — funding objection becomes a stack component, not a rebuttal).
   - **Fragment slices** → EDITIONS: reserve additions for the closer's pocket (feeds `/jh-offer-editions`).
   - **Noise** (one-offs) → logged, not acted on. Never let one loud prospect redesign the offer.
4. **Delay handling**: delays convert to timing/bridging components (pilots, phased starts, financing windows) — different design space than objection components.
5. **Draft the articulation update**: for each core addition, write the sentence the sales team/page now says, placed inside the offer presentation, not as a rebuttal script.

Execution prompt: references/prompts-v2/objection-to-component-pipeline.md — honor its Output Contract.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| No recordings, only CRM notes | Mine disposition notes + lost-deal reasons; label lower-fidelity |
| DM-close businesses | Threads are the transcripts; same pipeline |
| Recurring client cadence | Monthly run; diff against last month's pie — pattern GROWTH is the alarm |
| Pair with jeremy-miner NPQ | Miner handles the live conversation; this pipeline decides what stops needing handling |

## Output Requirements

Objection Mining Report: blocker inventory (verbatim, tagged), frequency table/pie, core additions with articulation sentences, editions list, noise log, sample-size caveat if applicable.

## Quality Gate

- Objections and delays never merged
- Every core addition tied to a majority-frequency pattern (percentage cited)
- Articulation sentences written (not "consider adding...")
- One-off anecdotes visibly quarantined in the noise log
