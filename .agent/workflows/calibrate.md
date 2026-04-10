---
description: Full calibration check
---

# /calibrate — System Calibration Scorecard

Honest assessment of how good the system actually is. Fires 3 parallel agents (ground truth, prose quality, revenue attribution), synthesizes a scorecard, and recommends actions. No sugarcoating.

## Usage

```
/calibrate
```

## When to Use

- Monthly (1st of month ritual)
- When you feel like the system might be coasting
- Before starting a major client project (verify quality baseline)
- After any system upgrade (verify nothing broke)

## Steps

### 1. Fire 3 Parallel Agents

Launch all 3 simultaneously:

**Agent 1 — Ground Truth**:

Check expert benchmark coverage:
```bash
python execution/ground_truth.py gap-report
```

If the copywriting domain has 3+ samples, pick a random recent deliverable from that domain and run a blind comparison:
```bash
python execution/ground_truth.py compare copywriting [deliverable-path]
```

Report:
- How many domains have benchmarks
- Total blind comparisons run to date
- Last comparison result (AI won / Expert won / Tie)
- Any domains with zero benchmark coverage

**Agent 2 — Prose Scanner**:

Find the 5 most recent deliverables in `deliverables/` directory (by modification date). For each one:
```bash
python execution/prose_classifier.py check [file]
```

Report:
- How many CLEAN, WARNING, FLAGGED out of 5
- Overall AI-prose detection rate
- Which files were flagged and why (specific patterns detected)

**Agent 3 — Revenue Check**:

Pull ROI data:
```bash
python execution/revenue_tracker.py report
```

Then check the pipeline for outcome tracking gaps:
```bash
python execution/revenue_tracker.py pipeline
```

Report:
- Total outcomes logged
- Total revenue tracked
- Deliverables awaiting outcome tracking
- Top ROI skill (name + dollar amount)

### 2. Gather System Health Metrics

While waiting for the 3 agents, pull supplementary data:

```bash
python execution/log_performance.py baseline
```

From this, extract:
- Total Performance Log entries
- Number of skill evolution cycles completed (search for `evolution` tags)
- Number of cross-pollination events logged

### 3. Synthesize Calibration Scorecard

Combine all findings into a single scorecard:

```
CALIBRATION SCORECARD — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GROUND TRUTH
  Domains with benchmarks: X/7
  Blind comparisons run: X total
  Last comparison result: [AI won / Expert won / Tie]

PROSE QUALITY
  Last 5 deliverables: X CLEAN, X WARNING, X FLAGGED
  Overall AI-prose rate: X%

REVENUE ATTRIBUTION
  Total outcomes logged: X
  Total revenue tracked: $X
  Deliverables awaiting outcomes: X
  Top ROI skill: [name] ($X)

SYSTEM HEALTH
  Performance Log entries: X
  Skill evolution cycles run: X
  Cross-pollination events: X

HONEST ASSESSMENT
  [1-3 sentences: what's actually working, what's not, what to do next.
   No hedging. No "the system is solid but could improve." 
   Name the weakest link. Name the strongest. State the gap.]
```

### 4. Present Scorecard

Deliver the scorecard as-is. Do not soften findings. If the system is coasting, say so. If prose quality is slipping, say so. If revenue attribution is sparse, say so.

### 5. Recommend Top 3 Actions

Based on scorecard findings, recommend exactly 3 prioritized actions:

| Priority | Finding | Action | Command |
|----------|---------|--------|---------|
| 1 | [Weakest finding] | [What to do] | [Specific command or workflow] |
| 2 | [Second weakest] | [What to do] | [Specific command or workflow] |
| 3 | [Third weakest] | [What to do] | [Specific command or workflow] |

Examples of actions:
- Ground truth gaps -> `/extract` for uncovered domains
- Prose flagged -> Review flagged files, rewrite AI-sounding sections
- Revenue tracking gaps -> Run `python execution/revenue_tracker.py log` for untracked deliverables
- Evolution stagnation -> `/evolution-sprint` on weakest skill
- Low Performance Log entries -> Enforce chain finalization on all expert output

### 6. Log the Calibration

```bash
python execution/chain_runner.py finalize "Calibration Scorecard — [Date]" \
    --expert system \
    --skill system \
    --workflow calibrate \
    --type System \
    --intent 10 --expert-score [overall-health-1-10] --adversarial 10 \
    --notes "Ground Truth: X/7 domains. Prose: X/5 clean. Revenue: $X tracked. Actions: [top 3 summary]"
```

## Protocol Reference

Ground truth engine: `execution/ground_truth.py`
Prose classifier: `execution/prose_classifier.py`
Revenue tracker: `execution/revenue_tracker.py`
Performance logger: `execution/log_performance.py`
Chain finalization: `execution/chain_runner.py`
