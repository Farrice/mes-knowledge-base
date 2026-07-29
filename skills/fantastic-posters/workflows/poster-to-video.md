# Workflow: Poster → Video Animation (Bridge Pattern)

> **Use**: Animate any poster generated in this skill (or any other still image) into video via Seedance 2.0 or Kling v3 Pro
> **Default model**: Kling v3 Pro (cheaper, multi-shot capable)
> **Default config**: 5s, audio on, $0.84/call
> **Hard rule**: ALWAYS pre-flight via `fal_budget_guard.py check` before generating

## Model Selection

| Pick this | When |
|---|---|
| **Kling v3 Pro** (`fal_video_kling.py`) | Default. Cheaper. Best for multi-shot narratives (`--multi-prompt`), character consistency (`--elements`), brand trailers, social trailers |
| **Seedance 2.0 720p** (`fal_video_seedance.py`) | Premium. Best for single-shot product reveals, cinematic camera moves, lipsync-grade synchronized audio, start→end frame transitions |
| Seedance 480p | Budget option for quick experiments ($0.13/s vs $0.30/s) |
| Seedance 1080p | **HARD-BLOCKED** — too expensive (~$10 single call) |

> **Prompt grammar**: For cinematic Seedance prompt construction, load `skills/cinema-worldbuilder-pro/SKILL.md` (block order, FOV in degrees, Capture Realism, write-the-visible). Fal surface = no @tags; use prose descriptors. Any still that seeds video follows the 18% gray flat-plate rule (`skills/banana-pro-director/SKILL.md`).

## Use-Case Presets (within $2 Kling / $3 Seedance-720p ceilings)

### My.BPM product reveal
**Goal**: Animate a streetwear poster into a 6-second product reveal with synthwave audio.
```bash
# Pre-flight
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=6
# Estimated: $1.81

# Generate
python3 execution/fal_video_seedance.py \
    --prompt "slow camera dolly forward through neon mist, palm tree silhouette sways, BPM logo glows pulse with the synthwave beat, no people" \
    --image "skills/fantastic-posters/out/<your-mybpm-poster>.png" \
    --duration 6 --resolution 720p --aspect 9:16 --audio on

# Log (uses --actual-cost from generator output)
python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=6 \
    --status=success --actual-cost=1.8144 \
    --brief="My.BPM product reveal"
```

### Parallax cover trailer
**Goal**: Animate a Parallax editorial cover into a 5-second silent trailer for Substack Notes.
```bash
python3 execution/fal_budget_guard.py check --mode=kling --duration=5 --audio=off
# Estimated: $0.56

python3 execution/fal_video_kling.py \
    --prompt "subtle camera push-in, dust particles drift in warm light, page edges curl gently, contemplative mood" \
    --start-image "skills/fantastic-posters/out/<your-parallax-cover>.png" \
    --duration 5 --audio off

python3 execution/fal_budget_guard.py log --mode=kling --duration=5 --audio=off \
    --status=success --actual-cost=0.56 \
    --brief="Parallax cover trailer"
```

### Jen's listing reveal
**Goal**: Animate a luxury-real-estate poster into an 8-second cinematic camera pan with ambient audio.
```bash
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=8
# Estimated: $2.42

python3 execution/fal_video_seedance.py \
    --prompt "slow camera reveal pan from foyer through living room toward backyard pool, golden hour light, gentle birdsong and distant breeze, no people, magazine-spread quality" \
    --image "<jen-listing-poster>.png" \
    --duration 8 --resolution 720p --aspect 16:9 --audio on

python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=8 \
    --status=success --actual-cost=2.4192 \
    --brief="Jen listing reveal"
```

### Strategy brief micro-intro
**Goal**: Animate a deliverable cover into a 3-second silent intro for video deck embedding.
```bash
python3 execution/fal_budget_guard.py check --mode=kling --duration=3 --audio=off
# Estimated: $0.34

python3 execution/fal_video_kling.py \
    --prompt "subtle motion: typography settles into place, faint geometric grid materializes, restrained corporate elegance" \
    --start-image "<deliverable-cover>.png" \
    --duration 3 --audio off

python3 execution/fal_budget_guard.py log --mode=kling --duration=3 --audio=off \
    --status=success --actual-cost=0.336 \
    --brief="Strategy brief micro-intro"
```

## Cost Envelope Reference

| Preset | Mode | Duration | Audio | Cost | Within ceiling? |
|---|---|---|---|---|---|
| My.BPM reveal | seedance-720p | 6s | on | $1.81 | ✓ ($3 ceiling) |
| Parallax trailer | kling | 5s | off | $0.56 | ✓ ($2 ceiling) |
| Jen listing pan | seedance-720p | 8s | on | $2.42 | ✓ ($3 ceiling) |
| Brief micro-intro | kling | 3s | off | $0.34 | ✓ ($2 ceiling) |

## Anti-Patterns

- ❌ **Generating a video before generating the poster.** The bridge pattern requires a strong still first. Iterate on the poster at low/medium quality, lock the winner, THEN animate.
- ❌ **Voice control without a script.** `--audio=voice_control` ($0.196/s) is for cases where you want the audio to lipsync to a character. For ambient/music, use `--audio=on`.
- ❌ **15-second videos by default.** Most uses don't need 15s. Default to 3-8s. Longer = more expensive AND more likely to drift in motion coherence.
- ❌ **Skipping the pre-flight check.** Fal does not refund if you generate something useless. The guard saves you from wasted spend.
- ✅ **Always start at the cheapest config** that could plausibly work. If 5s Kling audio-off ($0.56) doesn't capture what you need, escalate to Seedance.

## Output Pipeline

1. MP4 lands in `skills/fantastic-posters/out/<model>_<duration>s_<timestamp>.mp4`
2. Move to project folder: `_active/mybpm/videos/`, `_active/farrice-brand/content/parallax-packages/<edition>/trailer.mp4`, `_active/jen-santulan/listings/<address>/reveal.mp4`, etc.
3. For social distribution: re-encode if needed (Substack supports MP4 ≤256MB, Instagram has its own constraints)
4. For video deck embedding: keep as-is (most slide tools handle MP4)

## Output Schema

Each animation run produces one **Poster-to-Video Record**:

```markdown
## Poster → Video — <use-case preset name>
- Source still: `skills/fantastic-posters/out/<poster>.png` (generated and locked BEFORE this stage — never animate an unproven poster)
- Model: <kling|seedance-720p> · Duration: <Ns> · Audio: <off|on|voice_control> · Aspect: <9:16|16:9>
- Pre-flight: `fal_budget_guard.py check --mode=<model> --duration=<N> [--audio=<mode>]` → estimated $<n>, within ceiling
- Output file: `skills/fantastic-posters/out/<model>_<duration>s_<timestamp>.mp4` → moved to `<project>/videos/<slug>/`
- Post-flight log: `fal_budget_guard.py log --mode=<model> --duration=<N> --status=success --actual-cost=<n> --brief="<preset name>"` ✓
```

Complete only when the source still predates this run (not generated in the same pass) and the log's `--actual-cost` is filled from the generator's real output, not the estimate.

## Quality Gate

- [ ] **Poster locked before animation** — the bridge pattern requires a strong still first; a video generated before the poster is proven is the named anti-pattern.
- [ ] **Cheapest plausible config tried first** — default to 3-8s before escalating to Seedance-720p or longer durations.
- [ ] **Audio mode matches intent** — `voice_control` only when lipsync to a script is needed; ambient/music uses `on`.
- [ ] **Duration stays within its model's ceiling** — $2 Kling / $3 Seedance-720p, verified against the Cost Envelope Reference table, not assumed.
- [ ] **Pre-flight ran before generation** — Fal does not refund a wasted call; skipping the guard is an explicit anti-pattern here.
- [ ] **Output moved to the destination project folder** — not left sitting in `out/`.

**Pass criteria**: all checked. Animating an unlocked poster or skipping the pre-flight check fails this gate regardless of how the clip looks.
