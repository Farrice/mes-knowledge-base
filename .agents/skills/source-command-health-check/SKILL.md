---
name: "source-command-health-check"
description: "Check which Antigravity systems are active vs dormant"
---

# source-command-health-check

Use this skill when the user asks to run the migrated source command `health-check`.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/health-check.md` as the canonical
behavior source. It must stay a thin compatibility wrapper with no competing
behavior contract.

Verification phrases: canonical behavior source; real Codex subagents require explicit authorization; no competing behavior contract.

Preserve the current Health-check contract: read-only status by default;
`harness_status.py --plain` first; `system_health.py --quick` second;
`operator_core_status.py --plain` as the compact Operator Core alignment
closeout; no report writes, Notion sync, route optimization, Mission mutation,
cleanup, or destructive action unless explicitly requested; Mission remains
read-only unless `verify_mission_activation_contract.py` fails; system-failure
or drift-audit language routes to `/autopilot` or `/system-audit`; and real
Codex subagents require explicit authorization.

## Command Template

Read and execute the workflow at `.agent/workflows/health-check.md` — Check which Antigravity systems are active vs dormant
