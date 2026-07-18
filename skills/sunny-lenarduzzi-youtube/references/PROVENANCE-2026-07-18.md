# PROVENANCE — sunny-lenarduzzi-youtube repair

No `extractions/` entry exists for this expert (`ls extractions/ | grep -i lenarduzzi` and `grep -i sunny` both 0 results). Ground truth recovered via full per-member content scan of `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, `wc -c`; 7,728 members; 49 matched "lenarduzzi"). Full method and file-by-file claim ledger: `references/source-ledger.md`.

## Anchor → source table (new content added this pass)

| Anchor (genius.md location) | Source file (in tarball) | Location |
|---|---|---|
| Model Calibration section — Denver $1.36M/2,632 subs example | `.../8585118b-0e92-4a8d-b3da-430676367a5b.md` | timestamp 1:13–1:20 |
| Model Calibration section — Todd $500K/536 subs example | same file | timestamp 1:23–1:25 |
| CODE Sequence — Jeffrey $1.2M/18 months/$10M-in-4-years Real Example | `.../b17fabc8-4c47-4d3b-bbce-f29475fa0d44.md` | timestamp 2:36–2:51 |
| Reverse Funnel Hockey Stick — Source Anchor quote | same file | timestamp 11:01–11:20 |
| Five-Factor Topic Validation — Source Anchor ("the truth about winning your wife back") | same file | timestamp 15:29–16:59 |
| Congruent Metadata Insight — verbatim quote + flag warning | same file | timestamp 30:51–31:01 |
| Anti-pattern: "building the program before talking to real people" | `.../85bd453b-6646-4a1b-a7d4-774d37e73353.md` | conversation created 2025-12-18, "worst mistake" passage |
| Anti-pattern: "pricing on time instead of transformation" | same file | conversation created 2025-12-18, "Common mistake" passage |
| Anti-pattern: "teaching everything — expert's curse" | same file | conversation created 2025-12-18, "experts curse" passage |
| Anti-pattern: "posting content with nothing to sell" | `.../e970b085-8411-430a-9899-4a7ab0e6eed9.md` | conversation created 2026-02-25 |
| Anti-pattern: "running every growth lever at once" | same file | conversation created 2026-02-25 |
| Anti-pattern: "keyword-stuffing tags" | `.../b17fabc8-4c47-4d3b-bbce-f29475fa0d44.md` (youtube.com/watch?v=swBwRtHVVlA) | timestamp 30:51 |

All quotes reconstructed from SRT-style auto-transcripts by stripping inline `MM:SS -` timestamp tokens; no words were altered. Verify by opening the cited tarball member and searching the timestamp.

## Flagged gap (not fixed — pre-existing passing content, additive-first boundary)
- genius.md's Zero to Hero Program Packaging pattern (unchanged, was already passing the entity check) contains "Mike: 50 interviews → 32 clients → $89K in 30 days." The Mike/restaurants/$89K facts are VERIFIED (`c8390c2b-1447-4578-89fd-acf309ef66a0.md` and `ef4f510a-b13c-42ea-aa8e-48635bbfd064.md`), but "50 interviews," "32 clients," and "30 days" (vs. the sourced "3 weeks") were not located in any of the 10 files pulled. Left untouched per the "never rewrite passing content" boundary; flagged UNCONFIRMED in `references/source-ledger.md` instead. A future pass with a fuller re-source should either find the exact quote or replace it with the verified "3 weeks" figure.
