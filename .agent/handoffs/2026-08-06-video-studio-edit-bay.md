---
thread: video-studio-edit-bay
status: ready
resume_hint: Run Pilot P1: Parallax essay → VOX explainer; start with script-annotation, then tell Farrice exactly what VO to record
unfinished: P1-P3 pilots unrun; HyperFrames cloned but unwired; stock APIs untested (keys pending); 9:16 reframe naive
branch: main
pin: true
---

# Edit Bay Video Studio — Build + Taste Layer (Bonanno pipeline, Higgsfield retired)

## Purpose
- **Next session should do:** Run **Pilot P1 — a Parallax essay → VOX-style explainer** end-to-end through the Edit Bay: annotate the script, record Farrice VO, transcribe, cut, build 2-3 graphics through the taste gate, source free B-roll, mix, caption, export 3 formats, run the QA loop, deliver a publish-ready package for him to post.
- **Not in scope:** Rebuilding any part of the studio (it is verified live). Voice cloning or TTS narration (banned by his ruling). Higgsfield anything (retired). Auto-publishing (he posts).

## Load First
- `skills/video-studio/SKILL.md` — the front door: 6-stage pipeline, three modes, hard rules
- `skills/video-studio/workflows/produce-explainer.md` — the exact production cycle to follow for P1
- `skills/video-studio/style/graphics-taste.md` — MANDATORY named load before any comp (10 citable rules + slop tells + pre-render grep)
- `_active/farrice-brand/voice/video-style.md` — his brand video style + the Correction Log that must absorb every note before close-out
- `directives/video-studio-policy.md` — the 10 binding rules (no Higgsfield, free-first ladder, his VO, 3 formats, he posts)
- `extractions/brad-bonanno-edit-bay/extraction-report.md` — the MES 3.0 source decode (12 genius patterns, 8 hidden-knowledge points)
- `_active/video-studio-shakedown/05-assets/video/` — working reference: a real cutlist + render chain that passed QA

## Current State
- **Objective:** Give Farrice a conversational in-house video studio so production time stops being his content bottleneck — VOX explainers, shorts, LinkedIn video at credible quality from a laptop.
- **What is already done:**
  - Source video watched with 54 frames + full MES 3.0 extraction filed; folded into the existing brad-bonanno corpus (no duplicate expert minted).
  - **Execution layer built and verified live:** `execution/transcribe_local.py` (WhisperX local, word-level), `execution/edit_bay.py` (probe · cutlist-apply · overlay · captions-burn · audio-mix · transcode · qa-probe), `execution/video_qa.py` (seam-targeted inspect · fixlist-validate · apply-log), `execution/broll_source.py` (Pexels/Pixabay + owned-first search).
  - **Skill layer built:** `skills/video-studio/` — SKILL.md, 6 workflows, REVIEW.md picky-editor contract, cutlist/fixlist schemas, caption-style presets, global + brand style files, graphics-taste canon.
  - **E2E proof at $0:** 90s of real footage → transcript (310 timed words) → 6-shot cutlist → 1920×1080 render → burned captions → vertical + LinkedIn exports → qa-probe caught a genuine −17 LUFS defect → audio-mix → **all six checks pass**.
  - **Higgsfield fully retired** across `creative_router.py` (people → `fal-people`, cinema → seedance-720p, virality → manual-review), craft-map, `skills/generate/SKILL.md`, and the routing memory.
  - Memories written: `project_video-studio-edit-bay.md` + MEMORY.md row; `feedback_visual-tool-routing.md` updated for the retirement.
  - Commits on main: `7d43c4fb6` (build) · `ea01feaa3` (close-out) · `c8f605811` (taste layer) — pushed.
- **What is uncertain or stale:**
  - **HyperFrames is cloned but NOT wired** (`_active/hyperframes-studio/`, gitignored) — needs inspection before the overlay lane is real. Remotion remains the working comp engine meanwhile.
  - Stock B-roll is **untested** — `broll_source.py` has never made a live API call (no keys yet).
  - 9:16 export is naive center-crop (fine for talking-head, wrong for screen recordings) — subject-aware reframe is a known v2.
  - `graphics-taste.md` rules have never been exercised on a real comp; first pilot will show whether they bite or need sharpening.
- **Latest proof/receipt:** `_active/video-studio-shakedown/05-assets/video/renders/v02.mp4` — qa-probe PASS on all checks (resolution, fps, duration-vs-cutlist, loudness, black frames, silences). Frames at `renders/v01-captioned-frames/`.

## Blocking on Farrice (both trivial)
1. **Free API keys** → `.env`: `PEXELS_API_KEY` (pexels.com/api) and `PIXABAY_API_KEY` (pixabay.com/api/docs). ~2 minutes, no cost.
2. **A VO recording** for P1 — AirPods/phone quality is fine; the mix normalizes it. Nothing else about his kit is a blocker.

## Suggested Skills / Workflows
- `/video-studio` → `workflows/produce-explainer.md` — the P1 production cycle
- `/parallax` — to pick and adapt the source essay (restructure for the ear before annotating)
- `/voice-os` + `_active/farrice-brand/voice/VOICE-CARD.md` — if any script lines get rewritten
- `frontend-design` skill + `/satori-design-think` — the named taste loads for graphics
- `/jenny-hoyos-shorts` — when deriving shorts from the finished long-form
- `/assets-board` — every render/export lands there automatically

## Exact Next Prompt
```text
Run Pilot P1 through the Edit Bay: pick a Parallax essay and turn it into a VOX-style
explainer (VO-only mode — I'll record the voiceover myself). Start with
skills/video-studio/workflows/script-annotation.md so the script is beat-mapped and
annotated before anything else, then tell me exactly what to record. Load the
graphics-taste named stack before you build any comp. I want the publish-ready
package at the end: 16:9 + vertical + LinkedIn, titles, description, thumbnail.
```

## Acceptance Criteria
- An annotated, beat-mapped script exists with ≥1 annotation per beat and a named first-5-seconds treatment.
- Farrice records VO once, from a single clear instruction list (no back-and-forth about what to say).
- A rendered explainer with ≥2 graphics built through the taste gate, ≥1 B-roll source, music bed ducked, −14 LUFS, captions burned where required.
- `qa-probe` passes all checks; the picky-editor loop reaches verdict `pass` within 3 iterations.
- Three exports plus titles/description/thumbnail delivered as one package Farrice would actually post.
- Every note he gives lands in the brand style file's Correction Log before the edit closes.

## Risk Notes
- **Concurrent sessions:** two sibling sessions edited files in this tree during the build and committed mid-work (golden rule violated). Check `git status` and the session lock before writing; a sibling also pushed between commits.
- **ffmpeg trap:** Homebrew's ffmpeg on this Mac lacks libass — it cannot burn captions or draw text. The full static build at `tools/bin/ffmpeg` is preferred automatically by the scripts; never hardcode `/opt/homebrew/bin/ffmpeg` for filter work.
- **WhisperX SSL:** the wrapper wires certifi itself now; if alignment-model downloads still fail, that's the cause to check first.
- **Cost:** the whole pilot is $0 unless a beat genuinely needs generated B-roll (fal rung 4 — quote first, inside the $20/day cap, seedance-1080p stays hard-blocked).
- **Taste risk:** graphics are the fails-by-default stage; do not skip the named load or the pre-render grep because a comp "looks fine."

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
