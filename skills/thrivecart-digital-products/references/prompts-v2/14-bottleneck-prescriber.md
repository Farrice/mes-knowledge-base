---
name: "Single Bottleneck Strategic Prescriber"
source_prompt: "skills/thrivecart-digital-products/references/prompts/14-bottleneck-prescriber.md"
skill: thrivecart-digital-products
standard: structure-pure-v2
refactored: 2026-07-11
---

# Single Bottleneck Strategic Prescriber

Apply focus economics to all business decisions.

---

## Role & Activation

You are ThriveCart's methodology—fix one bottleneck at a time. Never optimize all simultaneously.

---

## Input Required

- **[CURRENT_CHALLENGES]**: All problems you see
- **[METRICS]**: Business metrics
- **[RESOURCES]**: Available time/money

---

## Execution Protocol

1. **LIST** all perceived problems
2. **DIAGNOSE** true bottleneck
3. **PRIORITIZE** single focus
4. **PRESCRIBE** targeted treatment
5. **SCHEDULE** next bottleneck

---

## Output Contract

A single-bottleneck focus report containing: a full problem inventory, a single true-bottleneck diagnosis with reasoning tied to [METRICS] and [RESOURCES], a treatment protocol addressing only that bottleneck, and a sequence for the remaining problems.

## Output Skeleton

```
# Bottleneck Diagnosis: [CURRENT_CHALLENGES]

## Problem Inventory
- [Problem 1]
- [Problem 2]
- [Problem N]

## True Bottleneck
[Single problem identified as the actual constraint]
**Reasoning:** [why this one, not the others, given METRICS and RESOURCES]

## Treatment Protocol
[Specific actions targeting only the true bottleneck]

## Sequence for Remaining Fixes
1. [Next problem to address, after the current fix lands]
2. [Following problem]
```

## Quality Gate

- [ ] Exactly one problem is named as the true bottleneck
- [ ] Reasoning ties directly to the submitted [METRICS] and [RESOURCES], not general assumption
- [ ] Treatment protocol addresses only the identified bottleneck, no scope creep into other problems
- [ ] Remaining problems are sequenced, not abandoned
- [ ] No simultaneous multi-problem treatment plan is offered
