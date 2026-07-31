# Kieran Flanagan — Content Engine — Source Ledger

Ground truth for `kieran-flanagan-content-engine` is a single primary extraction pair under `extractions/kieran-flanagan/` (the general-purpose AI content-team episode). The sibling folder `extractions/kieran-flanagan-second-brain/` covers a different, later video (personal-knowledge-base architecture) and is out of scope for this skill's content-production patterns — it was checked and excluded, not overlooked.

## Primary Source Corpus

| Source | Where found | Size (`wc -c`, verified 2026-07-17) | Label |
|---|---|---|---|
| `extractions/kieran-flanagan/transcript.txt` — raw transcript, "I Built an AI Team That Creates All My Content" (Marketing Against the Grain) | Repo root `extractions/kieran-flanagan/` | 27,523 bytes | VERIFIED — read in full this repair |
| `extractions/kieran-flanagan/extraction-report.md` — MES-style deep extraction (Genius Patterns, Hidden Knowledge, Methodology) built from the same transcript | Same directory | 14,945 bytes | VERIFIED — read in full this repair |

## Claim-by-Claim (anti-patterns added in this repair)

| Claim / quote | In-repo anchor | Label |
|---|---|---|
| "the content enrichment tools need a first draft to enrich and so trying to enrich just a idea is kind of hard" | `extractions/kieran-flanagan/transcript.txt` — re-verified verbatim via `grep -o` against the raw file this repair | VERIFIED |
| "obviously I would never ship this" / "this is a draft an idea and then you make much better" | `extractions/kieran-flanagan/transcript.txt` — both re-verified verbatim via `grep -o` | VERIFIED |
| "I was never a big fan of the kind of vibe marketing where it was workflow tools because it's not vibing. You have to actually drag and drop all the workflows together. This is not software." | `extractions/kieran-flanagan/transcript.txt` — re-verified verbatim via `grep -o` | VERIFIED |
| "Traditional personas are built from demographics and surveys — they're fiction" | `extractions/kieran-flanagan/extraction-report.md`, Hidden Knowledge §1 — re-verified verbatim via `grep -o`. Attributed as the extraction report's own analytical framing of Kieran's method, not quoted as Kieran's literal speech (the raw transcript does not contain this sentence). | VERIFIED (as extraction-report prose, not a Kieran direct quote) |
| "Never let LinkedIn style infect newsletter style... Cross-pollination produces 'uncanny valley' content that sounds right on no platform" | `extractions/kieran-flanagan/extraction-report.md`, Hidden Knowledge §5 (The Platform Isolation Rule) — re-verified verbatim via `grep -n` | VERIFIED (extraction-report synthesis, not literal transcript speech) |
| "the analytical models are 'too good' at following instructions for creative tasks, producing overly rigid output" | `extractions/kieran-flanagan/extraction-report.md`, Hidden Knowledge §4 (Model Routing Strategy) — re-verified verbatim via `grep -n`. Raw transcript does not contain a corresponding model-routing passage; this is the extraction report's synthesis of an off-camera or edited-out detail. Kept as a genuine anti-pattern but explicitly labeled as report-sourced, not transcript-sourced. | VERIFIED (extraction-report only — transcript does not corroborate) |
| Pre-existing genius.md patterns/quotes (Pattern 1-6, Hidden Knowledge 1-6, Hall of Fame exemplars, Signature Moves, Quality Rubric) | `extractions/kieran-flanagan/extraction-report.md` and `extractions/kieran-flanagan/transcript.txt`, both files | VERIFIED — pre-existing content, not modified this repair; spot-checked against both source files during this pass and found consistent |

## Absence Check (verified, not assumed)

- `ls extractions/ | grep -i flanagan` → returns `kieran-flanagan` and `kieran-flanagan-second-brain` (run 2026-07-17). Only `kieran-flanagan/` (transcript.txt + extraction-report.md) is in scope for this skill; the second-brain folder was opened and confirmed off-topic (personal-knowledge-base architecture, not content production), not skipped unread.
- No `references/` directory previously existed for this skill (`ls skills/kieran-flanagan-content-engine/references/` returned only `prompts-v2/` pre-repair) — the absence of a prior source-ledger was a real gap, not an unread file.

## Notes on This Repair

- Only the three failing heartbeat checks were addressed: `anti_patterns_sourced` (6 sourced anti-pattern bullets added to `genius.md` under a new "## Anti-Patterns (Sourced)" heading, anchors on the list-item line), `recognition_test` (new "## How to Use This Skill (Model Calibration)" section added to `genius.md`), `source_ledger` (this file).
- `verbatim_exemplars`, `named_entity_floor`, and `workflow_contracts` were already passing and were not touched.
- SKILL.md, the 8 workflow files, and `references/prompts-v2/*.md` are unmodified and not included in this output directory (flat layout, changed files only).

## 2026-07-30 Expansion: Content Signal Ideation

The prior repair note above describes the 2026-07-17 pass and is historical. The skill now has 9 workflows.

| Claim | Source | Label |
|---|---|---|
| Ideation loads an audience profile plus winning platform patterns | `extractions/transcripts/cSz_6SNEirU.txt` | VERIFIED |
| Recent signals are researched across named sources inside an operator-selected window | Same transcript; Kieran names Reddit, X, the web, 7-day, 28-day, and 30-day examples | VERIFIED |
| Strong candidates may appear in both proven-pattern and trend-upside lanes | Same transcript demonstration | VERIFIED |
| The creator is the domain expert whose taste and judgment select useful ideas | Same transcript | VERIFIED |
| The system supplies building blocks rather than finished content | Same transcript | VERIFIED |
| Every candidate must show its recommended platform | Same transcript self-correction: the system omitted platform labels and Kieran identified the miss | VERIFIED |
| Proven / Trending / Convergence is the production lane taxonomy | `extractions/kieran-flanagan-content-signal-loop/extraction-report.md` | INFERRED architecture from the demonstrated lanes |
| Ranking fields, staleness propagation, tombstone checks, and finished-content veto are implementation controls | Same extraction report and architecture checkpoint | INFERRED |

The new anti-pattern phrase "prompt-to-publish ideation" is a summary label. The rejected behavior chain is directly demonstrated in the transcript; the label itself is not a Kieran-named framework.
