---
description: "Turn a YouTube context package into an extraction-ready source map"
---

# Source-To-Skill Extract

Use this before `/extract` or `/extract-forge` when the source is a YouTube video.

## Run Order

```bash
/video-context-ledger <youtube-url>
/extract-forge extractions/video-context/<video-id>/video-context-ledger.md
```

## Extraction Notes

- Use `observed_spoken` rows for claims, frameworks, and phrasing.
- Use `observed_visual` rows for demos, slides, settings, edits, and product state only when actually reviewed.
- Use `observed_onscreen_text` rows for slide titles, UI labels, charts, and shown claims.
- Preserve `uncertain_or_unavailable` rows in extraction notes.

## Output Schema

A single "Source-to-Skill Extraction Map — [video title / id]" document, structured by routed source class, each entry citing the ledger row/timestamp it came from:

```
## Run Order
1. /video-context-ledger [YOUTUBE_URL]
2. /extract-forge extractions/video-context/[video-id]/video-context-ledger.md

## Claims, Frameworks, Phrasing (from observed_spoken)
- [row/timestamp]: [what it supports in the extraction target]

## Visual Proof, Demo Steps, Product State (from observed_visual, reviewed only)
- [row/timestamp]: [what it supports]

## On-Screen Claims, Slide/UI Labels (from observed_onscreen_text)
- [row/timestamp]: [what it supports]

## Inference — Labeled, Not Verified (from inferred_context)
- [row/timestamp]: [hypothesis or strategic read, explicitly marked as not directly observed]

## Carried-Forward Limitations (from uncertain_or_unavailable)
- [row/timestamp]: [what this blocks the extraction target from claiming]
```

## Quality Gate

The future skill must not depend on visual assumptions that the ledger did not verify. Before handoff, confirm: every routed item cites the row/timestamp it came from, `observed_visual` items are limited to actually-reviewed rows (unreviewed demo steps flagged as gaps instead), every `inferred_context` item is explicitly labeled as inference, and all `uncertain_or_unavailable` rows are carried forward rather than dropped.
