# PROVENANCE — extract-mastery repair (Wave 3 Batch 2)

Anchor → source file + location, for every claim/quote added to `genius.md` in this repair. Every quote below was re-read verbatim in its cited file before being written into genius.md (per ENVELOPE.md rule: "A quote you cannot find in a source file gets an UNCONFIRMED label, never an anchor").

## Anti-Patterns Section (genius.md, new "## Anti-Patterns (MES 3.0 Never Ships These)")

| # | Anti-pattern | Anchor quote | Source file | Location | Confidence |
|---|---|---|---|---|---|
| 1 | Transcript-only extraction for visual creators | "very straightforward and to the point… didn't capture the style and essence… I wouldn't be able to use any of this to see results." | `docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md` | "Problem" section, line 13 | VERIFIED |
| 2 | Self-graded blind-pass | "self-graded verification by the same fleet that built the thing is a rubber stamp, and it looks identical to a real pass in every ledger." | `docs/solutions/2026-07-16-rubber-stamp-blind-pass-artifact-only-retest.md` | "Problem" section, line 4 | VERIFIED |
| 3 | Taste rules as prose, not hard vetoes | "I don't like this M dash" | `docs/solutions/2026-07-07-blind-pass-taste-failure-hard-vetoes.md` | "Problem" section, line 13 | VERIFIED |
| 4 | Hardcoded finalize scores | `--intent 8/9 --expert-score 8/9` (literal flag string) | `directives/embodiment-standard.md` | "Scoring Discipline" section, line 40; corroborated in `directives/skill-craft-standard.md` §7 Anti-Pattern 3, line 56 | VERIFIED |
| 5 | Structure without heartbeat | "Farrice detected real experts only 5/15... preferred skill-generated work 8-6-1" (paraphrase of figures 5/15 and 8-6-1) | `directives/embodiment-standard.md` | Header note, line 3 | VERIFIED (figures read directly, not invented) |
| 6 | Zero-entity genius patterns | "the #1 mechanical hollowness tell" | `directives/embodiment-standard.md` | Build checklist item 9, line 17 | VERIFIED |
| 7 | Wholesale rebuild after one taste failure | Structure diagnosis "already embodied (objection→format→mechanic chain intact)" and the retry-once approach | `docs/solutions/2026-07-07-blind-pass-taste-failure-hard-vetoes.md` | "Approach That Worked" step 4 + "Dead Ends" section | VERIFIED |

## Recognition-Test / Model-Calibration Section (genius.md, new "## How to Use This Skill (Model Calibration)")

| Claim | Anchor | Source file | Location | Confidence |
|---|---|---|---|---|
| E1 factory audit found structure but not embodiment | Paraphrase of "found the extraction pipeline verified structure... never embodiment" | `directives/embodiment-standard.md` | Header note, line 3 | VERIFIED |
| Density mandate quote | "do not use 1,000 words if 200 words of lethal, paradigm-shifting insight will achieve the goal" | `directives/mes-3.0-extract.md` | "THE VIRTUOSO DENSITY MANDATE & ANTI-PATTERN LOCK" §1, line 12 | VERIFIED |
| Gravedigger pass | "The Gravedigger Safeguard (Feeling Density)... Concrete emotional resonance must scale with information density" | `directives/mes-3.0-extract.md` | §2, line 18 | VERIFIED |
| Recognition-test phrasing model ("would X recognize this as theirs, or as someone wearing their vocabulary") | Adapted from "would the expert recognize this as theirs, or as someone wearing their vocabulary?" | `directives/skill-craft-standard.md` | §1 "The Heartbeat Test", line 8 | VERIFIED — phrasing adapted to MES 3.0's own domain (Farrice as the expert), not copy-pasted verbatim into a different context |

## Structural Model (not a content source — cited per ENVELOPE.md's explicit instruction)

| Use | Source file | Location | Confidence |
|---|---|---|---|
| "How to Use This Skill" section format (intuition primitives / never announce machinery / expert texture / polish-is-the-tell) | `skills/ben-watkins-storytelling/genius.md` | Lines 7-16 | VERIFIED — read in full; zero prose reused, structure only |
| Source-ledger table format (adapted to add VERIFIED/LIKELY/UNCONFIRMED per-row) | `skills/claim-safe-health-marketing/references/source-ledger.md` | Full file | VERIFIED — format adapted, no content reused |

## Explicitly NOT Anchored (would-be claims considered and rejected)

- **Did not cite `skills/extract-mastery/genius.md` (this skill's own prior text) as a "source" for its own anti-patterns.** The already-committed Batch-3 repair (git commit `65d6039e6`) does exactly this — its 6 anti-pattern items all cite `genius.md` itself, dated uniformly "2026-07-01" (the extraction's own frontmatter date, not a real failure date). That is circular provenance, not a caught failure. This repair deliberately sources every anti-pattern to a file OUTSIDE the skill itself — a real dated incident record (`docs/solutions/*.md`) or a real governing standard (`directives/embodiment-standard.md`, `directives/skill-craft-standard.md`). See `REPAIR-NOTES.md` for the full comparison.
- **Did not claim "no source exists" for anything without a file read.** Every file referenced above was opened and read in full (or, for `extractions/jeremy-haynes/extraction-report.md`, the first 40 lines, sufficient to confirm the spine and one verbatim quote) before being cited. No "unrecoverable/0-byte" claims were made.
