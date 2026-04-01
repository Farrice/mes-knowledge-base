---
description: Run Karpathy-style experiment loops with git-branch isolation — propose hypothesis, test, commit only if improvement, iterate
---

# Auto-Experiment

> Load `skills/self-evolving-systems/genius.md` first. This is the Karpathy autoresearch pattern applied to Antigravity.

## When to Use
- You want to test multiple hypotheses about a workflow/skill improvement
- You're willing to let the system iterate autonomously for a defined period
- You want to discover optimizations you wouldn't manually try
- You have a clear metric for "better" (score, speed, token cost)

## Input Required
- **Target**: Component to experiment on
- **Hypothesis** (optional): Starting theory about what to improve. If omitted, proposer generates hypotheses.
- **Metric**: How to measure improvement (must be quantitative)
- **Max experiments**: Number of iterations to run (5-20)
- **Commit threshold**: Only commit changes that improve metric by at least X%

## Execution

### Phase 1 — Setup
1. Create git branch: `experiment/[target]-[timestamp]`
2. Record baseline metric on main branch
3. Define the experiment log format:
   ```
   experiment_NNN/
   ├── hypothesis.md      # What we're testing
   ├── changes.diff       # What was changed
   ├── result.json        # Metric score + traces
   └── committed: yes/no  # Did it pass the threshold?
   ```

### Phase 2 — Experiment Loop
For each experiment:
1. **Hypothesize**: What change might improve the metric?
   - If prior experiments exist, review their results first
   - Avoid re-testing failed hypotheses unless with a new twist
2. **Change**: Make the targeted modification
3. **Test**: Run against evaluation examples
4. **Evaluate**: Compare against baseline/best-so-far
5. **Commit or discard**: Only commit if improvement ≥ threshold
6. **Log**: Record hypothesis, changes, result regardless of outcome

### Phase 3 — Synthesize
1. Review all experiments — committed AND discarded
2. Identify emergent patterns (what types of changes consistently help?)
3. Generate a final "best practices" summary from successful experiments
4. Present the cumulative improvement: baseline → final

## Output
1. **Experiment log**: All N experiments with hypotheses, changes, results
2. **Committed improvements**: Only the changes that passed threshold
3. **Cumulative improvement**: Total metric gain from baseline
4. **Emergent patterns**: What types of changes consistently helped
5. **Git branch** ready for merge or further iteration
