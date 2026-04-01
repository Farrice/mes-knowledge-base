---
description: Inspect evolution history for any component — view Pareto frontier, detect regressions, trace causal chains through iteration history
---

# Evolution Audit

> Load `skills/self-evolving-systems/genius.md` first. This audits evolution history.

## When to Use
- After running `/self-evolve` or `/harness-evolve` — review what happened
- Suspecting an evolution introduced a regression
- Want to understand which changes actually drove improvement
- Periodic review of evolved components for drift or overfitting

## Input Required
- **Target**: The evolved component (workflow name or evolution store path)
- **Audit scope**: Full history or specific iteration range

## Execution

### Phase 1 — Load History
1. Read the evolution store for the target component
2. List all variants: iteration number, scores, timestamp
3. Identify the current deployed version and its origin iteration

### Phase 2 — Pareto Frontier Analysis
1. Plot all variants on accuracy × token cost axes (textual representation)
2. Identify the Pareto frontier (non-dominated variants)
3. Flag variants that are strictly dominated (worse on all metrics)
4. Identify "interesting failures" — low-scoring variants with novel approaches

### Phase 3 — Regression Detection
1. Compare each iteration against its predecessor
2. Flag regressions: where did performance DROP?
3. For each regression, trace the cause:
   - What changed in the code?
   - What execution traces differ?
   - Was the regression on specific examples or general?
4. Check if regressions were recovered in later iterations

### Phase 4 — Causal Analysis
1. Identify "confounded edits" — iterations that changed multiple things simultaneously
2. For the best-performing variants, isolate which specific changes drove improvement
3. Generate a "change impact map": which types of edits (prompt changes, flow restructuring, gate modifications) had the most consistent positive impact

### Phase 5 — Overfitting Check
1. Read the best variant's code for signs of overfitting:
   - Hard-coded if-chains targeting specific examples
   - Brittle pattern matching
   - Loss of generality vs. baseline
2. If overfitting detected, recommend: deploy the highest Pareto-frontier variant that avoids it

## Output
1. **Evolution timeline**: All iterations with scores and key changes
2. **Pareto frontier**: Best trade-off variants
3. **Regression report**: Where performance dropped and why
4. **Causal map**: Which change types drive improvement
5. **Overfitting assessment**: Is the best variant too specialized?
6. **Recommendation**: Deploy, continue evolving, or roll back
