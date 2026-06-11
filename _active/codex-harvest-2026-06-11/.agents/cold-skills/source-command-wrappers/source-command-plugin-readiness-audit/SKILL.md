---
name: "source-command-plugin-readiness-audit"
description: "Run plugin-readiness-audit to score workflow-family plugin readiness, fresh-thread reliability, packaging tradeoffs, and whether Antigravity workflows should stay prompts, workflows, skills, companion skills, repo-local plugins, global plugins, MCP/app connectors, or deterministic hooks."
---

# source-command-plugin-readiness-audit

Use this skill when the user asks to run `plugin-readiness-audit`, evaluate plugin packaging, decide whether a workflow family should become a Codex plugin, stay a skill/workflow, pass fresh-thread plugin tests, audit skill bloat versus plugin readiness, or apply the Workflow Packaging Ladder.

## Command Template

Read and execute the workflow at `.agent/workflows/plugin-readiness-audit.md` - Score workflows for Codex plugin packaging readiness and produce a plugin candidate scorecard
