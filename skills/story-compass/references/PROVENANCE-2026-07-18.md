# PROVENANCE — story-compass repair (Wave 3 Lane 4 Batch 16)

Source of truth: `extractions/Tim Runia/transcript.txt` (14,146 bytes per
`wc -c`, confirmed present, single file in that directory). No second Runia
source exists — `ls extractions/ | grep -i runia` and `grep -i "tim runia"`
returned only this one directory before repair began.

## Search discipline (per envelope SOURCE-SEARCH DISCIPLINE)
- `ls extractions/ | grep -i runia` → `Tim Runia` (only hit)
- `ls "extractions/Tim Runia/"` → `transcript.txt` only, 14,146 bytes
- `_archive/claude-export-2026-07-01.tar.gz` per-member content scan for
  fragments "Tim Runia", "story compass", "compass sentence" — not run this
  pass because the primary source (`transcript.txt`) was already sufficient
  to source every claim added; no absence claim is made about the archive
  (it was not scanned, so nothing is asserted about what it does or doesn't
  contain).

## Anchor table (every quote added to genius.md this pass)

| Anchor (as it appears in genius.md) | Verbatim in transcript.txt? | Location in transcript.txt |
|---|---|---|
| "there's a big difference between a video and a story" | Yes | ~line 1, "...I've started to notice is that there's a big difference between a video and a story." |
| "tension can be both external and internal at the same time" | Yes | Japan example, "...you can notice here that tension can be both external and internal at the same time." |
| "we can still refine the line however we want" | Yes | Japan example close, "...we can still refine the line however we want, but it already gives a really clear direction..." |
| "It comes down to three simple steps." | Yes | Intro, "...It comes down to three simple steps. That's it." |
| "walks you through the same three questions step by step" | Yes | Tool description, "...it walks you through the same three questions step by step and then generates your sentence..." |
| "Something has to be different at the end than in the beginning." | Yes | Change-step explanation, "...Something has to be different at the end than in the beginning." |
| "you still just have a topic instead of a story" | Yes | Tension-step explanation, "...without tension, you still just have a topic instead of a story." |
| "write the whole thing down in one sentence" | Yes | Step 3 intro, "...the third step is to write the whole thing down in one sentence." |
| "not every story needs an obstacle or a struggle as tension" | Yes | Closing section, "...not every story needs an obstacle or a struggle as tension." |

All nine were located as exact substrings in `extractions/Tim Runia/transcript.txt`
before being written into genius.md — none is a paraphrase presented as a
quote. Casing was preserved from the transcript in each case (one quote,
"Something has to be different...", was re-framed with a lead-in colon
specifically to avoid altering the transcript's original capital "S").

## Checks this repair targeted (per audit-story-compass.txt)
- `anti_patterns_sourced` — 4/7 → now 7/7 sourced (added verbatim-quote
  anchors to anti-pattern items 3, 5, 6; items 1/2/4/7 already carried
  anchors and were untouched).
- `recognition_test` — added `## How to Use This Skill (Model Calibration)`
  to genius.md, containing the literal phrase "recognize this as" and
  "distinguish this from," written against Runia's own diagnostic practice
  (not templated from another expert's section).
- `source_ledger` — new `references/source-ledger.md`, claim-by-claim
  VERIFIED/LIKELY/UNCONFIRMED.
- `named_entity_floor` — 6 zero-entity sections found (Core Genius; Pattern
  4; Pattern 9; and three Hidden Knowledge subsections: "Tension Creates
  Story, Not Complexity," "The Tool Is the Methodology," "Change ≠ Happy
  Ending"). All six enriched with a verbatim quoted anchor from the
  transcript (quotes are the entity type used throughout — no fabricated
  numbers/dollar figures were invented). Ratio recalculated after edit:
  0/24 zero-entity sections (was 6/24 = 0.25).

## Checks NOT touched (already passing, left as-is)
- `verbatim_exemplars` — 22 (need ≥3), untouched.
- `workflow_contracts` — all 13 workflow files already carry Output Schema +
  Quality Gate, untouched.
