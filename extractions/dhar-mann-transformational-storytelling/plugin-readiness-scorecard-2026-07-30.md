# Plugin Readiness Scorecard

Generated: 2026-07-30 18:50
Bundle: operator-core

## Verdict

- Bundle average: 54.0/100
- Package-now candidates: None
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `dhar-transformational-content-factory` | 20 | 9 | 0 | 6 | 15 | 4 | 54 | KEEP AS WORKFLOW | workflow/command/skill |

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
