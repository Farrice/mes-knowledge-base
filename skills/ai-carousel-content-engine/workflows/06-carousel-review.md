---
description: "Review carousel copy and generated design for source fidelity, text accuracy, brand fit, and CTA strength"
---

# Carousel Review

Read `review-checklist.md`, `carousel-script.md`, and `gpt-image-2-prompt.json`.

Check:

- hook strength
- slide fit
- text accuracy
- visual cohesion
- brand fit
- CTA clarity
- source fidelity

## Output Schema

The seven-point pass/fail check listed above, plus the three-domain checklist (copy / design / evidence-and-strategy), an explicit failure-condition scan (hidden-prompt implication, generic "viral" wording, copy too long for a slide, missing/dead-end CTA), and a repair-notes section naming, for every failed item, the slide number, what's wrong, and the specific fix. Full contract: `references/prompts-v2/carousel-review-repair.md`.

## Quality Gate

- Every checklist item carries an actual pass/fail judgment — no blank item or default pass.
- Every failed item has a specific, slide-numbered repair note, not a vague flag.
- Source fidelity is re-checked against the actual source material, not asserted without comparison.
- The failure-condition scan explicitly addresses hidden-prompt implication, even when the answer is "none found."
- A zero-issue review states that explicitly rather than leaving the result ambiguous.
