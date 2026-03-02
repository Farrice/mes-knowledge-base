---
description: Build any visual asset (website, landing page, UI) using a design-first pipeline. Prevents the "straight to code" trap by enforcing visual approval before implementation.
---

# /design-first-build — Design-First Visual Build Pipeline

> **Why this exists:** We learned the hard way that going critique → code without a design step in between produces results the user can't evaluate until it's too late. The fix: always get visual approval BEFORE writing code.

## Phase 1: Creative Direction Lock (BEFORE any code)

1. **Gather references.** Ask the user for 2-3 websites, brands, or images that represent the vibe they want. If they don't have any, deploy `@oren` (taste development) or `@alex-copper` (creative strategy) to generate a mood direction.

2. **Generate visual mockups.** Use the `generate_image` tool to create 2-3 UI mockup options for key sections (hero, cards, footer). These are NOT wireframes — they should look like finished designs with real colors, typography, and layout.

3. **Present options to the user.** Show the mockups and ask: "Which direction feels right? What would you change?" Iterate until they approve a direction.

> [!IMPORTANT]
> **DO NOT write any HTML or CSS until the user explicitly approves a visual direction.** This is the single most important rule.

## Phase 2: Design System Build

4. Once visual direction is approved, build the CSS design system FIRST:
   - Color palette (extract exact hex values from approved mockup)
   - Typography (font pairings, sizes, weights)
   - Spacing scale
   - Component patterns (cards, buttons, sections)

5. Build a single "design system preview" HTML page that shows all tokens and components. Screenshot it and get user confirmation before proceeding.

## Phase 3: Page Assembly

6. Build pages section-by-section. After each major section:
   - Take a browser screenshot
   - Compare against the approved mockup
   - Fix any drift before moving to the next section

7. Full-page preview for final approval.

## Skills to Deploy

| Phase | Skill | Purpose |
|-------|-------|---------|
| Direction | `@oren` / `oren-taste-development` | CEV critique on reference sites, taste calibration |
| Direction | `@alex-copper` / `alex-copper-creative-strategy` | Visual identity, brand positioning |
| Direction | `@kittl` / `kittl-graphic-design` | Design system generation, asset creation |
| Build | `frontend-design` | Frontend patterns and component architecture |
| QA | `@oren` / `oren-taste-development` | CEV critique on each built section |

## Anti-Patterns (What NOT to Do)

- ❌ Going from strategy docs straight to code
- ❌ Using CSS variables as a substitute for visual design
- ❌ Building all sections before getting any visual feedback
- ❌ Assuming the user can evaluate design quality from code descriptions
