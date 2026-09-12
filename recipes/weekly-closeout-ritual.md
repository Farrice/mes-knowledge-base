---
job: weekly-closeout-ritual
name: Weekly closeout ritual
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
Run the CORE outer-loop closure (~10 min, always completes) — evolution catch-up, revenue drain, calibration, evolution queue, close — with the DEEP monthly pass when due, never skipped for weight.

## Sub-jobs / lanes
- L1 Evolution catchup — `python3 execution/evolution_orchestrator.py auto`, `status` [parallel]
- L2 Revenue drain — `python3 execution/revenue_tracker.py pipeline`, 5 oldest pendings, one question each [parallel]
- L3 Calibration — `python3 execution/eval_harness.py calibrate --days 7`, `python3 execution/recall_logger.py report --days 7` [parallel]
- L4 Evolution queue — `python3 execution/evolution_orchestrator.py queue`, present the top item only [after: L1]
- L5 Deep pass — monthly only: `python3 execution/health_metrics.py flags --latest`, `python3 execution/skill_auditor.py audit`, `python3 execution/forge_gate.py status`, taste ratchet from `.agent/jam/taste-ledger.jsonl` [parallel]
- L6 Close — one-paragraph summary, `python3 execution/chain_runner.py finalize` [after: L2, L3, L4]

## Ask me first
- Q: Revenue or dead for each of the 5 oldest pendings? (max 5, one at a time) · look first: `execution/revenue_tracker.py pipeline` output
- Q: Accept or reject the one evolution queue item? · look first: `execution/evolution_orchestrator.py queue` output

## Handles alone
Evolution catch-up, calibration report, deep-pass audits (monthly), report drafting, finalize.

## Comes back when
- The 5 revenue questions (mandatory, one at a time, never more than 5)
- The one evolution-queue accept/reject decision
- Monthly DEEP-pass pending-review approvals — nothing executes without his yes

## Needs approval
Executing a pending-review archive or prune · accepting an evolution-queue item that changes production behavior.

## Needs
`execution/evolution_orchestrator.py` · `execution/revenue_tracker.py` · `execution/eval_harness.py` · `execution/skill_auditor.py` · `.agent/jam/taste-ledger.jsonl`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| inflation guardrail fires (scores clustering 8+) | show the flag and the worst offender, keep going | never hide it |
| evolution queue is empty | skip silently | never |
| DEEP pass runs long | CORE steps still complete and self-finalize | DEEP is skippable, CORE never is |

## Done means
CORE steps 1, 2, 3, 4, 6 all ran and self-finalized · revenue queue drained by up to 5 · finalize receipt exists with the closing summary.

## Ratchet log
- none yet
