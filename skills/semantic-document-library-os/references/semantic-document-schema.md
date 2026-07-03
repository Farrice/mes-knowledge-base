# Semantic Document Schema

Use this schema for every agent-executable semantic document.

```markdown
# [Work Primitive Name]

## Purpose And Operating Definition
[Define the unit of work. Name the action behind the interface, not the button.]

## When To Use
- [Situation where this document governs action]

## When Not To Use
- [Situation where the agent must pause, refuse, or escalate]

## Inputs
| Input | Required | Source Of Truth | Notes |
|---|---|---|---|

## Outputs
| Output | Format | Destination | Owner |
|---|---|---|---|

## Objects And Meaning
| Object | What It Means | Why It Matters |
|---|---|---|

## Authority And Permissions
| Action | Agent May Do | Requires Approval | Never Do |
|---|---|---|---|

## Execution Protocol
1. Interpret the task and name the work primitive.
2. Confirm required inputs and source of truth.
3. Classify risk, reversibility, and authority tier.
4. Execute only the allowed action.
5. Validate the output against the quality tests.
6. Escalate if a disambiguation trigger fires.

## Decision Rules
| Condition | Rule | Reason |
|---|---|---|

## Examples
### Good Example
[Concrete example the agent should imitate.]

### Counterexample
[Concrete example the agent should reject or handle differently.]

## Quality Tests
| Test | Pass Criteria | Failure Response |
|---|---|---|

## Failure Modes
| Failure Mode | Early Signal | Prevention | Recovery |
|---|---|---|---|

## Maintenance Protocol
- Owner:
- Review cadence:
- Update triggers:
- Last updated:
```

## Minimum Standard

A semantic document is not complete unless it answers:

- What work is really being done?
- What objects are being touched?
- What does each action mean?
- Who owns the source of truth?
- What authority does the agent have?
- What could go wrong?
- How is success checked?
- When should the agent stop?
