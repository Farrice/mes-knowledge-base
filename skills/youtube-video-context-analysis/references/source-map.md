# Video Context Source Map

Use this source map when converting a video ledger into another Antigravity workflow.

## Source Classes

| Source Class | Comes From | Can Support |
|---|---|---|
| Spoken evidence | Caption/subtitle transcript | claims, frameworks, examples, quotes, content hooks |
| Frame evidence | Extracted frame image or human/vision note | visual proof, demo steps, setting, composition, product state |
| OCR evidence | Text extracted from frames | slide titles, UI labels, chart labels, claims shown on screen |
| Inferred context | Analyst synthesis | hypotheses, strategy, creative interpretation |
| Uncertainty | Failed or unavailable adapter | limitations, follow-up tasks, audit flags |

## Downstream Routing

- Source-to-skill: feed `video-context-ledger.md` and `analysis.md` into `/extract` or `/extract-forge`.
- Creative reference: use frame notes and OCR rows before visual style inference.
- Claim audit: compare `observed_spoken` with `observed_visual` and `observed_onscreen_text`.
- Tutorial extraction: use spoken steps, visible UI state, and OCR labels as separate rows.
- Ads/reference breakdown: separate message, visual proof, edits, product shots, and inferred strategy.

