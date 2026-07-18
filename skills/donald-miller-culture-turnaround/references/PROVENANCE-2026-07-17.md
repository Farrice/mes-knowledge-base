# Provenance — donald-miller-culture-turnaround Wave 3 Lane 4 Batch 5 Repair

Anchor → source file+location for every new/changed claim introduced by this repair (2026-07-17). Full claim-by-claim ledger with VERIFIED/LIKELY/UNCONFIRMED labels lives in `references/source-ledger.md`; this table is the quick anchor index.

| Anchor (as it appears in genius.md) | Source file | Location / identifying text |
|---|---|---|
| BELAY quote: "It's years of you guys repeating it to train our brains to think that... there's actually a business strategy and identity involved." | `extractions/Donald Miller/transcript.txt` | Search term "years of you guys repeating it"; BELAY/Trisha Shurtino case-study segment |
| Chick-fil-A "my pleasure" 3-year campaign + David Salyers | `extractions/Donald Miller/transcript.txt` | Search term "David Salyers" |
| Chick-fil-A collateral/sales-scripts/breaking-lifelong-habits detail | `extractions/Donald Miller/transcript.txt` | Same passage, immediately following the David Salyers quote |
| Liked-vs-respected leadership quote | `extractions/Donald Miller Grow/transcript.txt` | Search term "trying to be liked" |
| Coffee-shop cognitive-load before/after (18 clicks -> 125 clicks, 600% increase) | `extractions/donald-miller/transcript.txt` | Search term "losing baristas" |
| "The confused mind says no" | `extractions/donald-miller/transcript.txt` | Search term "confused mind says no" |
| PEACE framework verbatim breakdown | `extractions/donald-miller/transcript.txt` | Search term "peace framework" |
| Three-step-plan sequencing quote | `extractions/Donald Miller Grow/transcript.txt` | Search term "three-step plan" |

## How these were verified

For every anchor, the exact phrase was located with a direct string search inside the transcript file (`python3` regex search over the full file text, since these transcripts are single-block text with no paragraph line breaks) and read in ~300-character surrounding context to confirm speaker and topic before use. Byte sizes of all three source files were recorded (34,611 / 44,426 / 45,960 bytes) to confirm none are empty or truncated.

## Negative-finding verification (absence claims)

Before labeling anything UNCONFIRMED, the following terms were searched across all three transcript files AND the whole `extractions/` directory tree, and confirmed absent (not merely "not read"): `Cignetti`, `James Madison`, `JMU football`, `thousand-page binder`, `privilege` (0 hits), `unsurprised` (0 hits), `negativity` (0 hits), `micromanage` (0 hits). Positive hits for the standalone word "thousand" (3 occurrences, all unrelated to a documentation binder) were individually read in context and confirmed not to support the Pattern 3 claim.

## Contamination check

`git status --porcelain skills/donald-miller-culture-turnaround` was run before and after this repair pass — no writes were made to `skills/`. All changed files were written only under `.tmp/wave3-lane4-b5/donald-miller-culture-turnaround/`.
