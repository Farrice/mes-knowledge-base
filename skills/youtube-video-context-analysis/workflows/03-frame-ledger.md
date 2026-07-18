---
description: "Sample frames and create frame notes without pretending to describe visuals automatically"
---

# Frame Ledger

Use this when a video needs visual inspection, scene references, slide capture, or demo-state review.

## Run

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode full --interval 60
```

## Review

Inspect `frames/` and `frame-notes.md`. Add human visual notes only as explicitly reviewed evidence. Do not infer visual content from transcript.

## Output Schema

- `frames/` — the sampled frame images, one per sampled timestamp, or an explicit note that extraction failed and why.
- `frame-notes.md` — one entry per reviewed frame:
  ```
  ## Frame [timestamp]
  - Review method: [human / vision adapter / not yet reviewed]
  - Observed: [scene, slide, UI state, product, composition — only what was actually seen]
  - Confidence: [reviewed in full / partial / illegible]
  ```
  Plus a trailing `## Unreviewed / Failed Samples` section listing `[timestamp]: [why]` for any frame that was sampled but never reviewed, or that failed to extract.
- Corresponding `observed_visual` (reviewed frames only) and `uncertain_or_unavailable` (unreviewed/failed frames) rows feeding `video-context-ledger.md` / `video-context-ledger.json`.

## Quality Gate

Frame rows prove that a sampled image exists at a timestamp. They do not prove what is inside the frame until reviewed by a human, OCR, or vision adapter. Before handoff, confirm: every `observed_visual` row names a review method rather than asserting content with no reviewer, zero visual content is inferred purely from what the transcript describes as on screen, and thumbnails/titles/descriptions are kept out of the frame-evidence lane entirely.
