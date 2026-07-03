---
description: "Create a GPT Image 2 structured JSON design prompt for a carousel"
---

# /carousel-design-prompt

```bash
python3 execution/ai_carousel_engine.py --mode prompt --source path/to/source.md --style "brand or reference direction"
```

Use the resulting `gpt-image-2-prompt.json` directly as a GPT Image 2 layout prompt. Any actual image generation must go through the cost-gated visual route (`creative_router.py` pre-flight, e.g. `skills/fantastic-posters/`).

