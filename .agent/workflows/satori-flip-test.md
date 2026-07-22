---
description: 90-second pre-delivery technical audit — flip the design to see structure not content. Catches alignment, white-space, micro-rhythm errors invisible during normal viewing.
---

# /satori-flip-test

> The fastest, freest, most ruthlessly diagnostic check Satori teaches. Flip the design upside down. Brain switches from content-mode to structure-mode. Catches amateur tells invisible during normal viewing.

## Quick Deploy

```
Load: skills/satori-graphics/genius.md
Execute: skills/satori-graphics/workflows/10-flip-test.md
```

## Usage

```
/satori-flip-test [design path / screenshot / URL]
```

## When to Use

- Final pre-ship check on any design
- You've been staring at a design for hours and need fresh-eyes diagnostic
- Auditing someone else's work and want a fast structural read
- A draft "feels off" but you can't articulate why

## Output

Flip-test report:
- Duration documented (target ≤90 seconds)
- 6-check structural audit: Alignment / Macro white space / Micro white space / Edge tension / Visual weight balance / Optical sizing
- Findings table with severity (High / Medium / Low) per issue
- Pre-delivery verdict (READY / REWORK / MAJOR REWORK)

## Related Workflows

- `/satori-lift-audit` — composition layer (this is structural; LIFT is compositional)
- `/satori-anti-ai-slop` — verify imperfection injections don't break structure
- `/satori-brand-audit` — flip-test is one layer in the brand audit chain

Full spec: `skills/satori-graphics/workflows/10-flip-test.md`

**Execution prompts**: before producing the deliverable, check `skills/satori-graphics/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
