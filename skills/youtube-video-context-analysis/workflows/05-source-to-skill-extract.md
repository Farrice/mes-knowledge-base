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

## Quality Gate

The future skill must not depend on visual assumptions that the ledger did not verify.

