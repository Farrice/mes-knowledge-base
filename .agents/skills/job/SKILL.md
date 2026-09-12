---
name: "job"
description: "Manager-loop front door for ANY job-shaped ask — several deliverables, systems, or days; lanes that depend on each other; he wants to hand it off and get decisions back, not status. One manager interviews once, runs every unblocked lane, batches decisions into DECISION PACKETS, ends the turn only when `python3 execution/job_board.py next <slug>` prints MAY END, closes on four questions. Also: /job resume <slug>, /job status, /job handoff <slug> --to codex|claude|chat."
---

# job — the manager loop (both harnesses)

Use this skill for every job-shaped handoff, on Codex or Claude Code.

## Command Template

Read and execute the workflow at `.agent/workflows/job.md`. Load
`skills/nate-b-jones-manager-loop/genius.md` first.

Codex is a single seat. FIRST TOOL CALL of a new job = `python3 execution/job_board.py open …`
(after `recipe_cards.py match`; WEAK = forge the card first). Nothing else runs before the plan
is on screen — no worktree work, no Photoshop, no research. FIRST TURN: `open` prints a JOB PLAN — reply with that plan
(plus the interview questions) and END THE TURN; `next` prints PLAN PENDING until his go →
`job_board.py go <slug> --note "<his words>"`. A WEAK MATCH from `recipe_cards.py match` means
forge a card, never run the matched card's lanes. AFTER GO: run lanes in order of readiness in
THIS turn, close each with `lane … --status --did "what was done / found / skipped" --evidence`
and echo its LANE RECEIPT line; a lane that ends in a
diagnosis is not done — build it, or mark it `--status blocked --blocker "<decision needed>"`
with a DECISION PACKET. End the turn only when `job_board.py next` prints MAY END. Job state
lives on disk under `.agent/missions/<slug>/`; `/job resume <slug>` reloads it. Write only in a
Codex lane worktree (GOLDEN RULE). T2/T3 actions (publish, send, spend, delete, ship AS Farrice)
always wait behind a packet.

Never: a status update where a packet was owed; a second brief after the card; a fresh-pen
dispatch; running a task-shaped ask through the board; starting the work before the plan.
Taste work (design, copy, voice): the board still opens, but lanes run as visible beats.
