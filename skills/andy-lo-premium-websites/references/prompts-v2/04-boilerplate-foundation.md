---
name: "Boilerplate Foundation"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/04-boilerplate-foundation.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Boilerplate Foundation

## Purpose
Generate a clean, professionally structured website foundation that handles all the invisible-but-critical setup work: document structure, viewport handling, responsive breakpoints, styling defaults, and component architecture. This is what separates amateur "AI websites" from agency-grade output.

## System Prompt

You are Andy Lo. You never start a website from scratch. You begin with the same foundation a senior developer would use — proper structure, responsive from the start, sensible defaults. This foundation should render cleanly in browser preview before any content is added.

## User Prompt

```
Generate a professional website boilerplate for {{PROJECT_NAME}}.

**Stack:**
- Framework: React with Vite (or vanilla HTML/CSS/JS for simple projects)
- Styling: CSS Modules (component-scoped, no Tailwind)
- Routing: React Router v6 (if multi-page)
- Build: Production-ready from the start

**Foundation Requirements:**

### Structure
- Clean folder architecture: /src/components, /src/pages, /src/styles, /src/assets
- index.html with proper meta tags (viewport, charset, description, OG tags)
- Main App component with routing scaffold
- Shared layout component (header, footer, main content area)

### Responsive Foundation
- CSS custom properties for spacing, colors, typography
- Mobile-first breakpoints: 480px, 768px, 1024px, 1440px
- Fluid typography scale (clamp-based)
- Container max-width with auto margins

### Styling Defaults
- CSS reset (box-sizing, margin reset, image handling)
- Dark theme base: {{PRIMARY_BG}} background, {{PRIMARY_TEXT}} text
- Typography: {{HEADING_FONT}} for headings, {{BODY_FONT}} for body
- Smooth scroll behavior
- Selection color matching brand palette
- Focus styles for accessibility

### Performance Defaults
- Image lazy loading attribute
- Font preload links
- Proper asset organization

### Component Stubs
Create empty but properly structured components for:
- Hero section
- Navigation (responsive with mobile menu)
- Section wrapper (reusable)
- Footer
- Loading/skeleton state

**Verification:**
The boilerplate should render a clean, empty dark-themed page with working navigation when previewed. No content needed — just a clean canvas ready for content.
```

## Output Contract
- A folder architecture spec (components/pages/styles/assets)
- An index.html with viewport, charset, description, and OG meta tags present
- A responsive foundation: CSS custom properties, named breakpoints, fluid typography scale, container max-width rule
- Styling defaults: CSS reset, dark theme base tokens, heading/body font assignment, smooth scroll, selection color, focus styles
- Performance defaults: lazy loading attribute, font preload, asset organization
- Five component stubs: hero, navigation, section wrapper, footer, loading/skeleton state
- A verification statement confirming clean render with no content

## Output Skeleton
```
FOLDER STRUCTURE
/src/components, /src/pages, /src/styles, /src/assets — [confirm present]

INDEX.HTML META
[viewport] [charset] [description] [OG tags] — [confirm present]

RESPONSIVE FOUNDATION
Breakpoints: [list, mobile-first]
Typography scale: [clamp-based rule]
Container: [max-width + auto margin rule]

STYLING DEFAULTS
Reset: [box-sizing, margin, image handling]
Theme base: background=[token], text=[token]
Fonts: heading=[token], body=[token]
Scroll/selection/focus: [confirm present]

PERFORMANCE DEFAULTS
[lazy loading] [font preload] [asset organization]

COMPONENT STUBS
- Hero: [structured, empty]
- Navigation: [responsive, mobile menu]
- Section wrapper: [reusable]
- Footer: [structured, empty]
- Loading/skeleton: [structured, empty]

VERIFICATION
[confirms clean dark-themed empty page renders with working navigation]
```

## Quality Gate
- [ ] Every folder in the architecture spec (components/pages/styles/assets) is present, not just named
- [ ] index.html includes all four meta categories (viewport, charset, description, OG) — none missing
- [ ] All four responsive breakpoints are defined and mobile-first ordered
- [ ] All five component stubs exist and are empty (no placeholder content baked in)
- [ ] The boilerplate renders in preview with zero console errors before any content is added

## Deploy When
- Starting any new website project (always first step in Path B)
- Before any creative content or asset work

## Genius Patterns Applied
- Boilerplate-First Foundation (#4)
- Progressive Polish Protocol (#6)
