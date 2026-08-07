# Source Ledger — dr-kriukow-humanization

> Repair-fleet artifact (Wave 3, Lane 4, Batch 5). Every claim in `genius.md` and
> `SKILL.md` traced to its source with a VERIFIED / LIKELY / UNCONFIRMED label, per
> `directives/skill-craft-standard.md` `source_ledger` heartbeat check.

## Sources Consulted

1. **`extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md`** —
   14,355 bytes, read in full. Itself a synthesis of a single YouTube video:
   "Humanize AI Writing & Bypass AI Detection with this KEY RULE" (2,901 words /
   15,818 characters, per report line 6). No raw transcript file exists in this repo
   for this expert — the extraction report is the closest artifact to a primary
   source available.

## Absence Check (a claim of "no source exists" is itself a provenance claim)

Per the envelope's hard rule — false "unrecoverable/0-byte" claims were caught by
adversarial verification elsewhere in this fleet run — the following were checked by
content grep, not assumed, before concluding the extraction report is the sole source:

| Location checked | Method | Result |
|---|---|---|
| `extractions/` | `ls extractions/ \| grep -i kriukow` | Only `extractions/dr-kriukow/` — one file, 14,355 bytes |
| `_active/harness/codex-harvest-2026-06-11/` | `find ... -iname "*kriukow*"` | `skills/dr-kriukow-humanization/SKILL.md` (1,652 bytes — an older/shorter SKILL.md variant, no genius.md) and `agents/dr-kriukow/AGENT.md` (4,106 bytes — derivative persona config, no new source quotes) |
| `_archive/claude-export-2026-07-01.tar.gz` | `tar -tzf ... \| grep -i kriukow` | Zero matches — confirmed empty by content grep, not assumed |
| `evolution_store/v2_variants/genius_compressed/dr-kriukow-humanization_genius.md` | `diff` against current genius.md | A compressed/reworded variant of the same 7 patterns already in genius.md — no new source material, no new quotes |

**Conclusion**: the 14,355-byte extraction report is the sole ground-truth source for
this expert in this repo. This is a genuinely thin-source skill (one ~2,900-word video,
no transcript on disk) — labeled honestly below rather than backfilled with invented
citations.

## Claims — VERIFIED / LIKELY / UNCONFIRMED

| # | Claim | Label | Basis |
|---|---|---|---|
| 1 | Statistical Unpredictability Principle (SUP) — AI text is the most statistically predictable version; structural change beats word change | VERIFIED | extraction report, Genius Pattern 1, lines 26-30 |
| 2 | Structure-Over-Words Hierarchy (structure → tense/voice → vocabulary priority) | VERIFIED | extraction report, Genius Pattern 2, lines 32-36 |
| 3 | Meaning Preservation Rewrite ("close your eyes and say it your way") | VERIFIED | extraction report, Genius Pattern 3, lines 38-42 |
| 4 | Deliberate Imperfection Injection | VERIFIED | extraction report, Genius Pattern 4, lines 44-48 |
| 5 | Order Reversal Technique | VERIFIED | extraction report, Genius Pattern 5, lines 50-54 |
| 6 | Anti-Mold Principle | VERIFIED | extraction report, Genius Pattern 6, lines 56-60 |
| 7 | Holistic Context Window (paragraph-level, not sentence-level, editing) | VERIFIED | extraction report, Genius Pattern 7, lines 62-66 |
| 8 | Oscillation Trap (sentence-level edits cause detector pass/fail flapping) | VERIFIED | extraction report, Hidden Knowledge #1, lines 72-73 |
| 9 | "Worse Is Better" Paradox (passive voice / imperfection improves humanization) | VERIFIED | extraction report, Hidden Knowledge #2, lines 75-76 |
| 10 | Aggressive Detector Advantage (GPT-Zero chosen as hardest test; "hardest first" validation) | VERIFIED | extraction report, Hidden Knowledge #3, lines 78-79 |
| 11 | Meaning-First Bypass (meaning-driven generation vs. form-driven editing) | VERIFIED | extraction report, Hidden Knowledge #4, lines 81-82 |
| 12 | "No Right Way" Principle (no single technique is mandatory; maximize divergence) | VERIFIED | extraction report, Hidden Knowledge #5, lines 84-85 |
| 13 | 4-phase methodology (Read the Mold → Extract Meaning Units → Reconstruct from Meaning → Validate) | VERIFIED | extraction report, Methodology, lines 89-113 |
| 14 | Dr. Kriukow runs a professional text-humanization service, giving him volume-based pattern recognition | LIKELY | extraction report, Executive Summary, line 18 — asserted by the extraction itself; not independently corroborated against an external bio in this repair pass |
| 15 | The two "Hall of Fame Exemplars" before/after text pairs (sustainable-practices / project-timeline) in genius.md are word-for-word demonstrations Kriukow used in the source video | UNCONFIRMED | Not found anywhere in `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md` — confirmed absent by grep for "sustainable practices", "Anti-Exemplar", "Superficial Word Swaps". These read as illustrative examples built for the skill, not transcript excerpts. Pre-existing content, not authored in this repair; `verbatim_exemplars` heartbeat check already PASSES independent of this label. Flagged in genius.md itself (provenance note above the Anti-Exemplar block) so downstream users don't cite the pairs as Kriukow's own words. |
| 16 | "AI writing and AI detection both operate on statistical probability" as the unifying frame of his method | LIKELY | extraction report Executive Summary states this as the "Core Genius" synthesis (line 17) — a reasonable compression of Genius Patterns 1-2, but phrasing is the extractor's paraphrase, not a direct transcript quote (no transcript on disk to check against) |

## Anti-Pattern Anchors (this repair's addition to genius.md § Anti-Patterns)

All six items added to fix `anti_patterns_sourced` quote the extraction report
verbatim (confirmed by `grep -n` against the source file before use):

| Anti-pattern | Quote | Report location |
|---|---|---|
| Word-swap-only humanization | "95%+ of AI content deployers are doing word-swapping" | Market Signals, line 126 |
| Sentence-by-sentence patching | "sentence-level edits preserve the inter-sentence statistical relationships" | Hidden Knowledge #1, line 73 |
| Treating one technique as mandatory | "none of his specific edits (order reversal, passive injection, etc.) are *the* right way" | Hidden Knowledge #5, line 85 |
| Leaving enumerations in AI order | "No list in the final text matches the original AI-generated order" | Genius Pattern 5, line 54 |
| Stopping at "too clean" prose | "AI tends to write in clean, efficient, active-voice prose. Humans don't." | Hidden Knowledge #2, line 76 |
| Reaching for more word substitutions post-flag | "If still flagged, increase structural divergence — never just swap more words" | Methodology Phase 4, line 112 |

All six labeled VERIFIED — each is a direct grep-confirmed substring of the source file.
