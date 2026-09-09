## Raw Intent Run Packet
- **Mode**: auto
- **Serves**: orphan (no active goal matched — flag only, execute fully) · **Tier**: T1 auto
- **Chosen route**: /knowledge-librarian (Knowledge Librarian)
- **Predicted need**: Route the request through /knowledge-librarian with enough intent clarity to act safely.
- **Center**: The /knowledge-librarian outcome, with proof and handoff included.
- **What good looks like**: /knowledge-librarian produces the requested artifact or action and verifies it.
- **Constraints**: Extend the existing control plane instead of adding a competing front door.
- **Missing inputs**: audience, success_standard
- **Questions that change execution**: None
- **Support gates**: /orchestrate, /routing-intelligence, /autopilot, /command-menu, /creative-quality-audit-system, /ground-truth, /design-to-code-execution

## Context Plan
- **Hot**: execution/raw_intent_run_packet.py, semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md, execution/co_creative_launchpad.py, execution/virtuoso_orchestration.py, .agent/workflows/autopilot.md
- **On demand**: .agent/workflows/source-to-skill-system.md, .agents/skills/source-command-virtuoso/SKILL.md, execution/routing_governor.py, execution/workflow_router.py, execution/plugin_readiness_audit.py
- **Cold**: full migrated command library, plugin marketplace files, global ~/.codex mirrors
- **Skip**: external writes, plugin marketplace edits, global ~/.codex writes during normal packet runs, real Codex subagents, destructive cleanup
- **Handoff**: Use /knowledge-librarian with the packet fields; load only the support gate needed for the next step.

## Composition Slots
- **Spine**: Knowledge Librarian — Own the final outcome through /knowledge-librarian.
- **Differentiator**: No extra stack; keep owner-led path — Add the non-obvious compound advantage only if it changes the output.
- **Mechanism**: /autopilot — Operationalize the route through the strongest support gate.
- **Craft**: owner integration pass — Make the final output read or behave as one system, not stitched parts.
- **Risk Gate**: /routing-intelligence — Catch broken trust, weak claims, overclaiming, or regression before closeout.

## Execution
- **Decision**: Running now
- **Approval needed**: No extra approval needed for safe local work; pause if a risk gate appears mid-run.
- **First safe action**: /knowledge-librarian Build The Homebase: unified hub command-center surface at / on the existing Readout OS (pulse_serve.py), three zones (Focus/Library/Launch), always-on launchd server, refresh action, nav registration
- **Operator run prompt**: /knowledge-librarian Build The Homebase: unified hub command-center surface at / on the existing Readout OS (pulse_serve.py), three zones (Focus/Library/Launch), always-on launchd server, refresh action, nav registration

## Verification
- **Checks**: python3 execution/verify_raw_intent_global_skill.py, python3 execution/verify_raw_intent_bridge_command.py, python3 execution/verify_raw_intent_run_packet.py, python3 execution/routing_governor.py evaluate "raw intent virtuoso bridge knowledge-librarian", python3 execution/verify_autopilot_runtime_preflight.py, python3 execution/verify_virtuoso_orchestration.py, python3 execution/verify_google_operator_core.py, python3 execution/verify_autopilot_routing.py, python3 execution/codex_harness_check.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate

## Plugin Packaging
- **Verdict**: deferred for `antigravity-operator-core`
- **Reason**: Package only after local cold-start proof passes for revenue, creative, system, and regression fixtures.
- **Boundary**: No plugin marketplace edits, no new plugin, and no unapproved global ~/.codex writes.
