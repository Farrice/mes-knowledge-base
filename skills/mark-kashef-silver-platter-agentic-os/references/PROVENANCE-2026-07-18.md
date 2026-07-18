# Provenance — Mark Kashef Silver Platter Agentic OS Repair

Anchor -> source file + location. All sizes via `wc -c`.

| Anchor in repaired files | Source file | Location | wc -c |
|---|---|---|---|
| All 8 genius.md anti-pattern items + Pattern quotes | `extractions/video-context/-WCNwxz3uoM/transcript.txt` | timestamps 00:04:12–00:20:45 (see source-ledger.md rows 1-8) | 93,160 |
| Video metadata (title, channel, date, duration) | `extractions/mark-kashef-perfect-agentic-os-kit/extraction-brief.md` | Source Evidence section | 3,486 |
| Build-Shape Verdict quote | `extractions/mark-kashef-perfect-agentic-os-kit/extraction-brief.md` | Build-Shape Verdict section | 3,486 |
| Validation date/counts | `extractions/mark-kashef-perfect-agentic-os-kit/validation-report.md` | Status + Validation Commands | 3,403 |
| Component Order steps referenced in workflows/*.md | `skills/mark-kashef-silver-platter-agentic-os/SKILL.md` (unmodified, existing) | Component Order section | 5,804 |
| Data-map assembly field logic referenced in `workflows/assemble-and-render-data-map.md` | `skills/mark-kashef-silver-platter-agentic-os/references/prompts-v2/data-map-assembly.md` (unmodified, existing) | Execution Protocol section | 12,975 |
| Audit-branch logic referenced in `workflows/audit-and-classify.md` | `skills/mark-kashef-silver-platter-agentic-os/references/prompts-v2/existing-setup-audit.md` (unmodified, existing) | Execution Protocol section | 6,726 |
| Opportunities/handoff logic referenced in `workflows/opportunities-and-handoff.md` | `skills/mark-kashef-silver-platter-agentic-os/references/prompts-v2/opportunities-brief.md` + `references/prompts-v2/builder-handoff.md` (unmodified, existing) | full files | 10,279 + 7,398 |
| Regulated example proof cited in `workflows/opportunities-and-handoff.md` | `extractions/mark-kashef-perfect-agentic-os-kit/validation-report.md` | Regulated Example Proof section | 3,403 |

## Verification method

Every quote attributed to the transcript was confirmed present verbatim via `grep -c "<exact substring>" extractions/video-context/-WCNwxz3uoM/transcript.txt` before being written into `genius.md` — each returned a count ≥1 (see command history for this session). No quote was written from memory or inference.

## What was NOT invented

- No new archetype, script, or example was fabricated. `workflows/*.md` reference existing `references/prompts-v2/*.md` and `scripts/*.py` files rather than duplicating or reinventing their contracts.
- No visual/on-screen claim was made anywhere — the extraction's own uncertainty report (`extractions/video-context/-WCNwxz3uoM/uncertainty-report.md`) states frame/OCR extraction was skipped for this source, and that boundary is preserved (see source-ledger.md row 14, UNCONFIRMED by design, not silently dropped).
