---
description: Reverse-engineer voice, structure, and patterns
---

# /style-from-creator — Creator Voice Cloner

Analyze a creator's published content to extract their style DNA. Produces a style card that can be used by the content engine to write in their voice.

## Usage

```
/style-from-creator [creator name] [links or file paths to their content]
/style-from-creator "Alex Hormozi" --platform LinkedIn
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-audience-intelligence/SKILL.md`
2. `skills/kieran-flanagan-audience-intelligence/genius.md`
3. `skills/kieran-flanagan-audience-intelligence/workflows/03-style-from-creator.md`

### 1.5. Fetch Visual Context for Video Sources
If any of the creator's content is video (YouTube, TikTok, Instagram Reels, on-camera LinkedIn), fetch frame-grounded context — voice DNA includes gesture, pacing, energy, and on-screen choices that are invisible in transcripts:
```bash
// turbo
for url in "<creator-video-url-1>" "<creator-video-url-2>" "..."; do
  python3 execution/fetch-video-context.py "$url" "<creator-slug>" || true
done
```
See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md).

### 2. Execute Workflow
Follow the workflow in `03-style-from-creator.md` using the loaded genius context. If visual-context.md exists, the style card MUST capture visual style markers (camera angle, gesture cadence, on-screen text choices, B-roll patterns) alongside verbal style markers.

### 3. Save Output
Save the derived style card to `.tmp/kieran-flanagan/style-card-[creator].md`.
