---
description: "Create a timestamped YouTube context ledger with transcript, frames, OCR fallback, analysis, and uncertainty"
---

# /video-context-ledger

Create a full YouTube video context package.

## Steps

1. Load `skills/youtube-video-context-analysis/SKILL.md`.
2. Run:
   ```bash
   python3 execution/video_context_ledger.py "<youtube-url>" --mode full
   ```
3. Review `extractions/video-context/<video-id>/uncertainty-report.md`.
4. Use `video-context-ledger.md` as the reusable source for extraction, strategy, creative analysis, or audit work.

