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

## Output Schema

- `metadata.json` — `{ video_id, url, caption_source, mode: "transcript", fetched_at }`.
- `transcript.txt` — cleaned, continuous, readable prose (VTT timing codes and duplicate lines stripped).
- `video-context-ledger.md` — a two-column-lane table: `Timestamp | Lane | Content`. Only `observed_spoken` and `uncertain_or_unavailable` rows are legal in this mode — a row in any other lane is a contract violation for this workflow specifically.
- `video-context-ledger.json` — machine-readable equivalent of the same rows.
- `analysis.md` — two required subsections: "What This Ledger Supports" (claims/frameworks/quotes drawn only from `observed_spoken` rows) and "What This Ledger Does Not Support" (any visual or on-screen-text claim, named explicitly out of scope for this mode).
- `uncertainty-report.md` — every caption gap or ambiguous segment, plus the standing note that no visual/OCR evidence was captured in Quick Transcript Ledger mode.

## Quality Gate

The ledger may contain `observed_spoken` and `uncertain_or_unavailable` rows. It must not make visual claims. Before handoff, confirm `video-context-ledger.md` contains zero `observed_visual` or `observed_onscreen_text` rows and that `uncertainty-report.md` explicitly flags the absence of visual/OCR evidence in this mode.
