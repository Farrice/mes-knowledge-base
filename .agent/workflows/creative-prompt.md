# Creative Prompt Generation

Generate production-ready AI prompts for any visual concept across Higgsfield, Kittl, Midjourney, and Flux platforms. Each prompt set includes 3 variants (safe, creative, wild card) with platform-specific syntax and parameters.

## Expert Loading

Load `skills/creative-direction/SKILL.md` at Tier 1. For complex or multi-platform prompts, load `genius.md` Section 3 (AI Platform Prompting) for full parameter references and model chains.

## Workflow

### Step 1: Identify the Target

- **What is being created?** (video, image, graphic design, mockup, photo, animation)
- **Which platform?** (Higgsfield CS 3.0, Kittl Image Board, Kittl Video Board, Midjourney v6, Flux Pro)
- **What style/aesthetic?** (reference art movements, brands, films, photographers)
- **Final use case?** (social media, print, campaign, product shot, apparel mockup)

If platform not specified, recommend based on Platform Selection Matrix:
| Need | Platform |
|---|---|
| Cinematic video (5-8s) | Higgsfield (Veo 3.1) |
| Photorealistic product | Flux Pro |
| Artistic/stylized | Midjourney v6 |
| Graphic design/mockups | Kittl Image Board |
| Design-to-video | Kittl Video Board |

### Step 2: Generate 3 Prompt Variants

**Variant A — Safe:** Proven approach, highest chance of quality output. Moderate stylize values, clear composition, standard lighting.

**Variant B — Creative:** Artistic push. Higher stylize, more interpretive lighting, bolder composition choices, stronger cultural references.

**Variant C — Wild Card:** Unexpected angle, high risk/high reward. Unusual camera choices, extreme lighting, cross-genre aesthetic mashups.

### Step 3: Apply Platform-Specific Formula

**Higgsfield Cinematic Video:**
```
[SUBJECT with specific details] + [ACTION with physics-aware motion] + [ENVIRONMENT with atmospheric details] + [CAMERA: shot type, movement, lens] + [LIGHTING: setup, quality, direction] + [MOOD/TONE] + [STYLE REFERENCE: specific film/director]
```
Use Logical Anchor System: Subject, Physics, Environment, Camera, Light anchors.

**Kittl Image Board:**
```
[SUBJECT] + [STYLE/AESTHETIC] + [COMPOSITION] + [COLOR PALETTE] + [TEXTURE/MATERIAL] + [TYPOGRAPHY INTEGRATION] + [BACKGROUND]
```
Define the Allowed (what to see) and the Locked (what must NOT change).

**Kittl Video Board:**
```
CAMERA: [movement and framing]
ACTION: [what happens in the scene]
AUDIO: [sound design direction]
TEXT: [any overlay text or titles]
```

**Midjourney v6:**
```
[SUBJECT], [ENVIRONMENT], [LIGHTING], [CAMERA/LENS], [STYLE], [MOOD], [QUALITY] --ar [RATIO] --v 6 --s [STYLIZE]
```
Include --no for negative prompts, --c for chaos, --w for weird if appropriate.

**Flux Pro:**
```
[DETAILED SUBJECT], [PRECISE ENVIRONMENT], [LIGHTING: direction + quality + color temp], [CAMERA: specific lens, aperture, ISO], [COLOR TEMPERATURE], [MOOD]
```
Be extremely specific: "Canon EOS R5, 85mm f/1.4, ISO 200" not "nice camera."

### Step 4: Add Pro Tips

For each variant, explain:
- What to adjust if the output isn't right
- Which parameter to tweak for different results
- Credit-saving tips (test with Popcorn/Kling before Veo 3.1)

## Output Format

```
## Prompts for: [Concept]
**Platform:** [Name] | **Mode:** [Type] | **Aspect:** [Ratio]

### Variant A: [Name] (Safe)
[Full prompt with all parameters]
> Pro Tip: [Adjustment guidance]

### Variant B: [Name] (Creative)
[Full prompt with all parameters]
> Pro Tip: [Adjustment guidance]

### Variant C: [Name] (Wild Card)
[Full prompt with all parameters]
> Pro Tip: [Adjustment guidance]

### Negative Prompt (if applicable)
[Elements to exclude]
```

## Universal Prompting Rules

1. Specificity > length. "85mm f/1.4" > "beautiful blurry background"
2. Front-load the subject. Most important element first.
3. Real-world references. "Shot on Arri Alexa" signals quality.
4. Describe light, not mood. "Warm golden backlight at 45°" > "beautiful lighting"
5. Never use vague descriptors: "beautiful," "nice," "cool," "amazing" = banned.
6. Think in layers: Subject > Environment > Light > Camera > Style > Mood
