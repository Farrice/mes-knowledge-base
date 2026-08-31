---
date: 2026-07-16
session: kieran-flanagan second-brain extraction
name: sparse-frames-focused-watch-zoom-midbuild-drop
problem_class: extraction / video frames / sparse sampling
domain: research
status: proven
problem_signature: "a long video extraction comes back with frames spread thin across the whole clip (the tool prints its own frame-coverage-is-sparse warning), the demo or screen-share segment gets 2-3 accidental frames, and the extraction quietly paraphrases what the speaker said about the screen instead of what the screen showed"
tags: [extraction, video, frames, watch, screen-recording, subagent]
---
# Sparse Frames → Focused /watch Zoom → Mid-Build Schema Drop

**Date**: 2026-07-16
**Problem solved**: A 20-minute video extraction under `fetch-video-context.py` gets ~100 frames spread thin across the full clip ("sparse at this length" — the tool's own warning). The demo/slides sections — where an on-screen system's REAL schema lives (field names, folder paths, confidence badges, card layouts) — come through as 2-3 accidental frames, and the extraction quietly falls back to transcript paraphrase for exactly the material that matters most. This is the transcript-only-generic failure (see `2026-07-07-transcript-only-extraction-generic-output.md`) recurring in visual form: frames exist, but not the right ones.

**Context**: Kieran Flanagan second-brain extraction (video nTiMbqFwv4c). First pass: 100 frames / 1224s. The demo UI (typed vault paths, priority-card schema, ingest triage lane) was under-sampled while the builder agent was already mid-flight.

---

## The Solution (3 steps, ~5 min, $0)

1. **Zoom with /watch on the local file** — the first fetch already downloaded the video to `extractions/<expert>/download/video.mp4`. Re-run the watch script focused on the demo/slides range; scene-detection on screen recordings is precise because the picture is static between real transitions:
   ```bash
   python3 <watch-skill>/scripts/watch.py "extractions/<expert>/download/video.mp4" \
       --start 9:00 --end 17:30 --out-dir extractions/<expert>/watch-demo-zoom --max-frames 60
   ```
   (20 distinct scene frames came back — every real UI state, no filler.)
2. **Conductor reads the frames and DECODES them into schema language** — not "there's a dashboard" but "priority card = title + urgency tag + WHY NOW / DEPENDS ON (named person) / SUGGESTED ACTION columns; blockers route to `<project>/blockers/*.md` with owner·age·severity·next metadata." The decoding is the value; raw frame paths alone don't transfer.
3. **SendMessage the decoded schema to the running builder agent mid-flight** — numbered items, each naming the frame + timestamp + which target workflow it belongs in, closing with "frames win over transcript inferences; report unchanged otherwise." The builder folds it in without a restart (this session: all 6 items incorporated, none contradicted, workflows shipped with verbatim UI contracts).

## Why it works
- Scene-aware selection over a **screen-recording segment** is near-lossless: static frames dedupe away, every kept frame is a distinct UI state.
- The mid-build drop avoids the parallel-builders-stale-contracts failure (`2026-07-07`) from the other direction: instead of the builder missing new files, the conductor pushes new *evidence* into the builder's context the moment it exists.

## Deploy when
- Any extraction where the source is >10 min AND contains a demo/screen-share/slides segment.
- Any time the visual-context report prints its own "frame coverage is sparse" warning.
- A builder agent is already running and new source evidence lands: decode + SendMessage beats restart.

## Anti-pattern guarded
Shipping "mastery" extraction workflows whose on-screen system details are paraphrased from what the speaker *said about* the screen rather than what the screen *showed*.
