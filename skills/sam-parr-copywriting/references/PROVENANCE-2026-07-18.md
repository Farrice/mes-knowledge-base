# PROVENANCE — sam-parr-copywriting repair (wave3-lane4-b15)

Anchor → source file + location, for every quote added to genius.md in this repair.

| Anchor (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "A lot of the incentives are just to like shove the benefits in your face" | `extractions/sam-parr/transcript.txt` | Mid-transcript, discussion of DR-ad incentive structure (`grep -o -i ".\{80\}shove.\{80\}"` match). |
| "the man was sad, he wanted to go fish" | `extractions/sam-parr/transcript.txt` | Hemingway / Old Man and the Sea rhythm passage. |
| "imagine storing your food in the toilet bowl" | `extractions/sam-parr/transcript.txt` | Caraway/Tupperware live-rewrite passage (same exemplar already used in genius.md Exemplar 3). |
| "Now everything I just said was fake. I don't know if that's true." | `extractions/sam-parr/transcript.txt` | Immediately after the AG1/AGZ sleep-supplement live rewrite (same moment already cited in genius.md's Non-Negotiable Guardrail and Exemplar 2). |
| "There's no such thing as too long, just too boring." | `extractions/sam-parr/transcript.txt` | Discussion of ad length vs. engagement. |
| 2026-05-30 extraction date | git history | `git log --diff-filter=A --format="%ad %h" --date=short -- extractions/sam-parr/copywriting-extraction.md` |

All five quoted anchors were independently re-verified by this worker via direct
`grep -o -i` substring search against `extractions/sam-parr/transcript.txt` — not taken
on the predecessor's word. The predecessor's one verified claim (the "shove the
benefits" quote) was spot-checked and confirmed identical to the live transcript text.

No claims of source absence were required for this repair — `extractions/sam-parr/`
contains three non-empty files (sizes recorded via `wc -c` in
`references/source-ledger.md`), so the tarball fallback scan was not triggered.
