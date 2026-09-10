# Mission: Manager Loop Harvest

## Charter
- Slug: manager-loop-harvest
- Mode: code
- Status: complete
- Goal: Harvest Nate B Jones's manager loop + recipe cards video into a native /job capability that runs hands-off in Claude Code and Codex, independently or together
- Created: 2026-09-10T02:33:06+00:00
- Updated: 2026-09-10T02:58:18+00:00
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
| T1 | claude | recipe-card-forge | complete | directives/recipe-card-standard.md + recipes/source-to-skill-harvest.md | directives/recipe-card-standard.md |  |  | write the standard and this job's own card |
| T2 | claude | build | complete | execution/recipe_cards.py + execution/job_board.py + session_brief jobs line | execution/job_board.py |  |  | board CLI incl. handoff/portable/status --all |
| T3 | claude | build | complete | steering_loop_hook.py JOB-HANDOFF mode + Stop observe + dialect lines | execution/hooks/steering_loop_hook.py |  |  | detector + two card variants |
| T4 | claude | verify | complete | execution/verify_job_handoff.py + parity job prompt | execution/verify_job_handoff.py |  |  | sabotage both directions |
| T5 | claude | extract | complete | skills/nate-b-jones-manager-loop/ (6 workflows, prompts-v2) + registration | skills/nate-b-jones-manager-loop/SKILL.md |  |  | /extract on the transcript |
| T6 | claude | build | complete | .agent/workflows/job.md + /go route row + 7 seed recipes | .agent/workflows/job.md |  |  | front door + seeds |
| T6b | claude | build | complete | global bridges + Homebase JOBS panel + cross-harness lane round-trip | .agent/handoffs/2026-09-09-manager-loop-harvest.md |  |  | back on claude |
| T7 | claude | job-closeout | complete | four-question closeout, ratchet, memory, verdict | .agent/missions/manager-loop-harvest/closeout.md |  |  | after all lanes |

## Execution Receipt
- Planned lanes: T1, T2, T3, T4, T5, T6, T6b, T7
- Executed lanes: T1, T2, T3, T4, T5, T6, T6b, T7
- Skipped or blocked lanes: [none]
- Proof artifacts: directives/recipe-card-standard.md, execution/job_board.py, execution/hooks/steering_loop_hook.py, execution/verify_job_handoff.py, skills/nate-b-jones-manager-loop/SKILL.md, .agent/workflows/job.md, .agent/handoffs/2026-09-09-manager-loop-harvest.md, .agent/missions/manager-loop-harvest/closeout.md
- Validators run: [none]
- Resume command: /mission resume manager-loop-harvest

## Fresh Session Packet
- Required: False
- Fresh session packet: `[none]`
- Resume command: `/mission resume manager-loop-harvest`
- Next command: `python3 execution/job_board.py lanes manager-loop-harvest`
- State sources: .agent/missions/manager-loop-harvest/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- None yet
