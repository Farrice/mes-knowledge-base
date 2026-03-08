---
description: Rapid wireframe-to-production shortcut — for when you already know what you want and just need it built
---

# /sketch-to-build — Rapid Visual Execution

Skip the iterative wireframe refinement and go straight from concept to build. This is the speed-run version for when you already have a clear mental model and just need it executed. Still uses wireframing as the specification layer, but compresses the process.

## Usage

```
/sketch-to-build [describe what you want + any style/tech preferences]
```

Examples:
- `/sketch-to-build React dashboard with dark mode, sidebar, 4 stat cards, revenue line chart, and user table`
- `/sketch-to-build landing page for an ebook — hero with mockup, 3 benefit blocks, testimonial, download CTA. Modern, clean.`
- `/sketch-to-build simple portfolio site — about section, project grid, contact form. Minimal black and white.`

## Steps

### 1. Load Skill
// turbo
Read `skills/mark-kashef-visual-design/genius.md` for genius context.

### 2. Rapid Wireframe
// turbo
Generate an ASCII wireframe from the user's description. Do NOT wait for approval — present it and simultaneously begin the build.

The wireframe serves as documentation, not a gate. If the user is using this command, they want speed.

### 3. Style Inference
Infer style annotations from the user's description and standard best practices:
- **"Modern"** → Clean sans-serif, generous whitespace, subtle shadows
- **"Dark mode"** → Deep navy/charcoal background, light text, accent colors
- **"Minimal"** → Maximum whitespace, reduced UI chrome, monochrome palette
- **"Corporate"** → Blues/grays, structured grid, professional iconography

### 4. Build
Compose and execute the production prompt:
- Include the generated wireframe as specification
- Include inferred style annotations
- Include standard quality overrides (no emoji icons, realistic data, etc.)
- Build and spin up

### 5. Present
Show the user:
- The wireframe generated (for reference)
- The built output
- "Want to refine? I can iterate on specific sections."

## When to Use This vs /visual-blueprint
- **Use `/sketch-to-build`** when you know what you want and want it NOW
- **Use `/visual-blueprint`** when accuracy matters more than speed (client deliverables, high-stakes assets)
- **Use `/wireframe`** when you just want the wireframe, not the build

## Speed Philosophy
This command trades precision for velocity. The wireframe still exists as a specification layer (preventing the "lazy prompt" failure mode), but iteration happens AFTER the first build rather than before. For many projects, this is the right trade-off — it's faster to see a real build and refine than to perfect a wireframe.
