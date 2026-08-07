---
name: "source-command-routing-intelligence"
description: "View routing analytics dashboard"
---

# source-command-routing-intelligence

Use this skill when the user asks to run the migrated source command
`routing-intelligence`, view routing analytics, inspect route feedback, check
the routing scoreboard, or run `source-command-routing-intelligence`.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/routing-intelligence.md` as the
canonical behavior source. It must stay a thin compatibility wrapper and
preserve:

- read-only routing analytics by default
- `routing_intelligence.py scoreboard` as the first dashboard surface
- focused read-only subcommands for utilization, unused, domain-dist, top-combos, and underperforming
- `misroute` writes only when the user explicitly reports a wrong route or asks to record a correction
- no auto-optimization, workflow mutation, Notion sync, Mission mutation, cleanup, destructive action, or global mirror unless explicitly requested
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- no competing behavior contract

## Command Template

Read and execute the workflow at `.agent/workflows/routing-intelligence.md` — View routing analytics dashboard
