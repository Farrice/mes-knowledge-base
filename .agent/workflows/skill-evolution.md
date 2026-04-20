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

### 5. Git Checkpoint (Karpathy Ratchet)

Before generating the variant, create a checkpoint so the ratchet can auto-revert on failure:

```bash
# Save current state as a checkpoint tag
git stash push -m "evolution-checkpoint-[skill-name]-$(date +%Y%m%d)" -- skills/[skill-name]/
# Immediately unstash to keep working (the stash is the checkpoint)
git stash pop
```

Or if the workflow file is already committed:
```bash
# Record the current commit hash as the revert target
CHECKPOINT=$(git rev-parse HEAD)
echo "Checkpoint: $CHECKPOINT"
```

This enables automatic revert if the variant is DISCARDED — the ratchet can only move forward.

### 6. Generate Variant

Create a variant workflow file:

```
skills/[skill-name]/workflows/[workflow-name].variant.md
```

The variant must:
- Keep the same Output Contract
- Keep the same genius.md reference
- Modify ONLY ONE targeted aspect (single variable — Karpathy constraint)
- Document what changed at the top

### 7. Test Both Versions (Time-Boxed: 10 min/task)

**Time limit: 10 minutes per benchmark task.** This prevents over-deliberation and forces decisive evaluation (Karpathy principle: constrained cycle time).

For each of the 3 **SEEN** benchmark tasks (from `skill_benchmark.py` `BENCHMARK_TASKS[domain]['seen']`):

**A.** Execute the current workflow → score output (Quality Gate 3-point check) — 10 min max
**B.** Execute the variant workflow → score output (same rubric) — 10 min max

Record all scores. Scoring must be blind (score current first, then variant, without comparing).

**Then run the HELD-OUT check (v3 — Nate GP-12 Metric Gaming Detection):**

```python
from execution.skill_benchmark import select_held_out_task, compute_gaming_delta

# Determine cycle number (use git commit count on the skill dir as simple rotation index)
# Or track in .agent/evolution-cycle-counter.json if you want stateful rotation

held_out_task = select_held_out_task(domain, cycle_number)
```

**C.** Execute the variant workflow on the HELD-OUT task → score output (same rubric) — 10 min max

This task was NOT shown to the meta-agent during variant generation. If variant scores dramatically lower here than on seen tasks, it's gaming the rubric.

```python
gaming_check = compute_gaming_delta(
    seen_scores=[variant_seen_score_1, variant_seen_score_2, variant_seen_score_3],
    held_out_score=variant_held_out_score,
)

# gaming_check = {'delta': X.X, 'flag': bool, 'seen_avg': X.X}
```

**If `gaming_check['flag'] is True` (delta > 1.5)**: auto-DISCARD the variant regardless of seen-task scores. Log failure signal: `{"step": "held_out", "signal_type": "gaming", "severity": "blocker", "description": f"seen_avg {seen_avg} vs held_out {held_out_score}, delta {delta}"}`. This variant was optimizing the wrong thing.

### 8. Compare Results (Binary Decision)

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

### 9. CHECKPOINT: User Approval

Present the comparison. If the variant wins:
- Show the specific changes made
- Ask for permission to replace the current workflow

If the variant loses or ties:
- Recommend discarding
- Note what was learned

### 10. Apply Result (Ratchet Forward or Revert)

**If KEPT (ratchet forward):**
- Replace current workflow with variant content
- Delete the .variant.md file
- Add Evolution Log entry to genius.md
- Log to Performance Log (status: "Keep", experiment_tag: "evolution-[date]")
- **Log v3 reasoning trace (Nate GP-6 — Traces Over Scores):**
  ```bash
  python3 execution/evolution_tracer.py log \
    --component "skills/[skill-name]/workflows/[workflow-name].md" \
    --operation "evolution_cycle_kept" \
    --expert "[expert-name]" \
    --workflow "[workflow-name]" \
    --quality-score [variant_avg] \
    --intent [X] --expert-score [Y] --adversarial [Z] --factual [W] \
    --hypothesis "[what was tested, one sentence]" \
    --variant-diff "[what changed, summary — or git diff -U0 output]" \
    --reasoning-chain '[{"step":1,"thought":"...","decision":"...","alternatives_considered":["..."]}]' \
    --benchmark-tasks "[task-1,task-2,task-3]" \
    --notes "KEPT. Target: [target]. Delta: +[delta]."
  ```
- **Git commit the change (ratchet moves forward):**
  ```bash
  git add skills/[skill-name]/workflows/[workflow-name].md
  git add skills/[skill-name]/genius.md
  git commit -m "evolution: [skill-name] — [hypothesis-summary]
  
  Result: KEPT — Score improved from [X] to [Y] (+[delta])
  Hypothesis: [what was tested]
  Target: [workflow or dimension]"
  ```

**If DISCARDED (ratchet reverts):**
- **Auto-revert**: `git checkout -- skills/[skill-name]/workflows/[workflow-name].md` (restore from checkpoint)
- Delete the .variant.md file
- Add Evolution Log entry to genius.md (marked as discarded, with lesson learned)
- Log to Performance Log (status: "Discard", experiment_tag: "evolution-[date]")
- **Log v3 reasoning trace with failure signals (Nate GP-6) — critical for diagnosis:**
  ```bash
  python3 execution/evolution_tracer.py log \
    --component "skills/[skill-name]/workflows/[workflow-name].md" \
    --operation "evolution_cycle_discarded" \
    --expert "[expert-name]" \
    --workflow "[workflow-name]" \
    --quality-score [variant_avg] \
    --intent [X] --expert-score [Y] --adversarial [Z] --factual [W] \
    --hypothesis "[what was tested]" \
    --variant-diff "[what changed]" \
    --failure-signals '[{"step":N,"signal_type":"[type]","severity":"[minor|major|blocker]","description":"[where direction was lost]"}]' \
    --notes "DISCARDED. Lesson: [what was learned]."
  ```
  **Why this matters**: discarded traces with failure signals are the fuel for future evolution cycles. Score-only logging of a discard teaches nothing. Reasoning-chain logging teaches the pattern to avoid.

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

### 11. Cross-Pollination Check

If the variant was KEPT and the improvement is pattern-based (not skill-specific):

```python
from execution.pattern_propagation import find_related_skills

candidates = find_related_skills(skill_name, pattern_type)
```

If candidates found, note them for the next cross-pollination cycle.

### 11b. Wiki Cascade + Pattern Archive (Karpathy Ingest)

After applying result, feed back into the knowledge wiki:

```bash
# Log the evolution event
python3 execution/knowledge_compiler.py log evolve "[skill_name] — [KEPT/DISCARDED]" --domain [domain] --expert [expert] --notes "delta:[score_delta] hypothesis:[hypothesis_summary]"

# If KEPT: regenerate briefing so future sessions know about the improvement
python3 execution/knowledge_compiler.py briefing
```

**If KEPT and score improvement >= 1.0**: Write the evolved pattern to `knowledge/patterns/`:

Create `knowledge/patterns/evolved-[skill-name]-[date].md`:
```markdown
---
type: evolved-pattern
skill: [skill-name]
date: [YYYY-MM-DD]
delta: [+X.X]
---

# [Skill Name] — [Hypothesis Summary]

## What Changed
[Describe the specific modification that improved the output]

## Why It Worked
[Analysis of why this change improved the target dimension]

## Transferability
[Could this pattern help other skills? Which ones?]
```

**If DISCARDED**: Append the lesson to `knowledge/patterns/discarded-lessons.md`:
```
- [YYYY-MM-DD] [skill-name]: [hypothesis] → DISCARDED because [reason]
```

This ensures evolution discoveries compound in the wiki — both successes AND failures inform future cycles.

### 12. Update Evolution Direction

Update `directives/evolution-direction.md`:
- Add row to **Evolution History** table with date, skill, hypothesis, result, score delta, notes
- Update **System Status** table (increment activation count, update last activated date)
- If 3 consecutive DISCARDs on same skill, note in Stopping Criteria that skill should be paused

### 13. Report

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
