# Higgsfield AI Platform Research Notes

## Platform Overview
- AI-first creative platform for video and image generation
- Positioned as a "creative control layer" sitting on top of multiple AI models
- Based in San Francisco

## Core Tools & Models Available
### Image Generation
- **Higgsfield Popcorn** — AI storyboard/keyframe generator (locks tone and composition)
- **Nano Banana Pro** — High-control image generation with spatial anchors, negative constraints, physics-based prompting
- **Nano Banana 2** — Updated image model
- **Soul 2.0 / Soul Cinema / Soul Cast** — Character-focused image generation
- **Soul ID Character** — Character consistency tools
- **Flux 2** — Image model
- **GPT Image 1.5** — OpenAI image model integration
- **Seedream** — Image editing/transformation (identity refinement, character changes)

### Video Generation
- **Google Veo 3.1** — Video generation from images (performance, dialogue, emotion)
- **Sora 2** — Video generation (continuous shots, action sequences)
- **Kling 3.0** — Video model
- **WAN 2.6** — Video model
- **Seedance / Seedance 2.0** — Motion/animation from images (micro-motion, dolly movements)
- **Recast** — Character replacement in video (swaps characters while preserving motion, lighting, atmosphere)

### Editing & Special Tools
- **Inpaint** — Image inpainting
- **Draw to Edit** — Sketch-based image editing
- **Draw to Video** — Sketch-based video generation
- **Edit Image** — General image editing
- **Image Upscale / Video Upscale / Sora 2 Upscale** — Resolution enhancement
- **Banana Placement / Product Placement** — Product placement in scenes
- **Multi Reference** — Multiple reference image control
- **Lipsync Studio** — Lip sync for video
- **Talking Avatar** — Avatar generation
- **UGC Factory** — User-generated content creation
- **Fashion Factory** — Fashion-specific generation
- **Photodump Studio** — Photo collection/editing
- **Cinema Studio 2.5** — Advanced cinematic control

### Other Features
- **Moodboard** — Visual mood board creation
- **Chat / Assist** — AI chat assistance
- **Copilot** — AI co-pilot for workflows
- **Reference Extension** — Browser extension for references
- **AI Influencer Studio** — Virtual influencer creation
- **Higgsfield Earn** — Monetization platform

## Cinematic Workflow Chain (from official guide)
1. **Higgsfield Popcorn** → Generate keyframe images (locks tone, composition)
2. **Seedream** → Refine identity, transform characters
3. **Seedance** → Add micro-motion, camera movements (dolly, orbit)
4. **Veo 3.1 or Sora 2** → Full video generation with performance, dialogue
5. **Recast** → Character replacement without breaking light/framing/atmosphere

## Prompt Structure Patterns (from official examples)

### Image Prompts (Popcorn) — Key Elements:
1. Shot type: "Cinematic close-up", "Wide cinematic shot", "Cinematic frontal close-up on wide angle lens"
2. Subject description: detailed character, clothing, expression
3. Camera position: "camera positioned through windshield", "slightly lower angle"
4. Lighting: "morning light softly filtering through lace curtains", "warm sunlight"
5. Atmosphere/mood: "quiet and introspective", "melancholic tone"
6. Technical specs: "Shot on 35mm film", "50mm lens", "shallow depth of field"
7. Color palette: "muted color tones", "yellow-green tones", "cream, faded green, soft yellow"
8. Film reference: "inspired by Roger Deakins cinematography", "Denis Villeneuve"

### Video Prompts (Veo 3.1/Sora 2) — Key Elements:
1. Camera movement: "slow dolly-in", "tracking rig low to ground", "slow cinematic orbit"
2. Temporal structure: "For the first two seconds... Suddenly..."
3. Character action: detailed physical movements, expressions
4. Dialogue (Veo 3.1): direct quotes in prompts
5. Atmosphere shift: describe how mood changes during the clip
6. Technical: "Handheld realism", "24mm wide lens", "high shutter speed"
7. Duration cues: implied through action description

### Seedance Prompts — Very Short:
- "Camera dolly in, woman looks at window."
- "Slow camera dolly in."

### Seedream Prompts — Transformation:
- "Make the old man look like a zombie, rotten flesh, white eyes."
- "Change the woman to an old man."
