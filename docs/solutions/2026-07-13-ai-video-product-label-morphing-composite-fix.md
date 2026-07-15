---
name: AI-Video Product-Label Morphing Fixed by Real-Image Composite
problem_signature: generative video (Higgsfield/Veo) morphs and misspells a real product label, and the corrupted close-up IS the product reveal — trimming around it can't work; the render reads unshippable (garbled label, generic lag, poor edit)
domain: creative
tags: [ai-video, product-label, remotion, overlays, compositing, paid-ads, ffmpeg, trendscale]
date: 2026-07-13
status: active
session: trendscale-trial
---

# AI-video product-label morphing → deterministic real-image composite

**Date:** 2026-07-13 · **Domain:** video production / paid ads · **Thread:** trendscale-trial

## Problem

Generative video (Higgsfield/Veo) cannot render a real product label — it morphs and misspells ("JCXED", "0G KAHR", melted icons). Trimming "before the label close-up corrupts" doesn't work when the product reveal IS the corrupted shot. Verdict from Farrice on the v2 "FINISHED" render: morphing + poor edit + generic lag = unshippable.

## Solution (verified working, $0, local)

1. **Never let the model render the product.** Composite the real product PNG over the generated footage. Added a manifest-driven `overlays[]` track to the Remotion ad pipeline (`projects/trendscale-trial/03-video-samples/remotion-pipeline/src/Ad.tsx`): path, start/end seconds, x/y/width percent, accent glow, fade-in. Glow doubles as an edge mask over the covered region.
2. **Size coverage from measured facts, not eyeballing.** Extract the cutout's alpha bounding box (`ffmpeg alphaextract` → parse PGM) — the JCKED cutout's visible bottle is only 25.4% of canvas width, so naive width% under-covers by ~4x. Size: neededVisibleWidth / contentRatio / frameWidth.
3. **Cut the beat before the push enlarges the generated product.** A static overlay can't track a zooming AI bottle; trim the reveal beat to end before the worst frame (here 9.4-10.8s of a 12s push), and let the END CARD be the close-up product hero (it already uses the real PNG).
4. **Kill the "generic lag" structurally:** slice one long AI push into 2-3 hard-cut beats (door 2.5s → key 2.0s → reveal 1.4s) with escalating captions instead of one caption over 12 silent seconds.

## Result

`out/JCKED_TeaserH3_v3.mp4` — 8.9s, 3 beats + end card, pixel-exact label, frame-verified at 4.7s/5.8s (no AI-bottle peek). Remaining gap: no music bed/VO (assets/audio + assets/music empty — the one asset the pipeline can't invent).

## Reuse

Any AI-video ad with a real product: overlay the real PNG, measure the alpha bbox first, cut beats around the generated footage's weakest frames. The overlays[] capability is generic — logos, badges, packshots.
