---
description: Score workflow-family plugin readiness, fresh-thread reliability, packaging tradeoffs, and whether a workflow should stay a prompt, skill, workflow, or Codex plugin
---

# /plugin-readiness-audit - Plugin Packaging Decision Gate

Decide whether a workflow family should stay as prompts/workflows/skills or become a repo-local or global Codex plugin.

## Usage

```bash
/plugin-readiness-audit
/plugin-readiness-audit autopilot mission orchestrate
/plugin-readiness-audit --plugin antigravity-operator-core
```

## Pre-Flight

Read:

1. `skills/plugin-readiness-audit/SKILL.md`
2. `semantic_libraries/antigravity/primitives/workflow-packaging-ladder.md`
3. `plugins/antigravity-operator-core/.codex-plugin/plugin.json` if the pilot plugin exists

## Execution

Run:

```bash
python3 execution/plugin_readiness_audit.py --stdout
```

For custom candidates:

```bash
python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate
```

Persist a scorecard only when explicitly requested:

```bash
python3 execution/plugin_readiness_audit.py --all-bundles --out deliverables/plugin-readiness/family-bundle-matrix.md
```

## Output

Return:

- scorecard text, or a generated scorecard path only when `--out` is used
- candidate scores
- package now / improve first / keep decision
- first plugin bundle recommendation
- fresh-thread tests required before calling the plugin proven

## Quality Gate

Do not recommend a plugin if the scorecard says the workflow is still vague, low-use, unverified, or path-fragile. Improve the skill/workflow layer first.
