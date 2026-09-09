# AI Creative Studio: Tool Selection & Comparison Reference

Choose the right AI creative tool for any task. This reference includes pricing, strengths, weaknesses, and access details for the most powerful image and video generation platforms.

## Table of Contents

1. [Image Generation Tools](#image-generation-tools)
2. [Video Generation Tools](#video-generation-tools)
3. [Decision Matrices](#decision-matrices)
4. [Budget Stacks](#budget-stacks)
5. [API Access](#api-access)

---

## Image Generation Tools

### Tier 1: Primary Workhorses

#### NanoBanana Pro (Google AI Studio)

- **Access**: Google AI Studio → Image generation → NanoBanana Pro model
- **Pricing**: Free tier available; Pro plan with Google AI Studio subscription
- **Strengths**: Best-in-class photorealistic humans, natural skin texture, authentic lighting, excellent facial detail, genuine human expressions
- **Weaknesses**: Less control over artistic style, can produce generic results without detailed prompts, limited stylization
- **Best for**: Portraits, headshots, lifestyle photography, UGC characters, realistic people, authentic human representation
- **Prompt style**: Descriptive, conversational, detailed scene description with context
- **Speed**: Fast (seconds)
- **Output**: Up to 1024x1024; can upscale externally

#### Midjourney v7

- **Access**: midjourney.com or Discord bot (@Midjourney)
- **Pricing**: $10/mo (Basic), $30/mo (Standard), $60/mo (Pro), $120/mo (Mega); annual discount available
- **Strengths**: Superior aesthetic composition, commercial-grade look, strong style control, excellent at mood/atmosphere, consistent branding across outputs
- **Weaknesses**: Less precise prompt following than Flux, stylized rather than photorealistic, Discord-based interface can be clunky, no true private API
- **Best for**: Product photography, branding assets, conceptual art, marketing imagery, mood boards, style exploration
- **Key parameters**: `--ar` (aspect ratio), `--s 0-1000` (stylize), `--c 0-100` (chaos), `--sref` (style reference), `--v 7`, `--niji 6` (anime mode)
- **Speed**: ~30-60 seconds per generation
- **Output**: Up to 2048x2048

#### Flux Pro (Black Forest Labs)

- **Access**: Replicate, fal.ai, Together AI, or local via ComfyUI/WebUI
- **Pricing**: ~$0.05-0.10 per image via API; free locally (requires GPU)
- **Strengths**: Best prompt adherence, excellent text rendering, complex multi-element scenes, open weights, fastest inference times, highest quality-to-speed ratio
- **Weaknesses**: Requires API/technical setup, less "magical" aesthetic than Midjourney, steeper learning curve for optimization
- **Best for**: Complex compositions, text-in-image, precise prompt following, technical artwork, batch processing, text-heavy designs
- **Prompt style**: Very detailed, explicit, every element specified, technical terminology acceptable
- **Speed**: ~5-15 seconds
- **Output**: Flexible resolution (native 512-1024, can scale to 2048+)
- **Variants**: Flux Pro, Flux Realism, Flux Schnell (faster, lower quality), Flux Pro Depth

#### DALL-E 3 / GPT Image (ChatGPT)

- **Access**: ChatGPT Plus/Pro interface, or OpenAI API
- **Pricing**: Included with ChatGPT Plus ($20/mo) or Pro ($200/mo); API pricing ~$0.04-0.08 per image
- **Strengths**: Excellent instruction following, great text rendering, iterative editing within conversation, conversational refinement, built-in contextual awareness, integrated in ChatGPT, natural language understanding
- **Weaknesses**: Sometimes overly "clean" aesthetic, limited style control, cannot modify images directly (requires regeneration)
- **Best for**: Quick concept iteration, typography, detailed specifications, when you need fast back-and-forth refinement, conversational creative development
- **Prompt style**: Natural language, conversational, edit instructions, can reference previous outputs
- **Speed**: Fast (seconds)
- **Output**: Up to 1024x1024 (square), 1024x1792 (portrait), 1792x1024 (landscape)

#### Ideogram 3

- **Access**: ideogram.ai web interface or API
- **Pricing**: Free tier (limited daily images), $8/mo (Basic), $20/mo (Plus), $60/mo (Pro)
- **Strengths**: Best-in-class text rendering/typography, accurate text placement, graphic design, readable font rendering, precise character placement
- **Weaknesses**: Less photorealistic than NanoBanana, less artistic control than Midjourney, smaller generation queue
- **Best for**: Logos, posters with text, infographics, anything requiring readable text in the image, brand guidelines, design system assets
- **Prompt style**: Clear text in quotes, explicit placement instructions, design terminology
- **Speed**: Fast (seconds)
- **Output**: Multiple sizes, square/landscape/portrait options

### Tier 2: Specialized / Platform-Specific

#### Artlist Original Model 1.0

- **Access**: Artlist AI Toolkit (artlist.com)
- **Pricing**: Part of Artlist subscription ($12.49-24.99/mo)
- **Strengths**: Commercial stock quality, consistent output, designed for marketing/advertising, reliable mood/color palette
- **Weaknesses**: Less distinctive than Midjourney, less creative control than Flux
- **Best for**: Stock-style commercial imagery, marketing campaign assets, corporate stock photos, lifestyle stock alternatives
- **Output**: Stock-optimized sizing

#### Lovart AI

- **Access**: lovart.ai web interface
- **Pricing**: Free tier available, Pro/Premium plans available
- **Strengths**: 3D pop poster effects, creative compositions, border-break designs, depth-of-field effects
- **Weaknesses**: Specialized niche, less versatile than general tools, learning curve for achieving desired effect
- **Best for**: 3D poster designs, dramatic compositions with depth effects, anime/pop art styles, social media promotional graphics

---

## Video Generation Tools

### Tier 1: Primary Workhorses

#### Kling AI (Kuaishou)

- **Access**: klingai.com web interface or Discord bot
- **Pricing**: Free tier (limited), ~$7.99/mo (Pro), ~$29.99/mo (Premium)
- **Versions**: 2.5, 2.6, 3.0 (latest, recommended)
- **Strengths**: Best camera control, excellent orbit shots, reliable image-to-video consistency, good subject consistency across frames, stone statue technique, motion brush precision
- **Weaknesses**: Occasional texture artifacts on fast motion, limited to 5-10 seconds per clip, occasional flicker on boundaries
- **Best for**: Product videos, orbit shots, cinematic shorts, controlled camera movements, smooth pans/zooms, hero product showcase
- **Key features**: Image-to-video, text-to-video, motion brush (precise trajectory control), camera path control, First Frame/Last Frame technique
- **Duration**: 5 seconds (standard), 10 seconds (extended)
- **Quality modes**: Standard / Professional
- **Speed**: ~2-5 minutes per generation
- **Output**: 1080p or 2K

#### Runway Gen-4 (formerly Runway, powered by Luma)

- **Access**: runwayml.com web interface
- **Pricing**: $12/mo (Standard), $28/mo (Pro), $76/mo (Unlimited)
- **Strengths**: Strong motion coherence, artistic quality, good at maintaining style across frames, motion brush with timeline scrubbing, camera preset library
- **Weaknesses**: More expensive per generation, less precise camera control than Kling, fewer specialized techniques
- **Best for**: Brand films, artistic content, motion graphics, style-driven video, multi-shot sequences, complex camera movements
- **Key features**: Image-to-video, text-to-video, motion brush, camera presets, loops, Gen-4 turbo option for speed
- **Speed**: ~1-3 minutes per generation
- **Output**: Up to 4K on higher tiers

#### Veo 3.1 (Google DeepMind)

- **Access**: Google AI Studio, Vertex AI, or Claude (via integration)
- **Pricing**: Part of Google AI Pro subscription (~$20/mo or included with credits)
- **Strengths**: Best photorealism, natural human motion, long coherence (up to 6 seconds), built-in audio generation, physics accuracy
- **Weaknesses**: Less explicit control over specific camera movements, learning curve for effective prompting, limited style control
- **Best for**: UGC-style content, realistic scenarios, testimonials, commercial video, natural human movement, product in-use demonstrations
- **Prompt style**: Detailed, naturalistic, include imperfection cues (breathing, blinking, natural interactions)
- **Speed**: ~2-4 minutes per generation
- **Output**: 1080p or 1440p

#### Sora 2 (OpenAI)

- **Access**: ChatGPT Plus/Pro, gradual rollout
- **Pricing**: Included with ChatGPT Plus ($20/mo) or Pro ($200/mo)
- **Strengths**: Complex multi-character scenes, physics understanding, narrative coherence, conversational refinement, natural language understanding
- **Weaknesses**: Less camera control, can be inconsistent, limited availability (waitlist)
- **Best for**: Narrative sequences, complex interactions, storytelling, conceptual video, multi-character scenes
- **Speed**: Variable (2-5 minutes)
- **Output**: 1080p, variable aspect ratios

### Tier 2: Specialized

#### Higgsfield

- **Access**: higgsfield.ai web interface
- **Pricing**: Free tier, paid plans available
- **Strengths**: Quick iterations, automated orbit presets, social-optimized output, preset templates
- **Weaknesses**: Less control than Kling/Runway, smaller feature set
- **Best for**: Social media video, quick prototypes, orbit automation, TikTok/Instagram Reels optimization

#### Arcads

- **Access**: arcads.ai platform
- **Pricing**: $99/mo+
- **Strengths**: AI spokesperson creation, UGC ad automation, script-to-video pipeline, one-click avatar video
- **Weaknesses**: Specialized for ads/UGC only, less creative flexibility
- **Best for**: UGC ads, testimonial videos, social commerce content, rapid ad production, talking head videos

---

## Decision Matrices

### Image Tasks Decision Matrix

Use this table to select the optimal tool for any image generation task.

| Task | First Choice | Alternative | Why | Speed | Cost |
|------|-------------|-------------|-----|-------|------|
| Professional headshot | NanoBanana Pro | Flux Pro | Best realistic faces, natural skin | 5s | Free-$20/mo |
| Product hero shot | Midjourney v7 | DALL-E 3 | Best commercial aesthetic, polish | 45s | $30/mo |
| Logo / text design | Ideogram 3 | Flux Pro | Best typography, readable text | 10s | Free-$20/mo |
| Fashion editorial | Midjourney v7 | NanoBanana Pro | Best mood/style, consistency | 45s | $30/mo |
| UI mockup/wireframe | DALL-E 3 | Flux Pro | Best iterative editing, precision | 10s | $20/mo |
| Brand lifestyle | NanoBanana Pro | Midjourney v7 | Best natural look, authentic feel | 5s | Free-$20/mo |
| 3D poster effect | Lovart AI | Midjourney v7 | Specialized 3D pop, depth effects | 20s | Varies |
| Complex multi-element | Flux Pro | DALL-E 3 | Best prompt adherence, detail | 8s | $0.05-0.10 |
| Quick concept/iteration | DALL-E 3 | NanoBanana Pro | Fastest feedback loop, conversation | 5s | $20/mo |
| Stock/commercial | Artlist Model 1.0 | Midjourney v7 | Commercial quality, licensable | 10s | $12.49/mo |
| Social media graphic | Ideogram 3 | Midjourney v7 | Text-heavy, optimized sizing | 10s | Free-$20/mo |
| Character/avatar | NanoBanana Pro | Midjourney v7 | Consistent face generation | 5s | Free-$20/mo |
| Detailed concept art | Flux Pro | Midjourney v7 | Complex details, precision | 8s | $0.05-0.10 |
| Product mockup | DALL-E 3 | Flux Pro | Fast iteration, edit feedback | 10s | $20/mo |

### Video Tasks Decision Matrix

Use this table to select the optimal tool for any video generation task.

| Task | First Choice | Alternative | Why | Duration | Cost |
|------|-------------|-------------|-----|----------|------|
| Product orbit/showcase | Kling 3.0 | Runway Gen-4 | Best camera control, smooth motion | 10s | $7.99/mo |
| UGC testimonial ad | Veo 3.1 | Kling 3.0 | Best photorealism, natural humans | 6s | $20/mo |
| Cinematic brand film | Runway Gen-4 | Kling 3.0 | Best artistic quality, mood | 10s | $28/mo |
| Multi-shot sequence | Kling 2.5 | Runway Gen-4 | Best frame continuity, consistency | 30s+ | $7.99/mo |
| Social media clip | Higgsfield | Kling 3.0 | Fastest output, optimized format | 10s | Varies |
| Motion graphics | Runway Gen-4 | Kling 3.0 | Best text animation, transitions | 10s | $28/mo |
| Dramatic reveal | Kling (First/Last) | Runway Gen-4 | Best controlled transitions | 10s | $7.99/mo |
| Stone statue effect | Kling + NanoBanana | — | Specialized technique, proven method | 10s | $7.99/mo |
| Product demo | Veo 3.1 | Kling 3.0 | Natural product interaction, realism | 6s | $20/mo |
| Talking head/avatar | Arcads | Veo 3.1 | Automated spokesperson, UGC ads | 30s+ | $99/mo |
| Landscape/nature | Veo 3.1 | Runway Gen-4 | Best natural motion, photorealism | 6s | $20/mo |
| Animation style | Midjourney + Kling | Runway Gen-4 | Keyframe consistency, style control | 10s | $30/mo |

---

## Budget Stacks

Choose a budget tier based on your needs and usage volume.

### Starter Stack ($20-30/month)

Ideal for: Solopreneurs, side projects, learning, low-volume creative work

- **NanoBanana Pro** (Free) — primary image generation, photorealistic humans
- **ChatGPT Plus** ($20/mo) — DALL-E 3 + Sora 2 + conversational refinement
- **Kling AI Free** (limited) — video generation, basic usage
- **Ideogram Free** — typography, logos, text-in-image
- **Google AI Studio Free** — NanoBanana Pro access

**Monthly Cost**: ~$20-30
**Image Generations/Month**: ~100-200
**Video Generations/Month**: ~5-10
**Best for**: Experimentation, learning, occasional projects

### Professional Stack ($70-90/month)

Ideal for: Freelancers, small studios, regular commercial work, consistent client projects

Everything in Starter, plus:

- **Midjourney Standard** ($30/mo) — premium aesthetic imagery, branding assets, higher quality
- **Kling Pro** ($8/mo) — unlimited video generation, priority processing
- **Runway Standard** ($12/mo) — motion graphics, brand film assets, expanded features

**Monthly Cost**: ~$70-90
**Image Generations/Month**: ~500-1000
**Video Generations/Month**: ~50-100
**Best for**: Professional freelance work, client deliverables, consistent output

### Power Stack ($200-300/month)

Ideal for: Agencies, studios, high-volume production, multiple clients, specialized needs

Everything in Professional, plus:

- **Midjourney Pro** ($60/mo) — maximum generations, stealth mode, premium priority
- **Arcads** ($99/mo) — automated UGC ad production, talking head videos, rapid scaling
- **Runway Pro** ($28/mo) — more generations, higher quality, extended duration
- **Kling Premium** ($30/mo) — priority processing, maximum duration, highest quality
- **Flux Pro API** ($50/mo estimated) — batch processing, automation, custom integrations

**Monthly Cost**: ~$237-350
**Image Generations/Month**: ~2000+
**Video Generations/Month**: ~200+
**Best for**: Agencies, Studios, high-volume UGC, content production, automation

---

## API Access for Automation

Use these platforms to build automated workflows or integrate into your production pipeline.

| Platform | API Available | Cost Model | Rate Limits | Best For | Setup Complexity |
|----------|--------------|------------|-----------|----------|------------------|
| Flux Pro | Yes (Replicate, fal.ai, Together AI) | Per-image (~$0.05-0.10) | Depends on provider | Batch image generation, automation, custom workflows | Medium |
| DALL-E 3 | Yes (OpenAI API) | Per-image ($0.04-0.08) | Depends on plan | Programmatic image creation, app integration, variable sizing | Low |
| Kling AI | Yes (limited) | Per-video, pay-as-you-go | Depends on plan | Automated video generation, batch processing, workflow integration | Medium |
| Midjourney | No public API (yet) | Subscription only | Depends on tier | Manual Discord/web only, no direct integration | N/A |
| Runway | Yes (limited) | Per-second of output | Depends on plan | Automated video generation, motion graphics pipeline | Medium |
| Ideogram | Yes | Per-image | Depends on plan | Batch text-in-image generation, design automation | Low |
| Veo 3.1 | Limited (Vertex AI) | Per-video | Depends on plan | Google Cloud integration, large-scale deployment | High |

### API Integration Recommendations

**For Image Batch Processing**: Use Flux Pro via Replicate or fal.ai—lowest cost, fastest, most flexible

**For Video Automation**: Use Runway API or Kling API integrated with your production tools

**For Text-Heavy Design**: Use DALL-E 3 API via OpenAI or Ideogram API—both excellent instruction following

**For Serverless Workflows**: Use fal.ai with their serverless architecture—minimal setup, pay-per-use

---

## Prompt Engineering Tips by Tool

### NanoBanana Pro Prompts

Structure: [Subject description] + [Style cues] + [Lighting] + [Camera/framing]

```
Example: "A 35-year-old female professional headshot, warm smile,
natural lighting, slight soft focus background, studio quality,
soft key light from left, shot on 50mm lens"
```

**Key phrases**: "natural," "authentic," "soft lighting," "genuine expression," "lifestyle," "real skin texture"

### Midjourney v7 Prompts

Structure: [Visual concept] + [Mood/atmosphere] + [Style reference] + [Technical params]

```
Example: "minimal product hero shot, matte black speaker on white
background, studio lighting, luxury aesthetic, commercial photography,
sharp focus, cinematic --ar 16:9 --s 750"
```

**Key phrases**: "hero shot," "mood," "aesthetic," "atmospheric," "cinematic," "commercial"

### Flux Pro Prompts

Structure: [Explicit description] + [Every element detailed] + [Technical specs] + [Quality notes]

```
Example: "A modern kitchen with white cabinets, black granite countertop,
three bar stools with blue upholstery, pendant lights above, large window
with natural light, hardwood floor, professional product photography,
sharp focus, 8k quality"
```

**Key phrases**: "detailed," "specific," "precise," "sharp," "exact placement"

### DALL-E 3 Prompts

Structure: [Natural language description] + [Edit instructions for iteration]

```
Example: "Create a professional business portrait of a woman in a blue
blazer, smiling warmly at the camera. Soft office lighting. Can you make
the background more blurred and add a subtle color to make it look more
professional?"
```

**Key phrases**: Natural conversational language, can reference "the previous image," can iterate naturally

### Ideogram 3 Prompts

Structure: [Text description] + ["EXACT TEXT IN QUOTES"] + [Placement instructions]

```
Example: "A colorful poster for a tech startup. Large text at top reading
'INNOVATION' in bold sans-serif. Subtitle 'Building the Future' centered
below. Abstract geometric shapes in background, vibrant colors."
```

**Key phrases**: Text in quotes, "centered," "bold," "above/below," specific font styles

### Kling AI Video Prompts

Structure: [Scene description] + [Camera movement] + [Subject action] + [Duration]

```
Example: "A sleek white smartphone rotating slowly on a minimalist white
background. Camera orbits 360 degrees around the phone. Professional studio
lighting. 5 seconds."
```

**Key techniques**: "orbit," "rotate," "pan," "zoom," "slow motion," "stone statue" (freeze background, move subject)

### Runway Gen-4 Prompts

Structure: [Scene] + [Mood/style] + [Movement] + [Artistic direction]

```
Example: "A luxury watch moving through clouds. Cinematic motion, soft
lighting, dreamy atmosphere. Camera floats around the watch gracefully.
Professional color grading."
```

**Key phrases**: "cinematic," "atmospheric," "artistic," "graceful," "mood"

### Veo 3.1 Prompts

Structure: [Realistic scenario] + [Natural action] + [Human elements] + [Environmental detail]

```
Example: "A woman using a coffee maker in her modern kitchen. She grinds
beans, fills the water, presses start. Natural morning light through window.
Realistic human movement. 4 seconds."
```

**Key phrases**: "realistic," "natural," "authentic," "genuine," avoid over-specification

---

## Workflow Integration Patterns

### Pattern 1: Concept to Asset (Image)

1. **Ideate with DALL-E 3** (conversational, iterative) → Quick exploration
2. **Refine with NanoBanana Pro** (photorealism) or **Midjourney** (aesthetics) → Directional asset
3. **Produce final with Flux Pro** (precision) or **Ideogram** (text) → Polished deliverable
4. **Upscale/Edit externally** → Final output

### Pattern 2: Fast Commercial Workflow (Image)

1. **Batch generate with Flux Pro API** → Test variations
2. **Select best direction** → Manual review
3. **Refine with DALL-E 3** → Final tweaks
4. **Export and polish** → Ready for use

### Pattern 3: Product Video Showcase

1. **Hero image with Midjourney** or **NanoBanana** → Static reference
2. **Video with Kling 3.0** (orbit) → Cinematic product movement
3. **Optional sound/music** → Artlist or similar
4. **Compile/edit** → Final video

### Pattern 4: Brand Campaign (Multi-Format)

1. **Moodboard with Midjourney** → Establish aesthetic
2. **Product images with NanoBanana + Flux** → Photo library
3. **Logo/text with Ideogram** → Brand assets
4. **Video with Kling + Runway** → Motion content
5. **Integrate and brand** → Cohesive campaign

### Pattern 5: UGC Ad Production (At Scale)

1. **Script writing** → Manual or AI-assisted
2. **Avatar video with Arcads** or **Veo 3.1** → Testimonial/demo
3. **Product images with NanoBanana** → Support assets
4. **Batch with Flux Pro API** → Multiple variations
5. **Compile and test** → Multi-variant ad sets

---

## Pricing Comparison: Cost Per Output

### Image Cost Efficiency

| Tool | Cost per Image | Best Value For |
|------|----------------|-----------------|
| Flux Pro API | $0.05-0.10 | High-volume batch |
| DALL-E 3 API | $0.04-0.08 | Production pipeline |
| NanoBanana Pro | Free | Unlimited usage |
| Ideogram Free | Free | Limited daily |
| ChatGPT Plus | $0.67/mo per image* | Iterative work |
| Midjourney Standard | $0.60/mo per image* | Professional use |
| Midjourney Pro | $1.50/mo per image* | High-volume agency |

*Based on typical usage; actual cost depends on generation speed

### Video Cost Efficiency

| Tool | Cost per Minute | Best Value For |
|------|----------------|-----------------|
| Kling Pro | $0.16-0.40 | Regular production |
| Veo 3.1 | $0.33-0.50 | Quality-focused |
| Runway Standard | $0.40-0.60 | Motion graphics |
| Runway Pro | $0.35-0.50 | Higher volume |
| Arcads | $1.65 per minute+ | Ad production |

---

## Common Questions Answered

### Should I use local Flux or cloud Flux?

**Use cloud** (fal.ai, Replicate) if: You want speed, don't have GPU, need batch processing, prioritize ease
**Use local** (ComfyUI) if: You have RTX 3080+ GPU, want unlimited generations, need customization, cost is primary concern

### When should I upgrade from Free/Starter tiers?

**Upgrade to Professional** when: You're generating 50+ images/week, have regular client projects, need Midjourney's aesthetic, want faster video

**Upgrade to Power** when: You're in an agency, generating 200+ images/week, need automation, want priority processing

### Can I use AI-generated images commercially?

Most tools allow commercial use with standard licensing:
- **NanoBanana Pro**: Yes (with attribution sometimes required)
- **Midjourney**: Yes (ownership with paid plans)
- **Flux Pro**: Yes (open weights)
- **DALL-E**: Yes (with API/Plus terms)
- **Artlist**: Yes (commercial license included)
- **Video tools**: Varies by tool, check terms

Always review specific terms for client/brand use.

### What's the best workflow for a one-person creative business?

1. **Start with Starter Stack** ($20/mo) — test tools, learn workflows
2. **Move to Professional Stack** ($70-90/mo) when you have consistent work
3. **Add API automation** only if generating 100+ per week
4. **Upgrade to Power Stack** only if managing multiple clients/projects

Most solopreneurs operate profitably at Professional tier.

### How do I integrate these tools into my existing software?

**For custom apps**: Use OpenAI API (DALL-E), Flux Pro API (Replicate), or Runway API
**For no-code**: Use Zapier, Make, or Integromat to connect tools
**For production**: Build with fal.ai or Together AI—easiest serverless integration

---

## Last Updated

This reference reflects pricing and features as of February 2026. Pricing and availability change frequently—verify current costs on official platforms.

**Tools included**: NanoBanana Pro, Midjourney v7, Flux Pro, DALL-E 3, Ideogram 3, Kling 3.0, Runway Gen-4, Veo 3.1, Sora 2, Artlist, Lovart, Higgsfield, Arcads

**For questions or updates**: Refer to official tool documentation and current pricing pages.
