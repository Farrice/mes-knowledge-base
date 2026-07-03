---
description: "Turn an article, raw idea, transcript, or brand insight into a complete AI carousel package"
---

# /ai-carousel-engine

Create a full AI carousel package.

## Steps

1. Load `skills/ai-carousel-content-engine/SKILL.md`.
2. Run:
   ```bash
   python3 execution/ai_carousel_engine.py --mode pack --source path/to/source.md --title "Topic"
   ```
3. Review `review-checklist.md`.
4. Use `gpt-image-2-prompt.json` as a GPT Image 2 layout prompt directly. Any actual image generation must go through the cost-gated visual route (`creative_router.py` pre-flight, e.g. `skills/fantastic-posters/`).

