---
name: Manager loop turn-end rule — make "keep going until blocked" physical
problem_signature: "Agent plans or compiles a long job well, then ends every turn with a status update and hands the job back; open missions pile up (54 open, oldest 41d) because nothing makes 'continue until every lane is done or waiting on the human' a mechanism"
domain: harness / orchestration
tags: [manager-loop, recipe-cards, job-board, turn-end, decision-packets, nate-b-jones, codex-parity]
date: 2026-09-09
status: solved
session: manager-loop-harvest (lane worktree-manager-loop-harvest)
---

## Problem
Every planning layer existed (`/go` compile + preflight, `/mission` charter, six-line specs, wargame ledgers) and none of them drove. The conductor worked one turn, wrote a polished update, and stopped — the "hand-back" Nate B Jones describes (youtube ix8SsXjBc7M, 06:24). Evidence on disk: `pulse_dashboard.py --open` showed 54 open missions, the oldest 41 days. Farrice's felt version: "I don't think we have anything consistent enough with the behavior where I can hand off something ambiguous and light and you go out and cover all the gaps."

## Context it was cracked in
Harvesting Nate's manager-loop video into a native capability, with the build itself run as the first job through its own board (dogfood). Constraints: nothing may block (compass doctrine), Fable and Astra must each run a job alone or together, no new state store, no edits to `.codex/hooks.json`.

## The approach (repeatable recipe)
1. **State on disk, not in the transcript.** A job = `.agent/missions/<slug>/` with `card.md` (instantiated recipe), `mission.json` (the `mission_control.py` activation queue IS the lane list, plus an `after` dependency field per lane), `decisions.md` (packets + answers). `execution/job_board.py` is a façade over that store; every write takes a file lock.
2. **One deterministic line decides whether the turn may end.** `job_board.py next <slug>` prints `TURN MUST CONTINUE` while any lane is planned/active with its dependencies met, and `MAY END` only when every lane is complete, skipped, or blocked on a decision that is the human's. The manager's hard rule: end the turn only on MAY END.
3. **Questions become packets, not stops.** `job_board.py packet add` records Choice · Irreversible? · Options + recommendation · If no answer. Packets batch into the turn-end reply; mid-run `AskUserQuestion` only for a T3 action.
4. **Per-prompt card, both harnesses.** `steering_loop_hook.py` gains `MODE JOB-HANDOFF` (detector: ≥200 chars + delegation verb + breadth ≥2 of {deliverables, systems, sequence}); the Claude card says "end only on MAY END", the Codex card says "single seat, run lanes in order in THIS turn, a diagnosed lane is not a done lane". The card suppresses the INTENT BRIEF and fresh-pen cards (one brief, never two).
5. **Observe the miss, never block it.** The Stop hook logs `job-turn-ended-unblocked` when a job turn ended with runnable lanes and no DECISION PACKET.
6. **Portable across harnesses.** `job_board.py handoff <slug> --to codex|claude|chat` writes `portable.md` (card + lane table + packets + answers + resume command) and a handoff-store entry; `/job resume <slug>` on either side reloads from disk.
7. **Closeout answers the four questions with receipts** (done? aligned? unauthorized? approvals surfaced?) and ratchets the recipe in place (`runs`, `last_ratchet`, a dated line).
8. **Verify both directions** (`verify_job_handoff.py`): positives fire, near-misses don't, the Codex runner wraps the card in the hook envelope, the board's `next`/`lint`/`packet` sabotage cases pass, the Stop observer logs exactly once for a runnable temp job and never for a blocked one.

## Why it works
The behavior that kept failing was a judgment call ("should I keep going?") left to a model at the end of a long turn. Moving it into a one-line deterministic verdict from on-disk state removes the judgment from the moment where it always failed, without adding a gate: the model can still stop, and the observer records that it did. Packets convert every "should I ask?" into a form with a default, so asking stops being a reason to end the turn. Disk-as-truth is what lets a second harness pick the job up without re-explanation.

## Reuse trigger
- Any "the agent plans well but doesn't finish" complaint → check whether a MAY END-style verdict exists for that loop; if not, add one from state, not prose.
- Any new long-horizon runner (overnight, Codex exec, chat-pasted) → give it the portable packet, not a re-briefing.
- Gotchas for the next builder: the worktree Bash guard rejects heredocs and the literal word "complete" in a command string (patch via script files); recipe lane names cannot contain hyphens; `handoff_store.py` accepts only its own status vocabulary (`mid-build`); verifiers on a temp root must skip the handoff store (`JOB_BOARD_SKIP_HANDOFF_STORE=1`).
- Orchestration seating: Fable manages and writes; read-only lanes are background Sonnet seats carrying the negative brief; Astra is one seat that runs lanes in order.
