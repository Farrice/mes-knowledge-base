# fresh-voice-system — Source Ledger

> Claim-by-claim provenance for every source consulted in this repair pass (Wave 3,
> Lane 3, 2026-07-17). Labels: **VERIFIED** (read directly, quote/fact confirmed
> verbatim in the cited file) · **LIKELY** (internally consistent synthesis, not
> independently confirmed against a primary transcript) · **UNCONFIRMED** (claim
> exists in the skill but could not be traced to a source in this pass).

## Primary Source

| Claim / Content | Label | Source | Note |
|---|---|---|---|
| 20-post serial narrative arc (Posts 1–20), the 5 Core Principles, the Five Story Beats, Open Loop Mechanics, the Meta-Prompt | VERIFIED | `_active/linkedin/04-deliverables/content-os/voice-captures/genspark-20-post-serial-arc.md` | Read in full. Added to the repo 2026-03-10, commit `4da54d14e` ("feat: add LinkedIn transition posts + GenSpark voice extraction"). This is the ground-truth extraction genius.md's "The Discovery" section is built on. |
| All 6 quotes in the new "Anti-Patterns (Sourced)" section (Posts 3, 4, 7, 12) | VERIFIED | same file, lines 59–286 (Post 3 ~L47-77, Post 4 ~L79-103, Post 7 ~L151-178, Post 12 ~L285-318) | Byte-checked against the raw file with a Python read (not the rendered view) to confirm exact wording. The source file carries a formatting artifact: an opening `\"` and often no closing `\"`, apparently unescaped-JSON residue from the original extraction. Quotes in this skill are normalized to drop the stray backslashes; the English content itself is unmodified. |
| "I figured out the secret and now I'll share it with you" (genius.md, Principle 4 anti-pattern callout, pre-existing) | UNCONFIRMED | — | Pre-existing paraphrase in genius.md, not found verbatim in the primary source during this pass. Left untouched (out of repair scope — this line was not part of a failing check) but flagged here so it isn't mistaken for a checked quote. |

## This Skill's Own Reference Files

| Claim / Content | Label | Source | Note |
|---|---|---|---|
| Hall of Fame Exemplars (Exemplar 1 "Chapter 3 - The Invisible Wall", Exemplar 2 "The Coach Who Refused to Write") and the Anti-Exemplar ("5 Ways to Optimize Your LinkedIn Content") | LIKELY | `skills/fresh-voice-system/references/exemplars.md` | Added 2026-04-02, commit `e7ae19898` ("Phase 2: Extract quality rubrics from 27 oversized genius.md files"). Read in full (65 lines). These are illustrative model-generated exemplars built to demonstrate the methodology's structure — not confirmed as Farrice's actually-published LinkedIn posts, so labeled LIKELY rather than VERIFIED. Quotes pulled from this file into genius.md (the "Numbered-tips-plus-CTA" anti-pattern, the David/Sarah paradox-reveal quote) are themselves verbatim against this file. |
| Quality Rubric (Score 4/7/10 anchors, 4 criteria) | VERIFIED (existence) / not content-audited | `skills/fresh-voice-system/references/quality-rubric.md` | File exists and was read; the markdown table's cell content is corrupted in one spot (an anomalously long run of repeated dash characters inside a table cell, likely a prior extraction artifact). Out of scope for this repair pass (not tied to any of the five failing checks) — flagged here, not fixed, per the additive-only / minimal-touch boundary. |

## Cognitive Signature Layer (2026-04-09 addition)

| Claim / Content | Label | Source | Note |
|---|---|---|---|
| The Three Cognitive Moves (Paradox Reveal / False Frame Demolition / Reframe Landing) | LIKELY | genius.md itself, marked "Added 2026-04-09, Evolution cycle: fresh-voice-system #1" | Self-declared synthesis from the skill's own evolution log, not re-derived from the primary genspark source in this pass. The worked example quoted ("Her depth was the problem...") is internal to genius.md, not traced to an external transcript — labeled LIKELY (structurally sound, not independently source-verified). |

## Adjacent Pointers (Expert Stack / Key References in SKILL.md)

| Claim / Content | Label | Source | Note |
|---|---|---|---|
| "Robert Mack — Comedy mechanics, parenthetical asides, deflation" (SKILL.md Expert Stack) | VERIFIED (pointer exists) | `agents/robert-mack/AGENT.md`, `skills/robert-mack-comedy-writing/` | Confirmed both directories exist and are populated (AGENT.md + memory + skills; SKILL.md + genius.md + references + workflows). Depth of the comedy-mechanics attribution itself was not re-audited in this pass — that skill was not in scope. |
| `.agent/workflows/voice-first-content.md` (Key References) | VERIFIED (pointer exists) | same path | File exists. |
| `_active/linkedin/04-deliverables/content-os/arcs/` (Key References, "Active Arcs") | VERIFIED (pointer exists) | same path | Directory exists, contains `00-transition`. |

## What Was NOT Re-Verified

Voice DNA, Sentence-Level Architecture, and Comedy Mechanics in SKILL.md (tone spectrum,
punctuation rules, signature vocabulary) are house-style synthesis consistent with the
genspark source's register but not line-by-line traceable to a single external quote —
labeled LIKELY as a class. None of this was touched in the repair pass; flagged for
completeness of the ledger, not as a new finding.
