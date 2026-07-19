---
description: "/mt-concept-headline-triage — the exact HubSpot demo shape: 2 (or more) copy/concept variants scored by a persona panel, individual dissent preserved by role, aggregated to a directional verdict with the model's own reasoning. Fastest deployment of the core mechanism."
---

# Concept / Headline Triage

The workflow that produced "Grow without the guesswork" beating the incumbent headline ~60/40, with reasons attached. This is the tightest, fastest application of the core panel mechanism — built for the moment you have 2-4 real copy or concept variants and need a directional read before spend, not a philosophy of research design.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Patterns 1-5, Exemplar 1).

> **Pre-Flight Gate**: This workflow needs REAL variants already written — not a request to "generate some headline options." If variants don't exist yet, write them first (route to the relevant copy skill), then bring them here for the triage.

## Input Required
- 2-4 real copy/concept variants, in full (never summarized)
- The product/brand (or category if unknown to the model — Pattern 4)
- The audience the copy targets

## Workflow

### Step 1: Generate the Panel
Standard scene-set: "give me 10 demographic personas... who would be buyers of [product/category]."

### Step 2: The Direct Comparison Ask
Present all variants verbatim and ask: "What [landing page copy / headline / concept] do you like the best: [Variant A] or [Variant B]?" Each persona answers critically from their background — never a generic "which is better."

### Step 3: Individual Verdicts, Attributed
Capture each persona's preference and their stated reasoning, attributed by role. This is where the real signal lives — a marketing-manager persona favoring the safe incumbent and a startup-founder persona favoring the challenger line isn't noise, it's a segmentation finding.

### Step 4: Joint Anonymous Aggregate
Close with the exact aggregation instruction (Pattern 2). Report the approximate split if the personas' preferences are countable (e.g., "6 of 10 leaned toward Variant B") alongside the synthesized reasoning paragraph.

### Step 5: The AB-Test Discipline
Never present the aggregate as the final answer. State explicitly: this is a directional read; the actual decision closes with a real AB test if the stakes (traffic, spend, launch) warrant one.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| Landing page headline (2 variants) | Direct application, as demonstrated |
| Ad copy (3-4 variants) | Same shape, report full ranking not just a winner |
| Positioning statement / tagline | Same shape; weight Identity Signal-style reasoning ("what does this say about the buyer") if paired with Meg Heckman's trigger vocabulary for physical products |
| Email subject line | Same shape; note open-rate is the real-world validation step, equivalent to the AB test |
| Thumbnail/hook concept (paired with content workflows) | Same shape; Social Currency-style reasoning (would they share/react) supplements preference alone |

## Output Format
```
CONCEPT/HEADLINE TRIAGE — [product] — [date]
GROUNDING TIER: [1/2/3]
VARIANTS: A) [...] B) [...] [C/D if applicable]

PERSONA VERDICTS (attributed)
[Role]: prefers [Variant] — "[reasoning in their voice]"
...

APPROXIMATE SPLIT: [n of N] favored [Variant]

JOINT ANONYMOUS ANSWER
[synthesized paragraph explaining the directional preference and why]

DIRECTIONAL VERDICT: [Variant] — [confidence: directional hunch, not a validated result]
NEXT STEP: AB test before committing spend/launch — this triage narrows the field, it doesn't close the decision.
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] Real variants were used, never a request to generate options inside this workflow
- [ ] Individual verdicts are attributed by role with real stated reasoning, not just a tally
- [ ] The exact joint-anonymous-answer aggregation phrase was used
- [ ] Output explicitly names AB testing (or equivalent real validation) as the next step, never presents the triage as final

## Common Pitfalls
- **Skipping straight to the aggregate.** The per-role dissent is the actual insight (who likes which variant and why); the aggregate alone loses the segmentation finding.
- **Treating the directional split as a statistically valid result.** It's a fast, cheap hunch — real spend still needs a real test.
- **Running this before variants exist.** This is a triage tool, not a copy generator — bring finished options to it.

Execution prompt: `references/prompts-v2/concept-headline-triage.md`
