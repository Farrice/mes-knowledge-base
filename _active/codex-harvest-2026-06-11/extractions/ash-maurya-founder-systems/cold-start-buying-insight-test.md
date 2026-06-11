# Cold-Start Test: `/ash-buying-insight`

## Test Setup

Workflow used: `skills/ash-maurya-founder-systems/workflows/13-buying-insight-interview.md`

Loaded context:

- `skills/ash-maurya-founder-systems/genius.md`
- `skills/ash-maurya-founder-systems/references/hidden-knowledge.md`
- `skills/ash-maurya-founder-systems/references/genius-patterns.md`

No hidden conversational explanation was required.

## Sample Input

Vague problem: "Consultants want AI dashboards for client delivery."

## Sample Output

### Old-Way Target

Interview consultants currently using spreadsheets, shared docs, manual status emails, or project dashboards to manage client delivery.

### Better Interview Question

"Walk me through the last client project where reporting or handoff got messy. What happened, and where did you struggle?"

### Behavior Reconstruction Map

- Trigger: client asked for status or deliverables were delayed.
- Old way: spreadsheet plus manual email updates.
- Search: tried project templates, dashboards, or assistants.
- Fired alternatives: too much setup, too generic, did not match delivery reality.
- Chosen alternative: kept spreadsheets because they were flexible and already understood.
- Tradeoff: accepted repeated manual updates and missed context.

### Buying Criteria

- Must reduce manual update work without forcing a new operating system.
- Must preserve client-specific nuance.
- Must show value within one active project.
- Must not require the consultant to rebuild their whole delivery process.

### Commitment Ask

"Based on the delivery handoff you described, I can map the exact manual steps costing you time and show a lightweight automation path for one active client project. If the map finds at least three hours per week of removable work, would you pay for a 48-hour workflow audit?"

## Result

Pass. The workflow converts a vague feature idea into past-tense interview questions, old-way diagnosis, buying criteria, and a commitment ask.

