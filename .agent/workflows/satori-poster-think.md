---
description: Composition + memory-encoding logic for streetwear / brand posters BEFORE production. The thinking layer that fantastic-posters needs to ship at quality.
---

# /satori-poster-think

> `fantastic-posters` is a production tool. Quality posters need *thinking before generation*. Run Satori's composition logic, memory encoding, and verb-not-noun ideation BEFORE the AI prompt.

## Quick Deploy

```
Load: skills/satori-graphics/genius.md
Execute: skills/satori-graphics/workflows/12-poster-think.md
```

## Usage

```
/satori-poster-think [poster brief — purpose + brand context + surface]
```

## When to Use

- Designing a poster for my.bpm (Farrice's EDM streetwear brand)
- Designing a poster for any brand campaign / event / launch
- Generating a poster series and you need conceptual coherence across pieces
- A previous AI-generated poster came back generic and you can't articulate why

## Output

1-page pre-flight brief (4 inputs only):
- **Verb** — one verb that captures what the poster *does* to the viewer
- **Visual primitive** — line type / geometry / motif from GP-09 cheat-sheet
- **Memory hook** — Move A/B/C/D with concrete implementation (or explicitly blank if speculative)
- **3-5 imperfections** — specific anti-AI-slop moves
- **Generation prompt** — 3-6 sentences, ready to hand to fantastic-posters
- **Forbidden** — what NOT to repeat from prior shipped pieces
- **Post-generation audit chain** — flip-test, anti-slop verify, memory verify

This is the minimum viable pre-flight. Nothing more. Earlier 9-step version was retired after adversarial review found it added overhead without speed advantage.

## Stacks With

- `/fantastic-posters` — production after this thinking layer
- `/art-direct` (Creative Director) — for series-level art direction

## Related Workflows

- `/satori-flip-test` + `/satori-lift-audit` + `/satori-anti-ai-slop` + `/satori-memory-encoding` — post-generation audit chain

Full spec: `skills/satori-graphics/workflows/12-poster-think.md`

**Execution prompts**: before producing the deliverable, check `skills/satori-graphics/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
