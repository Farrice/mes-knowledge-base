---
description: Park an open mission deliberately — stopped line + resumable handoff in one move; parking is a good outcome, not a failure
---

# /park — first-class deliberate close (apex W1, 2026-07-29)

`/park <slug-or-title-fragment> "<one-line reason>"`

WHY: the mission log recorded 115 starts and 53 finishes; the only park path
was a punishment tucked inside /go's "new" branch — used once in 178 lines.
Meanwhile every primitive already existed (handoff_store blocked/mid-build
states, unfinished/branch fields, resume-with-branch-drift). This workflow is
the missing verb, zero new Python.

## Steps (all deterministic — run them, don't paraphrase them)

1. **Identify** the mission: `python3 execution/pulse_dashboard.py --open` —
   match the slug/title fragment. Ambiguous → ask, one line.
2. **Log the close**: append to `.agent/missions.jsonl`:
   ```json
   {"ts":"<iso>","mission":"<title>","slug":"<slug>","serves":"<goal>","status":"stopped","outcome":"PARKED: <reason>. Resume: /resume <thread>"}
   ```
3. **Write the resumable handoff**:
   ```bash
   python3 execution/handoff_store.py save --thread <slug> --status blocked \
       --hint "<reason> — pick up at: <next concrete step>" \
       --unfinished "<what's left, one line>" \
       --branch $(git rev-parse --abbrev-ref HEAD)
   ```
4. **T2/T3 missions also** drop their card copy into `.agent/mission-queue/parked/`
   (the AFK runner reads that directory — a parked big mission can resume headless).
5. **Confirm in ONE line**: `Parked <slug> — resume anytime: /resume <slug>`.
   No Next Moves block; parking IS the move.

## Rules
- Parking never needs justification beyond the one-line reason. Two open
  missions parked beats five open missions rotting (the 07-29 audit found 17
  missions open 10-16 days — none parked, all just abandoned-in-place).
- A parked mission that stays parked 21+ days surfaces in handoff staleness —
  that's the system working, not nagging.
