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

### 2. Execute Workflow
Follow the workflow in `02-lookalike-content.md` using the loaded genius context.

### 3. Save Output
Save pattern analysis to `.tmp/kieran-flanagan/lookalike-analysis.md`.
