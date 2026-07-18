# Provenance — ross-minchev-digital-products repair

Ground truth located: no `extractions/` entry exists for this expert. The skill's own frontmatter (`source: claude.ai export 2026-07-01`) points at `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed by `ls -la`). Located 15 matching conversation files via `python3 tarfile` member scan for "Minchev"/"minchev" across all 7,728 archive members, cross-checked with `zgrep -a -c "Ross Minchev" _archive/claude-export-2026-07-01.tar.gz` (140 raw hits, confirming the text exists in the archive before trusting per-member reads). Extracted candidates to scratch, quote-matched with `python3 -c "re.finditer(...)"` against the exact skill text.

Full source table with sizes and VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.

## Anchor → Source Map (new Anti-Patterns section)

| Anchor (genius.md bullet) | Source file | Created | Verified quote location |
|---|---|---|---|
| "Mistake number one, building too complex..." | `claude-export/normalized/conversations/02416885-1509-4d7e-abd3-0796b6f3a753.md` | 2025-10-23 | timestamp ~11:03, quote-matched via python re.finditer |
| "Mistake number two, overpricing or underpricing..." | same file | 2025-10-23 | ~11:11-11:30 |
| "Mistake number three is no follow-ups..." | same file | 2025-10-23 | ~11:33-11:49 |
| "...just text on white pages which is it's a lazy job..." | `claude-export/normalized/conversations/3ee10b8d-e576-45f9-b884-fadd0eecba43.md` | 2025-12-24 | mid-transcript, packaging-pass section |
| "First mistake, trying multiple methods simultaneously..." | `claude-export/normalized/conversations/53cb090c-b879-426a-a6b1-0193fb29978e.md` | 2025-12-04 | "five critical mistakes" list, mistake 1 |
| "...this is the biggest mistake I see people make... Adjust weekly based on data..." | same file | 2025-12-04 | end of "five critical mistakes" section |
| "...direct product sales is extremely high due to the major retailers..." | `claude-export/normalized/conversations/3ee10b8d-e576-45f9-b884-fadd0eecba43.md` | 2025-12-24 | on-screen tool text Ross reads aloud |

All pre-existing genius.md pattern/insight quotes ("nobody's fighting for these niches," "the title is the actual targeting," "60% out of 50 bucks," "12,000 words, 85 pages, 45 complete recipes," "Facebook does the targeting for me," "vet visit is expensive") were re-verified against `3ee10b8d-e576-45f9-b884-fadd0eecba43.md` / `56732bd0-1ab9-42c1-85d8-498cfba39c92.md` (near-duplicate transcripts of the same video) during this pass — none were found to be fabricated; all carry VERIFIED labels in the new ledger.

Two LIKELY-labeled claims ("One Problem, One Solution" as a named discipline; "Speed-to-Demonstration" phrasing; "Affiliate Network Is a Free Back Office" paraphrase) are flagged honestly in the ledger as synthesis/paraphrase rather than single verbatim sentences — not demoted to UNCONFIRMED because the underlying practice is independently verified in the same transcripts.
