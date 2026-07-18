---
description: "Create a GPT Image 2 structured JSON prompt for carousel design"
---

# Carousel Design Prompt

```bash
python3 execution/ai_carousel_engine.py --mode prompt --source path/to/carousel-or-article.md --style "style direction"
```

Then use `gpt-image-2-prompt.json` directly as a GPT Image 2 layout prompt. Any actual image generation must go through the cost-gated visual route (`creative_router.py` pre-flight, e.g. `skills/fantastic-posters/`).

## Output Schema

A structured JSON GPT Image 2 design prompt: type/output block (format, platform, aspect ratio, slide count), resolved style block, brand_system (palette hex list, typography, composition), audience, topic, a complete layout_rules list, and a full per-slide array (slide number, label, headline, body, visual_direction — pulled verbatim from the carousel script), plus a human_review_note. Full contract: `references/prompts-v2/gpt-image-2-design-prompt.md`.

## Quality Gate

- Every slide's headline and body match the source carousel script exactly — no paraphrasing introduced at this stage.
- `slide_count` in the output block equals the number of entries in the `slides` array.
- Layout rules are explicit (regions, exact text, counts, hierarchy-when-copy-runs-long) — never a vague style paragraph.
- The `human_review_note` field is present and substantive, not a placeholder.
