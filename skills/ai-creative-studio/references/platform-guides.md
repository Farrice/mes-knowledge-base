# AI Creative Studio: Platform-Specific Workflow Guides

Reference document for executing professional creative workflows across platform combinations. Load this file when Claude needs step-by-step platform-specific instructions for video, design, or animation projects.

---

## Table of Contents

1. [Lovart + NanoBanana Pro + Kling 2.6 Workflow](#lovart--nanobanana-pro--kling-26-workflow)
2. [Arcads + NanoBanana Pro + Veo 3.1 Workflow](#arcads--nanobanana-pro--veo-31-workflow)
3. [Higgsfield + NanoBanana Pro + Kling Workflow](#higgsfield--nanobanana-pro--kling-workflow)
4. [Artlist AI Toolkit + NanoBanana Pro + Kling 2.5 Workflow](#artlist-ai-toolkit--nanobanana-pro--kling-25-workflow)
5. [Midjourney v7 Workflow](#midjourney-v7-workflow)
6. [Flux Pro Workflow](#flux-pro-workflow)
7. [Ideogram 3 Workflow](#ideogram-3-workflow)

---

## Lovart + NanoBanana Pro + Kling 2.6 Workflow

**Purpose**: Create 3D Pop Poster Designs with border-break effects. Produces dynamic, eye-catching posters where subjects burst through frame boundaries with extreme depth and cinematic flair.

### Step-by-Step

#### 1. Generate Initial Composition in Lovart AI
- Navigate to lovart.ai
- Select the "3D Pop" or poster design template/style
- Enter a detailed prompt describing the subject in an extreme dynamic pose
- Key elements to include:
  - Subject bursting out of frame
  - Extreme foreshortening for powerful depth
  - Bold typography with strong hierarchy
  - Cinematic lighting (rim light, directional, dramatic shadows)
  - High-contrast color treatment
- Generate multiple variations (minimum 5)
- Select the strongest composition with clearest border-break action

#### 2. Refine with NanoBanana Pro
- Access via Google AI Studio → Image generation → NanoBanana Pro
- Take the best Lovart output
- Upscale to maximum resolution
- Refine photorealistic details:
  - Enhance skin texture and pore detail
  - Improve material quality (leather, fabric, metal reflections)
  - Strengthen lighting consistency and shadows
  - Ensure border-break elements are clean, sharp, and dramatic
  - Correct any AI artifacts at the edges
- Export the refined image at full quality

#### 3. Animate with Kling 2.6
- Upload the refined still as the first frame
- Prompt for subtle 3D parallax movement or camera push-in
- The depth effect activates with slight camera motion — subjects appear to truly extend into 3D space
- Settings:
  - Duration: 5 seconds
  - Quality: Professional
  - Motion style: Smooth camera push or parallax shift
- Export the final animation

### Prompt Templates for Lovart 3D Pop

**Base Template**:
```
A [SUBJECT] in a dramatic [ACTION POSE], breaking through the border of a [POSTER STYLE] poster.
[SUBJECT'S BODY PART] extends beyond the frame into 3D space.
Extreme foreshortening creating powerful depth.
Bold [FONT STYLE] typography reading "[TEXT]".
[LIGHTING DESCRIPTION].
Rich color palette of [COLORS].
Cinematic composition, high contrast, studio lighting.
```

### Example Prompts

**Fight Poster**:
```
A female boxer in mid-punch stance, her gloved fist breaking through the border of a neon-lit fight poster. Her arm extends into 3D space with extreme foreshortening. Bold retro typography reading "CHAMPION" in white and gold. Dramatic rim lighting with red and blue color gels. Deep shadows, high contrast, cinematic studio setup.
```

**Action Movie Poster**:
```
A superhero leaping forward, bursting through the poster border mid-jump. One leg kicks through the frame edge into 3D space. Extreme foreshortening on the extended limbs. Bold sans-serif typography reading "RECKONING" in metallic silver. Dramatic backlighting with atmospheric haze. Dark blue and orange color palette. Cinematic depth, professional poster composition.
```

**Sports Poster**:
```
A basketball player mid-dunk, the ball slamming through the poster border. Both arms extend beyond the frame boundary. Extreme foreshortening on the shoulders and arms. Bold athletic typography reading "UNSTOPPABLE" in white block letters. Dramatic spotlight lighting from above. Red, white, and black color scheme. High-energy cinematic composition.
```

---

## Arcads + NanoBanana Pro + Veo 3.1 Workflow

**Purpose**: Create photorealistic UGC-style video ads that appear as authentic user-generated content. Emphasize natural imperfections and casual authenticity while maintaining professional product presentation.

### Step-by-Step

#### 1. Generate Photorealistic Character/Spokesperson with NanoBanana Pro
- Create a photorealistic person fitting the target demographic
- Specify natural, casual setting:
  - Kitchen counter with everyday items visible
  - Home office or workspace
  - Outdoor café or park bench
  - Living room with soft furnishings
- Key imperatives:
  - Include subtle imperfections — slight facial asymmetry, natural skin texture variations
  - Natural hair with loose waves or casual styling
  - Authentic expression, not overly polished
  - Avoid words like "perfect," "flawless," "supermodel," "airbrushed" — these trigger visible AI appearance
  - Use casual, unlayered clothing
  - Ensure lighting is soft and diffused, never studio-flat
- Export at high resolution for use as spokesperson image

#### 2. Build Script and UGC Video in Arcads
- Navigate to arcads.ai
- Upload the character image as the main spokesperson
- Write script in natural, conversational language:
  - Use contractions ("I'm," "it's," "you'll")
  - Include natural pauses and filler words ("like," "you know," "basically")
  - Keep sentences short and punchy
  - Speak directly to the camera as if talking to a friend
- Select emotion/delivery style:
  - Excited but not over-the-top
  - Casual and approachable
  - Informative but conversational
- Generate the UGC-style video ad
- Review for natural movement and authentic delivery

#### 3. Enhance Extended Sequences with Veo 3.1
- For additional shots or longer video sequences
- Use identical character description for consistency
- Include UGC authenticity cues in prompts:
  - "Filmed on iPhone 15 Pro, natural indoor lighting"
  - "Casual over-the-shoulder angle, slight camera shake"
  - "Kitchen counter background with everyday clutter"
  - "Natural skin with subtle blemishes and freckles"
  - "Hair slightly messy, authentic bedroom hair"
  - "Soft ambient room lighting, not professional studio"
  - "Slight lens flare from window light"
  - "Casual clothing, not styled or matched"
- Export individual clips and compile in final edit

### UGC Authenticity Keyword Library

Use these phrases liberally in all UGC prompts to trigger realistic user-content appearance:

**Filming Style**:
- "Filmed on iPhone [model], natural lighting"
- "Handheld phone camera, slight jitter"
- "Casual selfie angle, slightly off-center framing"
- "Unedited, raw footage feel"
- "Quick phone video, no post-production"

**Lighting**:
- "Natural window light only"
- "Soft ambient room lighting"
- "Slight lens flare from backlit window"
- "No ring light or studio setup"
- "Soft, diffused daylight"

**Background**:
- "Kitchen counter with everyday items visible"
- "Bedroom background, lived-in"
- "Home office corner"
- "Coffee shop or café background"
- "Blurred home interior"

**Appearance**:
- "Natural skin with visible freckles and light blemishes"
- "Slightly messy or tousled hair"
- "No makeup or minimal makeup"
- "Casual t-shirt or hoodie"
- "Authentic, unpolished expression"

**Movement**:
- "Slight camera shake from handheld"
- "Natural hand gestures, not choreographed"
- "Genuine laugh or smile, not fake"
- "Casual body language, relaxed posture"

### Example UGC Prompt

```
A woman in her kitchen, wearing a casual gray hoodie, sitting on a kitchen stool. Soft natural window lighting from the left. She's showing a skincare product bottle to the camera, holding it at chest level. Natural skin with light freckles, tousled brunette hair. Kitchen counter background with a coffee mug and plant visible out of focus. Handheld phone camera, slight lateral camera shake. Genuine smile, casual and approachable. iPhone 15 Pro aesthetic, natural color grading, slight lens flare. Unedited feel, real user-generated content appearance.
```

---

## Higgsfield + NanoBanana Pro + Kling Workflow

**Purpose**: Create cinematic orbit shots and dramatic reveals with stationary subjects. Perfect for product showcases, architectural reveals, and beauty shots where the camera moves but the subject remains perfectly still.

### Step-by-Step: Cinematic Orbit Technique

#### 1. Generate Subject with Maximum Detail (NanoBanana Pro)
- Create the subject or product with maximum photorealistic detail
- Use dramatic, directional lighting (side-lighting or rim-lighting preferred)
- Include clean, contrasting background (dark or neutral)
- Ensure subject is well-lit from multiple angles:
  - Primary light creates form
  - Secondary light separates subject from background
  - Subtle fill light maintains detail in shadows
- Export at highest quality

#### 2. Apply Stone Statue Technique (Optional, for Locked Subject)
This step locks the subject in place during camera movement:
- Re-prompt the same subject as a "marble statue" or "bronze sculpture"
- Example: "A detailed marble sculpture of [exact subject description], mounted on a dark marble pedestal, dramatic museum gallery lighting with spotlights"
- This creates a rigidly posed version ideal for orbit generation
- Use this version as the source image for orbit creation

#### 3. Generate Orbit in Higgsfield
- Navigate to higgsfield.ai
- Upload the subject image
- Select orbit or rotation camera preset
- Configure:
  - Rotation angle: 180-360 degrees
  - Speed: Slow and smooth (avoid fast rotation)
  - Direction: Clockwise or counterclockwise (clockwise more natural for most subjects)
  - Axis: Vertical (around Y-axis, standard for orbits)
- Generate the orbit shot
- Export and review for smooth motion

#### 4. Enhance Control with Kling (Advanced Option)
- If Higgsfield result needs refinement or more specific camera control
- Upload the same starting image
- Prompt explicitly:
```
Cinematic 180-degree orbit around [SUBJECT]. Slow, smooth camera movement counterclockwise. Subject remains perfectly still and centered. Dramatic lighting shifts as camera rotates around the subject. Professional quality, 5-second duration. Smooth rotation, no jump cuts.
```
- Settings: Professional quality, 5-10 second duration
- Export final orbit

### First Frame / Last Frame Detailed Workflow

Use this advanced technique to create seamless multi-shot transitions or specific opening and closing compositions:

#### 1. Create Frame A (Opening Shot)
- Generate a detailed still image of the starting composition
- Example: "Close-up of a luxury analog watch on a black velvet surface, 45-degree angle, dramatic side-lighting from left, gold tones, shallow depth of field, premium product photography"
- Ensure excellent lighting and composition
- Export at high quality

#### 2. Create Frame B (Closing Shot)
- Generate the ending composition with the SAME subject
- Match subject positioning but change environment/context:
  - Example: "Wide shot of the same luxury analog watch worn on a wrist, urban street café background, golden hour sunset, walking motion implied, lifestyle photography"
- Maintain consistent lighting direction and color temperature
- Export at high quality

#### 3. Generate Seamless Transition with Kling
- Upload Frame A as the first frame (starting point)
- Upload Frame B as the last frame (ending point)
- Prompt for smooth narrative transition:
```
Smooth cinematic transition from intimate close-up product shot to lifestyle wrist wear shot. Camera pulls back, rotates, and shifts perspective. Seamless morphing between compositions. The subject [SUBJECT NAME] maintains consistent appearance throughout. Professional product-to-lifestyle transition. 5-second duration, fluid camera movement.
```
- Settings: Professional quality, 5 seconds
- Export final transition

---

## Artlist AI Toolkit + NanoBanana Pro + Kling 2.5 Workflow

**Purpose**: Create continuous cinematic multi-shot sequences that feel like a professional film production. Each shot flows naturally into the next through careful frame continuity and strategic refinement.

### Step-by-Step: Multi-Shot Sequence Production

#### 1. Create Hero Image and Plan Shot List
- Use Artlist Original Model 1.0 for the initial hero image
- Generate at commercial-quality resolution
- Example: "Extreme close-up of poker chips cascading on green felt, cinematic lighting, sharp focus, motion blur on falling chips, casino atmosphere"
- Before proceeding, establish the complete shot list:
  - Map out 4-6 distinct shots
  - Define camera movement for each shot
  - Identify key subjects/characters that appear in multiple shots
  - Note lighting consistency requirements
  - Plan scene progression and narrative flow

#### 2. Shot 1: Generate with Kling 2.5
- Upload the hero image as the first frame
- Write detailed prompt specifying:
  - Action happening in this shot
  - Camera movement (push-in, pull-back, pan, tilt)
  - Expected motion and energy level
  - Duration and timing
- Example: "Extreme close-up of poker chips cascading down onto green felt. Camera slowly pushes in on the falling chips. Bright casino lighting. Shallow depth of field. 5 seconds."
- Settings: Professional quality
- Export and save the LAST FRAME of the output

#### 3. Shot 2: Chain from Shot 1's Last Frame
- Take Shot 1's last frame as the source image
- Refine in NanoBanana Pro if needed:
  - Correct any compression artifacts
  - Enhance details that will appear in Shot 2
  - Ensure clean transition to next shot
- Upload the refined frame as Shot 2's first frame
- Write prompt for Shot 2's action and camera movement:
  - Example: "Medium shot of the dealer's hands moving across the felt, organizing chips. Camera pulls back slightly. Same casino lighting, green felt table. Professional dealing hands, manicured. 5 seconds."
- Export and save the last frame

#### 4. Continue Chain for All Shots
- Repeat the process for each subsequent shot
- Each shot's last frame becomes the next shot's first frame
- Maintain visual continuity through identical descriptions

### Frame Continuity Rules (CRITICAL)

**Apply these rules across all shots to maintain professional production quality**:

- **ALWAYS describe the subject with EXACT same details across shots**:
  - Same character name/description
  - Same clothing and appearance
  - Same accessories and styling
  - Same skin tone, hair color, distinguishing features

- **ALWAYS match lighting direction**:
  - Primary light always from same direction
  - Secondary light positions consistent
  - Shadow angles match across shots
  - Color temperature remains constant

- **ALWAYS specify consistent color palette/grade**:
  - Use identical color descriptors: "warm golden," "cool blue," "desaturated"
  - Maintain same saturation level across shots
  - Match contrast and brightness levels

- **ALWAYS use NanoBanana Pro between shots**:
  - Clean up artifacts from video compression
  - Enhance fine details before they appear in next shot
  - Ensure smooth visual transitions

### Multi-Shot Sequence Example: Casino Scene

**Pre-Production Planning**:
- Shot 1: Extreme close-up of chips cascading
- Shot 2: Dealer's hands organizing chips
- Shot 3: Medium shot of player's reaction
- Shot 4: Wide shot of full poker table
- Shot 5: Close-up of card reveal
- Shot 6: Celebration/reaction shot

**Subject Continuity Example**:
```
For every prompt in the sequence, include:
"Professional male dealer, 40s, Asian, short dark hair, wearing black casino vest and white dress shirt, gold wedding ring on left hand, confident expression, casino lighting reflecting on skin"
```

This exact description in every prompt ensures the dealer looks identical across all six shots.

---

## Midjourney v7 Workflow

**Purpose**: Generate high-aesthetic commercial imagery, luxury branding, and conceptual art. Delivers polished, magazine-quality visuals with strong stylistic coherence.

### Access & Setup
- Access via Discord (midjourney.com) or web interface
- Subscription required for standard usage
- Use `/imagine` command to generate images

### Key Parameters Reference
| Parameter | Range | Purpose |
|-----------|-------|---------|
| `--ar` (aspect ratio) | 1:1, 4:5, 16:9, etc. | Set image dimensions |
| `--s` (stylize) | 0-1000 | Control Midjourney aesthetic — 750 is "rich and opinionated" |
| `--c` (chaos) | 0-100 | Variance between variations — higher = more unexpected |
| `--v` | 6.1, 7 | Model version — use 7 for latest |
| `--sref` | URL | Reference image style |
| `--cref` | URL | Reference image colors |
| `--niji` | — | Anime/illustrated style |

### Prompting Strategy

**Key Principles**:
- **Be concise and evocative** — Midjourney responds better to shorter, punchy prompts than verbose descriptions
- **Comma-separated descriptors** work better than long sentences
- **Lead with primary elements** — Put the most important visual elements first
- **Avoid overly complex descriptions** — Let Midjourney interpret details
- **Use style references** — Leverage `--sref` for consistent aesthetic

### Example Prompts

**Luxury Product Shot**:
```
luxury perfume bottle, floating in dark water, golden light reflections, moody, cinematic, product photography --ar 4:5 --s 750 --v 7
```

**Architectural Interior**:
```
minimal interior design, concrete walls, single green plant, morning light through window, architectural photography, editorial --ar 16:9 --s 500 --v 7
```

**Conceptual Art**:
```
abstract flowing silk fabric, deep indigo and gold, volumetric lighting, cinematic, dramatic, professional photography --ar 1:1 --s 850 --v 7
```

**Fashion Campaign**:
```
editorial fashion photography, model in cream linen suit, urban rooftop, golden hour, natural posing, high-fashion, luxury magazine --ar 4:5 --s 700 --v 7
```

**Food Photography**:
```
gourmet chocolate cake, dramatic plating, shallow depth of field, warm candlelight, food styling, editorial magazine --ar 1:1 --s 600 --v 7
```

### Quality Enhancement Techniques

**For commercial/luxury output**:
```
[Main prompt], professional photography, editorial, magazine quality, perfect composition, studio lighting --s 750 --ar 4:5
```

**For conceptual/artistic output**:
```
[Main prompt], digital art, concept art, illustration, dramatic lighting, cinematic --s 850 --c 50
```

**For product/catalog work**:
```
[Main prompt], product photography, clean background, studio lighting, sharp focus, commercial photography --s 600 --ar 4:5
```

---

## Flux Pro Workflow

**Purpose**: Generate images with maximum prompt adherence and complex multi-element scenes. Excels at literal interpretation, complex compositions, and accurate text rendering.

### Access & Setup
- Access via Replicate, fal.ai, or local deployment
- Model options:
  - **Flux Pro**: Maximum quality, slowest
  - **Flux Dev**: Good quality, moderate speed (free tier available)
  - **Flux Schnell**: Fast inference, good quality
- API available for programmatic access

### Prompting Strategy

**Key Principles**:
- **Write very detailed, explicit prompts** — Flux values specificity
- **Specify EVERY element** you want in the scene — Nothing is assumed
- **Describe composition explicitly** — "In the foreground," "middle ground," "background"
- **Strong text rendering** — Flux accurately renders text in images
- **Technical precision works** — Lens descriptions, lighting angles, camera specs

### Example Prompts

**Complex Interior with Multiple Elements**:
```
A modern minimalist living room interior. Concrete feature wall on the left painted matte white. Dark wood flooring. A low-profile gray sectional sofa positioned in the center, facing a large window on the right wall. Floor-to-ceiling window with white frame, showing green plants outside. A sculptural wooden side table with three legs in natural oak. A single potted fiddle leaf fig plant next to the sofa. Warm ambient lighting from recessed ceiling lights. Afternoon golden light streaming through the window. Professional interior photography, sharp focus, architectural lighting, published in design magazine.
```

**Technical Product Setup**:
```
A precision engineer's workbench. Centered subject: sleek titanium camera lens, 35mm focal length. Lens mounted on a white stand. Surrounding workspace: technical documentation, precision caliper on the left, soft focus workshop tools in background. Overhead studio lighting with soft key light and subtle fill. Shallow depth of field with sharp focus on the lens glass. Professional product photography, commercial lighting, technical documentation style.
```

**Complex Scene with Multiple Characters**:
```
A bustling café interior. Foreground: a barista in a navy apron steaming milk, creating latte art, focused expression. Middle ground: customer in the center sitting at a wooden table with a coffee cup and open laptop, warm natural light on face. Background: blurred pastry display case, other customers, warm café ambient lighting. Large windows with soft daylight on the left. Warm color temperature, cozy café atmosphere, professional lifestyle photography, natural composition, shallow depth of field.
```

### Quality Settings

**For commercial/professional output**:
- Use Flux Pro model
- Include "professional photography, sharp focus, perfect composition" in prompt
- Specify exact lighting setup

**For architectural/technical**:
- Use Flux Pro
- Include precise measurements and technical terms
- Specify camera lens and angle

**For fast iteration** (concept work):
- Use Flux Schnell
- Maintain detailed prompting
- Accept slightly lower resolution

---

## Ideogram 3 Workflow

**Purpose**: Create typography-heavy designs, logos, posters, and text-centric graphics. Best-in-class for accurate, readable text rendering within images.

### Access & Setup
- Access via ideogram.ai
- Subscription required for commercial usage
- Native text rendering capability

### Prompting Strategy

**Key Principles**:
- **Put desired text in quotation marks** within the prompt
- **Specify font style explicitly**: "bold sans-serif," "elegant serif," "handwritten script," "geometric modern," "retro blocked"
- **Describe text placement precisely**: "centered at top," "arching over subject," "bottom right corner," "diagonal across image"
- **Include typography hierarchy** if multiple text elements
- **Use text as design element** — Describe color, shadow, outline, effects
- **Best-in-class text accuracy** — Ideogram rarely misspells or distorts text

### Example Prompts

**Motivational Poster**:
```
A motivational poster design with large bold text reading "BELIEVE" in clean sans-serif white font, centered, slightly spaced letters. Background of a dramatic mountain sunrise, warm golden colors, soft clouds. Minimalist design, premium feel, modern aesthetic. Simple composition, high impact.
```

**Luxury Product Label**:
```
A premium product label design. Elegant serif text reading "ESSENCE" in gold, centered at the top. Underneath, script text reading "Luxury Fragrance" in smaller serif font. Background features a soft botanical illustration of jasmine flowers in muted colors. Minimalist layout, luxury brand aesthetic, premium packaging design.
```

**Bold Brand Logo**:
```
A modern brand logo. Geometric sans-serif text reading "NOVA" in bold black, centered. Letters are clean and angular with slight perspective. Above the text, an abstract geometric symbol combining a circle and upward arrow. Monochrome design, versatile for multiple uses, professional logo design, scalable design.
```

**Concert Poster**:
```
A concert event poster. Large bold text reading "ELECTRIC NIGHTS" in white heavy sans-serif font, all caps, centered at top. Beneath, text reading "June 15th" in smaller font. Background is a vibrant abstract composition with electric blues, purples, and neon pink colors, dynamic energy, concert atmosphere. Text has a subtle glow effect. Modern poster design, high visual impact.
```

**Sports Team Design**:
```
A sports team graphic. Bold block text reading "THUNDERS" in white with black outline, centered, strong athletic font. Above the text, a stylized lightning bolt symbol integrated into the design. Background gradient from dark blue to purple. Professional sports branding, team apparel design, vector style illustration.
```

### Text Rendering Best Practices

**For maximum text accuracy**:
- Keep text short (1-3 words per text element)
- Use common, straightforward fonts
- Avoid overly stylized fonts if legibility is critical
- Specify letter spacing: "tight spacing" or "loose spacing"
- Include text color in description: "white text" or "gold lettering"

**For complex text** (longer phrases, multiple lines):
- Break into multiple lines in the prompt description
- Specify line breaks: "BELIEVE on line one, ACHIEVE on line two"
- Use Ideogram's text-specific parameters if available

**Typography Style Reference**:
- Bold sans-serif: Clean, modern, athletic
- Elegant serif: Luxury, heritage, traditional
- Handwritten script: Personal, creative, feminine
- Geometric modern: Tech, minimal, contemporary
- Retro blocked: Vintage, bold, nostalgic
- Outline/stroke: Impact, visibility, design element

---

## Cross-Platform Quality Checklist

When executing any workflow above, verify completion with this checklist:

- [ ] **Final output matches brief requirements** (purpose, dimensions, style)
- [ ] **Quality is production-ready** (sharp, well-lit, professional)
- [ ] **All text is accurate and readable** (if applicable)
- [ ] **Color consistency** across multi-shot sequences or platform chains
- [ ] **Subject/character continuity** (appearance, lighting, positioning)
- [ ] **Motion is smooth** (if video or animation output)
- [ ] **File format and resolution** appropriate for intended use
- [ ] **No visible AI artifacts** (distorted faces, impossible geometry, warped text)

---

## Platform Selection Quick Reference

| Workflow Goal | Recommended Platforms | Output Type |
|---------------|----------------------|------------|
| 3D Pop Posters | Lovart + NanoBanana Pro + Kling 2.6 | Video/Animation |
| UGC Video Ads | Arcads + NanoBanana Pro + Veo 3.1 | Video |
| Orbit Shots | Higgsfield + NanoBanana Pro + Kling | Video |
| Multi-Shot Film | Artlist + NanoBanana Pro + Kling 2.5 | Video Sequence |
| Luxury Branding | Midjourney v7 | Static Image |
| Complex Scenes | Flux Pro | Static Image |
| Typography/Text | Ideogram 3 | Static Image |

---

**Document Version**: 1.0
**Last Updated**: February 2026
**Source Studies**: Lovart Professional Guides, Arcads Documentation, Higgsfield Workflows, Artlist AI Toolkit, Midjourney Official Reference, Flux Documentation, Ideogram 3 Specification
