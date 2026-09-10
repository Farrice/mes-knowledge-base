<!-- instance of recipes/mission-backlog-triage.md · opened 2026-09-10T05:20:34-07:00 by claude on claude · goal: Drain the 54 open missions: finish, park, or kill each; packets only for the calls that are Farrice's; zero open missions older than 14 days without a park handoff -->
---
job: mission-backlog-triage
name: Mission backlog triage
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Drain the open-mission backlog to a board he can trust: every open mission finished, parked with a resumable handoff, or killed, with decision packets only for the calls that are his.

## Sub-jobs / lanes
- L1 Board read — `python3 execution/pulse_dashboard.py --open`; `handoff_store.py list --rich --all`; `job_board.py status --all` [parallel]
- L2 Evidence per mission — for each open line: what shipped (deliverable paths, git log, catalog `work_catalog.py`), last handoff, days idle [after: L1]
- L3 Classify — DONE-UNCLOSED (write the done line) / DUPLICATE (close to the survivor) / STALE-DEAD (kill) / LIVE (park with hint) / HIS-CALL (packet) [after: L2]
- L4 Close the mechanical ones — done lines appended to `.agent/missions.jsonl`; duplicates closed with `outcome: superseded by <slug>` [after: L3]
- L5 Park the live ones — `python3 execution/pulse_actions.py park <slug> --reason "…"`; rich parks also `handoff_store.py save --thread <slug> --status blocked --hint … --unfinished …` [after: L3]
- L6 Packets for his calls — one per HIS-CALL mission: finish / park / kill with the evidence line [after: L3]
- L7 Regenerate + receipt — pulse board regen, `session_brief` missions line, one closing table (before/after counts) [after: L4, L5, L6]

## Ask me first
- Q: Any mission you already know is dead or sacred? · look first: `MEMORY.md` active projects, `.agent/cos/goals.json`, CAMPAIGN.md
- Q: Ambiguous park match — which slug did you mean? · look first: `pulse_dashboard.py --open` (ask in one line only when two match)

## Handles alone
Board read, evidence gathering, classification, done lines, duplicate closes, parks with handoffs, board regen, the closing table.

## Comes back when
- A mission is LIVE but the next step is a verdict of his (what to resume first — never auto-pick)
- Killing something that still has an unshipped deliverable on disk
- Two missions look like the same job and only he knows which survives

## Needs approval
Deleting deliverables or handoff files · anything touching a client-facing thread · killing a mission that serves the active campaign.

## Needs
`.agent/missions.jsonl` · handoff store · pulse actions · work catalog · git log.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| missions.jsonl line malformed | skip the line, list it in the receipt | it is a live mission |
| handoff save fails | write the park reason on the missions line, retry save once | second fail |
| evidence ambiguous (shipped or not) | classify HIS-CALL with the two paths in the packet | always — that is the packet |
| board regen fails | leave the receipt table, note the regen command | never |

## Done means
Zero open missions older than 14 days without a park handoff · before/after counts in the receipt · every packet answered or explicitly held · `pulse_dashboard.py --open` shows the finisher rule satisfied (≤3 open).

## Ratchet log
- none yet
