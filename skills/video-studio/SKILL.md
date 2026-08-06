---
name: video-studio
description: 'The Edit Bay — in-house conversational video studio (VOX-style explainers, documentaries, shorts, LinkedIn video). Transcript-driven cutting, B-roll ladder, motion graphics as code, captions, music, publish-ready packages — all agent-operated, free-first. Use when Farrice says "edit this video/footage", "make an explainer/documentary/short", "cut this recording", "add B-roll/captions/music", "turn this essay/post into a video", or any video production ask. Front door for three modes: talking-head, VO-only, zero-camera (his recorded VO + assembled visuals — NO voice clone, NO TTS narration, his ruling 2026-08-06). Source: Brad Bonanno agentic edit pipeline (extractions/brad-bonanno-edit-bay/), rebuilt on the house stack: WhisperX local + edit_bay.py ffmpeg assembly + HyperFrames/Remotion graphics + /generate (fal) — NO Higgsfield (retired 2026-08-06).'
version: "1.0"
expert: "Brad Bonanno (pipeline) × house craft-map masters (direction)"
domain: "agentic video editing + production"
---

# Video Studio — The Edit Bay

Raw inputs (script + any footage) → finished, captioned, 3-format, publish-ready video —
produced conversationally, reviewed by the agent's own eyes, compounding taste every run.

**The doctrine (from the extraction — internalize, don't re-derive):**
1. **Give the agent the missing sense.** Ears = `transcribe_local.py` word timestamps. Eyes = seam-targeted frame extraction of the render. Never conclude "can't" before naming the missing input.
2. **Controllable inspection > passive comprehension.** Review frames at cuts/graphic-edges/caption onsets — never uniform sampling, never a video-understanding model.
3. **Solved vs fails-by-default.** Rough cuts (transcript problem) = solved, spot-check only. Anything visual (overlays, captions, graphics) = fails by default, QA loop MANDATORY.
4. **Corrections compound or you pay forever.** No edit closes until every Farrice note is promoted into the style file's Correction Log.
5. **Pre-work beats iteration.** An annotated script (10 min) saves hours of back-and-forth. Never start assembly from an unannotated script — run `workflows/script-annotation.md` first.

## Pipeline (six stages — each one agent turn + one CLI call)

| # | Stage | Tool | Cost |
|---|-------|------|------|
| 1 | Transcribe | `python3 execution/transcribe_local.py <media> --project <slug> --srt` | $0 local |
| 2 | Rough cut | agent writes `cutlist.json` from transcript (silences, filler, bad takes out) → `python3 execution/edit_bay.py cutlist-apply --project <slug>` | $0 |
| 3 | B-roll | ladder per `workflows/broll-ladder.md`: own footage → manifest search → free stock → graphics → `/generate` (fal, cost-gated) | $0 default |
| 4 | Graphics | HyperFrames (overlays on footage) / Remotion (full comps) — graphics render FIRST, enter cutlist as `render:` shots. **Taste gate: load `style/graphics-taste.md` § named stack (graphics-taste + `frontend-design` skill + style merge; grace-liu on fog) before ANY comp — never default-style** | $0 |
| 5 | Audio | `edit_bay.py audio-mix` — music bed, VO sidechain ducking, −14 LUFS | $0 |
| 6 | Export + QA | `edit_bay.py transcode` ×3 presets · `qa-probe` · `workflows/qa-review-loop.md` | $0 |

**Modes**: `talking-head` (his footage carries) · `vo-only` (his recorded VO + visuals — the VOX default and current-gear native mode) · `zero-camera` (same as vo-only; the name means no camera exists, NOT synthetic voice). **His voice is always his own — no clone, no TTS narration.**

## Workspace (per project)

```
_active/<slug>/05-assets/video/
  project.json  cutlist.json  transcript.json  style-overrides.md
  footage/   broll/{stock,generated,screen}/   audio/{vo,music,sfx}/
  graphics/{hyperframes,remotion}/   captions/   renders/   exports/
```
Auto-indexed to `/assets-board` by the existing sweep. Renders version as `v01.mp4, v01-frames/, v01-fixlist.json`.

## Style files (3-level merge — read ALL before any graphic/caption decision)

1. `skills/video-studio/style/video-style-default.md` (global floor)
2. `_active/farrice-brand/voice/video-style.md` (**the compounding one** — corrections land here)
3. `_active/<slug>/05-assets/video/style-overrides.md` (project)

## Workflows

| Workflow | Use when |
|---|---|
| [produce-explainer](workflows/produce-explainer.md) | Full production: annotated script → shipped 3-format package |
| [script-annotation](workflows/script-annotation.md) | Turn a script/essay into an annotated, beat-mapped shooting doc |
| [qa-review-loop](workflows/qa-review-loop.md) | Render exists → picky-editor review → fixlist → revise (max 3 passes) |
| [broll-ladder](workflows/broll-ladder.md) | A beat needs a visual you don't have |

Reviewer contract: [REVIEW.md](REVIEW.md) · Schemas: `schemas/` · Caption presets: `caption-styles.json`

## Hard rules

- **NO Higgsfield** (retired 2026-08-06). Generated assets only via `/generate` + craft-map grammar + `fal_budget_guard`. seedance-1080p stays HARD-BLOCKED (720p is fine at B-roll/overlay scale).
- **Free-first ladder is ordered and mandatory** — paid generation is rung 4, quoted before running.
- **LinkedIn exports always burn captions** (silent-autoplay-safe).
- Stock downloads carry `license` + `source_url` in the manifest (audit trail).
- Every render manifest-indexed; every shipped video has a full version chain.
- Distribution = publish-ready packages; **Farrice posts** (sends stay human).
- Policy canon: `directives/video-studio-policy.md`. Codex parity: everything here is CLI + files on disk — no harness-specific APIs.

## Composes with (extend, never rebuild)

`skills/remotion-video-creation/` (34 rules; pacing = `rules/high-retention-editing.md`) · `skills/generate/` + craft-map masters (direction layer) · `skills/curious-refuge` (storyboard floor) · `skills/dave-clark` (flat-to-cinematic audit) · `skills/brad-bonanno-explainer-architecture` (what to SAY; this skill is how to CUT it) · `skills/jenny-hoyos-shorts` (shorts grammar) · fantastic-studio (thumbnails) · hook skills (titles).
