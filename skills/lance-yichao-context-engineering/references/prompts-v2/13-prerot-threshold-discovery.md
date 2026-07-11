---
name: "LANCE MARTIN & PEAK JI - PRE-ROT THRESHOLD DISCOVERY PROTOCOL"
source_prompt: "skills/lance-yichao-context-engineering/references/prompts/13-prerot-threshold-discovery.md"
skill: lance-yichao-context-engineering
standard: structure-pure-v2
refactored: 2026-07-11
---

# LANCE MARTIN & PEAK JI — PRE-ROT THRESHOLD DISCOVERY PROTOCOL
## Crown Jewel Practitioner Prompt #13

---

## ROLE & ACTIVATION

You are a Context Threshold Analyst discovering the actual working context limit for your specific model and task. You understand that the stated context limit is not the usable limit—performance degrades well before the maximum.

The "128K–200K" zone is a starting point, but YOUR threshold must be discovered through evaluation, not assumed.

---

## INPUT REQUIRED

- **[MODEL]**: Which model to evaluate
- **[TASK TYPE]**: Representative tasks to test
- **[QUALITY METRICS]**: How to measure output quality
- **[CONTEXT INCREMENTS]**: Step size for testing

---

## EXECUTION PROTOCOL

1. **Establish Baseline**: Quality at minimal context
2. **Design Test Suite**: Tasks with verifiable quality metrics
3. **Increment Context**: Add context in measured steps
4. **Measure Quality**: Track metrics at each increment
5. **Plot Degradation Curve**: Visualize quality vs. context
6. **Identify Inflection Point**: Where quality drops >10%

---

## Output Contract

A **Pre-Rot Threshold Report** containing:

- **Baseline Quality**: Performance at minimal context
- **Degradation Data**: Quality at each context level
- **Threshold Identification**: The actual working limit
- **Confidence Interval**: Reliability of threshold
- **Task-Specific Variations**: If threshold differs by task
- **Recommendations**: Safe operating ceiling (with buffer)

**Format**: Evaluation report with a data table (context level → quality metric) plus a stated threshold and operating recommendation
**Length**: Scaled to the number of context increments actually tested
**Quality Standard**: Every number in the report is a placeholder for a measured value from the test suite — the report structure must not be filled with assumed or invented figures

---

## Output Skeleton

```
BASELINE QUALITY
Context level: [minimal context size tested]
Quality metric result: [measured value — from actual test run, not assumed]
Task(s) used for baseline: [from TASK TYPE input]

DEGRADATION DATA
| Context level | Quality metric | Delta vs. baseline |
|---|---|---|
| [level 1] | [measured] | [—] |
| [level 2] | [measured] | [delta] |
| [level N] | [measured] | [delta] |

DEGRADATION CURVE (description)
[Describe the shape of the curve from the table above — flat, gradual decline, cliff — do not invent numbers not in the table]

THRESHOLD IDENTIFICATION
Inflection point: [context level where quality first drops more than the stated threshold, e.g. >10%]
Basis: [which row(s) in the degradation data support this]

CONFIDENCE INTERVAL
[How reliable this threshold is, given sample size / test suite coverage — flag low confidence if the test suite is thin]

TASK-SPECIFIC VARIATIONS
- Task type: [name] — Threshold: [if different from the general threshold]
- [repeat if variation exists; state "none observed" if not]

RECOMMENDATIONS
Safe operating ceiling: [inflection point minus stated buffer]
Buffer rationale: [why this buffer size]
```

---

## Deploy When

Given [MODEL], [TASK TYPE], [QUALITY METRICS], and [CONTEXT INCREMENTS], produce the full Pre-Rot Threshold Report above — output should reflect an actual test run's results, never an assumed degradation curve.

---

## Quality Gate

- [ ] Degradation data table has one row per tested context increment, not a smoothed or invented series
- [ ] Threshold Identification cites specific rows from the degradation data as evidence
- [ ] No fixed percentage (e.g. a specific "128K" or "200K" figure) is presented as universal — it is explicitly framed as this model/task's discovered result
- [ ] Confidence interval honestly reflects test suite size — flags low confidence when the increments tested are few
- [ ] Recommendation includes an explicit buffer and states the reasoning for the buffer size
