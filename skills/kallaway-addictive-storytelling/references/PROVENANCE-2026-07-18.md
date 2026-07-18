# Provenance — kallaway-addictive-storytelling repair (2026-07-18)

Anchor → source file+location table. All anchors point to either (a) a real file+location confirming the fact, or (b) the source-ledger.md UNCONFIRMED entry when no recoverable source exists.

| Anchor added in genius.md | Points to | Verification |
|---|---|---|
| Header "Source Verification" note | `references/source-ledger.md` (this repair) | VERIFIED — file exists at stated path, sizes confirmed via `wc -c` (see ledger table) |
| Anti-Pattern 1-8 dated anchors ("Pattern N ... extracted 2026-04-22") | genius.md's own Evolution Log, row `2026-04-22 \| Initial extraction ...` (unchanged, pre-existing content in this file) | VERIFIED — the date and pattern numbers are internal facts about this file's own history, not external claims about Kallaway |
| "claude.ai-export enrichment pass" note on Pattern 12 | genius.md Evolution Log row `2026-07-01 \| Enrich from claude.ai export ...` (unchanged, pre-existing) | VERIFIED as an internal-file fact; the underlying archive content itself is UNCONFIRMED (see source-ledger.md) |
| `_archive/claude-export-2026-07-01.tar.gz` size citation (332,779,255 bytes) | `_archive/claude-export-2026-07-01.tar.gz` | VERIFIED via `wc -c` — file exists, size confirmed; contents not searched at quote level |
| "1 incidental dopamine mention" in `extractions/kallaway-content-system/transcript.txt` | that file, grep hit | VERIFIED via `grep -io dopamine extractions/kallaway-content-system/transcript.txt` |
| "3 incidental dopamine mentions" in `.../B9l9TRhu5Vw.en-orig.vtt` | that file, grep hit | VERIFIED via same grep command |
| All 8 file sizes in source-ledger.md table | respective files under `extractions/kallaway/` and `extractions/kallaway-content-system/` | VERIFIED via `wc -c` on each file, run 2026-07-18 |
| Named-entity fixes (Core Genius, What Makes This Different, Pattern 12, Quality Rubric) | genius.md's own pre-existing content (Pattern 1 success metric quote, 7-criterion rubric table, evolution log dates) | VERIFIED — self-referential to already-present, unaltered content in this same file; no new external claim introduced |

No new claims about Kallaway's actual video content, quotes, or biography were introduced anywhere in this repair. Every addition either (1) cites this repair's own verification work, (2) cites this file's pre-existing internal history, or (3) is explicitly labeled UNCONFIRMED.
