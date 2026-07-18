# Source Ledger — Eric Roth Writing Mastery

Ground-truth sources for this skill (companion to `eric-roth-screenwriting-mastery`, same underlying extraction):

- `extractions/eric-roth/transcript.txt` — 88,599 bytes (verified via `wc -c`), single-block YouTube interview transcript, 17,553 words per the extraction report header. Confirmed readable, non-empty, contains all quotes cited below verbatim (checked with `grep -o -E` against the raw file, not against the extraction report's paraphrase).
- `extractions/eric-roth/extraction-report.md` — 19,446 bytes (verified via `wc -c`), dated 2026-03-10, MES 3.0 deep-extraction synthesis of the transcript plus "2 Perplexity research passes" (per its own header — those Perplexity passes are NOT separately archived as files, so any claim traceable only to them and not to the transcript is labeled LIKELY, not VERIFIED).
- `skills/eric-roth-screenwriting-mastery/genius.md` — sibling skill (companion, same source material), read for structural reference only (the "How to Use This Skill" section format). Not independently re-verified here since another worker owns that file this batch.

Claim-by-claim, for every sourced claim added or upgraded in `genius.md` this repair pass:

| Claim | Label | Anchor |
|---|---|---|
| "Good morning, Mr. Water Commissioner" is the worst exposition line, per a director Roth worked with | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim string match); synthesized as HK-2, `extractions/eric-roth/extraction-report.md:198-199` |
| "Talk about a dream you had rather than tell us that you're upset with your mother" — Roth's off-center teaching | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim); Pattern 5, `extractions/eric-roth/extraction-report.md:83-90` |
| Rewriting feels "laborious" vs. the "adventure of trying to create something new" | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim) |
| "I outline just with one word like five scenes in a row... wedding, shootout" | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim); Pattern 14, `extractions/eric-roth/extraction-report.md:182-189` |
| Bad openings "push you away"; good ones make the reader "a party to it" | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim, near-exact — extraction report's Pattern 12 quote at `extractions/eric-roth/extraction-report.md:160-167` is a lightly cleaned paraphrase of this same passage) |
| "Erosion" as re-entry from page one ("shore up what is kind of falling down") | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim); Pattern 1, `extractions/eric-roth/extraction-report.md:39-47` |
| Michael Cimino gave Mickey Rourke a character "wallet" of specific life details | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim, name spelled "Mickey Roor"/"Ror" in the raw transcript — auto-transcription artifact of "Rourke"); Pattern 4, `extractions/eric-roth/extraction-report.md:72-80` |
| The "third rail" collaboration principle with directors | VERIFIED | `extractions/eric-roth/transcript.txt` (verbatim) |
| "Are you tired of struggling with complicated software solutions?" anti-exemplar | UNCONFIRMED as a Roth quote — VERIFIED as a rule-violation illustration | Not from Roth; a synthesized anti-exemplar authored inside `skills/eric-roth-writing-mastery/genius.md` (Hall of Fame Exemplars section, pre-existing) to demonstrate the inverse of Patterns 5 and 7. Never present it as something Roth said. |
| "Coffee Going Cold" and "Sandcastle Architect" Hall of Fame exemplars | UNCONFIRMED as Roth's own writing | Pre-existing constructed illustrations in `genius.md` (not touched this pass), authored to demonstrate cross-domain application of Roth's principles — not verbatim Roth material, not attributed to him as quotes. Flagged here for downstream honesty; not re-labeled in the exemplar text itself because it does not claim Roth authorship. |
| Brad Pitt's "prose boner" comment | LIKELY | Widely circulated in extraction-report.md prose (line 9-ish context) and pre-existing skill copy, but the exact phrase does not appear verbatim in `extractions/eric-roth/transcript.txt` — likely sourced from one of the "2 Perplexity research passes" noted in the extraction report header, which are not separately archived. Downgraded from VERIFIED to LIKELY for this ledger; not re-worded in-place since it predates this repair pass and is not one of the failing checks. |

## Method note
All VERIFIED rows above were checked by `grep -o -i -E` against the raw `extractions/eric-roth/transcript.txt` file directly (not against the extraction report) to confirm the quote exists in the primary source, not just in a downstream synthesis. Any claim in this skill not listed above was out of scope for this repair pass (only `anti_patterns_sourced`, `recognition_test`, and `source_ledger` were failing per the heartbeat audit) and was left untouched.
