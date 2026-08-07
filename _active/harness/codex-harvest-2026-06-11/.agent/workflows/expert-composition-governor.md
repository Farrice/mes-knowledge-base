---
description: Detect and prevent expert soup; compose many experts, skills, workflows, or agents into one owner-led outcome with bounded roles, handoffs, and a Composition Ledger
---

# /expert-composition-governor - Expert Composition Governor

## Purpose

Use this when the system needs the full arsenal without becoming a pile of experts.

The governor decides:

- whether multiple experts are actually needed,
- who owns the final output,
- which specialists get bounded slots,
- which experts should be skipped,
- how the result is integrated,
- what evidence proves composition happened.

## Operator Core Alignment

This workflow is the canonical source of truth for Expert-composition-governor behavior.
Global and local Expert-composition-governor wrappers must stay thin
compatibility wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/expert-composition-governor` prevents expert soup and full-arsenal sprawl.
- Use it when more than three experts/routes are plausible or when the user asks for the full arsenal.
- One function owner must integrate the final result.
- Specialists must occupy bounded slots and return specific contributions, preservation notes, and downstream risk.
- The Composition Ledger must show accepted, skipped, or rejected contributions with evidence of change.
- Expert names are not proof; integration evidence is proof.
- Do not spawn real Codex subagents unless explicitly authorized.
- Route broad broken-harness triage to `/autopilot` or `/system-audit`; route reusable source-to-system builds to `/source-to-skill-system`.

## Trigger

Run this when:

- the user says "expert soup," "too many agents," "not interwoven," "hammer instead of scalpel," or "use the full arsenal,"
- the task crosses several functions,
- more than three experts/skills are plausible,
- Autopilot, Orchestrate, or Mission surfaces many adjacent routes,
- a prior output listed experts but still felt generic,
- the user wants true end-to-end deployment of the harness.

## Pre-Flight

Read:

1. `semantic_libraries/antigravity/primitives/expert-composition-contract.md`
2. `semantic_libraries/antigravity/primitives/agent-arsenal-routing-contract.md`
3. `semantic_libraries/antigravity/primitives/skill-system-contract.md` when the result becomes reusable
4. `semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md` when the composition concerns agent harnesses, context engineering, review loops, package safety, source truth, or launch/use-now behavior
5. `docs/solutions/high-taste-writing-os.md` when the issue is writing/copy/content
6. `docs/solutions/routing-governor-self-compounding-workspace.md` when the issue is routing failure

## Routing Pass

Run the normal arsenal lookup before choosing the composition:

```bash
python3 execution/command_menu.py search "[goal/context]"
python3 execution/workflow_router.py search "[goal/context]"
python3 execution/expert_router.py route "[goal/context]"
python3 execution/expert_router.py compounds "[goal/context]"
python3 execution/context_retriever.py search "[goal/context]" --top 8
python3 execution/tool_router.py route "[goal/context]"
```

For high-stakes full-arsenal, agent-elevation, subagent, cross-pollination, or
plugin/tool-blending work, run the Virtuoso composer as the integration surface:

```bash
python3 execution/virtuoso_orchestration.py "[goal/context]" --json
```

If real delegation was requested, add `--delegate-intent`. Do not add
`--log-routing` until the selected composition is actually used in the current
work.

## Composition Workflow

### 1. Decide If This Is Expert Soup

| Question | Soup Risk |
|---|---|
| Are more than three experts being considered? | High |
| Do experts overlap in role? | High |
| Is there no clear output owner? | High |
| Are experts named as proof instead of evidence? | High |
| Does the output need one voice, one workflow, or one user path? | High |

If risk is high, apply the contract before producing the output.

### 2. Pick The Function Owner

Choose one owner by output type. The owner writes or integrates the final result.

For agentic engineering system upgrades, the function owner is the system
workflow owner, not the loudest expert or tool. Use `/source-to-skill-system`
when source material becomes reusable, `/self-evolve` when a bounded mutation
loop is needed, and `/system-audit` when the issue is firing behavior,
verification, or control-plane drift.

### 3. Fill Contribution Slots

Use at most one expert per slot:

- Spine
- Differentiator
- Mechanism
- Craft
- Risk Gate

### 4. Run Specialist Passes

Each specialist returns only:

- diagnosis,
- top 1-3 changes,
- exact affected line, section, artifact, or decision,
- what to preserve,
- downstream risk.

### 5. Integrate

The owner integrates, removes duplication, resolves tension, and makes the output read or behave as one coherent thing.

For agentic engineering work, integration must preserve:

- human-owned objective and stop condition,
- thin context and exact source paths,
- small reviewable chunks,
- dependency safety gates,
- one use-now artifact before expansion.

### 6. Produce The Composition Ledger

Include the ledger for high-stakes, multi-expert, or previously failed work.

## Output Contract

```markdown
## Expert Composition Plan
| Slot | Expert/Asset | Why This Slot | Output It Must Produce |
|---|---|---|---|

## Composition Ledger
| Slot | Expert/Asset | Contribution Accepted | Evidence Of Change | Skipped/Rejected |
|---|---|---|---|---|

**Owner:**
**Integration rule:**
**Expert soup check:** PASS / REVISE / REWORK
**Skipped experts:**
**Next verification:**
```

For full-arsenal or agentic-system work, also include:

```markdown
## Virtuoso Trace
- **Route / Owner**:
- **Recommended stack**:
- **Composition slots**:
- **Delegation matrix**:
- **Plugin/tool surface**:
- **Routing evidence**:
- **Verification**:
- **First action**:
```

## Fail Conditions

Fail if:

- no owner is named,
- the output uses experts as decoration,
- two specialists are doing the same job,
- no evidence of change is shown,
- the user would still need to coordinate the pieces manually.
- an agentic engineering output names many tools but lacks a context plan, source-truth path, review stop condition, or dependency safety decision.

## Handoffs

- Writing/copy/content quality -> `/high-taste-writing-os`
- Public/revenue copy -> `/publishable-copy-gate` after composition
- System or routing failures -> `/system-audit`, `/self-evolve`, or `/mission`
- Reusable OS/workflow -> `/source-to-skill-system` and Mission artifact contract
- Agentic engineering harvests -> `/source-to-skill-system` plus `agentic-engineering-loop-contract.md`

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_expert_composition_governor.py --check
python3 execution/verify_operator_core_expert_composition_governor.py
python3 execution/verify_expert_composition_standard.py
python3 execution/validate_skill.py source-command-expert-composition-governor
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
