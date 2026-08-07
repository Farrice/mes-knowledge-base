# Source Ledger — nicolas-cole-nonfiction-value-architecture

Claim-by-claim confidence labels. Ground truth checked against the real, byte-verified
source transcript (not the path `references/source-map.md` originally pointed to — see
Gap Note below).

**Primary source found**: `_active/harness/codex-harvest-2026-06-11/extractions/nicolas-cole-nonfiction-value/transcript-consolidated.md`
(460 lines) and the identical `transcript.txt` (447 lines) in the same directory.
- Expert: Nicolas Cole
- Video: "The Framework I Use To Make Any Nonfiction Piece More Valuable" (YouTube, xv5E5ZSzlHM)
- Upload date: 2026-05-05, duration 18:25
- Caption source: YouTube English original automatic captions via yt-dlp

## Gap Note (read before re-sourcing)

`references/source-map.md` (pre-existing file, left in place) cites
`extractions/nicolas-cole-nonfiction-value/transcript-consolidated.md` — that exact path
does **not** exist under top-level `extractions/`. The file exists only under the
`_active/harness/codex-harvest-2026-06-11/` archive (confirmed via direct read, 460 lines, real
content, not a stub). This is a stale-path problem, not a fabrication problem: every
quote in source-map.md's claim table was checked against the archived transcript and is
genuinely verbatim (see VERIFIED rows below). Per the envelope's rule 2 (a claim that
sources are absent is itself a provenance claim), this ledger records the actual
verification rather than assuming absence from the broken path.

The generic `extractions/nicolas-cole/transcript.txt` (18,152 bytes, about offer
stacking) and the other three `nicolas-cole-*` extraction folders were also checked and
do **not** contain this skill's value-architecture material — confirmed by grep for
"reverse engineer," "spotlight," "unbundle," "skim," "subhead," "bundled." They are a
different Cole talk and are not the source for this skill.

## Claims — Core Thesis / Ten Value Modes / Genius Patterns

| Claim | Label | Source |
|---|---|---|
| "the value of any piece of writing can really just be reverse engineered into a simple list of things" | VERIFIED | transcript-consolidated.md line 14 |
| "10 magical ways to expand anything" (naming for the ten value modes) | VERIFIED | line 16 |
| Ten value modes: tips, stats, steps, lessons, benefits, reasons, mistakes, examples, questions, story | VERIFIED | lines 18-48 |
| "which of these am I giving the reader?" | VERIFIED | line 62 |
| "before you start debating sentence structure, before you start picking different adjectives" | VERIFIED | line 66 |
| "80% of the value and 80% of the decision before you even start writing is here" | VERIFIED | line 450 |
| "one of them has to be in the spotlight" | VERIFIED | line 328 (concept restated line 88) |
| "the first decision is which one is in the spotlight?" | VERIFIED | line 330 |
| "what's my list of that thing?" | VERIFIED | line 332 |
| "I do not need to go spend 4 hours writing 3,000 words in order to decide what am I giving the reader" | VERIFIED | line 384 |
| "I have mentored and trained north of probably 15,000 writers at this point" | VERIFIED | line 212 |
| "99% of the time when I look at and evaluate someone else's writing, this is what I see" | VERIFIED | line 214 |
| "the first tip is you got to love your kids. And the second tip is you got to push them. And the third tip is you got to hold them accountable." | VERIFIED | lines 160-164 |
| "these are bundled terms" | VERIFIED | line 196 |
| "I didn't tell you anything you didn't already know" | VERIFIED | lines 192/196/224 |
| "I need to tell the reader something they don't already know and or I need to unbundle the language" | VERIFIED | line 224 |
| Bundled-word list extended to "discipline, mindset, consistency, trust, authenticity, authority" (SKILL.md/genius.md, pre-existing) | LIKELY | Not spoken verbatim by Cole in this transcript — an inherited extrapolation from the verified "love / push / accountability" pattern to adjacent self-help vocabulary. Reasonable but not sourced. |
| "no phones at the dinner table" (moment-translation example) | VERIFIED | lines 268-276 (audience-prompted, Cole builds the tip live) |
| "How many nights a week did you allow phones at the dinner table? That is measurable." | VERIFIED | lines 292-294 |
| "I can imagine it. I can feel it. I can measure it." | VERIFIED | lines 286-290 |
| "they do not read it. They skim it." | VERIFIED | lines 392-394 |
| "this happens within 4 seconds" | VERIFIED | line 422 |
| "The subheads tell me how good the writer is at delivering on the thing that they're promising" | VERIFIED | line 434 |
| "They might be saying the same things but they're saying them in different levels of specificity" | VERIFIED | line 304 |
| "Could I also include steps if I wanted to?" | VERIFIED | line 318 |
| "meandering, you know, long opinions with no like where are we going" | VERIFIED | line 78 |
| Signature Moves list (operational restatement) | LIKELY | Synthesized from the verified concepts above; not a direct quote, but a faithful operational translation. |
| Quality Gate 10-point checklist | LIKELY | Synthesized checklist derived from verified concepts; not spoken by Cole as a numbered list. |
| Skill-stacking references to "tangible faucet" (SKILL.md, workflow 02) | UNCONFIRMED | Not present anywhere in this skill's source transcript. Per session memory (2026-07-18 re-acquisition queue), the "Cole Two-Rules/Tangible-Faucet source" is a known-missing source elsewhere in the system — this skill uses the term only as a cross-skill-stacking pointer to `nicolas-cole-newsletter-flywheel`, not as a claim attributed to this transcript. Left as-is; flagging so no one hunts for it here. |

## Scope note

Workflow files (`workflows/01-*.md` through `08-*.md`) were not re-verified claim-by-claim
this pass — the heartbeat audit already scored `workflow_contracts` as PASS (all 8 carry
Output Schema + Quality Gate) and they were out of scope for this repair (only
`anti_patterns_sourced`, `recognition_test`, `named_entity_floor` were failing). If a
future pass touches workflow content claims, extend this ledger.
