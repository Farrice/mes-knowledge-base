---
name: "plugin-readiness-audit"
description: "Audit Antigravity workflows, skills, agents, and command surfaces to decide whether they should stay as prompts/workflows/skills or be packaged as repo-local or global Codex plugins. Use when the user asks about plugin readiness, workflow packaging, skill bloat, missing operating context, fresh-thread reliability, or Nate B Jones style plugin restructuring."
---

# Plugin Readiness Audit

Use this skill to decide what should become a Codex plugin and what should stay as a workflow, skill, reference, or prompt.

## Load Order

1. Read `semantic_libraries/antigravity/primitives/workflow-packaging-ladder.md`.
2. If the user is asking about broad restructuring, performance, or overengineering, run `python3 execution/system_efficiency_benchmark.py` first.
3. Run `python3 execution/plugin_readiness_audit.py` for the target workflow family.
4. Read the generated scorecard before recommending any plugin scaffold.

## Default Candidate Set

When the user asks about the core Antigravity operating layer, score:

- `autopilot`
- `mission`
- `orchestrate`
- `extraction-governor-agent`
- `knowledge-librarian`
- `health-check`
- `routing-intelligence`
- `self-evolve`

## Decision Rule

- Package only candidates scoring 80+ or a tightly related bundle whose average score is 80+.
- If a candidate scores 65-79, fix the workflow/skill layer before adding plugin packaging.
- If the issue is command bloat, routing drift, or underuse, prefer routing and usage instrumentation over a new plugin.
- If the benchmark says router/metadata cleanup performs as well as plugin packaging, cleanup comes first.

## Required Output

Return:

- the scorecard path
- package now / improve first / keep as workflow decisions
- the first plugin candidate, if any
- required fresh-thread tests
- any path, permission, or marketplace risk
