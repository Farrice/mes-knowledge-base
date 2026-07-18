---
description: "Create a full article/idea-to-carousel package with copy, style, GPT Image prompt, review, and publish notes"
---

# AI Carousel Engine

Run the full package workflow.

```bash
python3 execution/ai_carousel_engine.py --mode pack --source path/to/source.md --title "Carousel Topic"
```

Use when you want the complete reusable asset package, not just slide copy.

## Output Schema

Full seven-part package matching `deliverables/ai-carousel-engine/<slug>/`: `source.md` (title/audience/mission/source), `carousel-script.md` (7-10 numbered slides, each with label, title, body, visual direction, transition), `slide-brief.json`, `gpt-image-2-prompt.json` (structured JSON design prompt — type/output/style/brand_system/layout_rules/slides/human_review_note), `style-board.md` (name/palette/typography/composition), `review-checklist.md` (seven-point pass/fail check), `publish-pack.md` (caption, CTA options, platform notes). Full field-level contract: `references/prompts-v2/full-carousel-package.md`.

## Quality Gate

- Every slide claim traces to the source material — no invented statistics or claims.
- Slide 1 stops, slide 2 retains, and each core slide carries exactly one idea (no paragraph-length body text).
- The GPT Image 2 prompt is a structured JSON spec (exact slide text, count, layout rules, style) — never a vague "make it viral" mood paragraph.
- The final slide names a real owned-content or offer pathway, not a generic follow/like ask.
- The review checklist is present in the package and genuinely flags anything unresolved rather than being rubber-stamped.
