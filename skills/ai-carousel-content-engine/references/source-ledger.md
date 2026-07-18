# Source Ledger — ai-carousel-content-engine

Claim-by-claim provenance for anchors added during Wave 3 Lane 4 Batch 1 repair (2026-07-17).

## Primary Source

**Video**: "I Replaced My Social Media Designer With ONE AI Prompt" — Luke Carter, published 2026-05-06, https://www.youtube.com/watch?v=_3SEUgRCXX0 (duration 9:11, video ID `_3SEUgRCXX0`).

**Live-path correction (verified by real file reads, not assumed)**: `skills/ai-carousel-content-engine/references/luke-carter-video-extraction-notes.md` cites `extractions/video-context/_3SEUgRCXX0/` at repo root. That path does **not** exist in the main tree — confirmed via `find . -iname "*3SEUgRCXX0*"`, zero hits under `extractions/`. The real extraction package is filed under `_active/codex-harvest-2026-06-11/extractions/video-context/_3SEUgRCXX0/` (confirmed present, three files, real byte sizes via `wc -c`, not `wc -l`):

- `frame-notes.md` — 1,426 bytes
- `analysis.md` — 2,258 bytes
- `video-context-ledger.md` — 66,967 bytes, 506 timestamped `observed_spoken` rows + 11 `observed_visual` frame rows + 1 `uncertain_or_unavailable` row (OCR unavailable — tesseract/pytesseract not installed, per the ledger's own row)

This is real, non-fabricated source material that was simply filed in a harvest subtree rather than the path the skill's own note names. Not flagged as "source absent" — it is present and was read in full for this repair.

All quotes below were reconstructed from the overlapping rolling-caption rows in `video-context-ledger.md` (each row repeats the tail of the prior row plus new words — standard rolling-ASR-caption output) and cross-checked against `analysis.md`'s Key Claims section.

## Claim Ledger

| # | Claim / Anchor | Label | Source |
|---|---|---|---|
| 1 | "I specifically didn't want to make this fully autonomous. I wanted to make the writing automated." | VERIFIED | video-context-ledger.md rows 00:01:55.600–00:01:59.680 |
| 2 | "it's reading our entire article, and it's going to turn it into a carousel that we can then go in and design using GBT image 2" | VERIFIED | video-context-ledger.md rows 00:01:45.680–00:01:51.600 (ASR renders "GPT" as "GBT" throughout — preserved verbatim, not corrected) |
| 3 | "we say we want you to match the style exactly, but we also want where photos or illustrations appear, generate new ones that fit the copy inside the slide, rendered in the same visual style as the references, so it feels cohesive." | VERIFIED | video-context-ledger.md rows 00:04:24.400–00:04:39.280 |
| 4 | "this whole process end to end can be automated, but I think it's really important that when we are working with agents, we're not going fully autonomous mode just for the sake of it. I still want to have uh me in the loop directing and guiding the design and what the copy is saying." | VERIFIED | video-context-ledger.md rows 00:06:26.479–00:06:40.400 ("uh" filler preserved verbatim) |
| 5 | "What are the problems they're struggling with on a daily basis? And your job from a content marketing perspective is to answer them as deeply as you possibly can." | VERIFIED | video-context-ledger.md rows 00:07:06.319–00:07:16.080 |
| 6 | "creating SEO optimized, go optimized articles is incredibly important to have before you go out and create these carousels." | VERIFIED (transcript text as captured) | video-context-ledger.md rows 00:07:45.360–00:07:51.440. "go optimized" is very likely an ASR mis-hear of "GEO optimized" — flagged, not silently corrected. |
| 7 | "you are now an orchestrator of an entire marketing operation" | VERIFIED | video-context-ledger.md rows 00:08:41.599–00:08:43.919 |
| 8 | "I'm going to try and get two to three references so we can see how to treat the rest of them." | VERIFIED | video-context-ledger.md rows 00:03:19.599–00:03:44.400 (reconstructed span) |
| 9 | "check out the link in the description. We've got an entire school community" | VERIFIED | video-context-ledger.md rows 00:08:31.840–00:08:37.680 |
| 10 | Anti-pattern "turning an article into 10 disconnected tips" attributed as Luke Carter's own framing | LIKELY / inferred | No transcript row uses this phrasing. Inferred from claim #5 (his depth-over-breadth strategy framing). Labeled inferred in genius.md, never presented as a direct quote. |
| 11 | Anti-pattern "overloading each slide with paragraph text" attributed as Luke Carter's own words | UNCONFIRMED as his words | Full 506-row ledger searched — no matching statement. Grounded instead in this skill's own `references/quality-rubric.md` failure condition ("Long copy that cannot fit on a slide"), which is VERIFIED against that file. |

## Pre-Existing Source Files (unchanged, already in skill)

- `references/source-map.md` — accepted-sources table + evidence rules (already caused the pre-existing `source_ledger` PASS independent of this file).
- `references/hidden-knowledge.md`, `references/genius-patterns.md`, `references/quality-rubric.md` — the skill's own synthesized design rules, not attributed to Luke Carter; cited above only where used to ground an anti-pattern honestly labeled UNCONFIRMED-as-Carter.
