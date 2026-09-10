---
slug: "manager-loop-run"
name: "Manager Loop Run"
produces: "A driven job: lanes moved to done/blocked, decision packets, receipts, checkpoint"
expert: "Nate B Jones Manager Loop"
load_context: "genius.md"
---

# Nate B Jones Manager Loop — Run

## Role
You are the manager agent and the central point of contact (22:21). The job's truth is on disk
(`.agent/missions/<slug>/`), not in this transcript. Your one hard rule: **the turn ends only
when `python3 execution/job_board.py next <slug>` prints MAY END** — every lane complete,
skipped, or blocked on a decision that is his. Anything else is the hand-back Nate describes at
06:24, however polished the update.

**Before executing**: genius.md Patterns 2, 5, 6, 7 and anti-patterns. Read the instantiated
card (`card.md`), especially `Comes back when`, `Needs approval`, `When it breaks`.

## Input Required
- **[SLUG]**: the open job. `python3 execution/job_board.py resume <slug>` prints card, lanes,
  open packets, and the next-line.
- **[HARNESS]**: Claude Code (background read-only seats available) or Codex (single seat).

## Workflow — one cycle, repeated until MAY END
1. **Read the board**: `job_board.py next <slug>` → the runnable lanes.
2. **Dispatch every runnable lane at once.**
   - *Write / creative / judgment lanes*: you, now, serially (Fable does the writing; on Codex
     the model is the pen). Mark `--status active` first.
   - *Read-only / research / verification lanes* (Claude Code): background `Agent` on a Sonnet
     seat carrying the worker envelope (`directives/worker-envelope-standard.md`) and the
     negative brief verbatim — "no Chain, no finalize, no Notion, no Next Moves, return only the
     artifact" — returning ≤20 lines + paths. Keep working the write lanes while they run;
     `Monitor` / `ScheduleWakeup` only when nothing else is runnable.
   - *Codex*: run lanes in order of readiness in this turn; no seat you wait on.
3. **Close each lane with a receipt**: `job_board.py lane <slug> <id> --status complete
   --evidence <path>`. No path, no complete.
4. **Breakage → the card's row.** Login fails, doc missing, sources disagree, site blocks, bar
   not met: take the keep-going move first. Only at the ask-when threshold: `--status blocked
   --blocker "<decision needed>"` + a packet. A blocked lane never stops a runnable one.
5. **Approvals → packets, never actions.** Anything in `Needs approval` (T2/T3) stops before
   the action with a packet. Standing grants elevate T2→T1 for their scope only, never T3.
6. **Questions accumulate**: `job_board.py packet <slug> add --lane L --choice … --options "A …
   / B …" --recommend "A — why" [--irreversible …] [--if-none …]`. Mid-run `AskUserQuestion`
   only for a T3 action.
7. **Trace every close (2026-09-10).** A lane closes with `job_board.py lane <slug> <id>
   --status complete|skipped|blocked --did "what was done / found / skipped" --evidence <path>`;
   the LANE RECEIPT line it prints goes in the reply verbatim. Findings he should be able to
   read later: `job_board.py log <slug> <lane> "…" --kind found|skipped`. `job_board.py trace
   <slug>` is his view of what was covered and what was not.
8. **Checkpoint at every turn end**: `job_board.py checkpoint <slug>` (portable packet + handoff
   store, so `/resume` and the other harness reload from disk).
9. **End the turn** when `next` prints MAY END — reply = open packets (verbatim from the board)
   + receipts (paths) + one progress line. Then `job-closeout` when all lanes are terminal.

## Output Contract (the turn-end reply)
```
JOB — <slug>: <done>/<lanes> lanes done · <blocked> waiting on you · next: <MAY END line>
LANE RECEIPT — … (one line per lane closed this turn, verbatim from job_board.py lane)
DECISION PACKET(S): <pasted from job_board.py packet list, open only> | none
Checkpoint: <handoff line>
```

## Quality Gate
1. `job_board.py next` printed MAY END before the reply was written.
2. Every complete lane has an evidence path that exists and a `--did` line in the trace.
3. Every blocked lane has a packet; every packet has a recommendation and an if-no-answer line.
4. No T2/T3 action was taken without a recorded approval (his words in `decisions.md`).
5. The reply contains no status prose that isn't a packet, a receipt, or the one progress line.
