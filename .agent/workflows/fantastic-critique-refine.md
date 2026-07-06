---
description: Critique each render on Virgil × LIFT × type × anti-slop, then make targeted --mask edits and re-render — the loop that makes it remarkable
---

# /fantastic-critique-refine

> Critique each render on Virgil × LIFT × type × anti-slop, then make targeted --mask edits and re-render — the loop that makes it remarkable.

## Quick Deploy

```
Load: skills/fantastic-posters/genius.md
Execute: skills/fantastic-posters/workflows/07-critique-refine.md
```

## Usage

```
/fantastic-critique-refine [brief, asset path, or a /satori-design-think Production Brief]
```

## When to Use

After generation, before shipping. Turns first-output into finished work; fixes garbled text without re-rolling.

## Cost & Safety

This is the thinking/plan layer. Any paid generation is **cost-gated and human-triggered**
(`python3 execution/cost_gate.py check --service <id>` → approve → run). Never auto-fired.
seedance-1080p is hard-blocked.

## Related Workflows

Studio stages: `/fantastic-studio` · `/fantastic-reference-ground` · `/fantastic-art-direct` · `/fantastic-divergence` · `/fantastic-model-route` · `/fantastic-prompt-compile` · `/fantastic-generate-run` · `/fantastic-critique-refine` · `/fantastic-format-pack`
Composes the design brain: `/satori-design-think` · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop`
Dispatcher: `execution/creative_router.py` · Full spec: skills/fantastic-posters/workflows/07-critique-refine.md
