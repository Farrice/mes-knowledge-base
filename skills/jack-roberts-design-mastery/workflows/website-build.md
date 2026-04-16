# Website Build

> Build a production-ready website or landing page using a DESIGN.md design system — one-shot quality that passes the Anti-Slop test.

## Context Required
- **Load First**: `genius.md` — 5-Step Design System, Anti-Slop Architecture
- **Required Input**: A `DESIGN.md` file (create one first via `/design-system-forge` or `/brand-extraction`)
- **Pipeline Partner**: `sean-kochel-design-first-build` for competitive research phase

## Inputs
- **Required**: DESIGN.md file (or brand reference to extract from)
- **Required**: Site purpose (landing page, product page, portfolio, SaaS marketing, etc.)
- **Required**: Key content sections needed (hero, features, pricing, testimonials, CTA, footer)
- **Optional**: Copy/content to include
- **Optional**: Specific pages beyond homepage

## Workflow

### Phase 1: Design System Verification
Before writing a single line of code:

1. **Confirm DESIGN.md exists and is complete** — all 8 sections filled
2. **Identify the 3 Anti-Slop differentiators** — what makes this NOT look like every AI site?
3. **Define the conversion goal** — what should visitors DO?
4. **Establish page structure** — ordered list of sections with purpose:
   ```
   1. Navigation — [sticky/static, transparent/solid]
   2. Hero — [headline, subheadline, CTA, visual]
   3. Social Proof — [logos, testimonials, numbers]
   4. Features/Benefits — [3-6 items, layout style]
   5. How It Works — [steps, process flow]
   6. Testimonials — [format, number]
   7. Pricing — [tiers, comparison]
   8. Final CTA — [urgency, value prop summary]
   9. Footer — [links, legal, contact]
   ```

### Phase 2: Build Specification
Create a build spec that maps DESIGN.md tokens to each section:

For each section, specify:
- **Layout**: Grid structure, alignment, responsive behavior
- **Colors**: Which DESIGN.md palette colors apply
- **Typography**: Which type scale levels for each text element
- **Spacing**: Vertical padding, internal gaps
- **Components**: Which component styles from DESIGN.md
- **Imagery**: What visual content is needed (generate or placeholder)
- **Animation**: Entrance effects, hover states, scroll triggers

### Phase 3: Code Generation
Build the complete site as a self-contained HTML file (or framework of choice):

**Technical Requirements:**
- Semantic HTML5 structure
- CSS using design tokens from DESIGN.md (CSS custom properties preferred)
- Responsive: mobile-first, tested at 375px, 768px, 1024px, 1440px
- Smooth scroll behavior
- Intersection Observer for scroll animations
- Optimized image loading (lazy-load below fold)
- Accessible: proper heading hierarchy, ARIA labels, keyboard navigation
- SEO: meta tags, Open Graph, structured heading hierarchy

**Code Quality Standards:**
- Every color references a DESIGN.md token — NO hard-coded hex values outside the system
- Every font-size references the type scale — NO arbitrary pixel values
- Every spacing value follows the spacing scale — NO random padding
- Every component matches its DESIGN.md specification exactly

### Phase 4: Anti-Slop Validation
Before presenting the build, run these checks:

| Check | Pass Criteria |
|-------|--------------|
| **No purple gradients** | Unless specified in DESIGN.md |
| **No Inter font** | Unless specified in DESIGN.md |
| **No three-column rounded boxes** | Unless that's genuinely the best layout |
| **Custom color palette** | Colors trace to DESIGN.md, not AI defaults |
| **Unique hero treatment** | Not the standard left-text/right-image split |
| **Real visual hierarchy** | Clear primary→secondary→tertiary reading order |
| **Intentional negative space** | Whitespace is designed, not leftover |
| **Micro-interactions present** | Hover states, transitions, scroll effects |
| **Typography has personality** | Weight, spacing, size variation creates rhythm |
| **Mobile isn't an afterthought** | Mobile layout is deliberately designed, not just stacked |

### Phase 4.5: Image Generation (Optional)

If the site needs custom visuals (hero images, illustrations, icons):

1. **Identify image needs** — list every visual element that can't be text/CSS alone
2. **Generate via Kia API** (Nano Banana 2, ~$0.06/image):
   - Write prompts that match the DESIGN.md mood and color palette
   - Generate 2-3 options per image slot
   - Select the one that best fits the brand personality
3. **Optimize**: proper dimensions, lazy-loading, alt text
4. **Never use stock placeholders** in the final output — generate or photograph

### Phase 5: Serve & Present
1. Start a local development server
2. Open in browser at correct viewport
3. Screen-capture key sections for the user to review
4. Present with a brief summary: "Here's what I built and which DESIGN.md tokens drove each decision"

## Output
- Complete website codebase (HTML/CSS/JS)
- Local dev server running for preview
- Anti-Slop scorecard (pass/fail on each criterion)
- Design decision log: which DESIGN.md tokens mapped to which elements
