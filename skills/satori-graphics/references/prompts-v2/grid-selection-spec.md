---
name: "Satori Graphics — Grid Selection Spec"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are selecting a grid using Satori's **11-type Grid Taxonomy** — a deliberate decision tool, not a default-to-12-column reflex. Grids are domain-specific tools chosen by purpose; the discipline is establish → adhere to most → break deliberately for exactly one point of impact.

> "Grids are insanely versatile. They don't just need to be kept for layout design for such things like magazines or newspapers." — Satori
> "Maybe a few boxes of typography and some imagery that fall in line with the grid columns and rows, but then have a design element that totally breaks the rule. This will create some contrast and visual impact." — Satori

## Input Required

- **[DOMINANT CONTENT TYPE]** — long-form text / mixed / visual-first / logo
- **[FORMAT]** — magazine / newspaper / book / e-commerce / social / web hero / poster / infographic / packaging / other
- **[DENSITY]** — low (2-5 elements) / medium (6-15) / high (15+)
- **[BREAKAGE TOLERANCE]** — none (corporate / trust-first) / low (editorial) / high (artistic / streetwear)

## Execution Protocol

### Step 1 — Establish Selector Inputs

Document content type, format, density, breakage tolerance from inputs.

### Step 2 — Run the Decision Tree

**A — Dominant content type**: long-form text → Manuscript / Baseline / Column; mixed → Column / Compound / Hierarchy; visual-first → Modular / Asymmetric / Square / Rule-of-thirds; logo/mark → Circular / Triangular.

**B — The 12 grid types by best-use and key move**:

| Grid | Best for | Key move |
|---|---|---|
| Baseline | Body text alignment | Multiples of base leading (e.g., 14pt body → 28pt headline) |
| Column | Magazines, newspapers, multi-content | Span content across columns for emphasis |
| Modular | E-commerce, product showcases | Vary module size by importance |
| Manuscript | Books, long-form reading | Single column + wide margins |
| Hierarchy | Headlines + nav-heavy layouts | Different module sizes; primary big+bold, secondary muted |
| Asymmetric | Dynamic, eye-catching layouts | Hero takes more space; secondary supports |
| Square | Galleries, Instagram, uniform feeds | Add color/pattern variation in select squares |
| Rule-of-thirds | Photo placement, key visuals | Place subject on intersection; break for drama |
| Compound | Multi-content with detail | Column for listings + modular for details |
| Isometric | 3D illustrations, infographics | Light on top + dark beneath = volume |
| Circular | Round/organic logos | Symmetry + interesting negative space |
| Triangular | Geometric packaging, modern boxes | Logo + product info at intersection points |

**C — Breakage plan**: for impact (one element disrupts — oversize / cross-column / off-grid), for hierarchy (top-tier content spans more cells), for tension (element rotated / partially off-grid).

### Step 3 — Lock the Grid

Specify primary grid type, secondary grid (if compound), column count/module size/spacing, and baseline leading (if text-heavy).

### Step 4 — Breakage Plan (budget: ONE major break per layout)

Document: will you break? which element? how (oversize/cross-column/rotated/off-grid/overlapping)? why does it serve the design (leverage/tension/hierarchy/brand-identity)? If breakage tolerance is "none," confirm no-break explicitly.

### Step 5 — White-Space Plan

Macro (outer margins, section spacing), micro (leading, letter-spacing, inter-element gaps), empty cells (default modular: 30-40% intentionally empty), and breathing zones — mandatory; a design without one fails LIFT-T.

### Step 6 — Logo-Specific Subset (if applicable)

Round/organic logo → Circular grid (concentric circles + radial lines). Geometric/modern packaging → Triangular grid (intersection points anchor logo + product info). Anything else → skip layout-grid thinking; use shape psychology instead (route to Logo Concept Brief).

## Output Contract

A Grid Spec: selector inputs, locked grid (with column/module/baseline specifics), breakage plan with budget enforcement (≤1 break), white-space plan (macro+micro+empty cells+breathing zones), anti-pattern checklist, and executable setup numbers a designer can implement without re-asking.

## Output Skeleton

```markdown
# Grid Spec — [layout name]

## Inputs
- Content type: [...]
- Format: [...]
- Density: [...]
- Breakage tolerance: [...]

## Grid
- Primary type: [...]
- Secondary (compound): [if applicable]
- Columns / modules: [specific numbers]
- Baseline leading: [body × multiples]

## Breakage Plan
- Will break? [yes/no]
- Element: [...]
- How: [...]
- Why this serves design: [...]

## White Space
- Macro: [...]
- Micro: [...]
- Empty cells: [...]
- Breathing zones: [...]

## Anti-Pattern Check
- [ ] Default 12-column avoided unless brief demands it
- [ ] Single primary grid
- [ ] One break maximum
- [ ] Breathing zone present
- [ ] Baseline grid honored if text-heavy

## Executable Setup
[implementable in Figma / Illustrator / InDesign without re-asking]
```

## Quality Gate

- The grid choice is brief-driven, not "12-column because standard"
- One grid type leads; any compound is explicit
- Breakage budget enforced (≤1) with documented reason
- Breathing zone present
- Baseline grid present if text is significant content

## Creative Latitude

The taxonomy is the toolkit, not the answer — the creative act is matching an unexpected grid to a brief that "shouldn't" call for it (a Triangular grid on a non-packaging brief, a Compound grid on a single-content-type brief) when the breakage tolerance and density genuinely support it. The one-break budget is where taste lives: choose the break that does the most work for the brief, not the safest one.

## Deploy When

Starting any layout from scratch; auditing a layout that "feels off" structurally; designing a new template/system that needs a grid; or adapting a design across formats (each may need a different grid). Do not use for logos outside the circular/triangular subset, pure typography decisions, or when the brief itself is still unclear.
