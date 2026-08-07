# System: Control Plane Audit - Autopilot Firing Repair

## Summary

This audit repaired a real control-plane failure: structural verifiers were passing while natural broken-system phrases still routed to unrelated specialist workflows.

The accepted architecture remains intact:

- `/autopilot` is the front door for raw context, intent lock, routing, visible trace, and safe execution.
- `/system-audit` is now the practical audit route for "built but not firing," competing defaults, broken routing, bridge drift, activation telemetry, and Autopilot behavior repair.
- `/orchestrate` remains the menu backend.
- `/mission` remains the persistent governance backend.

## Baseline Findings

| Severity | Symptom | Cause | Affected Surface | Fix | Verifier | Boundary |
|----------|---------|-------|------------------|-----|----------|----------|
| P0 | `things are not working` routed to `/godin-better-not-louder` and other unrelated commands | No system-failure lane existed above generic keyword rank | `routing_governor.py`, `command_menu.py`, `workflow_router.py` | Added system-failure intent detection, control-plane route bonuses, and governor explanation | `verify_system_control_plane.py` | workspace-only |
| P1 | `system audit` ranked `/kcs-system-audit` above `/system-audit` | Content-system audit matched generic audit terms better than the real control-plane route | Router scoring | Added query-aware `/system-audit` priority for audit intent and demoted `kcs-*` for system-failure lane | `verify_system_control_plane.py` | workspace-only |
| P1 | Existing checks passed while real conversation behavior failed | Verifiers tested file presence and selected canned routes, not the user’s friction phrases | Verification suite | Added golden query matrix covering broken-system, audit, Autopilot complaint, revenue, and skill-system intents | `verify_system_control_plane.py` | workspace-only |
| P1 | `/system-audit` was a shallow duplicate-file checklist | Audit workflow did not test authority, bridges, routing parity, activation, or telemetry | `.agent/workflows/system-audit.md` | Rebuilt it as a control-plane audit workflow with authority map, bridge map, activation map, issue ledger, and repair proof | Contract text check in `verify_system_control_plane.py` | workspace-only |
| P2 | Mandatory `intent-pipeline.md` was marked zombie | Protocol tracker did not reset review date on activation and the protocol had count 0 | `protocol_tracker.py`, directives usage tracking | Activation now resets review window; intent, session-state, and quality protocols were activated for this repair | Protocol activation check in `verify_system_control_plane.py` | workspace-only |
| P2 | Autopilot contract did not explicitly mark menu-only output as failure | Workflow allowed trace and route visibility but did not make first-action behavior strict enough | `.agent/workflows/autopilot.md` | Added menu-stop failure rule, system-failure lane behavior, and control-plane proof requirements | Contract text check in `verify_system_control_plane.py` | workspace-only |

## Repairs Applied

- Added `execution/control_plane_golden_queries.json`.
- Added `execution/verify_system_control_plane.py`.
- Added system-failure detection and bonuses to `execution/routing_governor.py`.
- Wired the new lane into `execution/command_menu.py` and `execution/workflow_router.py`.
- Rebuilt `.agent/workflows/system-audit.md` as the control-plane audit route.
- Tightened `.agent/workflows/autopilot.md` so meaningful work must choose a route and begin the first safe action instead of stopping at a menu.
- Updated `CODEX.md` so `/system-audit` is a hot control-plane route and the new verifier is part of the standard proof set.
- Updated `.agents/skills/source-command-system-audit/SKILL.md` so broken-system language discovers the audit route.
- Fixed `execution/protocol_tracker.py` so a deliberate protocol activation resets its 30-day review window.
- Activated `intent-pipeline.md`, `session-state-protocol.md`, and `quality_gate.md` for this repair cycle.

## Regression Proof

The new verifier now proves:

- `things are not working` -> `/autopilot` across menu, router, and governor.
- `feels broken cluttered slow` -> `/autopilot` across menu, router, and governor.
- `system audit` -> `/system-audit` across menu, router, and governor.
- `Autopilot is not doing what it is supposed to do...planning mode` -> `/autopilot`.
- `full system audit...not firing...competing defaults...autopilot` -> `/system-audit`.
- Skill-system and revenue lanes still route to their intended stacks.
- Control-plane commands have workflow, Codex skill, and source command bridge coverage.
- Autopilot and System Audit workflows contain the required behavior contract.
- Mandatory protocols have activation evidence.

## Remaining Watch Items

- Routing intelligence still has limited feedback data, so it can observe usage but cannot yet learn much from positive/negative outcomes.
- Skill Evolution and cross-pollination are still gated by performance-entry volume.
- Global `~/.codex` Autopilot mirroring was intentionally not changed in this repair. If workspace behavior holds, the next supervised step is to mirror only the necessary global language.

## Fresh-Session Smoke Test

Use this exact prompt in a fresh Codex session:

```text
Autopilot is not doing what it is supposed to do. Things we built are not firing, and I only get good output in planning mode. Figure out the route and start the safest repair step.
```

Expected behavior:

- Starts with Intent Lock and Clarity Score.
- Shows route/trace or chosen path.
- Chooses `/autopilot` with `/system-audit`, `/routing-intelligence`, and `/health-check` as support routes.
- Does not dump a command menu.
- Starts a safe local audit or asks only for an approval that truly changes execution.
