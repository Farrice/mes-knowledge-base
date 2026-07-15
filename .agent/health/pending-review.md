# Pending Review — removal/archive proposals (nothing executes without a human yes)

## PR-2026-07-15-V01
- proposed: 2026-07-15
- action: archive
- target: execution/verify_tiered_agent_routing.py
- reason: tests a tiered-routing framework routing_audit never implemented (build_tiered_routing_report does not exist in any git history) AND hardcodes 169 agents (there are 223) — rebuild-to-spec or retire
- status: pending

## PR-2026-07-15-V02
- proposed: 2026-07-15
- action: archive
- target: execution/verify_attention_hijack_hooks.py
- reason: expects .claude/agents/attention-hijack-hook-auditor.md — directly contradicts the BINDING 'No Claude Code Subagents' feedback (never .claude/agents/); verifier enforces a forbidden pattern
- status: pending

## PR-2026-07-15-V03
- proposed: 2026-07-15
- action: archive
- target: execution/verify_kimi_swarm.py
- reason: .agent/workflows/kimi-swarm.md never existed in git history; either the workflow should be built (Kimi K2.6 integration revisit is already overdue) or this verifier retires
- status: pending

## PR-2026-07-15-V04
- proposed: 2026-07-15
- action: archive
- target: execution/verify_codex_indexes.py
- reason: expects semantic_libraries/antigravity/indexes/codex-subagent-candidates.md which never existed in git history — aspirational index generation that was never wired
- status: pending

## PR-2026-07-15-V05
- proposed: 2026-07-15
- action: archive
- target: execution/verify_agentic_engineering_loop_contract.py
- reason: source-evidence file extractions/video-context/PzVV4X37ihg/analysis.md never committed anywhere — evidence unrecoverable; re-run the video extraction or retire
- status: pending

## PR-2026-07-15-V06
- proposed: 2026-07-15
- action: archive
- target: execution/verify_goal_loop_maintenance_contract.py
- reason: source-evidence extractions/video-context/5xrjO38WUYY/video-context-ledger.md never committed — same class as above
- status: pending

## PR-2026-07-15-V07
- proposed: 2026-07-15
- action: archive
- target: execution/verify_behavior_changing_extraction_contract.py
- reason: _active/sam-parr-copywriting-os/06-before-after-proof-lab.md never committed — proof-lab was local-only or never built; rebuild the proof lab or retire
- status: pending

## PR-2026-07-15-V08
- proposed: 2026-07-15
- action: archive
- target: execution/verify_buyer_trigger_research_contract.py
- reason: expects a meg-heckman research workflow file that never existed in git — contract written ahead of the build
- status: pending

## PR-2026-07-15-V09
- proposed: 2026-07-15
- action: archive
- target: execution/verify_intent_memory_contract.py
- reason: expects autopilot.md to document 'execution/intent_memory.py verify' — term never durably existed in autopilot.md; ADOPT the contract into autopilot.md or retire the verifier
- status: pending

## PR-2026-07-15-V10
- proposed: 2026-07-15
- action: archive
- target: execution/verify_steering_compass.py
- reason: expects .agents/cold-skills/source-command-wrappers/ (Codex-side cold-skill layer) which is absent from this repo and unrecoverable from git — rebuild wrappers in a Codex session via sync_operator_core_* or retire; same class: verify_convene, verify_deep_research_os
- status: pending
