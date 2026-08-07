# Provenance — youtube-video-context-analysis repair

Anchor → source file + location, for every date/quote/source anchor added to `genius.md`. All quotes were read directly from the cited file this session (not recalled from training memory).

| Anchor (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "~30-50% of meaning in modern video ... lives in the visual channel" (blockquote, Core Thesis) | `directives/video-vision-protocol.md` | "Purpose" section, line 7 |
| 600-second (10-minute) duration cap (Evidence Lanes) | `execution/fetch-video-context.py` | Line 49, `DEFAULT_MAX_DURATION_SEC = 600` |
| 18 recognized video hosts (Signature Moves) | `execution/fetch-video-context.py` | Lines 61-70, `KNOWN_VIDEO_HOSTS` tuple (hand-counted) |
| "collapsing 'the speaker probably showed X' into an observed visual row" (Anti-Patterns, item 1) | `skills/youtube-video-context-analysis/references/prompts-v2/full-visual-context-ledger.md` | Line 43, forged/refactored 2026-07-13 per frontmatter |
| "treating thumbnails, titles, or video descriptions as proof of in-video evidence" (Anti-Patterns, item 2) | `skills/youtube-video-context-analysis/references/prompts-v2/frame-ledger.md` | Line 29, forged/refactored 2026-07-13 per frontmatter |
| "YouTube captions were preserved as row-shaped ledger evidence but not reconstructed into a clean transcript surface" (Anti-Patterns, item 3) | `_active/harness/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md` | Line 7, "Summary" |
| ~2026-06-30 repair date (Anti-Patterns, item 3) | `execution/video_context_ledger.py`, `execution/verify_video_context_source_package.py` | Filesystem mtime (`ls -la`, `Jun 30 15:34` / `Jun 30 11:59`) — inference, labeled LIKELY in source-ledger.md, not an explicit changelog date |
| `extractions/video-context/Zc4E_K48v48` / attention-hijack-hooks / "quarantine from arsenal" (Anti-Patterns, item 4) | `_active/harness/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/may-june-extraction-integrity-ledger.md` | Row for `Zc4E_K48v48`, "Ledger" table; header states audit window 2026-05-01 to 2026-06-11 |
| 2026-05-03 banned-pattern date (Anti-Patterns, item 5) | `execution/fetch-video-context.py` (docstring citation) + `directives/video-vision-protocol.md` (line 9, corroborating citation) | Docstring line 7; protocol line 9. The underlying `feedback_ai-memory-dependent-observability.md` file itself was not opened this session — date is corroborated by two independent citing files, not read at its own source |
| Governor over-triage risk (Anti-Patterns, item 6) | `_active/harness/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md` | "Audit Goals" section, bullet 1 — phrased in genius.md as an open audit question, not a confirmed incident |
| "Claims that the system saw visuals" (Quality Standard) | `skills/youtube-video-context-analysis/references/quality-rubric.md` | "Failure Conditions" section, first bullet (fragment quoted) |
| "Gives every extraction workflow access to visual frames + Whisper-grade transcripts without depending on the AI assistant remembering to invoke the `/watch` slash command" (blockquote candidate considered, used in `references/source-ledger.md` claim table) | `execution/fetch-video-context.py` | Docstring lines 3-7 |

## Workflow Output Schema provenance

Each of the 8 `workflows/*.md` Output Schema sections was adapted from the corresponding `references/prompts-v2/*.md` file's existing "Output Contract" + "Output Skeleton" sections (born-v2, forged/refactored 2026-07-13) — already in-skill, workflow-specific content, not invented:

| Workflow | Prompts-v2 source |
|---|---|
| `01-quick-transcript-ledger.md` | `references/prompts-v2/quick-transcript-ledger.md` |
| `02-full-visual-context-ledger.md` | `references/prompts-v2/full-visual-context-ledger.md` |
| `03-frame-ledger.md` | `references/prompts-v2/frame-ledger.md` |
| `04-visual-ocr.md` | `references/prompts-v2/visual-ocr-notes.md` |
| `05-source-to-skill-extract.md` | `references/prompts-v2/source-to-skill-extraction-map.md` |
| `06-context-audit.md` | `references/prompts-v2/context-audit.md` |
| `07-creative-reference-breakdown.md` | `references/prompts-v2/creative-reference-breakdown.md` |
| `08-multi-video-comparison.md` | `references/prompts-v2/multi-video-comparison.md` |
