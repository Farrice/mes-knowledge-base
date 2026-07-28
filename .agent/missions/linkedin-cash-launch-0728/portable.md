## Raw Intent Run Packet
- **Mode**: auto
- **Serves**: orphan (no active goal matched — flag only, execute fully) · **Tier**: T1 auto
- **Chosen route**: /first-10k (First 10K Revenue System)
- **Predicted need**: Route the request through /first-10k with enough intent clarity to act safely.
- **Center**: A source-led answer with claims, confidence, and unresolved gaps separated.
- **What good looks like**: /first-10k produces the requested artifact or action and verifies it.
- **Constraints**: State assumptions and keep the first action local, reversible, and verifiable.
- **Missing inputs**: audience, success_standard
- **Questions that change execution**: None
- **Support gates**: /revenue-offer-agent, /client-acquire, /service-first-productization, /publishable-copy-gate, /red-team-agent, /research-intelligence-agent, /deep-research, /research-swarm, /parallel-research, /research-quality-gate

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
- **Decision**: Running now
- **Approval needed**: No extra approval needed for safe local work; pause if a risk gate appears mid-run.
- **First safe action**: /first-10k LinkedIn cash launch: fresh deep research (demand/pricing, ICP, zero-start momentum), wargame the teardown-to-sprint offer vs $500-2K/7-14d cash goal, 14-day launch plan, ICP battle card
- **Operator run prompt**: /first-10k LinkedIn cash launch: fresh deep research (demand/pricing, ICP, zero-start momentum), wargame the teardown-to-sprint offer vs $500-2K/7-14d cash goal, 14-day launch plan, ICP battle card

## Verification
- **Checks**: python3 execution/verify_raw_intent_global_skill.py, python3 execution/verify_raw_intent_bridge_command.py, python3 execution/verify_raw_intent_run_packet.py, python3 execution/routing_governor.py evaluate "raw intent virtuoso bridge first-10k", python3 execution/verify_autopilot_runtime_preflight.py, python3 execution/verify_virtuoso_orchestration.py, python3 execution/verify_google_operator_core.py, python3 execution/verify_deep_research_os.py, python3 execution/research_router.py --health, python3 execution/research_quality_gate.py validate [final_report.md] --strict --source-ledger [source_ledger.md], python3 execution/research_quality_gate.py, python3 execution/codex_harness_check.py, python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate

## Plugin Packaging
- **Verdict**: deferred for `antigravity-operator-core`
- **Reason**: Package only after local cold-start proof passes for revenue, creative, system, and regression fixtures.
- **Boundary**: No plugin marketplace edits, no new plugin, and no unapproved global ~/.codex writes.
