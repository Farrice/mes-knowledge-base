## Raw Intent Run Packet
- **Mode**: auto
- **Serves**: revenue-5k-incumbency (target match: from, content) · **Tier**: T1 auto
- **Chosen route**: /autopilot (Autopilot)
- **Predicted need**: Route the request through /autopilot with enough intent clarity to act safely.
- **Center**: The /autopilot outcome, with proof and handoff included.
- **What good looks like**: /autopilot produces the requested artifact or action and verifies it.
- **Constraints**: Extend the existing control plane instead of adding a competing front door., Stop before external, paid, destructive, global, public, connector-write, or real-subagent action.
- **Missing inputs**: audience, success_standard
- **Questions that change execution**: None
- **Support gates**: /orchestrate, /routing-intelligence, /knowledge-librarian, /first-10k, /revenue-offer-agent, /client-acquire, /zero-to-client-sprint, /service-first-productization, /capability-graph, /run-receipt, /plugin-forge
- **Container decision**: continue - Preparation can continue safely, but the next state-changing action crosses an approval boundary.
- **Capability recommendation**: Prepare the publish or send action, then request approval.
- **Why now**: The work is ready to approach an external state change.
- **What I can do**: Complete the local draft/checklist and stop before the external action.
- **Approval boundary**: Explicit approval is required before publish, send, outreach, connector write, paid, destructive, or global action.

## Context Plan
- **Hot**: execution/raw_intent_run_packet.py, semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md, execution/co_creative_launchpad.py, execution/virtuoso_orchestration.py, .agent/workflows/autopilot.md
- **On demand**: .agent/workflows/source-to-skill-system.md, .agents/skills/source-command-virtuoso/SKILL.md, execution/routing_governor.py, execution/workflow_router.py, execution/plugin_readiness_audit.py
- **Cold**: full migrated command library, plugin marketplace files, global ~/.codex mirrors
- **Skip**: external writes, plugin marketplace edits, global ~/.codex writes during normal packet runs, real Codex subagents, destructive cleanup
- **Handoff**: Use /autopilot with the packet fields; load only the support gate needed for the next step.

## Composition Slots
- **Spine**: Autopilot — Own the final outcome through /autopilot.
- **Differentiator**: Raw Intent Virtuoso Bridge — Translate rough operator language into a runnable Codex packet before normal execution.
- **Mechanism**: /orchestrate — Turn packet fields into route, gates, context plan, and first safe action.
- **Craft**: /virtuoso trace — Make the route, composition, plugin surface, and proof visible as one coherent handoff.
- **Risk Gate**: /routing-intelligence — Prevent generic advice, plugin-first drift, external writes, and unrelated creative-route capture.

## Execution
- **Decision**: Blocked by risk
- **Approval needed**: Approve the named risk gate before execution: publishing/external
- **First safe action**: /autopilot compile this raw intent into a run packet, then execute the first safe local action: ignite realtor content-pack subscription per income-master-2026-08 Pick A: hybrid vertical lock (general monthly agent pack, listing-content flagship), month-1 pack from Jen engine golden refs, Stripe-ready storefront package, 50-contact outreach list
- **Operator run prompt**: /autopilot compile this raw intent into a run packet, then execute the first safe local action: ignite realtor content-pack subscription per income-master-2026-08 Pick A: hybrid vertical lock (general monthly agent pack, listing-content flagship), month-1 pack from Jen engine golden refs, Stripe-ready storefront package, 50-contact outreach list

## Verification
- **Checks**: python3 execution/verify_raw_intent_global_skill.py, python3 execution/verify_raw_intent_bridge_command.py, python3 execution/verify_raw_intent_run_packet.py, python3 execution/routing_governor.py evaluate "raw intent virtuoso bridge autopilot", python3 execution/verify_autopilot_runtime_preflight.py, python3 execution/verify_virtuoso_orchestration.py, python3 execution/verify_google_operator_core.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate, python3 execution/capability_graph.py --json, python3 execution/codex_harness_check.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate

## Plugin Packaging
- **Verdict**: deferred for `antigravity-operator-core`
- **Reason**: Package only after local cold-start proof passes for revenue, creative, system, and regression fixtures.
- **Boundary**: No plugin marketplace edits, no new plugin, and no unapproved global ~/.codex writes.
