---
name: "source-command-health-check"
description: "Run the read-only Health-check status surface for harness trust, activation health, routing probes, and feedback-loop readiness"
---

# source-command-health-check

Use this skill when the user asks to run the migrated source command `health-check`, check harness status, inspect what is working/stale/broken, view activation health, or run `source-command-health-check`.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/health-check.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- read-only status by default
- `harness_status.py --plain` as the first trust/status surface
- `system_health.py --quick` as the activation and feedback-loop detail layer
- `operator_core_status.py --plain` as the compact Operator Core alignment closeout
- no report writes, Notion sync, route optimization, Mission mutation, cleanup, or destructive action unless explicitly requested
- Mission remains read-only unless `verify_mission_activation_contract.py` fails
- system-failure or drift-audit language routes to `/autopilot` or `/system-audit`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/health-check.md` — read-only harness status, activation health, routing probes, and feedback-loop readiness
