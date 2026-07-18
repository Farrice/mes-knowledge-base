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

## Output Schema

- `ocr-notes.md` — one entry per OCR-attempted frame, including explicit null/unavailable states:
  ```
  ## Frame [timestamp]
  - OCR status: [detected / nothing detected / tool unavailable]
  - Extracted text: [exact text, or "none"]
  - Element type: [slide title / UI label / chart label / lower-third / ad copy / caption]
  ```
  Plus a trailing `## Tool-Level Notes` entry covering OCR tool availability, run scope, and any systematic gaps (low-contrast text, non-Latin script, motion blur).
- Corresponding `observed_onscreen_text` and `uncertain_or_unavailable` rows feeding `video-context-ledger.md` / `video-context-ledger.json`. Extracted text must be reported verbatim, never paraphrased.

## Quality Gate

If OCR tooling is unavailable or detects nothing, the output must say so. Do not replace OCR with guesses. Before handoff, confirm: every OCR-attempted frame has an entry (including "nothing detected" / "tool unavailable"), extracted text is verbatim, and OCR rows stay in their own lane rather than merging into spoken or inferred rows.
