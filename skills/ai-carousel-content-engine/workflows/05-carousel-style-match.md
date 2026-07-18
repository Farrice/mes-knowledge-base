---
description: "Create carousel style-board direction from a brand, mood board, or design reference"
---

# Carousel Style Match

Use before recurring carousel generation.

1. Run `/mood-board` or `/design-md-synthesize` for the brand.
2. Capture palette, typography, composition, and visual motifs.
3. Feed that direction to `--style`.

## Output Schema

A style board with Name, Visual Style (one substantive descriptive passage: genre, brand tier, contrast, whitespace, clutter tolerance), Palette (hex list, 4-6 colors each with a stated role), Typography (headline / body / label treatments named as three distinct decisions), Composition (the compositional rule set applied to every slide), and — when a custom reference was supplied — a Custom Reference Direction field. Full contract: `references/prompts-v2/style-board.md`.

## Quality Gate

- Every palette entry is a real hex value with a stated role, not an adjective like "modern" or "clean."
- Headline, body, and label typography are specified as three distinct decisions, not one blanket font note.
- The composition section states a concrete ideas-per-slide and copy-density rule.
- If no reference input existed yet, the board says so plainly rather than presenting an invented brand system as grounded.
- The board is written for reuse across future carousels for this brand/client, not tuned to one topic.
