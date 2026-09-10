---
name: "job"
description: "Manager-loop front door for ANY job-shaped ask — several deliverables, systems, or days; lanes that depend on each other; he wants to hand it off and get decisions back, not status. One manager interviews once, runs every unblocked lane, batches decisions into DECISION PACKETS, ends the turn only when `python3 execution/job_board.py next <slug>` prints MAY END, closes on four questions. Also: /job resume <slug>, /job status, /job handoff <slug> --to codex|claude|chat."
---

# job — the manager loop (both harnesses)

Use this skill for every job-shaped handoff, on Codex or Claude Code.

## Command Template

Read and execute the workflow at `.agent/workflows/job.md`. Load
`skills/nate-b-jones-manager-loop/genius.md` first.

Codex is a single seat: run lanes in order of readiness in THIS turn; a lane that ends in a
diagnosis is not done — build it, or mark it `--status blocked --blocker "<decision needed>"`
with a DECISION PACKET. End the turn only when `job_board.py next` prints MAY END. Job state
lives on disk under `.agent/missions/<slug>/`; `/job resume <slug>` reloads it. Write only in a
Codex lane worktree (GOLDEN RULE). T2/T3 actions (publish, send, spend, delete, ship AS Farrice)
always wait behind a packet.

Never: a status update where a packet was owed; a second brief after the card; a fresh-pen
dispatch; running a task-shaped ask through the board.
