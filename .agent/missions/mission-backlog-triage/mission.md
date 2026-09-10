# Mission: Mission backlog triage

## Charter
- Slug: mission-backlog-triage
- Mode: system
- Status: active
- Goal: Drain the 54 open missions: finish, park, or kill each; packets only for the calls that are Farrice's; zero open missions older than 14 days without a park handoff
- Created: 2026-09-10T12:20:34+00:00
- Updated: 2026-09-10T12:34:21+00:00
- Librarian: not_applicable

## Validation Contract
- Define correctness before execution.
- Assign every feature or workstream to at least one assertion.
- Run scrutiny and user-outcome validators at milestone boundaries.

| ID | Assertion | Covered by | Validator | Pass signal |
|---|---|---|---|---|
| - | No assertions recorded yet | - | - | - |

## Artifact Contract
- Type: none


## Approved Package Load Set
- None recorded.


## Mission Activation Queue
| ID | Owner | Workflow/Skill | Status | Expected artifact | Evidence path | Assertion | Blocker | Next action |
|---|---|---|---|---|---|---|---|---|
| L1 | claude | Board read | complete | `python3 execution/pulse_dashboard.py --open`; `handoff_store.py list --rich --all`; `job_board.py status --all` | scratchpad/open-missions.json |  |  |  |
| L2 | claude | Evidence per mission | complete | for each open line: what shipped (deliverable paths, git log, catalog `work_catalog.py`), last handoff, days idle | scratchpad/evidence-a.json+evidence-b.json |  |  |  |
| L3 | claude | Classify | complete | DONE-UNCLOSED (write the done line) / DUPLICATE (close to the survivor) / STALE-DEAD (kill) / LIVE (park with hint) / HIS-CALL (packet) | scratchpad/triage.json |  |  |  |
| L4 | claude | Close the mechanical ones | complete | done lines appended to `.agent/missions.jsonl`; duplicates closed with `outcome: superseded by <slug>` | /Users/farricecain/Google Antigravity/.agent/missions.jsonl |  |  |  |
| L5 | claude | Park the live ones | complete | `python3 execution/pulse_actions.py park <slug> --reason "…"`; rich parks also `handoff_store.py save --thread <slug> --status blocked --hint … --unfinished …` | .agent/handoffs/2026-09-10-god-agent-offer.md |  |  |  |
| L6 | claude | Packets for his calls | blocked | one per HIS-CALL mission: finish / park / kill with the evidence line | .agent/missions/mission-backlog-triage/decisions.md |  | packet #1: Kith-style MyBPM site — finish / park / kill is his |  |
| L7 | claude | Regenerate + receipt | complete | pulse board regen, `session_brief` missions line, one closing table (before/after counts) | /Users/farricecain/Google Antigravity/.agent/pulse/pulse-board.html |  |  |  |

## Execution Receipt
- Planned lanes: L1, L2, L3, L4, L5, L6, L7
- Executed lanes: L1, L2, L3, L4, L5, L7
- Skipped or blocked lanes: L6: packet #1: Kith-style MyBPM site — finish / park / kill is his
- Proof artifacts: scratchpad/open-missions.json, scratchpad/evidence-a.json+evidence-b.json, scratchpad/triage.json, /Users/farricecain/Google Antigravity/.agent/missions.jsonl, .agent/handoffs/2026-09-10-god-agent-offer.md, .agent/missions/mission-backlog-triage/decisions.md, /Users/farricecain/Google Antigravity/.agent/pulse/pulse-board.html
- Validators run: [none]
- Resume command: /mission resume mission-backlog-triage

## Fresh Session Packet
- Required: False
- Fresh session packet: `[none]`
- Resume command: `/mission resume mission-backlog-triage`
- Next command: `python3 execution/job_board.py next mission-backlog-triage`
- State sources: .agent/missions/mission-backlog-triage/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- None yet
