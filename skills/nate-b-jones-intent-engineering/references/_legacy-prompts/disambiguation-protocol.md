# Disambiguation Protocol

Design when and how AI agents ask for clarification.

## Role

You create disambiguation trigger systems that fire appropriately—not too often, not too rarely.

## Required Input

- **[AGENT_CONTEXT]**: What the agent does
- **[ACTION_TYPES]**: Types of actions the agent takes
- **[RISK_TOLERANCE]**: How much uncertainty is acceptable

## Execution

1. **Map action consequences**: For each action type, what's the worst case?

2. **Design trigger conditions**:
   - Uncertainty threshold (how confident must agent be?)
   - Consequence severity (how bad if wrong?)
   - Reversibility (can it be undone?)

3. **Create clarification protocol**:
   - What to ask
   - How to phrase (not annoying)
   - When to proceed vs. wait

## Output

```markdown
# DISAMBIGUATION PROTOCOL

## Trigger Conditions

### Always Ask When:
- [High-stakes condition 1]
- [Multiple valid interpretations]
- [Confidence below X%]

### Never Ask When:
- [Trivial actions]
- [Highly reversible]
- [Clear precedent exists]

## Clarification Format

**Template**: "I understand you want [X]. Before I [action], can you confirm [specific ambiguity]?"

## Escalation Ladder
1. Quick clarification (1 question)
2. Full disambiguation (multiple questions)
3. Pause for human review
```
