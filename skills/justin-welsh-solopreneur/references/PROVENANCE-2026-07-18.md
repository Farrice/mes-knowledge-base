# Provenance — justin-welsh-solopreneur repair (2026-07-18, REDO pass)

Anchor → source table for every quote/claim touched this pass. All source files were
extracted via `python3 tarfile` from `_archive/claude-export-2026-07-01.tar.gz` to
`.tmp/wave3-lane4-b8/_welsh-extract/` (never `skills/`, never committed) and read
directly — not inferred, not assumed absent.

| Anchor (in repaired `genius.md`) | Source file | Location | Verification |
|---|---|---|---|
| "It's not like something that you go on a treasure hunt for. You don't like uncover rocks..." | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~5:33-5:35 | VERIFIED |
| "you don't do that thing if you haven't done that thing" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~9:54 | VERIFIED |
| "it's not clickbait in the headline if you deliver" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~33:04 | VERIFIED |
| "How many asks? Usually, just one." | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~32:50 | VERIFIED |
| "it pays to be clear, not clever" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~33:48 | VERIFIED |
| "the best way to build a habit is just stick with it" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~29:07 | VERIFIED (corrects prior pass's "just stick with your habits") |
| "don't force yourself to write about... the stuff that past you cared about" | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~14:16-14:20 | VERIFIED |
| "I try and build a lifestyle that generates income" | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~14:03-14:09 | VERIFIED |
| "they force me to barter for it... it's not free then" / "not a bartering experience" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~36:45-37:48 | VERIFIED (corrects prior pass's invented single-sentence "if you tell me it's free, don't make me barter for it") |
| "a fifth grader could understand it" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~27:12-27:14 | VERIFIED |
| "a lot of juice and not a lot of fluff" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~27:36-27:41 | VERIFIED |
| "I call it think once, publish 10 times" | `502221c3-f71b-473f-8ef6-d7c7227281f2.md` | Single non-timestamped transcript block (human message) | VERIFIED |
| Revenue stack breakdown (~65/10-12/10/5/5), $9/mo upsell, "$24,000 MRR," "one email" | `502221c3-f71b-473f-8ef6-d7c7227281f2.md` | Same transcript block | VERIFIED |
| "permissionless apprenticeship" (attributed to Jack Butcher by Welsh) | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~42:43-42:47 | VERIFIED |
| No employees / ~$600/month / $5M+ revenue / politics-legal-vacation-benefits-performance-management | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~9:38-11:04 | VERIFIED |
| "almost like a second mountain" | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~2:49 | VERIFIED |
| "the great creative migration" | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~1:38, ~36:24 | VERIFIED |
| "much in part thanks to me" | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~8:32-8:36 | VERIFIED |
| $100K ARR + 12K subscribers (video intro) vs. 8K subscribers/1,300 words (in-interview recap) | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~0:15-0:25 (intro) and ~5:21-5:32 (recap) | VERIFIED, with noted internal inconsistency between the two figures — both are genuine source text, not fabricated |
| "already written 30 issues... 30% of the year ahead" | `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | ~42:22-42:35 | VERIFIED |
| "say the same thing five different ways" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~38:50-38:57 | VERIFIED |
| "all advice is contextual, mine included" | `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | ~43:34-43:41 | VERIFIED |
| Data × Passion 90-Day Audit (5-7 topics, quarterly) | No matching source found | n/a | LIKELY (synthesis, not verbatim — see source-ledger.md) |
| "therapist to myself... yelling at myself," "do I truthfully believe this," "hollow" | Searched all 6 sources, zero matches | n/a | UNCONFIRMED — de-quoted and removed from genius.md this pass |

## Why the corrected quotes are safe edits, not new fabrication

The two corrected quotes ("just stick with it," the barter passage) replace
paraphrase-presented-as-verbatim with the actual transcript wording found at the cited
timestamps — a tightening toward the source, not a new claim. The de-quoted insight
(formerly "The Content Is Self-Therapy") had its specific quoted language removed
entirely rather than replaced with an invented substitute; the surviving prose in
"Personal Change Sets the Content Agenda" is built only from the VERIFIED "past you
cared about" quote plus non-quoted framing.

## Recognition-test language (already present, unchanged this pass)

`genius.md` "How to Use This Skill (Model Calibration)," line 5: "The test: would Welsh
recognize this as theirs — a builder writing from actual receipts and a lived operating
rhythm — or as someone using solopreneur vocabulary? If it's the second, rebuild." This
satisfies `recognition_test` and was not modified this pass beyond the line-11 fix
(swapping an unconfirmed quote for the VERIFIED "all advice is contextual, mine
included" line).
