# Model & SDK Notes

> Extracted from CLAUDE.md 2026-06-09 (rebuild). Read when writing scripts that call LLM APIs.

**Primary**: whatever the harness session runs (don't override). Sonnet 4.6 for single-turn; Haiku 4.5 for routing/classification.

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
