---
description: "Extract on-screen text from sampled frames when OCR tooling is available"
---

# Visual OCR

Use this for slides, tutorials, screen recordings, UI walkthroughs, charts, and ad text.

## Run

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode full
```

## Review

Read `ocr-notes.md` and `video-context-ledger.md` for `observed_onscreen_text` rows.

## Quality Gate

If OCR tooling is unavailable or detects nothing, the output must say so. Do not replace OCR with guesses.

