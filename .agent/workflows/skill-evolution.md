---
description: Skill evolution cycle
---

# /skill-evolution — Skill Evolution Workflow

Run the autoresearch-inspired evolution loop on a skill to improve its weakest dimension or workflow.

**Before starting**: Read `directives/evolution-direction.md` for current priorities and constraints.

## Usage

```
/skill-evolution <skill-name>
/skill-evolution <skill-name> --target <workflow-name>
/skill-evolution --list-candidates
```

## Steps

### 0. Read Evolution Direction

Read `directives/evolution-direction.md`. Check:
- Current priorities (which skills to target)
- Constraints (what not to change)
- Stopping criteria (when to pause)
- Evolution History (avoid re-testing failed hypotheses)

### 1. Identify Target Skill

If `--list-candidates` is used, scan Performance Log for skills with:
- 20+ entries (sufficient data)
- Declining trend
- Weakest dimension < 6/10
- Recent regression

Present candidates ranked by improvement potential. Wait for user to select one.

If a specific skill is given, proceed directly.

### 2. Benchmark Current State

```bash
python execution/skill_benchmark.py benchmark <skill-name>
```

Present the benchmark report:
- Performance summary (avg scores, trend)
- Weakest workflow + weakest dimension
- Recommendations

### 3. CHECKPOINT: Select Target

Present the evolution target options to the user:

```markdown
## Evolution Target Options

1. **Weakest Workflow**: [name] (avg [X]/10) — improve process or patterns
2. **Weakest Dimension**: [name] (avg [X]/10) — improve [specific aspect]
3. **User Choice**: Specify a different focus

Which target should we evolve? (or type a custom focus)
```

Wait for user decision.

### 4. Write Hypothesis

Based on the selected target, analyze the current workflow and formulate a hypothesis:

**Read the current workflow file** — understand its structure, genius pattern usage, quality gate, and output contract.

**Read the genius.md** — understand available patterns that might be underused.

**Read recent Performance Log notes** — what feedback has been given on this skill's outputs?

Write the hypothesis:

```markdown
## Evolution Hypothesis

**Skill**: [name]
**Target**: [workflow or dimension]
**Current Score**: [X/10]
**Problem**: [What's weak — be specific]
**Hypothesis**: [What change will improve it and why]
**Expected Impact**: [Score improvement target]
```

Present to user for approval.

### 5. Generate Variant

Create a variant workflow file:

```
skills/[skill-name]/workflows/[workflow-name].variant.md
```

The variant must:
- Keep the same Output Contract
- Keep the same genius.md reference
- Modify only the targeted aspect
- Document what changed at the top

### 6. Test Both Versions (Time-Boxed: 10 min/task)

**Time limit: 10 minutes per benchmark task.** This prevents over-deliberation and forces decisive evaluation (Karpathy principle: constrained cycle time).

For each of the 3 benchmark tasks (from `skill_benchmark.py`):

**A.** Execute the current workflow → score output (Quality Gate 3-point check) — 10 min max
**B.** Execute the variant workflow → score output (same rubric) — 10 min max

Record all scores. Scoring must be blind (score current first, then variant, without comparing).

### 7. Compare Results (Binary Decision)

```markdown
## Evolution Results

| Benchmark Task | Current | Variant | Delta |
|---------------|---------|---------|-------|
| Task 1 | [X]/10 | [Y]/10 | [+/-] |
| Task 2 | [X]/10 | [Y]/10 | [+/-] |
| Task 3 | [X]/10 | [Y]/10 | [+/-] |
| **Average** | **[X]** | **[Y]** | **[+/-]** |

**Verdict**: [KEEP / DISCARD]
**Reason**: [Why]
```

**Decision rule (binary — no "marginal"):**
- Variant composite >= 7 AND wins by 1+ avg → **KEEP**
- Everything else → **DISCARD**

No retries during evolution. Ambiguity kills velocity.

### 8. CHECKPOINT: User Approval

Present the comparison. If the variant wins:
- Show the specific changes made
- Ask for permission to replace the current workflow

If the variant loses or ties:
- Recommend discarding
- Note what was learned

### 9. Apply Result

**If KEPT:**
- Replace current workflow with variant content
- Delete the .variant.md file
- Add Evolution Log entry to genius.md
- Log to Performance Log (status: "Keep", experiment_tag: "evolution-[date]")
- **Git commit the change:**
  ```bash
  git add skills/[skill-name]/workflows/[workflow-name].md
  git add skills/[skill-name]/genius.md
  git commit -m "evolution: [skill-name] — [hypothesis-summary]
  
  Result: KEPT — Score improved from [X] to [Y] (+[delta])
  Hypothesis: [what was tested]
  Target: [workflow or dimension]"
  ```

**If DISCARDED:**
- Delete the .variant.md file
- Add Evolution Log entry to genius.md (marked as discarded)
- Log to Performance Log (status: "Discard", experiment_tag: "evolution-[date]")

```python
from execution.log_performance import log_output

log_output(
    output=f"Evolution: {skill_name} — {hypothesis_summary}",
    skill=skill_name,
    workflow="skill-evolution",
    task_type="System",
    quality_score=variant_avg,
    status="Keep" if kept else "Discard",
    notes=f"Target: {target}. Delta: {delta:.1f}. Hypothesis: {hypothesis}",
    experiment_tag=f"evolution-{date}",
)
```

### 10. Cross-Pollination Check

If the variant was KEPT and the improvement is pattern-based (not skill-specific):

```python
from execution.pattern_propagation import find_related_skills

candidates = find_related_skills(skill_name, pattern_type)
```

If candidates found, note them for the next cross-pollination cycle.

### 11. Update Evolution Direction

Update `directives/evolution-direction.md`:
- Add row to **Evolution History** table with date, skill, hypothesis, result, score delta, notes
- Update **System Status** table (increment activation count, update last activated date)
- If 3 consecutive DISCARDs on same skill, note in Stopping Criteria that skill should be paused

### 12. Report

```markdown
## Evolution Complete

**Skill**: [name]
**Target**: [workflow/dimension]
**Result**: [KEPT/DISCARDED]
**Score Change**: [X] → [Y] ([+/-])
**Hypothesis**: [summary]
**Cross-Pollination Candidates**: [list or "None"]
**Git Commit**: [hash if KEPT, N/A if DISCARDED]
**Evolution Direction Updated**: Yes
```

## Protocol Reference

Full protocol: `directives/skill-evolution-protocol.md`
Evolution compass: `directives/evolution-direction.md`
Benchmark tool: `execution/skill_benchmark.py`
Performance logger: `execution/log_performance.py`
