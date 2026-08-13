---
description: Score a workflow family for plugin packaging, compare it with simpler routing or metadata fixes, and return a package/keep/improve decision with cold-start tests.
---

# Plugin Readiness Audit

## Pre-Flight Gate

Load `../genius.md` and `../../../semantic_libraries/antigravity/primitives/workflow-packaging-ladder.md`.

Reject “important therefore plugin.” Name the actual job: portability, installation, reconstruction reduction, permissions, external tools, or distribution.

## Inputs

- Target workflow, skill, family, or bundle
- Intended destination: current repo, repo-local plugin, home/global plugin, or external distribution
- Known failure or reconstruction burden
- Required tools, permissions, apps, or MCP connections

## Execution

1. **Check existing ownership.** Locate the current skill, workflow, command bridges, tools, references, and verifiers.
2. **Run the efficiency comparison.** For broad restructuring, run `python3 execution/system_efficiency_benchmark.py`. Prefer cleanup when it closes the same gap.
3. **Score readiness.** Run `python3 execution/plugin_readiness_audit.py [candidate]` or use `--bundle <name>`.
4. **Inspect hidden dependencies.** Record repository paths, environment assumptions, global configuration, credentials, hooks, apps, and MCP requirements.
5. **Choose the smallest build shape.** Return one: KEEP AS REFERENCE, KEEP AS WORKFLOW, KEEP AS SKILL, IMPROVE FIRST, REPO-LOCAL PLUGIN CANDIDATE, or GLOBAL PLUGIN CANDIDATE.
6. **Define acceptance tests.** Require direct invocation, natural-language trigger, missing-information behavior, path resolution, and fresh-thread use.
7. **Separate evidence states.** Label structural readiness, cold-start portability, human acceptance, adoption, and outcome proof independently.

## Adaptations

| Target | Primary concern |
|---|---|
| One workflow | Repetition and reconstruction burden |
| Skill family | Shared method and smallest coherent bundle |
| Operator core | Router parity, path independence, and fresh-thread behavior |
| External connector | Permissions, authentication, and failure recovery |
| Public distribution | Privacy, licensing, dependencies, and install safety |

## Output Requirements

1. Current architecture and owner
2. Readiness score and evidence
3. Cleanup-only comparison
4. Verdict and smallest package
5. Hidden dependencies and permission boundaries
6. Acceptance tests
7. Proof states and next safe action

Execution prompt: `../references/prompts-v2/plugin-readiness-audit.md`

## Quality Gate

- Existing-route fit checked
- One smallest package named
- Cleanup considered before plugin work
- No broad pluginization without routing feedback
- Fresh-thread and path tests specified
- No structural score presented as adoption or outcome proof
