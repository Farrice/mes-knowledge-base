# Design System Forge

> Create a complete DESIGN.md from scratch, from brand references, or from an existing website — the foundational artifact that powers every other design workflow.

## Context Required
- **Load First**: `genius.md` — Jack Roberts' 5-Step Design System and Anti-Slop Architecture
- **Complementary**: `skills/design-md/SKILL.md` for Stitch-format DESIGN.md structure

## Inputs
- **Option A — From Brand URL**: A website URL to extract design language from
- **Option B — From References**: 2-5 visual references the user admires (screenshots, URLs, mood boards)
- **Option C — From Scratch**: A verbal description of the desired aesthetic, audience, and purpose
- **Option D — From Library (Fast Path)**: Fork a pre-built DESIGN.md from awesome-design-md (55+ brands, Google Stitch format). See `/design-library-import` for the full fork-and-customize workflow. Use this when the target brand exists in the library or when you want a proven starting point before customizing.

## Workflow

### Phase 1: Design Intelligence Gathering

**If starting from a URL (Option A):**
1. Use Firecrawl or web scraping to extract from the target URL:
   - Logo files and brand marks
   - Complete color palette (primary, secondary, accent, neutrals) with exact hex codes
   - Typography families (headings, body, accent, monospace)
   - Spacing patterns and grid structure
   - Component patterns (buttons, cards, navigation, forms)
   - Shadow and depth treatment
   - Border radius patterns
   - Animation/transition patterns
2. Take a full-page screenshot for visual reference
3. Document the overall "atmosphere" — mood, density, visual weight

**If starting from references (Option B):**
1. Analyze each reference for:
   - What makes it visually excellent (specific, not generic)
   - Color patterns that recur across references
   - Typography choices and their emotional effect
   - Spatial rhythm — how dense vs. airy
   - What design "rules" the references share
2. Synthesize a unified design direction from the common patterns
3. Identify the 2-3 signature elements that differentiate this from AI defaults

**If starting from scratch (Option C):**
1. Ask the user clarifying questions:
   - What is this for? (audience, purpose, context)
   - Name 3 brands/sites whose visual quality you admire
   - What emotion should someone feel? (not "modern" — that's meaningless)
   - Any absolute constraints? (brand colors, fonts, legal requirements)
2. Research 5-8 excellent examples in the target space
3. Present 3 distinct aesthetic directions with rationale

### Phase 2: DESIGN.md Construction

Build the DESIGN.md file with these mandatory sections:

```markdown
# Design System: [Project/Brand Name]

## 1. Visual Theme & Atmosphere
[2-3 paragraphs describing the overall mood, aesthetic philosophy, and the
emotional response the design should evoke. Use evocative adjectives.
Reference specific design movements or influences.]

## 2. Color Palette & Roles
### Primary
- **[Descriptive Name]** (#hex) — [Functional role: primary actions, headers, etc.]

### Secondary
- **[Descriptive Name]** (#hex) — [Functional role]

### Accent
- **[Descriptive Name]** (#hex) — [Functional role]

### Neutrals
- **[Descriptive Name]** (#hex) — [Background, dark text, light text, borders, subtle fills]

### Status Colors
- Success: **[Name]** (#hex)
- Warning: **[Name]** (#hex)
- Error: **[Name]** (#hex)
- Info: **[Name]** (#hex)

## 3. Typography Rules
### Font Stack
- **Display/Headings**: [Font family], [weight range], [letter-spacing]
- **Body**: [Font family], [weight range], [line-height]
- **Accent/Labels**: [Font family], [weight], [text-transform]
- **Code/Mono**: [Font family]

### Scale
- H1: [size] / [line-height] / [weight] / [letter-spacing]
- H2: [size] / [line-height] / [weight]
- H3: [size] / [line-height] / [weight]
- Body Large: [size] / [line-height]
- Body: [size] / [line-height]
- Small/Caption: [size] / [line-height]

## 4. Component Styles
### Buttons
- **Primary**: [background, text color, border-radius, padding, hover state]
- **Secondary**: [specifications]
- **Ghost/Outline**: [specifications]

### Cards & Containers
- [Border-radius, background, shadow, padding, border treatment]

### Inputs & Forms
- [Height, border style, focus state, label positioning, error state]

### Navigation
- [Structure, active states, mobile treatment]

## 5. Layout Principles
- **Max Content Width**: [value]
- **Grid**: [columns, gutter, breakpoints]
- **Section Spacing**: [vertical rhythm between major sections]
- **Component Spacing**: [standard gaps between elements]
- **Responsive Strategy**: [mobile-first/desktop-first, key breakpoints]

## 6. Imagery & Iconography
- **Photo Style**: [treatment, filters, aspect ratios]
- **Icon Style**: [line/filled, stroke weight, size system]
- **Illustration**: [style, color usage]

## 7. Motion & Animation
- **Timing Function**: [easing curve]
- **Standard Duration**: [ms]
- **Entrance Animations**: [description]
- **Hover/Interaction**: [description]
- **Scroll Behavior**: [description]

## 8. Anti-Slop Rules
[Explicit list of what this design system must NEVER do — the AI default
patterns that would make this look generic. Be specific.]
```

### Phase 3: Validation

Run the completed DESIGN.md through these checks:
1. **Completeness**: Every section filled with specific values (no TBDs)
2. **Anti-Slop**: Does the design system have at least 3 features that distinguish it from AI defaults?
3. **Implementability**: Could a developer build a component with only this document?
4. **Coherence**: Do color, typography, and spacing choices tell a unified visual story?
5. **Brand Fidelity** (if from URL): Side-by-side comparison against source

## Output
- `DESIGN.md` — Complete design system specification
- Optional: `design-references/` folder with collected visual references
- Quality Score: Rate 1-10 on Brand Fidelity, Visual Sophistication, Anti-Slop, System Coherence, Implementability
