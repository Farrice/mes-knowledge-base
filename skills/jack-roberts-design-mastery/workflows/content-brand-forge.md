# Content Brand Forge

> Build a personal DESIGN.md for your content brand — auto-generate branded carousel templates, newsletter headers, and social graphics that are visually distinctive across platforms.

## Context Required
- **Load First**: `genius.md` — Jack Roberts' 5-Step System + DESIGN.md pattern
- **Complementary**: `/design-philosophy-architect` for aesthetic direction, `/multi-format-deploy` for cross-platform templates

## When to Use
- Building or refreshing your personal content brand's visual identity
- You want every piece of content to be instantly recognizable before anyone reads a word
- You need consistent visual templates across LinkedIn, Substack, Twitter/X, Instagram
- You want to stop making ad-hoc design decisions for every post

## The Insight
> Content creators who are visually distinctive get recognized in the scroll. Your words compete with everyone. Your visual language competes with almost no one. A DESIGN.md for your content brand creates compounding recognition — every post reinforces the same visual identity.

## Inputs
- **Required**: Your content niche and positioning (who you are, who you serve)
- **Required**: Primary platforms (LinkedIn, Substack, Twitter/X, Instagram, YouTube, etc.)
- **Optional**: Brands/creators whose visual style you admire
- **Optional**: Existing brand elements (colors, fonts, logo you already use)
- **Optional**: Content types you create most (carousels, text posts, long-form, video thumbnails)

## Workflow

### Phase 1: Brand Identity Audit

1. **Audit what exists today:**
   - Do you have consistent colors across platforms?
   - Is your profile photo/avatar the same everywhere?
   - Do your posts have a recognizable visual style?
   - If someone saw your content without your name, would they know it's you?

2. **Define the brand persona:**
   ```
   Brand Name:      [Your name / brand name]
   Positioning:     [What you do + who it's for, in one sentence]
   Visual Mood:     [3 adjectives — e.g., "bold, clean, intellectual"]
   Anti-Mood:       [3 things you're NOT — e.g., "not corporate, not flashy, not templated"]
   Aspirational:    [3 brands/creators whose visuals you admire]
   ```

3. **Platform inventory:**
   | Platform | Content Type | Visual Format | Current Consistency (1-10) |
   |----------|-------------|---------------|---------------------------|
   | LinkedIn | Carousels, text posts | Headers, carousel slides | ___ |
   | Substack | Newsletter | Header image, pullquotes | ___ |
   | Twitter/X | Text, images | Header cards, thread visuals | ___ |
   | Instagram | Carousels, Stories | Grid aesthetic, story templates | ___ |
   | YouTube | Videos | Thumbnails, end screens | ___ |

### Phase 2: Content DESIGN.md Construction

Run `/design-system-forge` with content-brand-specific parameters:

```markdown
# Content Brand Design System: [Your Name]

## 1. Visual Identity
- **Primary Mark**: [Logo/avatar — describe or reference]
- **Brand Recognition Element**: [The ONE visual thing that's uniquely yours]
  - Could be: a signature color, a border style, a typography choice, an icon set
- **Mood**: [From Phase 1 — the feeling your content should evoke]

## 2. Color Palette (Content-Optimized)
- **Brand Primary**: #______ — [Used: headers, accent elements, carousel title slides]
- **Brand Secondary**: #______ — [Used: supporting graphics, section dividers]
- **Background Light**: #______ — [LinkedIn/Substack light theme]
- **Background Dark**: #______ — [Dark mode / video thumbnails]
- **Text Primary**: #______ — [Body text — must be readable on both backgrounds]
- **Highlight/Accent**: #______ — [Call-out boxes, key stats, emphasis]

NOTE: Limit to 4-5 colors. More = visual noise. Fewer = stronger recognition.

## 3. Typography (Platform-Safe)
- **Headlines**: [Font] — Bold, used in carousel titles and headers
- **Body**: [Font] — Regular, readable at mobile sizes
- **Accent/Callout**: [Font] — Used for quotes, stats, emphasis

NOTE: Choose fonts available on Canva + Google Fonts for maximum portability.

## 4. Content Templates
### Carousel Slides
- Dimensions: 1080×1350 (LinkedIn) / 1080×1080 (Instagram)
- Title slide: Brand color background, white text, logo at bottom
- Content slides: White/light background, dark text, accent color for emphasis
- Final slide: CTA + your handle/link

### Newsletter Header
- Dimensions: 1200×300
- Elements: Brand logo, edition number or title, date
- Treatment: Clean, not busy — the header is branding, not content

### Social Post Cards
- Dimensions: 1200×628 (LinkedIn/Twitter)
- Layout: Single key statement + brand visual treatment
- Text overlay: Headline font, high contrast against background

### Video Thumbnails
- Dimensions: 1280×720
- Elements: Face photo, 3-5 word title, brand color accent
- Treatment: High contrast, readable at mobile thumbnail size

## 5. Anti-Slop Rules for Content
- Never use default Canva template colors
- No generic stock photos — use brand photography style or none
- Every piece must include at least ONE brand recognition element
- Text-heavy posts still get visual treatment (pullquote cards, not just text)
- Consistency > perfection — match the system, even imperfectly
```

### Phase 3: Template Generation

Generate these starter templates using the Content DESIGN.md:

1. **LinkedIn carousel** (10 slides — populate with sample content)
2. **Newsletter header** (one master header)
3. **Social post card** (3 variations for different content types)
4. **Video thumbnail** (2 variations — with face and without face)

All templates as HTML files that can be screenshotted, exported, or modified.

### Phase 4: Cross-Platform Consistency Test

Place all generated templates side-by-side:

| Test | Pass/Fail |
|------|-----------|
| Do they look like they come from the same person? | ___ |
| Is the brand color used consistently (not randomly)? | ___ |
| Is the typography consistent across formats? | ___ |
| Could someone identify these as yours without your name? | ___ |
| Do they stand out in a feed scroll? | ___ |

Fix any failures before finalizing.

### Phase 5: Enshrinement

1. Save the Content DESIGN.md as a permanent skill file
2. Run `/design-skill-enshrine` so all future content automatically uses this system
3. Create a quick-reference card:
   ```
   My Brand Colors:  #______, #______, #______
   My Fonts:         [headline], [body]
   My Signature:     [the ONE recognizable element]
   Template Location: [path to generated templates]
   ```

## Output
- Content Brand `DESIGN.md` — permanent design system for your content
- Template library (carousel, header, card, thumbnail templates)
- Cross-platform consistency report
- Quick-reference brand card
- Enshrined skill file for one-command future generation

## The Compounding Effect
```
Week 1:   Templates look new — you're getting used to them
Week 4:   Your feed has visual consistency — followers notice the pattern
Week 12:  Your content is recognizable at a glance — brand equity compounds
Week 26:  People screenshot YOUR posts as examples of "good design" — you've become a reference
```
