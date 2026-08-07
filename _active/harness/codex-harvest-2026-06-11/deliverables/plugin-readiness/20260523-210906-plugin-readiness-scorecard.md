# Plugin Readiness Scorecard

Generated: 2026-05-23 21:09
Bundle: operator-core

## Verdict

- Bundle average: 88.1/100
- Package-now candidates: autopilot, mission, orchestrate, extraction-governor-agent, knowledge-librarian, health-check, routing-intelligence, self-evolve
- Recommended bundle: antigravity-operator-core

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `autopilot` | 20 | 20 | 14 | 15 | 15 | 15 | 99 | PACKAGE NOW | workflow/command/skill |
| `mission` | 20 | 18 | 13 | 15 | 15 | 12 | 93 | PACKAGE NOW | workflow/command/skill |
| `orchestrate` | 17 | 18 | 12 | 13 | 15 | 12 | 87 | PACKAGE NOW | workflow/command/skill |
| `extraction-governor-agent` | 16 | 18 | 12 | 14 | 15 | 13 | 88 | PACKAGE NOW | workflow/command/skill |
| `knowledge-librarian` | 15 | 17 | 12 | 14 | 15 | 12 | 85 | PACKAGE NOW | workflow/command/skill |
| `health-check` | 19 | 12 | 14 | 15 | 15 | 12 | 87 | PACKAGE NOW | workflow/command/skill |
| `routing-intelligence` | 14 | 14 | 13 | 14 | 15 | 13 | 83 | PACKAGE NOW | workflow/command/skill |
| `self-evolve` | 13 | 15 | 13 | 14 | 15 | 13 | 83 | PACKAGE NOW | workflow/command/skill |

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
