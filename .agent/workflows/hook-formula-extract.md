---
description: Discover what patterns work specifically for you
---

# /hook-formula-extract — Personal Hook Formula Miner

Analyze your own published content to discover which hook patterns consistently drive engagement. Builds a personal hook formula library that's uniquely calibrated to your audience.

## Usage

```
/hook-formula-extract [paths to published content with engagement data]
/hook-formula-extract --platform LinkedIn --content-folder [path]
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-engine/SKILL.md`
2. `skills/kieran-flanagan-content-engine/genius.md`
3. `skills/kieran-flanagan-content-engine/workflows/07-hook-formula-extract.md`

### 1.5. Fetch Visual Context for Video Hooks
If your published content includes video (Reels, Shorts, TikToks, on-camera LinkedIn), fetch frame-grounded context — visual hook patterns (cut timing, on-screen text, opening frame composition) are often the dominant predictor of stop-scroll on visual platforms:
```bash
// turbo
for url in "<your-video-url-1>" "<your-video-url-2>" "..."; do
  python3 execution/fetch-video-context.py "$url" "self-$(echo "$url" | shasum | head -c 8)" || true
done
```
See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md).

### 2. Execute Workflow
Follow the workflow in `07-hook-formula-extract.md` using the loaded genius context. If visual-context.md sidecars exist, the hook formula library should distinguish between **verbal hook formulas** (text-driven) and **visual hook formulas** (cut/composition/on-screen-text driven) — they're independent levers.

### 3. Save Output
Save hook formula library to `.tmp/kieran-flanagan/hook-formulas.md`.
