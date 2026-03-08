---
description: Quick ASCII wireframe generation and iteration for any visual asset — the universal pre-flight for all design work
---

# /wireframe — Visual Pre-Flight

Generate a production-ready ASCII wireframe for any visual asset and iterate until it matches your mental model. This is the fastest way to align your vision with AI execution before committing to production.

## Usage

```
/wireframe [describe what you want to build and key components]
```

Examples:
- `/wireframe landing page for an AI coaching service — hero, testimonials, pricing, and CTA`
- `/wireframe SaaS dashboard with sidebar, stat cards, two charts, and a data table`
- `/wireframe email template for a product launch — header, hero image, 3 feature blocks, CTA`
- `/wireframe infographic showing our 3-step methodology`

## Steps

### 1. Load Skill
// turbo
Read `skills/mark-kashef-visual-design/genius.md` for genius context.

### 2. Execute Workflow 01
// turbo
Read and execute `skills/mark-kashef-visual-design/workflows/01-ascii-wireframe-generator.md`.

Deploy the ASCII Wireframe Engine:
- Parse the user's component description
- Produce a full ASCII wireframe with labeled sections and realistic placeholders
- Surface assumptions explicitly
- Prompt for refinement

### 3. Iterate
Run the Scoped Refinement Protocol for each round of user feedback. Accept numbered changes, redraw the full wireframe, update assumptions.

### 4. Lock
When the user confirms the wireframe matches their mental model, declare it locked and ready for production.

**After locking**, offer next steps:
> "Wireframe locked. Want me to:"
> 1. "Build this now? I'll run the full Blueprint-to-Build pipeline (`/visual-blueprint`)"
> 2. "Run a taste audit first? I'll evaluate this against design principles (`/visual-taste-gate` workflow)"
> 3. "Save this wireframe as a specification for later?"

## Stacking
This command is designed to be the **pre-flight** for any visual workflow:
- Chain with `/design-first-build` for full design-first builds
- Chain with `/generate-image` for wireframed image compositions
- Chain with `/generate-asset` for wireframed marketing assets
- Use standalone for quick visual planning
