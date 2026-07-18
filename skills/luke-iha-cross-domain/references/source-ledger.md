# luke-iha-cross-domain — Source Ledger

> Ground-truth audit for `genius.md`. This skill is orchestration-layer only — it sequences the six specialist Luke Iha skills rather than teaching new frameworks, so the sourcing question is: are the anchored claims in `genius.md` genuinely traceable to the same extraction files those specialist skills were built from? Labels: **VERIFIED** (opened directly this pass, quote confirmed verbatim against the file) · **LIKELY** (file exists, on-topic, backs a sibling specialist skill, not re-diffed line-by-line this pass) · **UNCONFIRMED** (claimed or implied, no backing file in the extraction set).

## VERIFIED — opened directly, quotes checked verbatim

| File | Size | Covers | Used for |
|---|---|---|---|
| `extractions/luke-iha/extraction-report.md` | 7,915 bytes | 22 proof weapons, "$100M generated with VSLs" byline | Core Engine section entity/quote |
| `extractions/luke-iha/video-2-creative-strategy/extraction-report.md` | 8,409 bytes | Nuclear VSL, Over-Delivery Flywheel, Platform Leverage Ladder | Anti-Pattern: premium-before-proof · Anti-Pattern: hypothetical brands · "the work itself IS the pitch" |
| `extractions/luke-iha/video-6-offer-cycling/extraction-report.md` | 8,762 bytes | Agency Ladder, Category of One, Offer Cycling (video ID 2aEmSn7sypE) | Anti-Pattern: broad positioning · Category of One quote/exemplar |
| `extractions/luke-iha/video-7-million-dollar-mechanisms/extraction-report.md` | 13,953 bytes | UMP/UMS, SIN Framework, Characterization, Mechanism Validation Triangle (video ID 3B3nQNDWVWk) | Checkpoint Discipline pattern · SIN quote · Characterization quote · HK3 complexity quote |

## LIKELY — exists, on-topic, backs the sibling specialist skills this orchestrator sequences, not re-read this pass

| File | Size | Note |
|---|---|---|
| `extractions/luke-iha/video-4-copy-blocks/extraction-report.md` | 8,971 bytes | Backs `luke-iha-copy-blocks` (CASH Method, Hook Forge) — already VERIFIED in that skill's own source-ledger.md |
| `extractions/luke-iha/video-5-vsl-leads/extraction-report.md` | 10,102 bytes | Backs `luke-iha-vsl-leads` (micro leads, fascination bullets) |
| `extractions/luke-iha/video-3-levels-of-awareness/extraction-report.md` | 13,497 bytes | Backs `luke-iha-unaware-ads` (awareness-level targeting) |
| `extractions/luke-iha/video-1-proof-mechanisms/extraction-report.md` | 6,936 bytes | Backs `luke-iha-proof-mechanisms` / `luke-iha-proof-ladder` |
| `extractions/luke-iha/video-8-proof-ladder/extraction-report.md` | 17,119 bytes | Backs `luke-iha-proof-ladder` (5-tier proof hierarchy) |
| `extractions/luke-iha/transcript.txt` | 32,648 bytes | Root raw transcript; distilled root `extraction-report.md` above is the version actually quoted |

## UNCONFIRMED — the honest gap

- **"Cross-domain orchestration" as a framing Luke Iha himself taught**: no file in `extractions/luke-iha*` presents the six skills as an explicit sequenced pipeline with named checkpoints. The Phase 1→5 structure in `workflows/full-stack-ad-campaign.md` and the analogous structures in the other three workflows are Antigravity's synthesis of individually-taught frameworks (SIN, CASH, micro leads, awareness ladder) into a chained pipeline — not a direct Iha teaching. The individual pattern claims cited above (SIN threshold, Characterization naming, Agency Ladder, Nuclear VSL, Category of One) are each VERIFIED against their source file; the act of chaining them into "Phase 1/2/3/4/5" is the skill's own construction, flagged here so it is not mistaken for something Iha said verbatim.
- **`extractions/luke-iha-creative-strategist/transcript.txt`** and **`extractions/luke-iha-insight-mastery/transcript.txt`**: exist, on-topic by folder name, not opened this pass — no claim in this genius.md rests on them.

## How this ledger was built

Read the root `extraction-report.md` plus `video-2-creative-strategy`, `video-6-offer-cycling`, and `video-7-million-dollar-mechanisms` extraction reports directly (byte sizes above via `wc -c`). Every anchored quote in `genius.md`'s Anti-Patterns and Verbatim Exemplars sections was matched against these four files before being written; none was paraphrased into a false verbatim. The other five `extractions/luke-iha/video-*` reports and the `luke-iha-creative-strategist`/`luke-iha-insight-mastery` transcripts were not opened this pass — they back sibling specialist skills, not claims made here — and are labeled LIKELY/UNCONFIRMED accordingly rather than silently treated as checked.
