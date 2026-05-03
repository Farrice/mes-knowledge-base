# Mood Board Construction

Build strategic mood boards using the 5-layer system. Produces a complete creative brief with color palettes, texture direction, typography systems, image direction, cultural references, and AI-generatable reference image prompts.

## Expert Loading

Load `skills/creative-direction/SKILL.md` at Tier 1. For brand-level or campaign mood boards, load `genius.md` Section 2 (Creative Direction) for art movements and brand identity frameworks.

## Workflow

### Step 0: Reference Capture (when references include video)

If the concept references video material ("the mood of this short film", "this commercial's vibe", "this music video's palette"), fetch frame-grounded visual context first — Layer 4 (Photography/Image Direction) and Layer 5 (Cultural References) become MUCH stronger when grounded in actual frames vs. verbal descriptions:

```bash
// turbo
python3 execution/fetch-video-context.py "<video-reference-url>" "ref-$(echo "$url" | shasum | head -c 8)" || true
```

See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md). Read `extractions/ref-*/visual-context.md` and 3-5 representative frames before constructing the 5 layers. The Reference Image Prompts in Step 4 can then directly pull composition, lighting, and color from the actual frames.

### Step 1: Clarify the Concept

What is this mood board for?
- Brand identity
- Campaign
- Collection/product line
- Video/content series
- Social content direction
- Apparel/streetwear line
- Event/space

### Step 2: Build the 5 Layers

**Layer 1: Color**
- 3-5 dominant colors with hex codes
- Emotional reasoning for each choice (reference color psychology)
- Color relationships (complementary, analogous, triadic, split-complementary)
- Reference: "This palette evokes [specific film, brand, movement]"

**Layer 2: Texture**
- 3-4 material/texture qualities
- Physical descriptors: matte, glossy, gritty, smooth, organic, synthetic, woven, metallic, weathered, polished
- How textures create the desired mood
- AI prompt keywords for each texture

**Layer 3: Typography**
- Primary font (display/headline) with specific weight
- Secondary font (body) with specific weight
- Optional accent font (mono, script, decorative)
- Hierarchy rules (sizes, weights, spacing, line height)
- Cultural reference for the pairing ("this pairing echoes [brand/movement]")

**Layer 4: Photography/Image Direction**
- Shot types and framing rules (reference visual language)
- Lighting direction (specific setup names: Rembrandt, split, chiaroscuro, golden hour)
- Color treatment/grade (reference cinematic grades)
- Composition rules (which to follow, which to break)
- Subject treatment (how people/products are photographed)
- 3-5 reference image descriptions (specific enough to generate with AI)

**Layer 5: Cultural References**
- 2-3 film references (specific SCENES, not just titles)
- 2-3 music references (artists/albums that match the energy)
- 2-3 fashion/brand references (specific collections or campaigns)
- 1-2 architecture/space references
- 1-2 art/photography references (specific works)

### Step 3: Synthesize

Write one paragraph that captures the ENTIRE mood board in words — the creative brief distillation. This paragraph should be vivid enough that someone could recreate the mood board from this description alone.

### Step 4: Generate Reference Image Prompts

3 AI prompts (Midjourney or Flux Pro) that would produce images matching this mood board. These serve as visual anchors for the entire creative direction.

## Output Format

```
## Mood Board: [Concept Name]

### Creative Brief
[One paragraph synthesis — vivid, specific, evocative]

### Layer 1: Color Palette
| Color | Hex | Role | Reasoning |
|---|---|---|---|
[Colors with emotional and cultural reasoning]

### Layer 2: Texture & Material
[Texture descriptions with physical qualities and AI keywords]

### Layer 3: Typography System
**Display:** [Font, weight, size range]
**Body:** [Font, weight, size range]
**Accent:** [Font, weight, context]
**Hierarchy:** [Rules]
**Reference:** [Cultural anchor for the pairing]

### Layer 4: Image Direction
**Shots:** [Types and framing]
**Lighting:** [Specific setups]
**Grade:** [Color treatment]
**Composition:** [Rules + intentional breaks]
**Subject Treatment:** [How to photograph]

### Layer 5: Cultural References
**Film:** [Specific scenes]
**Music:** [Artists/albums]
**Fashion:** [Brands/collections]
**Architecture:** [Spaces]
**Art:** [Specific works]

### Reference Image Prompts
1. [Full AI prompt — mood anchor]
2. [Full AI prompt — texture/detail]
3. [Full AI prompt — subject/lifestyle]
```
