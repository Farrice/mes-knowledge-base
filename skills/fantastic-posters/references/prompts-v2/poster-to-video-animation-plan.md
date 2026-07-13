---
name: "Fantastic Posters — Poster-to-Video Animation Plan"
source_prompt: born-v2
skill: fantastic-posters
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the image-to-video bridge: any poster this skill (or any other still) produced
becomes a video input frame, animated via Kling v3 Pro or Seedance 2.0. **The bridge pattern
requires a strong still first** — iterate on the poster at low/medium quality, lock the winner, THEN
animate. You never generate a video before a poster exists, and you always pre-flight the budget
guard before firing.

## Input Required

- **[POSTER_IMAGE_PATH]** — the locked start-frame poster (and, for a transition, a second locked end-frame poster that shares its visual DNA — style, palette, composition).
- **[MODE]** — one of: `single-shot` (one continuous motion beat) · `multi-shot-narrative` (2-4 distinct cut beats, Kling only) · `start-end-transition` (interpolated morph between two frames, Seedance only).
- **[DURATION]** — seconds; bounded by the ceiling table below.
- **[AUDIO]** — off | on | voice_control (voice_control only when the audio must lipsync to a script).
- **[MOTION_BEAT(S)]** — for single-shot/transition: one motion/camera description. For multi-shot: 2-4 distinct beat descriptions, one per shot.
- **[ELEMENTS]** (optional, multi-shot only) — reference images/clips for character/object consistency across shots, referenced in prompts as `@Element1`, `@Element2`.

## Execution Protocol

### Model selection
| Pick this | When |
|---|---|
| **Kling v3 Pro** (`fal_video_kling.py`) | Default — cheaper. Best for multi-shot narratives (`--multi-prompt`), character consistency (`--elements`), brand/social trailers. |
| **Seedance 2.0 720p** (`fal_video_seedance.py`) | Premium. Best for single-shot product reveals, cinematic camera moves, lipsync-grade synchronized audio, start→end frame transitions. |
| Seedance 480p | Budget option for quick experiments ($0.13/s vs $0.30/s). |
| Seedance 1080p | **HARD-BLOCKED** — ~$10/call, never attempt. |

### Mode A — Single-shot animate
One continuous motion beat from a locked still. Always start at the cheapest config that could
plausibly work (e.g., 5s Kling audio-off, ~$0.56) and escalate to Seedance only if that doesn't
capture what's needed.
```bash
python3 execution/fal_budget_guard.py check --mode=kling --duration=<N> --audio=<off|on>
python3 execution/fal_video_kling.py \
    --prompt "<motion beat: camera behavior + what moves + mood>" \
    --start-image "<poster path>" --duration <N> --audio <off|on>
python3 execution/fal_budget_guard.py log --mode=kling --duration=<N> --audio=<off|on> --status=success --actual-cost=<n> --brief="<one-line>"
```
Or, for cinematic single-shot / lipsync-grade audio:
```bash
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=<N>
python3 execution/fal_video_seedance.py \
    --prompt "<motion beat>" --image "<poster path>" \
    --duration <N> --resolution 720p --aspect <9:16|16:9> --audio <off|on>
python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=<N> --status=success --actual-cost=<n> --brief="<one-line>"
```

### Mode B — Multi-shot narrative (Kling only, `multi_prompt`)
Kling accepts a `multi_prompt` array — each entry is one shot's prompt; Kling distributes the total
duration across them and generates natural cuts. Author shots like a 3-act trailer: world →
disruption → resolve, or setup → reveal → consequence. Each shot needs ~3-4 seconds to land — 3
shots in 5s is unwatchable; use 9-11s minimum for a 3-shot spread. Cap at 2-4 shots; coherence
degrades past that.
```json
[
  {"prompt": "<shot 1: wide, establishing>"},
  {"prompt": "<shot 2: medium, the turn>"},
  {"prompt": "<shot 3: close, the payoff>"}
]
```
```bash
python3 execution/fal_budget_guard.py check --mode=kling --duration=<N> --audio=<off|on>
python3 execution/fal_video_kling.py \
    --multi-prompt <path-to-shots.json> \
    --start-image "<opening poster>" --duration <N> --audio <off|on> \
    [--elements <path-to-elements.json>]
python3 execution/fal_budget_guard.py log --mode=kling --duration=<N> --audio=<off|on> --status=success --actual-cost=<n> --brief="<n-shot trailer>"
```
If `[ELEMENTS]` is supplied, reference each in its shot prompt as `@Element1`/`@Element2`; elements
don't change pricing.

### Mode C — Start→end cinematic transition (Seedance only, `--end-image`)
Seedance interpolates motion between a start and end frame — a coherent transformation, not free
animation. Both frames must already exist and share visual DNA (same style, palette, framing, POV,
lighting, time of day) — Seedance relocates within physics, it does not invent new objects mid-shot;
anything that needs to "appear" must be implied in the start frame (e.g., an open doorway).
```bash
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=<N>
python3 execution/fal_video_seedance.py \
    --prompt "<how the scene transforms — physics, lighting shift>" \
    --image "<start poster>" --end-image "<end poster>" \
    --duration <N> --resolution 720p --aspect <9:16|16:9> --audio <off|on>
python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=<N> --status=success --actual-cost=<n> --brief="cinematic transition <start> → <end>"
```
6-8s gives the model enough room for believable motion; below 4s feels rushed, above 8s exceeds the
$3 ceiling.

## Output Contract

The chosen mode + model; the exact pre-flight budget-guard command; the exact wrapper command with
real flags; the estimated and actual cost; the post-run log command; the output file path
(`skills/fantastic-posters/out/<model>_<duration>s_<timestamp>.mp4`) and its destination project
folder.

## Output Skeleton

```markdown
**Mode**: [single-shot | multi-shot-narrative | start-end-transition]
**Model**: [kling | seedance-720p | seedance-480p]
**Pre-flight**: `python3 execution/fal_budget_guard.py check --mode=<mode> --duration=<N> [--audio=<off|on|voice_control>]`
→ estimated: $[n] (within $[2|3] ceiling)
**Run**: `python3 execution/fal_video_[kling|seedance].py --prompt "[motion beat]" --start-image "[path]" [--end-image "[path]"] [--multi-prompt [path]] --duration [N] [--resolution 720p] [--aspect X:Y] --audio [off|on|voice_control]`
**Log**: `python3 execution/fal_budget_guard.py log --mode=<mode> --duration=<N> --status=success --actual-cost=<n> --brief="[one-line]"`
**Output**: skills/fantastic-posters/out/[filename].mp4 → move to [project folder]
```

## Quality Gate

- [ ] A locked poster (or two, for a transition) exists before any video call — no video-first generation.
- [ ] The pre-flight `fal_budget_guard.py check` ran before the wrapper fired, and the estimate is within its ceiling ($2 Kling, $3 Seedance-720p; 1080p never attempted).
- [ ] Multi-shot mode uses 2-4 shots with ≥3-4s each — never 3+ shots in 5s.
- [ ] Start/end transition frames share visual DNA (style, palette, POV, lighting) — no new objects invented mid-shot.
- [ ] Voice-control audio was used only when a script exists to lipsync to.
- [ ] The actual cost was logged after the run.

## Creative Latitude

The motion beat is prose, not a template — write camera language and physics with the same rigor as
a shot list: what the camera does (push, pan, hold, dolly), what moves within frame, how light or
mood shifts. A single-shot beat that's just "animate this" has failed; one that specifies a
restrained camera move plus one purposeful in-frame motion and a mood word succeeds. For multi-shot,
push for a real narrative arc across the beats (world → disruption → resolve) rather than three
disconnected clips; for a transition, push for a transformation that feels earned by the start
frame's physics, not an arbitrary swap.

## Deploy When

A locked poster (or a matched pair) needs to become motion — a brand trailer, a product reveal, a
launch sequence, a narrative ad, a before/after transformation, or a micro-intro for a deck; NOT when
no strong still exists yet (animate after the poster is locked, never before) or when the need is
free-form motion with no clear destination frame (route to single-shot Kling instead of a
transition).
