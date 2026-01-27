---
description: Spin up an AI council for any decision with multi-perspective deliberation
---

# /council

Instantly create and run an AI council for any decision requiring multiple perspectives.

## Usage

```
/council [your decision or question]
```

## Examples

```
/council Should I raise my prices from $500 to $1,500?
/council Which of these three product ideas should I build first?
/council Is it time to hire my first employee?
```

## Steps

### 1. Capture the Decision

If no decision provided, ask:
- What decision are you facing?
- What are the stakes if you get it wrong?
- What options are you considering?

### 2. Generate Council Configuration

Read and apply: `skills/mark-kashef-ai-councils/references/prompts/council-commander.md`

Generate:
- 3-4 perspective agents with behavioral mandates
- Natural tensions between agents
- Specific questions each agent must answer

### 3. Run Deliberation

**Round 1: Initial Positions**
Each agent states their position and reasoning from their mandate.

**Round 2: Steelman**
Each agent articulates the strongest version of opposing arguments.

**Round 3: Crux Isolation**
- Where exactly do agents disagree?
- What evidence would change minds?
- Are disagreements resolvable?

### 4. Synthesize and Deliver

Output:
- Areas of genuine agreement
- Primary recommendation with confidence level
- Minority report (dissenting view and when it would be right)
- Decision checkpoints (when to revisit)

## Output Format

```markdown
# COUNCIL DECISION: [Topic]

## The Council
[Brief description of agents assembled]

## Deliberation Summary

### Points of Agreement
- [Point 1]
- [Point 2]

### Key Disagreement
[The core tension]

## Recommendation

**Action**: [What to do]
**Confidence**: [High/Medium/Low]
**Reasoning**: [Why]

## Minority Report
**Dissenting view**: [Position]
**They would be right if**: [Conditions]

## Decision Checkpoints
Revisit this decision if:
- [ ] [Condition 1]
- [ ] [Condition 2]
```

## Quick Modes

- `/council [decision]` - Full deliberation (default)
- `/council rapid [decision]` - Quick synthesis, skip steelman
- `/council devil [decision]` - Just two opposing views

## Notes

- Best for high-stakes decisions where being wrong is costly
- Overkill for simple yes/no questions with obvious answers
- The value is in surfacing perspectives you'd otherwise miss
