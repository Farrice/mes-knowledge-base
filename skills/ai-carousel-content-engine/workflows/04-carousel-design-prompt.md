---
description: "Create a GPT Image 2 structured JSON prompt for carousel design"
---

# Carousel Design Prompt

```bash
python3 execution/ai_carousel_engine.py --mode prompt --source path/to/carousel-or-article.md --style "style direction"
```

Then use `gpt-image-2-prompt.json` directly as a GPT Image 2 layout prompt. Any actual image generation must go through the cost-gated visual route (`creative_router.py` pre-flight, e.g. `skills/fantastic-posters/`).

