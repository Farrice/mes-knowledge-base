---
description: "Create a transcript, frame, OCR, analysis, and uncertainty package from a YouTube URL"
---

# Full Visual Context Ledger

Use this for interviews, tutorials, screen recordings, lectures, ads, demos, and creative references where visuals matter.

## Run

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode full
```

## Evidence Rules

- Spoken evidence comes from captions/subtitles.
- Visual evidence comes from extracted frames or explicit visual notes.
- On-screen text comes from OCR.
- Missing tools become `uncertain_or_unavailable` rows.
- Inference never becomes observed evidence.

## Quality Gate

Before reuse, open `uncertainty-report.md` and confirm the visual/OCR limitations are acceptable for the job.

