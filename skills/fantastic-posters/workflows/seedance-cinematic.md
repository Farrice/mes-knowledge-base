# Workflow: Seedance Cinematic (Start → End Frame Transitions)

> **Use**: Animate a transformation between two posters — before/after reveals, transformation ads, narrative arcs
> **Model**: Seedance 2.0 720p (supports `--end-image-url` for frame interpolation)
> **Default config**: 8s, 720p, audio on
> **Cost**: $2.42 (within $3 Seedance-720p ceiling)

## Concept

Seedance 2.0 accepts BOTH `image_url` (start frame) and `end_image_url` (end frame). The model interpolates motion between them — generating a coherent transformation rather than free animation. This is the cinematic "morph" pattern: poster A → poster B with believable physics.

> **Prompt grammar**: For cinematic Seedance prompt construction, load `skills/cinema-worldbuilder-pro/SKILL.md` (block order, FOV in degrees, Capture Realism, write-the-visible). This is the Fal surface — no @tags; use prose descriptors. Any still that seeds video follows the 18% gray flat-plate rule (`skills/banana-pro-director/SKILL.md`).

## When to Use

- **Before/after product reveals**: empty room → furnished room (Jen)
- **Brand evolution**: vintage logo → modern logo for repositioning campaigns
- **Narrative arcs**: dawn → dusk, calm → storm, founder hooded → unhooded
- **My.BPM transformations**: garment folded → garment worn, store empty → store crowded
- **Parallax mood transitions**: edition opening pose → closing pose

**Don't use for**: free motion that doesn't have a clear "destination" frame (use Kling single-prompt instead).

## Standard Run

### Step 1: Generate two posters first

Use the existing `gen.sh` workflow to make a strong start frame AND end frame. They should share visual DNA (same style, palette, composition) but differ in the *moment*.

```bash
# Generate start frame
cd skills/fantastic-posters && ./gen.sh "<start brief>" --quality=high --style=<chosen>

# Generate end frame (use --refs to anchor visual continuity)
cd skills/fantastic-posters && ./gen.sh "<end brief>" --quality=high --style=<same> --refs=out/<start>.png
```

### Step 2: Pre-flight + animate transition

```bash
python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=8
# Estimated: $2.42

python3 execution/fal_video_seedance.py \
    --prompt "smooth cinematic transition: the scene transforms naturally from start to end, motion follows physics, lighting shifts to match" \
    --image "skills/fantastic-posters/out/<start>.png" \
    --end-image "skills/fantastic-posters/out/<end>.png" \
    --duration 8 --resolution 720p --aspect 16:9 --audio on

python3 execution/fal_budget_guard.py log --mode=seedance-720p --duration=8 \
    --status=success --actual-cost=2.4192 \
    --brief="cinematic transition <start> → <end>"
```

## Use-Case Examples

### Jen — empty listing → staged listing
- **Start frame**: Luxury-real-estate poster of empty interior
- **End frame**: Same room photo with furniture, art, warm lighting
- **Prompt**: "scene transforms as warm afternoon light fills the room, furniture and art appear naturally as if living here, golden hour"

### Parallax — opening mood → closing mood
- **Start frame**: Editorial cover, contemplative still
- **End frame**: Same composition with subtle resolution motion (e.g., dust settles, light shifts)
- **Prompt**: "subtle cinematic transition, the still composition releases tension, contemplative arc resolves"

### My.BPM — folded garment → worn garment
- **Start frame**: Streetwear-lookbook poster of folded hoodie on neon backdrop
- **End frame**: Same hoodie worn (silhouette only, no face) against same backdrop
- **Prompt**: "garment unfolds and rises into wear, atmospheric haze, synthwave palette holds, no face visible"

## Cost Reference (within $3 Seedance-720p ceiling)

| Duration | Cost | Within ceiling? |
|---|---|---|
| 4s | $1.21 | ✓ |
| 5s | $1.51 | ✓ |
| 6s | $1.81 | ✓ |
| 8s | $2.42 | ✓ |
| 10s | **BLOCKED** ($3.02) | over $3 |
| 15s | **BLOCKED** ($4.54) | over $3 |

**Rule of thumb**: For cinematic transitions, 6-8s gives the model enough room for believable motion. Below 4s feels rushed; above 8s exceeds the ceiling.

## Anti-Patterns

- ❌ **Wildly different start/end frames.** If the model can't find a motion path, output looks broken. Frames should share style, palette, framing.
- ❌ **End frame with new characters/objects appearing from nowhere.** Seedance interpolates, doesn't invent. If something needs to appear, it should be implied in the start frame (e.g., a doorway).
- ❌ **Using audio with no clear soundtrack intent.** Seedance auto-generates ambient sound; for branded video you may want silent + post-add music.
- ✅ **Match the start frame's POV and lighting in the end frame.** Same camera angle, same time of day. The model handles transitions, not relocations.

## Output Pipeline

Same as poster-to-video.md — MP4 lands in `out/`, move to project folder, deliver.
