# PROVENANCE.md — seth-godin-ideavirus repair (Wave 3 Lane 4 Batch 16)

Anchor → source file + location, for every claim added or newly cited in this repair pass. See `references/source-ledger.md` for the full VERIFIED/LIKELY/UNCONFIRMED table; this file is the flat anchor index.

| Anchor (genius.md location) | Source file | Location |
|---|---|---|
| "something that's easy to measure but not helpful" / "go in the wrong direction" | `extractions/seth-godin/transcript.txt` | char offset ~9899 (file is single-line; located via substring search for "false proxy") |
| "Permission is the idea of delivering anticipated personal and relevant messages..." / "Not spamming them, but being missed if you were gone" | `extractions/seth-godin/transcript.txt` | char offset ~1618 |
| "if you make audacious promises constantly and you don't keep them, then you're the Wizard of Oz. I don't trust you" | `extractions/seth-godin/transcript.txt` | char offset ~5560 |
| "that tendency to hit that quarterly earnings number" | `extractions/seth-godin/transcript.txt` | char offset ~11612 |
| "a real trap in a big way the me measuring the wrong thing" (rendered "the[,] measuring" — ASR artifact bracketed) | `extractions/seth-godin/transcript.txt` | char offset ~12127 |
| Gajist — "130,000 email addresses" / "We're not taking any new signups" | `extractions/seth-godin/transcript.txt` | char offset ~26406–27200 |
| "The point of perfectionism is not to make it better. It's to keep you from shipping it" | `extractions/seth-godin/extraction-report.md` | line 68, Pattern 8 ("Perfectionism as Hiding") |
| "Congratulations. You've built a perfect place to hide" / "I submitted to 20 publishers and they all turned me down" | `extractions/seth-godin/extraction-report.md` | line 133, Tacit Knowledge 5 ("The Safe Hiding Place Trap") |
| "once someone's closet is filled, the only way for them to buy new shoes is to get rid of the old ones" | `skills/seth-godin-ideavirus/genius.md` (pre-existing) | Pattern 11, 2026-07-01 dated addition — reused verbatim, not re-derived |
| "If you are not regularly sending folks to your competitors, you are not serious about picking the audience it's for" | `skills/seth-godin-ideavirus/genius.md` (pre-existing) | Pattern 15, 2026-07-01 dated addition — reused verbatim, not re-derived |
| 4/7/10 quality-rubric anchor scale | `skills/seth-godin-ideavirus/references/quality-rubric.md` | table header, "Score 4 (Acceptable) \| Score 7 (Good) \| Score 10 (Savant)" |
| "powerful sneezers" / "promiscuous sneezers" / "Magic Number" / "fashion moment" / "smoothest idea wins" terminology | *Unleashing the Ideavirus* (Godin's book, circa 2000) | NOT found in any local file under `extractions/seth-godin/` after full-text search for "sneezer," "magic number," "fashion," "smoothness," "promiscuous," "vacuum," "hive" — all zero hits. Labeled LIKELY in source-ledger.md, never presented as a file-anchored quote. |

## Absence check (rule 2 of the envelope — verified, not assumed)

Ran an exhaustive case-insensitive substring search across both `extractions/seth-godin/transcript.txt` (35,179 bytes, confirmed with `wc -c`) and `extractions/seth-godin/extraction-report.md` (17,901 bytes) for: `sneezer`, `magic number`, `monetiz`, `fashion`, `promiscuous`, `vacuum`, `hive`, `smoothness`. Zero hits for all eight terms in both files. This is the basis for labeling the pre-existing 8-Variable Framework (Patterns 1–10, Tacit Knowledge 1–2, 6–7) as LIKELY rather than VERIFIED — the terminology is real and well-documented (Godin's own published book), but not recoverable from this repo's local extraction files.
