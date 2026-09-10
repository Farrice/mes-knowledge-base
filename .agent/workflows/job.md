---
description: The manager-loop front door — hand off a job-shaped ask; one manager interviews once, runs every unblocked lane, batches decisions into packets, ends the turn only when the board says MAY END, and closes on Nate's four questions. Both harnesses, alone or together.
---

# /job — Hand Off a Job, Not a Task

`/job "<raw ask>"` is for work bigger than a prompt: several deliverables, several systems,
lanes that depend on each other, a plan that will change mid-run. Source: Nate B Jones's
manager loop + recipe cards (skill `nate-b-jones-manager-loop`, 2026-09-09). Scar it closes:
54 missions compiled by `/go` and never driven; the conductor handed the job back every turn.

**Farrice's dial (2026-09-09): hands-off for jobs.** Interview once, run to blocked, decision
packets — not visible beats. Visible beats stay the default for taste work (copy, voice, jams).

## Invocation

```
/job "<raw ask>"                 triage → interview → open → run (this turn continues until MAY END)
/job resume <slug>               reload a job from disk (either harness) and continue
/job status                      every open job, lanes, packets waiting on him
/job next <slug>                 TURN MUST CONTINUE | MAY END
/job packet <slug> answer <n> "<his words>"
/job handoff <slug> --to codex|claude|chat
/job close <slug>                four-question closeout + recipe ratchet + verdict ask
/job recipes                     the library (recipes/<slug>.md)
```

Every subcommand is a thin call into `python3 execution/job_board.py …` /
`python3 execution/recipe_cards.py …` — deterministic, identical under Claude Code and Codex.

## Steps (a new ask)

1. **Triage** — `skills/nate-b-jones-manager-loop/workflows/job-triage.md`. Run
   `python3 execution/recipe_cards.py match "<ask>"` and `python3 execution/job_board.py status --all`
   first; an open job or mission that matches is continued, never recompiled.
   TASK → route direct (`/go` or the named workflow), no board. DECISION → one packet, no lanes.
2. **Recipe** — `recipe_cards.py match` prints CONFIDENT MATCH or WEAK MATCH. **A weak match
   is a forge signal, never a plan**: forge a card from the workflows that already run the job
   (`recipe-card-forge.md`), save it to `recipes/`, and the plan beat shows it. Never run a
   matched card's lanes on an ask they were not written for.
3. **Interview once** — `manager-interview.md`: disk-first, ≤5 questions, only what changes
   execution. Then `python3 execution/job_board.py open <slug> --recipe <recipe> --goal "<his
   outcome sentence>"` and paste the filled card over `.agent/missions/<slug>/card.md`.
   **`open` prints a JOB PLAN and writes `plan.md`. The opening turn's reply IS that plan**
   (goal · recipe + match verdict · every lane as "what I'll do" · the questions · approvals) and
   the turn ends there — `next` prints PLAN PENDING until his nod. His "go" (or any edit) →
   `python3 execution/job_board.py go <slug> --note "<his words>"`, then the loop. `open --go`
   only when he said "just do it" in the ask. This card IS the brief — never a second INTENT
   BRIEF, never a fresh-pen dispatch. (Scar 2026-09-10: Coach Cooz ran the Poppy card's lanes
   with no plan shown and no interview — "it just does things".)
4. **Run** — `manager-loop-run.md`, every cycle: `job_board.py next` → dispatch all runnable
   lanes (writes = you, serial; read-only lanes = background Sonnet seats on Claude Code; Codex =
   in order, this turn) → close every lane with `job_board.py lane <slug> <id> --status … --did
   "what was done / found / skipped" --evidence <path>` and **echo its LANE RECEIPT line in the
   reply** → `job_board.py log <slug> <lane> "…" --kind found|skipped` for anything he should be
   able to read later → breakage per the card's row → approvals become packets →
   `job_board.py checkpoint <slug>` at turn end.
   **End the turn only when `job_board.py next <slug>` prints MAY END.** The reply is receipts +
   packets + one progress line; the trace (`job_board.py trace <slug>`) is how he sees what was
   covered and what was not.
5. **Answers** — when he answers a packet in chat, `job_board.py packet <slug> answer <n>
   "<his words>"`, unblock the lane, continue.
6. **Closeout** — `job-closeout.md` → `job_board.py close …`; last line verbatim
   `Verdict on this one — good / marginal / off?`; `/extract-approach` if something non-trivial
   was cracked.

## Harness rules

- **Disk is the only truth.** `.agent/missions/<slug>/{card.md, plan.md, trace.md, mission.json,
  decisions.md, portable.md}`. `/job resume <slug>` on either harness reloads from disk, never from a transcript.
- **Alone or together.** Fable usage out mid-job → `job_board.py handoff <slug> --to codex`, open
  Codex, `/job resume <slug>`. Reverse identical. `--to chat` = a paste-anywhere packet for ChatGPT
  / claude.ai; results come back as `LANE <id> RESULT` blocks he files with `job_board.py lane`.
  One writer per tree stands: Codex writes in its own lane worktree; lane ownership is recorded.
- **Tiers.** T1 lanes run; T2/T3 actions (publish, send, spend, delete outside repo, ship AS him)
  always wait behind a packet. Standing grants elevate T2→T1 for their scope only.
- **Nothing blocks** (compass doctrine). The Stop hook logs a job turn that ended with runnable
  lanes and no packet (`job-turn-ended-unblocked`) — it never holds the turn.
- **Seating.** Fable manages and writes. Subagents are read-only lanes on Sonnet/Haiku carrying
  "no Chain, no finalize, no Notion, no Next Moves, return only the artifact". Astra is one seat.

## Receipts

`.agent/missions.jsonl` gets one `compiled` line at open and one `done` line at close (pattern
`manager-loop`), so the pulse board and the finisher rule see every job. The SessionStart brief
prints `JOBS: …` while any job is open. Verifier: `python3 execution/verify_job_handoff.py`.
