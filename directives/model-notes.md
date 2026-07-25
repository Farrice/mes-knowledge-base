# Model & SDK Notes

> Extracted from CLAUDE.md 2026-06-09 (rebuild). Read when writing scripts that call LLM APIs.

**Primary**: whatever the harness session runs (don't override). **Executor seating is hard-coded in `directives/orchestration-doctrine.md` → Executor Model Registry (Farrice 2026-07-24): Opus 5 = heavy executor, Sonnet 5 = grunt/grind, Haiku 4.5 = mechanical only.**

## Opus 5 (`claude-opus-5`) — heavy executor tier (added 2026-07-24, source: claude-api skill)
- $5/$25 per MTok (same as 4.8, step-change capability). Separate rate-limit bucket from Opus 4.x.
- **Thinking is ON by default** (omitting `thinking` runs adaptive — unlike 4.8). `{type: "disabled"}` only at effort ≤ high, else 400. `max_tokens` caps thinking + text together — give headroom.
- No `temperature`/`top_p`/`top_k`, no `budget_tokens`, no assistant prefill (all 400).
- Effort ladder `low`→`max`: start `xhigh` for coding/agentic, `high` elsewhere, then SWEEP DOWN — `low`/`medium` are unusually strong on this model.
- **Prompting deltas that matter:** DELETE verification scaffolding (self-verifies; "double-check" instructions cause over-verification) · add scope-discipline line (expands task scope otherwise) · add conciseness line (effort does NOT shorten visible output) · CAP subagent spawns (delegates readily — opposite of 4.8) · give full task spec in ONE up-front turn.
- Prompt-cache minimum 512 tokens (down from 1024). Fast mode: Claude-API only, $10/$50.

## Sonnet 5 (`claude-sonnet-5`) — grunt/grind executor (added 2026-07-24)
- $3/$15 ($2/$10 intro through 2026-08-31). Near-Opus agentic/coding quality.
- Adaptive thinking on by default; manual `budget_tokens` 400s; non-default sampling params 400.
- **New tokenizer: ~30% more tokens for the same text vs 4.6** — re-baseline max_tokens/counts.
- Literal instruction-follower: state scope explicitly ("apply to EVERY section"); coverage-first prompts for review work (severity filters depress measured recall); effort `high` default, `xhigh` for hardest (first Sonnet with xhigh).

**Opus fallback policy (2026-06-11 — recurring "Claude Opus is not available" capacity errors):**
- NEVER pin Opus in agent frontmatter, settings, sub-agent spawns, or Hermes defaults — `platform_compiler.py lint` fails the build on active pins.
- Fallback chain everywhere: session default (inherit) → Sonnet → Haiku (bulk/routing). Opus is explicit-invoke only, with a stated reason, and expect to retry on capacity errors rather than loop.
- Sub-agents: spawn with inherit or `model: sonnet`; an Opus-pinned definition that errors "not available" = switch model and continue, never stall the mission.

**Current rules:**
- Anthropic SDK: do NOT set `temperature`, `top_p`, `top_k` (400 errors). Use `effort: "low|medium|high|xhigh"` instead of `thinking.budget_tokens`.
- Tokenizer: ~1.0x-1.35x more tokens vs 4.6. Factor into caching.
- Prompt caching: 5-min TTL default, 1-hour at higher cost. Cache reads = 10% of input cost.
- Python scripts in `execution/` call **Gemini** (not Anthropic) — their params are fine.
- Claude Code harness handles model config. You do not call Anthropic API from scripts.
- For current model IDs/pricing/params, consult the `claude-api` skill — never answer from memory.
- **Model Dialect Cards** (`directives/model-dialects/<model>.md`, via `/forge dialect <model>`):
  probe-evidenced quirks + DO/DON'T per model. Read the card before writing prompts, gates, or
  sub-agent dispatches pinned to that model. First card: `claude-haiku-4-5.md` (2026-07-15 —
  headline: inline instructions silently override standing rules; restate binding rules inside
  the task block).
