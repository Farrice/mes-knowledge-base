# Feedback Ratchet Protocol

> **Trigger**: After any significant expert-driven deliverable.
> **Purpose**: Close the feedback loop so skills compound, not merely accumulate.

---

## Core Principle

Every output is an experiment. Improvements ratchet upward. Regressions trigger review. The system can only get better or stay the same — never silently degrade.

---

## When to Log

Log after: workflow completion, strategy brief, content piece, research output, client deliverable, system improvement, creative asset.
**Do NOT log**: Trivial questions, follow-ups, file ops, debugging, routing decisions.

---

## How to Log

### Automated (Preferred)

```python
from execution.log_performance import log_output

log_output(
    output="[description]", agent="[agent]", skill="[skill]",
    workflow="[workflow]", task_type="[Content|Strategy|Extraction|Research|Client Work|System|Creative|Analysis]",
    quality_score=[1-10], intent_alignment=[1-10],
    expert_standard=[1-10], adversarial_resilience=[1-10],
    status="[Keep|Discard|Needs Improvement|Baseline]",
    notes="[what worked/didn't]",
)
```

### CLI

```bash
python execution/log_performance.py log "Brief description" --agent X --skill X --type X --quality 8 --status Keep --notes "Notes"
```

Manual: When user gives feedback, update User Rating on the most recent entry.

---

## Scoring: 9-10 Exceptional (publishable) | 7-8 Strong (minor polish) | 5-6 Adequate | 3-4 Weak (generic) | 1-2 Failed

Sub-scores (Intent Alignment, Expert Standard, Adversarial Resilience) map to Quality Gate's 3-point check.

---

## Ratchet Mechanism

**Regression** (score >1.0 below rolling 10-output avg): Flag "Needs Improvement", note degraded dimension, review recent skill changes. 3+ pattern → trigger `/skill-evolution`.

**Improvement** (score >1.0 above avg): Note cause, check transferability, update Evolution Log.

**Evolution Reminder**: After 5+ expert outputs in a session → surface `/skill-evolution` prompt. Reminder, not gate.

---

## Status: Keep (met baseline) | Discard (abandon approach) | Needs Improvement (fixable) | Baseline (first output, establishes starting point)

## Baselines

```bash
python execution/log_performance.py baseline --skill [name]
python execution/log_performance.py baseline --agent [name]
python execution/log_performance.py check --skill [name] --score 5
```

---

## Quality Gate Integration

Quality Gate runs DURING output (silent 3-point check). Feedback Ratchet runs AFTER delivery (captures signal permanently). Gate = referee. Ratchet = scoreboard.

## Notion DB: `31f49875a89781dbb599dee5e7961b5c` | Script: `execution/log_performance.py`

---

## Ground Truth Calibration

Run ground truth comparison when: skill evolution produces new variant, Expert Standard plateaus at 7-8, monthly for top 5 revenue skills, 10+ consecutive "Keep" entries.

```bash
python execution/ground_truth.py gap-report
python execution/ground_truth.py compare <domain> <path-to-ai-output>
python execution/ground_truth.py reveal <comparison-filename>
```

Revenue tracking: `python execution/revenue_tracker.py log "deliverable" --revenue <$> --outcome "what happened"`

Prose classifier integrated into `chain_runner.py finalize()` — auto-warns on banned AI vocab, uniform rhythm, inflated Expert Standard. Manual: `python execution/prose_classifier.py check <file>`

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-04-12 |
| **Activation Count** | 130 |

**Phase 2**: ✅ ACTIVATED (2026-03-30, 123 entries). Run `/skill-evolution` after shipping sessions.
**Phase 3**: ✅ ACTIVATED (2026-03-30). Cross-pollinated adversarial resilience to 5 skills.
**Phase 4**: 🔒 LOCKED. Requires 3+ recurring gaps in `.agent/gap-log.md`.

*Created: 2026-03-10 | Compressed: 2026-04-13*
