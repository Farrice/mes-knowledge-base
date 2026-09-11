# Pipeline Readout — `/jen-engine` run on Gigi Mironova · 2026-09-01 · operator only

**Nothing in this file goes to Gigi.** It answers one question: what does the 7-stage pipeline built for Jen do when it is pointed at a teammate with a fraction of Jen's context? Run in `--dry-run` (neither human gate fired; Farrice judges the finished artifacts instead).

## The one-line answer

The pipeline runs end to end on thin context and produces a complete, lint-clean, ledger-backed package. What thin context costs is **voice confidence**, not output. Every artifact after Stage 1 is as strong as Jen's would be, because Stages 2–7 run on research and documents, not on the agent. Stage 1 is the only stage that needs her, and the pipeline made that visible instead of papering over it.

## What Jen has that Gigi does not

| Input | Jen | Gigi |
|---|---|---|
| Verbatim voice on disk | scraped reel transcripts, 30,606-message register atlas (Farrice's own), 4 shipped listing packages, a calibration log with her felt verdicts | 3 sentences of her own, 1 brokerage bio paragraph, 2 Yelp reviews |
| Register ruling | her own (2026-08-05, two lanes, split by price) | inferred from 3 sources that happen to agree |
| Intake | 22-question form sent, not yet returned | never sent |
| Client CLAUDE.md, CANON.md | yes | no |
| Live listing to anchor on | several, with shoot sheets | one, and it is the perfect one |
| Relationship | wife | warm teammate; gift-with-offer |

## Stage by stage

**Stage 1 · Brain load.** `VOICE.md` and `BRAIN.md` were built from public material and labeled by confidence (MED on the dials, LOW on cadence). One register instead of Jen's two: her book is entry-price condos and leases; the luxury lane does not exist for her and was not invented. The file names exactly which intake questions replace which inferred sections. *This is the stage that would have paused at Gate 1 in a live run, and it is the only stage where thin context shows.*

**Stage 2 · Demand research.** 3,300 words, every phrase sourced (raw autocomplete JSON read in-browser, Reddit titles via search index, leginfo, Freddie Mac, Redfin). Three findings changed the plan:
1. **A ledger catch.** Both earlier Gigi lanes built their math on $319,999 and a $477 HOA figure recorded on another unit. The live listing today reads **$299,999 and $620/mo dues**. Confirmed by Playwright on Redfin before a single script was written. The math moved from $2,515 to $2,535 and the "recorded for this building" rail became unnecessary: the dues are on her listing. *This is the pipeline doing its job: facts route through research, not through memory of prior lanes.*
2. **SB 410 (VERIFIED, in force 2026-01-01)** puts the balcony inspection report in every condo seller's disclosure packet. Nobody local is covering it. Her listing's own text says "inspection and repairs completed." That is a content lane she owns by accident.
3. **Team dedup.** Jen's September slate (sibling lane, today) covers the Aug 3 condo review, the East Valley rail, and the FAIR plan. The pipeline tagged those SHARED-WITH-JEN; Gigi's calendar takes the condo review once from the listing-agent side, sequenced after Jen's post, and does not touch the other two. *Nothing in `/jen-engine` handles two agents on one team; this run did it by hand. See Forge Radar.*

**Stage 3 · Calendar.** 20 videos, 4 themed weeks (the condo file · the report in your file · selling with a tenant · the transaction explained), 10 ★ VISUAL, three to film first, three batch sessions. Every entry carries a Ledger line saying which numbers may be spoken and which go in captions with a label. Four Gate 2 questions are written where they would have fired.

**Stage 4 · Scripts.** Two Opus executors, ten videos each, same VOICE.md, negative-briefed. Both ran the fair-housing lint (PASS) and the prose classifier, removed em-dashes, and reported their weakest video. Pack A's own verdict: Video 8 rests on her opinion alone because the ledger forbids statistics there, which is exactly where thin context bites. Pack B: see `SCRIPT-PACK.md` header.

**Stage 5 · Carousel specs.** Ten sets, 61 slides, written by the conductor (one author per body). Copy lives in `slides.json`; the brief is `CAROUSEL-SPECS.md`.

**Stage 6 · Design.** Rendered here, not handed to Claude Design: `gen_slides.py` → `render.py` → `review_sheet.py`. Visual system: the shared editorial floor keyed to her (warm paper, band navy, one clay mark), carried from the "Calm Closer" pass in the earlier lanes, with square corners and no shadows so it meets the banlist. Her name outranks the brokerage lockup on every board. Reviewed on the grid; three defects found and fixed in one pass (hook headline floating mid-frame, translucent fact card, cramped stat unit).

**Stage 7 · Send.** `SEND-PACKAGE.md`: one forwardable message, reader-only language, pick-one options, the don't-say list, the three scripts to film first. Fair-housing lint and prose classifier run on the send text (receipts below).

## Lint receipts

| Artifact | fair_housing_lint | prose_classifier |
|---|---|---|
| All 61 slides' copy (`.tmp/gigi-carousel-copy.md`) | PASS, context=package | FLAGGED 10/10 on five signals, all slide grammar: caps eyebrows ("town crier"), numbered rows ("parallel structure"), short labels ("aphoristic endings"), the listing's own HOA inclusion list ("gerund tails"). No em-dashes, no banned vocabulary. Judged, not rewritten. |
| SCRIPT-PACK-A.md | PASS, context=script | FLAGGED on scaffold artifacts after 45 em-dashes removed; zero exclamation marks, zero banned phrases (executor's receipt) |
| SCRIPT-PACK-B.md | see executor receipt in `SCRIPT-PACK.md` header | same |
| SEND-PACKAGE.md | PASS, context=package (one WARN on "quiet neighborhood", which is inside the don't-say list as a banned phrase); `client_package_lint.py` PASS, 0 findings | FLAGGED 7/10: list structure, "slide"/"carousel" repeated in the story sequence, the sign-off. Judged. |

**Finalize receipt (chain_runner, 2026-09-01):** logged to Notion; generic scorer read the client-facing send text alone and returned intent 4 / expert 5 / adversarial 7, with a grounding flag for "14 factual claims with zero source URLs." The send text carries no URLs on purpose (reader-only, zero operator language); every number in it traces to `DEMAND-REPORT.md` and `../BRAIN.md`, which the scorer did not read. Same disagreement the codex gift-package lane logged on 2026-08-31. Preserved here rather than converted into a false green. Judging page: https://claude.ai/code/artifact/011fa032-4c68-49df-ab79-5131f5d7bc6b

## What the run cost

- Paid API: **$0.** Web research via free search and Playwright; Reddit's bot check was respected, not bypassed; Fannie Mae's PDF 403'd and its dates stayed LIKELY.
- Subagent dispatches: 3 (demand research, scripts A, scripts B). Conductor did Stages 1, 3, 5, 6, 7 and the readout.
- Wall clock: roughly 2 hours from kickoff to send package.

## What would change with her intake (the honest gap list)

1. **Cadence and word choice.** Every script is written toward three of her sentences. Ten minutes of her talking would replace the inferred dials with hers.
2. **The Russian lane.** Three videos and two carousel sets are in Russian, drafted by a non-native writer and flagged as hers to correct. If she does not want the lane, they park and the calendar is 17 videos in English.
3. **Her farm.** The neighborhood ranking is reconstructed from where her posts sit, not from her. The calendar leans on her listing's building; her answer to "where do you actually want business" would redistribute weeks 3–4.
4. **Rights on the unit photos.** She is the listing agent; she grants them. Until she does, the seven MLS frames are a drop-in.
5. **The live price.** $299,999 and $620 are on Redfin today. She confirms before Video 1 films.

## Prior work this run stands on (do not rebuild)

- `_active/clients/_shared/realtor-editorial-system/DESIGN.md` — the floor
- `.tmp/codex-worktrees/gigi-character-rebuild/_active/clients/gigi-mironova/` — Calm Closer tokens, the 4-slide Unit 124 gift, DEMAND-BRIEF, OPERATOR-NOTES (unmerged)
- `.claude/worktrees/gigi-concept/` — Same Door v1–v4 (unmerged)
- `skills/jen-engine/` — the pipeline contract this run followed

## Forge Radar (one line each, never a block)

- Missing tool: a `team_dedup` pass in `/jen-engine` Stage 2 that reads sibling agents' live slates and tags shared subjects automatically; this run did it by hand from the sibling lane.
- Missing tool: a public-material brain-load (`agent_brain.py bootstrap <handle>`) that writes a confidence-labeled VOICE/BRAIN from a scrape, so Stage 1 has a deterministic floor before intake.

## Farrice's calls (the only three things this run cannot decide)

1. **Register verdict.** Does the plain-spoken paperwork register read as her, or as a calmer version of her? Her personal post has more edge than the deck keeps.
2. **Send order.** The earlier lanes' advice stands: send the gift with no ask, let her react, name the founding rate only after she wants the thing. The send package is written that way. Confirm with Jen that showing team work to a teammate is fine before it goes.
3. **Which of the 10 carousels posts first.** The pipeline says c01 (Same door). If the price on Unit 124 is about to move again, c02 (Five pages) is the safer opener because it carries no numbers.
