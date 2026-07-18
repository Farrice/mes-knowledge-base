---
description: "Turn an article or owned content page into a 7-10 slide carousel script"
---

# Article To Carousel

```bash
python3 execution/ai_carousel_engine.py --mode copy --source path/to/article.md --mission position
```

The article remains the source of truth. The carousel becomes the distribution vehicle.

## Output Schema

A numbered 7-10 slide carousel script derived from the source article/owned-content page: per slide — label (Cover / Retention Bridge / Step N / Transformation / CTA), title (headline, ≤~9 words), body (one supporting line, slide-length, not a paragraph), visual direction (one designable instruction), and a transition cue. Full contract: `references/prompts-v2/carousel-copy-script.md`.

## Quality Gate

- The article remains the traceable source of truth — no slide claim exceeds what the article actually states.
- Exactly one idea per payload slide; no slide carries paragraph-length body text.
- The cover hook and promise match the stated mission (attract/position/convert) rather than a generic "viral" framing.
- The CTA routes back to the article/owned-content page, not a bare engagement ask.
