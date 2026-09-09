---
description: "/video-to-shorts — Long-form video → scored, face-aware 9:16 clips with burned captions for a named brand: BRAND LOCK → Scrapes 00-longform-to-shortform (yt-dlp, WhisperX, 5-category clip scoring, reframe, caption burn). Publish step OFF — sends stay human; his voice only, no TTS."
---
<!-- thin front door for the vendored Scrapes Skill Systems (2026-09-02). Machinery = .claude/skills/00-longform-to-shortform (+ vid-clip-selection, vid-clip-extractor, vid-ffmpeg-edit, tool-transcription). Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md -->

# /video-to-shorts — clips out of a long video, never posted

State the scale in one line: one source video, N clips (their scorer picks; cap it), captions on/off.

## Steps
1. **BRAND LOCK** — `python3 execution/scrapes_brand.py resolve --from-prompt "<ask>" --cwd "$PWD"`; exit 3 → ask. Caption color and fonts come from the locked brand's `tokens.json` / `design-tokens.md` (their `vid-ffmpeg-edit` reads design tokens for the highlight color) — pass `brand_context_path` explicitly.
2. **Publish OFF** — run the pipeline with the POST phase disabled (`publishing.mode` skip / no `l2s-content-packager` publish). Titles, descriptions, hashtags may be generated as a package; nothing is uploaded. `tool-video-upload` upload step and `tool-zernio-social` stay off.
3. **Scrapes machinery** — invoke `00-longform-to-shortform` with the URL or local file. Free: yt-dlp, WhisperX (local), OpenCV reframe, FFmpeg. If it proposes AI illustrations (`viz-image-gen`), state the count and cost first and run `openai_budget_guard.py check` for the GPT path.
4. **Our floor** — no TTS, no voice clone (his VO only). Clip captions run `python3 execution/prose_classifier.py check` on the package text. Any on-screen claim in the package gets a claim tag.
5. **Compound** — `asset_index.py` line per rendered clip (src=scrapes/vid-ffmpeg-edit, cost 0 unless illustrated); learnings entry under `## 00-longform-to-shortform`; `chain_runner.py finalize --skill vendor:00-longform-to-shortform --workflow video-to-shorts`; handoff on `<brand>-video`.

## Never
Auto-post. TTS or cloned voice. Edit inside `.claude/skills/*`. Skip the brand lock because "it's obviously his video".
