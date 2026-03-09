---
description: Generate consistent handcrafted artwork backgrounds for LinkedIn carousel slides using Nano Banana 2. Outputs clean parchment-style illustrations ready for Canva text composition.
---

# /generate-handcrafted-carousel

## Purpose
Generates **artwork-only** backgrounds in a consistent handcrafted aesthetic (charcoal + copper on aged parchment). Designed for LinkedIn carousels but works for any visual content.

**Workflow**: Write content → Generate artwork → Compose text in Canva/Figma

## Input Format

Create a markdown file with this structure:

```markdown
Slide 1:
Label: CONTENT STRATEGY FOR EXECUTIVE COACHES
Title: The Authenticity Trap
Body: Why "being yourself" is keeping you stuck—and what elite executives do instead
Visual: A vintage wooden door slightly ajar, warm light spilling through
```

Fields: `Label` (section tag), `Title` (headline), `Body` (paragraph), `Bullets` (comma-separated list), `Visual` (illustration concept)

## Generate Artwork

```bash
python execution/gen_handcrafted_carousel.py deliverables/carousel_scripts/YOUR_FILE.md
```

Options:
- `--out-dir deliverables/my_project` — custom output directory
- `--with-text` — also generate Pillow text overlay (optional, for quick previews)

## Output
- `artwork/art_01.png` through `art_XX.png` — clean backgrounds, no text
- Style-consistent across all slides (first slide anchors the visual style)

## Canva Composition
1. Upload artwork backgrounds
2. Add text using **Permanent Marker** (headlines) and **Caveat** (body) — both on Google Fonts
3. Color palette: dark brown `#2C1810` headlines, warm body `#4A3728`, copper `#C45A33` labels

## Future Enhancement
JSON schema layout approach: send artwork + content to Gemini → get layout JSON → Pillow renders with AI-driven composition taste. Logged for future sprint.
