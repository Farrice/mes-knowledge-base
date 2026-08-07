# Uncertainty Report

## Evidence Counts
- `inferred_context`: 0
- `observed_onscreen_text`: 0
- `observed_spoken`: 6
- `observed_visual`: 3
- `uncertain_or_unavailable`: 1

## Limitations
- OCR unavailable: tesseract/pytesseract not installed or not configured.

## Evidence Rule
Inferred context must not be merged into observed rows. Visual claims require a frame, OCR result, human note, or vision adapter output.
