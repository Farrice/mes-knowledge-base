---
description: Pick the right grid from the 11-type Satori taxonomy + breakage rules + white-space plan
---

# /satori-grid-select

> Choose the grid for the brief from the 11-type taxonomy. Default-grid syndrome (everything goes on a 12-column) is amateur thinking.

## Quick Deploy

```
Load: skills/satori-graphics/genius.md
Execute: skills/satori-graphics/workflows/03-grid-select.md
```

## Usage

```
/satori-grid-select [layout / brief description + format]
```

## When to Use

- Starting any layout from scratch
- Auditing a layout that "feels off" structurally
- Designing a new template / system that needs a grid
- Adapting a design across formats (each format may need a different grid)

## Output

Grid spec:
- Locked grid type (one of 12) with column / module / baseline specifics
- Breakage plan (≤1 break, with documented reason)
- White-space plan (macro + micro + empty cells + breathing zones)
- Anti-pattern checklist passed
- Executable setup numbers (ready to implement in Figma / Illustrator / InDesign)

## Related Workflows

- `/satori-movement-ladder` — pair grid with movement level
- `/satori-lift-audit` — verify grid choice via LIFT scoring
- `/satori-design-md-grid` — codify grid choices into DESIGN.md tokens

Full spec: `skills/satori-graphics/workflows/03-grid-select.md`

**Execution prompts**: before producing the deliverable, check `skills/satori-graphics/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
