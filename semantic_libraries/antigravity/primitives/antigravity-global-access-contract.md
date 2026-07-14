# Antigravity Global Access Contract

## Objective

Make Google Antigravity workflows available from unrelated Codex projects through a thin global dispatcher without copying the harness, broadening default context, or mutating the dirty canonical tree.

## Source Of Truth

- Canonical behavior: `/Users/farricecain/Google Antigravity/.agent/workflows/`
- Canonical wrappers: `/Users/farricecain/Google Antigravity/.agents/skills/`
- Safe mutation surface: the assigned Codex-owned worktree only
- Global bridge: `~/.codex/tools/antigravity_global.py`
- Global front doors: a small manifest of dispatcher/control skills; never a mirror of the full harness

## Skill System Contract

- **Function owner:** `/system-audit` owns global-access drift, routing, and hot/cold reconciliation.
- **Builder handoff:** `/source-to-skill-system` owns the manifest and plugin after audit proof.
- **Inputs:** raw operator intent, canonical root, Codex write root, global front-door manifest.
- **Outputs:** deterministic owner, bounded support gates, on-demand canonical route, verifier receipt.
- **Human checkpoint:** global writes, plugin install, external writes, publishing, destructive cleanup, or changes to the dirty canonical tree.
- **No duplicate contract:** global skills and the personal plugin are thin dispatchers; canonical workflows remain the only behavior source.

## Agentic Engineering Packet

- **Goal:** reliable cross-project access with no context rot and no Antigravity structural regression.
- **Hot context:** dispatcher, manifest, global helper, `/system-audit`, `/source-to-skill-system`.
- **On-demand context:** the exact canonical workflow, skill, agent specification, and supporting primitive selected for the current request.
- **Skipped context:** the full workflow corpus, full expert library, plugin marketplace catalogs, dirty working-tree state, and unrelated project context.
- **Review loop:** classifier fixtures -> workflow-router fixtures -> raw-intent packet fixtures -> plugin validator -> unrelated-project smoke test.
- **Stop condition:** targeted verifiers pass and no dirty-tree tracked file changes.
- **Dependency gate:** standard library and existing Codex/Antigravity tools only.
- **Rollback:** remove the personal plugin registration and dispatcher package; canonical Antigravity files remain unchanged.

## Hot And Cold Policy

Hot and cold are routing and context-loading states, not filesystem locations. The canonical workspace retains a single live wrapper tree for explicit discovery. Global Codex advertises only the minimal operator-core front doors. Everything else is resolved and loaded on demand after routing.

## Non-Regression Guard

This layer must not edit, move, delete, or duplicate canonical workflows, agents, hooks, command wrappers, or domain skills. It must not write to `/Users/farricecain/Google Antigravity` when that tree is dirty. Hook trust, secrets, and environment files are never copied between worktrees as part of installation.

