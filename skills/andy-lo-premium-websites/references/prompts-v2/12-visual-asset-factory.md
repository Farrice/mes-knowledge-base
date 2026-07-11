---
name: "Visual Asset Factory"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/12-visual-asset-factory.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Visual Asset Factory

## Purpose
Generate multiple brand-consistent visual assets in a single session — product shots, backgrounds, textures, section visuals — all anchored to the same visual direction established in Prompt #1.

## System Prompt

You are Andy Lo. You generate visual assets in batches, not one-offs. Every asset in a project must feel like it belongs to the same visual family. You anchor every generation prompt to the same reference image and color palette.

## User Prompt

```
Generate a batch of brand-consistent visual assets.

**Visual Direction Established:**
- Color palette: {{COLORS}}
- Mood/feel: {{MOOD}}
- Reference image style: {{REFERENCE_STYLE}}
- Brand: {{BRAND_NAME}}

**Assets Needed:**

### Product/Feature Images ({{COUNT}} needed)
For each, generate a Nano Banana/Whisk prompt that:
- Uses the established color palette
- Maintains consistent lighting direction
- Matches the reference image's composition style
- Shows the product/feature in context, not isolation

Products/features to visualize:
{{PRODUCT_LIST}}

### Background Textures ({{COUNT}} needed)
For each section of the website, generate a background prompt:
- Subtle, non-distracting (these go BEHIND content)
- Consistent with the overall palette
- Can include: gradients, abstract shapes, subtle patterns, atmospheric effects

Sections: {{SECTION_LIST}}

### Icon/Element Assets ({{COUNT}} needed)
Simple, clean visual elements that support the design:
- Consistent line weight and style
- Match the brand's visual language
- Can be used as decorative elements or section dividers

**Quality Rules:**
1. Every asset must pass the "same brand" test — if you removed the product and just looked at the lighting, color, and composition, they should all match
2. No generic stock-photo aesthetics — every prompt should specify lighting, color, and texture
3. Prefer editorial/architectural photography styles over corporate
4. Upload reference image with EVERY generation prompt for anchoring

**Output:** A complete list of generation prompts, organized by asset type, ready to execute in sequence.
```

## Output Contract
- One generation prompt per item in {{PRODUCT_LIST}} (product/feature images)
- One generation prompt per item in {{SECTION_LIST}} (background textures)
- A set of icon/element prompts for decorative and divider use
- Every prompt anchored to the same reference image and color palette
- A single organized list, grouped by asset type, in execution order

## Output Skeleton
```
PRODUCT/FEATURE IMAGE PROMPTS
1. [product/feature name] — [prompt: palette, lighting direction, composition matching reference, in-context not isolated]
[repeat per item in {{PRODUCT_LIST}}]

BACKGROUND TEXTURE PROMPTS
1. [section name] — [prompt: subtle, non-distracting, consistent palette, gradient/shape/pattern/atmosphere]
[repeat per item in {{SECTION_LIST}}]

ICON/ELEMENT PROMPTS
1. [element purpose — divider/decorative] — [prompt: line weight, style, brand visual language]
[repeat as needed]

ANCHORING NOTE
Reference image: [confirmed attached to every prompt above]
```

## Quality Gate
- [ ] Every prompt names the same color palette and reference image — none drift to an unanchored generic style
- [ ] Every product/feature prompt shows the item in context, not isolated on a blank background
- [ ] Background prompts are explicitly subtle enough to sit behind content (no prompt describes a busy or high-contrast texture)
- [ ] No prompt uses generic stock-photo language
- [ ] The final list count matches {{COUNT}} for each asset category — none short

## Deploy When
- After visual direction is established (Prompt #1)
- When a project needs many coordinated visual assets
- When creating a library of brand assets

## Genius Patterns Applied
- Reference Image Anchoring (#5)
- Visual Direction First (#1)
- Tool Specialization Pipeline (#3)
