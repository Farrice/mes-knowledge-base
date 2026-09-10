---
job: harness-audit-repair
name: Harness audit / repair mission
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Take a "something in the system is off" complaint to a green baseline: root cause named, mechanical failures healed and re-verified, judgment failures surfaced with the exact command, nothing loosened to fake green.

## Sub-jobs / lanes
- L1 Baseline proof — `/system-audit` step 1 verifiers (`verify_google_operator_core.py`, `verify_codex_authority.py`, `verify_autopilot_runtime_preflight.py`, `verify_skill_system_contract.py`, `verify_swarm_meter.py`, `verify_harness_behavior_report.py`, `platform_compiler.py lint --json`) [parallel]
- L2 Quick vitals — `/health-check`: `harness_status.py --plain`, `system_health.py --quick`, `operator_core_status.py --plain` [parallel]
- L3 Classify — `execution/self_heal.py report` → AUTO / EVIDENCE / JUDGMENT per failure [after: L1, L2]
- L4 Heal mechanical — `self_heal.py heal` (scoped auto-commits) then re-verify the same check; `[COULD NOT FIX]` when still red [after: L3]
- L5 Root cause the rest — for EVIDENCE items: read the failing script, name the cause, fix the artifact not the assertion [after: L3]
- L6 Routing + authority map — `verify_control_intent.py`, compare `CODEX.md` / `AGENTS.md` / `~/.codex/AGENTS.md` / `autopilot.md`; bridge map per control command [after: L4, L5]
- L7 Record — solution card via `/extract-approach` when non-trivial; `failure_learning.py`; lane merge receipts [after: L6]

## Ask me first
- Q: What did you see, in your words (the felt drift)? · look first: `.agent/sessions/steering-observe.jsonl`, `harness_behavior_report.py`
- Q: Is this Claude-side, Codex-side, or both? · look first: the newest rollout in `~/.codex/sessions/`, `.agent/handoffs/`

## Handles alone
Verifiers, vitals, classification, mechanical heals, re-verification, root-causing, maps, records, lane worktree.

## Comes back when
- A JUDGMENT-class failure (taste, unexplained) — packet with diagnosis + exact command
- A fix needs `~/.codex` or `~/.claude` global edits, or `.codex/hooks.json` (trust hashes)
- CHRONIC (heal failed ≥3×) — stop retrying, packet

## Needs approval
Global config edits · deleting anything outside the repo · disabling a hook or verifier · merging a parked lane over main's drift.

## Needs
Worktree lane · `.venv` · the verifier fleet · self_heal.py · session forensics access.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| verifier flakes (timeout) | rerun once with the 15s cap lifted | flakes twice |
| heal doesn't re-verify green | mark `[COULD NOT FIX]`, move on | it is the failure he reported |
| assertion loosened to pass ("laundering") | revert; structurally forbidden | never |
| lane parked on merge (dirty main) | `worktree_lane.py merge --lane <branch>` with the audit | Law-3 audit reports a real drop |

## Done means
`self_heal.py report` clean or every JUDGMENT item surfaced with a command · baseline verifiers green (deferred ones named) · solution card when warranted · lane merged with receipts.

## Ratchet log
- none yet
