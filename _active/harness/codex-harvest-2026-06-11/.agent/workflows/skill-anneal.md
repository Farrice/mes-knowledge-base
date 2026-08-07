---
description: Apply self-annealing to a specific skill's prompts
---

# Skill Anneal

> Load `skills/self-evolving-systems/genius.md` first. This bridges self-annealing and evolution.

## Operator Core Alignment

This workflow is the canonical source of truth for Skill-anneal behavior.
Global and local Skill-anneal wrappers must stay thin compatibility wrappers
that point back here, not competing behavior contracts.

Preserve these invariants:

- `/skill-anneal` is prompt-level skill/component annealing, not broad workflow evolution.
- Incomplete or vague goal packets produce a queue-only diagnosis and missing fields; do not edit the target.
- Annealing requires a target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause.
- If the skill belongs to a larger skill system, preserve upstream input, downstream output, and validation contract before editing.
- Limit edits to the single weakest criterion unless the user approves a broader rewrite.
- Side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`.
- Stop at a human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair.
- Route broad workflow evolution to `/self-evolve`; route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`.
- Real Codex subagents require explicit authorization.

## Pre-Flight Reads

1. `semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md`
2. `semantic_libraries/antigravity/primitives/skill-system-contract.md` when the skill belongs to a larger skill system
3. `semantic_libraries/antigravity/primitives/repeatability-spine-contract.md` when the anneal comes from a preservation lock

## When to Use
- A skill's outputs consistently score 6-7 on quality gates (acceptable but not great)
- You have a history of quality gate failures for this skill
- The skill has been manually tuned but specific failure modes persist
- Before loading genius.md for the skill — try annealing the SKILL.md first
- A component inside a skill system underperforms but the full orchestrator does not need a rewrite
- A Repeatability Spine pack identifies the component skill that lost the strongest part of the good run

## Input Required
- **Goal packet**: `target`, `scope`, `per_item_criteria`, `permitted_side_effect`, `proof_artifact`, `measurable_stop`, `turn_cap`, `evaluator`, `wake_up_check`, `human_checkpoint`, and `rollback_or_archive_rule`
- **Skill directory**: Path to the skill to anneal
- **Failure examples**: Past quality gate failures or low-scoring outputs (minimum 3)
- **Priority**: Which dimension to improve — intent alignment, expert standard, or adversarial resilience?
- **Boundary**: If the skill belongs to a skill system, name the upstream input, downstream output, and validation contract before editing
- **Repeatability lock**: If the issue came from `/repeatability-spine`, preserve the good example, failed example, and Preservation Lock while annealing

`rubric.md` and `test_inputs.md` equivalents are required before editing. They
can be local files, embedded tables, or verifier fixtures, but they must be
concrete enough for pass/fail scoring.

## Execution

### Phase 0 — Goal Packet And Council Preflight
1. Confirm the goal packet is complete.
2. Run the compact Evolution Council Preflight from `goal-loop-maintenance-contract.md`.
3. Limit the anneal to the single weakest criterion unless the user approves a broader rewrite.
4. If the packet is incomplete, write the missing-packet diagnosis and stop before edits.

### Phase 1 — Failure Mining
1. Read the skill's `SKILL.md` and active workflows
2. Collect past quality gate failures for this skill from Chain finalize logs
3. Group failures by pattern:
   - Same failure mode recurring? → Systematic issue in the skill text
   - Random failures? → Edge cases the skill doesn't cover
   - Quality ceiling? → The skill's methodology may be limiting

### Phase 2 — Root Cause on Skill Text
For each failure pattern:
1. Read the execution trace (what prompt was sent, what came back)
2. Identify which part of `SKILL.md` or the workflow governed that step
3. Diagnose: Is the instruction vague? Contradictory? Missing? Over-constrained?

### Phase 3 — Targeted Annealing
For each diagnosed weakness:
1. Propose a targeted edit to the skill text
2. Re-run against the failure examples
3. Score: Did the failure mode resolve?
4. Check: Did the edit break anything that was previously working?

### Phase 4 — Verify Generalization
1. Run the annealed skill against 3-5 NEW examples (not from the failure set)
2. Confirm no regression on normal performance
3. If regression detected, roll back the specific edit and try an alternative

## Output
1. **Goal packet and Evolution Council Verdict** — including proof artifact and stop condition
2. **Annealed skill files** — updated `SKILL.md` and/or workflow with targeted fixes
3. **Failure resolution report** — which failure modes were fixed, which persist
4. **Change log** — every edit with rationale and before/after scores
5. **Lesson learned entries** — append to the skill for permanent improvement

## Quality Gate

Reject the anneal if it lacks a rubric/test-input set, proof artifact,
measurable stop condition, turn cap, or explicit no-regression clause.

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_skill_anneal.py --check
python3 execution/verify_operator_core_skill_anneal.py
python3 execution/validate_skill.py source-command-skill-anneal
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
