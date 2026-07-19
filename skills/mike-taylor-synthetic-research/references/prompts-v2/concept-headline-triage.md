---
name: "Mike Taylor — Concept / Headline Triage"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running the exact demo that produced "Grow without the guesswork" beating HubSpot's incumbent headline roughly 60/40, with attributed reasoning. This is the fastest deployment of Mike Taylor's core mechanism — built for real, already-written copy/concept variants that need a directional read before spend, not a research-design exercise.

## Input Required

- [VARIANTS]: 2-4 real copy/concept variants, in full — never a request to generate options here
- [PRODUCT_OR_BRAND]: named directly, or [PRODUCT_CATEGORY] if unknown to the model
- [AUDIENCE]: who the copy targets

## Execution Protocol

**Step 1 — Generate the panel.** "Give me 10 demographic personas... who would be buyers of [PRODUCT_OR_BRAND/CATEGORY]."

**Step 2 — Direct comparison ask.** Present [VARIANTS] verbatim: "What [headline/copy/concept] do you like the best: [Variant A] or [Variant B]?" Each persona answers critically from their background.

**Step 3 — Individual verdicts, attributed.** Capture each persona's preference and stated reasoning by role.

**Step 4 — Joint anonymous aggregate.** Close with the exact aggregation phrase. Report the approximate split alongside the synthesized reasoning.

**Step 5 — AB-test discipline.** State explicitly: this is a directional read; real spend still closes with a real AB test.

## Output Contract

- Grounding tier stated
- All variants listed verbatim
- Per-role attributed verdicts with reasoning
- Approximate split
- Joint anonymous answer
- Explicit AB-test-before-spend next step

## Output Skeleton

```
CONCEPT/HEADLINE TRIAGE — [product] — [date]
GROUNDING TIER: [1/2/3]
VARIANTS: A) [...] B) [...] [C/D if applicable]

PERSONA VERDICTS (attributed)
[Role]: prefers [Variant] — "[reasoning]"
[...]

APPROXIMATE SPLIT: [n of N] favored [Variant]

JOINT ANONYMOUS ANSWER
[synthesized paragraph]

DIRECTIONAL VERDICT: [Variant] — directional hunch, not validated
NEXT STEP: AB test before committing spend/launch.
```

## Quality Gate

- Real variants used, never generated inside this workflow
- Individual verdicts attributed by role with real reasoning
- Exact joint-anonymous-answer phrase used
- AB testing (or equivalent) named as the explicit next step

## Deploy When

Real copy/concept variants already exist and need a fast directional read before committing spend or launch.
