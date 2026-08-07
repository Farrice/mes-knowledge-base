---
description: Improve a workflow, prompt, retrieval rule, or orchestration pattern using feedback, failure history, performance logs, regression checks, and measured evolution without adding unnecessary bloat
---

# Self-Evolve

> Load `skills/self-evolving-systems/genius.md` first. This is the master evolution command.

## Operator Core Alignment

This workflow is the canonical source of truth for Self-evolve behavior. Global
and local Self-evolve wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/self-evolve` is mutation-gated measured evolution, not casual improvement.
- Incomplete or vague goal packets produce a queue-only diagnosis and missing fields; do not edit the target.
- Mutation requires a complete goal packet, Evolution Council Verdict, baseline, search set, measurable stop condition, turn cap, proof artifact, and no-regression check.
- Permitted side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`.
- Stop at a human checkpoint for global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or scope expansion.
- Do not mutate Mission unless `verify_mission_activation_contract.py` fails and the user explicitly approves Mission repair.
- Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`; use `/self-evolve` for explicit feedback-backed workflow evolution.
- Real Codex subagents require explicit authorization.

## Pre-Flight Reads

1. `semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md`
2. `semantic_libraries/antigravity/primitives/skill-system-contract.md` when the target is a skill system or orchestrator
3. `semantic_libraries/antigravity/primitives/repeatability-spine-contract.md` when the search set comes from a failed route, revision, or regression
4. `semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md` when the evolution changes context policy, review loops, dependency safety, source truth, package behavior, or launch/use-now behavior

## When to Use
- A workflow/skill has plateaued despite manual tuning
- Quality gate scores consistently land 6-7 (good but not great)
- Same error class recurs 3+ times despite self-annealing fixes
- You want to discover approaches you wouldn't think of manually
- A skill system or orchestrator workflow has clear failure evidence in routing, handoffs, validation, or cold-start usability
- A Repeatability Spine pack supplies good examples, failed examples, preservation locks, and regression phrases that can become an evolution search set

## Input Required
- **Goal packet**: `target`, `scope`, `per_item_criteria`, `permitted_side_effect`, `proof_artifact`, `measurable_stop`, `turn_cap`, `evaluator`, `wake_up_check`, `human_checkpoint`, and `rollback_or_archive_rule`
- **Target**: The specific file or component to evolve (workflow, skill prompt, directive section)
- **System contract**: If evolving a skill system, read `semantic_libraries/antigravity/primitives/skill-system-contract.md` and preserve component boundaries
- **Evaluation metric**: How to score each variant (quality gate score, accuracy, token cost, etc.)
- **Search set**: Hard examples or past failures to test against (minimum 3, ideal 10-20)
- **Repeatability evidence**: If available, use `/repeatability-spine` outputs as the failure pack and preserve its regression guards
- **Iteration count**: 5 for quick sprint, 10-20 for full evolution
- **Constraints**: What the proposer CAN'T change (safety rails, brand voice, required behaviors)
- **Agentic engineering packet**: Required when context, dependency, review-loop, or source-truth behavior changes; include source truth, context plan, work chunks, review stop, dependency gate, structure pass, use-now artifact, and hardening proof

Reject vague requests like "improve this" as mutation-ready. If the goal packet
is incomplete, produce a queue-only diagnosis and the missing fields; do not
edit the target.

Reject vague agentic loops like "keep improving until it works" unless there is
a measurable stop condition, turn cap, no-regression check, and next action when
the loop fails.

## Execution

### Phase 0 — Evolution Council Preflight
1. Run the Mark Kashef-style council from `goal-loop-maintenance-contract.md`.
2. Produce the `Evolution Council Verdict` before changing files.
3. Require the Skeptic role to name at least one plausible failure mode.
4. Confirm the permitted side effect is local, reversible, and inside this workspace.
5. Stop at the human checkpoint when broad archive/delete/global mutation, external action, or failed validation changes scope.

### Phase 1 — Establish Baseline
1. Read the current version of the target component
2. Run it against the search set
3. Record baseline score per metric
4. Archive as `evolution_store/baseline/` with code + scores + traces

### Phase 2 — Propose
For each iteration:
1. Inspect prior variants: code, scores, and execution traces
2. Diagnose: What failed? Which earlier design choices contributed?
3. Shrink the change until it is reviewable as a small chunk with exact source paths.
4. Decide: Local edit (tweak prompt, adjust flow) OR structural rewrite (new approach)?
5. Generate the new variant as a complete, self-contained version
6. If the variant introduces a new package, repo, CLI, MCP server, or plugin, run the dependency safety gate before recommending install or adoption.

**Proposer freedom**: The proposer can inspect ANY prior variant — including low-performing ones (avoids local maxima). No parent-selection rule.

### Phase 3 — Evaluate
1. Run lightweight validation first (does it parse? does it run on 1-2 examples?)
2. If validation passes, run against the full search set
3. Score on all metrics (accuracy, token cost, etc.)
4. Check the review loop finish line: pass condition, turn cap, no-regression check, and next action on failure
5. Log to `evolution_store/variant_NNN/`: code, scores, execution traces (JSON)

### Phase 4 — Iterate
1. Repeat Phases 2-3 for the specified number of iterations
2. After each iteration, update the Pareto frontier (accuracy vs. cost)
3. The proposer may inspect any prior variant when proposing new ones

### Phase 5 — Report
1. Present the Pareto frontier: all non-dominated variants
2. Recommend the best variant for the user's priority (accuracy-first? cost-first? balanced?)
3. Show key discoveries: what worked, what didn't, surprising findings
4. Diff between baseline and recommended variant
5. User decides whether to deploy the evolved version

## Output
An evolution report containing:
1. **Goal packet** with proof artifact, stop condition, turn cap, and wake-up check
2. **Evolution Council Verdict** with owner, risk, and permitted side effect
3. **Baseline score** with execution traces
4. **Pareto frontier** of discovered variants
5. **Recommended variant** with rationale
6. **Key discoveries** — what the proposer learned
7. **Deployment recommendation** — swap baseline for evolved version?

---

## Quality Gate

> **🛡️ Pre-deployment check**: Before recommending deployment, verify the evolved variant on 3+ examples OUTSIDE the search set to confirm it generalizes.

Also reject deployment if the proof artifact is missing, the stop condition
cannot be checked with a command or review surface, or the no-regression clause
does not name what must remain passing.

For agentic engineering changes, also reject deployment if the change bloats
context, hides source truth, installs risky dependencies silently, produces no
use-now artifact, or leaves structure cleanup as a vague future task.

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_self_evolve.py --check
python3 execution/verify_operator_core_self_evolve.py
python3 execution/validate_skill.py source-command-self-evolve
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
