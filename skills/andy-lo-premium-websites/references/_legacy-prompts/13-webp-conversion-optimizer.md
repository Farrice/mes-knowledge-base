---
name: webp-conversion-optimizer
description: Optimize video-to-WebP conversion for the perfect performance/quality balance
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

## Expected Output
- Optimized WebP file(s) ready for web deployment
- Performance validation completed
- Frame sequence (if split) named and organized

## When to Use
- After generating animation in Google Flow (Prompt #2)
- Before uploading to Supabase (Prompt #7)

## Genius Patterns Applied
- WebP Sequence Scroll Animation Hack (#8)
- Tool Specialization Pipeline (#3)
