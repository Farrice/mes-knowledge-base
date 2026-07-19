---
description: "/mt-latent-demand-mining — surface unmet pain/need (not a preference between two options) via a persona panel, then drill one level deeper on the single most interesting finding. Mike Taylor's product-opportunity discovery loop."
---

# Latent Demand Mining

A different prompt shape from the headline/concept triage — this one hunts for the problem people haven't named as a product opportunity yet, then goes one layer deeper on whatever the panel surfaces as most interesting. One pass finds the pain; a second, targeted pass finds the product.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Pattern 13).

> **Pre-Flight Gate**: This is a discovery workflow, not a validation workflow — don't run it with a product already fixed in mind. If a specific product/feature already exists and needs a preference test, use `mt-persona-panel-triage.md` or `mt-concept-headline-triage.md` instead.

## Input Required
- The market/audience to mine (as specific as possible — "small business owners running an agency" beats "small business owners")
- Whether real customer transcripts exist for this audience (grounds the mining; route through `mt-persona-grounding.md`'s loading step first if so)
- Any prior hypothesis about pain points (optional — don't let it bias the panel's first pass)

## Workflow

### Step 1: Generate the Panel (same scene-set discipline as Pattern 3)
Standard persona generation for the audience (`mt-persona-panel-triage.md` Step 2), or transcript-grounded (`mt-persona-grounding.md`) if real data exists.

### Step 2: The Latent-Demand Prompt (distinct from a preference ask)
Issue the pain-mining question, not a preference question:
> "For [the persona/audience], what are the most pressing problems?"

This is structurally different from "which do you prefer" — it has no options to choose between, only pain to surface. Let each persona answer independently before any aggregation.

### Step 3: Surface Scan — Report the Full Spread
List every distinct pain point that surfaced across the panel, even ones that seem minor or off-topic. The point of this pass is breadth, not a single winner yet.

### Step 4: Pick the Single Most Interesting Finding
Choose ONE finding — the one with the strongest signal (recurs across personas, ties to a real stated frustration pattern, or surfaces something the operator hadn't considered). Name why it was chosen over the others.

### Step 5: The Drill-Down Pass
Re-run the panel, narrowed to that one finding:
> "What are the real specific set of problems, and what are possible products that would help address these problems?"

This second pass converts a surfaced pain point into a shape of a possible product or offer — the actual opportunity, not just the symptom.

### Step 6: Reality-Check the Finding
Note whether this pain point is: (a) something the panel invented with no real-world corroboration (Tier 3 risk — cold-generated panels can hallucinate plausible-sounding pain), or (b) something that shows up in real forums/reviews/transcript data if you have it. Flag which.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| New product/course opportunity scan | Direct application, as above |
| Feature-gap analysis on an existing product | Narrow the audience to current customers; ground with real transcripts if available (`mt-persona-grounding.md`) |
| Content/topic ideation | Pain points map directly to content angles — "the problem nobody's addressing" becomes the content hook |
| Positioning gap-finding | Latent-demand findings feed a repositioning brief — what's unmet becomes the new promise |

## Output Format
```
LATENT DEMAND MINING — [audience] — [date]
GROUNDING TIER: [1/2/3, per genius.md Grounding Ladder]

SURFACE SCAN (breadth pass)
1. [pain point] — surfaced by [which persona roles]
2. [pain point] — surfaced by [which persona roles]
...

SELECTED FINDING: [pain point] — chosen because [recurrence/signal strength/novelty reasoning]

DRILL-DOWN
Specific problems: [...]
Possible products/offers: [...]

REALITY CHECK: [corroborated by real data | Tier-3 hallucination risk flagged, needs real-world validation before spend]
NEXT STEP: [validate against real forums/reviews/customer data | mt-concept-headline-triage.md once a concept exists | escalate to real research if stakes warrant]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] The pain-mining prompt was used, not a disguised preference question
- [ ] Breadth pass reported all distinct findings before narrowing to one
- [ ] Selection reasoning for the chosen finding is explicit, not arbitrary
- [ ] Drill-down pass produced specific problems + possible products, not a restated summary
- [ ] Grounding tier stated, and Tier-3 hallucination risk flagged if no real corroboration exists

## Common Pitfalls
- **Fixing the product before mining.** Kills the discovery function — this workflow exists to find the opportunity, not confirm one already chosen.
- **Stopping at the surface scan.** "Cash flow was king" is a symptom; the drill-down is where the actual product shape appears.
- **Treating a cold-generated pain point as validated demand.** A Tier-3 panel can invent a plausible-sounding problem nobody actually has — corroborate before spending against it.

Execution prompt: `references/prompts-v2/latent-demand-mining.md`
