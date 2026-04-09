# Feedback Ratchet Protocol

> **Trigger**: After completing any significant output using an expert skill, agent persona, or workflow.
> **Inspired by**: Karpathy's autoresearch — constrained arena, objective metrics, ratcheting improvement.
> **Purpose**: Close the feedback loop so the system compounds skill rather than merely accumulating it.

---

## Core Principle

Every output is an experiment. Like autoresearch's 5-minute training runs, each output produces a measurable quality signal. Improvements ratchet upward. Regressions trigger review. The system can only get better or stay the same — never silently degrade.

---

## When to Log

Log a performance entry after ANY of these:

| Trigger | Task Type | Example |
|---------|-----------|---------|
| Workflow completion | Match the workflow domain | `/extract` → Extraction |
| Strategy brief delivered | Strategy | Competitive analysis, positioning |
| Content piece produced | Content | Social post, article, script |
| Research output delivered | Research | Market analysis, trend report |
| Client deliverable completed | Client Work | Proposal, audit, deck |
| System improvement made | System | New directive, workflow update |
| Creative asset generated | Creative | Copy, hooks, ads |

**Do NOT log**: Trivial questions, follow-ups, file operations, debugging, internal routing decisions.

---

## How to Log

### Automated (Preferred)

At the end of a workflow that produces a deliverable, run:

```python
from execution.log_performance import log_output

log_output(
    output="[Brief description of what was produced]",
    agent="[agent-name]",
    skill="[skill-directory-name]",
    workflow="[workflow-filename]",
    task_type="[Content|Strategy|Extraction|Research|Client Work|System|Creative|Analysis]",
    quality_score=[1-10],        # Your assessment
    intent_alignment=[1-10],     # From quality gate check 1
    expert_standard=[1-10],      # From quality gate check 2
    adversarial_resilience=[1-10], # From quality gate check 3
    status="[Keep|Discard|Needs Improvement|Baseline]",
    notes="[What worked, what didn't, what surprised you]",
)
```

### CLI

```bash
python execution/log_performance.py log "Strategy brief for SaaS" \
    --agent cardinal-mason \
    --skill cardinal-mason-ai-copywriting \
    --workflow 01-client-acquisition \
    --type Strategy \
    --quality 8 \
    --status Keep \
    --notes "Strong hook, weak CTA"
```

### Manual (User Rating)

When the user provides explicit feedback ("this is great" / "this missed the mark"), update the User Rating field on the most recent Performance Log entry.

---

## Scoring Guide

| Score | Meaning | Indicator |
|-------|---------|-----------|
| 9-10 | Exceptional | Would impress the actual expert. Publishable as-is. |
| 7-8 | Strong | Minor polish needed. Captures expert's thinking well. |
| 5-6 | Adequate | Gets the job done but lacks depth or nuance. |
| 3-4 | Weak | Misses key aspects. Generic rather than expert-grade. |
| 1-2 | Failed | Wrong direction, wrong audience, or fundamentally flawed. |

**The three sub-scores** (Intent Alignment, Expert Standard, Adversarial Resilience) map directly to the Quality Gate's 3-point check. Score each independently.

---

## The Ratchet Mechanism

### Regression Detection

After logging an output, automatically check for regression:

```python
from execution.log_performance import check_regression

result = check_regression(skill="[skill-name]", latest_score=[score])
# Returns: is_regression, baseline_avg, delta, message
```

**If regression detected** (score > 1.0 below rolling 10-output average):
1. Flag the output as "Needs Improvement"
2. Note what degraded (intent? expert standard? adversarial?)
3. Review the skill's recent changes — did a workflow update cause this?
4. If pattern persists across 3+ outputs → trigger skill evolution review (Phase 2)

### Improvement Detection

**If improvement detected** (score > 1.0 above rolling average):
1. Note what improved and why
2. Check if the improvement is transferable to related skills (Phase 3)
3. Update the skill's Evolution Log (Phase 2)

### Evolution Activation Reminder

After logging 5+ outputs in a session using expert skills, surface this prompt:

> **Evolution checkpoint**: You've shipped 5+ expert outputs this session. Consider running `/skill-evolution` on the most-used skill to close the improvement loop. Current priorities: `directives/evolution-direction.md`.

This is a reminder, not a gate — the human decides when to run evolution.

---

## Status Definitions

| Status | When to Use |
|--------|-------------|
| **Keep** | Output met or exceeded baseline quality. The approach works. |
| **Discard** | Output significantly below baseline. The approach should be abandoned. |
| **Needs Improvement** | Output is usable but below standard. Specific fixes identified. |
| **Baseline** | First output for this skill/workflow — establishes the starting point. |

---

## Baseline Queries

```bash
# Get rolling baseline for a skill
python execution/log_performance.py baseline --skill cardinal-mason-ai-copywriting

# Get rolling baseline for an agent across all skills
python execution/log_performance.py baseline --agent cardinal-mason

# Check if a score represents regression
python execution/log_performance.py check --skill cardinal-mason-ai-copywriting --score 5
```

---

## Integration with Quality Gate

The Feedback Ratchet and Quality Gate work together:

1. **Quality Gate** runs DURING output generation (silent 3-point check)
2. **Feedback Ratchet** runs AFTER delivery (captures the quality signal permanently)

The gate is the referee. The ratchet is the scoreboard. Together they create accountability.

---

## Notion Database

**Performance Log**: `31f49875a89781dbb599dee5e7961b5c`
- Script: `execution/log_performance.py`
- Properties: Output, Date, Agent, Skill, Workflow, Task Type, Quality Score, User Rating, Intent Alignment, Expert Standard, Adversarial Resilience, Status, Notes, Experiment Tag

---

## Ground Truth Calibration (Added 2026-04-03)

The feedback ratchet is self-referential (AI scoring AI) unless grounded against real expert output. Use the ground truth system to validate that quality scores reflect actual expert-level quality.

### When to Run Ground Truth Comparison

- After a skill evolution cycle produces a new variant
- When Expert Standard scores plateau at 7-8 but output feels generic
- Monthly, for the top 5 revenue-generating skills
- When a skill has 10+ consecutive "Keep" entries (possible score inflation)

### How to Run

```bash
# Check which domains have expert benchmarks
python execution/ground_truth.py gap-report

# Run blind comparison (AI output vs real expert)
python execution/ground_truth.py compare <domain> <path-to-ai-output>

# After scoring both outputs, reveal which was AI
python execution/ground_truth.py reveal <comparison-filename>
```

### Integration with Revenue Tracking

Quality scores without revenue data are incomplete. After client delivery:

```bash
python execution/revenue_tracker.py log "deliverable" --revenue <$> --outcome "what happened"
python execution/revenue_tracker.py pipeline  # See what needs tracking
```

### Prose Classifier Pre-Check

The prose classifier is now integrated into `chain_runner.py finalize()`. It automatically warns if:
- Banned AI vocabulary detected (delve, tapestry, landscape, etc.)
- Sentence rhythm is suspiciously uniform
- Expert Standard score may be inflated for AI-prose

Manual check: `python execution/prose_classifier.py check <file>`

---

## Workflow Integration Template

Add this step to any workflow that produces a deliverable. Copy-paste and fill in the brackets:

```markdown
### [N]. Performance Log
Log this output to the feedback ratchet (see `directives/feedback-ratchet.md`):

\```python
from execution.log_performance import log_output

log_output(
    output="[brief description of deliverable]",
    agent="[agent-name]",
    skill="[skill-directory-name]",
    workflow="[this-workflow-filename]",
    task_type="[Content|Strategy|Extraction|Research|Client Work|System|Creative|Analysis]",
    quality_score=[composite from quality gate],
    intent_alignment=[1-10],
    expert_standard=[1-10],
    adversarial_resilience=[1-10],
    status="Keep",
    notes="[what worked, what didn't]",
)
\```
```

**Already integrated**: `/extract` workflow (Step 9).

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-09 (chain_runner finalize for grace-andrews-media-company) |
| **Activation Count** | 101 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (performance logged after any output), update the "Last Activated" date and increment the count.

**Phase 2 Activation**: 20 entries needed. Currently at 76. **THRESHOLD MET** — Skill Evolution Engine is unlocked. Run `/skill-evolution` after significant shipping sessions. Read `directives/evolution-direction.md` for current priorities.

---

*Created: 2026-03-10 | Phase 1 of Autoresearch Integration*
