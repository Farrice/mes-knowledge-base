---
description: "Create a transcript-only YouTube evidence ledger with metadata, cleaned captions, and uncertainty"
---

# /video-transcript-ledger

Create a fast transcript-ledger package without claiming visual evidence.

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode transcript
python3 execution/verify_video_context_source_package.py "extractions/video-context/<video-id>"
```

Use when the user needs a quick spoken-evidence source for `/extract`, `/extract-forge`, content, or research.

The package must include raw `transcript.vtt`, clean `transcript.txt`, timestamped `transcript_segments.json`, metadata, ledger, and uncertainty report. Do not treat row-shaped ledger evidence as the main transcript.
