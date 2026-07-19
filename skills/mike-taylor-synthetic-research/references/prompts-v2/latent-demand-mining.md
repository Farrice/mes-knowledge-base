---
name: "Mike Taylor — Latent Demand Mining"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running Mike Taylor's product-opportunity discovery loop — a pain-mining pass, not a preference test. The prompt shape is different from a headline triage: it asks what hurts, not which option wins, then drills one layer deeper on whichever finding shows the strongest signal.

## Input Required

- [AUDIENCE]: the market/segment to mine, as specific as possible
- [GROUNDING]: real customer transcripts if available (route through persona-grounding's loading step first), otherwise cold-generated
- [PRIOR_HYPOTHESIS]: optional — do not let it bias the first pass

## Execution Protocol

**Step 1 — Generate the panel.** Standard scene-set persona generation for [AUDIENCE] (or transcript-grounded, per [GROUNDING]).

**Step 2 — The latent-demand prompt.** Ask: "For [AUDIENCE], what are the most pressing problems?" — never a preference question. Independent answers per persona.

**Step 3 — Surface scan.** List every distinct pain point that surfaced, including minor or off-topic ones. Breadth first, no winner picked yet.

**Step 4 — Select the single most interesting finding.** Choose ONE — strongest recurrence, ties to real stated frustration, or genuinely novel — and state why it was chosen over the others.

**Step 5 — Drill-down pass.** Re-run the panel narrowed to that finding: "What are the real specific set of problems, and what are possible products that would help address these problems?"

**Step 6 — Reality-check.** Flag whether the finding is corroborated by real data (forums, reviews, transcripts) or is a Tier-3 cold-generation risk that could be a plausible-sounding hallucination.

## Output Contract

- Grounding tier stated
- Full breadth-pass list, not just the winner
- Explicit selection reasoning
- Drill-down: specific problems + possible products
- Reality-check flag (corroborated vs. hallucination risk)
- Next step named

## Output Skeleton

```
LATENT DEMAND MINING — [audience] — [date]
GROUNDING TIER: [1/2/3]

SURFACE SCAN
1. [pain point] — surfaced by [roles]
[...]

SELECTED FINDING: [pain point] — chosen because [reasoning]

DRILL-DOWN
Specific problems: [...]
Possible products/offers: [...]

REALITY CHECK: [corroborated | Tier-3 hallucination risk flagged]
NEXT STEP: [validate against real data | mt-concept-headline-triage.md once a concept exists | escalate if stakes warrant]
```

## Quality Gate

- Pain-mining prompt used, not a disguised preference question
- Full breadth pass reported before narrowing
- Selection reasoning explicit
- Drill-down produced specific problems + possible products, not a restatement
- Reality-check flag present

## Deploy When

Discovering an unmet need or product opportunity in a market/audience — never when a product is already fixed and just needs validation (use persona-panel-triage or concept-headline-triage instead).
