# Plugin Readiness Scorecard

Generated: 2026-05-21 09:59
Bundle: operator-core

## Verdict

- Bundle average: 72.1/100
- Package-now candidates: autopilot, mission, orchestrate, knowledge-librarian, extraction-governor-agent, routing-intelligence, health-check, self-evolve
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `autopilot` | 20 | 20 | 14 | 15 | 15 | 15 | 99 | PACKAGE NOW | workflow/command/skill |
| `mission` | 20 | 18 | 13 | 15 | 15 | 12 | 93 | PACKAGE NOW | workflow/command/skill |
| `orchestrate` | 17 | 18 | 12 | 13 | 15 | 12 | 87 | PACKAGE NOW | workflow/command/skill |
| `knowledge-librarian` | 15 | 17 | 12 | 14 | 15 | 12 | 85 | PACKAGE NOW | workflow/command/skill |
| `extraction-governor-agent` | 16 | 18 | 12 | 14 | 15 | 13 | 88 | PACKAGE NOW | workflow/command/skill |
| `routing-intelligence` | 14 | 14 | 13 | 14 | 15 | 13 | 83 | PACKAGE NOW | workflow/command/skill |
| `health-check` | 19 | 12 | 14 | 15 | 15 | 12 | 87 | PACKAGE NOW | workflow/command/skill |
| `self-evolve` | 13 | 15 | 13 | 14 | 15 | 13 | 83 | PACKAGE NOW | workflow/command/skill |
| `end-session` | 20 | 11 | 6 | 9 | 15 | 6 | 67 | IMPROVE FIRST | workflow/command/skill |
| `repeatability-spine` | 18 | 11 | 2 | 4 | 15 | 9 | 59 | KEEP AS WORKFLOW | workflow/command/skill |
| `source-to-skill-system` | 4 | 9 | 9 | 6 | 15 | 2 | 45 | KEEP AS WORKFLOW | workflow/command/skill |
| `plugin-readiness-audit` | 4 | 3 | 4 | 6 | 11 | 0 | 28 | REFERENCE ONLY | workflow/command/no-skill |
| `system-efficiency-benchmark` | 4 | 6 | 6 | 4 | 11 | 2 | 33 | REFERENCE ONLY | workflow/command/no-skill |

## Plugin Acceptance Tests

1. Direct invocation names the plugin or bundled skill.
2. Natural-language request triggers the operating layer without magic words.
3. Missing information produces one small question or explicit assumptions.
4. Local paths resolve after installation from the repo marketplace.
5. A fresh Codex thread can use the plugin after restart.

## Before/After Proof Protocol

Use the same raw request before and after installation:

> I have messy context and do not know which Antigravity workflow to use. Route it, state the plan, and start the first safe action.

Before packaging, record whether the agent asks the user to reconstruct the system. After packaging, record whether it loads the operator-core route and names the checks without extra setup.

## Notes

- Scores are local decision support, not a public quality claim.
- A plugin should only wrap stable workflow behavior; it should not replace the existing Antigravity routers.
- Add MCP, apps, or hooks only after the base plugin can install and trigger.
