---
name: "antigravity-operator-core"
description: "Repo-local Antigravity operator plugin skill. Use when the user asks to use Antigravity Operator Core, route messy context, show a Virtuoso Trace, start Autopilot, create Mission Mode, audit plugin readiness, inspect system health, review routing intelligence, run Extraction Governor, use Knowledge Librarian, or decide whether to self-evolve a workflow."
---

# Antigravity Operator Core

Use this repo-local plugin skill as the hot operating layer for `/Users/farricecain/Codex Antigravity`.

## Route Order

1. Raw context, unclear route, or "what should I do with this?" -> `.agent/workflows/autopilot.md`
2. Long-running, system-changing, reusable, or multi-milestone work -> `.agent/workflows/mission.md`
3. User asks for a menu or candidate routes -> `.agent/workflows/orchestrate.md`
4. Source-to-system, skill boundary, extraction, or forge decision -> `.agent/workflows/extraction-governor-agent.md`
5. Library overlap, dormant knowledge, or reusable solution check -> `.agent/workflows/knowledge-librarian.md`
6. System health, dormant loops, or proof-of-life -> `.agent/workflows/health-check.md`
7. Route quality, misroutes, or usage evidence -> `.agent/workflows/routing-intelligence.md`
8. Repeated failure, plateau, or workflow improvement -> `.agent/workflows/self-evolve.md`
9. Full-arsenal, subagent, composition, plugin/tool-blending, agent-elevation, solo orchestration, or full-system excellence work -> `.agent/workflows/virtuoso.md`
10. Deep research, wide research, social listening, market intelligence, PMF/OMF, ICP deep canvassing, or claim verification -> `.agent/workflows/deep-research-os.md`
11. Plugin packaging decision -> `.agent/workflows/plugin-readiness-audit.md`

## Virtuoso Trace

For complex work, run:

```bash
python3 execution/virtuoso_orchestration.py "[goal]" --json
```

Preferred command surface:

```text
/virtuoso [goal]
```

Preferred deep-research surface:

```text
/virtuoso --mode research [research objective]
```

Route into `.agent/workflows/deep-research-os.md` when the work needs
source-backed research planning, social listening, wide decomposition, source
ledgers, claim labels, and anti-hallucination verification.

Use `--delegate-intent` when the user explicitly asks for subagents, delegated
agents, parallel agents, or swarm work. This prepares subagent-first packets but
does not spawn real Codex subagents. Use `--log-routing` only after the chosen
compound stack is actually used, so routing intelligence records real ensemble
evidence.

The trace must expose:

- primary route and function owner
- recommended stack or skip reason
- bounded composition slots
- delegation matrix and receipt boundary
- plugin/tool surface
- routing evidence
- verifier plan and first action
- execution receipt that separates considered gates from executed workflows/scripts

## Rules

- Prefer the current workspace workflow files when they exist.
- Do not replace Antigravity routers; use them.
- Ask before external writes, paid tools, destructive changes, or real subagents.
- Keep `system-audit`, `expert-composition-governor`, and `source-to-skill-system` as referenced dependencies until plugin readiness scores justify bundling them.
- For plugin packaging, run `python3 execution/plugin_readiness_audit.py` before creating or expanding a plugin.
- A plugin is proven only after direct invocation, natural language trigger, missing-info behavior, path resolution, and fresh-session checks pass.
