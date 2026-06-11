# Uncertainty Report

## Evidence Counts
- `inferred_context`: 0
- `observed_onscreen_text`: 0
- `observed_spoken`: 626
- `observed_visual`: 0
- `uncertain_or_unavailable`: 2

## Acquisition Log

- Initial sandboxed YouTube fetch failed because `www.youtube.com` DNS resolution was unavailable.
- Escalated network retry succeeded and produced metadata, VTT subtitles, a cleaned transcript, and the transcript ledger.
- Local PDF and zip sources were present in `/Users/farricecain/Downloads/` and were inspected without copying their full contents into this package.

## Available Evidence

- YouTube metadata is available in `metadata.json`.
- Timestamped spoken evidence is available in `transcript.txt`, `transcript.vtt`, `video-context-ledger.md`, and `video-context-ledger.json`.
- Companion PDF structure is summarized in `source-package.md` and `raw-prompt-inventory.md`.
- Raw prompt zip structure is summarized in `raw-prompt-inventory.md`.

## Limitations And Unavailable Evidence

- Frame extraction skipped because mode is transcript.
- OCR skipped because mode is transcript.
- No observed visual claims should be made from this package.
- No observed on-screen text claims should be made from this package.
- Auto-caption text contains duplicated rolling fragments and likely recognition errors. Treat transcript wording as subtitle evidence, not polished copy.
- PDF extraction used PyMuPDF because `pdftotext`, `pdfplumber`, and `pypdf` were unavailable.
- The prompt zip contains macOS `__MACOSX/` resource-fork entries; these were excluded from the usable prompt inventory.
- Exact prompt bodies are not reproduced in the package documents. Use the local zip as the exact-text source.

## Evidence Rule
Inferred context must not be merged into observed rows. Visual claims require a frame, OCR result, human note, or vision adapter output.
