---
description: 8 LinkedIn hook options across the 4 core 2026 formats (Dense / Punchy+Context / Bomb / Stacked) with gap + pixel-width fit + recommended pick
---

# `/diandra-hook-architect` — 5-Format Hook Architect

Takes a finished post (or raw idea) and engineers scroll-stopping hooks across the four formats that earn the "see more" click in 2026 — sized by pixel-width on mobile, built around the curiosity gap. From Diandra Escobar's 131-hook / 21-creator study.

## When to Use
- You have a post drafted and need the strongest possible hook
- A post flopped and you suspect the hook (not the insight) was the problem — re-hook it
- You're about to publish something from drafts and want hook options first
- You want format variety so your feed doesn't go "wallpaper" (Pattern 22)

**Not for**: optimizing the first 50 words for AI *retrieval signal* — that's `/diandra-first-50` (workflow 17). Run both: 20 finds the format/gap, 17 confirms the line carries semantic signal.

## Usage

```
/diandra-hook-architect "[paste the full post]" --bucket "[Growth|Authority|Conversion|Personal]"
```

## What It Does

1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` (Patterns 6, 19, 20, 21, 22)
2. **Reads**: `skills/diandra-escobar-linkedin-growth/references/hook-format-library.md` + `workflows/20-five-format-hook-architect.md`
3. **Extracts**: every hookable element in the body, each with the gap it opens
4. **Generates**: 8 hooks — 2 each across Dense / Punchy+Context / Single-Line Bomb / Stacked
5. **Pixel-checks**: every option against the ~110-width-units/line mobile budget
6. **Scores + recommends**: gap strength × scroll-stop × pixel-fit → recommended pick + runner-up
7. **Pre-publish reminder**: paste into a mobile post-previewer; insert manual line breaks for bomb/stacked

## Core Principle
The format is just packaging — the **gap** is the engine. No gap, no format will save it. Size by pixels, not characters. Provoke, don't explain. AI gets you a stronger start than a blank page; your judgment is the final filter.
