# Provenance — Steven Pressfield Narrative Mastery Repair

Anchor → source file + location, for everything added or changed this pass.

| Anchor (in `genius.md`) | Source file | Location |
|---|---|---|
| AN-1 quote ("stakes are bigger... a new form, a new meaning") | `extractions/steven-pressfield/transcript.txt` | ~char offset 10,357 (Godfather midpoint passage) |
| AN-2 quote ("hero is capable of self-sacrifice... zero sum game") | `extractions/steven-pressfield/transcript.txt` | ~char offset 22,478 |
| AN-3 quote ("second act belonging to the villain... Randy Wallace") | `extractions/steven-pressfield/transcript.txt` | ~char offset 21,135 |
| AN-4 quote ("give it meaning (theme)") | `extractions/steven-pressfield/extraction-report.md` | "18. The Five Aims of a Writer" section, "What He Does Unconsciously" bullet |
| AN-5 quote ("everything falls apart... never going to get out of this") | `extractions/steven-pressfield/transcript.txt` | ~char offset 14,856 |
| AN-6 quote ("chosen to fight the champ... we can kind of see the climax") | `extractions/steven-pressfield/transcript.txt` | ~char offset 4,340–4,738 |
| AN-7 quote ("antidote to anxiety is beauty... pros has to be be[autiful]") | `extractions/steven-pressfield/transcript.txt` | ~char offset 59,037 |
| Calibration section quote (Rocky, "we can kind of see the climax") | `extractions/steven-pressfield/transcript.txt` | ~char offset 4,340 (same passage as AN-6) |
| Calibration section quote (Godfather "new form, a new meaning") | `extractions/steven-pressfield/transcript.txt` | ~char offset 10,357 (same passage as AN-1) |
| Calibration section quote ("antidote to anxiety") | `extractions/steven-pressfield/transcript.txt` | ~char offset 59,037 (same passage as AN-7) |
| Provenance note above "The Resistance — War of Art Methodology" | This repair's own finding | Documents that R1–R4 have no local primary source; see `references/source-ledger.md` |
| Source file byte counts (62,549 / 27,217) | Direct `wc -c` run this pass | `extractions/steven-pressfield/transcript.txt`, `extractions/steven-pressfield/extraction-report.md` |
| Extraction file added-to-repo date (2026-03-05) | `git log --diff-filter=A -- extractions/steven-pressfield/*` | Commit `4fb2d7fdad466ae3003dc2f0592be8b40dd30d3d`, Thu Mar 5 2026 |
| Archive search for Resistance/War of Art primary material | `_archive/claude-export-2026-07-01.tar.gz` | Python `tarfile` per-member content scan, 7,728 members, 26 matches for "pressfield" (all `claude-export/normalized/conversations/*.md`); spot-checked `874c45a5-be56-46ef-b83d-8ef47bdaf5ba.md` — third-party incidental mention, not primary source |

All quote offsets are approximate character positions in the single-line transcript file
(confirmed via `wc -c`; the file has no embedded newlines, so `wc -l` reads 0 — a
transcription-format artifact, not an empty-file signal). Offsets were located via direct
Python string `.find()` against the exact quoted substring this pass, not estimated.
