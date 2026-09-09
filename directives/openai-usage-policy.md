# OpenAI API Usage Policy (GPT Image via Scrapes `viz-image-gen`)

> **Cap**: **$15.00 per calendar month, hard block** (Farrice, 2026-09-02). Warn at $10. Daily block $5. Per-call ceiling $1.
> **Tracker**: `.agent/openai-usage.json` (auto-created) | **Guard**: `execution/openai_budget_guard.py` | **Hookify**: `.claude/hookify.openai-budget.local.md` | **Hook gate**: `execution/hooks/cost_gate_hook.py` pattern `generate_image_gpt.py` → service `openai-image`
> **Key**: `OPENAI_API_KEY` in project-root `.env` (never in chat, never committed). Verified live 2026-09-02.

## Why this exists
Farrice prefers the GPT Image path over Gemini for the Scrapes image skill. It is a new paid surface with no prepaid wallet, so the only brake is this guard. Compass doctrine: the cost gate is one of the two things allowed to block work. Denied = surface to Farrice, never retry.

## Hard rule
Every OpenAI image call is preceded by a guard check and followed by a guard log.

```bash
# 1. PRE-FLIGHT
python3 execution/openai_budget_guard.py check --quality=<low|medium|high|auto> --n=<count> --size=<1024x1024|1536x1024|1024x1536>

# 2. RUN (the skill's own script; export the key first, its script reads os.environ not .env)
export $(grep -E "^OPENAI_API_KEY=" .env | xargs) && uv run .claude/skills/viz-image-gen/scripts/generate_image_gpt.py --prompt "…" --filename out.png --quality high

# 3. POST-FLIGHT
python3 execution/openai_budget_guard.py log --quality=<...> --n=<count> --size=<...> --status=success [--actual-cost=N]
```

`render_template.py` inside the same skill calls the GPT script itself; the hook pattern catches the direct script only. When a pipeline (00-social-content → ssc-image-generator) generates images, run the guard once per batch with `--n` set to the slide count before starting the pipeline.

## Pricing (UNCONFIRMED against OpenAI's 2026 list; actuals overwrite estimates)
| Quality | 1024×1024 | 1536-px sizes |
|---|---|---|
| low | $0.011 | $0.017 |
| medium | $0.042 | $0.063 |
| high / auto | $0.167 | $0.25 |

At high quality that is roughly 90 images a month. Prefer medium for drafts and high only for the final pick.

## Craft gate still applies
Never freehand a generator prompt. Load the matching master per `skills/generate/references/craft-map.md` before the call. The Scrapes 6-element framework wraps execution; it does not replace the master.

## Admin
`status` shows the month; `reset-month` is Farrice's call only. Raising the cap is a new decision from him, never a self-adjustment.
