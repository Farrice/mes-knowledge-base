---
description: Pick the right grid from the 11-type Satori taxonomy + breakage rules + white-space plan
---

# /satori-grid-select — Grid Taxonomy Selector

Choose the grid for the brief from Satori's 11-type taxonomy. Default-grid syndrome (everything goes on a 12-column) is amateur thinking. This workflow forces a deliberate grid decision and a breakage plan.

## Pre-Flight Gate

**Use this when**:
- Starting any layout from scratch
- Auditing a layout that "feels off" structurally
- Designing a new template / system that needs a grid
- Adapting a design across formats (each format may need a different grid)

**Do NOT use this when**:
- The format is logo (use circular/triangular subset only — see Step 4)
- Pure typography selection (use Kittl)
- The brief itself is unclear (run `/satori-why-before-what` first)

## Skill Acquisition

Load:
- `genius.md` — GP-05 (Grid Taxonomy)
- `references/grid-taxonomy-selector.md` — full decision tree, all 12 grid types, breakage rules

## Execution

### Step 1: Establish the Selector Inputs

Document:
- **Dominant content type**: long-form text / mixed / visual-first / logo
- **Format**: magazine / newspaper / book / e-commerce / social / web hero / poster / infographic / packaging
- **Density**: low (2-5 elements) / medium (6-15) / high (15+)
- **Breakage tolerance**: none (corporate / trust-first) / low (editorial) / high (artistic / streetwear)

### Step 2: Run the Decision Tree

From `references/grid-taxonomy-selector.md`:

**Step A — What's the dominant content type?**
- Long-form text → see Text-First grids (Manuscript, Baseline, Column)
- Mixed content → see Hybrid grids (Column, Compound, Hierarchy)
- Visual-first → see Visual-First grids (Modular, Asymmetric, Square, Rule-of-thirds)
- Logo / mark → see Logo grids (Circular, Triangular)

**Step B — What's the format?** (Use the Quick Selector table from the reference doc)

**Step C — How will you break the grid?**
- For impact: one element disrupts (oversize, cross-column, off-grid)
- For hierarchy: top-tier content spans more cells
- For tension: element rotated / partially outside grid

### Step 3: Lock the Grid

Specify:
- **Primary grid type**: [one of the 12]
- **Secondary grid** (if compound): [if applicable]
- **Column count / module size / spacing**: [specific numbers]
- **Baseline grid leading**: [if text involved — body leading × multiples for headlines]

### Step 4: Breakage Plan

**Breakage budget: ONE major break per layout. Multiple breaks compound to chaos.**

Document:
- **Will you break?** Yes / No
- **If yes — what element breaks?** [specific element]
- **How does it break?** Oversize / cross-column / rotated / off-grid / overlapping
- **Why does this break serve the design?** Leverage / tension / hierarchy / brand-identity
- **If breakage tolerance is "none" (corporate / trust-first), confirm No-break.**

### Step 5: White-Space Plan

White space is a function of grid choice. Specify:
- **Macro white space**: outer margins / section spacing
- **Micro white space**: leading / letter-spacing / inter-element gaps
- **Empty cells**: which grid cells are intentionally empty? (Default modular: 30-40% of cells empty)
- **Breathing zones**: where does the design release tension? (Mandatory — design without breathing zone fails LIFT-T)

### Step 6: Logo-Specific Grid Subset (if applicable)

If the brief is a logo:
- **Round / organic logo** → Circular grid (concentric circles + radial lines for symmetry)
- **Geometric / modern packaging** → Triangular grid (intersection points anchor logo + product info)
- **Anything else** → Logo doesn't need a layout grid; use shape psychology instead (route to `/satori-logo-concept`)

### Step 7: Output the Grid Spec

```markdown
# Grid Spec — [layout name]

## Inputs
- Content type: [...]
- Format: [...]
- Density: [...]
- Breakage tolerance: [...]

## Grid
- **Primary type**: [...]
- **Secondary** (compound): [if applicable]
- **Columns / modules**: [specific numbers]
- **Baseline leading**: [body × multiples]

## Breakage Plan
- Will break? [yes/no]
- Element: [...]
- How: [...]
- Why this serves design: [...]

## White Space
- Macro: [outer margins / section spacing]
- Micro: [leading / letter-spacing / gap rules]
- Empty cells: [cells / zones intentionally empty]
- Breathing zones: [where tension releases]

## Anti-Pattern Check
- [ ] Default 12-column avoided unless brief demands it
- [ ] Single primary grid (no parallel grids without compound rationale)
- [ ] One break maximum
- [ ] Breathing zone present
- [ ] Baseline grid honored if text-heavy

## Executable Setup
[Designer can implement this in Figma / Illustrator / InDesign without re-asking]
```

## Content Type Adaptations

| Content type | Recommended grid | Breakage |
|---|---|---|
| **LinkedIn carousel** | Square or Modular | Optional — one slide off-grid for emphasis |
| **Listing reel frame** | Asymmetric or Hierarchy | Hero image breaks; secondary info anchored to grid |
| **Streetwear poster** | Asymmetric or Hierarchy | Strong — one element rotated or oversized |
| **Newsletter article** | Manuscript + Baseline | None — readability first |
| **Brand pitch deck** | Hierarchy or Modular | Strategic — title slide breaks; content slides hold |
| **Product e-commerce** | Modular + Compound | Featured product breaks via 2-cell span |
| **Logo on round seal** | Circular | None — symmetry serves brand |
| **3D infographic** | Isometric | None — system serves the depth illusion |
| **Magazine spread** | Column + Baseline | Featured spread breaks via cross-column image |
| **Mobile app onboarding** | Hierarchy | None — clarity beats expression |
| **Resume / CV** | Manuscript or Hierarchy | None — readability rules |
| **Wedding invitation** | Manuscript or Asymmetric | One ornamental element off-grid |
| **Streetwear merch tag** | Triangular | High — brand intentionally disruptive |
| **Real estate flyer** | Hierarchy | Low — corporate trust expectation |

## Output Requirements

Spec must include:
1. Selector inputs (content type / format / density / breakage tolerance)
2. Locked grid type with column / module / baseline specifics
3. Breakage plan with budget enforcement (≤1 break)
4. White-space plan (macro + micro + empty cells + breathing zones)
5. Anti-pattern checklist passed
6. Executable setup (numbers a designer can implement)

## Quality Gate (Genius Rubric)

- [ ] **Default avoided**: Not "12-column because that's standard" — the choice is brief-driven
- [ ] **Single primary**: One grid type leads; compounds explicit
- [ ] **Breakage budget enforced**: ≤1 break, with documented reason
- [ ] **Breathing zone present**: at least one zone where tension releases
- [ ] **Baseline grid present** if text is significant content

## Source Grounding

> *"Maybe a few boxes of typography and some imagery that fall in line with the grid columns and rows, but then have a design element that totally breaks the rule. This will create some contrast and visual impact."* — Satori, on grid breakage

> *"Grids are insanely versatile. They don't just need to be kept for layout design for such things like magazines or newspapers."* — Satori, on grid scope
