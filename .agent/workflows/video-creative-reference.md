---
description: "Break down video creative references; on-demand content analyst for taste, extraction, adaptation and bounded batch planning"
---

# /video-creative-reference

Create or use a video context package, then extract creative reference notes grounded in observed evidence.

For **content analyst**, batch analysis, taste learning, original adaptation or
explicit spending-control requests, first read
`skills/youtube-video-context-analysis/references/content-analyst-pilot.md` and its
execution prompt. This opt-in pilot is offline; it does not authorize Gemini,
Whisper, paid discovery or uploads. Existing source evidence can be used now.
Execution prompt: `skills/youtube-video-context-analysis/references/prompts-v2/content-analyst.md`.
For ordinary single-video work, the existing path below is unchanged.

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode full
```

Keep visual proof tied to frames, OCR, human notes, or vision output.

