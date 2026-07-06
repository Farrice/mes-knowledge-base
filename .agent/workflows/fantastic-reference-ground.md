---
description: Anchor a visual brief in real high-taste design lineage (Swiss, Polish poster school, Yokoo, AIGA annuals) before any prompt
---

# /fantastic-reference-ground

> Anchor a visual brief in real high-taste design lineage (Swiss, Polish poster school, Yokoo, AIGA annuals) before any prompt.

## Quick Deploy

```
Load: skills/fantastic-posters/genius.md
Execute: skills/fantastic-posters/workflows/01-reference-ground.md
```

## Usage

```
/fantastic-reference-ground [brief, asset path, or a /satori-design-think Production Brief]
```

## When to Use

The start of a Studio run, or whenever output is drifting generic and needs a named craft anchor.

## Cost & Safety

This is the thinking/plan layer. Any paid generation is **cost-gated and human-triggered**
(`python3 execution/cost_gate.py check --service <id>` → approve → run). Never auto-fired.
seedance-1080p is hard-blocked.

## Related Workflows

Studio stages: `/fantastic-studio` · `/fantastic-reference-ground` · `/fantastic-art-direct` · `/fantastic-divergence` · `/fantastic-model-route` · `/fantastic-prompt-compile` · `/fantastic-generate-run` · `/fantastic-critique-refine` · `/fantastic-format-pack`
Composes the design brain: `/satori-design-think` · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop`
Dispatcher: `execution/creative_router.py` · Full spec: skills/fantastic-posters/workflows/01-reference-ground.md
