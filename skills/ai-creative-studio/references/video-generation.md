# AI Video Generation: Professional Reference

## Table of Contents

1. [Five-Part Video Prompt Structure](#five-part-video-prompt-structure)
2. [Camera Movement Vocabulary](#camera-movement-vocabulary)
3. [Signature Techniques](#signature-techniques)
   - [First Frame / Last Frame Method](#first-frame--last-frame-method)
   - [Stone Statue Trick (Subject Freezing)](#stone-statue-trick-subject-freezing)
   - [3D Border-Break / Cutout Poster Effect](#3d-border-break--cutout-poster-effect)
   - [UGC Imperfection Prompting](#ugc-imperfection-prompting)
   - [Continuous Multi-Shot Sequences](#continuous-multi-shot-sequences)
   - [Speed Ramping](#speed-ramping)
4. [Platform-Specific Video Guides](#platform-specific-video-guides)
5. [Video Post-Production Workflow](#video-post-production-workflow)
6. [Failure Modes & Corrections](#failure-modes--corrections)
7. [Aspect Ratios by Platform](#aspect-ratios-by-platform)

---

## Five-Part Video Prompt Structure

Master professional AI video by understanding the five essential components. Each part builds on the previous to create a complete visual specification.

**Complete Structure:**
```
[Subject/Action] + [Camera Movement] + [Environment/Setting] + [Lighting/Mood] + [Technical Specs]
```

### Part 1: Subject & Action
Define what is happening and who/what is doing it.

**Purpose**: Establish the primary focus and narrative motion.

**Guidelines**:
- Be specific about character/product appearance
- Describe the primary motion or transformation
- Use consistent descriptors across multiple prompts

**Examples**:
- "A sleek chrome product spinning on a white pedestal"
- "A woman confidently walking through a modern office lobby"
- "A golden liquid pouring into a crystal glass with splash dynamics"
- "A spaceship gradually rotating to reveal detailed hull plating"

### Part 2: Camera Movement
Specify how the camera moves relative to the subject. This is the most powerful control lever.

**Purpose**: Create cinematic depth and visual interest.

**Guidelines**:
- Use single camera movement per prompt (multiple movements = unpredictable results)
- Pair with descriptive speed words: "slow", "smooth", "gentle", "sweeping", "dynamic"
- Avoid contradictory movements ("pan left while rotating right")

**Examples**:
- "Slow dolly in on the subject's face"
- "Smooth 360-degree orbit around the product"
- "Gentle crane up from tabletop to full-body reveal"
- "Steady tilt up from feet to face"

### Part 3: Environment & Setting
Paint the world the subject inhabits.

**Purpose**: Establish spatial context and visual depth.

**Guidelines**:
- Describe backgrounds explicitly
- Include spatial scale indicators ("intimate room" vs "vast warehouse")
- Specify depth layers (foreground, midground, background elements)
- Note texture and material properties

**Examples**:
- "In a minimalist studio with white walls and soft shadow gradient"
- "Against a futuristic cityscape with neon signs reflecting in rain-wet streets"
- "In a sunlit garden with out-of-focus green foliage in the background"
- "Inside a luxury penthouse with floor-to-ceiling windows overlooking the ocean"

### Part 4: Lighting & Mood
Define the emotional temperature and visual quality of light.

**Purpose**: Create atmosphere and guide viewer emotion.

**Guidelines**:
- Specify light direction (from above, side-lit, backlit, rimlit)
- Include color temperature ("warm golden", "cool blue", "harsh white")
- Note shadow quality (soft, dramatic, high-contrast)
- Pair with mood descriptors

**Examples**:
- "Dramatic side-lighting with deep shadows, moody and cinematic"
- "Warm golden hour sunlight with soft lens flare, intimate and nostalgic"
- "Cool blue-tinted lighting with high contrast, futuristic and sleek"
- "Soft diffused light from large windows, clean and professional"

### Part 5: Technical Specifications
Specify format, duration, and style parameters.

**Purpose**: Ensure output matches platform and brand requirements.

**Guidelines**:
- Specify duration in seconds (5s, 10s, 15s)
- Include quality level (standard, professional)
- Note aspect ratio or platform target
- Specify frame rate if critical (24fps cinematic, 60fps smooth motion)

**Examples**:
- "10 seconds, professional quality, 16:9 aspect ratio"
- "5 seconds, cinematic look, 2.39:1 widescreen"
- "Smooth 60fps motion for social media, 1080×1920 vertical"
- "Professional quality with slight film grain for authenticity"

### Complete Prompt Examples

**Example 1: Product Video**
```
A luxury watch catching light as it rotates on a black marble surface.
Slow 180-degree orbit camera movement revealing the watch face and intricate casework.
Modern minimalist setting with subtle shadows and depth of field.
Warm spotlight illumination from above, creating dramatic reflections on the metal.
10 seconds, professional quality, 16:9 ratio.
```

**Example 2: Character Commercial**
```
A confident professional woman opening her laptop with purpose.
Smooth dolly in combined with gentle tilt up from the laptop screen to her face.
Modern office with floor-to-ceiling windows and soft natural light in the background.
Golden hour sunlight streaming in from the side, warm and aspirational mood.
5 seconds, professional quality, vertical 9:16 format for mobile.
```

**Example 3: Brand Cinematic**
```
A glass coffee cup with steam rising, placed on a wooden table.
Slow push in combined with subtle upward crane movement.
Cozy coffee shop interior with blurred warm interior lighting, out-of-focus bokeh background.
Soft diffused natural light from a window, creating a hazy atmospheric glow.
8 seconds, cinematic 2.39:1 aspect ratio, professional quality.
```

---

## Camera Movement Vocabulary

Use these terms precisely in your prompts. Each creates distinct visual storytelling.

### **Dolly**
The camera physically moves forward or backward on a fixed track, moving closer to or farther from the subject.

- **Use for**: Emphasis and emotional intensity
- **Speed descriptors**: "slow dolly in", "gentle dolly back", "moderate dolly forward"
- **Prompt example**: "Slow dolly in on the subject's face, revealing growing emotion"
- **Best on**: Kling AI, Runway Gen-4

### **Pan**
The camera rotates left or right on a fixed pivot point, as if turning your head horizontally.

- **Use for**: Revealing new elements, following action horizontally
- **Speed descriptors**: "smooth pan", "sweeping pan", "subtle pan"
- **Prompt example**: "Smooth pan left revealing the cityscape beyond the window"
- **Best on**: Kling AI, Veo 3.1

### **Tilt**
The camera rotates up or down on a fixed pivot point, as if nodding your head vertically.

- **Use for**: Vertical reveals, establishing scale
- **Speed descriptors**: "slow tilt up", "gentle tilt down", "dramatic tilt"
- **Prompt example**: "Slow tilt up from the subject's feet to their face"
- **Best on**: Kling AI, Runway Gen-3

### **Truck**
The camera moves laterally left or right while maintaining forward-facing direction, sliding sideways across the scene.

- **Use for**: Following characters, showing spatial relationships
- **Speed descriptors**: "smooth truck right", "slow truck left", "tracking truck"
- **Prompt example**: "Truck right following the subject walking, revealing the storefront behind them"
- **Best on**: Kling AI, Sora 2

### **Pedestal**
The camera moves straight up or down vertically while remaining at the same forward position, like an elevator movement.

- **Use for**: Vertical scale reveals, building to overhead views
- **Speed descriptors**: "gentle pedestal up", "slow pedestal down"
- **Prompt example**: "Pedestal up revealing the full building height"
- **Best on**: Kling AI, Runway Gen-4

### **Orbit / Arc**
The camera circles around the subject maintaining constant distance, creating a 360-degree or partial circular path.

- **Use for**: Product showcases, dramatic reveals, hero moments
- **Speed descriptors**: "360-degree orbit", "180-degree arc", "slow orbit around"
- **Prompt example**: "360-degree orbit around the product with the subject remaining centered"
- **Best on**: Kling AI 2.6+, Higgsfield (optimized for this)

### **Crane / Boom**
The camera rises or descends dramatically, as if mounted on a crane arm, revealing scale and context.

- **Use for**: Epic reveals, establishing shots, transitions between scales
- **Speed descriptors**: "crane up from", "boom down revealing", "sweeping crane"
- **Prompt example**: "Crane up from ground level to aerial perspective revealing the landscape"
- **Best on**: Kling AI, Runway Gen-4

### **Steadicam / Gimbal**
The camera moves smoothly through space with natural floating motion, eliminating jitter and wobble.

- **Use for**: Immersive navigation, following through environments
- **Speed descriptors**: "steadicam follow", "smooth gimbal movement", "floating camera"
- **Prompt example**: "Steadicam follow through the hallway maintaining smooth lateral motion"
- **Best on**: Runway Gen-3/Gen-4, Veo 3.1

### **Handheld**
The camera moves with subtle natural shake and imperfection, mimicking human handheld filmmaking.

- **Use for**: Documentary feel, UGC content, intimate moments
- **Speed descriptors**: "handheld documentary style", "subtle handheld shake"
- **Prompt example**: "Handheld camera movement with subtle natural shake, documentary aesthetic"
- **Best on**: Veo 3.1, Sora 2

### **Zoom**
The lens magnifies (zoom in) or diminishes (zoom out) the subject while camera position remains fixed.

- **Use for**: Focus shifts, dramatic emphasis, isolation of details
- **Speed descriptors**: "slow zoom into", "gradual zoom out from", "quick zoom in"
- **Prompt example**: "Slow zoom into the subject's eyes creating intimate focus"
- **Best on**: Kling AI, Runway Gen-3

### **Rack Focus**
The focus shifts from one plane of depth to another, keeping one element sharp while blurring another.

- **Use for**: Drawing attention sequentially, reveal through focus
- **Speed descriptors**: "smooth rack focus", "slow focus shift"
- **Prompt example**: "Rack focus from foreground flower to background figure, both in frame"
- **Best on**: Runway Gen-4, Kling AI 3.0

### **Dutch Tilt**
The entire frame tilts at an angle rather than remaining level, creating visual tension and energy.

- **Use for**: Building tension, stylized moments, dynamic shots
- **Speed descriptors**: "Dutch angle increasing", "tilted composition"
- **Prompt example**: "Dutch tilt angle increasing tension during the reveal"
- **Best on**: Kling AI, Runway Gen-3

### **Aerial / Drone**
The camera position rises to overhead perspective, typically 50+ feet above ground, capturing expansive views.

- **Use for**: Establishing shots, landscape reveals, scale context
- **Speed descriptors**: "drone pullback", "aerial approach", "overhead reveal"
- **Prompt example**: "Drone pullback revealing the landscape from 100 feet altitude"
- **Best on**: Sora 2, Runway Gen-4

### **Push In / Pull Back**
Combined dolly and zoom creating simultaneous forward/backward movement of both camera position and lens focal length.

- **Use for**: Dynamic emphasis, maintaining size while changing perspective
- **Speed descriptors**: "smooth push in", "gentle pull back"
- **Prompt example**: "Smooth push in combined with zoom maintaining subject size while changing background perspective"
- **Best on**: Kling AI 2.6+, Runway Gen-4

---

## Signature Techniques

These proven workflows deliver professional results and overcome common AI video limitations.

### First Frame / Last Frame Method

The most powerful technique for achieving precise control over video generation and subject transformation.

**How It Works**:
1. Generate a still image as the FIRST FRAME (the exact opening composition you want)
2. Generate a separate still image as the LAST FRAME (the exact ending composition you want)
3. Feed both images to the video model with a transition prompt
4. The model interpolates smooth motion between your two fixed bookends
5. Result: Predictable, controlled motion with guaranteed start and end states

**When to Use**:
- Character transformations or emotional progressions
- Product reveals (closed → open, off → on, hidden → visible)
- Scene transitions with precise compositional control
- Subject state changes (still → moving, or vice versa)

**Supported By**: Kling AI 2.5+, Runway Gen-3/Gen-4

**Prompt Format**:
```
First frame: [Detailed description of opening state]
Last frame: [Detailed description of ending state]
Smooth cinematic transition between these two states.
[Camera movement if desired]
```

**Example 1: Product Transformation**
```
First frame: Luxury product box closed on white surface, pristine and sealed.
Last frame: Same box opened at 45 degrees revealing the product inside glowing softly.
Smooth transition with camera tilting up to follow the opening lid.
Professional quality, 10 seconds, bright studio lighting.
```

**Example 2: Emotional Character Arc**
```
First frame: Person looking down with uncertain expression, hands folded on desk.
Last frame: Same person looking directly at camera with confident smile, hands open and relaxed.
Smooth transition capturing the internal transformation.
Slow dolly in combined with the emotional shift.
Professional quality, 8 seconds, warm office lighting.
```

**Example 3: Environmental Transition**
```
First frame: Empty white gallery space with single spotlight, no subject present.
Last frame: Same gallery space now with illuminated art installation centered, dramatic backlighting.
Smooth transition revealing the transformed space.
Camera crane up to reveal full scale.
Professional quality, 12 seconds, gallery ambient lighting.
```

**Pro Tips**:
- Ensure both frames have identical camera position and framing
- Describe lighting consistently between frames
- Keep background elements stable unless transition is about environment change
- Use this to avoid morphing/distortion during motion

---

### Stone Statue Trick (Subject Freezing)

Lock the subject perfectly still while the camera moves dynamically around it.

**How It Works**:
1. Describe the subject as if it were a marble or stone statue
2. Add texture descriptors: "polished marble", "carved stone", "statue material"
3. Prompt the video model to move the camera around the statue
4. The model's training associates stone/statue texture with "immobile subject"
5. Result: Subject remains perfectly frozen while camera orbits, tilts, or dolly's

**When to Use**:
- Product showcases (hero shots, premium positioning)
- Character hero moments (dramatic power poses)
- Dramatic character reveals (pose locked, camera reveals them)
- Any moment requiring subject stability

**Prompt Example**:
```
A marble statue of [subject description] positioned on a polished pedestal.
Cinematic 180-degree orbit shot around the statue.
Dramatic professional lighting with deep shadows emphasizing form.
The statue remains perfectly still as camera smoothly circles around it.
Professional quality, 10 seconds, dramatic gallery lighting.
```

**Example 1: Product Hero Shot**
```
A gleaming bronze statue of the luxury smartphone, positioned at center on a black marble base.
Smooth 360-degree orbit camera movement, maintaining tight focus on the form.
Professional museum-quality lighting with dramatic side-light and rim-light.
The statue is completely motionless as the camera gracefully circles it.
10 seconds, professional quality, cinematic grade color.
```

**Example 2: Character Power Pose**
```
A carved stone statue of the warrior in a powerful battle stance, sword raised.
Slow 270-degree arc camera movement revealing the figure from multiple angles.
Dramatic backlighting with volumetric mist, heroic and cinematic mood.
The figure remains perfectly still in their power pose as camera orbits.
8 seconds, professional quality, epic fantasy lighting.
```

**Pro Tips**:
- Combine with dramatic lighting for maximum impact
- Use orbit shots (most predictable motion around statues)
- Avoid rapid camera movements; keep them slow and steady
- Works especially well on Kling AI's orbit functionality

---

### 3D Border-Break / Cutout Poster Effect

Create subjects bursting out of frames and posters with dramatic 3D depth.

**How It Works**:
1. Use an image generation tool (Lovart AI recommended) to create a 3D pop poster design
2. Design features extreme foreshortening and perspective distortion
3. Extend subject elements beyond the frame border (hand extending out, weapon breaking through)
4. Add bold typography and compositional imbalance
5. Animate with Kling 2.6 for dynamic depth effect

**When to Use**:
- Movie/trailer style announcements
- Product launches with dramatic emphasis
- Character introductions
- Social media hero content

**Prompt Structure for Image Generation**:
```
[Subject] in dynamic aggressive/celebratory pose, breaking through the frame of a movie poster.
Extreme foreshortening making the [closest element: hand/foot/weapon] appear to extend directly toward viewer.
[Subject's extended part] overlaps the poster border and extends into 3D space beyond the frame edge.
Bold cinematic typography and design elements framing the composition.
Dramatic side-lighting and deep shadows emphasizing the 3D depth effect.
Professional movie poster aesthetic with maximum visual impact.
```

**Example 1: Action Character**
```
A superhero in dynamic flying pose, bursting through the frame of an action movie poster.
Extreme foreshortening on the outstretched fist extending directly toward camera.
The character's hand breaks through the poster border into 3D space.
Bold red and gold typography: "COMING SOON" arcing around the composition.
Dramatic orange and purple backlighting, intense and powerful mood.
Professional blockbuster poster style.
```

**Video Animation Prompt** (after creating the poster image):
```
[First frame: the poster image itself]
Animate the poster with subtle dynamic energy.
The character appears to be actively pushing against the poster border.
Camera slowly approaches the character's extended hand.
Dramatic lighting intensifies as camera gets closer.
5 seconds, professional quality, maintaining poster aesthetic.
```

**Pro Tips**:
- Design the image with maximum perspective distortion
- Make extended elements clearly overlap the frame edge
- Use the video animation to add subtle pressure/motion suggesting 3D breaking
- Pair with sound design of breaking glass or impact for full effect

---

### UGC Imperfection Prompting

Generate AI video that authentically reads as user-generated content, not slick commercial production.

**Purpose**: Create content that feels relatable and passes viewer scrutiny as "real" UGC.

**Elements to Add**:
- **Optical imperfections**: "slight lens flare", "natural chromatic aberration", "subtle lens dust particles"
- **Human imperfections**: "natural blink rate", "subtle hand tremor", "micro-expressions and natural pauses"
- **Framing imperfections**: "slightly off-center composition", "occasional slight tilt in framing", "edge of finger visible"
- **Lighting authenticity**: "everyday indoor lighting", "natural ambient lighting variation", "shadows under eyes"
- **Audio feel**: "natural ambient sound feel", "subtle background noise", "realistic breath patterns"

**Elements to AVOID** (these signal "AI generated"):
- "perfect", "flawless", "studio quality"
- "perfectly centered", "precise composition"
- "ideal lighting", "perfectly balanced"
- "pristine", "immaculate"
- "professional color grade", "color-corrected"

**Prompt Example**:
```
[Subject] speaking directly to camera in casual home setting.
Natural handheld camera movement with subtle shake, everyday framing.
Bedroom or home office background with natural window light, slight underexposed areas.
Casual off-center composition with occasional subtle tilt.
Genuine micro-expressions and natural pauses in speech.
Slight lens artifacts and natural ambient lighting variation.
5 seconds, natural authentic feel, handheld documentary style.
```

**Example 1: Testimonial**
```
A satisfied customer speaking directly to camera about their experience.
Handheld framing with subtle natural shake and occasional slight tilt.
Home office background with everyday natural lighting, slight shadows.
Genuine expression with natural pauses and micro-expressions.
Off-center composition with laptop visible at edge of frame.
Natural ambient lighting variation and subtle eye reflection.
10 seconds, authentic unscripted feel, natural color (not color-graded).
```

**Example 2: Product Demo**
```
Hand holding product and demonstrating feature casually.
Handheld camera with natural movement, slight shake in framing.
Kitchen or home table background with warm natural indoor light.
Occasional fingers visible at frame edge, realistic hand positioning.
Natural speaking pace with genuine discovery and reaction.
Subtle shadow variation and natural ambient light quality.
8 seconds, authentic user-generated demo, unpolished aesthetic.
```

**From**: Arcads + Veo 3.1 workflow (highest authenticity results)

**Pro Tips**:
- Keep motion subtle; avoid dance-like camera movements
- Limit dialogue speed to conversational pace
- Include realistic pauses between thoughts
- Avoid symmetric framing; offset slightly
- Let real ambient light determine darkness/brightness

---

### Continuous Multi-Shot Sequences

Maintain visual consistency across multiple video clips to create seamless narrative sequences.

**How It Works**:
1. Generate the hero frame/image with maximum detail and clarity
2. Use that exact same image as the STARTING FRAME for Shot 1
3. After Shot 1 completes, export or capture the LAST FRAME
4. Use Shot 1's last frame as the STARTING FRAME for Shot 2
5. Continue the frame continuity chain for all subsequent shots
6. Describe character/product identically across every single prompt

**When to Use**:
- Narrative sequences requiring multiple angles
- Product walkthroughs across different environments
- Character story arcs spanning multiple scenes
- Commercial sequences that need visual continuity

**Critical Consistency Rules**:
- Describe character clothing, appearance, and positioning identically
- Maintain identical lighting direction and color temperature
- Keep background elements stable unless intentional transition
- Use the EXACT same character descriptors word-for-word in each prompt
- Verify framing continuity between shots before proceeding

**Workflow Example: Three-Shot Sequence**

**Shot 1 - Opening**:
```
[First frame: Hero image of character in starting position]
Camera slow dolly in from wide to close-up framing.
Modern office setting with warm window light from the left.
Character: [Exact description including outfit, hair, expression]
Professional quality, 5 seconds, 16:9 aspect ratio.
[Use exact hero image as the "First frame"]
```

**Shot 2 - Transition**:
```
[First frame: The last frame exported from Shot 1]
Character: [IDENTICAL description as Shot 1]
Slow truck right revealing the office beyond character.
Same warm left-side window lighting, consistent with previous shot.
Professional quality, 5 seconds, maintain scene continuity.
[Export the last frame when complete]
```

**Shot 3 - Conclusion**:
```
[First frame: The last frame exported from Shot 2]
Character: [IDENTICAL description as Shots 1 and 2]
Camera gentle tilt up revealing full window view and cityscape.
Consistent warm golden light throughout frame.
Professional quality, 5 seconds, concluding scene.
```

**Example: Product Walkthrough**

**Shot 1 - Hero Introduction**:
```
First frame: Luxury product centered on white surface, pristine presentation.
Slow dolly in combined with gentle tilt up.
Professional studio setting with soft directional lighting from upper left.
Product: [Specific color, material, and design details - EXACT description]
Professional quality, 8 seconds.
```

**Shot 2 - Feature Detail**:
```
First frame: [Last frame from Shot 1]
Close-up of product feature in detail, side-lit to emphasize texture.
Product: [IDENTICAL description as Shot 1, showing same specific details]
Smooth 180-degree orbit revealing the feature from multiple angles.
Consistent studio lighting, same color temperature and direction.
Professional quality, 6 seconds.
```

**Shot 3 - Lifestyle Context**:
```
First frame: [Last frame from Shot 2]
Product integrated into lifestyle scenario, hand holding product with precision.
Product: [IDENTICAL description, same color and design elements]
Slow pull back revealing the lifestyle context and environment.
Warm ambient lighting consistent with previous shots.
Professional quality, 7 seconds.
```

**From**: Artlist AI Toolkit workflow (proven casino/poker chip example)

**Pro Tips**:
- Create a "Character Brief" document with exact descriptors to copy-paste
- Always export/screenshot the last frame before proceeding to next shot
- Test the transition between shots before committing to full sequence
- Backup hero image; use it as reference for all shots
- Watch clips back-to-back to verify continuity

---

### Speed Ramping

Create dynamic pacing and emphasize key moments through variable playback speed.

**How It Works**:
1. Generate video at standard playback speed
2. In post-production, apply speed curve: slow → normal → fast → slow
3. Strategically place moments of maximum speed at crucial turning points
4. Synchronize speed changes with music beats and emotional peaks
5. Use slow sections for emotional beats, fast for energy/impact

**When to Use**:
- Product reveals (slow build, fast reveal, slow landing)
- Action sequences (slow impact moment, fast recovery)
- Emotional climaxes (slow into moment, speed up action, slow resolution)
- Music-driven content (sync speed with beat drops and buildups)

**Prompt Specifications**:
```
Generate at standard speed (specify: 5-10 seconds normal playback)
[Specify the moment that will be ramped]
Professional quality ready for post-production speed ramping.
```

**Example 1: Product Reveal**
```
Luxury product box positioned unopened.
Slow dolly in with anticipation.
Box lid begins to open, revealing product inside.
Professional quality, 10 seconds standard playback.
[In post: Ramp slow (0-3s) → normal (3-5s) → fast (5-7s for reveal) → slow (7-10s for landing)]
```

**Example 2: Action Climax**
```
Character approaching the moment of impact or revelation.
Build tension with steady camera movement.
Action sequence or impact moment occurring.
Recovery and aftermath following the climax.
Professional quality, 8 seconds standard playback.
[In post: Ramp slow build (0-2s) → normal (2-5s) → fast (5-6s impact) → slow (6-8s resolution)]
```

**Music Synchronization**:
```
Generate video timed to [specific song/beat reference]
Build speed through the pre-chorus
Fast pacing during the chorus drop
Slow motion on the emotional chorus moment
Professional quality, 15 seconds.
```

**Pro Tips**:
- Speed ramp should feel organic, not jarring
- Maximum speed ramp: 2x-3x (beyond this looks unnatural)
- Pair with sound design; fast visuals with punchy sound, slow with atmospheric audio
- Test ramps on mobile viewers; some may experience motion sickness at extreme speeds
- Save speed ramp curve as preset for consistent application

---

## Platform-Specific Video Guides

Choose the right model for your specific use case and platform requirements.

### Kling AI (2.5 / 2.6 / 3.0)

**Strengths**:
- Exceptional camera control (dolly, orbit, tilt, pan, all highly predictable)
- Orbit shots are nearly flawless
- Strong subject consistency across shots
- Image-to-video is best-in-class for First Frame / Last Frame method
- Handles motion brush (draw camera paths) intuitively
- Excellent stone statue trick results

**Weaknesses**:
- Sometimes struggles with multiple simultaneous moving elements
- Physics simulation (water, cloth, particles) less realistic than Sora
- Can be cautious with extreme angles or dynamic motion

**Best For**:
- Product videos with precise camera control
- Cinematic shorts with specific camera choreography
- 3D effects and rotation showcases
- Character hero moments with locked positioning

**Key Features**:
- **Duration**: 5s or 10s options
- **Quality**: Standard or Professional (Professional recommended for final output)
- **Motion Brush**: Draw camera path directly on image
- **Image-to-Video**: Feed reference image; specify motion

**Prompting Tips**:
- Be explicit about camera movement; "orbits around" not just "rotating"
- Describe camera speed: "slow", "smooth", "gentle" produce best results
- Use specific orbit angles: "180-degree", "270-degree", "full 360-degree"
- Pair camera movement with subject stability for predictable output
- Include lighting direction and shadow quality for visual cohesion

**Recommended Settings**:
- Product/Commercial: Professional quality, 10s duration
- Social media: Standard quality, 5s duration
- Hero moments: Professional quality, 5s duration

**Example Prompt**:
```
A sleek silver laptop opening slowly, revealing the screen with blue glow.
Smooth camera dolly in combined with gentle tilt up from the keyboard to the screen.
Minimalist white desk in soft natural light from a window above and to the left.
Warm color temperature with soft shadows defining the laptop form.
Professional quality, 8 seconds, 16:9 aspect ratio.
```

---

### Runway Gen-3 / Gen-4

**Strengths**:
- Exceptional motion coherence and smoothness
- Strong artistic style interpretation
- Consistent character animation across poses
- Excellent subject tracking during motion
- Gen-4 has improved image-to-video capabilities
- Natural camera movement feels organic

**Weaknesses**:
- Less precise camera choreography than Kling
- Can struggle with simultaneous multiple movements
- Sometimes over-interprets prompts into unintended motion

**Best For**:
- Brand films and narrative content
- Artistic and stylized content
- Smooth flowing motion sequences
- Character-driven storytelling

**Key Features**:
- **Duration**: 5s standard (5-60s extended)
- **Aspect Ratio**: 16:9, 9:16, 1:1
- **Motion Intensity**: Adjustable (affects how pronounced movement is)
- **Motion Brush**: Draw motion vectors on keyframes
- **Camera Presets**: Predefined movement types

**Prompting Tips**:
- Keep prompts concise and evocative; less is more
- Focus on mood and movement direction rather than technical specs
- Single primary action works best
- Describe emotion and pacing rather than exact camera mechanics
- Use artistic reference points ("cinematic like [Film Title]")

**Recommended Settings**:
- Brand content: 16:9 widescreen, 10s, medium motion intensity
- Social vertical: 9:16, 5-6s, high motion intensity
- Artistic: 1:1 square, 5-8s, custom motion intensity

**Example Prompt**:
```
A professional in a modern office confidently presenting an idea, gesturing with flowing hands.
Camera smoothly glides right following the presenter's motion.
Bright contemporary workspace with large windows and soft natural light.
Warm and professional atmosphere with gentle shadows.
10 seconds, 16:9, medium motion intensity.
```

---

### Veo 3.1 (Google)

**Strengths**:
- Photorealism and naturally realistic motion
- Excellent long-form coherence (handles 30-60s sequences well)
- Strong UGC and realistic scenario generation
- Great at environmental authenticity
- Handles everyday imperfections naturally
- Commercial/advertising excellence

**Weaknesses**:
- Less precise camera control than Kling
- Prefers natural motion to stylized movement
- Can struggle with fantastical or highly stylized subjects

**Best For**:
- UGC-style advertising and testimonials
- Realistic commercial scenarios
- Everyday product demonstrations
- Long-form narrative sequences
- Lifestyle and aspirational content

**Key Features**:
- **Duration**: Up to 60 seconds
- **Aspect Ratio**: Multiple options
- **Prompt Style**: Detailed and descriptive works best
- **Image Input**: Can use reference images
- **Coherence**: Excellent across longer sequences

**Prompting Tips**:
- Provide detailed descriptions; Veo benefits from specificity
- Include everyday details and textures
- Specify authentic imperfections for realism
- Describe lighting in natural terms ("morning sunlight", "warm afternoon light")
- Add subtle sound design notes ("ambient office sounds", "natural background noise")

**Recommended Settings**:
- UGC: 8-15 seconds, full detail prompt
- Commercial: 12-20 seconds, aspirational tone
- Long-form: Up to 60 seconds, segmented narrative

**Example Prompt**:
```
A satisfied customer in a bright home office genuinely demonstrating a productivity app on their laptop screen.
Handheld camera with natural subtle movement and occasional slight tilt.
Warm natural window light streaming in from the left, creating realistic shadow variation.
The person speaks with authentic enthusiasm and natural pauses.
Genuine hand gestures and micro-expressions, realistic human behavior.
10 seconds, natural color (not color-corrected), authentic documentary feel.
```

---

### Sora 2 (OpenAI)

**Strengths**:
- Complex physics understanding and realistic simulation
- Excellent at multi-character interactions and group dynamics
- Strong scene composition and spatial relationships
- Handles complex narrative scenes
- Impressive particle effects and environmental dynamics
- Best for chaotic/dynamic scenes

**Weaknesses**:
- Longer generation times
- Less predictable than specialized tools
- Can struggle with precise static positioning

**Best For**:
- Narrative sequences with multiple characters
- Complex interactions and physics-based scenarios
- Epic scenes with environmental scale
- Choreographed group dynamics

**Key Features**:
- **Prompt Style**: Story-like, descriptive narratives work best
- **Interactions**: Excels at characters interacting with each other and environment
- **Physics**: Natural simulation of movement, collisions, interactions

**Prompting Tips**:
- Write prompts like a story; include narrative flow
- Specify character interactions explicitly
- Describe the emotional arc
- Include sensory details
- Structure like a scene description from a screenplay

**Example Prompt**:
```
In a bustling modern office, three professionals collaborate at a sleek conference table.
The leader presents ideas while the team responds with engaged gestures and expressions.
Warm office lighting with floor-to-ceiling windows showing a cityscape beyond.
The camera slowly orbits the table capturing the dynamic interaction and energy.
12 seconds, professional collaborative atmosphere, natural group dynamics.
```

---

### Higgsfield

**Strengths**:
- Quick iteration speeds
- Cinematic presets and professional templates
- Orbit automation (one-click orbit shots)
- Fast social media content generation
- Intuitive UI for rapid prototyping

**Weaknesses**:
- Less control than Kling or Runway for custom camera paths
- More limited to preset movement types
- Best for shorter-form content

**Best For**:
- Social media content requiring rapid iteration
- Quick product showcases with orbit automation
- Template-based commercial content
- Fast prototyping and testing

**Workflow Integration**:
- Use Higgsfield for rapid concept testing
- Use Kling or Runway for final production when camera control is critical
- Combine with Kling for enhanced orbit effects

**From the Higgsfield x Kling workflow**: Generate quick concepts in Higgsfield, then use Kling's superior orbit control for the final hero shot.

---

## Video Post-Production Workflow

Execute this five-stage process to transform raw AI output into broadcast-quality content.

### Stage 1: Review Raw AI Output
**Inspect** for artifacts, consistency issues, and quality gates.

**Checklist**:
- No morphing or distortion of key subjects
- Lighting remains consistent throughout
- Camera movement is smooth without jitter
- Color grading is appropriate or neutral
- Audio (if present) is clean or workable
- Duration matches specifications
- Aspect ratio is correct

**Decision**: Pass to next stage, regenerate with adjusted prompts, or reject entirely.

---

### Stage 2: Color Grade
**Match** brand palette or establish mood through color correction.

**Process**:
1. Analyze source color palette and lighting
2. Apply consistent color grading across all shots in sequence
3. Adjust exposure, contrast, saturation to match brand aesthetic
4. Ensure color continuity between clips
5. Add subtle color overlays for mood reinforcement

**Tools**: DaVinci Resolve, Premiere Pro, Final Cut Pro

**Common Grades**:
- **Warm/Inviting**: Increase warmth (+orange), lift shadows, slightly reduce blue
- **Cool/Professional**: Cool color cast (+blue), increase contrast, darken shadows
- **Cinematic**: Crush blacks, increase contrast, slightly desaturate
- **Vibrant**: Increase saturation, boost warm and cool tones selectively
- **Vintage/Nostalgic**: Add slight color shift, reduce contrast, add subtle grain

**Brand Alignment**: Apply grading preset matching brand guidelines or create custom LUT.

---

### Stage 3: Speed Ramp
**Add** dynamic pacing and emphasize key moments.

**Process**:
1. Identify emotional peaks and impact moments
2. Create speed curve: slow build → normal → fast reveal → slow landing
3. Test on target playback device
4. Adjust timing to sync with audio if applicable
5. Fine-tune for viewer comfort (avoid extreme speeds over 3x)

**Tools**: Premiere Pro, Final Cut Pro, DaVinci Resolve

**Best Practices**:
- Keep acceleration/deceleration smooth
- Avoid abrupt speed changes
- Maximum speed: 2-3x for comfortable viewing
- Synchronize with music beats for impact

---

### Stage 4: Sound Design
**Build** complete audio landscape with music, SFX, and ambient elements.

**Process**:
1. Add primary music track (licensed or royalty-free)
2. Layer sound effects synchronized to visual moments
3. Add ambient background sound establishing environment
4. Mix dialogue or voiceover if present
5. Add foley for natural movement sounds
6. Normalize and level all audio elements
7. Export with balanced dynamic range

**Audio Layer Structure**:
- **Layer 1**: Primary music track
- **Layer 2**: Sound effects (impacts, transitions, key moments)
- **Layer 3**: Ambient environmental audio
- **Layer 4**: Dialogue/voiceover (if applicable)
- **Layer 5**: Foley and subtle movement sounds

**Music Selection**:
- Match tempo to visual pacing
- Choose tracks matching brand tone
- Sync major beats to visual peaks
- Fade in/out smoothly for professional feel

**Tools**: Adobe Audition, Logic Pro, Final Cut Pro, Premiere Pro

---

### Stage 5: Text & Graphics Overlay
**Integrate** titles, captions, CTAs, and brand elements.

**Process**:
1. Establish typographic hierarchy matching brand
2. Time text elements to appear at logical moments
3. Add brand logos and watermarks strategically
4. Ensure all text is legible at intended viewing size
5. Add motion graphics or animated text if appropriate
6. Maintain clear visual hierarchy

**Text Timing**:
- Introductory text: First 1-2 seconds
- Key messaging: At visual peaks or camera pauses
- Call-to-action: Final 2-3 seconds
- Captions: 2-3 seconds each, clear sightlines

**Brand Integration**:
- Logo placement: Bottom right or top left (non-intrusive)
- Watermark: Semi-transparent, corner placement
- Typography: Match brand font guidelines
- Color: Use brand palette

**Tools**: Premiere Pro, After Effects, Final Cut Pro, Adobe Express

---

### Stage 6: Export & Optimization
**Finalize** for platform-specific requirements and distribution.

**Export Settings by Platform**:

| Platform | Codec | Bitrate | Resolution | Frame Rate |
|----------|-------|---------|------------|-----------|
| YouTube | H.264 | 8-16 Mbps | 1920×1080 or 3840×2160 | 24/30fps |
| Instagram | H.264 | 5-8 Mbps | 1080×1920 (vertical) | 30fps |
| TikTok | H.264 | 3-6 Mbps | 1080×1920 (vertical) | 30fps |
| Facebook | H.264 | 4-6 Mbps | 1920×1080 or 1080×1080 | 30fps |
| LinkedIn | H.264 | 5-8 Mbps | 1920×1080 | 30fps |
| Email/Web | H.264 | 2-4 Mbps | 1280×720 | 30fps |
| Archive/Master | ProRes 422 HQ | VBR | 3840×2160 | 24/30fps |

**Master File Creation**:
- Export highest quality version as archive (ProRes HQ or DNxHR)
- Store with all original assets and project files
- Create batch exports for all platform variations
- Maintain backup on external drive and cloud storage

---

## Failure Modes & Corrections

Troubleshoot common issues and implement targeted fixes.

| Problem | Cause | Fix |
|---------|-------|-----|
| Subject morphing mid-shot | Vague or inconsistent subject description | Use First Frame/Last Frame method; lock description word-for-word across prompts |
| Subject transforming unexpectedly | Subject description changed between shots | Copy-paste exact subject description; never paraphrase |
| Camera movement too fast | Prompt uses "quick", "fast", "rapid" | Replace with "slow", "smooth", "gentle", "gradual" |
| Camera movement too slow | Motion feels sluggish | Specify "dynamic", "sweeping", "flowing" movement; increase duration |
| Inconsistent character across shots | Multiple different prompt variations | Use "Character Brief" document; copy-paste identical descriptions |
| Uncanny valley in faces | Model limitation with high facial detail | Add subtle imperfections: "natural skin texture", "micro-imperfections", "realistic lighting shadows" |
| Jittery/unstable motion | Using standard quality with complex motion | Switch to Professional quality; reduce simultaneous moving elements; simplify composition |
| Background changing unexpectedly | Insufficient environmental description | Describe background explicitly: "white wall behind", "cityscape remains in background", "lighting stays consistent" |
| Hands/fingers distorted | Close-up hand focus; model limitation | Avoid extreme hand close-ups; position hands slightly out of focus; use First Frame to show correct hand position |
| Color inconsistency between shots | No color direction specified | Describe lighting color temperature in every prompt: "warm golden light", "cool blue tones", "neutral white light" |
| Subject too small in frame | Framing not specified | Specify framing: "tight close-up", "medium shot from waist up", "wide full-body frame" |
| Unexpected elements appearing | Prompt too open-ended | Be specific: "nothing else in background", "white surface only", "empty clean environment" |
| Motion blur excessive | High motion speed + standard quality | Use Professional quality; ensure camera descriptors use "smooth" and "gentle"; reduce motion speed in prompts |
| Lighting changes direction | Inconsistent light descriptions | Specify consistent light source: "consistent left-side lighting", "same overhead light throughout" |
| Subject stops partway | Duration too short for described motion | Increase duration: try 10 seconds instead of 5 seconds; simplify motion complexity |
| Weird warping at edges | Aspect ratio too extreme | Avoid ultra-wide (16:9 is safest); test with standard 16:9 first before vertical or square |
| Multiple characters incompatible | Group dynamics too complex | Simplify to fewer characters; give Sora 2 explicit interaction instructions; keep positioning clear |
| Scene too chaotic/busy | Too many moving elements | Reduce background activity; lock some elements stationary; use "stone statue trick" for stable positioning |
| Prompt ignored | Vague or contradictory directions | Simplify prompt; remove contradictions; use clear imperative language: "Camera orbits", "Subject stands still" |

---

## Aspect Ratios by Platform

Optimize dimensions for each distribution channel.

| Platform | Aspect Ratio | Resolution | Notes |
|----------|---|---|---|
| **YouTube** | 16:9 | 1920×1080 (HD) | Standard horizontal format; 3840×2160 for 4K |
| | 16:9 | 3840×2160 (4K) | Recommended for uploads requiring quality |
| | 9:16 | 1080×1920 (Vertical) | YouTube Shorts and mobile viewing |
| **Instagram Reels** | 9:16 | 1080×1920 | Full-screen mobile format |
| **Instagram Feed** | 1:1 | 1080×1080 | Square post format |
| | 4:5 | 1080×1350 | Optimal feed image (less crop) |
| **Instagram Stories** | 9:16 | 1080×1920 | Full-screen story format |
| **TikTok** | 9:16 | 1080×1920 | Standard TikTok vertical format |
| **Facebook** | 16:9 | 1920×1080 | Feed video horizontal format |
| | 1:1 | 1080×1080 | Feed square video format |
| | 9:16 | 1080×1920 | Vertical feed video |
| **Twitter / X** | 16:9 | 1920×1080 | Standard tweet video |
| | 1:1 | 1080×1080 | Square format (common for Twitter) |
| **LinkedIn** | 16:9 | 1920×1080 | Professional standard |
| | 1:1 | 1080×1080 | Carousel/square format |
| **Email** | 16:9 | 1280×720 | Safe for most email clients |
| **Cinematic** | 2.39:1 | 2560×1070 | Ultra-widescreen theatrical format |
| **Academy** | 1.37:1 | 1456×1080 | Classic film format |
| **IMAX** | 1.43:1 | 1544×1080 | Large format cinema |

**Platform Priority**:
1. **Generate at platform's primary ratio** to minimize cropping
2. **Create variations** for secondary formats (16:9 → 1:1 crop for Instagram feed)
3. **Test composition** at target ratio before final generation
4. **Safe title area**: Keep critical elements 10% inset from edges (for any crops)

**Optimization Tips**:
- Vertical (9:16): Subject should be centered; keep action within center 70% width
- Horizontal (16:9): Use full width for impact; assume 10% crop on sides possible
- Square (1:1): Center subject; avoid extreme edges; most balanced framing
- Ultra-wide (2.39:1): Subject framing very wide; background becomes key component

---

**Last Updated**: February 2026
**Kling AI Version Reference**: 2.5 / 2.6 / 3.0
**Runway Reference**: Gen-3 / Gen-4
**Additional Platforms**: Veo 3.1, Sora 2, Higgsfield

This reference enables masterful control over professional AI video generation workflows.
