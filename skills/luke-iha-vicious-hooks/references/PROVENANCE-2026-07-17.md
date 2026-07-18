# PROVENANCE — luke-iha-vicious-hooks repair (2026-07-17)

Every anchor cited in `genius.md` and `references/source-ledger.md` traces to one of these files. File+line references below are given as "line 1" where a source file is a single continuous paragraph (no internal line breaks) — confirmed via `wc -l` returning 0 for these files.

## Primary source consulted (grounds all new anti-pattern quotes)

**`extractions/luke-iha-hooks/transcript.txt`** (line 1, single-paragraph transcript, ~25,569 bytes)
This is the transcript of the exact video the `luke-iha-vicious-hooks` skill is built from — Luke Iha teaching the 8 Vicious Hook Principles. It was already the implicit source for SKILL.md and the pre-existing genius.md content (the 8 principles, the 3 Hall of Fame exemplars, the Germanic word-pair table). This repair re-read it in full and pulled 5 additional verbatim excerpts to source AP1-AP5:

| Anti-Pattern | Verbatim excerpt used | Confirmed present in transcript.txt |
|---|---|---|
| AP1 (Warm-Up Intro) | "most people... start their ad actually three to four sentences in... throat clearing and a bunch of warm-up before they get to the point" | Yes — searched and confirmed |
| AP2 (Polished Professional) | "A polite hook is a dead hook. A comfortable hook is a dead hook." / "They're not polite. They're not sanitized. Again, they're vicious." | Yes — confirmed (two separate passages, both cited) |
| AP3 (Mechanism Lecture) | "silver releases ions that neutralize bacteria in stored water..." / "this weird morning habit causes electrical imbalance in your body..." | Yes — confirmed (two examples, both already used elsewhere in genius.md's Principle 8 section prior to this repair; repair added them as sourced AP3 bullets too) |
| AP4 (Loose Loop) | "Don't do this one thing, you know, with AI, right?... the number one thing to avoid if you use this specific AI tool..." | Yes — confirmed |
| AP5 (Word Snobbery) | "a French word for sweat would be persspire..." + "fabrics versus cloth, excessive versus too much, insomnia versus sleeplessness, severe versus bad, synthetic versus man-made" | Yes — confirmed (note: transcript itself contains the typo "persspire" for "perspire" — preserved verbatim, not corrected, since it's a direct quote) |

## Secondary sources checked but NOT used as anti-pattern grounding

Checked during this repair specifically to see if they contained additional Luke Iha "don't do this" statements about hooks that could strengthen the sourcing:

- `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` (line 1, single-paragraph) — grepped for mistake/generic/boring/predictable/"too safe"/"too vague"/"don't work"/"doesn't work"/"weak hook"/fails — zero matches. Also grepped for "hook" — present but in affirmative/how-to framing (10 hook archetypes), not anti-pattern framing. Not used.
- `extractions/luke-iha/video-2-creative-strategy/transcript.txt` — grepped for "hook" — zero matches (this video is about creative strategy generally, not hook-writing specifically). Not used.
- `extractions/luke-iha/video-3-levels-of-awareness/extraction-report.md` — this is an AI-generated synthesis report derived FROM the video-3 transcript, not verbatim Luke Iha language. Read in full for context; not cited as a Luke quote anywhere (would be LIKELY-tier at best, and none of its phrasing was distinctive/quotable enough to warrant citing as source-grounding for an anti-pattern in this skill). Belongs conceptually to the sibling `luke-iha-unaware-ads` skill, not this one.
- `extractions/luke-iha/transcript.txt` (the "Ladder of Proof" video) — read; about proof mechanisms and client acquisition, not hooks. Not used.
- `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` and `video-4` through `video-8` extraction-report.md files — not reviewed in this pass (out of scope: proof mechanisms, copy blocks, VSL leads, offer cycling, million-dollar mechanisms, proof ladder — none are the hooks skill's domain).

## AP6 — explicitly could not be grounded

No source file located contains a direct Luke Iha statement matching the "generic stakes" framing ("This could hurt your business" / "You might be missing out"). This was flagged UNCONFIRMED in both `genius.md` (inline sourcing-status note under AP6) and `references/source-ledger.md` (per-claim ledger table) rather than paired with an invented quote. The underlying principle (Principle 4 — Stakes & Rubbernecking) IS grounded in the transcript; only the specific "generic stakes" anti-pattern framing is unconfirmed as Luke's own words.

## Workflow contract fix — no new claims

The `workflow_contracts` fix (renaming `## Output Contract` → `## Output Schema` in all 14 workflow files) involved zero new factual claims about Luke Iha — it is a heading-string change only, matching the house style found via `skills/attention-hijack-hooks/workflows/03-four-format-hook-generator.md` and `skills/alex-m-smith-natural-strategy/workflows/01-natural-strategist-audit.md` (both confirmed to use the literal heading `## Output Schema` followed by a fenced markdown template — the auditor's regex `output\s+(schema|format|requirements?)` requires this phrasing; `Output Contract` does not match it). No workflow body content was altered.

## What was NOT touched

- SKILL.md — unchanged (no failing check required a SKILL.md edit; `recognition_test` was satisfiable via genius.md alone and was placed there to sit next to the principles it tests).
- Luke Iha's biographical claims in SKILL.md (revenue figures, "Genesis" program, student results) — not re-verified in this pass; out of scope for this repair (heartbeat checks target sourcing/structure, not bio-fact verification).
- The pre-existing 3 Hall of Fame exemplars and Principle 1-8 definitions — untouched; they were already grounded in the same transcript prior to this repair and were not flagged as failing.
