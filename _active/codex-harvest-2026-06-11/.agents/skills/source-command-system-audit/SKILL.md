---
name: "source-command-system-audit"
description: "Control-plane audit for Autopilot, routing, bridges, activation, telemetry, and firing behavior"
---

# source-command-system-audit

Use this skill when the user asks to run the migrated source command `system-audit`, says the system is broken, says things are not firing, asks why Autopilot is not working, or wants a control-plane audit of routing and activation behavior.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/system-audit.md` as the canonical behavior source.
It must stay a thin compatibility wrapper and preserve:

- control-plane audit and repair for broken, drifted, cluttered, or not-firing harness behavior
- read-only proof first across routing, bridge, activation, telemetry, cohesion, and verifier checks
- structural health is distinct from firing behavior
- repairs are severity-ranked, verifier-backed, and workspace-local by default
- global `~/.codex` edits require explicit approval
- external writes, publishing, connector writes, destructive cleanup, broad archive/delete, and Mission mutation require explicit approval and proof
- Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair
- status reads route to `/health-check`, routing analytics to `/routing-intelligence`, raw/broad triage to `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/system-audit.md` — Control-plane audit for Autopilot, routing, bridges, activation, telemetry, and firing behavior
