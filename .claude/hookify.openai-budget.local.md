---
name: openai-budget-check
enabled: true
event: bash
pattern: generate_image_gpt|openai_budget_guard|gpt-image
action: warn
---

**OpenAI GPT Image Budget Guard — MANDATORY**: $15/month hard cap (Farrice 2026-09-02), warn at $10, daily $5, per-call $1. Before any GPT Image call (`viz-image-gen/scripts/generate_image_gpt.py`, direct or via `render_template.py`), run:
```
python3 execution/openai_budget_guard.py check --quality=<low|medium|high|auto> --n=<count> --size=<1024x1024|1536x1024|1024x1536>
```
Only proceed on exit 0. After the call:
```
python3 execution/openai_budget_guard.py log --quality=<...> --n=<...> --size=<...> --status=success [--actual-cost=N]
```
Tracker: `.agent/openai-usage.json`. Policy: `directives/openai-usage-policy.md`. Craft gate still applies: load the master per `skills/generate/references/craft-map.md` before prompting.

If you see this hook fire and HAVEN'T run the check first, STOP. Run the check, then proceed only if allowed.
