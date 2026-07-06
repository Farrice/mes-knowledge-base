---
description: Design, audit, or upgrade AI employee systems, company agents, and AI coworkers with context isolation, scoped integrations, event semantics, proactive workflow suggestions, trust ladders, rollout gates, and model/personality regression checks
domains: system, agentic, operations, memory, trust
---

# /ai-employee-os - AI Employee Operating System

## Purpose

Design, audit, or upgrade an AI employee system so it behaves like a trusted role-scoped teammate instead of a generic assistant. Use this when a system needs ambient work-surface fit, shared context, memory isolation, scoped integrations, event semantics, proactivity, rollout gates, or model/personality regression checks.

## Source Evidence

Read these live sources before serious use:

1. `CODEX.md` — the Codex-native operating authority for this workspace.
2. `semantic_libraries/antigravity/primitives/ai-employee-operating-contract.md` — the operating contract this command enforces.
3. `skills/fryderyk-wiatrowski-ai-employee-os/SKILL.md` — the extracted source skill.
4. `skills/fryderyk-wiatrowski-ai-employee-os/workflows/ai-employee-os.md` — the detailed source workflow.
5. `extractions/video-context/ohKt066uFhg/evidence-map.md` — the source evidence map.
6. `extractions/video-context/ohKt066uFhg/uncertainty-report.md` — the source uncertainty limits.
7. `.agents/skills/source-command-ai-employee-os/SKILL.md` — the command wrapper that delegates here.

Load detailed references only when needed:

- `skills/fryderyk-wiatrowski-ai-employee-os/references/context-memory-isolation.md`
- `skills/fryderyk-wiatrowski-ai-employee-os/references/shared-integration-permission-design.md`
- `skills/fryderyk-wiatrowski-ai-employee-os/references/ambient-interface-event-handling.md`
- `skills/fryderyk-wiatrowski-ai-employee-os/references/trust-proactivity-rollout-gates.md`
- `skills/fryderyk-wiatrowski-ai-employee-os/references/model-personality-regression-guard.md`
- `skills/fryderyk-wiatrowski-ai-employee-os/references/quality-rubric.md`

## Modes

```bash
/ai-employee-os [target system or agent]
/ai-employee-os --audit [target]
/ai-employee-os --design [role/context/tools]
/ai-employee-os --upgrade [route/skill/workflow]
```

Mode rules:

- `--audit`: evaluate an existing system and produce a scorecard plus fix sequence.
- `--design`: design a new employee role, contract, context/access map, trust ladder, and implementation path.
- `--upgrade`: propose or implement safe local changes to an existing Antigravity route, skill, workflow, or agent.

If no mode is provided, infer it. Use `--audit` for existing targets and `--design` for new roles.

## Operating Contract

| Field | Required Behavior |
|---|---|
| Source evidence | Cite the live operating contract and keep source/visual limits explicit; never invent capabilities the evidence does not support. |
| Objective | Produce an AI employee scorecard, contract, maps, regression guard, and first implementation sequence. |
| Components | This workflow, the `source-command-ai-employee-os` wrapper, the semantic primitive, supporting routes, and validation scripts. |
| Step order | intent -> routing -> scorecard -> system contract -> context/access map -> integration map -> event semantics -> trust ladder -> regression guard -> implementation sequence |
| Inputs | Target system/role, work surface, context sources, tools, approvals, rollout expectations. |
| Outputs | Scorecard, employee contract, context/access map, integration map, event map, trust ladder, validation checklist, first build path. |
| Human checkpoint | Required before external connections, external messages, account actions, broad activation, private/client data access, or real Codex subagents. |
| Validation | Skill validation, router discoverability, leakage tests, event tests, personality canaries, cold-start prompts. |
| Context policy | Keep this command and the semantic contract compact; load the archived source package and detailed references on demand only. |

## Routing Stack

Run targeted routing before choosing supporting components:

```bash
python3 execution/command_menu.py search "[ai employee/system goal]"
python3 execution/workflow_router.py search "[ai employee/system goal]"
python3 execution/expert_router.py route "[ai employee/system goal]"
python3 execution/context_retriever.py search "[ai employee/system goal]" --top 8
```

Supporting routes (use the ones that exist for the situation):

- `/context-audit`: context bloat, leakage, and compression.
- `/memory-architect`: persistent memory and retrieval tiers.
- `/source-to-skill-system`: future source-to-OS expansions.

## Execution

1. **Intent lock**: state mode, target, desired outcome, and external-action boundary.
2. **Evidence and target read**: load the compact live source set and the target files.
3. **Scorecard**: score role clarity, surface fit, context isolation, integration governance, event semantics, proactivity, approvals, model regression, rollout safety, and user trust.
4. **System contract**: define job, non-job, owner, surface, inputs, outputs, handoffs, and approvals.
5. **Context/access map**: separate personal, project, team, company, client, and public context.
6. **Integration map**: define owner, scope, actions, approvals, audit trail, and revocation.
7. **Event semantics**: define how new messages, DMs, threads, edits, deletes, reactions, files, and recurring triggers are handled.
8. **Trust ladder**: define proactivity from observe -> suggest -> ask -> draft -> sandbox -> approved act -> narrow autonomy -> broader activation.
9. **Regression guard**: define model/personality, leakage, event, integration, and proactivity canaries.
10. **Implementation sequence**: give the smallest safe build, validation commands, and a cold-start prompt.

## Operator Core Closeout

Close every meaningful run with persistent steering: for substantial design/audit/upgrade work, include **3 Next Prompts** (Use Now / Harden / Expand), and always end with an **Operator Lesson** plus a **Next-time prompt**, a **Subagent worth it?** check (real Codex subagents require explicit authorization and default to read-only diagnostics), and a **Reuse hook** for what to make repeatable.

## Validation

```bash
python3 execution/validate_skill.py source-command-ai-employee-os
python3 execution/command_menu.py search "AI employee memory isolation shared integrations"
python3 execution/workflow_router.py search "company agent proactive workflow suggestions"
```

After bridge, registry, or routing changes, also run the relevant Codex harness proof set from `CODEX.md`.

## Cold-Start Proof

A fresh operator should be able to ask:

```text
/ai-employee-os --design "AI employee for client delivery"
/ai-employee-os --audit "this agent for memory leakage between projects"
/ai-employee-os --upgrade ".agent/workflows/client-delivery-agent.md for proactive suggestions"
```

The system must identify the live source-evidence paths, the component order, context/access risks, approval gates, validation checks, and the first action without hidden chat context.
