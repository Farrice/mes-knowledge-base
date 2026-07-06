---
description: Check which Antigravity systems are active vs dormant
---

# /health-check — System Activation Health

Run a health check on all Antigravity systems to see what's active, what's dormant, and what needs attention.

## Operator Core Alignment

This workflow is the canonical source of truth for Health-check behavior.
Global and local Health-check wrappers must stay thin compatibility wrappers
that point back here, not competing behavior contracts.

Preserve these invariants:

- `/health-check` is read-only by default.
- Start with `python3 execution/harness_status.py --plain` for the trust/status surface.
- Add `python3 execution/savant_control_room.py --plain` for the compact control-room view.
- Add `python3 execution/operator_core_fast_proof.py --plain` for fast Operator Core proof.
- Then run `python3 execution/system_health.py --quick` for activation and feedback-loop detail.
- Include `python3 execution/operator_core_status.py --plain` as the compact Operator Core alignment closeout.
- Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested.
- Mission remains read-only unless `python3 execution/verify_mission_activation_contract.py` fails.
- Route system-failure or drift-audit language to `/autopilot` or `/system-audit`; use `/health-check` for explicit status and health questions.
- Real Codex subagents require explicit authorization.

## Usage
```
health-check
```

## Steps

### 1. Run the Health Check Script
```bash
python3 execution/harness_status.py --plain
python3 execution/savant_control_room.py --plain
python3 execution/operator_core_fast_proof.py --plain
python3 execution/system_health.py --quick
python3 execution/operator_core_status.py --plain
```

### 2. Present the Report
Display the health report to the user with clear status indicators:
- **ACTIVE**: System is firing and producing data
- **DORMANT**: System has never activated or hasn't fired recently
- **BLOCKED**: System is waiting for upstream dependencies
- **READY**: System has met its activation conditions and can be run

### 3. Recommend One Safe Next Action
For any CRITICAL or DORMANT systems, explain:
- What the system does
- Why it's not firing
- What specific read-only proof or explicitly approved next step activates it

Do not write reports, sync Notion, optimize routes, mutate Mission, or perform cleanup unless explicitly requested.
