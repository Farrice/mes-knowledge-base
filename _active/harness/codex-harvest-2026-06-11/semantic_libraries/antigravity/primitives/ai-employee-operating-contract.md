# AI Employee Operating Contract

## Purpose

Use this primitive when an Antigravity workflow, agent, automation, recurring job, or command should act like a reliable AI employee rather than a generic assistant. The goal is a role-scoped coworker with clear ownership, context boundaries, tool permissions, event handling, trust gates, and model regression checks.

This contract is grounded in `extractions/video-context/ohKt066uFhg/`, a transcript-backed package from "Viktor: AI Coworker That Lives in Slack - Fryderyk Wiatrowski".

## When To Use

- A user asks for an AI employee, AI coworker, company agent, operating partner, internal operator, or agent team member.
- A workflow should live inside an existing surface rather than a new app.
- A system needs shared context or shared integrations.
- A system may proactively suggest or perform work.
- A model, prompt, or tool swap could change trust, tone, or user comfort.
- Multiple people, projects, clients, channels, or private contexts could be mixed.

## Core Rule

An AI employee earns scope. It does not start with broad access, broad memory, broad proactivity, or broad autonomy.

## Required Contract Fields

| Field | Requirement |
|---|---|
| Role ownership | Name the employee role, job-to-be-done, owner, and work it must not own. |
| Work surface | Identify where the employee lives: Codex thread, local repo, Slack, email, Drive, calendar, dashboard, or other surface. |
| Context map | Define personal, project, team, client, and public context partitions. |
| Memory policy | Define what can be remembered, decayed, summarized, excluded, and deleted. |
| Integration map | List connectors/tools, owner, scope, allowed actions, approval gates, and revocation path. |
| Event ledger | Define how messages, edits, deletes, reactions, threads, file changes, schedules, and handoffs are interpreted. |
| Proactivity ladder | Define when the employee may observe, suggest, ask, draft, act in sandbox, act with approval, or act autonomously. |
| Trust/personality guard | Define model/prompt regression tests for tone, helpfulness, restraint, and user trust. |
| Rollout stage | Start with private/sandbox use, then small trusted cohort, then broader activation only after proof. |
| Validation | Include leakage tests, permission tests, event-semantics tests, trust canaries, and cold-start prompts. |
| Result surface | Define how the operator sees the scorecard, contract, map, checklist, and first implementation sequence. |

## AI Employee Scorecard

Score each area from 0 to 3.

| Area | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Role clarity | Vague helper | Broad domain | Named owner | Clear job, non-job, and escalation boundary |
| Work surface fit | Separate destination | Surface named | Surface behavior mapped | Surface changes perceived latency and trust correctly |
| Context isolation | Mixed context | Basic file/thread boundary | Project/team partitions | Tested leakage barriers and summary handoffs |
| Integration governance | Raw tool access | Tool list | Scoped permissions | Owner, approval, audit, and revocation path |
| Event semantics | Last message only | Some events considered | Event types mapped | Edits/deletes/reactions/thread drift handled |
| Proactivity | Random interruption | Suggests sometimes | Stage-gated suggestions | Earned ladder with quiet/safe defaults |
| Human approval | None | Manual review implied | Gates named | Gates tied to action risk and surface |
| Model regression | Task pass only | Model named | Model compare included | Personality/trust canaries protect swaps |
| Rollout safety | Big-bang launch | Private use | Small cohort | Broad activation only after evidence |
| User trust | Helpful output | Clear output | Friendly and restrained | Feels like a trusted teammate, not a tool blast |

## Default Step Order

1. **Intent lock**: decide audit, design, or upgrade mode.
2. **Evidence read**: inspect the target system plus this contract and source package.
3. **Surface map**: identify where the employee lives and what events it receives.
4. **Context/access map**: partition memory and integrations before adding autonomy.
5. **Employee contract**: define role, inputs, outputs, ownership, and gates.
6. **Trust ladder**: design proactivity and rollout in stages.
7. **Regression guard**: add model/personality, leakage, and event tests.
8. **Implementation sequence**: propose or build the smallest safe change.

## Human Checkpoints

Checkpoint before:

- Connecting Slack, Gmail, Drive, calendar, CRM, analytics, finance, or production systems.
- Giving an agent access to private, client, regulated, or cross-team data.
- Enabling proactive messages, external posts, account actions, or team-wide activation.
- Replacing a model/prompt used in a trusted employee role.

## Validation

Minimum proof for a deployed AI employee system:

```bash
python3 execution/validate_skill.py source-command-ai-employee-os
python3 execution/validate_skill.py fryderyk-wiatrowski-ai-employee-os
python3 execution/command_menu.py search "AI employee memory isolation shared integrations"
python3 execution/workflow_router.py search "company agent proactive workflow suggestions"
python3 execution/routing_governor.py evaluate "audit this agent for memory leakage"
```

Run broader Codex harness checks after command, routing, or registry changes.

## Cold-Start Prompts

- "Design an AI employee for client delivery."
- "Audit this agent for memory leakage between projects."
- "Upgrade this workflow so it can proactively suggest next actions."
- "Check whether swapping models degraded the agent's personality or trust."
- "Map which integrations a team-level agent should inherit versus block."
