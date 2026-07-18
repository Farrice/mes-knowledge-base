---
description: "Forge carousel copy from a raw idea, client insight, transcript, or article"
---

# Carousel Copy Forge

Use Jun Yuh, Josh Sanders, and LinkedIn 2026 carousel architecture:

- cover hook
- retention bridge
- one idea per payload slide
- transformation summary
- save/share/click CTA

```bash
python3 execution/ai_carousel_engine.py --mode copy --text "raw idea"
```

## Output Schema

Slide-by-slide carousel copy built on the cover hook / retention bridge / one-idea-per-slide / transformation / CTA architecture named above: numbered slides, each with label, title, body, visual direction, transition cue. Full field contract: `references/prompts-v2/carousel-copy-script.md`.

## Quality Gate

- The cover hook is specific to the source material, not a generic "viral" line.
- The retention bridge earns the next swipe rather than restating the hook.
- No payload slide carries more than one idea.
- The CTA names a save/share/click action tied to an owned-content pathway, not a bare engagement ask.
