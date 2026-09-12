---
job: harness-mechanism-and-verifier
name: Harness mechanism + both-direction verifier
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Build or repair a harness mechanism and prove it with a verifier fixture that sabotages both directions — proving the good path executes and the bad path is refused or parked — before it lands on main.

## Sub-jobs / lanes
- L1 Scope — which mechanism (script, hook, workflow) and its risk surface [parallel]
- L2 Build and repair — write or fix `execution/<mechanism>.py` matching existing patterns [after: L1]
- L3 Verifier fixture — `execution/verify_<mechanism>.py`; prove the good path AND the bad path, pattern in `execution/verify_mission_runner.py` [after: L2]
- L4 Wiring check — `.agent/health/wiring-index.json`, hook wiring in `.claude/settings.json` → `execution/hooks/` [after: L2]
- L5 Lane land — `python3 execution/worktree_lane.py bootstrap` then `merge` [after: L3, L4]
- L6 Receipt — `python3 execution/job_board.py status`, before/after proof [after: L5]

## Ask me first
- Q: Which mechanism, and what does "broken" look like today? · look first: `.agent/health/wiring-index.json`, `.agent/health/daily-audit.json`
- Q: Does this touch the cost gate or the fleet write guard? · look first: `directives/merge-discipline.md`

## Handles alone
Build and repair, fixture design, wiring check, lane bootstrap, merge attempt, receipt.

## Comes back when
- The fixture cannot prove the bad path is refused (mechanism has no refusal net)
- A fix touches the cost gate or the fleet write guard
- The lane merge PARKS on dirty main

## Needs approval
Nothing outward by default — repo-internal. The two tree interlocks named in the Compass Doctrine (dangerous-git patterns, fleet write guard) block mechanically, never by agent judgment.

## Needs
`execution/worktree_lane.py` · `execution/job_board.py` · `directives/merge-discipline.md` · the existing `execution/verify_*.py` library as pattern reference.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| fixture only proves the happy path | add the sabotage case before shipping | never ship a one-direction verifier |
| lane merge PARKS | print the absorb command, stop | never force past the fleet write guard |
| mechanism would touch the live queue during test | build the fixture with dry-run or dir overrides first | it must touch anything outward |

## Done means
`execution/verify_<mechanism>.py` exists and passes, proving both directions · wiring-index reflects the change · lane merged clean or PARKED with the absorb command named.

## Ratchet log
- none yet
