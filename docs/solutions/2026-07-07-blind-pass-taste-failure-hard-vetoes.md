---
name: Blind-Pass Fails on Taste → Convert the Grader's Rejects into Hard Vetoes, Not Prose
problem_signature: an extraction blind-passes on STRUCTURE (the objection→format→mechanic chain is embodied) but a cold run still ships the expert's stated taste-rejects (an em dash she removes on camera, a "clean and safe" line where she pushes visceral, a buried product where she demands one focal point) — because the taste rules live in genius.md as PROSE and the producing agent reads them, flags them, and ships the violation anyway
domain: extraction
tags: [extraction, embodiment, blind-pass, quality-gate, hard-veto, taste, adversarial-review, dara-denney]
date: 2026-07-07
status: active
session: dara-denney-static-ads-masterclass-forge
---

## Problem

The Dara Denney static-ads expansion blind-passed on structure the first time — a cold agent ran `/dara-static-engine` on My.BPM and produced a genuinely Dara-shaped strategy (one goal, specific persona + objection, objection→format→mechanic chain). But the adversarial grader scored it **WEAK-PASS 6.5** and would-send-back, because the *ad itself* tripped three things Dara states on camera: it shipped an **em dash** (she removes one live: "I don't like this M dash"), the copy was **clean-and-safe greeting-card** where she explicitly pushes visceral, and it was a **full-bleed lifestyle crowd shot with the product buried** — her single most-repeated kill condition — while self-scoring the 1-second test an inflated 8. The producing agent had *read* the em-dash rule in genius.md, *flagged it in its own notes*, and shipped it anyway.

## Root Cause

Taste rules written as **prose guidance** in genius.md are advisory — an agent treats them as "considerations," notes the tension, and proceeds. Structure embodies from prose because structure is a *process* (do these steps); taste does not, because taste is a *veto* (never ship this). Prose can't express "never." The rubric compounded it: "1-second comprehension" was scored on whether the *vibe* was nameable, not whether the *product* was — so a mood-board shot could score 8.

## Approach That Worked

1. **Run the blind-pass as produce → adversarial-grade, and mine the grader's rejects.** The grader's three specific catches (em dash / clean-not-visceral / buried product + inflated score) became the fix list. The grader is the taste oracle; its findings are the spec.
2. **Convert each reject into a HARD VETO — a pass/fail auto-send-back — in genius.md, placed right after the rubric so every workflow's Quality Gate inherits it.** Not "prefer no em dashes" but "**Em dash anywhere in copy → send back.**" Six vetoes: em dash; product-not-nameable-at-a-glance (mood-board trap); headline generalizes away the persona's specific detail; headline vs CTA competing concepts; clean-and-safe where the audience rewards visceral; self-congratulatory scoring.
3. **Fix the rubric to measure the right thing.** 1-second comprehension now requires naming the **PRODUCT CATEGORY**, not the scene/vibe. Visual-hierarchy anchor now requires the **product to be a legible focal element** (not buried in a lifestyle shot). Sharpened the Headliner definition so a full-bleed crowd shot can't be mislabeled as one.
4. **Retry the blind-pass once, cold.** Fresh agent, same brief, hardened skill → **PASS 7.5**. All six vetoes cleared, fixes structural not cosmetic, grader verdict: *"the taste layer is now judgment, not vocabulary."* The one residual (headline at the *floor* of visceral, not the ceiling) is a directorial note the expert would give her *own* work — not an imitation tell.

## Why It Generalizes

Every voice/taste extraction has rejects the expert states explicitly (banned words, banned moves, "I'd kill this if…"). Those belong in a **Hard Vetoes block** inherited by the Quality Gate, phrased as pass/fail — never as prose preferences. If a blind-pass fails on taste rather than structure, don't rewrite the whole skill: extract the grader's specific rejects, install them as vetoes, retry once. Structure embodies from process; taste only embodies from a veto.

## Dead Ends

- **Trusting the taste prose in genius.md to be honored.** The agent read it and shipped the violation anyway. Prose ≠ enforcement.
- **Scoring 1-second comprehension on "is it recognizable."** A vibe is recognizable while the product is invisible — that's the exact failure. Score product-nameability.
- **Rebuilding the skill after a taste failure.** The structure was already embodied; a rebuild would have risked the good frameworks (see [[2026-07-07-multi-engine-rebuild-degrades-elevated-content]]). Surgical veto-install + one retry is the fix.

## Related

- [[2026-07-07-transcript-only-extraction-generic-output]] — watch the source for verbatim exemplars; this card is the taste-enforcement layer on top of that grounding.
- [[2026-07-07-parallel-builders-stale-contracts]] — the same session also caught a pre-existing fabricated parallel build (SKILL.md table ≠ files, invented headlines); fixed by auditing against frame-ground-truth and reconciling SKILL.md after a barrier.
