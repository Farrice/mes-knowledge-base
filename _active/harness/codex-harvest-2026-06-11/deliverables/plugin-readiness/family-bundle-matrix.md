# Plugin Readiness Bundle Matrix



Generated: 2026-05-09 09:15



| Bundle | Avg | Package Now | Improve First | Missing Workflows | Recommendation |

|---|---:|---:|---:|---:|---|

| `client` | 27.9 | 0 | 0 | 0 | keep as workflows |

| `content` | 26.9 | 0 | 0 | 0 | keep as workflows |

| `creative` | 31.9 | 0 | 0 | 0 | keep as workflows |

| `extraction` | 41.6 | 2 | 0 | 0 | keep as workflows |

| `operator-core` | 88.1 | 8 | 0 | 0 | package candidate |

| `revenue` | 28.9 | 0 | 0 | 0 | keep as workflows |

| `system` | 61.7 | 7 | 0 | 0 | keep as workflows |



## Bundle Details



# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
Bundle: client

## Verdict

- Bundle average: 27.9/100
- Package-now candidates: None
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `client-delivery-agent` | 4 | 11 | 11 | 0 | 15 | 2 | 43 | REFERENCE ONLY | workflow/command/skill |
| `client-acquire` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `client-interview` | 4 | 3 | 0 | 0 | 15 | 0 | 22 | REFERENCE ONLY | workflow/command/skill |
| `draft-proposal` | 4 | 11 | 4 | 4 | 15 | 2 | 40 | REFERENCE ONLY | workflow/command/skill |
| `no-portfolio-client-landing` | 4 | 9 | 4 | 4 | 15 | 0 | 36 | REFERENCE ONLY | workflow/command/skill |
| `blue-chip-client` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `client-conversion` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `24-assets-client-audit` | 4 | 0 | 0 | 0 | 15 | 0 | 19 | REFERENCE ONLY | workflow/command/skill |

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


# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
Bundle: content

## Verdict

- Bundle average: 26.9/100
- Package-now candidates: None
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `content-media-agent` | 4 | 11 | 11 | 0 | 15 | 2 | 43 | REFERENCE ONLY | workflow/command/skill |
| `content-sprint` | 4 | 6 | 6 | 6 | 15 | 0 | 37 | REFERENCE ONLY | workflow/command/skill |
| `content-orchestrate` | 4 | 0 | 0 | 0 | 15 | 0 | 19 | REFERENCE ONLY | workflow/command/skill |
| `content-series-plan` | 4 | 3 | 4 | 6 | 15 | 0 | 32 | REFERENCE ONLY | workflow/command/skill |
| `article-to-carousel` | 4 | 0 | 4 | 0 | 15 | 0 | 23 | REFERENCE ONLY | workflow/command/skill |
| `ai-carousel-engine` | 4 | 0 | 4 | 0 | 15 | 0 | 23 | REFERENCE ONLY | workflow/command/skill |
| `content-review-cycle` | 4 | 0 | 0 | 0 | 15 | 0 | 19 | REFERENCE ONLY | workflow/command/skill |
| `platform-adapt` | 4 | 0 | 0 | 0 | 15 | 0 | 19 | REFERENCE ONLY | workflow/command/skill |

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


# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
Bundle: creative

## Verdict

- Bundle average: 31.9/100
- Package-now candidates: None
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `creative-brief-gen` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `creative-design-agent` | 4 | 11 | 11 | 0 | 15 | 2 | 43 | REFERENCE ONLY | workflow/command/skill |
| `design-brief` | 4 | 9 | 2 | 6 | 15 | 0 | 36 | REFERENCE ONLY | workflow/command/skill |
| `higgsfield-studio` | 4 | 6 | 6 | 2 | 11 | 0 | 29 | REFERENCE ONLY | workflow/no-command/skill |
| `mood-board` | 4 | 3 | 0 | 0 | 15 | 0 | 22 | REFERENCE ONLY | workflow/command/skill |
| `creative-review` | 4 | 6 | 0 | 2 | 15 | 0 | 27 | REFERENCE ONLY | workflow/command/skill |
| `anti-slop-audit` | 4 | 9 | 0 | 4 | 15 | 6 | 38 | REFERENCE ONLY | workflow/command/skill |
| `design-taste-gate` | 4 | 14 | 0 | 4 | 15 | 2 | 39 | REFERENCE ONLY | workflow/command/skill |

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


# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
Bundle: extraction

## Verdict

- Bundle average: 41.6/100
- Package-now candidates: extraction-governor-agent, knowledge-librarian
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `extraction-governor-agent` | 16 | 18 | 12 | 14 | 15 | 13 | 88 | PACKAGE NOW | workflow/command/skill |
| `extract-forge` | 4 | 9 | 4 | 9 | 15 | 2 | 43 | REFERENCE ONLY | workflow/command/skill |
| `extract` | 4 | 6 | 4 | 9 | 15 | 2 | 40 | REFERENCE ONLY | workflow/command/skill |
| `extract-vision` | 4 | 6 | 0 | 2 | 15 | 0 | 27 | REFERENCE ONLY | workflow/command/skill |
| `extract-amplify` | 4 | 0 | 0 | 0 | 15 | 2 | 21 | REFERENCE ONLY | workflow/command/skill |
| `video-context-ledger` | 4 | 0 | 4 | 0 | 15 | 2 | 25 | REFERENCE ONLY | workflow/command/skill |
| `video-source-extract` | 4 | 3 | 4 | 0 | 15 | 0 | 26 | REFERENCE ONLY | workflow/command/skill |
| `convert-extraction` | 4 | 3 | 4 | 6 | 15 | 0 | 32 | REFERENCE ONLY | workflow/command/skill |
| `compile-knowledge` | 4 | 0 | 4 | 4 | 15 | 2 | 29 | REFERENCE ONLY | workflow/command/skill |
| `knowledge-librarian` | 15 | 17 | 12 | 14 | 15 | 12 | 85 | PACKAGE NOW | workflow/command/skill |

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


# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
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


# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
Bundle: revenue

## Verdict

- Bundle average: 28.9/100
- Package-now candidates: None
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `first-10k` | 4 | 11 | 4 | 9 | 15 | 4 | 47 | KEEP AS WORKFLOW | workflow/command/skill |
| `revenue-offer-agent` | 4 | 11 | 11 | 0 | 15 | 2 | 43 | REFERENCE ONLY | workflow/command/skill |
| `client-acquire` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `zero-to-client-sprint` | 4 | 9 | 4 | 4 | 15 | 0 | 36 | REFERENCE ONLY | workflow/command/skill |
| `service-first-productization` | 4 | 0 | 0 | 4 | 15 | 0 | 23 | REFERENCE ONLY | workflow/command/skill |
| `cash-method` | 4 | 0 | 0 | 0 | 15 | 0 | 19 | REFERENCE ONLY | workflow/command/skill |
| `profile-conversion` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `ash-offer-test` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |

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


# Plugin Readiness Scorecard

Generated: 2026-05-09 09:15
Bundle: system

## Verdict

- Bundle average: 61.7/100
- Package-now candidates: autopilot, mission, orchestrate, health-check, routing-intelligence, self-evolve, knowledge-librarian
- Recommended bundle: improve workflow layer first

## Score Table

| Workflow | Rep | Rebuild | Tools | Verify | Port | Fail | Total | Decision | Bridge |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `autopilot` | 20 | 20 | 14 | 15 | 15 | 15 | 99 | PACKAGE NOW | workflow/command/skill |
| `mission` | 20 | 18 | 13 | 15 | 15 | 12 | 93 | PACKAGE NOW | workflow/command/skill |
| `orchestrate` | 17 | 18 | 12 | 13 | 15 | 12 | 87 | PACKAGE NOW | workflow/command/skill |
| `plugin-readiness-audit` | 4 | 3 | 4 | 6 | 15 | 0 | 32 | REFERENCE ONLY | workflow/command/skill |
| `health-check` | 19 | 12 | 14 | 15 | 15 | 12 | 87 | PACKAGE NOW | workflow/command/skill |
| `system-efficiency-benchmark` | 4 | 6 | 6 | 4 | 15 | 2 | 37 | REFERENCE ONLY | workflow/command/skill |
| `routing-intelligence` | 14 | 14 | 13 | 14 | 15 | 13 | 83 | PACKAGE NOW | workflow/command/skill |
| `system-audit` | 4 | 3 | 0 | 2 | 15 | 2 | 26 | REFERENCE ONLY | workflow/command/skill |
| `harness-audit` | 4 | 6 | 0 | 4 | 15 | 4 | 33 | REFERENCE ONLY | workflow/command/skill |
| `context-audit` | 4 | 0 | 0 | 2 | 15 | 0 | 21 | REFERENCE ONLY | workflow/command/skill |
| `bloat-optimizer` | 4 | 11 | 0 | 6 | 15 | 0 | 36 | REFERENCE ONLY | workflow/command/skill |
| `self-evolve` | 13 | 15 | 13 | 14 | 15 | 13 | 83 | PACKAGE NOW | workflow/command/skill |
| `knowledge-librarian` | 15 | 17 | 12 | 14 | 15 | 12 | 85 | PACKAGE NOW | workflow/command/skill |

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
