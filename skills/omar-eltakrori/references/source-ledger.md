# Source Ledger — Omar Eltakrori

> Every source consulted for the Wave 3 Lane 3 heartbeat repair (2026-07-17), with a VERIFIED/LIKELY/UNCONFIRMED label per claim class. This ledger is additive: the skill's existing `source-quotes.md` (verbatim quote bank + per-claim Claims Ledger for the two 2026 teach-to-sell videos) and `genius-patterns.md` (labeled Exterior Game patterns) remain the primary source ledgers and are unchanged. This file adds the sources newly cited by the repair (the Anti-Patterns section in `genius.md` and the Model Calibration section) and states their checkability.

## Files Consulted (this repair)

| File | Bytes | Consulted for | Label |
| :--- | :--- | :--- | :--- |
| `extractions/omar-eltakrori/transcript.txt` | 125,945 | Interview-transcript anti-pattern quotes (discount/cheap-gear, perfectionism, inconsistency) | VERIFIED — read directly, quotes matched verbatim against file content via grep |
| `extractions/omar-eltakrori/teach-grow-rich/v1-start-teaching.txt` | 29,662 | V1 "How To Become A Millionaire in 2026 (Start Teaching)" — WHAT-not-HOW anti-pattern quote | VERIFIED — cross-checked against `references/source-quotes.md` lines 77-78, which already carries this quote labeled (V1) |
| `extractions/omar-eltakrori/teach-grow-rich/v2-teach-and-grow-rich.txt` | 38,595 | V2 "How To Teach and Grow Rich In 2026" — fire-hose and insecurity anti-pattern quotes | VERIFIED — cross-checked against `references/source-quotes.md` lines 41 and 46, and against the existing `genius.md` "Over-Teaching" section (both already carry these quotes) |
| `extractions/omar-eltakrori/teach-grow-rich/mastery-extraction-teach-to-sell.md` | 24,076 | Structural cross-check for the Exterior Game claims already in genius.md | VERIFIED (existing) — file exists and is non-empty; not independently re-quoted by this repair |
| `extractions/omar-eltakrori/extraction-report.md` | 18,961 | Background on extraction provenance and structure | VERIFIED (existing) — read, no new claims lifted from it for this repair |
| `references/source-quotes.md` (in-skill) | — | Ground-truth verbatim bank + Claims Ledger for V1/V2; used to verify two of the new Anti-Patterns quotes match exactly | VERIFIED (pre-existing, unmodified) |
| `genius.md` "Patterns from claude.ai export — Omar Eltakrori conversations (2026-07-01)" (in-skill, unmodified body) | — | Source for the Program-Not-Course and Overspiritualize→Undermonetize anti-pattern quotes (already verbatim-quoted in that section, dated and episode-attributed) | VERIFIED (pre-existing, unmodified) — self-reported revenue figures inside these patterns remain UNCONFIRMED per that section's own header |
| `skills/omar-eltakrori/workflows/personal-brand-blueprint.md` Phase 0 (in-skill, unmodified body) + `references/prompts-v2/personal-brand-business-blueprint.md` line 39 | — | Source for the "lecturing become-X" anti-pattern (workflow's own Anti-Pattern note, reused verbatim) | VERIFIED (pre-existing, unmodified) |

## Note on Empty-Looking Files (Rule 2 compliance)

`extractions/omar-eltakrori/transcript.txt`, `v1-start-teaching.txt`, and `v2-teach-and-grow-rich.txt` report `wc -l` = 0 because they are single-line files (no embedded newlines — the raw transcript export has no line breaks). They are NOT empty: `ls -la` confirms 125,945 / 29,662 / 38,595 bytes respectively, and `head -c 500` on each returns substantial, coherent transcript prose. Do not mistake `wc -l` = 0 for a 0-byte or unrecoverable file.

## What Changed vs. What's Inherited

This repair added ONE new section to `genius.md` ("Anti-Patterns (What Omar Explicitly Warns Against)") built entirely from quotes already verbatim-present elsewhere in the skill (source-quotes.md, genius.md's own existing sections, the workflow's own anti-pattern note) plus two net-new quotes pulled directly from `transcript.txt` and grep-verified against the raw file. No new source material outside `extractions/omar-eltakrori/` was consulted. No claim in the new section carries a label stronger than what its origin already carried (self-reported revenue/timeline claims inherited from claude.ai-export patterns remain UNCONFIRMED).
