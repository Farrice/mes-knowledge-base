---
name: "Gap Identifier"
source_prompt: "skills/business-intelligence-audit/references/prompts/06-gap-identifier.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 06: Gap Identifier

> Find what's missing, broken, or underutilized.

---

## Purpose

This is the "opportunity finder"—systematically identify gaps that represent improvement opportunities.

---

## Input Required

- All previous audit data (Prompts 01-05)
- Or: Run standalone with fresh extraction

---

## Execution Protocol

```
You are identifying business gaps as a senior consultant preparing recommendations.

Based on all available data for [COMPANY], systematically identify gaps.

## Framework: MECE Gap Categories

Analyze gaps across six mutually exclusive, collectively exhaustive categories:

1. Product/Service Gaps — missing offering, adjacent problem, absent tier, absent entry point
2. Market/Audience Gaps — underserved segment, geographic expansion, adjacent audience, who competitors capture that they don't
3. Messaging/Positioning Gaps — uncommunicated value, missing proof, unclear differentiation, unaddressed objection
4. Channel/Distribution Gaps — untapped traffic source, missing partnership channel, absent platform, missing referral mechanism
5. Operations/Process Gaps — visible inefficiency, missing automation, customer experience gap, likely scaling bottleneck
6. Asset/Content Gaps — missing content type, missing lead magnet, untold case study, missing authority piece

Every gap identified must answer: why does this matter, what happens if it's not fixed, what's the upside of fixing it.
```

---

## Output Contract

- **Gap Summary Matrix:** every identified gap scored on Impact (1-10) and Effort (1-10), mapped to one of the six MECE categories
- **Priority Quadrant:** gaps sorted into Quick Wins / Strategic Priorities / Easy Extras / Avoid
- **Top 5 Gaps (Detailed):** each with What's Missing, Evidence, Impact if Fixed, How to Fix, Quick Win Version
- **The "Invisible Obvious":** at least one gap that's normalized/invisible to insiders
- **Comparison Check table:** client vs. top competitor on gap-relevant elements

---

## Output Skeleton

```
### Gap Summary Matrix

| Gap Category | Specific Gap | Evidence | Impact (1-10) | Effort (1-10) | Priority |
|---------------|--------------|----------|----------------|----------------|----------|
| [category] | [gap] | [evidence] | [score] | [score] | [quadrant] |

### Priority Quadrant

High Impact / Low Effort (QUICK WINS): [list]
High Impact / High Effort (STRATEGIC PRIORITIES): [list]
Low Impact / Low Effort (EASY EXTRAS): [list]
Low Impact / High Effort (AVOID): [list]

### Top 5 Gaps (Detailed)

#### Gap 1: [Name]
- What's Missing: [description]
- Evidence: [what was actually observed]
- Impact if Fixed: [realistic outcome]
- How to Fix: [specific approach]
- Quick Win Version: [smallest viable first step]

[repeat for Gaps 2-5]

### The "Invisible Obvious"
[the gap so normalized inside the business that it's become invisible — with the evidence that surfaced it]

### Comparison Check

| Element | [Company] | Top Competitor | Gap? |
|---------|-----------|-----------------|------|
| [element] | [value] | [value] | [yes/no] |
```

---

## Quality Gate

- [ ] Gap Summary Matrix covers gaps from all six MECE categories (or explicitly notes a category has none)
- [ ] No gap appears in more than one MECE category (mutual exclusivity check)
- [ ] Every Top-5 gap answers all three "So What" questions: why it matters, cost of inaction, upside of fixing
- [ ] Priority Quadrant placement matches the Impact/Effort scores in the matrix
- [ ] The "Invisible Obvious" gap is genuinely non-obvious, not a restatement of a Top-5 gap
