# Provenance — russell-brunson-funnels repair

Ground truth located via name-fragment search (`grep -ril brunson`) which found no `extractions/russell-brunson*` dir. Traced instead through `_active/claude-export/harvest/census-full.json` (expert="Russell Brunson", 10 conversation ids) to the raw tarball `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes). Used `python3 tarfile` to scan and extract the 10 matching conversation markdown files from `claude-export/normalized/conversations/<id>.md` — sizes recorded in `references/source-ledger.md`. Every quote cited below was read directly from the extracted transcript text, not from memory.

## Anchor → Source Table (new content added this repair)

| Anchor in genius.md | Source file (extracted from tarball) | Location |
|---|---|---|
| "a lot of times we get in the mistake of trying to sell the process..." | 156c576f-536b-4a6d-a33b-3b5efd30b38e.md | 8:41-8:48 |
| "believing their own bio" / 100-employee crash | c6416fe8-9783-478c-ad64-42d7577d26d4.md | 6:44-7:19 |
| Bernays WWI war bonds, "features and the benefits... logically" | 0a89743f-81f6-47cc-b539-86345323a94f.md | 1:41-1:58 |
| propaganda → public relations rename | 0a89743f-81f6-47cc-b539-86345323a94f.md | 8:31-8:43 |
| "not based on ideas or hoping stuff work" | 156c576f-536b-4a6d-a33b-3b5efd30b38e.md | 11:29-11:36 |
| Nautilus / 200,000 copies vs. "20 copies... Facebook, Instagram" | e111041c-a359-43db-9a42-6d7c481470c1.md | 9:07-9:20 |
| "you got to grab their attention first" | 156c576f-536b-4a6d-a33b-3b5efd30b38e.md | 7:21-7:22 |
| "torches of freedom" cigarette campaign | 0a89743f-81f6-47cc-b539-86345323a94f.md | 3:46-4:32 |
| Irving Allen / 10 Basic Laws / healthy egotism | c6416fe8-9783-478c-ad64-42d7577d26d4.md | 0:20-2:34, 4:07 |
| "grain of truth... not the same outcome" | 156c576f-536b-4a6d-a33b-3b5efd30b38e.md | 4:43-4:46 |
| shower / concentrated-thought | b7261d84-0983-405d-9940-8244bff594d4.md; e111041c-a359-43db-9a42-6d7c481470c1.md | 6:30-6:37; 6:23-6:28 |
| $12,500 for first-edition *Propaganda* | 0a89743f-81f6-47cc-b539-86345323a94f.md | 0:05 |

No claims of "source absent" were made — every existing genius.md quote checked this pass resolved to VERIFIED or LIKELY against the extracted transcripts (see `references/source-ledger.md` for the full breakdown, including the two LIKELY entries and the reasoning).
