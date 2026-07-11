---
name: "Recommendation Engine"
source_prompt: "skills/business-intelligence-audit/references/prompts/09-recommendation-engine.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 09: Recommendation Engine

> Generate prioritized, actionable recommendations.

---

## Purpose

Transform all analysis into a prioritized action plan the business can execute.

---

## Input Required

- All previous prompt outputs (especially Gap Identifier and SWOT)

---

## Execution Protocol

```
You are generating recommendations as a senior consultant preparing the final deliverable.

Based on all analysis for [COMPANY], create a prioritized recommendation set.

## Instructions

1. Review all gaps, opportunities, and weaknesses identified
2. Generate specific, actionable recommendations
3. Prioritize by impact and effort
4. Group into time horizons: This Week, 30 Days, 90 Days, 6-12 Months
```

---

## Output Contract

- **Executive Recommendation Summary:** "The One Thing" (single most important action) + Three Priorities, each with a "why now"
- **Four tiers of recommendations:** Quick Wins (this week), Short-Term (30 days), Medium-Term (90 days), Strategic (6-12 months) — each recommendation scored on Effort/Impact
- **Recommendation Details:** for every Tier 1-2 item — What, Why, How (step-by-step), Expected Outcome, Risk, Quick Start
- **Dependencies Map:** shows sequencing where one recommendation unlocks or requires another
- **Investment vs. Return:** $ investment, time investment, and expected return per recommendation — stated in realistic ranges the business could verify, never invented precision
- **What NOT To Do:** at least 3 items to stop, avoid, or not invest in, each with a reason

---

## Output Skeleton

```
### Executive Recommendation Summary

The One Thing:
> If they do nothing else, they should: [single most important action]

The Three Priorities:
1. [Priority 1] — [why now]
2. [Priority 2] — [why now]
3. [Priority 3] — [why now]

### Tier 1: Quick Wins (This Week)

| # | Recommendation | Effort | Impact | Owner |
|---|------------------|--------|--------|-------|
| 1 | [recommendation] | Low | [level] | [role] |

### Tier 2: Short-Term (30 Days)

| # | Recommendation | Effort | Impact | Dependency |
|---|------------------|--------|--------|-------------|
| 1 | [recommendation] | Medium | [level] | [dependency] |

### Tier 3: Medium-Term (90 Days)

| # | Recommendation | Effort | Impact | Resources Needed |
|---|------------------|--------|--------|---------------------|
| 1 | [recommendation] | High | [level] | [resources] |

### Tier 4: Strategic (6-12 Months)

| # | Recommendation | Why It Matters |
|---|------------------|-------------------|
| 1 | [recommendation] | [reason] |

### Recommendation Details

#### Recommendation: [Name]
- What: [specific action]
- Why: [gap/opportunity addressed]
- How: [step-by-step implementation]
- Expected Outcome: [measurable, realistic result]
- Risk: [what could go wrong]
- Quick Start: [first action to take today]

### Dependencies Map

[Recommendation A] → [Recommendation B] ← [Recommendation C] → [Recommendation D]

### Investment vs. Return Matrix

| Recommendation | $ Investment | Time Investment | Expected Return |
|------------------|----------------|--------------------|---------------------|
| [recommendation] | [realistic range] | [estimate] | [realistic, not invented] |

### What NOT To Do

1. [Stop doing X because...]
2. [Avoid pursuing Y because...]
3. [Don't invest in Z because...]
```

---

## Quality Gate

- [ ] "The One Thing" is a single, specific, executable action — not a category or theme
- [ ] Every Tier 1-2 recommendation has a full Recommendation Details entry (What/Why/How/Outcome/Risk/Quick Start)
- [ ] Dependencies Map reflects an actual sequencing logic, not a decorative diagram
- [ ] Investment vs. Return figures are stated as realistic ranges the client could verify, with zero invented precision numbers
- [ ] What NOT To Do has at least 3 items, each with a stated reason
