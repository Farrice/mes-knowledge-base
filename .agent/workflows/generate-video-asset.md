---
description: Generate video assets using the Keyframe-to-Video method for AI video tools
---

# /generate-video-asset

Generate **Start Frame**, **End Frame**, and **Motion Prompt** for any video scene. You execute manually in your tool of choice (Veo, Higgsfield, LoveArt, Kling, Runway), then return the `.mp4` for Remotion assembly.

> [!NOTE]
> This workflow produces the "ingredients" for AI video generation. It does NOT call APIs directly.

---

## 1. Input: Define the Scene

Provide a scene spec in this format:

```yaml
scene_name: "Chaos to Peace"
intent: "Show the transformation from overwhelm to clarity"
emotion_start: "Anxiety, frustration, drowning"
emotion_end: "Calm, control, clarity"
duration: "4-6 seconds"
camera_motion: "Slow push forward" # OR: Static, Pan, Dolly, Handheld
color_grade: "Cool/desaturated → Warm/golden"
```

---

## 2. Agent Execution

When I receive this spec, I will:

### Step A: Generate Start Frame
Using `generate_image` with a prompt like:
> "Cinematic still of [SCENE DESCRIPTION at START EMOTION]. [LIGHTING]. [FRAMING]. Photorealistic, 16:9."

### Step B: Generate End Frame
Using `generate_image` with:
> "Cinematic still of [SCENE DESCRIPTION at END EMOTION]. [LIGHTING]. [FRAMING]. Photorealistic, 16:9."

### Step C: Engineer Motion Prompt
Using PJ Accetturo's video generation patterns:
> "[START → END transformation]. [CAMERA MOTION]. [PHYSICS/EASING]. [COLOR SHIFT]. [DURATION]. Photorealistic, cinematic 16:9."

---

## 3. Output: Your Generation Package

You receive:

| Asset | What It Is | Your Action |
|-------|------------|-------------|
| `start_frame.png` | The opening keyframe | Upload to Veo/Kling as "Input Image" |
| `end_frame.png` | The closing keyframe (optional) | Use for tools that support end-frame guidance |
| `motion_prompt.txt` | The exact prompt for I2V generation | Paste into the text prompt field |
| `tool_notes.md` | Tool-specific recommendations | Reference for best results |

---

## 4. Your Execution (Manual Step)

1. Open your tool: **Google VideoFX**, **Higgsfield**, **LoveArt**, **Kling**, **Runway**, or **Pika**
2. Upload `start_frame.png` as the input image
3. Paste the `motion_prompt` into the text field
4. Select **4-6 second** duration, **16:9** aspect ratio
5. Generate and download the best take as `.mp4`
6. Drop the file into: `Google Antigravity/launch_video/public/`
7. Tell me the filename (e.g., `chaos_to_peace.mp4`)

---

## 5. Return to Antigravity

Once you provide the filename, I will:
1. Update `Composition.tsx` to use the video instead of static images
2. Apply **High-Retention Editing Rules** (cut timing, transitions, audio sync)
3. Render the final assembled video

---

## Example Request

```yaml
scene_name: "Janitor Mode Chaos"
intent: "Visceral overwhelm of admin tasks"
emotion_start: "Frantic anxiety"
emotion_end: "N/A (single-emotion scene)"
duration: "3-4 seconds"
camera_motion: "Handheld shake, jittery"
color_grade: "Cool blue monitor glow, desaturated"
```

**Expected Output:**
- `janitor_chaos_start.png` (AI Image)
- `motion_prompt_janitor_chaos.txt` (To paste into Veo)
- No end frame needed for single-state scenes
