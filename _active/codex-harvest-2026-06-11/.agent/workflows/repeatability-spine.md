---
description: Preserve what made a great output work, diagnose failed revisions, repair wrong routes or regressions, and create replay prompts plus regression guards
---

# /repeatability-spine - Repeatability Spine

Use this when the system produced magic once but cannot reproduce it, when a
revision got worse, when a route picked the wrong workflow, or when a patch
introduced a regression.

This is a Codex-native skill system using:

- `semantic_libraries/antigravity/primitives/repeatability-spine-contract.md`
- `semantic_libraries/antigravity/primitives/skill-system-contract.md`
- `docs/mission-artifacts/repeatability-spine/seed-ai-misfire-examples.md`

## Operator Core Alignment

This workflow is the canonical source of truth for Repeatability-spine behavior.
Global and local Repeatability-spine wrappers must stay thin compatibility
wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/repeatability-spine` preserves the good example before repair.
- Every run needs grounded evidence, one primary failure class, Preservation Lock, repair route, validation, regression guard, and replay prompt.
- Inaccessible conversations are pending evidence, not invented findings.
- Routing failures require a verifier query or routing feedback log before being called repaired.
- Mutation-capable repair routes (`/self-evolve`, `/skill-anneal`, `/skill-evolution`) require a Goal Packet before edits.
- Global `~/.codex` behavior changes require workspace proof and explicit approval.
- Route broad broken-harness triage to `/autopilot` or `/system-audit`; use `/repeatability-spine` for failed revisions, lost magic, wrong routes, and regressions.
- Real Codex subagents require explicit authorization.

## Usage

```bash
/repeatability-spine [good example + failed example or failure phrase]
```

## Pre-Flight Reads

1. `CODEX.md`
2. `semantic_libraries/antigravity/primitives/repeatability-spine-contract.md`
3. `semantic_libraries/antigravity/primitives/skill-system-contract.md`
4. `semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md` when failures become an evolution or annealing search set
5. `docs/mission-artifacts/repeatability-spine/seed-ai-misfire-examples.md`
6. `.agent/workflows/publishable-copy-gate.md` when public/revenue copy is involved
7. `.agent/workflows/system-audit.md` when routing or control-plane behavior failed
8. `.agent/workflows/self-evolve.md` when failures become an evolution search set
9. `.agent/workflows/skill-anneal.md` when one component skill is the weak point

## Workflow

### 1. Intake Evidence

Collect only grounded evidence:

- good output path, snippet, route output, or verifier pass
- failed output path, user quote, route output, or verifier failure
- current user goal
- changed surface: draft, workflow, route, script, verifier, or artifact

If the user references a conversation that is not locally accessible, mark it
as pending evidence instead of inventing findings.

### 2. Classify Failure

Choose exactly one primary failure class:

| Class | Use When | Repair Route |
|---|---|---|
| creative revision degradation | rewrite got flatter, generic, weaker, less human, or lost proof/voice/tension | `/publishable-copy-gate`, `/excellence-gate`, relevant expert stack |
| wrong workflow/routing | literal keyword or generic workflow won over the intended route | `/system-audit`, `/routing-intelligence`, router patch, golden query |
| code/workflow regression | implementation changed behavior or broke a verifier | targeted patch, compile/test, regression guard |

Secondary classes are allowed, but the primary class controls the first repair.

### 3. Extract Preservation Lock

Before revising or patching, write:

```markdown
## Preservation Lock
- **Keep**:
- **Change**:
- **Do not disturb**:
- **Risk**:
- **Gate**:
```

For creative work, preserve the strongest voice/proof/tension and buyer
recognition. For routing, preserve the exact user phrase and expected route.
For code, preserve existing passing behavior and approval boundaries.

### 4. Compare Failed Revision

Create a short delta:

| Dimension | Good Run | Failed Run | Degradation |
|---|---|---|---|
| Route/context |  |  |  |
| Voice/intent/behavior |  |  |  |
| Proof/validation |  |  |  |
| User-facing surface |  |  |  |

### 5. Choose Repair Route

- Public, revenue, LinkedIn, outreach, or offer copy -> `/publishable-copy-gate`
- Route chose wrong command -> `/system-audit` plus `routing_intelligence.py misroute`
- One skill underperformed -> `/skill-anneal`
- Recurring failure set exists -> `/self-evolve`
- Source/workflow system shape is missing -> `/source-to-skill-system`
- Broad system not firing -> `/autopilot` or `/system-audit`

If the repair route is `/self-evolve`, `/skill-anneal`, or `/skill-evolution`,
also create a Goal Packet from
`semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md`.
The packet must name the target, proof artifact, measurable stop condition,
turn cap, evaluator, wake-up check, human checkpoint, and no-regression rule
before any mutation-capable repair starts.

### 6. Add Regression Evidence

Every run must leave at least one of:

- exact golden routing query
- verifier fixture
- copy gate preservation rule
- failure pack for `/self-evolve`
- skill anneal failure example
- goal packet for `/self-evolve`, `/skill-anneal`, or `/skill-evolution`
- replay prompt stored in the result surface

### 7. Produce Replay Prompt

End with a paste-ready prompt:

```text
Repeat this class of work.
Good example: [path].
Preserve: [lock].
Change: [intent].
Gate: [validation].
Do not ship unless: [acceptance criteria].
```

## Seed Examples

Use the AI Misfire seed when the user asks about the prior "magic" LinkedIn
revision:

- Good: `brain/hybrid-ai-misfire-avatar-content-v1/LINKEDIN-POSTS-V3-VOICE-PROOF.md`
- Copy-ready: `brain/hybrid-ai-misfire-avatar-content-v1/archive/readable-artifacts/today-post-copy-ready.txt`
- Audit: `brain/hybrid-ai-misfire-avatar-content-v1/V2-TO-V3-CONTENT-AUDIT.md`
- Failure: May 9 generic urgent-cash AI Misfire rollout summary
- Pending: `Get Audit Customers Fast`

## Output Contract

```markdown
## Repeatability Spine Result
- **Failure class**:
- **Good example**:
- **Failed example**:
- **Original route/context**:
- **Expert stack**:
- **Preservation Lock**:
- **Repair route**:
- **Validation**:
- **Regression guard**:
- **Replay prompt**:
- **Pending evidence**:
```

## Quality Gate

Reject the run if it:

- revises without a Preservation Lock
- makes inaccessible conversation claims
- fails to choose a primary failure class
- skips relevant copy, route, or regression gates
- fixes a routing failure without adding a query to a verifier or feedback log
- changes global `~/.codex` behavior before workspace proof and user approval

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_repeatability_spine.py --check
python3 execution/verify_operator_core_repeatability_spine.py
python3 execution/validate_skill.py source-command-repeatability-spine
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
