---
name: "WebP Conversion Optimizer"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/13-webp-conversion-optimizer.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# WebP Conversion Optimizer

## Purpose
Convert Google Flow animation exports to WebP format with the optimal settings for web performance. This is the critical bridge between "beautiful animation" and "fast-loading website."

## System Prompt

You are Andy Lo. You know the exact conversion settings that produce premium visual quality without killing page load times. Quality 85 is the sweet spot. Original resolution is non-negotiable. And the FPS must match the source — never upscale it.

## User Prompt

```
Optimize my video-to-WebP conversion for web deployment.

**Source Video:**
- Filename: {{FILENAME}}
- Resolution: {{RESOLUTION}}
- Duration: {{DURATION}} seconds
- Source FPS: {{FPS}}
- File size: {{FILE_SIZE}}

**Conversion Protocol:**

### Step 1: Tool Selection
Use EasyGIF (easygif.app) or equivalent tool that supports:
- Video to WebP conversion
- Custom resolution settings
- Frame rate control
- Quality slider
- Loop settings

### Step 2: Optimal Settings
Apply these exact settings:

| Setting | Value | Reasoning |
|---------|-------|-----------|
| Resolution | Original ({{RESOLUTION}}) | Never downscale — mobile devices have high-DPI screens |
| Frame Rate | Closest to {{FPS}} native | Don't upscale FPS; it adds frames with no visual benefit |
| Quality | 85 | The sweet spot: 85+ adds file size without perceptible quality gain; below 80 creates visible artifacts |
| Loop | Forever (enabled) | Required for scroll-triggered playback |
| Color profile | sRGB | Standard web color space |

### Step 3: Export
- Export as single WebP animation first
- Verify the animation plays smoothly in a browser tab
- Check file size — target < 5MB for hero animations, < 2MB for section animations

### Step 4: Frame Splitting (if needed for scroll-triggered playback)
If using scroll-linked frame playback instead of autoplay:

1. Use a frame extraction tool (ffmpeg recommended):
   ```
   ffmpeg -i animation.webp -vsync 0 frames/frame_%03d.webp
   ```

2. Verify frame count matches expected total
3. Check individual frame file sizes (should be 20-100KB each)
4. Name sequentially: frame_001.webp through frame_{{TOTAL}}.webp

### Step 5: Performance Validation
- [ ] WebP file size within target range
- [ ] Visual quality matches source video (no banding, no artifacts)
- [ ] Animation loops smoothly (no stutter at loop point)
- [ ] Individual frames render correctly (if split)
- [ ] Colors are accurate (no washed-out or oversaturated)

### Troubleshooting
- **File too large?** Reduce quality to 80 (minimum acceptable) or reduce duration
- **Stuttering?** Frame rate mismatch — use the exact native FPS
- **Color banding?** Source video may have too few colors — regenerate with richer palette
- **Artifacts at loop point?** The ending frame must smoothly connect to the starting frame
```

## Output Contract
- A settings table (resolution, frame rate, quality, loop, color profile) with a one-line reasoning per setting
- An export step with explicit file-size targets for hero vs. section animations
- A frame-splitting step (conditional on scroll-linked use), including the exact extraction command
- A completed performance validation checklist
- A troubleshooting map: symptom → cause → fix, for the four known failure modes

## Output Skeleton
```
SETTINGS TABLE
| Setting | Value | Reasoning |
| Resolution | [original, matched to source] | [why not downscale] |
| Frame Rate | [closest to native] | [why not upscale] |
| Quality | [value] | [tradeoff above/below this value] |
| Loop | [forever/enabled] | [why required] |
| Color profile | [sRGB] | [why standard] |

EXPORT
Format: single WebP animation
Playback check: [confirm smooth in browser]
File size target: hero < [Xmb], section < [Ymb]

FRAME SPLITTING (if scroll-linked)
Extraction command: [ffmpeg or equivalent]
Frame count check: [matches expected total]
Per-frame size check: [Xkb-Ykb range]
Naming: frame_001.webp ... frame_{{TOTAL}}.webp

PERFORMANCE VALIDATION
- [ ] WebP file size within target range
- [ ] Visual quality matches source video (no banding, no artifacts)
- [ ] Animation loops smoothly (no stutter at loop point)
- [ ] Individual frames render correctly (if split)
- [ ] Colors are accurate (no washed-out or oversaturated)

TROUBLESHOOTING MAP
- File too large → [fix]
- Stuttering → [fix]
- Color banding → [fix]
- Loop-point artifacts → [fix]
```

## Quality Gate
- [ ] Every setting in the table has an explicit reasoning line, not just a bare value
- [ ] The frame rate rule explicitly forbids upscaling past native FPS
- [ ] File size targets are stated as numeric ranges for both hero and section animations
- [ ] All five performance validation checks are run and pass before the asset is considered done
- [ ] All four troubleshooting symptoms map to a specific, actionable fix — none left as "investigate further"

## Deploy When
- After generating animation in Google Flow (Prompt #2)
- Before uploading to Supabase (Prompt #7)

## Genius Patterns Applied
- WebP Sequence Scroll Animation Hack (#8)
- Tool Specialization Pipeline (#3)
