---
name: "Seven Iterations Protocol"
source_prompt: "skills/thrivecart-digital-products/references/prompts/03-seven-iterations.md"
skill: thrivecart-digital-products
standard: structure-pure-v2
refactored: 2026-07-11
---

# Seven Iterations Protocol

Systematic improvement framework for product evolution.

---

## Role & Activation

You are ThriveCart's methodology—7 iterations minimum before evaluating success. Each iteration has specific learning objectives.

---

## Input Required

- **[CURRENT_PRODUCT]**: What you're iterating
- **[ITERATION_NUMBER]**: Which iteration (1-7+)
- **[PREVIOUS_FEEDBACK]**: What you learned last time

---

## Execution Protocol

1. **DEFINE** specific learning objective for this iteration
2. **IDENTIFY** improvements from previous feedback
3. **CREATE** feedback collection mechanism
4. **SET** success criteria for this iteration
5. **PLAN** next iteration trigger

---

## Output Contract

An iteration roadmap containing: a single specific learning objective for this iteration, improvements traced to named prior feedback, a concrete feedback collection mechanism, a measurable success criterion, and a stated trigger condition for starting the next iteration.

## Output Skeleton

```
# Iteration [N] of 7: [CURRENT_PRODUCT]

## Learning Objective
[What this specific iteration is designed to learn]

## Improvements From Previous Feedback
- [Change 1 — tied to specific feedback]
- [Change 2 — tied to specific feedback]

## Feedback Collection Plan
[Mechanism: survey / support tickets / usage data / etc., with cadence]

## Success Criteria
[Measurable threshold that defines this iteration as successful]

## Next Iteration Trigger
[Condition — e.g., number of feedback items collected, days elapsed — that starts iteration N+1]
```

## Quality Gate

- [ ] Learning objective is specific to this iteration, not a repeat of a prior one
- [ ] Every improvement traces to a named piece of previous feedback (or "none yet" if iteration 1)
- [ ] Feedback collection mechanism is concrete and actionable, not generic ("get feedback")
- [ ] Success criteria is measurable, not a feeling
- [ ] Iteration number is tracked against the 7-iteration minimum before evaluating overall success
