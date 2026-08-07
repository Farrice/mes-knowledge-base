# Codex Global Alignment Mirror Proposal

## Status

Approved and applied. The narrow global mirror was written to the five approved
global wrapper surfaces after Farrice explicitly confirmed approval.

This document began as the proposal to mirror the workspace-local Operating
Alignment proof into global Codex behavior. The mirror stayed thin: global
surfaces route to the canonical Antigravity workflow and contract, not a
competing operating system.

Applied surfaces:

- `/Users/farricecain/.codex/AGENTS.md`
- `/Users/farricecain/.codex/skills/autopilot/SKILL.md`
- `/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md`
- `/Users/farricecain/.codex/skills/system-audit/SKILL.md`
- `/Users/farricecain/.codex/skills/source-command-system-audit/SKILL.md`

Post-application proof:

- global wrapper snippet smoke: PASS
- `python3 execution/verify_system_control_plane.py`: PASS
- non-Antigravity operating-alignment smoke from `/private/tmp`: PASS
- Google Antigravity remained untouched

## Source Proof

Workspace-local proof:

- `semantic_libraries/antigravity/primitives/operating-alignment-contract.md`
- `semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md`
- `.agent/run-receipts/latest.md`
- `execution/routing_governor.py`
- `execution/autopilot_runtime_preflight.py`
- `execution/virtuoso_orchestration.py`
- `execution/recurring_ops.py`

Passed proof:

- `python3 execution/verify_recurring_ops_dry_run.py`
- `python3 execution/verify_autopilot_runtime_preflight.py`
- `python3 execution/verify_virtuoso_orchestration.py`
- `python3 execution/verify_automation_cohesion_standard.py`
- direct command menu, workflow router, routing governor, and stack recommender proof
- `python3 execution/run_receipt.py --verify`
- artifact and export guards

Known limitation:

- `python3 execution/verify_system_control_plane.py` hung with no output and was
  stopped. Direct changed-surface proof passed. Treat the full verifier as a
  hardening item before broad global rollout, not as proof that the mirror is
  unsafe.

## Mirror Decision

Recommended mirror scope:

1. `/Users/farricecain/.codex/AGENTS.md`
2. `/Users/farricecain/.codex/skills/autopilot/SKILL.md`
3. `/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md`
4. `/Users/farricecain/.codex/skills/system-audit/SKILL.md`
5. `/Users/farricecain/.codex/skills/source-command-system-audit/SKILL.md`

Do not mirror execution scripts, recurring automations, local state files,
Coach Cooz/Josh project artifacts, or the whole expert library into global
Codex.

## Proposed Global Behavior

Operating-alignment requests should route like this:

| Trigger | Owner | Support gates |
|---|---|---|
| system feels ineffective, noisy, disjointed, globally inconsistent, over-abstracted, or not using Autopilot/Virtuoso/skills well | `/system-audit` | `/autopilot`, `/virtuoso`, `/expert-composition-governor`, `/routing-intelligence`, `/health-check`, `/repeatability-spine`, `/self-evolve` |

Global behavior should preserve these boundaries:

- one owner before experts
- expert composition as support, not owner, unless the user asks for expert-soup repair directly
- no real Codex subagents without explicit authorization
- no global writes without explicit approval
- no Google Antigravity edits unless explicitly approved
- no automation deletion or disabling without an approval list
- no broad plugin/global expansion until workspace proof and mirror approval pass

## Patch Plan

### 1. Global AGENTS.md

Add a section near Global System-audit or Global Autopilot:

```markdown
## Global Operating Alignment Repair

Use `/system-audit` as the owner when Farrice says Codex feels ineffective,
noisy, disjointed, globally inconsistent, over-abstracted, not firing, not
using Autopilot/Virtuoso/skills well, or asks for a unified operating layer
across global and workspace contexts.

Default behavior: raw intent -> Co-Creative Launchpad -> meta-intent
classification -> one owner -> bounded support gates -> Orchestration Receipt
-> verifier proof -> feedback hook -> one next action.

Support gates are `/autopilot`, `/virtuoso`,
`/expert-composition-governor`, `/routing-intelligence`, `/health-check`,
`/repeatability-spine`, and `/self-evolve`. Do not route these requests to a
random domain expert stack. Do not spawn real Codex subagents without explicit
authorization. Do not write `~/.codex`, edit Google Antigravity, delete
automations, publish, or perform destructive cleanup without explicit approval.

The canonical workspace contract is
`/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/operating-alignment-contract.md`.
Magic preservation evidence lives at
`/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md`.
```

### 2. Global Autopilot Skill

Add to `/Users/farricecain/.codex/skills/autopilot/SKILL.md`:

```markdown
## Operating Alignment

When the raw intent asks for global/workspace Codex alignment, orchestration
repair, output consistency, automation cleanup, subagent/expert coordination,
or "maximum firepower" from the system itself, classify the meta-intent as
`operating-alignment`.

Operating alignment is owned by `/system-audit`. Autopilot should render the
Launchpad and trace, then hand off with support gates instead of asking Farrice
to pick from a menu.

Every meaningful operating-alignment trace should include an Orchestration
Receipt with objective, meta_intent, owner, composition_owner, route,
support_gates, expert_lenses, subagent_boundary, verifier_results, and
feedback_hook.
```

### 3. Global Source-command Autopilot Alias

Add a compact alias note:

```markdown
For operating-alignment requests, follow the global Autopilot Operating
Alignment section: `/system-audit` owns the run, support gates stay bounded,
and the response must show the Orchestration Receipt. Do not create a domain
expert stack or real subagents unless explicitly authorized.
```

### 4. Global System-audit Skill

Add to `/Users/farricecain/.codex/skills/system-audit/SKILL.md`:

```markdown
Operating-alignment repair is part of System-audit ownership. When Farrice asks
for a unified Codex operating layer, global/workspace alignment, full-system
orchestration repair, automation cleanup, or expert/subagent coordination, use
System-audit as the owner and Autopilot/Virtuoso/Expert Composition as support
gates. Keep the global wrapper thin and defer to the canonical project workflow
and operating-alignment contract.
```

### 5. Global Source-command System-audit Alias

Add:

```markdown
Operating-alignment repair remains `/system-audit` owned. This alias should
load the global System-audit wrapper and the canonical Antigravity workflow,
then preserve the no-global-write, no-real-subagent, no-Google-Antigravity
boundary unless explicitly approved.
```

## Acceptance Criteria

The mirror is acceptable only if a fresh global invocation can produce:

- `meta_intent=operating-alignment`
- owner `/system-audit`
- composition owner `System Audit`
- no forced domain expert stack
- Orchestration Receipt visible
- risk block for global writes and real subagents
- Run Prompt when blocked
- explicit statement that Google Antigravity remains read-only

## Approval Gate

Before applying the mirror, Farrice should approve one of these paths:

1. **Narrow Mirror Now:** Apply only the five global text updates above, then
   run a global smoke prompt. This is reasonable because the mirror is thin and
   non-executable.
2. **Harden First:** Fix the hanging full control-plane verifier, rerun it, then
   apply the five global text updates.

Recommended path: **Narrow Mirror Now**, because the changes are global text
wrappers that point back to workspace proof rather than changing execution
scripts. Keep the broad verifier hardening as the next reliability item.

## Stop Condition

The stop condition was satisfied before application. Farrice approved the narrow
global mirror after reviewing the proposal. Future global writes still require
explicit approval.

