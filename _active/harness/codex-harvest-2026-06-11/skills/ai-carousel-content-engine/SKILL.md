---
name: "AI Carousel Content Engine"
description: "Turn articles, raw ideas, transcripts, or brand insights into 7-10 slide carousel packages with copy, visual direction, GPT Image 2 prompts, review checklists, and publish packs."
version: "1.0"
format: "completion-engine"
expert: AI Carousel Content Engine
domain: social carousels, GPT Image 2 prompts, content repurposing, brand style systems, marketing asset production
workflows: 7
---

# AI Carousel Content Engine

This skill creates Farrice's own version of the article-to-carousel workflow demonstrated in the Luke Carter video. It does not copy the hidden community prompt. It builds a reusable capability from observed workflow mechanics, existing Antigravity carousel frameworks, GPT Image 2 prompt direction, and human-in-the-loop creative review.

## Core Promise

Turn a source idea into a visual marketing asset fast:

1. Start with an article, idea, transcript, or client insight.
2. Extract the strongest claims and sequence them into a 7-10 slide carousel.
3. Generate a style board and GPT Image 2 structured prompt.
4. Review for taste, text accuracy, brand fit, and strategic CTA.
5. Package for Instagram, LinkedIn, client delivery, or a weekly content pipeline.

## Available Workflows

| # | Workflow | Slash Command | Produces |
|---|---|---|---|
| 1 | [AI Carousel Engine](workflows/01-ai-carousel-engine.md) | `/ai-carousel-engine` | Full carousel package |
| 2 | [Article To Carousel](workflows/02-article-to-carousel.md) | `/article-to-carousel` | Article-derived slide script |
| 3 | [Carousel Copy Forge](workflows/03-carousel-copy-forge.md) | `/carousel-copy-forge` | Swipe-worthy slide copy |
| 4 | [Carousel Design Prompt](workflows/04-carousel-design-prompt.md) | `/carousel-design-prompt` | GPT Image 2 JSON prompt |
| 5 | [Carousel Style Match](workflows/05-carousel-style-match.md) | `/carousel-style-match` | Style board and reference direction |
| 6 | [Carousel Review](workflows/06-carousel-review.md) | `/carousel-review` | Human review checklist and repair notes |
| 7 | [Carousel Publish Pack](workflows/07-carousel-publish-pack.md) | `/carousel-publish-pack` | Caption, CTA, platform notes, client handoff |

## Local CLI

```bash
python3 execution/ai_carousel_engine.py --mode pack --source path/to/article.md --title "Topic"
python3 execution/ai_carousel_engine.py --mode copy --text "raw idea"
python3 execution/ai_carousel_engine.py --mode prompt --source path/to/carousel.md --style "brand/style direction"
```

## Output Package

Each full run writes to `deliverables/ai-carousel-engine/<slug>/`:

- `source.md`
- `carousel-script.md`
- `slide-brief.json`
- `gpt-image-2-prompt.json`
- `style-board.md`
- `review-checklist.md`
- `publish-pack.md`

## Stack With

| Workflow | Role |
|---|---|
| `/gpt-image-2` | Convert or refine the structured carousel design prompt |
| `/mood-board` | Build visual references before prompt generation |
| `/design-md-synthesize` | Create a durable brand/design system before recurring carousels |
| `/creative-review` | Taste-check generated outputs |
| `/video-context-ledger` | Extract source material from videos before carousel creation |
| `/extract-forge` | Build a deeper skill if a carousel system should become a broader content engine |

## Quick Reference

- Genius context: [genius.md](genius.md)
- Source map: [references/source-map.md](references/source-map.md)
- Quality rubric: [references/quality-rubric.md](references/quality-rubric.md)
- Luke Carter extraction notes: [references/luke-carter-video-extraction-notes.md](references/luke-carter-video-extraction-notes.md)
- Prompt patterns: [references/genius-patterns.md](references/genius-patterns.md)
- Hidden knowledge: [references/hidden-knowledge.md](references/hidden-knowledge.md)

