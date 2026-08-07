# Semantic Document Examples

## Example 1: Meeting Reschedule

Primitive: Reschedule a meeting.

Meaning: This is not "change a calendar time." It may change attendee prep windows, customer commitments, internal dependencies, and relationship expectations.

Authority:

- Agent may propose alternate times.
- Agent may move internal low-stakes meetings when all attendees are available.
- Agent must request approval for customer meetings, executive meetings, interviews, or meetings within 24 hours.
- Agent must never delete a meeting without explicit approval.

Quality tests:

- No attendee loses required prep time.
- The new time has no conflicts.
- The message explains why the change happened when external people are affected.
- The original meeting purpose is preserved.

## Example 2: Client Audit Delivery

Primitive: Deliver an AI Business Asset Audit.

Meaning: This is not "write a report." It is a trust-building diagnostic that identifies where the client can use AI to remove friction, create leverage, or reduce risk.

Authority:

- Agent may analyze public assets and supplied files.
- Agent may draft findings and recommendations.
- Agent must not claim access to private dashboards unless exports were provided.
- Agent must not promise revenue outcomes without evidence.

Quality tests:

- Every finding has evidence.
- Recommendations are ranked by speed, value, and difficulty.
- The first implementation step is clear.
- The client can act within 48 hours.

## Example 3: Agent Workflow Update

Primitive: Update a workflow.

Meaning: This is not "edit markdown." It changes how future agents behave.

Authority:

- Agent may edit workflow docs inside the approved workspace.
- Agent must preserve bridge layers if command discoverability is affected.
- Agent must validate routing after changes.
- Agent must not modify the original Google Antigravity workspace unless asked.

Quality tests:

- Command appears in command menu.
- Workflow router finds it.
- Skill validation passes or known warnings are documented.
- The workflow can be executed without hidden assumptions.
