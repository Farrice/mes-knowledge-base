# AI Platform Prompting & Production Workflows

## Higgsfield Cinema Studio 3.0

### The Logical Anchor System
Higgsfield uses a reasoning engine that interprets prompts through physics-aware logic. Structure prompts with:
1. **Subject Anchor** — Specific, detailed subject description (not vague)
2. **Physics Anchor** — Motion that obeys real-world physics (gravity, momentum, fluid dynamics)
3. **Environment Anchor** — Atmospheric details that ground the scene
4. **Camera Anchor** — Specific shot type, movement, and lens
5. **Light Anchor** — Direction, quality, and color of light

### Higgsfield Model Chain
| Step | Model | Purpose |
|---|---|---|
| 1 | Popcorn | Quick concept validation (2-3s clips) |
| 2 | Seedance 1.5 Pro | Motion refinement, dance/movement |
| 3 | Veo 3.1 | High-fidelity generation, complex scenes |
| 4 | Sora 2 Enhancer | Quality upscaling and detail enhancement |
| 5 | Recast | Style transfer and aesthetic refinement |
| 6 | SoulID | Character consistency across shots |
| 7 | Higgsfield Upscale | Resolution enhancement to 4K |

### Genre Presets
| Genre | Visual Treatment | Speed | Color |
|---|---|---|---|
| Horror | High contrast, desaturated, grain | Slow with sudden bursts | Cool blue-green, red accents |
| Action | High saturation, sharp, dynamic | Fast cuts, speed ramps | Warm, teal-orange |
| Romance | Soft, warm, shallow DOF | Slow, flowing | Warm pastels, golden |
| Sci-Fi | Clean, high contrast, cool | Measured, deliberate | Blue, cyan, white |
| Documentary | Natural, handheld, available light | Real-time, observational | Neutral, desaturated |
| Fashion | Stylized, bold color, sharp | Slow, deliberate, posed | Brand-specific |
| Music Video | High energy, creative lighting | Beat-synced, dynamic | Neon, saturated |

### The 9-Step Solo Studio Pipeline
1. **Sketch-to-Video Pre-Viz** — Rough concept → Popcorn for quick validation
2. **Reference World Building** — Generate 9 reference images establishing the visual world
3. **Core Generation** — Primary video generation with Veo 3.1 or Seedance
4. **Genre Preset Application** — Apply genre-specific color, speed, and mood
5. **Speed Ramp Integration** — Add dynamic pacing (Flash In, Slow Burn, Heartbeat, etc.)
6. **Sora 2 Enhancement** — Quality pass for detail and coherence
7. **Higgsfield Upscale** — Resolution boost to 4K
8. **SoulID Consistency** — Lock character appearance across multi-shot sequences
9. **Asset Standardization** — Export at proper specs for delivery platform

## Kittl AI Platform

### Kittl Image Board (Design)
The building blocks formula:
```
[SUBJECT] + [STYLE] + [COMPOSITION] + [COLOR] + [TEXTURE] + [TYPOGRAPHY] + [BACKGROUND]
```

Key principles:
- **Define the Allowed** — Tell Kittl exactly what you want to see
- **Define the Locked** — Specify what must NOT change
- Kittl excels at graphic design, logos, patterns, and typography-heavy work
- Use "vector illustration" or "flat design" for clean graphic outputs
- Use "photorealistic" or "studio photography" for product shots

### Kittl Video Board (Animation)
Modular prompt structure:
```
CAMERA: [movement and framing]
ACTION: [what happens in the scene]
AUDIO: [sound design direction]
TEXT: [any overlay text or titles]
```

### Kittl Flows — Node Pipeline
**Blueprint Production Pipeline:**
1. Photo Reference → 2. Outline Extraction → 3. Style Application → 4. Multi-Angle Generation → 5. Detail Close-Ups

**Design-to-Mockup-to-Video Pipeline:**
1. Design on Image Board → 2. Apply to Mockup → 3. Animate on Video Board

### Kittl Video Engine Comparison
| Engine | Strength | Duration | Best For |
|---|---|---|---|
| Veo 3.1 | Cinematic quality, complex scenes | 5-8s | Hero content, cinematic |
| Seedance 1.5 Pro | Motion quality, dance/movement | 5s | Fashion, movement, dance |
| Kling 3.0 | Fast generation, good quality | 5s | Quick iterations, social |
| Wan 2.1 | Artistic style, anime | 5s | Stylized content, anime |
| Ray 2 | Photorealism, product | 4s | Product shots, realism |

## Midjourney v6

### Prompt Structure
```
[SUBJECT DESCRIPTION], [ENVIRONMENT/SETTING], [LIGHTING], [CAMERA/LENS], [STYLE/AESTHETIC], [MOOD/ATMOSPHERE], [QUALITY MODIFIERS] --ar [ASPECT] --v 6 --s [STYLIZE 0-1000]
```

### Key Parameters
| Parameter | Range | Effect |
|---|---|---|
| --s (stylize) | 0-1000 | 0 = literal, 1000 = maximum artistic interpretation |
| --ar | Any ratio | Aspect ratio (16:9, 9:16, 1:1, 3:4, etc.) |
| --c (chaos) | 0-100 | Variation between outputs |
| --w (weird) | 0-3000 | Unconventional aesthetic |
| --no | Text | Negative prompt (exclude elements) |
| --q | 0.25-2 | Quality/detail level |

### Stylize Guide
| Range | Effect | Use Case |
|---|---|---|
| 0-100 | Very literal, follows prompt closely | Technical/specific needs |
| 100-300 | Balanced literal + artistic | Most commercial work |
| 300-600 | Artistic interpretation dominant | Editorial, mood pieces |
| 600-1000 | Maximum artistic freedom | Abstract, experimental |

## Flux Pro

### Prompt Structure
```
[HIGHLY DETAILED SUBJECT], [PRECISE ENVIRONMENT with specifics], [LIGHTING: direction, quality, color temp], [CAMERA: specific lens, aperture, ISO], [COLOR TEMPERATURE in Kelvin], [MOOD/ATMOSPHERE]
```

### Key Strengths
- Best-in-class photorealism
- Excellent text rendering in images
- Strong prompt adherence
- Natural skin tones and textures
- Precise lighting control

### Best Practices
- Be extremely specific about lighting direction ("light from upper left at 45 degrees")
- Specify camera settings like a real photographer ("Canon EOS R5, 85mm f/1.4, ISO 200")
- Include material descriptions ("matte cotton," "brushed aluminum," "frosted glass")
- Describe the exact environment, not just "studio" but "white cyclorama studio with infinity curve"

## Universal Prompting Rules

1. **Specificity beats length.** "85mm f/1.4 lens" beats "beautiful blurry background"
2. **Front-load the subject.** Put the most important element first
3. **Use real-world references.** "Shot on Arri Alexa" or "Hasselblad medium format" signals quality
4. **Describe light, not mood.** "Warm golden backlight at 45 degrees" beats "beautiful lighting"
5. **Include negative space.** Tell the AI what NOT to include
6. **Think in layers.** Subject → Environment → Light → Camera → Style → Mood
7. **Test with cheap models first.** Validate concepts with Popcorn/Kling before using Veo 3.1
