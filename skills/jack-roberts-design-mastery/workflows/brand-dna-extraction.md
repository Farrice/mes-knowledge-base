# Brand DNA Extraction

> Extract a brand's exact visual identity from its live website — logos, colors, typography, components — so the AI can replicate it with pixel accuracy.

## Context Required
- **Load First**: `genius.md` — Brand DNA Extraction pattern (Genius Pattern #4)

## Inputs
- **Required**: Target brand URL (e.g., `stripe.com`, `apple.com`, `nike.com`)
- **Optional**: Specific pages to analyze (homepage, pricing, about, product pages)
- **Optional**: What you need extracted (full system vs. specific elements)

## Workflow

### Step 1: Full-Page Reconnaissance
1. Navigate to the target URL
2. Capture full-page screenshots of:
   - Homepage (above the fold + full scroll)
   - One product/feature page
   - Pricing page (if exists)
   - Footer and navigation states
3. Record: overall atmosphere, density, visual weight, mood

### Step 2: Color Extraction
Extract every meaningful color from the CSS/HTML:

```
Primary Brand Color:    #______ — [where it appears]
Secondary Color:        #______ — [where it appears]  
Accent/CTA Color:       #______ — [where it appears]
Background(s):          #______ — [light mode], #______ — [dark mode]
Text Primary:           #______ — [headings/body]
Text Secondary:         #______ — [captions/muted]
Border/Divider:         #______ — [lines/separators]
Gradient(s):            [from] → [to] — [where used]
```

**Validation:** Check extracted colors against the actual rendered site. Are they exact?

### Step 3: Typography Extraction
Identify every font in use:

```
Display Font:     [Family] — [Where: hero headlines, section titles]
Heading Font:     [Family] — [Weight range: 600-800]
Body Font:        [Family] — [Weight: 400, Line-height: 1.5-1.7]
Accent Font:      [Family] — [Labels, buttons, navigation]
Mono Font:        [Family] — [Code blocks, technical content]
```

Extract the complete type scale:
- Hero headline size and weight
- Section heading sizes (H1-H4)
- Body text size and line-height
- Caption/small text
- Button text size and weight
- Navigation text style

### Step 4: Logo & Brand Mark Extraction
1. Extract the logo from the site (SVG preferred, PNG fallback)
2. Document logo variations found (light/dark, icon-only, full wordmark)
3. Note logo placement conventions (header position, footer usage, sizing)
4. Extract favicon and any secondary brand marks

### Step 5: Component Pattern Library
Analyze and document the styling of key components:

**Buttons:**
- Primary CTA: border-radius, padding, font-weight, background, hover state
- Secondary: same treatment
- Link/text buttons: color, underline behavior

**Cards:**
- Border-radius, shadow depth, padding, background, hover effect
- Image treatment within cards (aspect ratio, border-radius, overlay)

**Navigation:**
- Header height, background, scroll behavior (sticky? blur?)
- Nav link style, active state, mobile hamburger pattern

**Forms:**
- Input height, border style, border-radius, focus ring color
- Label positioning (above/floating/inline)

**Sections:**
- Vertical spacing between major sections
- Horizontal max-width and padding
- Background alternation pattern (white/gray/colored)

### Step 6: Spatial & Layout DNA
- **Grid system**: Column count, gutter width, max content width
- **Spacing scale**: What multiples of base unit are used? (4px, 8px, 16px, etc.)
- **Section rhythm**: How much vertical space between sections?
- **Responsive approach**: Key breakpoints, mobile adaptation strategy
- **Negative space philosophy**: Dense and information-rich or airy and minimal?

### Step 7: Motion & Micro-Interaction DNA
- Scroll animations (fade-in, slide-up, parallax?)
- Hover effects on interactive elements
- Transition durations and easing curves
- Loading states and skeleton patterns
- Page transition approach

### Step 8: Compile Brand DNA Package

Produce a complete `DESIGN.md` using the Design System Forge format, plus:

```markdown
## Brand DNA Source
- **Extracted From**: [URL]
- **Extraction Date**: [Date]
- **Pages Analyzed**: [List]
- **Confidence Level**: [High/Medium/Low — based on access and completeness]

## Brand Personality Notes
[2-3 sentences on what the brand's visual language communicates about
its values, market position, and target audience]

## Replication Guidelines
[Specific instructions for reproducing this brand's look in generated output.
What is the #1 thing that makes this brand visually distinctive?]
```

## Output
- `DESIGN.md` — Complete design system extracted from the brand
- `brand-assets/` — Extracted logos, screenshots, reference images
- Confidence assessment: How complete is the extraction?
