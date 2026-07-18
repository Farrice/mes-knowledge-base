---
description: "Analyze a video as a creative reference without inventing unseen visuals"
---

# Creative Reference Breakdown

Use this for ads, brand films, creator references, product demos, edits, sets, wardrobes, layouts, and visual emphasis.

## Run Order

```bash
/video-context-ledger <youtube-url>
/creative-review extractions/video-context/<video-id>/
```

## Breakdown Lanes

- Spoken positioning and message.
- Verified frame references.
- OCR-visible text.
- Inferred creative strategy.
- Unverified visual assumptions.

## Output Schema

A "Creative Reference Breakdown — [video title / id]" document tied to the stated creative goal:

```
Creative goal: [CREATIVE_GOAL]

## Spoken Positioning & Message
[what the video claims/promises, in its own language, with row/timestamp citations]

## Verified Frame References
[composition, setting, wardrobe, product state, pacing, color/lighting — only from reviewed frames, with citations; state plainly if this lane is empty]

## OCR-Visible Text
[exact on-screen copy, captions, lower-thirds, slide/chart text, with citations]

## Inferred Creative Strategy
[the sharpest, most useful read of what strategy/choice this reflects — clearly labeled as inference]

## Unverified Visual Assumptions
- [open question a creative reviewer would want answered, explicitly not guessed at]
```

Verified frame/OCR lanes must cite actual reviewed rows. The Inferred Creative Strategy lane is where creative judgment is allowed to stretch — name the specific mechanism (contrast cutting, product-as-hero framing, testimonial stacking) rather than a vague "good branding" — but it stays clearly labeled as inference, never blended into the verified lanes.

## Quality Gate

Creative inspiration can be inferred, but visual proof must stay tied to reviewed frames or OCR. Before handoff, confirm: Verified Frame References is populated only from actually-reviewed evidence (left explicitly empty when no review happened), thumbnails/titles/descriptions are excluded from the verified lanes, and Unverified Visual Assumptions reads as open questions rather than answers dressed as findings.
