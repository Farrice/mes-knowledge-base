---
description: "Prepare a YouTube video context ledger for /extract or /extract-forge"
---

# /video-source-extract

Turn a public YouTube URL into an extraction-ready source package.

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode full
python3 execution/verify_video_context_source_package.py "extractions/video-context/<video-id>"
```

Then route:

```bash
/extract-forge extractions/video-context/<video-id>/
```

Use `transcript.txt` as the clean human reading surface and `transcript_segments.json` plus `video-context-ledger.md` as timestamped evidence. Preserve `uncertain_or_unavailable` rows in downstream extraction notes.
