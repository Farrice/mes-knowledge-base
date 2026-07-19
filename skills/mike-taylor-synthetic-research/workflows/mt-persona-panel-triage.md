---
description: "/mt-persona-panel-triage — Mike Taylor's core two-step prompt: generate N distinct demographic personas, get each to answer the decision question independently, then aggregate into one joint-anonymous-answer verdict. The foundation every other workflow in this skill builds on."
---

# Persona Panel Triage

The move that replaces "the stock answer — kind of the average of the internet" with something that has actual range in it. Never ask the model the real question directly. Generate the panel first, get independent answers second, aggregate third — in that order, never collapsed into one instruction.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Patterns 1-5, Decision Framework) before executing.

> **Pre-Flight Gate**: Run Decision Framework Q1 — is the DECISION this panel needs to inform directional (headline, angle, early positioning smell test) or literal (a specific named individual's predicted action)? If literal, stop; this workflow isn't built for that — see `mt-distribution-calibration-check.md`.

## Input Required
- The product/brand (name it directly if well-known to the model; otherwise see Step 1 category-substitution)
- The decision question — the exact thing you want feedback on (copy variants, concept preference, positioning)
- Panel size (default 10 — his standard)
- Whether real customer transcripts exist for this audience (if yes, route to `mt-persona-grounding.md` instead — this workflow is the cold-generation/Tier-3 path)

## Workflow

### Step 1: Category Test
Is the brand/product well-known enough that the model likely has direct training data on its buyers? If yes, name it directly. If no ("if your product isn't as well known then you might need to describe what type of product you are"), substitute the product CATEGORY instead of the brand name — the model's category-level buyer knowledge is broader than its brand-specific knowledge.

### Step 2: Scene-Set (persona generation, standalone)
Issue this as its own instruction, not combined with the question:
> "Give me 10 demographic personas, just like regular people, who would be buyers of [PRODUCT/CATEGORY]."

Report the resulting persona list as a standalone finding before moving on — new segments the operator hadn't considered belong in the output even if they're not used downstream (Pattern 5).

### Step 3: Independent Critical Response
Issue the real question as a second instruction: "answer this question critically from their experience given their background." State the decision question plainly. Every persona answers independently — do not let one persona's answer visibly influence another's during generation (see `mt-distribution-calibration-check.md` for the isolation discipline when stakes are higher).

### Step 4: The Joint Anonymous Answer
Close with the exact aggregation phrase — do not paraphrase it loosely:
> "Combine all of those personas back into a single paragraph answer, as if these people had collaborated in writing a joint anonymous answer."

### Step 5: Report Dissent, Don't Bury It
Before the aggregate, note where individual personas split by role (e.g., a startup-founder persona favoring one option, a marketing-manager persona favoring another). The aggregate paragraph is the deliverable; the dissent underneath it is what makes the aggregate trustworthy rather than a second stock answer.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| Landing page / ad copy variants | Decision question = "which of these two versions do you prefer and why" |
| Concept / positioning smell test | Decision question = "does this positioning resonate, and why or why not" |
| Feature / product idea | Decision question = "would you use this, and what would need to be true for you to pay for it" |
| Latent-demand scan | Route to `mt-latent-demand-mining.md` instead — different prompt shape, not a preference test |

## Output Format
```
PERSONA PANEL TRIAGE — [product/decision] — [date]
GROUNDING TIER: 3 (cold-generated, no real customer data) — see mt-persona-grounding.md to upgrade

PERSONA LIST (standalone finding)
1. [Role] — [1-line descriptor]
... (up to panel size)
New segment ideas surfaced: [any personas that reframe targeting]

INDIVIDUAL DISSENT (by role)
[Role]: [position + one-line reasoning]
[Role]: [position + one-line reasoning]
...

JOINT ANONYMOUS ANSWER
[the aggregated paragraph, in the personas' collective voice]

DIRECTIONAL VERDICT: [which option wins, approximate split if discernible]
NEXT STEP: [AB test before spend | escalate to mt-persona-grounding.md if transcripts exist | escalate to real research per mt-synthetic-vs-real-decision.md if stakes warrant]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] Persona generation and the real question were two separate instructions, never combined
- [ ] The persona list is reported as a standalone finding, not just scaffolding
- [ ] The exact "joint anonymous answer" phrase was used for aggregation
- [ ] Individual dissent is visible before the aggregate, not smoothed away
- [ ] Grounding tier (3, cold-generated) is stated explicitly
- [ ] Output names a next step — AB test, grounding upgrade, or real research — never presents itself as final

## Common Pitfalls
- **Skipping the scene-set.** Asking the question with personas named inline in one sentence collapses back toward the stock-answer problem.
- **Averaging away the dissent.** The aggregate is supposed to synthesize disagreement, not erase the fact that disagreement existed.
- **Treating a Tier-3 panel like a Tier-1 one.** Cold-generated panels are directional hunches, not validated research — say so.

Execution prompt: `references/prompts-v2/persona-panel-triage.md`
