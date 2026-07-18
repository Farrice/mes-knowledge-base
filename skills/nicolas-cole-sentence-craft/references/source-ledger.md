# Nicolas Cole — Sentence Craft — Source Ledger

Claim-by-claim provenance for `genius.md`, `references/genius-patterns.md`, and
`references/hidden-knowledge.md`. Written 2026-07-18 as part of the Wave 3
Lane 4 heartbeat repair.

## Method

Every file under `extractions/` whose name matches `nicolas-cole*` was read in
full and grepped for the mechanical vocabulary this skill's content depends
on: "adverb," "comma," "sentence," "compress," "vocabulary," "rhythm,"
"fourth-grade"/"fourth grade," "redundan(cy)," "repetition," "terminal word,"
and "jargon." Sizes recorded via `wc -c`:

| File | Size (bytes, `wc -c`) | Content |
|---|---|---|
| `extractions/nicolas-cole/transcript.txt` | 18,152 | Offer-stacking livestream (digital products / landing-page copy) |
| `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` | 30,638 | "30-day plan to land writing clients" (client acquisition) |
| `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | 21,487 | Ghostwriting business-model session |
| `extractions/nicolas-cole-client-acquisition/extraction-report.md` | 14,158 | Extraction report, client-acquisition domain |
| `extractions/nicolas-cole-digital-products/transcript.txt` | 39,852 | "The 6 Types of Digital Products" livestream |
| `extractions/nicolas-cole-digital-products/extraction-report.md` | 13,760 | Extraction report for the above |

## Result: zero matches

None of the six files contain the word "sentence" at all (`grep -c -i
"\bsentence\b"` returns 0 across all four transcripts). "Compress\*" appears
once, in `ghostwriting-v1`, but refers to "a compressed time period" (a
goal-timeline framing in a client-acquisition context) — not prose
compression. No file contains "adverb," "comma," "vocabulary," "rhythm,"
"fourth-grade," "redundan(cy)," "repetition," "terminal word," or "jargon"
in any writing-craft sense.

**Conclusion**: the six mechanical patterns this skill teaches — terminal
word power, three-pass compression, the two-comma rule, Hemingway adverb
elimination, fourth-grade vocabulary anchoring, and the contraction/
abbreviation protocol — are not traceable to any source file currently
under `extractions/nicolas-cole*/`. This is consistent with the finding
already on record in `skills/nicolas-cole-digital-products/references/
source-ledger.md` (a sibling skill in this same repair batch), which
independently confirmed the same six extraction files contain no sentence-
level craft material — those transcripts are offer-strategy and business-
model content, not prose-mechanics teaching.

One real, verifiable anchor exists: `extractions/nicolas-cole/transcript.txt`
closes with Cole recommending his own book, quoted verbatim: *"I recommend
reading The Art and Business of Online Writing."* This confirms the book's
existence and that Cole wrote it, and it is plausible the book is the
original source of granular sentence-level rules given Cole's public
teaching reputation — but this repair worker did not have access to the
book's text, so that link is a hypothesis, not a verified citation.

## Labels

**VERIFIED** = quote/claim confirmed verbatim in a cited `extractions/` file.
**LIKELY** = underlying concept confirmed in a source; specific number or
example in the skill is an unverified elaboration. **UNCONFIRMED** = no
anchor found in any `extractions/nicolas-cole*/` file; carries no source
citation.

## Genius Patterns 1-12 (genius.md + references/genius-patterns.md)

| # | Pattern | Status | Anchor |
|---|---------|--------|--------|
| 1 | Terminal Word Power Placement | UNCONFIRMED | No match for "terminal word," "last word," or comparable phrasing in any `extractions/nicolas-cole*/` file. |
| 2 | Three-Pass Economic Compression | UNCONFIRMED | No match for "compress" in a prose-editing sense (the one "compress\*" hit, in ghostwriting-v1, is about a goal timeline, not word count). |
| 3 | Contraction Introduction Protocol | UNCONFIRMED | No match for "abbreviation" or the first-mention/subsequent-mention pattern. |
| 4 | Audience Sizing Through Vocabulary | UNCONFIRMED | No match for "vocabulary" or "audience size" framed around contractions. |
| 5 | Redundancy Elimination Radar | UNCONFIRMED | No match for "redundan\*" in any file. |
| 6 | Word Variation Substitution | UNCONFIRMED | No match for repeated-word substitution guidance. |
| 7 | Fourth-Grade Vocabulary Anchoring | UNCONFIRMED | No match for "fourth grade," "fourth-grade," or Flesch-Kincaid language. |
| 8 | The Two-Comma Rule | UNCONFIRMED | No match for "comma" in any file. |
| 9 | Hemingway Adverb Elimination | UNCONFIRMED | No match for "adverb" or "-ly" editing guidance; "Hemingway" attribution not found in source. |
| 10 | Opening Sentence Power | LIKELY | No verbatim match, but the underlying instinct ("don't bury the lead," answer questions fast) is directionally consistent with Cole's education-first sales philosophy documented in `extractions/nicolas-cole/transcript.txt` ("sales has everything to do with education"). Not a direct anchor — flagged LIKELY, not VERIFIED. |
| 11 | Information Density Optimization | UNCONFIRMED | No match for "information density" or paragraph-level new-information auditing. |
| 12 | Voice Preservation | UNCONFIRMED | No match for "voice" used in a prose-craft sense. |

## Hidden Knowledge 1-7 (references/hidden-knowledge.md)

All 7 items (Terminal Word Echo Effect, Contractions as Audience Signals,
Writing as Compression, Repetition as Disengagement Trigger, Vocabulary
Friction Threshold, Comma Count as Clarity Barometer, Adverbs as Training
Wheels) are restatements of Genius Patterns 1, 3, 2, 5, 7, 8, and 9
respectively — each inherits that pattern's UNCONFIRMED/LIKELY status above.

## Hall of Fame Exemplars + Anti-Exemplar

Constructed before/after illustrations (labeled "Original thought
(pre-Cole)" vs. "Cole's Craft" in the file itself) — these are pattern
demonstrations, not quotes attributed to a transcript, and were not
represented as sourced material before this repair either. No status change.

## Anti-Patterns (genius.md, new section — 8 items)

All 8 items UNCONFIRMED — each restates a Genius Pattern in "never" form and
carries an inline UNCONFIRMED status pointing back to this ledger. No new
claims introduced; this is a reformatting of the pre-existing Anti-Exemplar
bullet list (lines under "Anti-Exemplar: Bloated, Weak-Ending, Repetitive
Prose") into a standing checklist, per the additive-first / content-
preserving boundary.

## Signature Moves / Expert-Specific Quality Rubric

Restate the Genius Patterns above in compressed form (e.g. "The Echo Audit"
restates Pattern 1, "The Compression Gauntlet" restates Pattern 2).
Provenance status inherits from the pattern each move restates.

## Not used / not applicable

- No other `extractions/` directories match "cole" beyond the six files
  above (`ls extractions/ | grep -i cole` confirms this is the complete set).
- Cole's book *The Art and Business of Online Writing* is referenced by
  title in `extractions/nicolas-cole/transcript.txt` but its text is not
  present under `extractions/` and was not consulted — flagged above as an
  unverified hypothesis, not treated as a source.
