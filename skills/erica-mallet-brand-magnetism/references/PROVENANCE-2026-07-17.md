# Provenance — erica-mallet-brand-magnetism repair (Wave 3 Lane 4 Batch 5)

Anchor → source file + location. Full quote text and VERIFIED/LIKELY/
UNCONFIRMED labels live in `references/source-ledger.md`; this table is the
fast lookup from a specific line in the repaired `genius.md` to where its
claim actually comes from.

## Primary transcript, item-by-item

Source file (this repair's own retrieval, not committed to the repo):
`_archive/claude-export-2026-07-01.tar.gz` → `claude-export/raw/batch-0001/
conversations.json`, uuid `0306caa8-5469-4c3d-9096-7cf8f7e15167`, message[0]
attachment `extracted_content` (118,576 chars). Original recording:
`https://www.youtube.com/watch?v=aN02fSGO2TU` ("How to Make Your Brand So
Magnetic They Stop Scrolling ft. Erica Mallett," THE 505 PODCAST ep. 177).

| Ledger item | genius.md lines | Approx. char offset in transcript |
|---|---|---|
| T1 | 26, 149, 147 | ~0–900 (opening teaser block) |
| T2 | 58, 124, 146, 207 | ~16,479–17,399 (vegetable-in-cake / Gary Vee) |
| T3 | 67 | "zonic effect" / Mona Lisa passage (found via keyword search, not offset-recorded) |
| T4 | 115, 150, 198 | ~5,734 (on-air "cringe" backstory) and ~18,460 ("cringe mountain") |
| T5 | 42, 216, 257 | "cheat code to have two of you" passage (keyword-located) |
| T6 | 147, 257 | ~76,357 ("it's not about copying... mind of a scientist") |
| T7 | 148, 275 | ~45,668 ("be authentic is the most annoying thing") |
| T8 | 171 | ~33,261–33,692 (enemy effect, Andrew Tate / Taylor Swift) |
| T9 | 180, 189, 266 | "themes" / Gary Vee vs. Alex Hormozi passage (keyword-located) |
| T10 | 225 | "platform" / YouTube passage (keyword-located; quote runs past captured window) |
| T11 | 248 | "connection economy" passage (keyword-located) |

## Live web, item-by-item

| Ledger item | genius.md lines | URL | Retrieved |
|---|---|---|---|
| W1 | (source-ledger only; bio context) | `https://www.ericamallett.com/` | 2026-07-17, via WebFetch |
| W2 | 58 | `https://www.ericamallett.com/themagneticedge` | 2026-07-17, via WebFetch |
| W3 | 150, 151 | `https://realbusinessconnections.com/podcast/ericamallett/` | 2026-07-17, via WebFetch |
| W4 | (existence confirmation only) | WebSearch results: Spotify/Apple/RedCircle episode 177 listings, `youtube.com/@ericamallett`, `linkedin.com/in/erica-mallett-ab7232a0` | 2026-07-17, via WebSearch |

## In-repo LIKELY sources

| Ledger item | genius.md lines | File |
|---|---|---|
| L1 | 83, 162, 284 | `skills/erica-mallet-brand-magnetism/references/prompts-v2/crown_jewel_prompt_1_belief_architecture.md` line 50 |
| L2 | 106 | `skills/erica-mallet-brand-magnetism/references/prompts-v2/crown_jewel_prompt_7_tone_filter.md` lines 11–51 |
| L3 | 189 | Skill's own pre-existing `genius.md` Pattern 7 / Tacit 4 text (no external transcript match found) |

## Illustrative / non-factual

| Ledger item | genius.md lines | Note |
|---|---|---|
| U1 | 290–319 | Hall of Fame Exemplars — composite, not real people. Pre-existing content, now labeled inline. |

## Absence verification trail (commands actually run this pass)

```
ls extractions/ | grep -i mallet                     # → zero results
find _active/codex-harvest-2026-06-11 -iname "*mallet*"  # → agents/erica-mallet/AGENT.md (8,285 bytes)
                                                          #   skills/erica-mallet-brand-magnetism/ (mirror, +2 unshipped sections)
tar tzf _archive/claude-export-2026-07-01.tar.gz | grep -i mallet   # → zero filename hits (expected: it's one big JSON)
tar xzOf _archive/claude-export-2026-07-01.tar.gz | grep -a -c -i mallet  # → 252 content hits
wc -c _archive/claude-export-2026-07-01.tar.gz       # → 332,779,255 bytes
```
Full transcript then recovered via targeted `ijson` streaming pull of the
single matching conversation object (867MB source JSON; see
`references/source-ledger.md` for the exact retrieval method).
