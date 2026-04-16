# Multi-Format Deploy

> Take one DESIGN.md and express it across every format your business needs — websites, presentations, social graphics, reports, and brand assets, all visually unified.

## Context Required
- **Load First**: `genius.md` — Codify-Once-Replicate-Infinitely (Genius Pattern #1)
- **Required**: A completed DESIGN.md (via `/design-system-forge` or `/brand-extraction`)

## Inputs
- **Required**: DESIGN.md file to deploy across formats
- **Required**: Which formats to produce (select 2+):
  - [ ] Website / Landing Page
  - [ ] HTML Presentation / Slide Deck
  - [ ] Social Media Templates (LinkedIn, Instagram, Twitter)
  - [ ] PDF Report / Proposal
  - [ ] Email Template
  - [ ] Brand Identity Kit (logo lockup, business card, letterhead)
  - [ ] Data Visualization / Dashboard
  - [ ] Infographic
- **Optional**: Format-specific content to include
- **Optional**: Priority order (which format first)

## Workflow

### Phase 1: Design System Audit for Multi-Format Readiness

Before deploying, verify the DESIGN.md covers multi-format needs:

```
□ Color palette has enough depth (≥ 8 colors including neutrals)
□ Typography has ≥ 3 distinct levels (display, heading, body)  
□ Spacing system scales properly (works for both dense and airy formats)
□ Component styles are described abstractly (not page-specific)
□ Brand marks are available in multiple formats (full, icon, monochrome)
□ Motion/animation rules exist (can be adapted per format)
```

If gaps exist, fill them from the DESIGN.md before proceeding.

### Phase 2: Format-Specific Token Mapping

For each selected format, map DESIGN.md tokens to format-specific rules:

#### Website Token Map
```
DESIGN.md Token     →  Website Application
─────────────────────────────────────────
Display typography  →  Hero headline (48-72px)
H1                  →  Section titles (36-48px)
Body                →  Content text (16-18px)
Primary color       →  CTA buttons, links
Background          →  Page background
Section spacing     →  Vertical padding between sections (80-120px)
Card style          →  Feature cards, testimonial cards
```

#### Presentation Token Map
```
DESIGN.md Token     →  Presentation Application
─────────────────────────────────────────
Display typography  →  Slide titles (32-48px)
H2                  →  Key statements (24-36px)
Body Large          →  Bullet points (20-24px, max 6 per slide)
Primary color       →  Accent bars, highlights
Background          →  Slide background (may alternate)
Section spacing     →  Slide transitions
```

#### Social Media Token Map
```
DESIGN.md Token     →  Social Application
─────────────────────────────────────────
Display typography  →  Quote/headline text (bold, large)
Body                →  Supporting context (smaller, lighter)
Primary color       →  Background or accent element
Accent color        →  Highlight text, icons
Card style          →  Post container shape
Brand mark          →  Watermark/attribution (corner)
```

#### Report/Proposal Token Map
```
DESIGN.md Token     →  Report Application
─────────────────────────────────────────
H1                  →  Chapter/section titles
H2                  →  Subsection headings
Body                →  Main content (12-14px, longer line-length)
Primary color       →  Section headers, table headers
Accent color        →  Data visualization, callout boxes
Card style          →  Info boxes, sidebars
```

### Phase 3: Parallel Production

Build each format using its specific token map:

For each format:
1. Apply the format-specific token map
2. Generate the design using the appropriate workflow:
   - Website → `/website-build`
   - Presentation → `/presentation-build`
   - Social → Generate as HTML card (1080x1080, 1200x628, 1080x1920)
   - Report → Generate as HTML with print CSS
   - Email → Generate as inline-styled HTML
   - Brand kit → Generate as SVG/PNG compositions
3. Validate format-specific requirements
4. Run Anti-Slop audit on each output

### Phase 3.5: Image Generation Per Format

For formats that need custom visuals (website heroes, presentation backgrounds, social graphics):

1. Generate via **Kia API** (Nano Banana 2, ~$0.06/image)
2. Write prompts that reference the DESIGN.md mood and color palette
3. Ensure the same illustration style carries across formats — consistency includes imagery, not just layout
4. Never use different stock photo styles across formats — one visual language everywhere

### Phase 3.6: Emotional Consistency Check (Optional — Stack with Hoffman)

If deploying a brand where emotional resonance matters:

1. Run `/emotional-value` to define the brand's emotional core
2. Map emotions to design tokens: Which colors evoke the target feeling? Which typography personality?
3. Verify each format communicates the same emotion — a presentation shouldn't feel "corporate" if the website feels "warm"

### Phase 4: Cross-Format Consistency Check

Place all generated formats side-by-side and verify:

| Check | Standard |
|-------|----------|
| **Color match** | Same hex values used across all formats |
| **Typography match** | Same font families and weight patterns |
| **Mood match** | Same emotional response from all formats |
| **Logo consistency** | Same logo version and placement logic |
| **Quality parity** | No format feels "lesser" than others |
| **Brand recognition** | Removing labels — could you tell these are the same brand? |

### Phase 5: Package Delivery

Organize all outputs into a cohesive delivery:

```
[brand-name]-design-system/
├── DESIGN.md                 # The source of truth
├── website/
│   ├── index.html
│   └── assets/
├── presentations/
│   └── template.html
├── social/
│   ├── linkedin-post.html    # 1200x628
│   ├── instagram-square.html # 1080x1080
│   └── instagram-story.html  # 1080x1920
├── reports/
│   └── template.html
├── email/
│   └── template.html
├── brand-kit/
│   ├── logo-dark.svg
│   ├── logo-light.svg
│   ├── color-swatches.html
│   └── typography-specimen.html
└── README.md                 # Usage guide for all formats
```

## Output
- Complete multi-format design package
- Cross-format consistency report
- Per-format Anti-Slop scores
- Usage guide for reproducing any format on demand
