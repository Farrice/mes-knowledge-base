# Provenance — nate-b-jones-trust-architecture repair

Anchor → source file+location. Full narrative in references/source-ledger.md.

| Anchor text (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "We have to engineer deterministic bridges on top of probabilistic cores." | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/0ee5fc4c-9a58-447a-9a1e-b93f6d2c8aaf.md` | transcript lines ~68-93, spoken timestamp 1:55-2:03 |
| "It can still be functional but be completely wrong." (used compressed as "still functional but be completely wrong") | same file | transcript lines ~140-144, timestamp 4:36-4:38 |
| "there are lots and lots of shades of gray, maybe 50 shades of gray" | same file | transcript lines ~246-248, timestamp 8:19-8:21 |
| "dramatically different computes, hundreds of multiples of different computes" | same file | transcript lines ~186-189, timestamp 6:16-6:20 |
| "AI behavior depends on accumulated context ... validate as you go or else you're going to not know where you are going off the tracks" | same file | transcript lines ~274-278, timestamp 9:19-9:26 |
| "require context and learn behaviors and those disappear on a restart" | same file | transcript lines ~44-49, timestamp 0:44-0:49 |
| "there was a checkpoint there and it worked" | same file | transcript lines ~283-285, timestamp 9:39-9:41 |
| "Fraud model scores great in tests but misses real fraud" | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` | line 149, "Metric Gaming" bullet |
| Video title / date anchor "2025-09-23 transcript ... Sept 2025" | same claude-export .md | YAML frontmatter: `created: 2025-09-23T15:54:13Z`; transcript attachment title states the underlying YouTube video published "09/24/25" window |

## Full-archive search record (source-search discipline)
- `_archive/claude-export-2026-07-01.tar.gz`: 332,779,255 bytes compressed, 7,728 total tar members, 3,711 of them under `claude-export/normalized/conversations/*.md`.
- Method: `python3 tarfile.open(..., 'r|gz')` streaming single-pass iteration (stream mode — required for gz, avoids re-decompressing per member), `extractfile()` per matching member, substring search per target phrase, sizes recorded as read.
- Phrases searched: "deterministic bridges", "probabilistic core", "Vigilance Fallacy", "Insider Personnel Threat", "Subtle-Failure", "Graduated Health State", "Capability-Based Routing", "Reality Anchor", "Safe Word".
- Hits: "deterministic bridges" and "probabilistic core" → single file `0ee5fc4c-9a58-447a-9a1e-b93f6d2c8aaf.md` (34,337 bytes) — read in full, confirmed genuine Nate B Jones transcript source. "Reality Anchor" → 5 files, all confirmed unrelated to Nate B Jones by title/frontmatter (prompt-engineering frameworks, solopreneur coaching, Lulu Cheng Meservey interview notes) — none cited. All other phrases → zero hits across all 3,711 files.
- `extractions/nate-b-jones/`: 4 files read (sizes: transcript.txt 30,609B; karpathy-loop-mes-extraction.md 25,368B; smoothing-jagged-frontier-extraction.md 16,368B; turbokvant-context-engineering-extraction.md 19,104B). Only karpathy-loop-mes-extraction.md line 149 yielded a usable, on-topic quote.
- `_archive/nate-b-jones-trust-architecture.skill` (zip, 13,253B): listed via `zipfile`, contents identical to current `references/` — no new provenance.
