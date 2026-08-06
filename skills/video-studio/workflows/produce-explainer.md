# Produce Explainer — annotated script → shipped 3-format package

The full production cycle. Every step names its artifact; nothing ships without the QA loop.

## 0. Intake (one turn)
- Confirm: project slug, mode (talking-head / vo-only / zero-camera), target length, platform priority.
- Scaffold `_active/<slug>/05-assets/video/` tree + `project.json` (`{"v":1,"project":slug,"mode":...,"formats":["yt-169","vert-916","linkedin"],"style_merge":["default","farrice-brand","project"],"current_render":null}`).
- Read all three style files NOW (default → brand → project). Load `skills/remotion-video-creation/rules/high-retention-editing.md` for pacing law.

## 1. Script + annotation
- If the script isn't beat-mapped and annotated → run `script-annotation.md` first (never assemble from a bare script).
- Output: script.md with beat IDs and `[music:] [broll:] [graphic:] [camera:] [ref:] [gesture:]` tags → mirrored into `cutlist.json.beats[]`.

## 2. Record + transcribe
- Farrice records VO/takes per beat (voice-memo grade OK — `edit_bay.py audio-mix` normalizes; light cleanup: ffmpeg afftdn).
- Drop files in `footage/` or `audio/vo/`. Then: `python3 execution/transcribe_local.py <file> --project <slug> --srt`.

## 3. Rough cut (SOLVED stage — no loop needed)
- From `transcript.json`, write `shots[]`: remove silences >0.7s, filler words, false starts, weakest take per repeated line. Cut on word boundaries. Pacing per the retention rules (staccato for hooks, measured for explanation).
- `python3 execution/edit_bay.py cutlist-apply --project <slug> --dry-run` → check plan → apply → `renders/v01.mp4`.
- Spot-check duration vs. target; do NOT frame-review a rough cut.

## 4. B-roll + graphics (FAILS-BY-DEFAULT stage)
- Per annotated beat: source visuals via `broll-ladder.md`. Fire any paid generation EARLY (async — keep working while it renders; quote cost first).
- Graphics: **TASTE GATE FIRST — load the named stack in `style/graphics-taste.md` § "The named load"** (graphics-taste rules + `frontend-design` skill + style-file merge; grace-liu on taste-fog). A comp built without the load is a defect even if it looks fine — the 2026-08-02 freehand-vs-loaded scar applies to graphics too. Run the file's deterministic pre-render grep before every render. Then build comps (HyperFrames overlay / Remotion full-frame) → `graphics/` → add as `role:"graphic"` shots with `render:` paths, or overlay via `edit_bay.py overlay`.
- Honor `[gesture:]` cues: time overlay entrances to gesture/emphasis moments found in the rough-cut frames.

## 5. Audio
- `edit_bay.py audio-mix --in <render> --music <bed> --duck -10 --lufs -14 --out <next-version>` (+ `--sfx t=SEC:file` per annotation).

## 6. Captions
- `edit_bay.py captions-burn` with the platform style. Apply the brand wordlist corrections (style file § wordlist) to the SRT BEFORE burning.

## 7. QA loop (MANDATORY)
- Run `qa-review-loop.md` — deterministic probe + picky-editor frame review → fixlist → revise cutlist → re-render. Max 3 iterations; every iteration appends to `cutlist.revisions[]`.

## 8. Export + package
- `edit_bay.py transcode` → `exports/` for yt-169, vert-916, linkedin (captions burned for linkedin ALWAYS, shorts usually).
- Package per `package-release.md` (Phase 4; until it exists: titles via hook skills, thumbnail via /generate + fantastic-studio, description + hashtags). Deliver as one publish-ready folder + a forwardable summary. **Farrice posts.**

## 9. Close-out gate (the compounding step — NON-NEGOTIABLE)
- Present Feedback Triad (like / don't like / top changes).
- EVERY Farrice note → `_active/farrice-brand/voice/video-style.md` Correction Log (dated) BEFORE the edit is marked done.
- Update `project.json.current_render`, confirm manifest indexing, log fal spend if any.
