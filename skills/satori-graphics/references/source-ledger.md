# Source Ledger — satori-graphics

> Claim-by-claim source accounting for the satori-graphics skill, per `directives/skill-craft-standard.md`. Complements (does not replace) `references/source-quotes.md`, which holds the full verbatim quote set.

## Sources Consulted

| ID | Source | Size | Status |
|---|---|---|---|
| S1 | `extractions/satori-graphics/extraction-report.md` — MES 3.0 deep extraction, v1 (4 videos, 10,652 words), dated 2026-05-03 | 20,288 bytes | VERIFIED (read in full) |
| S2 | `extractions/satori-graphics/transcript.txt` — raw transcript, v1 Video 4 ("How to design like a pro": flip-test, more≠better, AI-as-tool, speed) | 10,173 bytes | VERIFIED (read in full; 1,853 words matches extraction-report's Video 4 word count) |
| S3 | `extractions/satori-graphics/expansion-2026-07-04/vid1-transcript.txt` — v2 Video 1 (communication-problem-first, feeling-before-information) | 7,505 bytes | VERIFIED (read in full) |
| S4 | `extractions/satori-graphics/expansion-2026-07-04/vid2-transcript.txt` — v2 Video 2 | 9,535 bytes | VERIFIED (present, spot-checked) |
| S5 | `extractions/satori-graphics/expansion-2026-07-04/vid3-transcript.txt` — v2 Video 3 (color system) | 10,024 bytes | VERIFIED (read in full) |
| S6 | `extractions/satori-graphics/expansion-2026-07-04/vid4-transcript.txt` — v2 Video 4 (creative concept engine) | 9,059 bytes | VERIFIED (read in full) |
| S7 | `extractions/satori-graphics/expansion-2026-07-04/vid5-transcript.txt` — v2 Video 5 (perception gap) | 9,564 bytes | VERIFIED (read in full) |
| S8 | `skills/satori-graphics/references/source-quotes.md` — pre-existing curated verbatim quote file (v1 + v2), already shipped with the skill | 17,106 bytes | VERIFIED (all quotes cross-checked against S2–S7 where a raw transcript exists; see gap note below) |

## Claim → Source Map (repair-added anchors only)

Every anchor added in this repair pass traces to S8 (`source-quotes.md`) at minimum; the quotes below were additionally confirmed **verbatim, exact substring match** against the raw per-video transcript (S2–S7) where one exists:

| Quote (truncated) | Confirmed against raw transcript |
|---|---|
| "Speed is useful, obviously..." | S2 (`transcript.txt`, Video 4) |
| "Some designers do consider, somehow, that more layers..." | S2 |
| "That comfort is where most designers stop improving." | S2 |
| "Apple starts with a communication problem first..." | S3 (vid1) |
| "little to no money at disposal" | S3 (vid1) |
| "unimportant things quieter" | S3 (vid1) |
| "Instead of asking what color looks good..." | S5 (vid3) |
| "ushered along by hierarchy" | S5 (vid3) |
| "trying to achieve" (color job framing) | S5 (vid3) |
| "specific audience deeply enough to speak their language" | S6 (vid4) |
| "Information tells people what to think..." | S6 (vid4) |
| "real problem is... consequence... emotional impact" | S6 (vid4) |
| "pushing it further than everybody else would" | S6 (vid4) |
| "noticing tiny details that everybody else just overlooks" | S6 (vid4) |
| "Aesthetics are subjective, but confusion isn't..." | S7 (vid5) |
| "already convinced, already interested" | S7 (vid5) |
| "transformed into a metaphor. Music becomes emotion." | S7 (vid5) |
| "body-shaped absence" | S7 (vid5) |
| "evaporated from your memory" | S7 (vid5) |

## Known Gap (honest disclosure, not new to this repair)

The v1 series is billed as "4 videos, 10,652 words" (extraction-report.md, S1), but only **one** raw per-video transcript survives under `extractions/satori-graphics/` — `transcript.txt`, which is Video 4 (1,853 words, confirmed by word count match). Raw transcripts for v1 Videos 1–3 (psychology mindsets, composition + layout, logo design guide) are **not present** as separate files; their content survives only as paraphrase + embedded verbatim quotes inside S1 (`extraction-report.md`) and the pre-existing curated file S8 (`source-quotes.md`).

Quotes used in this repair that trace ONLY to S1/S8 (no raw-transcript confirmation available) — labeled **LIKELY** rather than VERIFIED:
- "The meaning should come way, way before the aesthetic in your process... throwing confetti at a layout" (Video 2)
- "Things like shields, arrows, mountains, initials... generic ideas start to creep in" (Video 3)
- "The logo is just one part of a much bigger brand system" (Video 3)
- "AI can give you the clean version every time, but only you can give the human version" (Video 1)
- "It assumes the viewer is already convinced, already interested" (Video 1) — note: this exact line also appears independently in S7 (vid5, v2 series), so this one is VERIFIED via S7
- "Every concept we present with a client uses the exact same layout and structure" (Video 3)
- "That's the difference between good friction and bad friction" (Video 2)
- "Now, instead of designing freely and hoping something meaningful just appears on the screen later..." (Video 3)
- "The brands or businesses that hire actual human designers do so for their thinking..." (Video 1)

**This gap pre-dates this repair pass** — it was true of the skill before this worker touched it (S8 and the genius.md GP-01/GP-07/GP-10 quotes already shipped on these same sources). This repair did not fabricate new provenance; it reused already-shipped verbatim material and labeled the confidence honestly. See `.tmp/wave3-lane4-b15/satori-graphics/PROVENANCE.md` for the full anchor-by-anchor table.

## Labels Summary

- **VERIFIED**: quote confirmed by exact-substring match against a raw video transcript file under `extractions/`.
- **LIKELY**: quote sourced from `extraction-report.md` and/or the pre-existing `source-quotes.md` (both count as sanctioned ground truth per the repair envelope's own definition — "files under extractions/... plus verbatim quotes already inside the skill files") but no raw transcript survives independently for cross-check.
- **UNCONFIRMED**: none used in this repair — every quote added traces to at least S1 or S8.
