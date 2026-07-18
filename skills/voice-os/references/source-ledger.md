---
skill: voice-os
purpose: >-
  Claim-by-claim source ledger for genius.md and SKILL.md. Voice OS is a
  first-party skill — the "expert" is Farrice Cain himself, not an external
  extraction. Ground truth lives in _active/farrice-brand/voice/ and the real
  corpus it cites, not in extractions/ (there is no extractions/ directory for
  a first-party subject).
compiled: 2026-07-17
labels: VERIFIED = re-confirmed by direct file read/grep during this repair pass | LIKELY = internally cited by a compiled source with named sub-sources, not independently re-walked to the raw file this pass | UNCONFIRMED = pattern claim with no traceable written receipt found
---

# Voice OS — Source Ledger

## Compiled voice sources (primary)

| Source | Status | Note |
|---|---|---|
| `_active/farrice-brand/voice/VOICE-CARD.md` | VERIFIED | Read in full this pass. Its own frontmatter lists sub-sources (FARRICE-MASTER-CONTEXT.md, FOUNDER-CONTEXT-BRIEF.md, CLAUDE.md, content-voice-calibration.md, ai-slop-detector.md, and named corpus files) — those sub-sources were spot-checked (see below), not each re-walked line by line. |
| `_active/farrice-brand/voice/PLATFORM-NARRATIVE-CARD.md` | VERIFIED (card itself) / LIKELY (its cited engagement figures) | Card read in full. Its own §2 flags two rows with ⚑ live gut-check status ("verify before locking benchmarks") and its §4 explicitly labels the 27%/50% engagement figures "single-source directional... treat as compass, never quote as fact." Carried into genius.md with the same caveat. |
| `_active/farrice-brand/voice/calibration-log.md` | VERIFIED | Read in full. Append-only felt-verdict log; every row cites a source piece and date. Rows quoted in genius.md are the same rows present in this file at time of read. |
| `_active/farrice-brand/CLAUDE.md` (project-level, Farrice/Parallax) | VERIFIED | Read in full via system context this session; voice rules section cross-checked against VOICE-CARD.md §2/§5 for consistency (matches). |
| `directives/ai-slop-ban-bank.md` | VERIFIED | Grepped for Farrice-specific em-dash rule; line 133 confirmed verbatim: "em-dash count > 0 (Farrice tell; default ZERO, max 1)." |
| `skills/voice-os/references/prompts-v2/*.md` (4 files) | VERIFIED | Read in full. Pre-existing structure-pure-v2 prompts (felt-verdict-capture, post-draft-voice-verification-pass, pre-draft-voice-grounding-brief, voice-card-recompile); unmodified by this repair, cross-referenced for genius.md's Voice Law section. |

## Corpus quotes re-verified this pass (grep line-number confirmed)

| Quote | File | Line | Status |
|---|---|---|---|
| "The 'pick one thing' advice is a cage with better lighting." | `_active/farrice-brand/content/parallax-packages/01-manifesto.md` | 348 | VERIFIED |
| "You can't tell presence from performance from the outside." | `_active/farrice-brand/content/parallax-packages/02-coachella-reckoning.md` | 371 | VERIFIED |
| "For eighteen years I was the best trainer in every gym I worked at. You've never heard of me." | `deliverables/linkedin/2026-07-16-jenny-transfer-post-v2-i-narrative.md` | 11 | VERIFIED |
| "Every year of mastery buries the plain version deeper." | `deliverables/linkedin/2026-07-16-jenny-transfer-post-v2-i-narrative.md` | 23 | VERIFIED |
| "hear this the way I needed to hear it: nothing is wrong with you" | `deliverables/linkedin/2026-07-16-jenny-transfer-post-v2-i-narrative.md` | 29 | VERIFIED |
| "the undercut is the engine of the whole post; softening it would kill the contradiction gap" | `deliverables/linkedin/2026-07-16-jenny-transfer-post-v2-i-narrative.md` | 59 | VERIFIED |
| "if it survives being pasted elsewhere, it's generic" (paste test) | `deliverables/linkedin/2026-07-16-jenny-transfer-post-v2-i-narrative.md` | 78 | VERIFIED |
| Sentence-count/stdev stylometric table (Ed 01, Ed 02, Ed 04) | `_active/farrice-brand/voice/VOICE-CARD.md` | §3 | LIKELY — VOICE-CARD.md states these are "direct word/sentence counts, not estimation" against the three named corpus files; this pass re-read VOICE-CARD.md's presentation of the numbers but did not independently re-run a word count against the three corpus files to reproduce the arithmetic. |

## Claims carried from VOICE-CARD.md without independent re-verification this pass

| Claim | Status | Why |
|---|---|---|
| Identity spine facts (age 37, wife Jennifer, son JJ, dog Bella, 18 years / 1,000+ client transformations) | LIKELY | Sourced by VOICE-CARD.md to `FARRICE-MASTER-CONTEXT.md` §1-§6, which was not re-opened this pass; treated as first-party self-reported identity data, standard trust level for a first-party subject. |
| "52% conversion penalty" on question-hooks vs. statement-hooks | LIKELY | VOICE-CARD.md §4 cites `NOTES_TRAILER_PLAYBOOK.md` as source; not independently re-opened this pass. Same caveat as PLATFORM-NARRATIVE-CARD.md's own benchmark figures — directional, not to be presented as external fact. |
| Em-dash counts per edition (2 in Ed 01, 4 in Ed 02) | LIKELY | VOICE-CARD.md §3 states these as direct counts against the named edition files; not independently recounted this pass. |
| "15+ times in rejected Parallax drafts" ("It's not X. It's Y." tell) | UNCONFIRMED as an exact count | VOICE-CARD.md §5 states this as a system-observed frequency claim with no single citable draft-by-draft receipt found in this pass's source set. Carried into genius.md as a claim attributed to VOICE-CARD.md's own audit history, not independently reproduced. |

## Anti-pattern items — source-attribution check (genius.md § Anti-Patterns)

All 7 anti-pattern items in genius.md carry either a dated `calibration-log.md` row, a
VOICE-CARD.md §-numbered citation, a direct file+line quote, or a `directives/ai-slop-ban-
bank.md` line-number citation. None are asserted without a locatable anchor.

## What is explicitly NOT claimed

No claim in genius.md or SKILL.md asserts that extractions/ material exists for this skill —
Voice OS has no extraction directory because Farrice is a first-party subject, not a third-party
expert extraction. This ledger and `PROVENANCE.md` are the substitute grounding mechanism for a
first-party skill, per the dispatch instruction for this repair.
