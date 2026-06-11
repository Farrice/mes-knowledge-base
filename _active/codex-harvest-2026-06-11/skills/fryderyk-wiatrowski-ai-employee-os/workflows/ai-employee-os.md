# AI Employee OS Workflow

## Role

You are designing or auditing an AI employee system. Think like a product-minded AI systems architect: the employee must do useful work, live in the right surface, know the right context, protect private context, use tools through scoped permissions, and earn autonomy through trust.

## Inputs

- Mode: `--audit`, `--design`, or `--upgrade`
- Target system, role, agent, skill, workflow, or route
- Current work surface: Codex thread, local files, Slack, email, calendar, Drive, CRM, dashboard, or other
- Context sources and memory rules
- Tools/integrations and approval constraints
- Desired result surface

## Pre-Flight Reads

Read compact files first:

1. `semantic_libraries/antigravity/primitives/ai-employee-operating-contract.md`
2. `extractions/video-context/ohKt066uFhg/evidence-map.md`
3. `skills/fryderyk-wiatrowski-ai-employee-os/SKILL.md`

Read detailed references only when needed:

- `references/ai-employee-operating-model.md`
- `references/context-memory-isolation.md`
- `references/shared-integration-permission-design.md`
- `references/ambient-interface-event-handling.md`
- `references/trust-proactivity-rollout-gates.md`
- `references/model-personality-regression-guard.md`
- `references/quality-rubric.md`

## Mode Resolution

- Use `--audit` when the target already exists and the user wants a score, risks, or gaps.
- Use `--design` when the user wants a new AI employee role or system.
- Use `--upgrade` when the user wants concrete changes to an existing route, skill, workflow, agent, or command.
- If the user does not name a mode, infer it from the task. If still unclear, default to `--audit` for existing targets and `--design` for new roles.

## Execution

### 1. Intent Lock

State the selected mode, target, desired outcome, and external-action boundary.

### 2. Routing Trace

Run or emulate targeted routing:

```bash
python3 execution/command_menu.py search "[target intent]"
python3 execution/workflow_router.py search "[target intent]"
python3 execution/routing_governor.py evaluate "[target intent]"
python3 execution/expert_router.py route "[target intent]"
python3 execution/context_retriever.py search "[target intent]" --top 8
```

Use supporting routes as components. Do not let adjacent routes replace `/ai-employee-os` when the core question is AI employee design, memory leakage, shared integrations, proactivity, ambient events, or employee trust.

### 3. Scorecard

Score 0-3:

- Role clarity
- Work surface fit
- Context isolation
- Integration governance
- Event semantics
- Proactivity
- Human approval
- Model regression
- Rollout safety
- User trust

### 4. System Contract

Produce:

- Employee role and job-to-be-done
- Non-job and escalation boundary
- Work surface and expected latency
- Inputs, outputs, and handoffs
- Human checkpoint and approval gates

### 5. Context/Access Map

Separate:

- Personal/private context
- Project context
- Team/company context
- Client/regulatory context
- Public/reference context
- Memory retention, decay, and deletion rules
- Allowed and blocked cross-context flows

### 6. Integration Map

For each tool/connector:

- Owner
- Scope
- Allowed actions
- Required approvals
- Audit trail
- Revocation path
- Personal versus team availability

### 7. Event Semantics Map

Define how the employee handles:

- New messages
- Thread replies
- DMs
- Mentions
- Edits
- Deletes
- Reactions
- File changes
- Scheduled or recurring triggers
- Cross-thread or cross-channel continuation

### 8. Proactivity And Trust Ladder

Default ladder:

1. Observe silently
2. Suggest in response
3. Ask before drafting
4. Draft for review
5. Act in sandbox
6. Act with approval
7. Act autonomously inside narrow scope
8. Broader activation after proof

### 9. Regression Guard

Define tests for:

- Personality/tone drift
- Model or prompt swaps
- Context leakage
- Incorrect integration choice
- Event misinterpretation
- Over-proactivity
- Silent quality drift

### 10. First Implementation Sequence

Provide the smallest safe next build:

- Files/routes/components to touch
- Validation commands
- Cold-start prompt
- Human checkpoint
- Rollout stage

## Output Schema

```markdown
## AI Employee OS
- **Mode**:
- **Target**:
- **External boundary**:

## Scorecard
| Area | Score | Evidence | Fix |

## System Contract

## Context And Access Map

## Integration Map

## Event Semantics

## Proactivity And Trust Ladder

## Model And Personality Guard

## Validation Checklist

## First Implementation Sequence
```

## Cold-Start Proof

A fresh run should handle:

- "Design an AI employee for client delivery."
- "Audit this agent for memory leakage between projects."
- "Upgrade this workflow so it can proactively suggest next actions."
- "Check whether swapping models degraded the agent's personality or trust."
- "Map which integrations a team-level agent should inherit versus block."

## Quality Gate

Reject or revise the output if:

- It describes a generic assistant instead of a role-scoped employee.
- It grants broad memory, tools, or proactivity without staged trust.
- It ignores edits/deletes/thread drift when the surface is conversational.
- It treats connector count as more important than scope and auditability.
- It swaps or recommends models without a personality/trust canary.
