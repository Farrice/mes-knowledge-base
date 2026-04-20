---
description: Define the editable surface, metric, and time budget for an auto-improvement project. The gate — no loop starts without a clear triplet.
---

# Karpathy Triplet Design

> Load `genius.md` first. This is the first workflow. If the triplet is fuzzy, every downstream workflow fails.

## Pre-Flight Gate (from genius.md)

> "The magic isn't in the agent's intelligence — it's in the constraints."

Three components, each statable in ONE sentence. If any is fuzzy, you don't have a project — you have a foundation task.

## When to Use

- Evaluating a candidate system for auto-improvement
- Before any readiness audit (WF 02), architecture design (WF 03), or deployment plan (WF 07)
- When a team says "we want to use AI to optimize X" — start here

## Skill Acquisition

Load: `genius.md` (GP-1, GP-13, GP-14, HK-6, SM-1), `references/karpathy-loop-quotes.md` (Constraint Mechanism section)

## Input Required

- A candidate system to auto-improve (pricing engine, fraud model, content pipeline, agent harness, etc.)
- Current state: how is this system optimized today (human ops, periodic review, etc.)?
- Business value: what does "better" mean to the organization?

## Execution

### Phase 1 — Editable Surface Identification

**Question to answer**: What is the ONE file (or minimal file set) the agent can modify?

Test:
- Can you point at a single file path?
- Can the agent read its entire context in one pass?
- Do changes to it have observable effects on the metric?

If the answer spans multiple files, multiple systems, or configuration scattered across repos → **the editable surface is not yet defined**. That's your first project: consolidate the surface.

Produce:
- File path(s) that can be edited
- Justification: why this surface, not a broader one
- Out-of-scope list: what the agent CANNOT touch

### Phase 2 — Metric Definition

**Question to answer**: What is the ONE scorable number that measures success?

Required properties:
1. **Objectively testable** — no human judgment required to compute
2. **Business-value correlated** — does going up on this metric mean the business wins? (If unsure, it's a proxy — flag as risk per GP-13)
3. **Bounded evaluation time** — can be computed within the time budget (Phase 3)
4. **Revert-safe** — can the metric be restored if a change degrades it?

Produce:
- Metric name + formula
- Evaluation method (automated test, eval suite, external API call, etc.)
- Business-value correlation evidence (or explicit "proxy, not primary" flag)
- Baseline value (current state)

### Phase 3 — Time Budget Setting

**Question to answer**: How long can ONE experiment run?

Considerations:
- Karpathy's original: 5-minute training experiment
- Auto-agent: benchmark suite (longer per run, fewer iterations)
- Business systems: typically 5-30 minutes per experiment

Target: **iteration rate > 10 experiments per hour** (minimum 100 overnight).

Produce:
- Time budget per experiment (in minutes)
- Expected overnight throughput (experiments per 8-hour window)
- Compute cost per experiment (informs overnight budget)

### Phase 4 — Fuzziness Audit

For each of the three components, score 0-10:

| Dimension | 0-4 (Fuzzy) | 5-7 (Adequate) | 8-10 (Sharp) |
|-----------|-------------|----------------|--------------|
| Editable Surface | Multiple files across systems | Single file with some adjacent dependencies | One file, self-contained |
| Metric | Qualitative or human-judged | Quantitative but uncertain business link | Quantitative + validated business link |
| Time Budget | Undefined or >1 hour | Defined but untested | Tested, reproducible, <30 min |

**Gate**: min score 7 on each dimension. Below → fix before proceeding.

### Phase 5 — Triplet Specification Document

Produce the single-page triplet specification:

```markdown
# Auto-Improvement Triplet — [System Name]

## Editable Surface
Path: [file path]
Justification: [why this, not broader]
Out-of-scope: [what agent cannot touch]

## Metric
Name: [metric name]
Formula: [how computed]
Evaluation: [method]
Business-value correlation: [evidence OR proxy flag]
Baseline: [current value]

## Time Budget
Per experiment: [N minutes]
Overnight throughput: [N experiments / 8hr]
Compute cost: [$ per experiment]

## Fuzziness Scores
Editable Surface: [0-10]
Metric: [0-10]
Time Budget: [0-10]

## Gate Decision
[PROCEED to WF 02 — Readiness Audit] OR [FIX FIRST: <specific gap>]
```

## Content Type Adaptations

| Target Type | Editable Surface Example | Metric Example | Time Budget Example |
|-------------|-------------------------|----------------|---------------------|
| Agent harness | `system-prompt.md` | SpreadsheetBench score | 10 min/run |
| Pricing engine | `pricing-rules.yaml` | Revenue per customer | 15 min/run |
| Fraud model | `detection-thresholds.json` | Precision × Recall | 20 min/run |
| Content pipeline workflow | `workflow.md` | Composite quality score | 10 min/run |
| Email sequence | `sequence.md` | Conversion rate on held-out | 30 min/run |
| Code-generation skill | `skill.md` | Test pass rate | 5 min/run |

## Output Requirements

- One-page Triplet Specification Document
- Fuzziness scores with justification
- Gate decision (PROCEED or FIX-FIRST)
- If FIX-FIRST: specific foundation task to complete before re-attempting

## Quality Gate (from genius.md rubric)

- **Triplet Clarity** (0-10): all three components statable in one sentence
- **Judgment Leverage** (0-10): can a human write a program.md on top of this triplet?
- **Revert Capability** (0-10): can any change to the editable surface be cleanly reverted?

Minimum: 7 on each. Composite: 7.0 avg, no dim below 6.

## Anti-Patterns (from genius.md)

- ❌ Editable surface = "whatever the agent thinks is relevant"
- ❌ Metric = activity count (messages sent, experiments run) instead of outcome
- ❌ Time budget = "until it finishes"
- ❌ Skipping the fuzziness audit because "it feels clear enough"
- ❌ Treating business-value correlation as obvious without evidence

## Hand-off

Once triplet is APPROVED → proceed to `/nate-auto-audit` (WF 02) for readiness assessment.
