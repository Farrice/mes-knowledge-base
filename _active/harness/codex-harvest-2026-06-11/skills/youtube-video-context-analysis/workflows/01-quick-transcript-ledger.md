---
description: "Create metadata, cleaned transcript, spoken-evidence ledger, and uncertainty report from a YouTube URL"
---

# Quick Transcript Ledger

Use this when speed matters or visual tooling is unnecessary.

## Run

```bash
python3 execution/video_context_ledger.py "<youtube-url>" --mode transcript
```

## Output

- `metadata.json`
- `transcript.vtt` when captions are available
- `transcript.txt`
- `video-context-ledger.md`
- `video-context-ledger.json`
- `analysis.md`
- `uncertainty-report.md`

## Quality Gate

The ledger may contain `observed_spoken` and `uncertain_or_unavailable` rows. It must not make visual claims.

