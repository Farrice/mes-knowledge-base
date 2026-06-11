---
name: "source-command-kimi-swarm"
description: "Cold bridge for /kimi-swarm packet compiler"
---

# source-command-kimi-swarm

Use this skill when the user asks to run the migrated source command `kimi-swarm`.

## Command Template

Read and execute the workflow at `.agent/workflows/kimi-swarm.md`.

This wrapper is intentionally cold-quarantined. `/kimi-swarm` is a thin bridge
behind `/virtuoso`, `/deep-research-os`, and `/convene`.
