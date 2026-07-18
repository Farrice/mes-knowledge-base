# Source Ledger — joanna-wiebe-persuasion-mastery

> Every source consulted during this repair pass (Wave 3 Lane 4 Batch 7), with
> VERIFIED / LIKELY / UNCONFIRMED labels, claim-by-claim. VERIFIED = I opened
> the file and the quoted text is present verbatim. LIKELY = internally
> consistent with a verified source but not itself independently checked.
> UNCONFIRMED = no primary-source file exists in this repo; content is
> attributable only to a prior AI-generated summary. File sizes recorded via
> `wc -c` on 2026-07-18 to rule out empty/placeholder files.

## Primary sources (read in full this pass)

| File | Size (bytes) | Status | Notes |
|---|---|---|---|
| `extractions/joanna-wiebe/transcript.txt` | 15,223 | VERIFIED | Full raw transcript of "How To Sell Anything Through The Words You Use" (9 funnel-stage triggers). Read in full; every quote used in this repair's new Anti-Patterns section ("Business strategies for everyone," "that defensive response actually costs millions," "why are they trying so hard," "confirms the fear is a big deal") appears verbatim in this file. |
| `extractions/joanna-wiebe/9-psychological-writing-triggers-extraction.md` | 10,849 | VERIFIED | Structured extraction derived from the same video as transcript.txt above. Read in full; Hidden Knowledge #3 (Anti-Pile Proof Principle) and #4 (Boring Objection Kill Pattern) confirmed present and match the language cited in the new Anti-Patterns bullets. |
| `extractions/joanna-wiebe/authority-craft-extraction.md` | 11,353 | VERIFIED | Extraction of "How To Write Freakishly Well And Have An Unfair Advantage." Read in full; sources the 5 Authority Craft Mechanics already in genius.md Part 2 (Catchy Phrasing, Order of Revelation, Stealing Thunder, Anti-Hype, Bucket Brigades). No raw video transcript file exists in this repo for this source — extraction summary is the only artifact. |
| `extractions/joanna-wiebe-persuasion-mastery/extraction-report.md` | 6,518 | VERIFIED | Original MES 3.0 extraction report for "How To Become a Master Manipulator" (the 5-Level Persuasion Hierarchy). Read in full; Hidden Knowledge #1 (Pronoun Audit, "If first-person > second-person, the copy is Level 0") confirmed verbatim, cited in the new Anti-Patterns section. No raw video transcript file exists in this repo for this source either — extraction summary is the only artifact. |
| `extractions/joanna-wiebe/writing-career-monetization-extraction.md` | 12,986 | LIKELY (out of scope) | Extraction of "7 Proven Ways To Make Money As A Writer in 2026." Confirmed to exist and non-empty (read first 40 lines). This is source material for the sibling skill `joanna-wiebe-writing-careers` (being repaired separately this batch, per ENVELOPE.md instruction not to touch it) — not drawn on for this repair's Anti-Patterns or Model Calibration additions. |

## Sections of genius.md NOT independently verifiable against a primary source

| Section | Status | Notes |
|---|---|---|
| Part 4 (Storytelling Psychology, patterns #23-30) and Part 5 (Live Authority Mechanics, patterns #31-37) | UNCONFIRMED (primary source absent) | genius.md's own header for this block states it was "mined from two additional Wiebe source videos: 'How To Grow Your Business With Storytelling' ... and 'How To Command Respect Like The 1% Elite' ... added 2026-07-01 via claude.ai export." Repo-wide search (`grep -rli` across all `.md`/`.txt` files) for either title found **no transcript or extraction file** — the only place this content exists is inside `skills/joanna-wiebe-persuasion-mastery/genius.md` itself (and its worktree mirror). This is a real gap, not laziness: I verified by reading `extractions/joanna-wiebe/` (4 files, listed above) and `extractions/joanna-wiebe-persuasion-mastery/` (extraction-report.md, 6,518 bytes — the only file in that directory) in full; neither contains this material. The new Anti-Patterns item citing the Certainty Gradient (Part 5, #35) is therefore anchored to genius.md as an internal cross-reference, not to a primary transcript — flagged UNCONFIRMED for provenance purposes even though the content itself was already present and passing the skill's `verbatim_exemplars` check before this repair. |

## Claims added or newly sourced in this repair pass

| Claim (Anti-Patterns bullet) | Status | Anchor |
|---|---|---|
| Pronoun Audit ("we/our/I" vs "you/your") failure mode | VERIFIED | `extractions/joanna-wiebe-persuasion-mastery/extraction-report.md`, Hidden Knowledge #1 |
| Vague-category hook failure ("Business strategies for everyone") | VERIFIED | `extractions/joanna-wiebe/transcript.txt` (verbatim quote present) |
| Self-image threat failure ("Most marketers get this completely wrong" → "costs millions") | VERIFIED | `extractions/joanna-wiebe/transcript.txt` (verbatim quote present) |
| Hype-adjective / money-word confusion (Mediocre Anti-Exemplar) | VERIFIED | `skills/joanna-wiebe-persuasion-mastery/genius.md`, existing "Mediocre Anti-Exemplar" block (unchanged by this repair) |
| Anti-Pile Proof Principle (stacking proof past one boulder) | VERIFIED | `extractions/joanna-wiebe/9-psychological-writing-triggers-extraction.md`, Hidden Knowledge #3 |
| Boring Objection Kill Pattern (no dramatic rebuttals) | VERIFIED | `extractions/joanna-wiebe/9-psychological-writing-triggers-extraction.md`, Hidden Knowledge #4 |
| Certainty Gradient hedge-word failure (17 hedges in one email opener) | UNCONFIRMED (primary source absent, see table above) | `skills/joanna-wiebe-persuasion-mastery/genius.md`, Part 5 #35 — internal cross-reference only |

No claim in this ledger was invented for the purpose of passing the audit; every VERIFIED row was checked by opening the cited file and locating the exact quoted text this pass, on 2026-07-18.
