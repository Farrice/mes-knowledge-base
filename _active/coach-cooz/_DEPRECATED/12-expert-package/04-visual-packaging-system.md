# 04 — Visual Packaging System
## The Resurrection Coach Visual Nervous System

> **What this is**: The complete visual operating system for Coach Cooz's content. Brand identity, AI image prompts, photo direction, fallback playbook. Everything needed to make the posts LOOK as good as they READ.
>
> **Who it's for**: Cooz (primary). Farrice as execution partner. Any future designer, VA, or agency hire who needs to stay on-brand without re-inventing the wheel.
>
> **How to use it**: Section 1 is the law (brand DNA, don't violate). Section 2 is the toolbox (six content categories, prompt templates, failure fixes). Section 3 is the lookup table (what visual goes with what content type). Section 4 is the photo playbook. Section 5 is the 10 ready-to-use prompts for Week 1. Section 6 is the fallback when the AI barfs.

---

## Table of Contents

1. [The Resurrection Brand Visual Identity](#section-1--the-resurrection-brand-visual-identity)
2. [The 6 Content Visual Categories](#section-2--the-6-content-visual-categories)
3. [The Post-Type Visual Defaults](#section-3--the-post-type-visual-defaults)
4. [Cooz-Specific Imagery — Personal Photo Direction](#section-4--cooz-specific-imagery-personal-photo-direction)
5. [Quick-Start Visual Prompts for Week 1](#section-5--quick-start-visual-prompts-for-week-1)
6. [The Fallback When AI Image Gen Fails](#section-6--the-fallback-when-ai-image-gen-fails)

---

# SECTION 1 — THE RESURRECTION BRAND VISUAL IDENTITY

Everything downstream obeys this section. If a prompt, template, or image violates the rules here, kill it and start over.

## 1.1 The Visual Thesis (One Sentence)

> **The Resurrection Coach brand looks like a cathedral, a gym at dawn, and a hand-loaded 35mm camera had a child — and that child grew up reading Cormac McCarthy.**

Cinematic. Masculine. Restrained. Spiritual without being churchy. Premium without being corporate. Raw without being sloppy. Quiet confidence, not loud optimization.

## 1.2 Color Palette — "Soil, Cathedral, Dawn"

These are the only six colors in the brand. Every asset uses a subset of them. No rainbow palettes, no off-brand accents, no trends.

### Primary Colors

| Role | Name | Hex | RGB | Use Case |
|---|---|---|---|---|
| **Primary Dark** | Cathedral Black | `#0E0E0C` | 14, 14, 12 | Dominant background. Text on light. The weight of the brand. Not pure black — has a warm undertone, like aged leather or dark coffee. |
| **Primary Light** | Dawn Linen | `#F3EEE3` | 243, 238, 227 | Light backgrounds. Quote card surfaces. Text on dark. Warm off-white — the color of morning light on a cathedral wall, not medical white. |

### Secondary Colors

| Role | Name | Hex | RGB | Use Case |
|---|---|---|---|---|
| **Secondary Warm** | Soil Brown | `#3A2A1F` | 58, 42, 31 | Rich brown for photo overlays, gradient ends, card frames. The color of wet earth after rain. |
| **Secondary Cool** | Stone Gray | `#5B5B55` | 91, 91, 85 | Body copy on light backgrounds, secondary UI, photo shadow lifts. Warm-leaning gray. NEVER pure gray — has a hint of olive. |

### Accent Colors (use sparingly — 5% of any composition max)

| Role | Name | Hex | RGB | Use Case |
|---|---|---|---|---|
| **Accent 1** | Ember Gold | `#C08A3E` | 192, 138, 62 | THE one accent color. Used for highlights, pull-quotes, the one word that needs to punch. Think brass bell, votive candle, single sunset ray. NEVER neon. NEVER yellow. |
| **Accent 2** | Blood Rust | `#6B2B1D` | 107, 43, 29 | Very rare use. Emotional weight moments (Resurrection Chronicles before/after, intense confession posts). Dried blood, oxidized iron. Signals: this is the serious one. |

### Gradient Recipes (pre-approved)

1. **Dawn Wash**: `#0E0E0C` → `#3A2A1F` — dark-to-brown for photo bottoms, gives text room to breathe
2. **Cathedral Light**: `#F3EEE3` → `#C08A3E` (10%) — warm gradient for Dawn Linen backgrounds that need atmospheric depth
3. **Soil Fade**: `#3A2A1F` → `#0E0E0C` — rich brown-to-black for YouTube thumbnail backgrounds

### What These Colors ARE NOT

- NOT corporate blue + white (Justin Welsh slide trap — clean but cold)
- NOT wellness-industry sage + cream (every other fitness coach in 2026)
- NOT Huberman hospital-blue-on-white (too clinical, too optimization)
- NOT Liver King primal red/black (too aggro, too primal-LARP)
- NOT Bryan Johnson tech-white (too sci-fi, too "trying not to die")

If a palette test looks like any of those, restart.

---

## 1.3 Typography System

Three fonts. Chosen for specific jobs. Available on Google Fonts so anyone can use them for free.

### Primary — Headlines & Display

**Font**: [**Fraunces**](https://fonts.google.com/specimen/Fraunces) (Google Fonts, free)

- **Why**: Fraunces is a contemporary serif with historical weight. It reads as editorial (Monocle, The Atlantic, Bloomberg Longform) not corporate (Times New Roman). Has a variable-weight axis that goes from delicate (300) to thunderous (900). The optical size axis lets display sizes feel sculpted, not stretched.
- **Weights to use**: 900 for Name/Hero (Cathedral Black), 700 for section headers, 300 italic for soft pull-quotes.
- **The psychology**: It signals "this was written by someone who reads books, not just TED Talks." That's Cooz.
- **Fallback**: Georgia, serif

### Secondary — Body & Long-Form

**Font**: [**Inter**](https://fonts.google.com/specimen/Inter) (Google Fonts, free) — *used sparingly*

- **Why**: Inter is the cleanest humanist sans-serif available free. Use it only where Fraunces would be overkill (long body copy in blog posts, LinkedIn carousel body). Pair it with Fraunces to get editorial hierarchy.
- **Weights to use**: 400 regular for body, 600 for subtle emphasis, NEVER 700+ (Fraunces does all the shouting).
- **CAVEAT**: Inter is overused in tech/SaaS. To keep the brand from collapsing into Justin-Welsh-default, body copy should prefer Fraunces at 400 whenever possible. Inter is the backup, not the default.
- **Fallback**: system-ui, sans-serif

### Accent — All-Caps Micro-Type

**Font**: [**Syne**](https://fonts.google.com/specimen/Syne) or [**Space Grotesk**](https://fonts.google.com/specimen/Space-Grotesk) (Google Fonts, free)

- **Why**: For small all-caps labels, category tags, episode numbers, datestamps. Adds a touch of contemporary grit without going retro.
- **Weights to use**: 700 all-caps, letter-spacing `0.08em`.
- **Use case**: "EPISODE 07 // THE RESURRECTION PODCAST" / "DEPLETION DIARIES Nº 03" / a 2-word kicker above a Fraunces headline.
- **Fallback**: Helvetica Neue, sans-serif

### Typographic Rules (Non-Negotiable)

1. **Never more than 3 font weights per composition.** Hierarchy comes from size and space, not a zoo of weights.
2. **Headlines get generous tracking**: Fraunces at display sizes should have `-0.01em` to `-0.02em` tracking. Tight, sculptural.
3. **All-caps needs `0.08em` letter-spacing minimum.** Otherwise it reads as shouting.
4. **Body copy line-height**: 1.45 to 1.6. Never tighter (claustrophobic), never looser (loose).
5. **Never center-align body paragraphs.** Only headlines, pull-quotes, and single-line statements center. Everything else is left-aligned. Center-aligned body reads as a wedding invitation or a motivational meme.

---

## 1.4 Mood Keywords — Put These In Every AI Prompt

These seven words are the backbone of every image-generation prompt. If a prompt doesn't include the spirit of these, it's not on brand.

```
cinematic, masculine, restrained, golden hour lighting,
single subject, shallow depth of field, 35mm film grain
```

### Extended keyword library (pick 3-5 per prompt, in addition to the core 7)

- **Lighting**: *low-key lighting, chiaroscuro, volumetric light through window, side-lit, rim light, natural window light, candlelit, dawn light, dusk blue hour*
- **Camera/Lens**: *Leica Q2, Kodak Portra 400 film stock, 50mm prime, shallow focus, medium format, Hasselblad, anamorphic*
- **Mood**: *contemplative, introspective, weight, stillness, reverent, quiet intensity, solitary, meditative, pensive, unguarded*
- **Texture**: *film grain, dust motes in light, soft shadows, natural skin texture, weathered surfaces, concrete, leather, raw wood, linen*
- **Composition**: *negative space, rule of thirds, asymmetrical, tight crop, wide environmental portrait, over-the-shoulder, from behind*
- **Reference aesthetic**: *editorial portrait, New York Times Sunday Magazine, Monocle Magazine, Cormac McCarthy novel cover, Terrence Malick film, Roger Deakins cinematography*

### Emotional keyword bank (for Depletion Diaries / vulnerable content)

*weight of responsibility, quiet exhaustion, held composure, private moment, unguarded, 2 AM hour, before the day starts, after everyone leaves, the moment no one sees, honest fatigue, the space between*

### Spiritual keyword bank (for Resurrection content — use sparingly, max 30% of prompts)

*reverent, dawn through cathedral window, empty chapel at sunrise, candlelight, iconographic framing, stone texture, light as grace, buried and unburied, stillness before resurrection*

---

## 1.5 What To AVOID — The Brand Killers

These visual moves destroy the brand instantly. If a generated image contains any of them, delete and regenerate.

### Visual Failure Modes (the No-Fly List)

1. **Stock photo athleticism** — the generic "handsome man smiling at the gym with a water bottle" energy. Every transformation coach on Unsplash. Dead on arrival.
2. **Corporate wellness pastels** — sage green + cream + beige + a sprig of eucalyptus. Looks like a day spa brochure. Not the Resurrection Coach.
3. **Neon / cyberpunk / tech-bro gradients** — purple-to-blue gradient, glitch effects, HUD overlays, AI hexagon patterns. Screams SaaS, not soul.
4. **Overly-styled influencer aesthetic** — heavy skin smoothing, perfect teeth, Beverly Hills backdrops, luxury-watch hero shots. That's the optimization lane. Cooz is the resurrection lane.
5. **Liver King primal LARP** — shirtless, ancestral, meat-hanging, "how primal I am" energy. Destroys credibility with the founder ICP.
6. **The generic "coach pointing at camera"** — arms crossed, gym background, motivational-speaker posture. Every other fitness coach on LinkedIn. Instant credibility drop.
7. **Mirror transformation shots from the front** — the flexing-in-the-mirror shot. Inherently cheap no matter how good the transformation is. Side-profile or environmental shots only.
8. **MrBeast / ClickBait yellow+red thumbnail energy** — arrows, circles, shocked-face reactions, giant yellow CAPS text. Wrong audience. Dan Go's restrained thumbnails are the reference.
9. **AI-obvious slop tells** — 6-fingered hands, melting fonts, warped text, symmetrical-face "uncanny valley" subjects, perfectly smooth plastic skin, triple-rendered eyeballs. If an image looks like it was generated in 2023, kill it.
10. **Emoji-heavy Canva templates** — fire emojis, arrows, speech bubbles, comic-style impact text. Reads as amateur.
11. **Generic "entrepreneur in front of city skyline"** — the bridge-at-sunset, cityscape-silhouette, cliché-founder-pose trap. No.
12. **Quote cards on solid colored backgrounds with no texture** — flat, dead, Pinterest-amateur. All quote cards must have atmospheric depth (grain, gradient, photo underlay).

### When you see any of these: **delete and regenerate.** Do not ship.

---

# SECTION 2 — THE 6 CONTENT VISUAL CATEGORIES

For each category: the visual job, a universal prompt template, 3 example prompts, technical specs, and common failure modes.

> **Prompting convention used below**: Prompts are written in **Midjourney v7 / Flux 1.1 Pro** syntax. Each ends with a `--ar X:Y` aspect ratio and `--style raw --v 7` (for Midjourney) or equivalent Flux flags. For Sora 2 video prompts, the structure is descriptive paragraph → action beats → camera direction → style tag.

---

## CATEGORY A — LinkedIn Carousel Slides

### The Visual Job
Typography-first slides that hold attention on their own AND contribute to a narrative arc. The image is NOT the hero — the words are. The image is atmosphere and pacing. Each carousel is 5-10 slides. Slide 1 is the hook slide. Slides 2-N are the argument. Final slide is the payoff + CTA.

### Visual Approach
- Dominant: Cathedral Black (`#0E0E0C`) background with Dawn Linen (`#F3EEE3`) text. This is the default.
- Alternate: Dawn Linen background with Cathedral Black text for slides that need breathing room.
- Atmospheric photo as a muted underlay (opacity 15-30%) to add texture without competing with type.
- Fraunces 900 for the hero statement on each slide.
- Ember Gold (`#C08A3E`) used ONLY for the one word per slide that needs emphasis.

### Prompt Template (Atmospheric Photo Underlay for Carousel Slides)

```
[subject/scene description], cinematic, masculine, restrained,
shot on Kodak Portra 400 film, shallow depth of field,
natural golden hour window light, 35mm film grain,
moody editorial atmosphere, desaturated earth tones,
ample negative space for text overlay, dark dominant background,
tonal range from black #0E0E0C to warm brown #3A2A1F,
editorial portrait style, New York Times magazine aesthetic
--ar 4:5 --style raw --v 7
```

### 3 Example Prompts (Copy-Paste Ready)

**Example 1 — "The 2 AM Founder" (Depletion Diaries carousel slide 1)**
```
A man in his late 30s sitting alone at a kitchen counter at 2 AM,
only the glow of a laptop screen lighting his face, the rest of the
kitchen in deep shadow, his hand holding his forehead, wedding ring
visible, shot from a 3/4 angle behind him so his expression is half-hidden,
cinematic, masculine, restrained, shot on Kodak Portra 400, 50mm lens,
shallow depth of field, low-key lighting, 35mm film grain, desaturated
earth tones, ample dark negative space above for text overlay,
editorial portrait, NYT magazine aesthetic
--ar 4:5 --style raw --v 7
```

**Example 2 — "The Empty Gym at Dawn" (Resurrection Chronicles carousel opener)**
```
An empty commercial gym at 5 AM, cold blue dawn light spilling through
industrial windows onto a single barbell on the floor, no people,
weight plates stacked in perfect rows, chalk dust hanging in a shaft
of light, wide environmental shot, cinematic, masculine, restrained,
shot on Hasselblad medium format, dawn light, volumetric light,
deep shadow in the foreground, ample negative space upper third
for text, moody editorial, tonal range black to warm brown,
Terrence Malick cinematography
--ar 4:5 --style raw --v 7
```

**Example 3 — "Empty Cathedral Pew" (Spiritual resurrection content, use sparingly)**
```
An empty stone cathedral pew at dawn, single shaft of golden light
cutting across the wooden seat from a high stained glass window,
dust motes visible in the light, no people, warm shadows, deeply
reverent mood, cinematic, masculine, restrained, shot on Leica Q2,
natural light only, film grain, tonal range warm brown #3A2A1F to
ember gold #C08A3E to Cathedral black, editorial, Monocle magazine
aesthetic, ample negative space left side for text overlay
--ar 4:5 --style raw --v 7
```

### Technical Specs
- **Aspect ratio**: 4:5 (LinkedIn carousel native — fills the mobile feed better than 1:1)
- **Output size**: 1080 × 1350 px minimum, 2160 × 2700 px preferred (2x retina)
- **File format**: PNG for final slides with text, JPG for raw photo underlays
- **Text overlay**: Done in Canva or Figma AFTER image generation. Prompts generate atmosphere only.
- **Max words per slide**: 25 (hook slide) / 40 (argument slide) / 15 (CTA slide)

### Common Failure Modes + Fixes

| Failure | Fix |
|---|---|
| Image is too busy — text can't breathe | Add "ample negative space upper/lower third" to prompt, use a tighter crop |
| Subject is looking at camera (breaks the voyeur/witness feel) | Add "3/4 angle behind subject" or "looking away from camera" |
| Too clean / too saturated | Add "desaturated earth tones, 35mm film grain, shot on Kodak Portra 400" |
| Stock-photo vibe | Add "editorial portrait, NYT magazine aesthetic, shallow depth of field" and specify a film stock |
| Wrong era (looks like 2018 stock photo) | Add a reference film/photographer: "Terrence Malick" / "Roger Deakins" / "Robert Frank" |
| Generated hands look broken | Crop them out. Hands below frame. Or use "hands hidden in pockets" |

---

## CATEGORY B — LinkedIn Single-Image Post

### The Visual Job
The single image attached to a standalone post. It is a *film still* — one frame from an imaginary movie that captures the emotional core of the post. Should work at a glance as someone scrolls past.

### Visual Approach
- Always feels like a screenshot from a prestige drama, not a stock photo.
- Single subject OR clearly composed environmental scene.
- Cooz's own photos (from Section 4) are the highest-quality version of this — AI is the fallback when his library is thin.

### Prompt Template

```
Cinematic film still, [subject], [action or state], [environment],
cinematic, masculine, restrained, [specific lighting setup],
shot on [film stock or camera], [lens length], shallow depth of field,
35mm film grain, editorial portrait, [specific mood keywords],
[specific reference aesthetic], tonal range Cathedral black #0E0E0C
to warm brown #3A2A1F to dawn linen #F3EEE3
--ar 3:2 --style raw --v 7
```

### 3 Example Prompts (Copy-Paste Ready)

**Example 1 — "Car in the Driveway" (the 30-second driveway story, LinkedIn hero image)**
```
Cinematic film still, a man in his late 30s sitting alone in a parked
pickup truck at dusk, hands on the steering wheel, staring at his own
closed garage door through the windshield, suburban driveway, warm
interior dashboard light, blue hour outside, the weight of the day
visible in his posture, cinematic, masculine, restrained, shot on
Arri Alexa with anamorphic lens, shallow depth of field, editorial
portrait, contemplative mood, Roger Deakins cinematography,
tonal range black to warm brown to amber, 35mm film grain
--ar 3:2 --style raw --v 7
```

**Example 2 — "Hands on the Barbell" (Resurrection Protocol illustration)**
```
Cinematic film still, close-up of a man's weathered hands gripping a
rough iron barbell on the gym floor, chalk dust on knuckles, single
wedding ring visible, wide-format low-angle shot, dawn light spilling
in from behind, deep shadow in the foreground, cinematic, masculine,
restrained, shot on Leica M11 with 50mm Summilux, Kodak Portra 400,
shallow depth of field, editorial, 35mm film grain, tonal range
warm brown to cathedral black, Terrence Malick aesthetic
--ar 3:2 --style raw --v 7
```

**Example 3 — "The Empty Chair at Dinner" (Witness voice illustration — his absence)**
```
Cinematic film still, an empty chair at a warmly lit family dinner
table at night, plates of half-eaten food, kids' half-finished drawings
on the side, one seat at the head of the table obviously empty and
still set, pulled back just slightly, shot from across the table,
cinematic, masculine, restrained, warm tungsten interior light,
shot on Arri Alexa, shallow depth of field on the empty chair,
bokeh on kitchen background, 35mm film grain, editorial,
NYT Sunday magazine aesthetic, melancholic, restrained, quiet
--ar 3:2 --style raw --v 7
```

### Technical Specs
- **Aspect ratio**: 3:2 (1.91:1 is LinkedIn's max — 3:2 gives a cleaner cinematic ratio that still fills the feed)
- **Output size**: 1800 × 1200 px minimum
- **File format**: JPG (smaller file = faster LinkedIn load)

### Common Failure Modes + Fixes

| Failure | Fix |
|---|---|
| Looks like a commercial, not a film | Remove any "bright" / "smiling" / "energetic" and replace with "contemplative, unguarded, honest" |
| Too symmetrical, too posed | Add "asymmetrical composition, candid moment, shot from behind or 3/4 angle" |
| Generic man-in-gym vibe | Add a specific narrative detail: "wedding ring visible" / "coffee cup on the bench" / "phone face-down" |
| Color palette off | Explicitly list hex colors: "tonal range #0E0E0C to #3A2A1F to #C08A3E" |

---

## CATEGORY C — YouTube Thumbnails

### The Visual Job
High-CTR thumbnails that function at a glance in a crowded feed. Cooz's face + one word + one visual element. **Dan Go's thumbnails are the reference** (muted, masculine, emotional) — NOT MrBeast yellow-and-red overload.

### Visual Approach
- Cooz's face is the hero (from his photo library, see Section 4). AI-generated "Cooz-like" faces are NOT allowed — this is the one category where real photography is non-negotiable.
- One word overlay in Fraunces 900, Dawn Linen `#F3EEE3`, with optional Ember Gold `#C08A3E` highlight.
- One visual element: a barbell, a chair, a garage door, a clock, a phone. Symbolic, not decorative.
- Background: atmospheric Soil Brown to Cathedral Black gradient OR a desaturated photo.

### The Dan Go Thumbnail Formula (Adapted for Cooz)

```
[Cooz face, emotional, looking off-camera or directly at viewer]
+ [1 high-contrast symbolic object]
+ [1 word in large Fraunces 900]
+ [Soil-to-black gradient background]
+ [Subtle film grain overlay]
```

### Prompt Template (For the Background + Symbolic Element Only — Cooz's face is composited in Canva/Figma)

```
YouTube thumbnail background plate, [symbolic object] centered with
ample space left or right for subject composite, cinematic, masculine,
restrained, dramatic chiaroscuro lighting, shot on Arri Alexa with
anamorphic lens, Cathedral black #0E0E0C to warm brown #3A2A1F
gradient background, 35mm film grain, single light source,
editorial, no people, high contrast, 16:9 aspect
--ar 16:9 --style raw --v 7
```

### 3 Example Prompts (Copy-Paste Ready)

**Example 1 — "Empty chair background plate" (for a "Running on Fumes" thumbnail)**
```
YouTube thumbnail background plate, an empty worn leather office chair
pushed back from a desk in a dark room, single warm desk lamp still on,
papers scattered, suggesting someone just got up, cinematic, masculine,
restrained, chiaroscuro lighting, shot on Arri Alexa anamorphic,
Cathedral black to warm brown gradient, 35mm film grain, high contrast,
ample negative space right side for subject composite, no people
--ar 16:9 --style raw --v 7
```

**Example 2 — "Single barbell on concrete" (for a "Stop the Bleeding" thumbnail)**
```
YouTube thumbnail background plate, a single heavy iron barbell lying
on a raw concrete floor in a dim warehouse gym, dramatic side light
cutting across the bar from the right, deep shadow left side,
cinematic, masculine, restrained, chiaroscuro, shot on anamorphic lens,
warm brown to black gradient, 35mm film grain, high contrast,
ample negative space left side for subject composite, no people
--ar 16:9 --style raw --v 7
```

**Example 3 — "Driveway + closed garage door at dusk"**
```
YouTube thumbnail background plate, a dark suburban driveway at blue
hour, pickup truck in the foreground facing a closed garage door,
single warm porch light above the garage, rest of the scene in deep
blue shadow, cinematic, masculine, restrained, dramatic contrast,
shot on Arri Alexa, 35mm film grain, Cathedral black to dusk blue
gradient, ample negative space upper right for subject composite,
no people, editorial
--ar 16:9 --style raw --v 7
```

### Text Overlay Rules for Thumbnails

- **Maximum 3 words**. One word is better. "DEPLETED." "FUMES." "RESURRECTED." "LISTEN."
- **Fraunces 900, all caps, letter-spacing `-0.02em`**, Dawn Linen or Ember Gold depending on background.
- Text fills 25-40% of the frame width. Not too big (tacky), not too small (unreadable).
- Text goes on the side opposite Cooz's face (right face → left text).
- Optional: a thin Ember Gold underline or colon separator for hierarchy.
- NEVER use arrows, circles around objects, or shocked-face emojis.

### Technical Specs
- **Aspect ratio**: 16:9
- **Output size**: 1920 × 1080 px (YouTube recommends 1280 × 720 min, but 1920 is retina-safe)
- **Max file size**: 2 MB (YouTube cap)
- **File format**: JPG

### Common Failure Modes + Fixes

| Failure | Fix |
|---|---|
| Too MrBeast (bright, loud) | Desaturate. Reference "Dan Go thumbnail style, muted, editorial, cinematic" in the prompt |
| Cooz's face looks AI-fake | Never generate Cooz's face. Composite a real photo in Canva over an AI background plate. |
| Can't read the word at small sizes | Use only 1 word. Fraunces 900. High contrast with background. Test at 320px wide preview. |
| Blends into feed | Add Ember Gold `#C08A3E` as the ONE accent color — a thin underline, a highlighted word, a lit object |

---

## CATEGORY D — Instagram Quote Cards

### The Visual Job
Typography-first cards where the quote IS the hero. The card stands alone OR chains with others in a carousel. The brand goal: when someone scrolls Cooz's Instagram grid, it should look like a single coherent zine or indie magazine, not a random content dump. **Max 3 quote-card templates** — consistency is the whole game.

### The 3 Approved Quote Card Templates

---

#### Template D1 — "The Stone" (Heavy Statement)

The flagship quote card. Use for the big I-led confessions and cut-through one-liners.

**Layout spec**:
```
+---------------------------------------------------+
|                                                   |
|                                                   |
|                                                   |
|  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   |
|  ┃ "Exhaustion isn't a                       ┃   |
|  ┃  discipline problem.                      ┃   |
|  ┃                                           ┃   |
|  ┃  It's a                                   ┃   |
|  ┃  fuel problem."                           ┃   |
|  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   |
|                                                   |
|                                                   |
|                                                   |
|  ─ COACH COOZ                                     |
|    THE RESURRECTION COACH                         |
|                                                   |
+---------------------------------------------------+
```

- **Background**: Cathedral Black `#0E0E0C` with a subtle Soil Brown `#3A2A1F` radial gradient bloom from top-left. Add a 5-8% grain overlay.
- **Quote text**: Fraunces 900, Dawn Linen `#F3EEE3`. Size calibrated so the quote fills ~55% of the card width. The ONE key word in the quote (e.g., "fuel," "discipline," "depleted") gets Ember Gold `#C08A3E`.
- **Attribution**: Syne/Space Grotesk 700 all caps, letter-spacing `0.1em`, Stone Gray `#5B5B55`. Bottom left, with an em-dash prefix.
- **Margin**: 10% on all sides. Never tight.

---

#### Template D2 — "The Cathedral Window" (Soft Confession)

Lighter-weight. Used for vulnerability-heavy Confession-voice content.

**Layout spec**:
```
+---------------------------------------------------+
|  [SOFT BACKGROUND PHOTO — golden hour light       |
|   through a window, heavily desaturated, 20%      |
|   opacity over Dawn Linen #F3EEE3 background]    |
|                                                   |
|  "For two years                                   |
|   I had a habit                                   |
|   nobody knew about."                             |
|                                                   |
|                                                   |
|                                                   |
|                                                   |
|  ─ COACH COOZ                                     |
|                                                   |
+---------------------------------------------------+
```

- **Background**: Dawn Linen `#F3EEE3` with a desaturated (20% opacity) cathedral-window photo overlay. Warm, glowing, quiet.
- **Quote text**: Fraunces 400 italic (softer, confessional), Cathedral Black `#0E0E0C`. Size 70% of Template D1 — this is the "whispered" card.
- **Attribution**: Syne 700 all caps, Stone Gray, bottom.
- **Key word emphasis**: NONE. This card is quiet. Don't accent.

---

#### Template D3 — "The Pull-Quote Sheet" (Multi-Quote Carousel)

For carouseling multiple quotes from the same post. Format is consistent so the carousel builds rhythm.

**Layout spec**:
```
+---------------------------------------------------+
|  Nº 01                                            |
|                                                   |
|                                                   |
|  "The men                                         |
|   sitting in driveways                            |
|   aren't undisciplined.                           |
|                                                   |
|   They're                                         |
|   DEPLETED."                                      |
|                                                   |
|                                                   |
|                                                   |
|  ─────────────────────                            |
|  THE RESURRECTION COACH                           |
+---------------------------------------------------+
```

- **Background**: Cathedral Black `#0E0E0C` solid with 5% grain.
- **Number**: Syne 700 all caps, Ember Gold `#C08A3E`, top left.
- **Quote**: Fraunces 700, Dawn Linen. The final emphasized word (DEPLETED, FUMES, LISTEN) gets 1.3x size and Ember Gold.
- **Bottom rule**: 1px Ember Gold horizontal rule + brand name in Syne.

### Technical Specs (All Quote Cards)
- **Aspect ratio**: 1:1 for Instagram feed cards, 4:5 for IG carousel (tallest allowed)
- **Output size**: 1080 × 1080 or 1080 × 1350 px
- **File format**: PNG
- **Grid consistency**: Alternate templates D1, D2, D3 across posts — never use only one. The grid reads as "one zine" when you rotate.

### Common Failure Modes + Fixes

| Failure | Fix |
|---|---|
| Card looks like a generic motivation meme | Confirm Fraunces is actually rendering (not Georgia fallback). Check the grain overlay is present. |
| Too many words | Cut. A quote card should be 5-15 words max. If it needs 30, it's a carousel slide, not a quote card. |
| Color is off | Check hex codes verbatim. `#0E0E0C` is NOT pure black — if the card looks flat, Cathedral Black probably collapsed to `#000000` |
| Key word emphasis looks tacky | Ember Gold only. Never yellow. Only ONE word per card gets emphasis. |
| Grid looks chaotic | Rotate the 3 templates in strict order (D1, D2, D3, D1, D2, D3...) for the first 30 days |

---

## CATEGORY E — Blog Post / Substack Header Images

### The Visual Job
Wide-format hero images that set the emotional tone of a longer piece. Screenshot-worthy — if someone screencaps the top of the blog post, the image alone should feel like it came from a design publication. This is where Cooz's brand earns its "premium" read.

### Visual Approach
- Fully cinematic environmental photography. Wider format (16:9 or 2:1).
- No text on the image itself — the blog title lives in HTML below/overlaid in the CMS. The image is atmosphere only.
- This is the category where AI image gen shines brightest — it's essentially mood-board-as-image.

### Prompt Template

```
Wide cinematic establishing shot, [environment or scene],
[single or no human subject], [time of day], [specific lighting],
cinematic, masculine, restrained, shot on Hasselblad medium format
or Arri Alexa, anamorphic lens, shallow depth of field on foreground,
35mm film grain, desaturated earth tones, tonal range from Cathedral
black #0E0E0C through Soil brown #3A2A1F to Dawn linen #F3EEE3,
Terrence Malick cinematography, editorial magazine aesthetic,
negative space left or right third for CMS text overlay
--ar 16:9 --style raw --v 7
```

### 3 Example Prompts (Copy-Paste Ready)

**Example 1 — "Dawn Gym Exterior" (for a "Stop the Bleeding" blog post)**
```
Wide cinematic establishing shot of a single-story warehouse gym at
5:30 AM, one window glowing warm from inside, empty parking lot,
the first blue light of dawn in the sky, morning mist on asphalt,
no people, cinematic, masculine, restrained, shot on Hasselblad
medium format, dawn light, 35mm film grain, desaturated earth tones,
tonal range Cathedral black to warm brown to dawn blue, editorial,
Terrence Malick aesthetic, ample negative space in upper sky for
blog title overlay
--ar 16:9 --style raw --v 7
```

**Example 2 — "Kitchen at 2 AM" (for the AI Brain Fry / 2 AM piece)**
```
Wide cinematic establishing shot of a dark suburban kitchen at 2 AM,
only the blue-white glow of an open laptop on the counter, the kitchen
in deep shadow, an abandoned half-empty glass of water, a phone face-down
beside the laptop, no people but their presence felt, cinematic,
masculine, restrained, shot on Arri Alexa with anamorphic lens,
shallow depth of field, 35mm film grain, chiaroscuro, tonal range
from Cathedral black through warm brown to laptop-screen cold blue,
Roger Deakins cinematography, editorial magazine aesthetic
--ar 16:9 --style raw --v 7
```

**Example 3 — "Empty Cathedral at Dawn" (for Resurrection-themed longform)**
```
Wide cinematic establishing shot of an empty stone cathedral interior
at dawn, a single massive shaft of golden light cutting from a high
stained glass window across empty wooden pews, dust motes visible in
the light, no people, reverent stillness, cinematic, masculine,
restrained, shot on Hasselblad medium format, natural light only,
warm brown to ember gold tonal range, 35mm film grain, editorial,
Monocle magazine aesthetic, ample negative space upper right for
blog title overlay
--ar 16:9 --style raw --v 7
```

### Technical Specs
- **Aspect ratio**: 16:9 primary, 2:1 for Substack native header
- **Output size**: 2400 × 1350 px minimum (retina-safe)
- **File format**: JPG, 85% quality (smaller file for web load)
- **Alt text**: Always include a 1-sentence plain-language description for accessibility

### Common Failure Modes + Fixes

| Failure | Fix |
|---|---|
| Too busy, too many elements | Simplify. Remove a person. Remove a third of the objects. Emptiness is the brand. |
| Reads as generic stock | Add a specific narrative detail that implies a story (half-empty glass, pushed-back chair, open book) |
| Color is too saturated | Add "desaturated earth tones, muted color palette" and specify the hex range |
| Wrong time of day | Be explicit: "5:30 AM, first blue light of dawn" not "morning" |

---

## CATEGORY F — Podcast Cover Art + Episode Art

### The Visual Job
Two jobs: (1) ONE static podcast cover that never changes (Apple/Spotify listing), and (2) per-episode episode art that stays on-brand while signaling the specific episode. Consistency is everything — the podcast cover is seen 10,000x more than any individual episode, so it has to carry the brand weight alone.

### F1 — The Permanent Podcast Cover (Design Once)

**Concept**: A single stylized portrait of Cooz + the brand mark. Made once, lives forever.

**Layout spec**:
```
+---------------------------------------------------+
|                                                   |
|                                                   |
|  ┌─────────────────────┐                          |
|  │                     │                          |
|  │   [COOZ PORTRAIT    │                          |
|  │    3/4 PROFILE,     │      THE                 |
|  │    LOOKING OFF TO   │      RESURRECTION       |
|  │    HIS RIGHT,       │      COACH              |
|  │    CATHEDRAL BLACK  │                         |
|  │    BACKGROUND,      │      WITH COACH COOZ    |
|  │    SIDE LIT]        │                         |
|  │                     │                          |
|  └─────────────────────┘                          |
|                                                   |
|  ─────────────────                                |
|                                                   |
+---------------------------------------------------+
```

- **Portrait**: Cooz in a 3/4 profile, 1 light source from the right (cathedral window vibe), Cathedral Black background. This is a REAL photo by a real photographer — spend the money here. This photo lives forever.
- **Background**: Cathedral Black `#0E0E0C` with very subtle Soil Brown bloom.
- **"THE RESURRECTION COACH"**: Fraunces 900, Dawn Linen, stacked three lines.
- **"WITH COACH COOZ"**: Syne 700 all caps, Ember Gold, smaller, below the wordmark.
- **Decorative rule**: 1px Ember Gold horizontal rule below the byline.

### F2 — Per-Episode Episode Art (Repeatable Template)

**Concept**: Same cover frame, different episode image. The frame (wordmark + episode number) stays identical. The image inside the frame changes per episode.

**Layout spec**:
```
+---------------------------------------------------+
|  THE RESURRECTION COACH       EP. 07              |
|  ─────────────────────        ─────               |
|                                                   |
|  ┌──────────────────────────────────────────┐    |
|  │                                          │    |
|  │      [EPISODE-SPECIFIC IMAGE             │    |
|  │       — single cinematic photo           │    |
|  │       matching episode theme]            │    |
|  │                                          │    |
|  │                                          │    |
|  └──────────────────────────────────────────┘    |
|                                                   |
|  THE 2 AM SLACK CHECK                             |
|                                                   |
|  WITH COACH COOZ                                  |
+---------------------------------------------------+
```

- **Top wordmark**: Syne 700 all caps, Dawn Linen.
- **Episode number**: Ember Gold, same font.
- **Episode image**: Framed inside the card. Uses prompts from Category B (LinkedIn single-image) style.
- **Episode title**: Fraunces 700, Dawn Linen, under the image.
- **Background**: Cathedral Black.

### Prompt Template (for the episode-specific image inside the frame)

Use the Category B (LinkedIn Single-Image Post) prompt template, but swap `--ar 3:2` for `--ar 1:1` to fit the podcast art square.

### 3 Example Prompts (Copy-Paste Ready)

**Episode 1 — "The Thirty Seconds Nobody Talks About"**
```
Cinematic film still, a man in his late 30s sitting alone in a parked
pickup truck in a suburban driveway at dusk, both hands on the steering
wheel, staring forward at a closed garage door, warm interior dashboard
light illuminating his weathered face, blue hour outside, the weight
of the day visible in his shoulders, cinematic, masculine, restrained,
shot on Arri Alexa anamorphic, shallow depth of field, 35mm film grain,
contemplative, Roger Deakins aesthetic, tonal range Cathedral black
to warm amber
--ar 1:1 --style raw --v 7
```

**Episode 2 — "Stop the Bleeding" (body-first thesis episode)**
```
Cinematic film still, close-up of a single heavy iron barbell lying
on a raw concrete warehouse gym floor, chalk dust in a shaft of
morning light from a high window, no people, deep shadow dominating
the frame, cinematic, masculine, restrained, shot on Hasselblad medium
format, dawn light, 35mm film grain, chiaroscuro, tonal range warm
brown #3A2A1F to Cathedral black #0E0E0C, Terrence Malick aesthetic
--ar 1:1 --style raw --v 7
```

**Episode 3 — "Bryan Johnson's $2M and Your $0" (contrarian episode)**
```
Cinematic film still, a family dinner table warmly lit from above,
the man's seat at the head of the table empty but visibly pulled out
as if just abandoned, his plate half-eaten, a kid's drawing on the side,
warm tungsten light, shot from across the table, cinematic, masculine,
restrained, shot on Arri Alexa, shallow depth of field on the empty
chair, 35mm film grain, tonal range tungsten warm to Cathedral black,
editorial, melancholic, quiet
--ar 1:1 --style raw --v 7
```

### Technical Specs
- **Podcast cover**: 3000 × 3000 px (Apple Podcasts minimum 1400 × 1400, recommended 3000)
- **Episode art**: 3000 × 3000 px, JPG
- **File format**: JPG for episode art, PNG for the permanent cover
- **Color mode**: RGB

### Common Failure Modes + Fixes

| Failure | Fix |
|---|---|
| Cooz's face on the permanent cover looks AI-generated | Pay a real photographer for the permanent cover. This is the $500-2000 spend. Non-negotiable. |
| Episode art feels inconsistent across episodes | Lock the frame (wordmark, episode number position, title placement). Only the inner image changes. |
| Square format cramps the episode scene | Use environmental shots (no people) or very tight crops for square format — wide scenes don't work at 1:1 |

---

# SECTION 3 — THE POST-TYPE VISUAL DEFAULTS

Quick-reference lookup. When Cooz is producing a post and doesn't want to think about the visual, default to this table.

## The Content Voice Rotation (from `strategic-dossier.md` §6.3)

The 4-voice rotation from the dossier maps 1:1 to a default visual approach:

| Voice | % of Mix | Default Visual | Category | Prompt Reference |
|---|---|---|---|---|
| **Confession (40%)** | "I had this habit for two years..." | Cinematic solo shot of Cooz OR environmental scene (car, kitchen, driveway). Dim lighting, introspective. | Category B | Section 2B Example 1 (Car in Driveway) |
| **Reframe (25%)** | "Most men think discipline is missing. It's not." | Quote card D1 (Stone). Heavy statement, single word in Ember Gold. | Category D | Section 2D Template D1 |
| **Witness (20%)** | "I know a guy. Built something real..." | Environmental scene of the absent protagonist — empty chair, empty kitchen, empty driveway. No people. | Category B | Section 2B Example 3 (Empty Chair at Dinner) |
| **Proof (15%)** | "Brian came to me 30 lbs heavier..." | Before/after photo OR client environmental shot. Restrained. No mirror selfies. | Category B (photo) | Use client's real photo. AI only for abstracted b-roll. |

## The Cooz Content Bucket Defaults (Inferred — Create if Missing)

Since `02-content-buckets-architecture.md` doesn't exist yet, here are the five buckets implied by the strategic dossier + week 1 brief, with visual defaults:

| Content Bucket | Voice Mix | Default Visual | Category | Prompt Reference |
|---|---|---|---|---|
| **Depletion Diaries** (Confession-heavy, 2 AM stories) | Confession 80% / Reframe 20% | Cinematic solo shot, dim/low-key lighting, introspective, environmental | Category B | §2B Example 1 |
| **Resurrection Chronicles** (Proof + transformation stories) | Proof 60% / Witness 40% | Environmental gym shot, dawn light, OR client photo with restraint | Category B, Category E | §2B Example 2, §2E Example 1 |
| **The Contrarian File** (Reframes: Huberman, Bryan Johnson, Liver King) | Reframe 70% / Confession 30% | Quote card D1 (Stone) with single Ember Gold word | Category D | §2D Template D1 |
| **Witness Posts** (I know a guy... the universal founder story) | Witness 70% / Reframe 30% | Environmental scene of absent protagonist (empty chair, empty driveway, empty desk) | Category B | §2B Example 3 |
| **Cultural Moments** (Dorsey layoffs, AI Brain Fry, news-jacking) | Reframe 50% / Confession 50% | Cinematic single-image post referencing the cultural moment abstractly | Category B, Category E | §2B Example 1, §2E Example 2 |

## Channel-Specific Default Ratios

| Channel | Carousel | Single-Image | Quote Card | Video Still |
|---|---|---|---|---|
| **LinkedIn** | 40% | 40% | 20% | 0% |
| **Instagram** | 30% | 10% | 50% | 10% (Reels covers) |
| **YouTube** | 0% | 0% | 0% | 100% (thumbnails) |
| **Substack** | 0% | 100% (header) | 0% | 0% |
| **Podcast** | 0% | 0% | 0% | 100% (episode art) |

---

# SECTION 4 — COOZ-SPECIFIC IMAGERY (Personal Photo Direction)

Cooz must build a personal photo library. AI image generation cannot replace this — his face IS the brand, and AI-generated "Cooz-likes" are uncanny and cheapen everything. This section is the playbook for building that library the right way.

## 4.1 The Five Core Photo Shoots Cooz Needs (In Priority Order)

### Shoot #1 — "The Empty Gym at Dawn" (Highest Priority — Hero Library)
**Budget**: Premium — hire a real photographer, $400-800. This is the one shoot that MUST be pro.
**Duration**: 90 minutes
**Location**: Empty commercial gym at 5:30-7:00 AM (golden hour through the windows)
**Wardrobe**: Dark gray or black fitted tee, dark joggers or shorts, weathered sneakers. NO branded gear. NO sleeveless. Watch and wedding ring visible.
**Shot list** (the photographer must capture all 12):

1. **Hands on barbell**, tight crop, shot from the side, window light rim-lighting the bar
2. **Back to camera**, walking into the gym under doorway light, wide environmental shot
3. **Eye contact straight to lens**, from waist up, standing in front of a wall, chiaroscuro side light
4. **3/4 profile looking off camera** to the right (for podcast cover art — this is THE shot)
5. **Candid loading plates onto a bar**, no posed eye contact, shot from 15 feet away
6. **Sitting on a bench**, elbows on knees, head down, staring at the floor (depletion mood)
7. **Leaning against a wall**, arms crossed, looking out a window, from 3/4 behind
8. **Writing in a small notebook** at a gym bench, hands in focus, face out of focus in background
9. **Holding a worn cup of coffee**, standing, shot from below, window light behind him
10. **Wide establishing shot** — him small in frame, gym large around him, dawn light filling the space
11. **Tight face crop** — jawline, beard, the beginning of gray, side-lit (for thumbnails)
12. **Walking out the door** at the end, backlit by rising sun, silhouette + warm fill

**Deliverables**: 60-100 edited images in the Cathedral Black / Soil Brown / Dawn Linen palette. Desaturated earth tones, 35mm film-style edit (no HDR, no Instagram filter).

### Shoot #2 — "The Kitchen / Home Before Dawn" (High Priority)
**Budget**: Medium — $200-400 OR iPhone + tripod + one helper for golden hour
**Duration**: 60 minutes
**Location**: Cooz's own kitchen, 5:30-6:30 AM
**Wardrobe**: Dark hoodie or robe, unshaven, no product in hair — the honest version
**Shot list**:

1. **Hands holding a coffee mug** at the counter, steam rising, tight crop
2. **Back to camera** staring out a kitchen window at pre-dawn
3. **Seated at the kitchen table** with a notebook, morning light coming in from the left
4. **Opening the fridge** — shot from inside the fridge looking out, fridge light on his face
5. **Hands on the counter**, head down, the "weight of the day hasn't started" pose

### Shoot #3 — "The Driveway / Parking Lot" (Medium Priority — but critical for THE 2 AM content)
**Budget**: Low — iPhone + natural light, 30 min shoot
**Duration**: 30 minutes (blue hour, 8:00-8:30 PM)
**Location**: Cooz's own driveway or a quiet parking lot
**Wardrobe**: Casual work clothes — button-down, no tie, slightly rumpled
**Shot list**:

1. **Sitting in the driver's seat**, hands on the wheel, through the windshield
2. **From outside the car** through the driver's side window, phone in hand, face lit by the phone
3. **Leaning on the car** facing away, looking at a closed garage door
4. **Walking toward a front door** at dusk, shot from 20 feet behind

### Shoot #4 — "The Client Session" (Medium Priority — for Proof content)
**Budget**: Low — iPhone, natural light, ongoing across real sessions (with client consent)
**Duration**: Captured over time during actual coaching sessions
**Wardrobe**: Same as Shoot #1 — this is the coach-at-work library
**Shot list**:

1. **Coaching from the side**, client in focus foreground, Cooz in supportive-guide posture in background
2. **Hands adjusting a client's form** (never the client's face — anonymity preserved)
3. **Cooz watching a client**, arms crossed, attentive, over-the-shoulder shot
4. **Post-session conversation** at a bench, both leaning in, natural light

### Shoot #5 — "The Quiet Moments" (Lowest Priority — for spiritual resurrection content)
**Budget**: Low — iPhone
**Duration**: Opportunistic, 10-20 minutes at a time
**Location**: A quiet church, a park bench at dawn, a library, a drive
**Wardrobe**: Everyday Cooz, unstyled
**Shot list**:

1. **Sitting in an empty pew** at a quiet church, back of head or 3/4
2. **Walking a trail** at dawn, shot from behind
3. **Reading a book** in a quiet space, hands on the page, face half in shadow

## 4.2 Clothing & Styling Guidance (The Cooz Wardrobe)

### The Uniform (Always on-brand)
- Dark gray, black, or charcoal fitted tees (Buck Mason, Flint & Tinder, or plain Hanes)
- Dark joggers, utility pants, or raw denim
- Weathered boots, dark sneakers, or white low-tops (no logos)
- Watch (mechanical, masculine — not smartwatch on camera)
- Wedding ring (never remove — it IS the brand)
- Beard, trimmed but not shaved

### The Off-Duty (For confessional / vulnerable content)
- Hoodies (dark, unbranded)
- Henleys
- Worn flannels (for cooler-weather shoots)
- No product in hair — the honest version

### What NEVER to wear
- Branded gym gear (Gymshark, Alphalete, etc.) — reads as influencer
- Sleeveless anything — reads as bro
- Bright colors (red, yellow, neon) — breaks the palette
- Suits or ties — breaks the founder-peer trust
- Logos of any kind — unless his own future brand merch

## 4.3 Locations That Fit The Brand

**YES**:
- Empty commercial gym at dawn
- His own kitchen, unstyled
- A suburban driveway
- A quiet library
- A church, empty
- A forest trail at dawn
- A parking lot at blue hour
- A coffee shop before it opens (with permission)

**NO**:
- Fancy restaurants (reads as wealth-LARP)
- City skylines at night (founder-cliché)
- Gym selfies in the mirror
- Beach / vacation settings
- "Moody warehouse with graffiti" (Instagram coach trope)
- Hotel rooms
- Airport lounges / business-travel tropes

## 4.4 iPhone vs. Paid Photographer Decision Tree

**Pay a photographer ($400-800) for**:
- Shoot #1 (Empty Gym at Dawn) — THE hero library
- The permanent podcast cover portrait (F1) — this shot lives forever
- Any shoot intended for the website hero / "about" page

**Use iPhone + natural light for**:
- All other shoots (Kitchen, Driveway, Client, Quiet Moments)
- Day-to-day content capture
- Opportunistic moments

**iPhone shoot settings**:
- Portrait mode OFF (fake bokeh ruins the cinematic feel)
- Raw/ProRaw if available
- Never zoom — physically move
- Natural light only — never built-in flash
- Golden hour (30 min after sunrise / before sunset) or blue hour (30 min after sunset)
- Edit in Darkroom or VSCO — preset: desaturated, shadows lifted slightly, highlights rolled off, grain added

## 4.5 What NOT To Do (Photo Anti-Patterns)

- **Gym mirror selfies** — the single fastest way to destroy a premium brand
- **Front-facing transformation shots** (flexing in mirror) — use side profile or environmental
- **"Coach pointing at camera"** — every other fitness coach, instantly cheap
- **Overly-produced lifestyle photography** (sunglasses, glass of whiskey, watch close-up) — reads as hustle-influencer
- **Kids' faces** — never publish. Their backs or silhouettes only. Protect.
- **Wife's face without explicit written permission** — same rule
- **Any photo that shows him smiling broadly with teeth** — not on brand. The brand is quiet intensity, half-smiles, closed-mouth weight.
- **Filters** — VSCO or Darkroom natural edits only. No Instagram presets.

---

# SECTION 5 — QUICK-START VISUAL PROMPTS FOR WEEK 1

10 ready-to-use prompts matched to the Week 1 Creative Brief topics. Copy-paste-ready. Each includes the aspect ratio and mood keywords pre-loaded. Feed directly into Midjourney v7, Flux 1.1 Pro, or Sora 2 (for video prompts).

## Week 1 Topics (from `week-1-creative-brief.md`)
1. **AI Brain Fry** (Axios, April 4) — "founders as collateral"
2. **Jack Dorsey layoffs** — "you can't fire 4,000 people"
3. **Bryan Johnson Immortals** — "$2M vs. $0 contrast"
4. **The 2 AM Slack Check** (primary voice memo for Week 1)

---

### PROMPT 1 — "The 2 AM Slack Check" (Primary Week 1 LinkedIn hero image)

**Use for**: LinkedIn single-image post + Substack blog header + episode art
**Category**: B + E + F

```
Cinematic film still, a man in his late 30s standing alone in a dark
suburban kitchen at 2 AM, only the blue-white glow of an open laptop
on the granite counter lighting his face, phone in his hand, the rest
of the kitchen in deep shadow, wedding ring visible, his posture
exhausted, head slightly tilted forward, cinematic, masculine,
restrained, shot on Arri Alexa with anamorphic lens, shallow depth
of field, chiaroscuro lighting, 35mm film grain, tonal range from
Cathedral black #0E0E0C through warm brown #3A2A1F to cold laptop
blue, Roger Deakins cinematography, editorial NYT magazine aesthetic,
ample negative space upper third for text overlay
--ar 4:5 --style raw --v 7
```

---

### PROMPT 2 — "Empty Kitchen 2 AM" (No-subject version, safer + more universal)

**Use for**: Substack blog header, LinkedIn carousel slide, podcast episode art
**Category**: A + E + F

```
Wide cinematic establishing shot of a dark suburban kitchen at 2 AM,
only the blue-white glow of an open laptop on the counter, the kitchen
in deep shadow, an abandoned half-empty glass of water beside the
laptop, a phone face-down, kid's crayon drawing on the fridge barely
visible in ambient light, no people but their presence felt, cinematic,
masculine, restrained, shot on Arri Alexa anamorphic, shallow depth
of field, 35mm film grain, chiaroscuro, tonal range Cathedral black
through warm brown to cold blue, Roger Deakins aesthetic, editorial,
ample negative space upper left for blog title overlay
--ar 16:9 --style raw --v 7
```

---

### PROMPT 3 — "Dorsey Layoffs / Empty Office" (Cultural Moment — Dorsey)

**Use for**: LinkedIn single-image post on the Dorsey layoffs angle
**Category**: B

```
Cinematic film still, an empty modern office at night, rows of empty
desks, monitors dark, one chair pulled away and abandoned, emergency
exit sign casting a warm amber glow, cold blue window light from outside,
a single abandoned coffee cup still on a desk, no people, the weight
of absence, cinematic, masculine, restrained, shot on Arri Alexa with
anamorphic lens, shallow depth of field, chiaroscuro, 35mm film grain,
tonal range Cathedral black #0E0E0C through warm amber to cold blue,
editorial, melancholic, Roger Deakins aesthetic
--ar 3:2 --style raw --v 7
```

---

### PROMPT 4 — "Bryan Johnson Contrast / The Family Dinner Table" (Cultural Moment — Bryan Johnson)

**Use for**: LinkedIn single-image post contrasting $2M Bryan Johnson vs. $0 family dinner
**Category**: B

```
Cinematic film still, a warmly lit family dinner table at night, warm
tungsten chandelier above, four plates set with half-eaten meals, kids'
crayon drawings visible on the side, one chair at the head of the table
obviously empty and pushed back slightly, a folded napkin left on the
plate, shot from across the table at eye level with the empty chair in
soft focus, cinematic, masculine, restrained, shot on Arri Alexa,
shallow depth of field, 35mm film grain, warm tungsten tonal range
with deep shadow falloff, editorial NYT Sunday magazine aesthetic,
melancholic, quiet, honest
--ar 3:2 --style raw --v 7
```

---

### PROMPT 5 — "AI Brain Fry / The Slot Machine Hand" (Cultural Moment — AI Brain Fry)

**Use for**: LinkedIn carousel slide 1 hook OR Instagram quote card underlay
**Category**: A + D

```
Close-up cinematic film still, a man's weathered hand with a wedding
ring resting on a MacBook trackpad at 2 AM, blue laptop screen light
illuminating just the hand, the rest of the desk in deep shadow,
tension visible in the fingers, slight tremor suggested, a coffee cup
blurred in the background, cinematic, masculine, restrained, shot on
Leica Q2 with 50mm lens, shallow depth of field, chiaroscuro, 35mm
film grain, tonal range Cathedral black through warm brown to cold
screen blue, editorial, macro portrait aesthetic
--ar 4:5 --style raw --v 7
```

---

### PROMPT 6 — "The Driveway at Dusk" (Week 1 alternate — the driveway story)

**Use for**: Blog header + LinkedIn single image + podcast episode art
**Category**: B + E + F

```
Cinematic film still, a man in his late 30s sitting alone in a parked
pickup truck in a suburban driveway at dusk, both hands on the steering
wheel, staring forward at a closed garage door, warm interior dashboard
light illuminating his face from below, blue hour sky outside, porch
light just visible above the garage, the weight of the day visible in
his shoulders, cinematic, masculine, restrained, shot on Arri Alexa
anamorphic, shallow depth of field on him, soft focus on the garage,
35mm film grain, tonal range Cathedral black through warm amber to
dusk blue, Roger Deakins aesthetic, contemplative, unguarded
--ar 3:2 --style raw --v 7
```

---

### PROMPT 7 — "Stone Quote Card Underlay — The Dark Cathedral" (For Template D1 backgrounds)

**Use for**: Atmospheric underlay for Instagram quote cards
**Category**: D (Template D1)

```
Atmospheric cinematic texture background, stone cathedral interior wall
in deep shadow with a single shaft of golden hour light cutting diagonally
from upper right, dust motes visible in the light, no subject, heavy
negative space, rough stone texture, cinematic, masculine, restrained,
shot on Hasselblad medium format, low-key lighting, 35mm film grain,
tonal range Cathedral black #0E0E0C through warm brown #3A2A1F to
ember gold #C08A3E, Monocle magazine aesthetic, ample negative space
center for text overlay, reverent, quiet
--ar 1:1 --style raw --v 7
```

---

### PROMPT 8 — "Empty Gym at Dawn" (Week 1 YouTube thumbnail background plate + Substack header)

**Use for**: YouTube thumbnail background + Substack blog header for "Stop the Bleeding" piece
**Category**: C + E

```
Wide cinematic establishing shot, interior of an empty commercial gym
at 5:30 AM, cold blue dawn light spilling through industrial windows,
a single heavy iron barbell on the rubber floor, weight plates stacked
in perfect rows in the background, chalk dust hanging in a visible
shaft of light, no people, deep shadow in the foreground, cinematic,
masculine, restrained, shot on Hasselblad medium format, dawn light,
volumetric light through windows, 35mm film grain, tonal range
Cathedral black through warm brown to cold dawn blue, Terrence Malick
aesthetic, ample negative space right side for text overlay
--ar 16:9 --style raw --v 7
```

---

### PROMPT 9 — "Hands on Barbell Macro" (Proof / Resurrection Chronicles hero)

**Use for**: LinkedIn single-image for Proof-voice content, or quote card underlay
**Category**: B + D

```
Close-up cinematic film still, a man's weathered hands gripping a
rough iron barbell on the gym floor, chalk dust on the knuckles,
single wedding ring visible, veins and tendons clear, wide low-angle
shot, dawn light rim-lighting the bar from behind, deep shadow
foreground, cinematic, masculine, restrained, shot on Leica M11
with 50mm Summilux, Kodak Portra 400 film stock, shallow depth of
field, 35mm film grain, tonal range warm brown #3A2A1F to Cathedral
black #0E0E0C with ember gold #C08A3E highlights, Terrence Malick
aesthetic, tactile, honest
--ar 3:2 --style raw --v 7
```

---

### PROMPT 10 — "Sora 2 Video: The 30-Second Stare" (Video B-roll for Reels or YouTube Shorts)

**Use for**: Instagram Reels cover / YouTube Short / podcast clip visual
**Category**: Video (Sora 2 format)

```
A cinematic 8-second video clip, static camera mounted on a tripod,
shooting through the windshield of a parked pickup truck at dusk in
a suburban driveway. A man in his late 30s sits in the driver's seat,
both hands on the wheel, staring forward at a closed garage door.
He doesn't move for 6 seconds. Then, slowly, his head tilts just
slightly forward as he exhales. Camera does not move. Warm dashboard
light illuminates his face from below. Blue hour sky outside. Porch
light just visible above the garage.

Style: cinematic, masculine, restrained, shot on Arri Alexa with
anamorphic lens, shallow depth of field, 35mm film grain, chiaroscuro
lighting, Roger Deakins cinematography, tonal range Cathedral black
through warm amber to dusk blue, editorial, no music, no dialogue,
ambient suburban soundscape only

Aspect ratio: 9:16 vertical for Reels / Shorts
Duration: 8 seconds
```

---

## Week 1 Visual Workflow (How To Actually Use These)

1. **Monday**: Cooz records the Week 1 voice memo (Question A — the 2 AM Slack Check).
2. **Tuesday**: Farrice runs the flywheel. While the content draft is being generated, run Prompts 1, 2, 5, and 10 in parallel on Midjourney + Sora. Generate 4 variants of each.
3. **Wednesday AM**: Review the 16 outputs. Kill anything on the No-Fly List (Section 1.5). Pick the top 4.
4. **Wednesday post**: LinkedIn single-image post (Prompt 1 or 6) + carousel (Prompt 2 or 5 as underlay for slides).
5. **Thursday blog**: Substack header (Prompt 2 or 8).
6. **Friday podcast**: Episode art (use Category F template + Prompt 1/6 for the inner image).
7. **Saturday YouTube**: Thumbnail (Prompt 8 background + composited Cooz photo + 1-word Fraunces overlay).
8. **Sunday Instagram**: Quote card (Template D1 with Prompt 7 underlay + pull-quote from Wednesday LinkedIn post).

**One voice memo → 8 pieces of visual content.** That's the flywheel applied to visuals.

---

# SECTION 6 — THE FALLBACK WHEN AI IMAGE GEN FAILS

AI image generation produces garbage ~30% of the time. Plan for it. Here's the escalation ladder when a generated image fails.

## Fallback Tier 1 — Regenerate With Fixes (5 min)

Most "failures" are prompt failures. Before giving up:
1. **Check against Section 1.5 No-Fly List** — is this a brand violation or a technical failure?
2. **Run the Failure Mode + Fix table** for the relevant category (Section 2A-F)
3. **Re-roll 4 variants** with a tweaked prompt (add specificity, remove a competing element)
4. **Switch models** — if Midjourney fails, try Flux 1.1 Pro. If Flux fails, try Sora for stills.

**Budget**: 2 regeneration rounds. If Round 3 is still garbage, escalate to Tier 2.

---

## Fallback Tier 2 — Cooz's Own Photo Library (10 min)

Go to Cooz's Section 4 library. Pick a photo that matches the content emotional register.

**Rules**:
- Apply the brand-consistent edit preset (desaturated, lifted shadows, 35mm grain)
- Crop to the target aspect ratio
- Add text overlay in Canva or Figma using the brand fonts

**This is often BETTER than AI**. Cooz's real photos have what AI cannot fake: honesty.

---

## Fallback Tier 3 — Curated Stock (15 min)

When the library is thin and AI is failing, hit curated stock. Only use:

### Approved Stock Sources (In Priority Order)
1. **Unsplash** — [unsplash.com](https://unsplash.com) (free, best curation)
2. **Pexels** — [pexels.com](https://pexels.com) (free, slightly lower quality)
3. **Stocksy** — [stocksy.com](https://stocksy.com) (paid, but high-end editorial — $15-50/image)

### Approved Unsplash Search Terms (Pre-Validated to Stay On-Brand)

For **Depletion / 2 AM / exhaustion content**:
- `"man kitchen night"`
- `"laptop dark room"`
- `"empty office late"`
- `"blue hour driveway"`
- `"shadows window"`

For **Resurrection / gym / dawn content**:
- `"empty gym morning"`
- `"barbell concrete"`
- `"dumbbells dawn light"`
- `"empty warehouse gym"`
- `"weight plates shadows"`

For **Witness / environmental scenes**:
- `"empty chair dinner"`
- `"suburban house dusk"`
- `"parking lot evening"`
- `"pickup truck driveway"`

For **Spiritual / resurrection**:
- `"empty church morning"`
- `"cathedral light"`
- `"stone wall shadow"`
- `"dust motes light"`
- `"forest trail dawn"`

### Stock Photo Rules
- **Always** filter to landscape (for single-image) or portrait (for quote cards)
- **Always** prefer desaturated, moody shots over bright ones
- **Always** check the image doesn't have identifiable logos or brand trademarks
- **Never** use Unsplash's "Trending" category — it's full of Instagram cliches
- **Never** use images that clearly appear in other LinkedIn posts (they get stale fast)
- **Always** apply the brand edit preset after download

### Approved Unsplash Photographers to Follow for Constant Supply
- **Nathan Dumlao** — moody editorial portraits
- **Alex McCarthy** — empty gyms, industrial spaces
- **Annie Spratt** — domestic interiors, honest light
- **Anthony Tran** — low-key male portraits
- **Alex Iby** — cinematic suburban Americana

---

## Fallback Tier 4 — Typographic-Only Card (5 min)

When NOTHING visual is working, default to a pure-type Quote Card Template D1 (Section 2D).

**Why this works**: The brand's fonts and colors are strong enough that a pure type card is always on-brand. A card with zero image and perfect Fraunces typography is better than a weak AI image.

**Execution**:
1. Open Canva or Figma
2. Use a pre-built D1 template (create one master, duplicate per use)
3. Drop the quote in Fraunces 900, Cathedral Black background
4. One word in Ember Gold
5. Export

**Time to ship**: 3-5 minutes. This should be the 30% fallback, not the default.

---

## Fallback Tier 5 — Skip The Image Entirely (Text-Only Post)

For LinkedIn specifically, there are moments when the text is so strong that an image dilutes it. The fallback is to ship the post with no image at all.

### When Text-Only Is Correct
- The post is 40 words or less, a single sharp statement (Sheedy's "Pay attention to what you feed" hit 19,878 likes with a 12-word caption + one video — proof that brevity beats imagery)
- The post is a confession where an image would feel like a distraction
- You're out of time and the post is scheduled
- You have a hot take on a cultural moment that needs to ship NOW before the moment cools

### When Text-Only Is WRONG
- Any blog post (always needs a header)
- Any podcast episode (always needs episode art)
- Any YouTube video (always needs a thumbnail)
- Any Instagram post (the platform is visual — never text-only there)

### LinkedIn Text-Only Format Notes
- Break paragraphs aggressively (LinkedIn's line-break engagement trick)
- Use a 1-sentence hook on line 1
- Use white space as visual hierarchy
- Optional: start with an em-dash `—` or a bullet `•` as a visual anchor

---

## The Decision Tree (Visual Escalation Ladder)

```
START: Need a visual for content piece

├─ Does Cooz have a real photo that fits from Section 4 library?
│   ├─ YES → Use it. Apply edit preset. (Fastest, best)
│   └─ NO → Try AI generation
│       │
│       ├─ Generate 4 variants with Category prompt
│       │   ├─ Any hit? → Ship it
│       │   └─ All miss? → Regenerate with fix table (1 more round)
│       │       ├─ Hit? → Ship it
│       │       └─ Miss? → Switch model (Flux/Sora), 1 more round
│       │           ├─ Hit? → Ship it
│       │           └─ Miss? → Go to Stock
│       │
│       ├─ Search Unsplash with approved keywords
│       │   ├─ Good match found? → Apply edit preset, ship it
│       │   └─ Nothing fits? → Go to Type-Only Card
│       │
│       ├─ Pure type Quote Card (Template D1)
│       │   └─ Ship it. Always works.
│       │
│       └─ OR, for LinkedIn only: text-only post, no visual
```

**Time budget for visual production per post**: 15 minutes max. If you're spending more than 15 min, something is wrong — escalate to the next fallback tier.

---

# APPENDIX — QUICK REFERENCE CARDS

## A — The Brand Color Hex Codes (Memorize These)

```
Cathedral Black   #0E0E0C   (primary dark)
Dawn Linen        #F3EEE3   (primary light)
Soil Brown        #3A2A1F   (secondary warm)
Stone Gray        #5B5B55   (secondary cool)
Ember Gold        #C08A3E   (accent — use sparingly)
Blood Rust        #6B2B1D   (rare emotional-weight accent)
```

## B — The Brand Fonts (Google Fonts Links)

```
Fraunces  —  https://fonts.google.com/specimen/Fraunces
Inter     —  https://fonts.google.com/specimen/Inter
Syne      —  https://fonts.google.com/specimen/Syne
```

## C — The 7 Mood Keywords (Every AI Prompt Uses These)

```
cinematic, masculine, restrained, golden hour lighting,
single subject, shallow depth of field, 35mm film grain
```

## D — Aspect Ratio Cheat Sheet

```
LinkedIn carousel        →  4:5
LinkedIn single image    →  3:2
YouTube thumbnail        →  16:9
Instagram quote card     →  1:1 or 4:5
Substack / blog header   →  16:9 or 2:1
Podcast art              →  1:1
Reels / YT Shorts        →  9:16
```

## E — The 10 Week-1 Prompts (Bookmark This Section)

Prompts 1-10 live in Section 5. Copy-paste ready. Run them on Monday, ship by Sunday.

## F — The 12-Shot Cooz Hero Library Shot List (Section 4.1, Shoot #1)

1. Hands on barbell
2. Back to camera, walking in
3. Eye contact, chiaroscuro
4. 3/4 profile (THE shot)
5. Candid loading plates
6. Sitting on bench, head down
7. Leaning against wall, window
8. Writing in notebook
9. Coffee cup, below angle
10. Wide establishing shot
11. Tight face crop
12. Walking out backlit

## G — The No-Fly List (Delete If Any Generated)

1. Stock photo athleticism
2. Corporate wellness pastels
3. Neon/cyberpunk gradients
4. Overly-styled influencer aesthetic
5. Liver King primal LARP
6. Generic "coach pointing at camera"
7. Mirror transformation shots (front)
8. MrBeast yellow/red thumbnails
9. AI-obvious slop (bad hands, warped text)
10. Emoji-heavy Canva templates
11. Entrepreneur-in-front-of-skyline cliche
12. Quote cards on flat solid colors

---

## Final Notes — The Dev Compile

**This is the visual nervous system for Resurrection Coach.** Every asset that ships must trace back to this document. When in doubt:

1. Check Section 1 (brand DNA) first
2. Check Section 2 for the prompt template
3. Check Section 6 for the fallback
4. Ship within 15 minutes of start

**If you spend more than 15 minutes on one visual, something is broken** — escalate down the fallback ladder, don't grind.

**The rule of the brand**: Cinematic. Masculine. Restrained. Spiritual without churchy. Premium without corporate. Raw without sloppy. When something feels wrong, it's usually because one of these six has drifted. Tune it back.

---

*Visual Packaging System v1.0 | Compiled April 2026 | Built against `strategic-dossier.md`, `flywheel-demo-output.md`, `WS1.6-voice-validation`, and `week-1-creative-brief.md`. Cross-validated against Mark Kashef visual design, Kittl graphic design, and brand-guidelines skills. Ready for Week 1 deployment.*
