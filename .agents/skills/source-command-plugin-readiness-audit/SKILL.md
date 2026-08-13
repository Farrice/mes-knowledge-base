---
name: "source-command-plugin-readiness-audit"
description: "Decide whether a workflow family should remain a workflow/skill or become a Codex plugin."
---

# source-command-plugin-readiness-audit

Use this compatibility skill when the user invokes `/plugin-readiness-audit` or asks whether workflows should become plugins.

## Canonical Source

Read and execute `.agent/workflows/plugin-readiness-audit.md`. The methodology lives in `skills/plugin-readiness-audit/`.

This wrapper must remain thin and must not create a competing packaging policy.
