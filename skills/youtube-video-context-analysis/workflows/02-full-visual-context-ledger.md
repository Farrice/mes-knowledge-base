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

## Output Schema

- `metadata.json`, `transcript.vtt` (if available), `transcript.txt`, `transcript_segments.json` (timestamped spoken-evidence segments).
- `frames/` — sampled frame images, when frame extraction succeeded.
- `frame-notes.md` — human/reviewed notes per sampled frame.
- `ocr-notes.md` — OCR output per frame, or an explicit note that OCR was unavailable.
- `video-context-ledger.md` / `video-context-ledger.json` — a four-column table (`Timestamp | Lane | Content | Source`) across all five evidence lanes: `observed_spoken`, `observed_visual`, `observed_onscreen_text`, `inferred_context`, `uncertain_or_unavailable`. Every `observed_visual` and `observed_onscreen_text` row must carry a `Source` value that names the frame index, human reviewer, or vision-adapter — never "transcript."
- `analysis.md` — two required subsections: "Cross-Channel Findings" (where spoken, visual, and OCR evidence agree, disagree, or are silent) and "Extraction Handshake" (which lanes/rows are ready for `/extract`, `/extract-forge`, research, content, creative, or audit use).
- `uncertainty-report.md` — one entry per tool/lane limitation: `[tool/lane]: [what failed or was unavailable, and what it blocks downstream]`.

## Quality Gate

Before reuse, open `uncertainty-report.md` and confirm the visual/OCR limitations are acceptable for the job. Also confirm: all five lanes are present and never mixed within a single row, every `observed_visual`/`observed_onscreen_text` row cites an actual frame/OCR pass/human note/vision-adapter output, and `analysis.md` names a clear extraction handshake per lane.
