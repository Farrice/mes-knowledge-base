---
description: Run a MetaHarness-style self-improvement loop on any Antigravity component — workflow, prompt, retrieval logic, or orchestration pattern
---

# Self-Evolve

> Load `skills/self-evolving-systems/genius.md` first. This is the master evolution command.

## When to Use
- A workflow/skill has plateaued despite manual tuning
- Quality gate scores consistently land 6-7 (good but not great)
- Same error class recurs 3+ times despite self-annealing fixes
- You want to discover approaches you wouldn't think of manually

## Input Required
- **Target**: The specific file or component to evolve (workflow, skill prompt, directive section)
- **Evaluation metric**: How to score each variant (quality gate score, accuracy, token cost, etc.)
- **Search set**: Hard examples or past failures to test against (minimum 3, ideal 10-20)
- **Iteration count**: 5 for quick sprint, 10-20 for full evolution
- **Constraints**: What the proposer CAN'T change (safety rails, brand voice, required behaviors)

## Execution

### Phase 1 — Establish Baseline
1. Read the current version of the target component
2. Run it against the search set
3. Record baseline score per metric
4. Archive as `evolution_store/baseline/` with code + scores + traces

### Phase 2 — Propose
For each iteration:
1. Inspect prior variants: code, scores, and execution traces
2. Diagnose: What failed? Which earlier design choices contributed?
3. Decide: Local edit (tweak prompt, adjust flow) OR structural rewrite (new approach)?
4. Generate the new variant as a complete, self-contained version

**Proposer freedom**: The proposer can inspect ANY prior variant — including low-performing ones (avoids local maxima). No parent-selection rule.

### Phase 3 — Evaluate
1. Run lightweight validation first (does it parse? does it run on 1-2 examples?)
2. If validation passes, run against the full search set
3. Score on all metrics (accuracy, token cost, etc.)
4. Log to `evolution_store/variant_NNN/`: code, scores, execution traces (JSON)

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
1. **Baseline score** with execution traces
2. **Pareto frontier** of discovered variants
3. **Recommended variant** with rationale
4. **Key discoveries** — what the proposer learned
5. **Deployment recommendation** — swap baseline for evolved version?

---

## Quality Gate

> **🛡️ Pre-deployment check**: Before recommending deployment, verify the evolved variant on 3+ examples OUTSIDE the search set to confirm it generalizes.
