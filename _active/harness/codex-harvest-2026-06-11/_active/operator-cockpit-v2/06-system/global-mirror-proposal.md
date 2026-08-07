# Operator Cockpit V2 Global Mirror Proposal

## Purpose

Mirror the local Operator Cockpit V2 behavior into global Codex wrappers only after local proof passes and Farrice explicitly approves the global write.

## Local Source Of Truth

- `CODEX.md`
- `.agent/workflows/autopilot.md`
- `.agent/workflows/system-audit.md`
- `.agent/workflows/health-check.md`
- `execution/operator_cockpit.py`
- `execution/autopilot_runtime_preflight.py`
- `execution/routing_governor.py`
- `execution/co_creative_launchpad.py`
- `execution/recommend_stack.py`

## Candidate Global Surfaces

- `/Users/farricecain/.codex/AGENTS.md`
- `/Users/farricecain/.codex/skills/autopilot/SKILL.md`
- `/Users/farricecain/.codex/skills/source-command-autopilot/SKILL.md`
- `/Users/farricecain/.codex/skills/system-audit/SKILL.md`
- `/Users/farricecain/.codex/skills/source-command-system-audit/SKILL.md`
- `/Users/farricecain/.codex/skills/health-check/SKILL.md`
- `/Users/farricecain/.codex/skills/source-command-health-check/SKILL.md`

## Mirror Content

- Non-trivial work should start with an Intent Confidence Packet.
- Operator Cockpit V2 should be the command-backed pre-action surface for meaningful work.
- Engineering debt, user failure modes, bottlenecks, safeguards not working, Codex/Claude intent mismatch, retrieval overload, and full-arsenal access concerns route to `/system-audit`.
- The intelligence arsenal remains available on demand; irrelevant expert stacks are suppressed until a bounded support slot is justified.
- Local friction capture may record operator struggle, retrieval failure, stale proof, misroutes, stuck verifiers, unclear approval, and unanswered confidence-packet questions.
- Global writes, Google Antigravity edits, external writes, destructive cleanup, Mission mutation, publishing, and real Codex subagents still require explicit approval.

## Required Proof Before Approval

- `python3 execution/verify_operator_cockpit.py`
- `python3 execution/verify_autopilot_runtime_preflight.py`
- `python3 execution/verify_system_control_plane.py`
- `python3 execution/verify_autopilot_routing.py`
- `python3 execution/verify_agent_arsenal_routing.py`
- `python3 execution/verify_savant_control_room.py`
- `python3 execution/verify_artifact_router.py`
- `python3 execution/friction_ledger.py verify`
- `python3 execution/run_receipt.py --verify`
- `python3 execution/codex_live_surface_audit.py --strict`
- `python3 execution/codex_harness_check.py`

## Approval Boundary

Do not edit global `~/.codex` surfaces from this proposal. After local proof passes, ask Farrice for explicit approval to apply a narrow global mirror.
