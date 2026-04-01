# Context Engine — Tiered Loading

> Check Hot first, then start at Tier 0, escalate only when needed.

## Loading Tiers

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **Hot** | Nothing (already loaded) | 0 | Expert was loaded earlier this conversation |
| **0 — Card** | `agents/_framework/invocation-cards.md` | ~80 | Routing, ensemble selection |
| **1 — Standard** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task |
| **2 — Deep** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3 — Sub-Agent** | Spawn sub-agent (fresh context) | ~300 main | Multi-expert, 10+ files loaded |

## Hot Context Rule

Before loading any expert, check if they were already loaded this conversation:
- Hot at **Tier 1** and Tier 2 needed → only read `genius.md` (incremental)
- Hot at **Tier 2** → skip all reads, expert is fully loaded
- **Anti-pattern**: Re-reading SKILL.md twice in one conversation wastes ~1,350 tokens

## Deferred Tier Escalation

Start at Tier 1 (SKILL.md only). Load `genius.md` ONLY if:
- The first-pass output doesn't meet quality expectations
- The task is explicitly creative/complex (screenwriting, brand strategy, deep extraction)
- The user asks for "the best" or "world-class" output

## Never Rely on General Training

Route via invocation cards first. Full protocol: `directives/agent-loading-protocol.md`.
