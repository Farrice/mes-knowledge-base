---
date: 2026-07-28
session: About rebuild
name: co-creation-enforcement-layer
problem_class: harness / steering / unmeasured doctrine
domain: harness
status: proven
problem_signature: "the same co-creation failure repeats with the doctrine fully documented and live — round after round of variants optimized against the last complaint instead of verifying the feedback — because nothing counts renditions, rejections, or whether a question was asked before producing"
tags: [co-creation, steering-hook, spiral-brake, feedback, counters, doctrine]
---
# Solution Card — Co-Creation Enforcement Layer: a doctrine without a counter is a vibe

**Date:** 2026-07-28 · **Domain:** harness / steering · **Session:** About rebuild (ee1d3250)

## The problem

Two documented sessions failed the same way with the doctrine fully present:
- **2026-07-27 headline session**: eight rounds of variants, each optimized against
  the last complaint, 26,000 words of source research unread.
- **2026-07-28 About session**: five renditions (v10→v14) produced from educated
  guesses about feedback instead of verified alignment; Farrice: *"I've been
  directing everything this entire time, and the feedback you've just been taking
  educated guesses on versus verifying, aligning, and actually taking action and
  co-creating together."*

In both, CLAUDE.md Step 0 (PARTNER dial), the iteration brake ("two rejected
takes = stop"), and the steering hook's per-exchange reminder were all live. They
didn't fire because **nothing measured anything**: no rendition count, no
rejection count, no observation of whether a question was asked before producing.

## The root rule (transferable)

**A doctrine without a counter is a vibe.** A behavioral rule only becomes real
when (a) its trigger condition is measured as state, (b) the state is injected
into the turn where the behavior happens, and (c) misses are observed and
escalate. Prose reminders — even deterministic per-exchange ones — describe the
loop; they don't close it. (Same family as 2026-07-27 expert-load truth: the
instruction that cannot be checked will be faked or drift.)

## The fix (live in `execution/hooks/steering_loop_hook.py`, zero new wiring)

Three mechanisms riding the existing UserPromptSubmit/Stop channel, state in
`.agent/co-creation-state.json`, renditions derived from the session ledger's
`produced_paths`:

1. **SPIRAL BRAKE** — 2 rejected takes on one artifact stem OR 3+ renditions →
   injected order: no more variants; fresh crack from source / AskUserQuestion
   gut-check / present takes for a pick. Escalates + logs `spiral` at 5
   renditions.
2. **FEEDBACK-TURN PROTOCOL** — critique-shaped prompt → restate verdicts as a
   numbered list, ONE AskUserQuestion on ambiguity BEFORE producing, log to
   voice_ratchet, produce ONE take. Stop-hook observer logs
   `feedback-turn-blind-produce` when a Write/Edit happens without asking.
3. **WORK-MODE FRONT DOOR** — every substantive raw prompt classified
   BUILD-NEW / REFINE-EXISTING / IDEATE / DECIDE / CAPTURE and given the matching
   operating card (Chain-at-/go-standard, Pen Protocol, decision-before-artifact,
   thought-bank capture). First line names the mode; "mode X" overrides.

Compass-compliant: instructs the model, never blocks Farrice. Kill switches:
`CO_CREATION_OFF=1` / `.agent/co-creation.off`.

## Verification receipts

CLI bench 2026-07-28: spiral brake fired on this session's own ledger (4 `about`
renditions); rejection counter incremented across consecutive critiques;
BUILD/DECIDE/IDEATE/override/conversational-fallback all classified correctly;
corrupted ledger + state → silent exit 0; stop observer logged blind-produce on
the miss case and stayed silent when AskUserQuestion preceded the Write.

## Applies to

Any standing behavioral rule that keeps being violated despite being documented:
find the counter it lacks, store the counter, inject the counter, observe the
miss. Candidates already visible: send-before-build (teardowns built, never
sent), memoir-front-facing ratio, offer-deliverable specificity.
