---
description: Inject Satori's grid taxonomy + leverage rules into a DESIGN.md spec — composition tokens that make Jack Roberts' code-first system inherit Satori's composition theory
---

# /satori-design-md-grid

> Inject Satori's grid taxonomy + leverage rules + movement-level defaults into a DESIGN.md spec. UI/page code generated downstream inherits composition discipline at the token level.

## Quick Deploy

```
Load: skills/satori-graphics/genius.md
Execute: skills/satori-graphics/workflows/13-design-md-grid.md
```

## Usage

```
/satori-design-md-grid [path to existing DESIGN.md]
```

## When to Use

- Building a new DESIGN.md from scratch with Satori-grade composition
- Auditing an existing DESIGN.md that produces "AI-default" page layouts
- Need composition consistency across many pages produced from one DESIGN.md
- Want to encode "anti-AI-slop" defaults at the system level

## Output

Enhanced DESIGN.md with new `## Composition` section:
- Brand composition DNA (5 axes: density / asymmetry / movement / breakage / friction)
- Grid taxonomy (default + per-page-type)
- Leverage defaults (rule + dominance tools + anti-pattern veto)
- Movement defaults (default + per-page + disruption budget)
- Friction & flow tokens (philosophy + zones + ratio + good/bad examples)
- Transferability requirements
- Anti-AI-slop defaults (5+ imperfection rules + forbidden patterns)
- Component audit + per-component fixes
- CLI lint validation reference

## Stacks With

- `/design-md-extract` (Jack Roberts) — extract baseline DESIGN.md first
- `/design-md-validate` — lint after enhancement (`npx @google/design.md lint`)
- `/product-build` — UI code generation downstream consumes the enhanced DESIGN.md

## Related Workflows

- `/satori-grid-select` — grid system fundamentals
- `/satori-lift-audit` — score live pages produced from the enhanced DESIGN.md

Full spec: `skills/satori-graphics/workflows/13-design-md-grid.md`
