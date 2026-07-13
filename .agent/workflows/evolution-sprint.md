---
description: Background skill improvement
---

# /evolution-sprint — Background Skill Improvement

Improve a skill while you work on something else. Fires 3 parallel agents (benchmark, analyze, scout), synthesizes an evolution hypothesis, and runs a blind test.

## Usage

```
/evolution-sprint <skill-name>
/evolution-sprint                  # auto-picks most-used skill from Performance Log
```

## When to Use

- `/maintenance` flagged a skill for evolution
- Monthly on top 3 revenue-generating skills
- After a regression is detected
- When you want the system improving while you do other work

## Steps

### 1. Identify Target Skill

If a skill name is provided, validate it exists in `skills/[skill-name]/`.

If no skill specified, pick the most-used skill from the Performance Log:

```bash
python execution/log_performance.py baseline
```

Scan for the skill with the most entries. Present the selection to the user before proceeding:

```markdown
**Auto-selected skill**: [skill-name] (X entries, avg Y.Y/10)
Proceeding unless you redirect me.
```

### 2. Fire 3 Parallel Agents

Launch all 3 as background tasks (`run_in_background: true`) so the user can continue working:

**Agent 1 — Benchmarker**:
```bash
python execution/skill_benchmark.py benchmark [skill-name]
```
Objective: Report current performance baseline, weakest workflow, weakest dimension (Intent / Expert / Adversarial).

**Agent 2 — Analyst**:
```bash
python execution/log_performance.py baseline
```
Query Performance Log for this skill specifically. Find:
- Average quality over last 10 outputs
- Trend: improving / stable / declining
- Weakest dimension consistently across entries
- Any regressions flagged (score drops > 1.0 below rolling average)

**Agent 3 — Scout**:
```bash
python execution/pattern_propagation.py related [skill-name]
```
Objective: Find transferable patterns from related skills that scored higher. Report which pattern families (persuasion, hooks, structure, voice, research, conversion, storytelling, positioning, systems) have cross-pollination candidates.

### 3. Synthesize Evolution Hypothesis

When all 3 agents return, combine their findings into a single hypothesis:

```markdown
## Evolution Hypothesis

**Skill**: [name]
**Current Avg Score**: [X.X/10] (trend: [improving/stable/declining])
**Weakest Dimension**: [Intent Alignment / Expert Standard / Adversarial Resilience] at [X.X/10]
**Weakest Workflow**: [workflow-name] at [X.X/10]
**Problem**: [Specific weakness — not "needs improvement" but what exactly is wrong]
**Transferable Pattern**: [Pattern from Scout agent — which skill, which pattern family, what it does]
**Proposed Change**: [Concrete modification to a specific workflow file]
**Blind Test Plan**: 3 benchmark tasks to compare baseline vs variant
```

### 4. CHECKPOINT: Present Hypothesis

Present the hypothesis to the user. Wait for approval before proceeding.

Options:
1. **Approve** — proceed to variant creation and blind test
2. **Modify** — adjust the hypothesis target or proposed change
3. **Abort** — discard and return to normal work

### 5. Create Variant Workflow

If approved, create a variant workflow file:

```
skills/[skill-name]/workflows/[workflow-name].variant.md
```

The variant must:
- Keep the same Output Contract as the original
- Keep the same genius.md reference
- Modify only the targeted aspect (the proposed change from Step 3)
- Document what changed at the top of the file in a `## Changes` section

### 6. Run Blind Test

Execute 3 benchmark tasks. For each task:

**A.** Execute the current (baseline) workflow and score the output using the Quality Gate 3-point check:
- Intent Alignment (1-10)
- Expert Standard (1-10)
- Adversarial Resilience (1-10)

**B.** Execute the variant workflow on the same task and score with the same rubric.

Record all scores.

### 7. Present Results

```markdown
## Evolution Sprint Results — [skill-name]

| Benchmark Task | Baseline | Variant | Delta |
|---------------|----------|---------|-------|
| Task 1 | [X]/10 | [Y]/10 | [+/-] |
| Task 2 | [X]/10 | [Y]/10 | [+/-] |
| Task 3 | [X]/10 | [Y]/10 | [+/-] |
| **Average** | **[X.X]** | **[Y.Y]** | **[+/-]** |

**Weakest Dimension Before**: [name] at [X.X/10]
**Weakest Dimension After**: [name] at [Y.Y/10]

**Verdict**: [KEEP / DISCARD]
**Reason**: [Why — reference specific task results]
```

### 8. Apply Result

**If KEEP:**
- Replace current workflow with variant content
- Delete the `.variant.md` file
- Add Evolution Log entry to `genius.md`
- Log to Performance Log:

```bash
python execution/chain_runner.py finalize "Evolution Sprint: [skill-name] — [hypothesis summary]" \
    --expert system \
    --skill [skill-name] \
    --workflow evolution-sprint \
    --type System \
    --intent 10 --expert-score [variant-avg] --adversarial 10 \
    --notes "Target: [dimension/workflow]. Delta: [+/-]. Pattern source: [related-skill]. KEPT."
```

**If DISCARD:**
- Delete the `.variant.md` file
- Add Evolution Log entry to `genius.md` (marked as discarded with reason)
- Log to Performance Log:

```bash
python execution/chain_runner.py finalize "Evolution Sprint: [skill-name] — DISCARDED" \
    --expert system \
    --skill [skill-name] \
    --workflow evolution-sprint \
    --type System \
    --intent 10 --expert-score [variant-avg] --adversarial 10 \
    --notes "Target: [dimension/workflow]. Delta: [+/-]. Hypothesis disproven: [reason]. DISCARDED."
```

### 9. Cross-Pollination Flag

If the variant was KEPT and the improvement is pattern-based (not skill-specific):

```bash
python execution/pattern_propagation.py related [skill-name]
```

Note any related skills that could benefit from the same pattern. Flag them for the next `/evolution-sprint` or `/maintenance` cycle.

## Protocol Reference

Benchmark tool: `execution/skill_benchmark.py`
Pattern propagation: `execution/pattern_propagation.py`
Performance logger: `execution/log_performance.py`
Full evolution protocol: `directives/skill-evolution-protocol.md`
Cross-pollination protocol: `directives/cross-pollination.md`

---

## Prompt Coherence Guard (2026-07-13 — spec: `directives/prompt-forging-spec.md`)

If the skill being modified has `references/prompts-v2/`, its execution prompts were forged FROM the workflow/genius material this run may have just changed. Before closing out: reconcile any prompt whose Execution Protocol no longer matches the evolved methodology (edit the v2 file, or re-forge it per spec), then re-run the wiring trio — `python3 execution/renaissance_audit.py` (0 fail) → `python3 execution/prompt_library.py build` → `python3 execution/wire_prompt_pointers.py --write`. An evolved skill with stale prompts silently desyncs the deterministic layer.
