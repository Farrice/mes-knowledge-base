# Semantic Document Validation Rubric

## Cold-Start Execution Test

Give an agent only the semantic document and a realistic task. It passes if the agent can:

- identify the work primitive
- ask only necessary clarifying questions
- use the right source of truth
- respect authority boundaries
- produce the required output
- run the quality tests
- escalate when the document says to stop

## Scoring

| Criterion | Pass | Fail |
|---|---|---|
| Primitive clarity | Agent names the real unit of work | Agent describes surface UI actions only |
| Input sufficiency | Agent knows what it needs and where to get it | Agent invents missing context |
| Authority handling | Agent distinguishes allowed, approval, and never-do actions | Agent treats permission as generic write access |
| Risk detection | Agent spots money, customer data, production, legal, or reputation risk | Agent executes high-consequence action casually |
| Validation | Agent checks output against explicit tests | Agent relies on vague human review |
| Maintenance | Document has owner, review cadence, and update triggers | Document will silently rot |

## Validator Output

```markdown
# Semantic Document Validation: [Document]

## Verdict
PASS / REVISE / REWORK

## Execution Result
- Task attempted:
- Agent could execute from document alone: yes/no
- Clarifications required:
- Boundary respected:

## Gaps
| Gap | Severity | Fix |
|---|---|---|

## Revised Acceptance Criteria
[What must be true before this document can govern agent work.]
```
