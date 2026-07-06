---
description: Apply self-annealing to a specific skill's prompts
---

# Skill Anneal

> Load `skills/self-evolving-systems/genius.md` first. This bridges self-annealing and evolution.

## Operator Core Alignment

This workflow is the canonical source of truth for Skill-anneal behavior:
prompt-level skill/component annealing, not broad workflow evolution.

Incomplete or vague goal packets produce a queue-only diagnosis. Annealing
requires a target skill directory, failure examples, rubric/test-input set,
proof artifact, measurable stop condition, turn cap, and explicit
no-regression clause.

Annealing must preserve upstream input, downstream output, and validation
contract. Limit edits to the single weakest criterion unless the user approves
a broader rewrite. Side effects must be local, reversible, and inside
`/Users/farricecain/Google Antigravity`.

Stop at a human checkpoint for broader workflow evolution, global mirrors,
external actions, broad archive/delete, destructive cleanup, new dependencies,
failed validation, or Mission repair. Route broad workflow evolution to
`/self-evolve`. Real Codex subagents require explicit authorization.

Verifier phrases: Annealing requires a target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause. preserve upstream input, downstream output, and validation contract. Limit edits to the single weakest criterion unless the user approves a broader rewrite. Side effects must be local, reversible, and inside `/Users/farricecain/Google Antigravity`. Stop at a human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair. Route broad workflow evolution to `/self-evolve`.

## When to Use
- A skill's outputs consistently score 6-7 on quality gates (acceptable but not great)
- You have a history of quality gate failures for this skill
- The skill has been manually tuned but specific failure modes persist
- Before loading genius.md for the skill — try annealing the SKILL.md first

## Input Required
- **Skill directory**: Path to the skill to anneal
- **Failure examples**: Past quality gate failures or low-scoring outputs (minimum 3)
- **Priority**: Which dimension to improve — intent alignment, expert standard, or adversarial resilience?

## Execution

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
1. **Annealed skill files** — updated `SKILL.md` and/or workflow with targeted fixes
2. **Failure resolution report** — which failure modes were fixed, which persist
3. **Change log** — every edit with rationale and before/after scores
4. **Lesson learned entries** — append to the skill for permanent improvement
