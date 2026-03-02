---
name: motion-design-orchestrator
description: Convert static frames to premium parallax-ready animations using Google Flow
---

# Motion Design Orchestrator

## Purpose
Transform static visual assets into smooth, scroll-ready animations using Google Flow (Veo 3.1). This prompt guides the entire motion design process from frame upload to WebP conversion.

## System Prompt

You are Andy Lo, a premium AI website creator. You understand that motion is what separates a "$500 template site" from a "$15K agency site." Your animations are intentional — every movement serves the brand story. You use the **Bookend Frame Architecture**: define start + end, let AI generate the journey.

## User Prompt

```
I need to create premium motion design for a website using Google Flow.

**Assets Available:**
- Starting frame description: {{START_FRAME_DESC}}
- Ending frame description: {{END_FRAME_DESC}}
- Brand mood: {{BRAND_MOOD}}
- Animation placement: {{PLACEMENT}} (hero section / background / section transition / product showcase)

**Generate the following:**

### 1. Google Flow Setup Instructions
Step-by-step for converting these frames to motion:
1. Open Google Flow (labs.google.com/fx/tools/video-fx)
2. Switch to "Frames to Video" mode
3. Upload sequence: starting frame first, ending frame second
4. Set the motion prompt (below)

### 2. Motion Prompt for Google Flow
Write a precise animation prompt that describes:
- **Pacing**: How fast/slow the motion should feel (cinematic slow = 0.3x, natural = 1x, energetic = 1.5x)
- **Camera movement**: Static, slow pan, gentle zoom, orbital rotation, parallax shift
- **Element behavior**: What moves (background, foreground, particles, lighting)?
- **Atmospheric effects**: Lighting shifts, color temperature changes, depth-of-field changes
- **Emotional arc**: What feeling does the animation build toward?

**Important**: The motion should feel INTENTIONAL and PREMIUM. No random zooming. No chaotic particle effects. Every movement serves the visual arc from opening frame to closing frame.

### 3. Quality Settings
Specify:
- Resolution: Original (match source frames)
- Duration: {{DURATION}} seconds (recommend 3-6 for hero, 2-4 for sections)
- Style: Cinematic / Natural / Dynamic (based on brand mood)

### 4. WebP Conversion Protocol
After downloading the animation from Flow:
1. Open EasyGIF (or equivalent converter)
2. Settings:
   - Resolution: Original (do NOT downscale)
   - Frame rate: Use closest to native FPS (NOT maximum)
   - Quality: 85 (the sweet spot — higher adds file size without perceptible gain)
   - Loop: Forever (enabled)
3. Export as WebP
4. Split into individual frames if needed for scroll-triggered playback

### 5. Frame Storage
- Upload frames to Supabase bucket (public access)
- Note all frame URLs for website assembly step
- Naming convention: `{{PROJECT}}_frame_001.webp`, `{{PROJECT}}_frame_002.webp`, etc.

**What to watch for:**
- Transitions should be smooth — no jarring cuts or stutters
- Colors should remain consistent between frames (no random color shifts)
- Motion should create DEPTH — elements at different distances moving at different speeds
- The ending should feel like a natural resolution, not an abrupt stop
```

## Expected Output
- Complete Google Flow setup guide
- Optimized motion prompt
- Quality/conversion settings
- Frame storage instructions

## When to Use
- After visual direction is established (Prompt #1)
- When converting any static design to animated
- When creating scroll-triggered parallax effects

## Genius Patterns Applied
- Bookend Frame Architecture (#2)
- Tool Specialization Pipeline (#3)
- WebP Sequence Scroll Animation Hack (#8)
