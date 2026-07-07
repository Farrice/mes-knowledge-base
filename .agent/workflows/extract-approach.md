---
description: Capture a Solution Card for any solved non-trivial problem before it evaporates
---

# 🧠 /extract-approach — Solution Recorder

> **Purpose**: After any non-trivial solved problem — system fix, content recipe that
> finally worked, client-format crack, strategy unlock, ANY domain — capture the
> approach before it evaporates. This is not a system-debugging-only tool.

**Principle** (Farrice, 2026-07-07, binding): *"A solved non-trivial problem without a
Solution Card is unfinished work."*

## Operator Core Alignment

This is the canonical capture point for reusable approaches, distinct from:
- `/end-session` — whole-session closeout (handoff, index, commit offer).
- `/handoff` — the portable cross-tool transfer document.
- Session-state protocol — mid-session context survival.

`/extract-approach` produces one durable, searchable artifact per solved problem: a
Solution Card under `docs/solutions/`. It composes into the others (closeout can nudge
it; a handoff can point at it) but never absorbs their jobs.

## Flow

### 1. Draft the evidence bundle
// turbo
```bash
python3 execution/solution_recorder.py draft --slug <slug> --problem "<one-line signature>"
```
Produces an evidence bundle (recent diffs, receipts, ledger state) and a prefilled
card template at `docs/solutions/<date>-<slug>.md`. The `--problem` string becomes the
draft's `problem_signature` — write it as the symptom shape that would recur, not a
narrative ("SessionEnd hook double-fires because marker-detection can't see
hook-internal subprocess calls," not "we fixed the hook").

### 2. Fill the card from ACTUAL session evidence
Ground every section in the real conversation, diffs, and receipts — never
reconstruct from memory of what "probably" happened. Required H2s (exact, matching
the shared contract): `## Problem`, `## Root Cause`, `## Approach That Worked`
(numbered steps), `## Dead Ends`, `## Verification`, `## Weaker-Model Trap`,
`## Pointers`.

- **Dead Ends is mandatory.** Name what was actually tried first and failed — the
  specific wrong turn, not a vague gesture at difficulty. If truly nothing failed
  before the working approach, write one sentence explaining why the problem still
  qualifies as non-trivial (e.g. it required tracing an invisible code path, or
  reconciling two files that looked contradictory).
- **Weaker-Model Trap is a calibration block, not a warning label.** Name the specific
  shortcut, overpolish, or skip a mid-tier model would take on this exact problem —
  what it would ignore, over-trust, or stop checking too early.
- Keep the whole card dense: target ≤60 lines. Density over completeness — write for
  a future reader under time pressure, not a completionist audience.

### 3. Save
// turbo
```bash
python3 execution/solution_recorder.py save --file docs/solutions/<date>-<slug>.md
```
Validates the H2 contract (all seven sections present, Dead Ends non-empty,
`## Approach That Worked` has ≥2 numbered steps), rebuilds `docs/solutions/index.md`,
and writes a marker that clears this session's learning debt in the ledger. If
validation fails, fix the flagged section and re-run — do not hand-edit the index.

### 4. Surface it
One line in chat: the card path and its `problem_signature` verbatim. Nothing more —
the card itself is the artifact, not the chat message about it.

## When It Fires
- Learning-debt nudge from the Stop hook (a session produced a real fix/unlock with
  no card).
- Finalize latch refusal on a qualifying session.
- Closeout spine report (`/end-session`) flags open learning debt.
- Manually, anytime a problem just got solved and it's worth remembering.

## Anti-Patterns
- **Retroactive vagueness** — "we fixed the hook," "improved the approach." Name the
  actual failure shape so the card is searchable by symptom later.
- **Skipping Dead Ends** — a card with only the winning path teaches nothing about
  what looks right but isn't.
- **Essay-length cards** — if it's pushing past 60 lines, cut prose, not evidence;
  move detail into Pointers as a file reference instead of inline explanation.

## Recall Note
Cards resurface automatically — router-hook injection, the memory facade, `/resume`
and session-kickoff, the COS weekly board. Write each card for your future self
reading 20 lines under time pressure, not for a first-time reader who needs the full
story.
