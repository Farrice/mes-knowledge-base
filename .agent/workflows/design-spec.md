# Design Specification

Complete graphic design specifications and direction for apparel, logos, posters, social content, packaging, and brand assets. Produces production-ready specs with AI prompts, print methods, and file specifications.

## Expert Loading

Load `skills/creative-direction/SKILL.md` at Tier 1. For streetwear/apparel, load `genius.md` Section 4 (Streetwear Design) for archetypes, placement guides, and print methods. For any design, load Section 1 (Visual Language) for typography and composition.

## Workflow

### Step 1: Identify the Deliverable

- **Type:** T-shirt graphic, logo, poster, social post, packaging, pattern, brand asset, album art, merch line
- **Dimensions/format:** Specific sizes, aspect ratios
- **Print method:** Screen print, DTG, DTF, sublimation, embroidery, puff print, discharge, foil, digital only
- **Brand/style context:** Existing brand DNA, or new direction?

### Step 2: Design Direction

- **Graphic archetype** (for streetwear): Logo Play, Vintage Bootleg, Art Piece, Typography Statement, Pattern/All-Over
- **Art movement/style reference** (be specific — name the movement, the era, the visual signature)
- **Color palette** (specific hex codes, max 4-5 colors + Pantone for print)
- **Typography** (specific fonts, weights, sizes — not "bold font" but "Futura Bold Condensed at 72pt")
- **Composition/layout** (with placement guide for apparel — center chest, left chest, full front, back print, oversized, sleeve)
- **Texture/treatment** (distressed, clean, halftone, gradient, grain, metallic, puff, embossed)

### Step 3: AI Prompts

Generate platform-specific prompts for:
- **Kittl Image Board** — The design itself (use building blocks formula)
- **Midjourney** — Reference/inspiration image
- **Flux Pro** — Photorealistic product mockup
- **Kittl Video Board** (optional) — Animated version (CAMERA/ACTION/AUDIO/TEXT format)

### Step 4: Production Specs

- **File format** (AI, PSD, PNG, SVG, PDF)
- **Resolution** (300 DPI for print, 72 DPI for digital, 150 DPI for large format)
- **Color mode** (CMYK for print, RGB for digital, Pantone for brand colors)
- **Bleed and safe zone** (for print — typically 0.125" bleed, 0.25" safe)
- **Placement dimensions** (for apparel — width, height, position from collar)
- **Print method recommendation** with reasoning (cost, look, feel, quantity)

## Output Format

```
## Design Direction: [Concept]
**Type:** [Deliverable] | **Archetype:** [Style] | **Print:** [Method]

### Visual Direction
[Complete design description with specific references — movements, artists, brands]

### Color Palette
| Color | Hex | Pantone | Role |
|---|---|---|---|
[Colors with usage rules]

### Typography
**Primary:** [Font, weight, size, usage]
**Secondary:** [Font, weight, size, usage]
**Rules:** [Spacing, case, alignment]

### Composition
[Layout description with placement guide]
[For apparel: position from collar, width, height]

### AI Prompts
**Kittl Image:** [Full prompt]
**Midjourney Reference:** [Full prompt with parameters]
**Flux Mockup:** [Full prompt with camera specs]
**Video (optional):** [CAMERA/ACTION/AUDIO/TEXT]

### Production Specs
**Format:** [File type]
**Resolution:** [DPI]
**Color Mode:** [CMYK/RGB/Pantone]
**Bleed:** [If applicable]
**Placement:** [If apparel]
**Print Method:** [Recommendation + reasoning]
```

## Streetwear-Specific Notes

- Apply the Virgil Test to every design: tension? POV? one-sentence concept?
- Reference the 5 graphic archetypes — know which one you're using and why
- Color palette construction: start black > add signature > add neutral > optional accent
- Test on black garments first
- Consider the mockup hierarchy: editorial > on-model environmental > on-model studio > ghost mannequin > flat lay
