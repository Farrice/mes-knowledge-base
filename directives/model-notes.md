# Model & SDK Notes

> Extracted from CLAUDE.md 2026-06-09 (rebuild). Read when writing scripts that call LLM APIs.

**Primary**: Claude Opus 4.7 (1M context). Sonnet 4.6 for single-turn; Haiku 4.5 for routing/classification.

**Current rules:**
- Anthropic SDK: do NOT set `temperature`, `top_p`, `top_k` (400 errors). Use `effort: "low|medium|high|xhigh"` instead of `thinking.budget_tokens`.
- Tokenizer: ~1.0x-1.35x more tokens vs 4.6. Factor into caching.
- Prompt caching: 5-min TTL default, 1-hour at higher cost. Cache reads = 10% of input cost.
- Python scripts in `execution/` call **Gemini** (not Anthropic) — their params are fine.
- Claude Code harness handles model config. You do not call Anthropic API from scripts.
- For current model IDs/pricing/params, consult the `claude-api` skill — never answer from memory.
