# Agentic OS Data Map Contract

## Purpose

Use this primitive when an operator's AI system is underused because the data layer is not organized. The contract turns business tools into a Pantry -> Prep -> Plate map, then into a build order for summary tables, hooks, rules, orchestrators, approval gates, and commands.

## When To Use

- A user asks for `/silver-platter`.
- A user wants to build an agentic OS for a business.
- A user says their assistant is running but not producing business value.
- A workflow needs to decide what data summaries agents should read before building more agents.
- A business has regulated data and needs model containment, path scoping, audit logs, or approval gates.

## Required Objects

| Object | Meaning | Required Fields |
|---|---|---|
| Pantry | Raw data sources and tools | id, tool, format, cadence, volume, feeds, status, explanation |
| Prep | Silver platters or summary tables | id, name, domain, sources, schedule, status, sample_content |
| Plate | Human-facing outputs | id, name, agent, consumers, approval_gate, reads_from, sample_output |
| Recipe | Repeated workflow to automate | id, headline, goal, ingredients, stack, walkthrough, before, after |
| Setup priority | Ordered build plan | title, title_friendly, requires, what_to_do, why, working_when |
| Interaction layer | Where humans read outputs | id, channel, type, status, description, consumes |
| Opportunity | What to build or defer | surface, type, title, explanation, feature, impact |

## Order

1. Audit local setup.
2. Classify archetype.
3. Ask only for missing operator facts.
4. Derive Pantry from named tools plus defaults.
5. Derive Prep from archetype and weekly pain.
6. Derive Plate from decisions humans actually read.
7. Add recipes.
8. Add setup priority.
9. Add interaction layer.
10. Render dashboard, opportunities, and handoff.

## Regulated Data Rule

For healthcare, law, wealth advisory, and any sensitive-client data domain, model containment and scoped access come before convenience automation. The first setup step must lock the approved model/deployment path, and later steps must include path-scoped rules, audit logs, and approval gates.

## Result Surface

- `data_map.html` is allowed as a visual dashboard.
- `data_map.json` is the canonical data object.
- `OPPORTUNITIES.md` is a Local Markdown Source.
- Written recommendations should be shown in conversation as a Rendered Conversation Document.
- External exports require explicit user request.

## Validation

A valid run must prove:

- Example data maps parse.
- Regulated examples put containment before automation.
- The renderer writes HTML.
- Opportunities and handoff are deterministic scripts, not only prompt instructions.
- Command bridge exists across `.agent/workflows/`, `.claude/commands/`, and `.agents/skills/source-command-*`.
- A cold-start user can identify the first action without this chat.

