# Brand-in-a-Box

> Package the entire design pipeline as a productized service: "I'll build your complete code-first design system in 48 hours." Client gets a DESIGN.md, sample website, presentation template, and social media templates — all visually unified.

## Context Required
- **Load First**: `genius.md` — Full 5-Step System + Anti-Slop Architecture
- **Required Workflows**: `/brand-dna-extraction`, `/design-system-forge`, `/website-build`, `/presentation-build`, `/multi-format-deploy`, `/anti-slop-audit`
- **This is a compound workflow** — it orchestrates 6+ sub-workflows into a single deliverable

## When to Use
- Selling brand design systems as a productized service ($2,500-$5,000)
- A client needs a complete visual identity operationalized for AI-generated output
- You want to demonstrate the full power of code-first design in a single engagement
- Building a "tangible faucet" offer for repeatable revenue

## The Offer
```
BRAND-IN-A-BOX — Complete Code-First Design System

What you get:
✅ DESIGN.md — Your complete visual language in one file
✅ Sample website — Full landing page in your brand
✅ Presentation template — Interactive HTML slide deck
✅ Social media templates — 3 formats (post, carousel, story)
✅ Anti-Slop Certification — Verified unique, not generic

Turnaround: 48 hours
Investment: $2,500 (standard) / $5,000 (premium with revisions)
```

## Inputs
- **Required**: Client's website URL (existing brand to systematize) OR brand brief (new brand to create)
- **Required**: Primary use case (what they create most — presentations? social content? internal docs?)
- **Optional**: Aspirational brands they admire (for aesthetic direction)
- **Optional**: Meeting/call recording for context

## Workflow

### Hour 0-4: Discovery & Extraction

1. **Client intake:**
   - What does their business do? Who do they serve?
   - What content do they create most often? (identifies highest-leverage format)
   - What brands do they admire visually? (establishes taste direction)
   - Any existing brand guidelines? (don't reinvent what exists)

2. **Brand DNA Extraction** (`/brand-dna-extraction`):
   - Extract from their existing website
   - If no website: Run `/reference-collection-sprint` → `/design-philosophy-architect` to establish direction from scratch

3. **Competitive scan** (comparison mode):
   - Extract 2 competitor brands
   - Build the Contrast Map
   - Identify visual whitespace for differentiation

### Hour 4-12: DESIGN.md Construction

1. **Run `/design-system-forge`** — build the master DESIGN.md:
   - Option A (from URL) if they have a site
   - Option D (from library) if their aesthetic matches an awesome-design-md template
   - Option C (from scratch) if building new

2. **Anti-Slop hardening:**
   - Add at least 5 explicit "never do this" rules
   - Ensure every token is specific (no "modern blue" — exact hex codes)
   - Validate the DESIGN.md produces distinctive output

3. **Client review checkpoint:**
   - Present the DESIGN.md with a small sample (one card component)
   - Incorporate feedback before generating full assets

### Hour 12-24: Asset Generation

Run these in parallel using the approved DESIGN.md:

**Track A — Website** (`/website-build`):
- Build a complete landing page
- Include hero, features, pricing, testimonials, footer
- Self-contained HTML, runs in any browser

**Track B — Presentation** (`/presentation-build`):
- Build a 10-slide template deck
- Include cover, content, data, section break, and closing templates
- Self-contained HTML with keyboard navigation

**Track C — Social** (`/multi-format-deploy`):
- Generate 3 social media templates:
  1. Square post (1080×1080)
  2. Carousel slide (1080×1350)
  3. Story/vertical (1080×1920)
- Each template shows the brand system in action

### Hour 24-36: Quality Assurance

1. **Run `/anti-slop-audit`** on each generated asset:
   - Website must score: 13+/15
   - Presentation must score: 13+/15
   - Social templates must score: 12+/15
   - Any score below threshold → iterate until passing

2. **Cross-format consistency check:**
   - Place all assets side-by-side
   - Do they feel like the same brand? Same color usage, same typography personality, same spacing rhythm?
   - Fix any drift

3. **Content truth check:**
   - Verify any data, stats, or claims in the sample content
   - Replace placeholder content with real client copy if available

### Hour 36-48: Packaging & Delivery

1. **Compile the Brand-in-a-Box package:**
   ```
   brand-in-a-box/
   ├── DESIGN.md                    (the master design system)
   ├── website/
   │   └── index.html               (complete landing page)
   ├── presentation/
   │   └── template.html            (10-slide template deck)
   ├── social/
   │   ├── post-template.html       (square post)
   │   ├── carousel-template.html   (carousel slide)
   │   └── story-template.html      (story format)
   ├── brand-assets/
   │   ├── logo.svg
   │   ├── color-palette.md
   │   └── typography-guide.md
   ├── anti-slop-report.md          (certification)
   └── README.md                    (how to use this system)
   ```

2. **Write the README:**
   - How to use the DESIGN.md with AI tools (Claude, Cursor, etc.)
   - How to modify colors/fonts while maintaining system coherence
   - How to generate new assets using the established system
   - Common mistakes to avoid (the anti-slop rules)

3. **Deliver via:**
   - GitHub repository (best for technical clients)
   - Zip file download (for non-technical clients)
   - Live walkthrough call (for premium tier)

### Premium Tier Add-Ons ($5,000)

- **1 round of revisions** — client provides feedback on all assets, you iterate
- **Design philosophy document** — written rationale for every design decision
- **Enshrinement** — `/design-skill-enshrine` so the client's team can generate new assets at one-command quality
- **Monthly refresh** option — quarterly update to the DESIGN.md based on brand evolution

## Output
- Complete Brand-in-a-Box package (all files listed above)
- Anti-Slop Certification report
- README documentation
- Client delivery call notes

## Revenue Math
```
Time investment:    ~8-12 hours actual work (AI does the heavy lifting)
Standard price:     $2,500
Premium price:      $5,000
Effective rate:     $208-$625/hour
Automation:         90% — workflows do the production
Your value-add:     Taste judgment, client communication, quality gate
Scalability:        2-3 per week once systems are proven
Monthly potential:  $20,000-$60,000
```

## Output Schema
```
Client Delivery: [client name] Brand-in-a-Box
├── DESIGN.md                    (master design system, ≥5 Anti-Slop rules)
├── website/index.html           (complete landing page)
├── presentation/template.html   (10-slide deck)
├── social/{post,carousel,story}-template.html  (3 formats)
├── brand-assets/                (logo.svg, color-palette.md, typography-guide.md)
├── anti-slop-report.md          (per-asset scores: website/presentation/social)
├── README.md                    (usage + modification + common-mistakes guide)
└── Revenue Math                 (hours logged, tier price, effective rate — for your own tracking)
```

## Quality Gate
- Website and presentation each score 13+/15 on `/anti-slop-audit`; social templates score 12+/15 — per Hour 24-36, anything below threshold is iterated, never shipped as-is.
- Cross-format consistency check completed and passing: same color usage, same typography personality, same spacing rhythm across all three tracks.
- DESIGN.md carries at least 5 explicit "never do this" rules (Hour 4-12 requirement) — a DESIGN.md with zero rejections does not clear this gate.
- No placeholder content in the delivered package — content truth check from Hour 24-36 confirms real client copy or clearly-marked sample copy, never lorem ipsum.
- README documents at least the 4 items listed in Hour 36-48 (AI-tool usage, modification, regeneration, anti-slop rules) before delivery.
