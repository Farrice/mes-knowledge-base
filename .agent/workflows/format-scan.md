---
description: Scan trending formats
---

> **Browser tools**: When format identification requires actually viewing live content on platforms (Instagram Reels, TikTok, LinkedIn carousels) — most of which is JS-rendered and login-gated — use Playwright (`mcp__playwright__browser_*`) per `directives/browser-automation-routing.md`.

# Cross-Niche Format Scanner

Find fresh format inspiration from completely unrelated niches.

## Workflow

1. Load `skills/alex-content-science/genius.md`
2. Load `skills/alex-content-science/workflows/05-cross-niche-format-scanner.md`
3. **For each video-format candidate** (Reels, Shorts, TikToks, YouTube videos), fetch visual context — the entire point of cross-niche format scanning is structural pattern recognition, and that pattern lives in the visual cadence:
   ```bash
   // turbo
   python3 execution/fetch-video-context.py "<format-example-url>" "format-$(echo "$url" | shasum | head -c 8)" || true
   ```
   See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). Wrapper auto-skips non-video sources and >10min content.
4. Execute with user's niche, platform, and stale format complaints
5. Deliver:
   - Format identification across 5-10 unrelated niches
   - Structure extraction (pure skeleton, topic stripped)
   - Niche translation with litmus tests
   - Priority matrix (Freshness × Producibility × Audience Fit)
   - Production blueprints for top 3 formats
6. Quality gate: 5+ niches scanned, 10+ formats found, 3+ survive translation, no formats traceable to source
