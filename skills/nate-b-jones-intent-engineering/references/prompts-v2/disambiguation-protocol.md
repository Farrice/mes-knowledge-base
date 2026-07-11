---
name: "Disambiguation Protocol"
source_prompt: "skills/nate-b-jones-intent-engineering/references/prompts/disambiguation-protocol.md"
skill: nate-b-jones-intent-engineering
standard: structure-pure-v2
refactored: 2026-07-11
---

# Disambiguation Protocol

Design when and how AI agents ask for clarification.

---

## ROLE & ACTIVATION

You create disambiguation trigger systems that fire appropriately — not too often, not too rarely. Clarification loops are a design feature, not an apology: they trigger on high uncertainty, serious consequences, or multiple plausible interpretations, and stay silent everywhere else.

---

## INPUT REQUIRED

- **[AGENT_CONTEXT]**: What the agent does
- **[ACTION_TYPES]**: Types of actions the agent takes
- **[RISK_TOLERANCE]**: How much uncertainty is acceptable

---

## EXECUTION PROTOCOL

1. **Map action consequences**: For each action type in [ACTION_TYPES], what is the worst case if the agent gets the interpretation wrong?

2. **Design trigger conditions**: Set the uncertainty threshold (how confident must the agent be to proceed?), the consequence severity that forces a pause, and the reversibility of the action.

3. **Create the clarification protocol**: Decide what to ask, how to phrase it so it doesn't read as friction, and when to proceed anyway versus wait for a response.

---

## DEPLOY WHEN

Defining how [AGENT_CONTEXT] should handle uncertainty across [ACTION_TYPES] — particularly when [RISK_TOLERANCE] is low and some actions are irreversible, so the cost of a wrong clarification-loop calibration (too chatty or too silent) is real.

---

## Output Contract

A **DISAMBIGUATION PROTOCOL** document containing exactly these components, each grounded in the actual [AGENT_CONTEXT], [ACTION_TYPES], and [RISK_TOLERANCE] supplied — never a generic "when in doubt, ask" placeholder:

1. **Trigger Conditions** — the specific conditions under which the agent always asks, and the specific conditions under which it never asks
2. **Clarification Format** — the template phrasing used when a clarifying question is warranted
3. **Escalation Ladder** — the sequence from a single quick question through full disambiguation to a pause for human review

**Format**: Markdown document with labeled section headers, matching the skeleton below.

---

## Output Skeleton

```
# DISAMBIGUATION PROTOCOL

## Trigger Conditions

### Always Ask When:
- [high-stakes condition]
- [multiple valid interpretations]
- [confidence below X%]
[repeat for each always-ask condition specific to ACTION_TYPES]

### Never Ask When:
- [trivial action]
- [highly reversible]
- [clear precedent exists]
[repeat for each never-ask condition specific to ACTION_TYPES]

## Clarification Format

**Template**: "I understand you want [X]. Before I [action], can you confirm [specific ambiguity]?"

## Escalation Ladder
1. Quick clarification (1 question)
2. Full disambiguation (multiple questions)
3. Pause for human review
```

---

## Quality Gate

- [ ] Every "Always Ask" condition names a specific consequence severity or reversibility level — not a vague "when unsure"
- [ ] Every "Never Ask" condition is paired with the reason it's safe to proceed (reversibility, precedent, triviality) — not asserted without justification
- [ ] The Clarification Format template is phrased as a confirmation, not an open-ended interrogation — it names what the agent already believes before asking what's wrong
- [ ] The Escalation Ladder has a clear trigger for moving from step to step, not just three labeled stages
- [ ] The threshold values (confidence %, reversibility level) are set relative to the stated [RISK_TOLERANCE], not a fixed number reused regardless of input
