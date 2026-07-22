## Raw Intent Run Packet
- **Mode**: auto
- **Serves**: revenue-5k-incumbency (thread match: linkedin-launch) · **Tier**: T2 waiting
- **Chosen route**: /first-10k (First 10K Revenue System)
- **Predicted need**: Convert taste and quality ambition into concrete acceptance criteria before producing work.
- **Center**: A result that matches Farrice's taste bar, not merely a technically complete output.
- **What good looks like**: The output can be judged against explicit quality criteria, not vague excellence language.
- **Constraints**: Turn taste language into acceptance criteria before drafting or building., Stop before external, paid, destructive, global, public, connector-write, or real-subagent action.
- **Missing inputs**: success_standard
- **Questions that change execution**: What would make this excellent enough to keep using?
- **Support gates**: /revenue-offer-agent, /client-acquire, /service-first-productization, /publishable-copy-gate, /red-team-agent

## Context Plan
- **Hot**: execution/raw_intent_run_packet.py, semantic_libraries/antigravity/primitives/raw-intent-virtuoso-bridge-contract.md, execution/co_creative_launchpad.py, execution/virtuoso_orchestration.py, .agent/workflows/autopilot.md
- **On demand**: .agent/workflows/source-to-skill-system.md, .agents/skills/source-command-virtuoso/SKILL.md, execution/routing_governor.py, execution/workflow_router.py, execution/plugin_readiness_audit.py
- **Cold**: full migrated command library, plugin marketplace files, global ~/.codex mirrors
- **Skip**: external writes, plugin marketplace edits, global ~/.codex writes during normal packet runs, real Codex subagents, destructive cleanup
- **Handoff**: Use /first-10k with the packet fields; load only the support gate needed for the next step.

## Composition Slots
- **Spine**: First 10K Revenue System — Own the final outcome through /first-10k.
- **Differentiator**: Raw Intent Virtuoso Bridge — Translate rough operator language into a runnable Codex packet before normal execution.
- **Mechanism**: /revenue-offer-agent — Turn packet fields into route, gates, context plan, and first safe action.
- **Craft**: /virtuoso trace — Make the route, composition, plugin surface, and proof visible as one coherent handoff.
- **Risk Gate**: /publishable-copy-gate — Prevent generic advice, plugin-first drift, external writes, and unrelated creative-route capture.

## Execution
- **Decision**: Blocked by risk
- **Approval needed**: Approve the named risk gate before execution: publishing/external
- **First safe action**: /first-10k Week 1 LinkedIn launch content for the Proof-to-Market offer — posts that feel like receipts not promises, aimed at supplement and performance brand founders, ready to publish Monday
- **Operator run prompt**: /first-10k Week 1 LinkedIn launch content for the Proof-to-Market offer — posts that feel like receipts not promises, aimed at supplement and performance brand founders, ready to publish Monday

## Verification
- **Checks**: python3 execution/verify_raw_intent_global_skill.py, python3 execution/verify_raw_intent_bridge_command.py, python3 execution/verify_raw_intent_run_packet.py, python3 execution/routing_governor.py evaluate "raw intent virtuoso bridge first-10k", python3 execution/verify_autopilot_runtime_preflight.py, python3 execution/verify_virtuoso_orchestration.py, python3 execution/verify_google_operator_core.py, python3 execution/verify_autopilot_routing.py, python3 execution/routing_intelligence.py scoreboard, python3 execution/codex_harness_check.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate

## Plugin Packaging
- **Verdict**: deferred for `antigravity-operator-core`
- **Reason**: Package only after local cold-start proof passes for revenue, creative, system, and regression fixtures.
- **Boundary**: No plugin marketplace edits, no new plugin, and no unapproved global ~/.codex writes.
