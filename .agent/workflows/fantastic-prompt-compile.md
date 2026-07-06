---
description: Compile each art-direction spec into a model-specific production prompt (and a Fal --brief JSON the generator consumes)
---

# /fantastic-prompt-compile

> Compile each art-direction spec into a model-specific production prompt (and a Fal --brief JSON the generator consumes).

## Quick Deploy

```
Load: skills/fantastic-posters/genius.md
Execute: skills/fantastic-posters/workflows/05-prompt-compile.md
```

## Usage

```
/fantastic-prompt-compile [brief, asset path, or a /satori-design-think Production Brief]
```

## When to Use

After routing, to produce ready-to-run, richly-specified prompts per model.

## Cost & Safety

This is the thinking/plan layer. Any paid generation is **cost-gated and human-triggered**
(`python3 execution/cost_gate.py check --service <id>` → approve → run). Never auto-fired.
seedance-1080p is hard-blocked.

## Related Workflows

Studio stages: `/fantastic-studio` · `/fantastic-reference-ground` · `/fantastic-art-direct` · `/fantastic-divergence` · `/fantastic-model-route` · `/fantastic-prompt-compile` · `/fantastic-generate-run` · `/fantastic-critique-refine` · `/fantastic-format-pack`
Composes the design brain: `/satori-design-think` · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop`
Dispatcher: `execution/creative_router.py` · Full spec: skills/fantastic-posters/workflows/05-prompt-compile.md
