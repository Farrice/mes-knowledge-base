---
description: Generate images using Nano Banana 2 (Gemini image generation)
---

# /generate-image — AI Image Generation

Generate images from text prompts using Google's Nano Banana 2 model (`gemini-3.1-flash-image-preview`).

## Usage

```
/generate-image [prompt]
/generate-image --aspect 16:9 [prompt]
/generate-image --edit path/to/image.png [prompt]
/generate-image --reference path/to/style.png [prompt]
```

## Examples

- `/generate-image "A futuristic logo for an AI company with anti-gravity themes"`
- `/generate-image --aspect 16:9 "LinkedIn banner about AI agents disrupting consulting"`
- `/generate-image --edit deliverables/images/logo.png "Make the background gradient darker"`
- `/generate-image --reference assets/hero.png "Another angle of this exact character, cinematic lighting"`

## Steps

### 1. Clarify the Prompt

If the user provides a vague prompt, sharpen it using **Nano Banana 2 Best Practices**:
- **Subject**: Describe scenes narratively, not keyword-based ("A warm amber-lit café" instead of "café, warm")
- **Style**: Use photographic/cinematic terminology (e.g., "35mm lens, golden hour glow, macro photography")
- **Text**: Provide exact text in quotes and specify desired font style and placement.
- **Format**: Square (social), 16:9 (banner), 9:16 (story)?
- **Consistency**: Is there a reference image? Use `--reference`.

### 2. Generate the Image

Run the generation script:

```bash
python /Users/farricecain/Google\ Antigravity/execution/generate_image.py --aspect [RATIO] "[PROMPT]"
```

For image editing (modifying an existing image):
```bash
python /Users/farricecain/Google\ Antigravity/execution/generate_image.py --edit [INPUT_PATH] "[EDIT_INSTRUCTIONS]"
```

For style transfer or character consistency (using prior image as reference):
```bash
python /Users/farricecain/Google\ Antigravity/execution/generate_image.py --reference [REF_PATH] "[PROMPT]"
```

### 3. Deliver

- Show the saved file path
- Offer iterations: "Want me to adjust the style, colors, or composition?"
- Suggest follow-ups:
  - `/generate-image --edit [path]` to refine
  - Different aspect ratios for other platforms

## Output Location

Images saved to: `deliverables/images/[timestamp]_[slug].png`

## Cost

Approximately $0.01-0.05 per generation (token-based pricing on `gemini-3.1-flash-image-preview`).

## Aspect Ratios

| Ratio | Use Case |
|-------|----------|
| 1:1 | Social media posts, profile images |
| 16:9 | LinkedIn/YouTube banners, presentations |
| 9:16 | Instagram/TikTok stories |
| 4:3 | Blog post images |
| 3:4 | Pinterest, portrait content |
