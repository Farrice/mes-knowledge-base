---
description: Find and analyze viral content in your niche
---

> **Browser tools**: LinkedIn / Instagram / TikTok / Twitter posts are JS-rendered and often login-gated — WebFetch returns empty hydration shells. Use Playwright (`mcp__playwright__browser_navigate` + `browser_evaluate` for text extraction, `browser_take_screenshot` for visual evidence) per `directives/browser-automation-routing.md`. Persistent profile carries Farrice's logins; never type credentials per `browser-automation-safety.md`.

# /lookalike-content — Lookalike Content Pattern Miner

Analyze high-performing content from competitors and adjacent creators to extract the structural patterns that made them work — then apply those patterns with your own voice and talking points.

## Usage

```
/lookalike-content [niche or topic] --platform [platform]
/lookalike-content "AI productivity" --platform LinkedIn
/lookalike-content --analyze [URL or file path to viral content]
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-engine/SKILL.md`
2. `skills/kieran-flanagan-content-engine/genius.md`
3. `skills/kieran-flanagan-content-engine/workflows/02-lookalike-content.md`

### 1.5. Fetch Visual Context for Video Sources
If any analyzed lookalike is a video URL (TikTok/Reels/YouTube Shorts), fetch frame-grounded visual context — the visual hook patterns drive most short-form virality and are invisible in transcript-only analysis:
```bash
// turbo
for url in "<lookalike-url-1>" "<lookalike-url-2>" "..."; do
  python3 execution/fetch-video-context.py "$url" "lookalike-$(echo "$url" | shasum | head -c 8)" || true
done
```
See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). Wrapper auto-skips non-video and >10min sources.

### 2. Execute Workflow
Follow the workflow in `02-lookalike-content.md` using the loaded genius context. If visual-context.md sidecars exist for any analyzed lookalikes, load them alongside the post text — visual hook patterns belong in the lookalike pattern library.

### 3. Save Output
Save pattern analysis to `.tmp/kieran-flanagan/lookalike-analysis.md`.
