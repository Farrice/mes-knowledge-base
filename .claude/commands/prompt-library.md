---
description: "Search and deploy the 3,610 Crown Jewel / practitioner prompts harvested across all skills and extractions — find the battle-tested prompt for any job, then run it as-is or route to its owning skill."
---

Search the prompt-asset registry for the user's need:

```bash
python3 execution/prompt_library.py search "<user's topic/need>" --top 10
```

(If the index is stale or missing: `python3 execution/prompt_library.py build` first. `stats` shows coverage; `orphans` audits wiring.)

Then, for the best match(es):
1. Read the prompt file at the returned path.
2. Offer the user two deployment modes:
   - **Run as-is** — execute the prompt directly on their input (these are practitioner-mode, zero-shot deployable; fill any `[BRACKET]` inputs from context).
   - **Route to owning skill** — load the owning skill (SKILL.md + genius.md) and run its matching workflow instead, when the need calls for the full engine rather than one atomic prompt.
3. Treat exaggerated example metrics inside old prompts as style, not fact — per the factual-grounding standard, never repeat their invented statistics as claims. The structural execution is the asset.
