# AI Employee Operating Model

## Definition

An AI employee is a role-scoped agentic system that owns a repeatable job inside the user's existing work environment. It is not a generic chatbot and not a one-off automation.

## Required Design Questions

| Question | Good Answer |
|---|---|
| What job does it own? | A concrete recurring job with clear outputs. |
| What does it not own? | Explicit non-job and escalation boundary. |
| Where does it live? | The natural work surface for the job. |
| What context may it use? | Partitioned sources with allowed flows. |
| What tools may it touch? | Scoped integrations with owner and approvals. |
| When can it interrupt? | Proactivity ladder tied to trust stage. |
| How does it prove itself? | Scorecard, event tests, and staged rollout. |

## Antigravity Translation

For this workspace, an AI employee usually starts as:

- A command front door.
- A source-backed skill or workflow.
- A local memory/context policy.
- A validation and routing proof.
- A human-reviewed rollout path.

External channels such as Slack can be designed later, but the local OS contract should exist first.
