---
name: "Mike Taylor — Personalized Message Cascade"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running Mike Taylor's post-validation personalization discipline: "I use this more for insights in general... and then once I understand the angle of attack, then I'll kind of write it myself." This workflow mines the AI's draft for the angle that made it specific to one recipient — it never ships that draft as finished copy.

## Input Required

- [VALIDATED_MESSAGE]: a top-level message/offer already validated via persona-panel-triage or concept-headline-triage
- [GROUNDING]: transcript-grounded panel context if available, otherwise persona-based
- [RECIPIENT]: the specific individual or segment to personalize for

## Execution Protocol

**Step 1 — Confirm validation.** State [VALIDATED_MESSAGE] and confirm it was already validated elsewhere. Do not generate a new top-level message here.

**Step 2 — Personalization prompt.** "Write a personalized [email/message] to [RECIPIENT] telling them about [VALIDATED_MESSAGE]."

**Step 3 — Extract the angle.** Read the draft for what made it specific to [RECIPIENT] — the concern, phrase, or framing that differs from a generic version. That angle is the deliverable, not the literal sentences.

**Step 4 — Human-written final.** Write the actual outreach informed by the extracted angle. Label it explicitly as human-written, distinct from the AI draft.

**Step 5 — Segment discipline.** If this needs to scale beyond one recipient, generalize the angle into a segment template rather than re-running per individual at mass scale.

## Output Contract

- Validated top-level message stated
- AI draft labeled angle-discovery only
- Extracted angle named specifically
- Human-written final, distinguished from the draft
- Segment-scaling guidance if relevant

## Output Skeleton

```
PERSONALIZED MESSAGE CASCADE — [recipient/segment] — [date]
VALIDATED TOP-LEVEL MESSAGE: [...]
GROUNDING: [transcript-grounded / persona-based]

AI DRAFT (angle-discovery only, not final)
[draft]

EXTRACTED ANGLE: [specific concern/phrase/framing]

HUMAN-WRITTEN FINAL
[shipped copy]
```

## Quality Gate

- Top-level message was already validated, not generated fresh here
- AI draft explicitly labeled angle-discovery, never final
- Extracted angle is specific, not "make it more personal"
- Human-written final exists and is distinguished from the draft
- Not run per-individual at mass scale without segment templating

## Deploy When

A validated message/offer needs individual or segment-level positioning for high-value outreach — never for mass-personalizing hundreds of emails per-recipient.
