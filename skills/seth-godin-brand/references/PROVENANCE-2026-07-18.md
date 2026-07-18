# PROVENANCE.md — seth-godin-brand repair (Wave 3 Lane 4 Batch 15)

Anchor → source file + location, for every quote added or verified during this repair. `extractions/seth-godin/transcript.txt` is a single-line file (confirmed via `wc -c` = 35,179 bytes, `wc -l` = 0 — a raw ASR transcript with no line breaks; **`wc -l` alone would misread this as empty, which is exactly the false-absence failure mode this batch was warned against**). Character offsets below are from `text.find(quote)` against that file, read in full.

## New Anti-Patterns section (genius.md)

| Anchor quote | Char offset | Source file |
|---|---|---|
| "something that's easy to measure but not helpful" | 9,912 | `extractions/seth-godin/transcript.txt` |
| "Authenticity is overrated. Authenticity is a trap. Authenticity is for your best friend." | 12,774 | `extractions/seth-godin/transcript.txt` |
| "Not spamming them, but being missed if you were gone." | 1,728 | `extractions/seth-godin/transcript.txt` |
| "you can't cost reduce yourself to greatness" | 4,100 | `extractions/seth-godin/transcript.txt` |
| "Has it sold one Frosty? Has it sold one hamburger?" | 24,809 | `extractions/seth-godin/transcript.txt` |
| "there were 3,000 people who sat there all day long watching the stock price" | 11,250 | `extractions/seth-godin/transcript.txt` |
| "don't be an unpaid doobie for them" | 24,043 | `extractions/seth-godin/transcript.txt` |

All seven confirmed with a Python exact-substring search (`quote in text`) before being written into genius.md — not pattern-matched loosely, not paraphrased. Verification script and full transcript both re-read in this session; see `references/source-ledger.md` for the claim-by-claim table covering the pre-existing genius.md content as well (25 VERIFIED, 1 LIKELY, 0 UNCONFIRMED after a corrected second pass — see that file's history note for the 4 items initially mis-labeled LIKELY that a second grep pass confirmed as VERIFIED).

## Model Calibration section (genius.md)

No new factual claims about Godin — this section is craft-texture guidance synthesized from the existing genius.md patterns (Signature Moves 1-4, already-verified Pattern 4's flat-verdict register) and the Ben Watkins genius.md's structural precedent (`skills/ben-watkins-storytelling/genius.md` lines 7-16, read for format only, no content borrowed).

## Workflow files (10x `## Output Schema` additions)

No new factual claims — each schema section documents the field structure of that workflow's own pre-existing ASCII output block (e.g., `godin-brand-promise.md`'s "BRAND PROMISE ARCHITECTURE" block, already in the file before this repair). Source = the workflow file itself, not `extractions/`.

## Files NOT modified

`SKILL.md` — untouched. The recognition-test check passes via genius.md alone (`_HB_RECOG_RE` checks SKILL.md OR genius.md), so no edit was needed there; per the boundaries rule (additive-first, minimal-touch), it was left as-is.
