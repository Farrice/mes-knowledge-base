# Skill Evolution Protocol

> **Trigger**: Performance Log has 20+ entries for any skill, OR a regression is detected, OR user runs `/skill-evolution`.
> **Inspired by**: Karpathy's autoresearch — the agent modifying train.py and keeping winning changes.
> **Purpose**: Systematically improve skill workflows through variant testing, not random edits.
> **Extends**: Feedback Ratchet (Phase 1) — uses its data to drive improvement.
> **Effective**: 2026-03-10

---

## Core Principle

Skills are mutable code. Like autoresearch's `train.py`, workflow files can be modified, tested, and improved — but only through controlled experimentation with objective evaluation. No change ships without beating the current version on benchmark tasks.

---

## When to Trigger Evolution

| Trigger | Condition | Action |
|---------|-----------|--------|
| **Regression** | Quality score > 1.0 below rolling average | Immediate: investigate + fix |
| **Plateau** | 10+ outputs with < 0.5 variance | Scheduled: try variant approaches |
| **User request** | `/skill-evolution <skill-name>` | On-demand: full evolution cycle |
| **Data threshold** | 20+ Performance Log entries for a skill | Scheduled: first comprehensive review |
| **Cross-pollination** | Related skill improved a shared pattern | Candidate: apply transferred pattern |

---

## The Evolution Loop

### Step 1: Benchmark Current State

```bash
python execution/skill_benchmark.py benchmark <skill-name>
```

This produces:
- Performance history (avg quality, trend, per-workflow breakdown)
- Weakest workflow and dimension
- Domain-matched benchmark tasks
- Actionable recommendations

### Step 2: Identify the Target

From the benchmark report, pick ONE target for improvement:

**Priority order:**
1. Declining trend → Fix the regression first
2. Weakest dimension (< 6/10) → Address the gap
3. Weakest workflow → Improve the worst performer
4. Highest-traffic workflow → Even small gains compound

**Do NOT try to fix everything at once.** One change per evolution cycle.

### Step 3: Hypothesize the Fix

Before modifying anything, write a hypothesis:

```markdown
## Evolution Hypothesis

**Skill**: [name]
**Target**: [workflow or dimension]
**Current Score**: [X/10]
**Problem**: [What's weak — be specific]
**Hypothesis**: [What change will improve it and why]
**Expected Impact**: [Score improvement target]
```

### Step 4: Generate Variant

Create a variant workflow file:

```
skills/[skill-name]/workflows/[workflow-name].variant.md
```

The variant MUST:
- Keep the same Output Contract (produces the same deliverable type)
- Keep the same genius.md reference (don't change the knowledge base)
- Modify only the targeted aspect (process steps, inline patterns, quality gate criteria)
- Document what changed at the top of the file

### Step 5: Test Variant

Run the variant against all 3 benchmark tasks for the skill's domain:

1. Execute the **current** workflow against each benchmark task
2. Execute the **variant** workflow against the same benchmark tasks
3. Score both outputs using the Quality Gate (`directives/quality_gate.md`)
4. Compare scores across all 3 dimensions

**Scoring must be blind** — score the current version first, then the variant, without comparing during scoring.

### Step 6: Decide

| Result | Action |
|--------|--------|
| Variant wins by 1+ avg | **KEEP**: Replace current workflow with variant |
| Variant ties (< 0.5 diff) | **DISCARD**: Not enough improvement to justify change |
| Variant loses | **DISCARD**: Current version is better |

### Step 7: Log the Result

Whether kept or discarded, log the evolution attempt:

**If KEPT** — update the skill's genius.md Evolution Log:

```markdown
## Evolution Log

### [Date] — [Target] Improvement
- **Hypothesis**: [What you tried]
- **Result**: KEPT — Score improved from X to Y
- **Change**: [Brief description of what changed]
- **Benchmark scores**: Current [X, X, X] → Variant [Y, Y, Y]
```

**If DISCARDED** — still log to prevent re-trying the same thing:

```markdown
### [Date] — [Target] Attempt (Discarded)
- **Hypothesis**: [What you tried]
- **Result**: DISCARDED — No improvement (or regression)
- **Lesson**: [What this taught us about the skill]
```

Also log to Performance Log:

```python
from execution.log_performance import log_output

log_output(
    output=f"Evolution: {skill_name} — {hypothesis_summary}",
    skill=skill_name,
    workflow="skill-evolution",
    task_type="System",
    quality_score=variant_avg_score,
    status="Keep" if kept else "Discard",
    notes=f"Hypothesis: {hypothesis}. Delta: {delta}",
    experiment_tag=f"evolution-{date}",
)
```

---

## Evolution Log Format

Add this section to any `genius.md` that has been through evolution:

```markdown
## Evolution Log

> Tracks all evolution attempts — kept AND discarded.
> Each entry documents a hypothesis, result, and lesson.

### [Date] — [Description]
- **Hypothesis**: [What was tried]
- **Result**: [KEPT/DISCARDED] — [Score change]
- **Change**: [What was modified]
- **Lesson**: [What was learned]
```

---

## Safety Rails

1. **Never modify genius.md content** during evolution — only workflow files and the Evolution Log section
2. **Never test more than one hypothesis per cycle** — isolated variables only
3. **Always keep the variant file** until testing is complete — don't overwrite the current workflow before scoring
4. **Log every attempt** — even failures are data
5. **Human approval required** for workflow replacements — present the comparison, wait for confirmation
6. **Rollback plan**: Git history preserves every previous workflow version

---

## Regression Response

When `check_regression()` returns `is_regression: True`:

1. **Immediate**: Flag the skill in Performance Log (status = "Needs Improvement")
2. **Investigate**: Check git history — what changed since the last good score?
3. **If recent workflow edit caused it**: Revert the edit, re-score, confirm fix
4. **If no clear cause**: Run full benchmark to identify the degraded dimension
5. **Fix**: Generate a targeted variant addressing the specific regression
6. **Verify**: Confirm the fix by scoring 3 benchmark tasks

---

## Integration

- **Data source**: Performance Log (Notion DB `31f49875a89781dbb599dee5e7961b5c`)
- **Benchmark tool**: `execution/skill_benchmark.py`
- **Performance logger**: `execution/log_performance.py`
- **Quality Gate**: `directives/quality_gate.md` (scoring rubric)
- **Triggered by**: Feedback Ratchet regression detection, user request, or scheduled review
- **Feeds into**: Cross-Pollination Network (Phase 3) — kept improvements are candidates for transfer

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-09 |

**Update Rule**: When this protocol fires (evolution cycle completed), update the date and increment count.

---

*Created: 2026-03-10 | Phase 2 of Autoresearch Integration*
*Depends on: Phase 1 (Feedback Ratchet) — needs performance data to operate*
