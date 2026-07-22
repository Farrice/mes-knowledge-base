---
description: The count-the-contrasts diagnostic — walk an existing design zone by zone, name every contrast form present/absent/conflicting, score stack depth, and prescribe the minimum moves to reach the ship zone
---

# /satori-contrast-audit

> Read any design the way Satori reads the Nike poster: name every contrast form present. Fewer than 3 deliberate = FLAT (generic risk). Many accidental = NOISE. Prescriptions are minimum-move and quiet-first.

## Quick Deploy

```
Load: skills/satori-graphics/genius.md
Load: skills/satori-graphics/references/contrast-stack.md
Execute: skills/satori-graphics/workflows/23-contrast-audit.md
```

## Usage

```
/satori-contrast-audit [design file/screenshot/URL/description]
```

## When to Use

- A draft is "clean but forgettable" — the AI-default suspicion
- Pre-delivery gate on any generated/AI-assisted layout
- Reverse-engineering a reference design that works
- A conversion surface underperforms and the hypothesis is "nothing wins"

## Output

A Contrast Audit Report: apparent anchors (or "no spine" flag), the 9-form verdict table (PRESENT-deliberate / PRESENT-accidental / CONFLICTING / ABSENT with evidence), depth score (FLAT / SHIP ZONE / NOISE), and a quiet-first minimum-move prescription list.

## Related Workflows

- `/satori-contrast-stack` — generative twin; rebuild the stack after the audit
- `/satori-anti-ai-slop` — pairs on generated work
- `/satori-lift-audit` — when the deeper failure is hierarchy
- `/satori-three-flow` — where the prescription starts when no spine exists

Full spec: `skills/satori-graphics/workflows/23-contrast-audit.md`

**Execution prompts**: before producing the deliverable, check `skills/satori-graphics/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
