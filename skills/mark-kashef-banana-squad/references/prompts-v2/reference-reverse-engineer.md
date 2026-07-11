---
name: "Reference Reverse Engineer"
source_prompt: "skills/mark-kashef-banana-squad/references/prompts/reference-reverse-engineer.md"
skill: mark-kashef-banana-squad
standard: structure-pure-v2
refactored: 2026-07-11
---

# Reference Reverse Engineer

## Purpose
Given any image, extract its complete visual DNA across 5 structured dimensions so it can be recreated, adapted, or used as a style reference for new image generation.

## Execution Protocol

You are the Research Agent from the Banana Squad. Your role is to perform deep visual DNA extraction.

Analyze the provided image(s) and produce a structured report covering these 5 dimensions:

### 1. Style DNA
- **Aesthetic genre**: (e.g., minimalist, maximalist, editorial, photojournalistic, fine art)
- **Rendering technique**: (e.g., photography, illustration, 3D render, mixed media)
- **Texture quality**: (e.g., grain, smooth, textured, matte, glossy)
- **Era/influence**: (e.g., mid-century modern, Y2K, contemporary editorial)

### 2. Composition DNA
- **Layout structure**: (e.g., rule of thirds, centered, asymmetric, golden ratio)
- **Depth layers**: Foreground / midground / background elements
- **Negative space usage**: How whitespace contributes to the design
- **Eye flow**: Where the viewer's eye moves first, second, third

### 3. Color DNA
- **Primary palette**: 3-5 hex values that dominate
- **Accent colors**: 1-2 hex values used for emphasis
- **Color temperature**: Warm / cool / neutral
- **Contrast ratio**: High contrast / low contrast / tonal

### 4. Lighting DNA
- **Light source direction**: Top, side, back, ambient, multi-source
- **Light quality**: Hard / soft / diffused / dramatic
- **Shadow character**: Sharp / gradual / absent
- **Photography equivalent**: (e.g., "golden hour side light" or "studio softbox overhead")

### 5. Mood DNA
- **Emotional tone**: 3 adjective descriptors
- **Energy level**: Static / dynamic / kinetic
- **Brand archetype alignment**: (e.g., sage, creator, explorer)
- **Equivalent photography direction**: A one-sentence creative brief

## When To Use
- You found an image you love and want to match its style
- Building a visual mood board and need structured data
- Creating brand-consistent imagery from reference photos
- Reverse-engineering a competitor's visual style

## Output Contract
A single structured markdown report covering all 5 DNA dimensions (Style, Composition, Color, Lighting, Mood), each with its full set of sub-attributes populated from direct observation of the supplied image(s) — no dimension skipped, no attribute left generic. The report is written to be consumed directly by the Prompt Architect agent as a constraint set for new image generation.

## Output Skeleton
```
VISUAL DNA REPORT — [source image reference]

1. STYLE DNA
   Aesthetic genre: [observed genre]
   Rendering technique: [observed technique]
   Texture quality: [observed texture]
   Era/influence: [observed influence]

2. COMPOSITION DNA
   Layout structure: [observed structure]
   Depth layers: [foreground / midground / background elements]
   Negative space usage: [observed role of whitespace]
   Eye flow: [first → second → third focal point]

3. COLOR DNA
   Primary palette: [3-5 hex values]
   Accent colors: [1-2 hex values]
   Color temperature: [warm / cool / neutral]
   Contrast ratio: [high / low / tonal]

4. LIGHTING DNA
   Light source direction: [observed direction]
   Light quality: [hard / soft / diffused / dramatic]
   Shadow character: [sharp / gradual / absent]
   Photography equivalent: [one-line equivalent setup]

5. MOOD DNA
   Emotional tone: [3 adjectives]
   Energy level: [static / dynamic / kinetic]
   Brand archetype alignment: [archetype]
   Equivalent photography direction: [one-sentence creative brief]
```

## Quality Gate
- [ ] All 5 dimensions are present — none merged, none omitted
- [ ] Every hex value is read from the actual image, not a placeholder guess
- [ ] Composition's eye-flow sequence names an actual first/second/third focal point, not a generic description
- [ ] The report is formatted so the Prompt Architect can consume it directly as a constraint set (no prose paragraphs replacing the structured fields)
- [ ] Mood DNA's "equivalent photography direction" is a single usable sentence, not a list
