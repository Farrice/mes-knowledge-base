---
name: "source-command-autopilot"
description: "Intent-to-outcome front door for raw context, route choice, safe workspace-local execution, proof, and risk-gated judgment"
---

# source-command-autopilot

Use this skill when the user asks to run `/autopilot`, drops raw thoughts, wants
the system to choose the best workflow/skill stack, wants fewer manual passes,
needs route traceability, or wants the Antigravity harness to execute safe local
work and report proof.

Autopilot is now safe execute-by-default for Codex Antigravity workspace-local
work. It must emit Intent Lock, Autopilot Trace, Execution Decision, Chosen Path,
Capability Graph, Execution Plan, Run Prompt, Run Receipt, Friction Ledger, and
Approval/Risk Gate. The Execution Decision is one of `Running now`, `Needs
judgment`, `Blocked by risk`, or `Plan only`.

Pause only for real risk or judgment gates: external/public action, publishing,
outreach, paid or budget-sensitive tools, destructive edits, global `~/.codex`
changes, `/Users/farricecain/Google Antigravity` edits, connector writes, real
Codex subagents without explicit delegation, low-clarity execution, or explicit
`--plan`/`--menu` mode.

When blocked, include a copy-paste Run Prompt. Plugin packaging requests must go
through `/plugin-readiness-audit` and the helper/script -> workflow -> skill
wrapper -> plugin candidate -> plugin ladder before a plugin is recommended.

## Operator Core Alignment

This project wrapper follows `.agent/workflows/autopilot.md` as the canonical behavior source.
It must preserve `3 Next Prompts`, `Operator Lesson`,
`Next-time prompt`, `Subagent worth it?`, `Reuse hook`, and the rule that real
Codex subagents require explicit authorization.

## Command Template


Read and execute the workflow at `.agent/workflows/autopilot.md` - Intent-to-outcome front door for route choice, safe execution, proof, and risk-gated judgment.
