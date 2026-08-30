## Raw Intent Run Packet
- **Mode**: auto
- **Serves**: orphan (no active goal matched — flag only, execute fully) · **Tier**: T2 waiting
- **Chosen route**: /first-10k (First 10K Revenue System)
- **Predicted need**: Convert taste and quality ambition into concrete acceptance criteria before producing work.
- **Center**: A result that matches Farrice's taste bar, not merely a technically complete output.
- **What good looks like**: The output can be judged against explicit quality criteria, not vague excellence language.
- **Constraints**: Extend the existing control plane instead of adding a competing front door., Turn taste language into acceptance criteria before drafting or building., Stop before external, paid, destructive, global, public, connector-write, or real-subagent action.
- **Missing inputs**: success_standard
- **Questions that change execution**: What would make this excellent enough to keep using?
- **Support gates**: /revenue-offer-agent, /client-acquire, /service-first-productization, /publishable-copy-gate, /red-team-agent, /capability-graph, /run-receipt, /plugin-forge
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
- **First safe action**: /first-10k Package what we built for Jen (listing content engine, shoot sheets, teleprompter packs, reels scripts, SEND packages, compliance pack) into a repeatable $200 introductory content/messaging/positioning offer for three agents on her team. Deliverable: creative brief defining the exact offer + repeatable delivery process outline. Goal: $300-600 in 30 days, proof-of-concept that pulls Jen on board.
- **Operator run prompt**: /first-10k Package what we built for Jen (listing content engine, shoot sheets, teleprompter packs, reels scripts, SEND packages, compliance pack) into a repeatable $200 introductory content/messaging/positioning offer for three agents on her team. Deliverable: creative brief defining the exact offer + repeatable delivery process outline. Goal: $300-600 in 30 days, proof-of-concept that pulls Jen on board.

## Verification
- **Checks**: python3 execution/verify_raw_intent_global_skill.py, python3 execution/verify_raw_intent_bridge_command.py, python3 execution/verify_raw_intent_run_packet.py, python3 execution/routing_governor.py evaluate "raw intent virtuoso bridge first-10k", python3 execution/verify_autopilot_runtime_preflight.py, python3 execution/verify_virtuoso_orchestration.py, python3 execution/verify_google_operator_core.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate, python3 execution/capability_graph.py --json, python3 execution/codex_harness_check.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate

## Plugin Packaging
- **Verdict**: deferred for `antigravity-operator-core`
- **Reason**: Package only after local cold-start proof passes for revenue, creative, system, and regression fixtures.
- **Boundary**: No plugin marketplace edits, no new plugin, and no unapproved global ~/.codex writes.
