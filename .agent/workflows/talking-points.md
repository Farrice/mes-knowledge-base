---
description: Extract and score talking points from source material
---

# /talking-points — Talking Point Extractor

Mine source material for the creator's authentic perspectives and build a scored library of talking points. This is the raw material the content engine uses to produce content.

## Usage

```
/talking-points [source material — transcript, article, notes, or URL]
/talking-points extractions/transcripts/my-talk.txt
/talking-points --append [existing library path]
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/kieran-flanagan-content-engine/SKILL.md`
2. `skills/kieran-flanagan-content-engine/genius.md`
3. `skills/kieran-flanagan-content-engine/workflows/01-talking-points.md`

### 1.5. Fetch Visual Context if Source is Video
If source is a YouTube URL, recorded talk, or video file, fetch frame-grounded context — slide content, demonstrations, and on-screen text are often the highest-density talking points and are invisible in transcript-only mining:
```bash
// turbo
python3 execution/fetch-video-context.py "<source-url-or-path>" "<source-slug>" || true
```
See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). Wrapper auto-skips non-video sources.

### 2. Execute Workflow
Follow the workflow in `01-talking-points.md` using the loaded genius context. If visual-context.md exists, mine slide quotes, demo callouts, and on-screen text as their own talking-point candidates.

### 3. Save Output
Save talking point library to `.tmp/kieran-flanagan/talking-points.md`.
