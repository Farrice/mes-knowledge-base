# Codex Operator Surface and Packaging Audit

**Date:** 2026-08-13
**Scope:** Google Antigravity command, workflow, skill, and plugin packaging
**Mode:** bounded implementation in isolated `codex/operator-card-packaging` lane

## Verdict

The repository does not need broad skill conversion or plugin packaging. It needs a tiny operator-facing surface over a large cold arsenal, plus repair of one missing packaging owner.

## Current evidence

| Surface | Count / result |
|---|---:|
| Root skills | 400 |
| Skill workflows | 2,688 |
| Workflow wrappers | 2,761 |
| Skill-owned wrappers | 2,325 |
| Standalone/conductor wrappers | 436 |
| Indexed arsenal assets | 6,054 |
| Unreachable workflows | 0 |
| Skills missing `SKILL.md` | 0 |
| Operator Core verifier | PASS |
| Skill-system contract | PASS |
| Platform lint | 0 failures |

## Package-shape decision

| Surface | Decision | Reason |
|---|---|---|
| One-page Operator Card | Standalone reference workflow | It displays operating guidance; it is not a reusable expert method |
| Plugin-readiness audit | Restore as focused system skill | A deterministic engine and packaging method exist, while live routing points to a missing owner |
| Existing command library | Keep cold and searchable | Zero workflows are unreachable; mass conversion adds duplication |
| Operator-core plugin | PARKED candidate | Local score is 87.4/100, but routing feedback and fresh-thread portability proof are insufficient |
| Domain bundles | Keep as skills/workflows | Current readiness benchmark does not justify plugin packaging |

## Efficiency benchmark

- Current routing quality: **8.7/10**
- Router/metadata cleanup projection: **9.3/10**
- Operator-core plugin projection: **10.0/10**, unproven
- First-choice route hits: **8/10**
- Broad packaging remains blocked until routing feedback and fresh-thread evidence improve.

## Context policy

```text
Hot: natural language, /go, and five control front doors
  -> Warm: expert and domain skill front doors
  -> Cold: exact workflows found through routing and /arsenal
  -> Backend: source-command shims, prompts, hooks, indexes, verifiers
```

## Plugin judgment

Plugins are installable distribution units. They are useful when a stable bundle must travel, install, carry tools, or work outside repository-local context. They are not necessary merely to use capabilities inside this primary Google Antigravity harness.

No plugin was created in this pass. The responsible next proof would be a fresh-thread operator-core trial that compares:

1. current routing,
2. metadata cleanup,
3. a repo-local plugin candidate.

## Changes made

1. Added `guides/CODEX-OPERATOR-CARD.md`.
2. Added the lightweight `/operator-card` reference command and Codex compatibility bridge.
3. Restored `plugin-readiness-audit` as a focused skill with one workflow, operating intelligence, references, and a born-v2 execution prompt.
4. Restored `/plugin-readiness-audit` workflow and command bridges.
5. Left every existing skill and workflow in place.

## Proof boundary

This pass proves repository structure, command discoverability, prompt structure, and deterministic routing checks. It does not prove long-term adoption, improved market output, or plugin portability outside this checkout.
