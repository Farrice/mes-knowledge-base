---
name: "Mike Taylor — Persona Panel Triage"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running Mike Taylor's core synthetic-research mechanism — co-author, O'Reilly's *Prompt Engineering for Generative AI*; co-founder, Ask Rally. A direct question to a chatbot returns "the stock answer — kind of the average of the internet" because a single model instance answering as itself has no structural reason to disagree with itself. Instead: generate a panel of distinct personas, get each to answer the real question independently, then instruct the model to combine those answers "as if these people had collaborated in writing a joint anonymous answer." This is a cold-generated (Tier 3) panel — a fast directional instrument, never a validated research result.

## Input Required

- [PRODUCT_OR_BRAND]: name directly if well-known to the model; otherwise describe the [PRODUCT_CATEGORY] instead
- [DECISION_QUESTION]: the exact thing you want feedback on
- [PANEL_SIZE]: default 10
- [AUDIENCE_CONTEXT]: anything else the personas should be aware of

## Execution Protocol

**Step 1 — Category test.** Decide: is [PRODUCT_OR_BRAND] well-known enough that the model likely has direct buyer-behavior training data on it? If not, substitute [PRODUCT_CATEGORY] — the model's category-level buyer knowledge is broader than its brand-specific knowledge.

**Step 2 — Scene-set (standalone instruction, never combined with the question).** Generate exactly [PANEL_SIZE] demographic personas — "just like regular people who would be buyers of [PRODUCT_OR_BRAND / PRODUCT_CATEGORY]." Report this list as a standalone finding: note any segment that reframes targeting, even if unused downstream.

**Step 3 — Independent critical response.** As a second, separate instruction, pose [DECISION_QUESTION] and require each persona to "answer this question critically from their experience given their background." Every persona answers independently — do not let earlier personas' answers visibly steer later ones.

**Step 4 — The joint anonymous answer.** Close with the exact aggregation phrase, never paraphrased: "Combine all of those personas back into a single paragraph answer, as if these people had collaborated in writing a joint anonymous answer."

**Step 5 — Report dissent before the aggregate.** List where personas split by role and why, before presenting the synthesized paragraph — the dissent is what makes the aggregate trustworthy rather than a second stock answer.

## Output Contract

- Grounding tier stated (Tier 3, cold-generated)
- Full persona list as a standalone finding, with any new-segment ideas flagged
- Per-role dissent, attributed, with reasoning
- The joint anonymous answer, verbatim aggregation framing
- A directional verdict, never presented as final
- An explicit next step (AB test / grounding upgrade / real-research escalation)

## Output Skeleton

```
PERSONA PANEL TRIAGE — [product/decision] — [date]
GROUNDING TIER: 3 (cold-generated, no real customer data)

PERSONA LIST (standalone finding)
1. [Role] — [1-line descriptor]
[... up to PANEL_SIZE]
New segment ideas surfaced: [...]

INDIVIDUAL DISSENT (by role)
[Role]: [position] — "[reasoning]"
[...]

JOINT ANONYMOUS ANSWER
[synthesized paragraph]

DIRECTIONAL VERDICT: [which option/finding wins, approximate split if countable]
NEXT STEP: [AB test | mt-persona-grounding.md if transcripts exist | mt-synthetic-vs-real-decision.md if stakes warrant]
```

## Quality Gate

- Persona generation and the real question were two separate instructions
- Persona list reported as a standalone finding, not just scaffolding
- Exact "joint anonymous answer" phrase used
- Individual dissent visible before the aggregate
- Grounding tier stated explicitly
- Output names a concrete next step, never presents itself as final

## Deploy When

A directional read is needed fast on a decision question with no existing real customer transcripts, before any real research spend.
