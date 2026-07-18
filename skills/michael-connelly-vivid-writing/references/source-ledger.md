# Source Ledger — michael-connelly-vivid-writing

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 11). Every source file was opened and read in full before labeling; sizes below are `wc -c` on the actual files, not estimates.

## Sources on disk

| File | Size | Status |
|---|---|---|
| `extractions/michael-connelly/transcript.txt` | 64,634 bytes | VERIFIED present — full "How I Write" podcast episode transcript ("How to Write Vividly Well"), read in full for this repair |
| `extractions/michael-connelly/extraction-report.md` | 21,582 bytes | VERIFIED present — synthesis document (10 genius patterns, 6 hidden-knowledge insights), read in full |
| Perplexity research (7 sources), cited in SKILL.md frontmatter (`extracted_from`) and extraction-report.md line 6 | — | **UNCONFIRMED — no retained file.** No source list, URLs, or cached content for these 7 sources exists under `extractions/michael-connelly/`. Any claim traceable ONLY to this leg of the extraction (not corroborated in transcript.txt) is labeled LIKELY below, never VERIFIED, per the "false unrecoverable claims must be file-checked" rule. |

## Claim-by-claim (genius.md + SKILL.md)

| Claim | Label | Basis |
|---|---|---|
| "42 books" / 42 novels | VERIFIED | Connelly's own words, transcript.txt: "I'm up to like 42 books now" |
| "100M+ copies sold" | VERIFIED | Interviewer's spoken intro, transcript.txt: "combined his series have sold more than a hundred [snorts] million books" |
| Creator of Harry Bosch and The Lincoln Lawyer | VERIFIED | Transcript.txt intro + Connelly's own references to both series throughout |
| First Bosch novel published 1992 | VERIFIED | transcript.txt: "That book came out in 1992" |
| 98 episodes of *Bosch* / 50+ of *Lincoln Lawyer* (TV) | VERIFIED | transcript.txt: "we ended up getting like 98 episodes of Bosch. There's now going to be 50 of Lincoln Lawyer" |
| Journalist for ~14 years covering courts/crime | VERIFIED | transcript.txt: "I covered courts and I covered crime for about 14 years" |
| That journalism was specifically at **the Los Angeles Times** | LIKELY | Not stated by name in transcript.txt (Connelly says only "14 years," no outlet named); asserted in extraction-report.md line 70 without its own citation — most likely sourced from the unretained Perplexity research leg. Public biographical record is consistent with this, but it is not independently verified against a retained primary source here. |
| "Give me six inches on that" newspaper-economy quote | VERIFIED | transcript.txt: "they'd be saying like, 'Give me 6 in on that.'" |
| Telling-detail earpiece-groove example | VERIFIED | transcript.txt, detective-at-his-desk anecdote: "he had a groove in the plastic of his earpiece... his teeth are clenched" / "said a lot about the character with just one little moment" |
| Nod economy / editor's 540-nod count | VERIFIED | transcript.txt: "he's nodded 540 times and we're only on page 200" |
| Dual-pass rewrite (daily print-and-pencil + full-manuscript pass) incl. "RW"/"NSG" shorthand | VERIFIED | transcript.txt, full description including "RW means like rewrite this whole paragraph. NSG means not so good." |
| Vonnegut "glass of water" advice + Bosch cigarette-addiction mechanism | VERIFIED | transcript.txt: Vonnegut quote verbatim + Bosch smoking anecdote |
| Chandler Ritual (Chapter 13 of *The Little Sister* before each book) | VERIFIED | transcript.txt: Connelly names the book, describes the ritual, both parties quote passages from it |
| Richard Price "murder is a tale of a city" framing | VERIFIED | transcript.txt, attributed correctly to Richard Price, with Connelly noting Bosch is the one who "added that part" |
| Real-world anchor principle ("plant that character's feet in as real a world as possible") | VERIFIED | transcript.txt, near-verbatim |
| Slingshot principle (10 pages → 25 pages → no longer timed) | VERIFIED | transcript.txt, Connelly's own account of the evolution |
| Subtext dialogue example (captain/Bosch "wrapped up... yesterday" scene) | UNCONFIRMED as a literal Connelly quote | This is a constructed Hall-of-Fame exemplar built from Connelly's *described* subtext principle ("conversations that on face are about this, but they're really about that"), not a verbatim line from a published Bosch novel or the transcript. The **principle** is VERIFIED (transcript.txt); the **exemplar dialogue itself** is skill-authored illustration, not sourced prose — treat it as instructional fiction, not a Connelly quote, in any downstream use. |
| Anti-Exemplar ("The old, decrepit, forgotten alley...") | N/A — self-labeled | Explicitly a constructed failure case in genius.md, not attributed to Connelly. No claim of provenance. |
| "Existing Overlap: Partial with Eric Roth" | VERIFIED | extraction-report.md, Content Assessment block, verbatim |
| "Genius Patterns: 10 identified" / "Hidden Knowledge: 6 tacit insights detected" | VERIFIED | extraction-report.md, Content Assessment block, verbatim |
| Newly added AN-1–AN-6 anti-pattern source anchors (this repair pass) | VERIFIED | Every quote is a verbatim substring of transcript.txt, confirmed by direct string search before insertion (see PROVENANCE.md for exact offsets/context) |
| 16 workflow files carry Output Schema + Quality Gate | VERIFIED | `workflow_contracts` heartbeat check already PASSED pre-repair; untouched by this pass |

## Gaps named honestly

- The 7 Perplexity research sources referenced in the extraction's provenance are not retrievable — no cached URLs, snapshots, or citations exist on disk. Treat any claim that depends solely on that leg (flagged LIKELY above) as needing re-verification before it is used in a client-facing or public claim.
- The subtext-dialogue and adjective-stacking prose exemplars in genius.md are skill-authored teaching illustrations, not lifted Connelly prose — labeled accordingly above so they are never mistaken for verbatim quotes from his published fiction.
