# Design Library Import

> Fork a pre-built DESIGN.md from the awesome-design-md library (55+ brand systems, 56k+ GitHub stars) and customize it — eliminating cold-start friction for new design projects.

## Context Required
- **Load First**: `genius.md` — Jack Roberts' 5-Step Design System and Anti-Slop Architecture
- **Complementary**: `skills/design-md/SKILL.md` for Stitch-format reference
- **Source Library**: `github.com/xb1g/awesome-design-md` — 55+ pre-built DESIGN.md files following Google Stitch format

## When to Use
- You want to build in an established brand's visual language (e.g., Stripe, Linear, Vercel, Apple)
- You need a high-quality starting point faster than building from scratch
- You're studying excellent design systems to learn what "good" looks like
- You want to A/B test multiple established aesthetics before committing

## Inputs
- **Required**: Target brand/style name OR desired aesthetic direction (e.g., "clean like Linear" or "bold like Stripe")
- **Optional**: Customization requirements (different colors, typography, brand-specific overrides)
- **Optional**: Target format (website, presentation, social media) for format-specific adaptation

## Workflow

### Phase 1: Library Discovery

1. **Browse the awesome-design-md repository:**
   ```
   URL: https://github.com/xb1g/awesome-design-md
   Format: Each brand has a complete DESIGN.md in Google Stitch format
   Stars: 56,100+ (validates community trust)
   ```

2. **Identify the best-match template:**
   - Search by brand name if the user has a specific reference
   - Search by aesthetic quality if the user describes a style
   - Present 2-3 options with rationale if the match isn't obvious
   - Flag the template's strengths and any gaps

3. **Fetch the raw DESIGN.md:**
   - Pull the complete markdown file from the repository
   - Preserve all original formatting, tokens, and structure
   - Note the original brand attribution for reference

### Phase 2: Template Analysis

Before customizing, audit the imported template:

| Check | What to Look For |
|-------|-----------------|
| **Completeness** | All 8 sections present (Theme, Color, Typography, Components, Layout, Imagery, Motion, Anti-Slop) |
| **Token Quality** | Specific hex codes, exact font names, real measurements (not placeholders) |
| **Anti-Slop Score** | Does this template produce distinctive output or is it generic? |
| **Format Fit** | Is this template optimized for the user's target format? |
| **Stitch Compatibility** | Does it follow the Google Stitch DESIGN.md specification? |

Flag any gaps found. A good library template should score 7+ on completeness.

### Phase 3: Customization

Apply the user's requirements to the imported template:

1. **Brand Override Layer:**
   - Replace brand name and attribution
   - Swap primary/accent colors to the user's brand palette
   - Replace typography if the user has brand fonts
   - Update logo placement and brand mark references

2. **Format Adaptation:**
   - If the template is website-focused but the user needs presentations → adapt typography scale, spacing, and component styles for slide format
   - If the template needs social media adaptation → add format-specific dimensions and text density rules

3. **Anti-Slop Hardening:**
   - Review the imported Anti-Slop rules — are they specific enough?
   - Add user-specific "never do this" rules
   - Ensure the customized version doesn't drift back toward AI defaults

4. **Token Verification:**
   - Every color has a descriptive name + hex + functional role
   - Every font has family + weight range + fallback
   - Every spacing value has a purpose annotation

### Phase 4: Validation

Run the customized DESIGN.md through:

1. **Diff Check**: Compare against the original template. What changed? What was preserved?
2. **Coherence Test**: Do the customized tokens still tell a unified visual story? (Swapping one color shouldn't break the palette harmony)
3. **Implementation Test**: Generate a small sample (a single card component or hero section) using only the customized DESIGN.md to verify it produces good output
4. **Anti-Slop Gate**: Score the customized output 1-10 on distinctiveness

### Phase 5: Enshrinement

Save the customized DESIGN.md as a project asset:
- Store at `[project-root]/DESIGN.md` or `[project-root]/design/DESIGN.md`
- Add a header comment noting the source template and customization date
- Register in the project's skill file if this becomes a recurring style

## Output
- Customized `DESIGN.md` — production-ready design system specification
- Template attribution note (source brand + library version)
- Customization changelog (what was changed from the original)
- Quality Score: Rate 1-10 on Completeness, Anti-Slop, Coherence, Format Fit

## Available Library Templates (Sample)

The awesome-design-md repository includes 55+ brands. High-quality examples:
- **Technology**: Linear, Vercel, Stripe, Supabase, Raycast, Arc Browser
- **Consumer**: Apple, Nike, Spotify, Notion
- **Enterprise**: Figma, GitHub, Slack
- **Media**: Netflix, YouTube
- **Design Tools**: Framer, Webflow

> **Pro Tip**: Even if you don't use a template directly, browsing 3-5 excellent DESIGN.md files teaches you what world-class design systems look like — training your eye before building from scratch.
