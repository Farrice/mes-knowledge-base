# Nano Banana Pro & Nano Banana 2 Prompting Research

## Models
- Nano Banana Pro = Gemini 3 Pro Image
- Nano Banana 2 = Gemini 3.1 Flash Image
- Built on Gemini 3 family, deep reasoning capabilities

## Tech Specs
- Context: NBP 65,536 input tokens; NB2 131,072 input tokens; both 32,768 output
- Resolutions: 1K, 2K, 4K (NB2 also 512px)
- Aspect ratios: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (NB2 adds 1:4, 4:1, 1:8, 8:1)
- Up to 14 reference images per prompt
- Real-time web search powered
- C2PA + SynthID watermarking

## 5 Prompting Frameworks

### 1. Image Generation
**Text-to-image formula:** [Subject] + [Action] + [Location/context] + [Composition] + [Style]
**Multimodal formula:** [Reference images] + [Relationship instruction] + [New scenario]

### 2. Image Editing
- Semantic masking (inpainting) via text
- Composition and style transfer with references
- Be explicit about what to keep the same

### 3. Real-time Information
**Formula:** [Source/Search request] + [Analytical task] + [Visual translation]

### 4. Text Rendering & Localization
- Use quotes for exact text
- Specify font name/style
- Text-first hack: generate text concepts first, then image
- Multilingual: 10+ languages

### 5. Prompting Like a Creative Director
**Lighting:** "three-point softbox setup", "Chiaroscuro lighting", "Golden hour backlighting"
**Camera/Lens:** GoPro (immersive), Fujifilm (color science), disposable camera (nostalgic); specify f-stop, lens type
**Color Grading:** "1980s color film, slightly grainy", "Cinematic color grading with muted teal tones"
**Materiality:** Specify textures — "navy blue tweed", "ornate elven plate armor, etched with silver leaf patterns"

## Best Practices
- Be specific: concrete details on subject, lighting, composition
- Use positive framing: describe what you want, not what you don't
- Control the camera: photographic/cinematic terms
- Iterate: refine with follow-up prompts conversationally
- Start with strong verb for primary operation
- Negative prompting: "no text except the title", "no logos"
