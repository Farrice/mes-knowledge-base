# Codex Dynamic Workflow Manifest

## Purpose

Use this primitive when a task is too large or verification-heavy for one chat
thread, but should still remain owner-led, approval-gated, and traceable inside
Codex Antigravity.

The manifest keeps orchestration state outside the main conversation: objective,
recipe, phases, worker packets, inputs, outputs, verification rules, approval
gates, resume state, and the final integration owner.

## When To Use

- Large codebase audits or many-file migrations.
- Cross-checked research that needs independent angles and claim reconciliation.
- Adversarial review loops where the plan must survive critique before build.
- Source-to-system extraction where evidence, route fit, proof, and live surface
  validation should happen in sequence.
- Any task where intermediate results should be resumable without relying on
  hidden chat context.

## Runtime Boundary

`execution/codex_dynamic_workflow.py` owns manifests, status, phase completion,
resume markers, verification, and receipts. It never spawns real Codex
subagents by itself.

The runtime is portable. Installed globally, it can run from any Codex
workspace and stores state in that workspace under `.agent/dynamic-workflows/`.
Set `CODEX_DYNAMIC_WORKFLOW_ROOT=/absolute/path` when a run should bind to a
specific workspace root.

Real Codex subagents remain gated by the Codex subagent tool surface and require
explicit user authorization. The runtime may prepare worker packets, but the
main Codex thread remains the integration owner.

## Manifest Fields

| Field | Requirement |
|---|---|
| `schema_version` | `codex-dynamic-workflow/v1` |
| `run_id` | Stable saved-run identifier |
| `objective` | User-owned objective |
| `recipe` | One of the approved workflow recipes |
| `phases` | Ordered phase list with inputs, outputs, workers, gates, and verifiers |
| `worker_packets` | Bounded tasks with input and output contracts |
| `approval_gates` | External, paid, destructive, global, connector, Mission, and real-subagent gates |
| `runtime_state` | Current status, phase index, completed phases, blocked reason, and next action |
| `verification_rules` | Structural and behavior checks before receipt |
| `final_integration_owner` | Always the main Codex thread unless explicitly changed |
| `receipt` | Final summary of planned work, approvals, checks, and remaining gates |

## Operational Commands

```bash
python3 execution/codex_dynamic_workflow.py plan "[objective]"
python3 execution/codex_dynamic_workflow.py status
python3 execution/codex_dynamic_workflow.py complete-phase [phase-id] --result-path [path] --summary "[summary]"
python3 execution/codex_dynamic_workflow.py verify
python3 execution/codex_dynamic_workflow.py receipt
```

Use `complete-phase` after saving a phase result artifact. It updates the phase,
worker packets, completed phase list, current phase pointer, status, and
receipt-visible result paths.

## Recipes

| Recipe | Use When | Core Phases |
|---|---|---|
| `codebase-audit` | Broad repo or harness audit | scope map, slice audits, cross-check, synthesis |
| `migration-planning` | Many-file migration or compatibility change | inventory, partition, dependency map, rollout plan |
| `cross-checked-research` | Current or high-stakes research | angle plan, independent evidence, claim reconciliation, brief |
| `adversarial-plan-review` | Plan needs critique before execution | decompose, red team, repair, approval packet |
| `source-to-system-extraction` | Source should become reusable capability | evidence, route fit, build shape, proof, live surface |

## Validation

Run:

```bash
python3 execution/verify_codex_dynamic_workflow.py
```

For Virtuoso integration, also run:

```bash
python3 execution/verify_virtuoso_orchestration.py
python3 execution/codex_harness_check.py
```

## Last Updated

2026-05-30
