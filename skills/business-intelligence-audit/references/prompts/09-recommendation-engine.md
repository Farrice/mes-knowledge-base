# Prompt 09: Recommendation Engine

> Generate prioritized, actionable recommendations.

---

## Purpose

Transform all analysis into a prioritized action plan the business can execute.

---

## Input Required

- All previous prompt outputs (especially Gap Identifier and SWOT)

---

## Prompt

```
You are generating recommendations as a senior McKinsey consultant preparing the final deliverable.

Based on all analysis for [COMPANY], create a prioritized recommendation set.

## Instructions

1. Review all gaps, opportunities, and weaknesses identified
2. Generate specific, actionable recommendations
3. Prioritize by impact and effort
4. Group into time horizons

## Output Structure

### Executive Recommendation Summary

**The One Thing:**
> If they do nothing else, they should: [Single most important action]

**The Three Priorities:**
1. [Priority 1] — [Why now]
2. [Priority 2] — [Why now]
3. [Priority 3] — [Why now]

### Prioritized Recommendations

#### Tier 1: Quick Wins (This Week)
Low effort, immediate impact.

| # | Recommendation | Effort | Impact | Owner |
|---|----------------|--------|--------|-------|
| 1 | | Low | High | |
| 2 | | Low | Medium | |
| 3 | | Low | High | |

#### Tier 2: Short-Term (30 Days)
Moderate effort, significant impact.

| # | Recommendation | Effort | Impact | Dependency |
|---|----------------|--------|--------|------------|
| 1 | | Medium | High | |
| 2 | | Medium | High | |
| 3 | | Medium | Medium | |

#### Tier 3: Medium-Term (90 Days)
Requires planning and resources.

| # | Recommendation | Effort | Impact | Resources Needed |
|---|----------------|--------|--------|------------------|
| 1 | | High | High | |
| 2 | | High | High | |

#### Tier 4: Strategic (6-12 Months)
Foundational changes.

| # | Recommendation | Why It Matters |
|---|----------------|----------------|
| 1 | | |
| 2 | | |

### Recommendation Details

For each Tier 1-2 recommendation, provide:

#### Recommendation: [Name]
- **What:** Specific action to take
- **Why:** How this addresses identified gap/opportunity
- **How:** Step-by-step implementation
- **Expected Outcome:** Measurable result
- **Risk:** What could go wrong
- **Quick Start:** First action to take today

### Dependencies Map

```
[Recommendation A]
        ↓
[Recommendation B] ← [Recommendation C]
        ↓
[Recommendation D]
```

### Investment vs. Return Matrix

| Recommendation | $ Investment | Time Investment | Expected Return |
|----------------|--------------|-----------------|-----------------|
| | | | |

### What NOT To Do

Based on analysis, things they should STOP or AVOID:

1. [Stop doing X because...]
2. [Avoid pursuing Y because...]
3. [Don't invest in Z because...]
```

---

## Expected Output

An action plan that:
- Is immediately executable
- Prioritizes by realistic impact/effort
- Includes specific "how" for each recommendation
- Provides clear first steps

---

## Quality Standard

This should feel like a $5,000-$10,000 consulting recommendation document—specific, prioritized, actionable.
