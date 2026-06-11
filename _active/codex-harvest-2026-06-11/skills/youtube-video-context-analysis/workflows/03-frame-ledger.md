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

## Quality Gate

Frame rows prove that a sampled image exists at a timestamp. They do not prove what is inside the frame until reviewed by a human, OCR, or vision adapter.

