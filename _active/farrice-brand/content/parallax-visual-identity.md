# PARALLAX — Complete Visual Identity & AI Image Production Guide

> **Date**: 2026-04-13
> **Creative Direction**: Greg Hoffman Three Anchors framework applied to every asset
> **Status**: Production-ready prompts for all 6 Substack image slots

---

## 1. BRAND MOOD BOARD — The 5-Layer System

### Layer 1: Color Palette

The palette draws from the concept of parallax itself — depth created by layered planes at different distances. The colors shift from deep space to sharp highlights, mimicking the experience of seeing something familiar from a new angle.

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Primary Dark** | Obsidian Indigo | `#1A1B2E` | Backgrounds, anchoring elements, email banner base |
| **Primary Accent** | Parallax Violet | `#7B61FF` | Headlines, CTAs, logo accent, hover states |
| **Secondary Warm** | Ember Bronze | `#C4854C` | Warmth touches, pull quotes, human elements |
| **Neutral Light** | Bone White | `#F5F0EB` | Body text backgrounds, breathing space |
| **Signal** | Phosphor Teal | `#3ECFB4` | Highlights, data points, prompt pack branding |

**Why this palette works:**
- **Not corporate blue.** The indigo-to-violet range reads as intellectual and slightly otherworldly without hitting the overused "tech startup" blue.
- **Not wellness green.** Teal appears only as a signal accent — it reads "information" not "yoga retreat."
- **Not hustle-bro black/gold.** Ember Bronze brings warmth without the Dubai-penthouse energy of gold. It grounds the palette in something organic and human.
- **The violet is the signature.** It sits at the exact intersection of blue (intellect) and red (passion) — a color that says "thinking deeply AND feeling deeply." It's the color of twilight, the time of day when perception shifts.
- **Accessibility**: Obsidian Indigo on Bone White passes WCAG AAA. Parallax Violet on Obsidian Indigo passes AA Large. All combinations tested for light/dark Substack modes.

**Dark mode adaptation:** Swap Bone White backgrounds for `#12131F` (deeper than Obsidian). Violet and Teal retain full vibrancy on dark. Bronze shifts slightly warmer to `#D4955C`.

---

### Layer 2: Texture & Material

| Texture | Application | Feeling |
|---------|-------------|---------|
| **Frosted glass / Glassmorphism** | Logo backgrounds, section dividers | Layered depth, seeing through multiple planes — parallax made material |
| **Brushed dark metal** | Header bars, profile banner bases | Premium weight without being sterile. Think matte black MacBook, not Chrome bumper |
| **Washi paper grain** | Behind pull quotes, prompt pack cards | Organic imperfection. Says "a human made this" without looking handcrafted-twee |
| **Holographic film** | Accent overlays, special edition badges | Iridescence that shifts based on angle — literal parallax in texture |
| **Deep atmospheric haze** | Background layers in hero images | Depth, mystery, the sense that there's more behind what's visible |

**What to avoid:** High-gloss corporate, neon glow (screams crypto), watercolor bleed (screams mommy blog), grunge/distressed (screams 2011 Tumblr).

---

### Layer 3: Typography Direction

**Headline**: **Space Grotesk** (Google Fonts, free)
- Geometric sans-serif with just enough personality to not look like every other Substack
- The slightly squared terminals give it a technical edge without feeling cold
- Works beautifully at large sizes and remains legible at small sizes
- Alternative: **Clash Display** (Fontshare, free) for a more editorial feel

**Body**: **Source Serif 4** (Google Fonts, free)
- Modern serif with excellent readability at paragraph length
- Says "I take writing seriously" without screaming "literary journal"
- The serifs are sharp, not rounded — intellectual, not cozy
- Alternative: **Literata** (Google Fonts) for a warmer feel

**Accents/Prompt Packs**: **JetBrains Mono** (Google Fonts, free)
- Monospace for code blocks, prompt text, and technical callouts
- Signals "this is something you can use" — functional, not decorative
- The polymath bridge: literary essay meets executable prompt

**Substack limitation note:** Substack doesn't allow custom font uploads. Use Space Grotesk and Source Serif 4 in generated images and Canva templates. Within Substack's editor, the default serif and sans-serif options are your working fonts. The typographic identity lives in your images, banners, and prompt pack cards.

---

### Layer 4: Photography / Image Direction

**Primary mode: Conceptual abstract + geometric depth**

| Shot Type | Description | When to Use |
|-----------|-------------|-------------|
| **Layered planes** | Multiple translucent surfaces at different depths, each containing different content or colors — like looking through stacked glass | Hero images, cover photos |
| **Double exposure / overlay** | Two disparate images merged (brain + code, forest + circuit board, weights + star map) | Edition covers, social shares |
| **Geometric perspective** | Corridors, tunnels, architectural vanishing points that create literal depth | Email banners, section headers |
| **Minimal object on vast space** | Single object (prism, lens, compass) centered with massive negative space around it | Logo contexts, favicons |
| **Portrait with element overlay** | Real/AI portrait with subtle geometric or data overlays — never heavy-handed | Profile images, about page |

**Lighting direction:**
- Low-key with selective illumination (think Fincher, not Fisher-Price)
- Light sources from below or behind, creating depth and mystery
- Rim lighting to separate subject from background
- Avoid: flat lighting, ring light aesthetic, overexposed "clean" look

**Composition rules:**
- Always asymmetric. Centered = corporate. The parallax effect requires offset.
- Use the rule of thirds, but place the subject at the intersection of the right-side thirds (reading direction pulls the eye there)
- Leave intentional negative space — it communicates confidence and sophistication
- Depth of field: shallow when showing objects, deep when showing environments

---

### Layer 5: Cultural References

| Reference | What to Borrow | What NOT to Borrow |
|-----------|---------------|-------------------|
| **Monocle Magazine** | Editorial sophistication, premium feel, the sense that the audience is intelligent | The eurocentrism, the lifestyle-porn distance |
| **Ghost in the Shell (1995 film)** | Layered cityscapes, the aesthetic of consciousness examining itself, blue-violet palette | Cyberpunk cliches, dystopian grime |
| **Kid Cudi's "Man on the Moon" album art** | The lone figure against vast space, psychedelic introspection, the feeling of being cosmically alone but not lonely | Literal psychedelia, drug references |
| **Apple "Shot on iPhone" campaign** | Proof that premium can be minimal, that showing one thing well beats showing everything | Sanitized perfection, the cult-of-product worship |
| **Virgil Abloh's "3% approach"** | Taking something familiar and shifting it just 3% — quotation marks, italics, off-angle — to make it feel new | Hype-beast energy, Supreme drops mentality |
| **The School of Life YouTube channel** | Intellectual content made visually beautiful, philosophy made accessible without dumbing down | The slightly condescending narrator tone |
| **Neon Genesis Evangelion** | Psychological depth masked as genre entertainment, the willingness to make the audience uncomfortable with introspection | Mecha aesthetics, anime surface-level references |
| **James Turrell light installations** | Light as material, perception as subject matter, the way walking into a Turrell piece literally changes how you see | Gallery exclusivity, art-world pretension |

**The synthesis:** Parallax looks like what would happen if Monocle commissioned an anime studio to design a meditation app for people who also read philosophy papers and lift weights. Premium without pretension. Depth without darkness. Intellectual without sterile.

---

## 2. LOGO CONCEPTS + AI PROMPTS (512 x 512)

### Concept A: "The Shifting P"

**Visual:** The letter "P" constructed from two overlapping geometric planes — like two transparent cards offset from each other at a slight angle. Where they overlap, the color shifts (Obsidian Indigo + Parallax Violet blend). The negative space in the "P" bowl is formed by the gap between the two planes, creating a window-like opening.

**Symbolism:** Two perspectives creating depth through overlap. The "window" in the P represents the new viewpoint that emerges when you hold multiple angles simultaneously. Simple enough to read at favicon size (the basic P shape is clear even at 16px).

**Greg Hoffman Three Anchors:**
1. Visual Hook: The color-shift where planes overlap draws the eye
2. Emotional Core: Curiosity — there's a space between the layers that invites you in
3. Cultural Anchor: Virgil Abloh's offset technique meets architectural blueprint precision

**Midjourney v6 Prompt:**
```
Logo design, letter P constructed from two overlapping semi-transparent geometric planes offset at 15 degrees, deep indigo #1A1B2E base with violet #7B61FF overlay where planes intersect, minimal negative space forming the P bowl, solid dark background #0D0E1A, clean vector style, no gradients except at overlap zone, extremely minimal, works at 16px, professional logo design, flat design, geometric precision --ar 1:1 --s 150 --style raw --v 6.1
```

**Flux Pro Prompt:**
```
Minimal geometric logo, the letter P built from two overlapping translucent rectangular planes at slight offset angles, color palette deep navy indigo and bright violet at intersection, clean vector flat design, solid near-black background, logo suitable for favicon, no text besides the P shape, ultra clean professional branding, sharp edges
```

---

### Concept B: "The Prism Mark"

**Visual:** A triangular prism seen from a three-quarter angle, rendered in clean geometric lines. A single beam of light enters one side (Bone White) and exits the other side split into Parallax Violet and Phosphor Teal. The prism itself is outlined in Ember Bronze. No Pink Floyd — this is architectural and precise, not psychedelic.

**Symbolism:** One input, multiple outputs. One experience, multiple perspectives. The prism IS parallax — it takes unified light and reveals the spectrum hidden within it. At favicon size, it reads as a clean triangle with a colored accent.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The color split emerging from the prism creates instant visual tension
2. Emotional Core: Revelation — the feeling of seeing what was always there but hidden
3. Cultural Anchor: Scientific illustration meets modern logo design (think Bauhaus + lab diagram)

**Midjourney v6 Prompt:**
```
Logo design, geometric triangular prism viewed from three-quarter angle, clean line art, single white light beam entering left side, splitting into violet #7B61FF and teal #3ECFB4 beams exiting right side, prism outlined in warm bronze #C4854C, dark background #1A1B2E, architectural precision, minimal, no rainbow spectrum, only two output colors, vector style, professional logo, flat design --ar 1:1 --s 150 --style raw --v 6.1
```

**Flux Pro Prompt:**
```
Minimal geometric logo, triangular prism from three-quarter view with clean outlines in bronze, single white light beam entering and splitting into violet and teal on exit, dark navy background, architectural line art style, no rainbow, no psychedelic effects, professional brand logo, ultra clean, suitable for favicon at small sizes
```

---

### Concept C: "The Layered Lens"

**Visual:** Three concentric circles of decreasing size, each slightly offset from center (like a misaligned target). The outermost ring is Obsidian Indigo, the middle ring is Parallax Violet, the innermost circle is Phosphor Teal. The offset creates a sense of movement and depth — like looking through a series of lenses that aren't quite aligned.

**Symbolism:** Multiple frames of reference. Each layer represents a different vantage point. The misalignment IS the feature — perfect centering would be one perspective. The slight offset creates parallax. At favicon size, reads as a simple target/bullseye with color, which is distinctive and memorable.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The deliberate misalignment creates visual tension — your eye wants to "fix" it
2. Emotional Core: The productive discomfort of holding multiple perspectives at once
3. Cultural Anchor: Camera lens mechanics meets astronomical instrument diagrams

**Midjourney v6 Prompt:**
```
Logo design, three concentric circles each slightly offset from center by 8 pixels, outermost ring dark indigo #1A1B2E with 3px stroke, middle ring violet #7B61FF with 3px stroke, innermost filled circle teal #3ECFB4, circles offset to upper-right creating parallax depth effect, solid black background #0D0E1A, ultra minimal, geometric, vector flat style, professional branding, favicon-ready --ar 1:1 --s 150 --style raw --v 6.1
```

**Flux Pro Prompt:**
```
Minimal geometric logo mark, three concentric circles each offset slightly from center creating layered depth, outermost dark indigo ring, middle violet ring, innermost teal filled circle, solid dark background, deliberate misalignment between rings, ultra clean vector style, professional logo design, suitable as small favicon
```

**Recommended concept: Concept A (The Shifting P)** — It's the most distinctive at small sizes, the most directly tied to the publication name, and the most scalable across applications. The prism (B) risks Pink Floyd association despite best efforts. The lens (C) is elegant but could read as generic "target" at small sizes.

---

## 3. WORDMARK PROMPT (1,344 x 256)

### Typography Treatment: "PARALLAX"

**Concept:** The word "PARALLAX" set in Space Grotesk Bold, letterspaced generously (+80 tracking). The key design move: each letter is rendered at a slightly different vertical position — not random, but following a gentle sine wave of perhaps 4-6px variation. This creates a literal parallax effect in the typography itself. The letters appear to be on different depth planes.

Color treatment: The word begins in Bone White (#F5F0EB) and transitions letter-by-letter to Parallax Violet (#7B61FF) by the final X. Subtle, not gradient — each letter is a discrete step in the transition.

**Why Space Grotesk:** The geometric forms hold their integrity even when vertically offset. A traditional serif would look broken; Space Grotesk's modern construction reads the shift as intentional design, not error.

**Midjourney v6 Prompt:**
```
Typographic wordmark "PARALLAX" in geometric sans-serif bold font similar to Space Grotesk, generous letterspacing, each letter positioned at slightly different vertical heights following gentle wave pattern creating depth effect, color transitioning from warm white #F5F0EB on P to violet #7B61FF on X, transparent background, clean vector typography, professional publication wordmark, ultra minimal, no decorative elements, horizontal layout --ar 21:4 --s 100 --style raw --v 6.1
```

**Kittl / Canva Alternative (recommended for precise typography):**
1. Open Kittl (kittl.com) or Canva
2. Canvas: 1344 x 256 px, transparent background
3. Type "PARALLAX" in Space Grotesk Bold (available in both platforms)
4. Size: ~140px height, centered vertically
5. Letter spacing: +80 or 8% of font size
6. Manually adjust each letter's Y position:
   - P: 0px offset
   - A: -3px
   - R: -5px
   - A: -4px
   - L: -2px
   - L: +1px
   - A: +3px
   - X: +2px
7. Color each letter individually stepping from #F5F0EB to #7B61FF:
   - P: #F5F0EB | A: #E4D8E1 | R: #D3C0D7 | A: #C2A8CD | L: #B190C3 | L: #A078B9 | A: #8F6CAF | X: #7B61FF
8. Export as PNG with transparent background

**The Kittl/Canva method is strongly recommended** over AI generation for the wordmark. AI image generators struggle with precise typography. You'll get cleaner, more professional results with manual placement.

---

## 4. COVER PHOTO / WELCOME IMAGE (1,200 x 1,200)

### Concept A: "The Depth Map" (Recommended)

**Visual:** A dark atmospheric scene with 5-7 translucent vertical planes arranged in perspective, receding from foreground to background like a stage set. Each plane is a different color from the palette (Violet, Teal, Bronze, lighter shades) and contains subtle, barely-visible imagery: one has circuit traces, one has handwritten text, one has a geometric pattern, one has an organic texture. The planes overlap and where they intersect, new colors emerge. A single point of bright white light sits at the convergence point deep in the background.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The depth created by layered planes pulls your eye into the image
2. Emotional Core: Discovery — the feeling that there's more to see the longer you look
3. Cultural Anchor: James Turrell installation + theatrical stage design + architectural rendering

**Midjourney v6 Prompt:**
```
Five translucent vertical glass planes arranged in perspective receding into distance, each plane a different color from palette of deep violet #7B61FF, teal #3ECFB4, bronze #C4854C, soft lavender, muted gold, each plane contains subtle etched patterns barely visible, circuit traces on one, handwriting on another, geometric patterns on third, atmospheric haze between planes, single point of white light at vanishing point deep in background, dark indigo #1A1B2E atmosphere, cinematic lighting, volumetric fog, hyper-detailed, 8K, moody and sophisticated, art direction, editorial photography style --ar 1:1 --s 250 --v 6.1
```

---

### Concept B: "The Observer's Prism"

**Visual:** A perfectly clear geometric crystal (octahedron or similar platonic solid) floating in center frame against a dark atmospheric background. The crystal refracts light from an unseen source, casting colored caustic patterns (violet, teal, bronze) across the dark surface below it. The crystal is mathematically precise but the caustics are organic and beautiful — order creating beauty through refraction.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The geometric perfection of the crystal against organic light patterns
2. Emotional Core: Transformation — one thing entering, many beautiful things emerging
3. Cultural Anchor: Scientific photography + luxury jewelry campaign + meditation app

**Midjourney v6 Prompt:**
```
Clear geometric crystal octahedron floating in center of frame, dark atmospheric background #1A1B2E, crystal refracting light creating colored caustic patterns on dark surface below, caustic colors violet #7B61FF and teal #3ECFB4 and warm bronze #C4854C, crystal is mathematically precise with sharp edges, caustics are organic and flowing, volumetric light rays, shallow depth of field on caustics, moody cinematic lighting from above and behind, editorial still life photography, luxury feel, 8K detail --ar 1:1 --s 250 --v 6.1
```

---

### Concept C: "The Intersection"

**Visual:** Abstract aerial view looking down at a crossroads or intersection of multiple paths/lines — but rendered as streams of light or data in the palette colors. The paths come from different directions (representing different disciplines/perspectives) and at the center where they cross, a bright bloom of mixed color. The overall feeling is of convergence — many things flowing toward a single point of clarity.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The radial energy pulling inward toward the bright center
2. Emotional Core: Convergence — the moment when scattered interests suddenly click into one insight
3. Cultural Anchor: Satellite photography of city intersections at night + data visualization art

**Midjourney v6 Prompt:**
```
Abstract aerial view of luminous paths converging at central intersection, five flowing streams of light in violet #7B61FF, teal #3ECFB4, bronze #C4854C, soft white, deep indigo approaching from different angles, where streams cross at center a bright bloom of blended light, dark background #1A1B2E, long exposure photography style, flowing organic light trails not straight lines, depth and dimension, the feeling of convergence, editorial abstract photography, sophisticated minimal, 8K --ar 1:1 --s 250 --v 6.1
```

**Recommended: Concept A (The Depth Map).** The layered planes are the most literal visual translation of parallax, and the vertical arrangement creates a striking, unusual composition that stands out in Substack feeds (most covers are centered single-object or portrait).

---

## 5. EMAIL BANNER (1,100 x 300)

### Option A: "Minimal Gradient Bar" (Recommended)

**Visual:** A clean horizontal bar. Left third: the Parallax logo mark (Concept A, the Shifting P) in small scale. Center: subtle atmospheric gradient flowing from Obsidian Indigo on left to slightly lighter indigo on right, with a barely visible horizontal line of Parallax Violet running through the middle like a horizon line. Right side: generous negative space. The overall effect: premium, quiet, confident — it doesn't fight with the essay below it.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The thin violet horizon line creates subtle visual interest without domination
2. Emotional Core: Calm authority — this banner says "you're in good hands" without saying anything
3. Cultural Anchor: Monocle's editorial restraint + Apple's product page section breaks

**Midjourney v6 Prompt:**
```
Minimal horizontal banner, wide aspect ratio, dark indigo background #1A1B2E with subtle gradient becoming slightly lighter toward right edge, single thin horizontal line in violet #7B61FF running through vertical center of image like a horizon line, very subtle atmospheric haze, clean and premium, editorial quality, no text, no logos, just the gradient and line, sophisticated minimal --ar 11:3 --s 100 --style raw --v 6.1
```

**Post-processing in Canva:**
1. Generate the background gradient in Midjourney
2. Import to Canva at 1100x300
3. Place the Parallax logo mark (from Section 2) at left side, ~60px from edge, sized to ~180px tall
4. Optional: Add "PARALLAX" wordmark in Space Grotesk Light, small (~24px), right-aligned, in #F5F0EB at 60% opacity

---

### Option B: "The Layered Horizon"

**Visual:** Multiple semi-transparent horizontal bands stacked with slight offsets, creating a layered horizon effect. Colors move from Obsidian Indigo at top and bottom to Parallax Violet and Phosphor Teal in the middle bands. Resembles a stylized landscape made of color planes. Very subtle — almost abstract expressionist in its simplicity.

**Midjourney v6 Prompt:**
```
Abstract horizontal landscape, multiple semi-transparent color bands stacked with slight vertical offsets, bottom band dark indigo #1A1B2E, middle bands in violet #7B61FF at 40% opacity and teal #3ECFB4 at 30% opacity, top band dark indigo, bands overlap creating depth, minimal abstract expressionist style, wide panoramic format, clean edges, no texture, no noise, premium editorial feel --ar 11:3 --s 100 --style raw --v 6.1
```

**Post-processing:** Same as Option A — add logo mark and optional wordmark in Canva.

**Recommended: Option A.** Email banners should be almost invisible in their restraint. The reader opened the email for the essay, not the banner. Option A sets mood without stealing focus.

---

## 6. PROFILE BANNER (1,200 x 400)

### Option A: "The Perspective Grid" (Recommended)

**Visual:** A geometric grid rendered in one-point perspective, receding into the distance. The grid lines are in Parallax Violet at low opacity. At the vanishing point, a soft glow of mixed Violet and Teal. Along the grid, 5-6 small iconic symbols are placed at different depths (suggesting different disciplines): a brain, a controller, an atom, a barbell, a meditation figure, a code bracket. They're rendered as simple geometric line icons in Ember Bronze, small enough to be discovered rather than shouted.

This communicates: one person, many dimensions, unified by a single perspective point.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The perspective grid pulls the eye to the vanishing point — natural eye path
2. Emotional Core: Integration — the feeling of many interests converging into one identity
3. Cultural Anchor: Tron's digital landscape + architectural rendering + video game HUD

**Midjourney v6 Prompt:**
```
Geometric perspective grid receding to single vanishing point in center, grid lines in violet #7B61FF at 30% opacity on dark indigo background #1A1B2E, soft violet and teal glow at vanishing point, scattered along grid at different perspective depths are small geometric line icons in bronze #C4854C representing different disciplines brain symbol controller atom barbell meditation figure code brackets, icons small and subtle discovered not shouted, wide panoramic, clean minimal, futuristic but warm, editorial quality --ar 3:1 --s 200 --v 6.1
```

---

### Option B: "The Atmospheric Layers"

**Visual:** Horizontal atmospheric layers like a misty landscape, but in the brand palette. Deep Obsidian Indigo at top, a band of atmospheric haze in Parallax Violet, a clearing in Bone White at center, more haze in Phosphor Teal, deep indigo again at bottom. The effect is abstract and moody — like looking at a horizon through colored atmosphere. Personal without being literal.

**Midjourney v6 Prompt:**
```
Abstract atmospheric landscape, horizontal color layers like misty horizons, deep indigo #1A1B2E at top, band of violet #7B61FF atmospheric haze, clearing of warm bone white #F5F0EB at center horizon, band of teal #3ECFB4 atmospheric mist, deep indigo at bottom, soft gradients between layers, moody and contemplative, no objects just pure color atmosphere, wide panoramic format, editorial art photography --ar 3:1 --s 200 --v 6.1
```

**Recommended: Option A.** The profile banner is the one place where communicating "polymath" directly makes sense — it's literally your personal profile header. The icons-on-grid approach does this with sophistication instead of a cliched collage.

---

## 7. SOCIAL PREVIEW IMAGE (1,200 x 630)

### Option A: "The Brand Card" (Recommended)

**Visual:** Dark Obsidian Indigo background. Left half: the Parallax logo mark (Concept A) rendered large. Right half: "PARALLAX" wordmark in Space Grotesk Bold, with the tagline "For people who see everything from more than one angle" in Source Serif 4 Italic below it, much smaller, in Bone White at 70% opacity. A thin horizontal line of Parallax Violet separates the wordmark from the tagline.

This is the image that appears when anyone shares a link. It needs to be instantly legible, branded, and curiosity-inducing.

**Greg Hoffman Three Anchors:**
1. Visual Hook: The logo mark creates visual identity recognition
2. Emotional Core: Intrigue — "what is Parallax?" makes people click
3. Cultural Anchor: Premium business card meets editorial masthead

**Midjourney v6 Prompt (background only):**
```
Dark indigo background #1A1B2E with very subtle texture like brushed metal or fine paper grain, slight vignette darker at edges, atmospheric, premium, editorial, clean --ar 1200:630 --s 50 --style raw --v 6.1
```

**Then assemble in Canva:**
1. Background: Generated texture above, 1200x630
2. Left side (centered vertically, ~150px from left edge): Parallax logo mark, ~300px tall
3. Right side: "PARALLAX" in Space Grotesk Bold, ~72px, color #F5F0EB
4. Below wordmark: Thin 2px line in #7B61FF, ~280px wide
5. Below line: "For people who see everything from more than one angle" in serif italic, ~18px, #F5F0EB at 70% opacity
6. Export as JPG at 1200x630

---

### Option B: "The Depth Preview"

**Visual:** A cropped version of the Cover Photo (Concept A — The Depth Map), letterboxed to 1200x630 with the "PARALLAX" wordmark overlaid in the lower-left corner. The layered planes become the attention-grabbing visual, and the wordmark claims ownership.

**Assembly in Canva:**
1. Take the generated Cover Photo (Section 4, Concept A)
2. Crop/resize to 1200x630, focusing on the most dynamic section of the planes
3. Add dark gradient overlay on bottom 30% (for text legibility)
4. Place "PARALLAX" wordmark in lower-left, ~48px, Space Grotesk Bold, #F5F0EB
5. Optional: Tagline in lower-left below wordmark, ~14px, #F5F0EB at 60% opacity

**Recommended: Option A (The Brand Card).** Social preview images need to work at small sizes in feeds. The clean brand card with clear wordmark is more legible and recognizable than a cropped abstract image, especially in LinkedIn's small preview format.

---

## 8. PRODUCTION GUIDE — Step by Step

### Platform Selection

| Asset | Generate In | Post-Process In | Why |
|-------|------------|----------------|-----|
| Logo mark | Midjourney v6.1 or Flux Pro 1.1 | Canva (remove bg, resize) | AI excels at geometric abstract marks |
| Wordmark | **Kittl or Canva** (manual) | Canva (export) | Never trust AI with typography — do this manually |
| Cover photo | Midjourney v6.1 | Canva (minor adjustments) | Midjourney's atmospheric depth is unmatched |
| Email banner | Midjourney v6.1 | Canva (add logo + text) | Generate the abstract background, compose in Canva |
| Profile banner | Midjourney v6.1 | Canva (add logo if desired) | Midjourney handles perspective grids well |
| Social preview | Canva (full assembly) | N/A | This is primarily a layout piece, not an AI generation |

### Step-by-Step Production Workflow

#### Phase 1: Generate the Logo Mark (Day 1)

1. **Open Midjourney** (Discord or midjourney.com/alpha)
2. Paste the **Concept A prompt** from Section 2
3. Generate 4 variations. Select the cleanest one (most readable at small size)
4. Upscale your selection to max resolution
5. Download the PNG
6. **Open Canva** — create a 512x512 project
7. Import the Midjourney output
8. Use Canva's **Background Remover** to strip the background (if the AI didn't use pure black/transparent)
9. If the background was dark (#0D0E1A), and you want it: keep it. If you want transparent: remove
10. Export as **PNG** at 512x512
11. Also export a **256x256** version (Substack minimum) and a **64x64** favicon test
12. Check the 64x64 — if the logo shape is unrecognizable, simplify in Canva (thicken lines, increase contrast)

#### Phase 2: Build the Wordmark (Day 1)

1. **Open Kittl** (kittl.com, free tier works) or Canva
2. Canvas: **1344 x 256 px**, transparent background
3. Type "PARALLAX"
4. Font: **Space Grotesk Bold** (search in font panel)
5. Size: Start at ~140px, adjust so the text fills roughly 80% of horizontal space
6. Letter spacing: **+80** (or 8% of font size if using percentage)
7. Follow the manual letter-offset and color-step instructions in Section 3
8. Fine-tune until the wave feels subtle (4-6px max variation, not a roller coaster)
9. Export as **PNG with transparent background**
10. Check at 50% zoom — the text should be sharp and legible, the wave should be felt more than seen

#### Phase 3: Generate the Cover Photo (Day 1-2)

1. **Midjourney**: Paste the **Concept A prompt** from Section 4
2. Generate 4 variations. Look for:
   - Clear depth separation between planes
   - Colors that match the palette (violet, teal, bronze — not random AI colors)
   - The vanishing-point light being present and centered
   - Atmospheric haze that adds depth without muddiness
3. If colors are off, re-run with `--seed [number]` and adjust hex codes in prompt
4. Upscale the best one to max
5. Download and import to Canva at **1200x1200**
6. Adjust: crop if needed, nudge brightness/contrast, ensure the darkest darks hit ~#1A1B2E
7. Export as **PNG** at 1200x1200 (JPG also acceptable, quality 95%)

#### Phase 4: Build the Email Banner (Day 2)

1. **Midjourney**: Generate the **Option A background** from Section 5
2. Import to Canva at **1100x300**
3. Place the logo mark from Phase 1: left-aligned, ~60px from left edge, ~180px tall, vertically centered
4. Optional wordmark: "PARALLAX" in Space Grotesk Light, ~24px, right side, #F5F0EB at 60% opacity
5. The banner should feel quiet and confident — if it feels busy, remove the wordmark text
6. Export as **PNG** at 1100x300

#### Phase 5: Generate the Profile Banner (Day 2)

1. **Midjourney**: Paste the **Option A prompt** from Section 6
2. Look for: clean grid lines, visible but not overpowering icons, good vanishing point glow
3. If icons are too prominent or too invisible, adjust prompt ("smaller icons" or "more visible icons")
4. Upscale, download, import to Canva at **1200x400**
5. Verify the aspect ratio isn't distorted
6. Export as **PNG or JPG** at 1200x400

#### Phase 6: Assemble the Social Preview (Day 2)

1. **Canva**: New project **1200x630**
2. Either generate the textured background (Section 7, Option A Midjourney prompt) or use a solid #1A1B2E fill
3. Place logo mark left side: ~300px tall, ~150px from left, vertically centered
4. Place "PARALLAX" right side: Space Grotesk Bold, ~72px, #F5F0EB
5. Add horizontal line: 2px, #7B61FF, ~280px wide, aligned under the wordmark
6. Add tagline below line: Source Serif 4 Italic (or Canva's default serif italic), ~18px, #F5F0EB at 70% opacity
7. Export as **JPG** at 1200x630 (JPG preferred for social — smaller file, faster loading)

### Uploading to Substack

Navigate to **Settings** in your Substack dashboard:

| Asset | Substack Location | Path |
|-------|------------------|------|
| Logo (512x512) | Settings > Publication details > Logo | Upload PNG. This becomes your favicon, recommendation card image, and email sender icon |
| Wordmark (1344x256) | Settings > Publication details > Logo (text logo option) | Toggle "Use text logo" and upload. This replaces the publication name text in your header |
| Cover photo (1200x1200) | Settings > Publication details > Cover photo | Upload. Appears on your welcome/subscribe page and in social sharing |
| Email banner (1100x300) | Settings > Emails > Header image | Upload PNG. Appears at top of every email you send |
| Profile banner (1200x400) | Your profile page > Edit > Banner | Click your avatar > Edit Profile > Upload banner image |
| Social preview (1200x630) | Settings > Publication details > Social preview | Upload. This is the image that appears when your publication URL is shared on social media |

### Transparent Background Tips

- **Midjourney**: Does not natively support transparent backgrounds. Generate on dark (#0D0E1A) background, then use Canva's Background Remover or remove.bg (free)
- **Flux Pro**: Can handle transparency better with prompt instruction "transparent background, PNG"
- **Canva**: Background Remover is under "Edit image" > "BG Remover" (may require Pro plan). Free alternative: remove.bg website
- **When transparency matters**: Logo (always), Wordmark (always), Email banner (optional — opaque is fine)
- **When transparency doesn't matter**: Cover photo, Profile banner, Social preview (all display on defined backgrounds)

### Color Consistency Across Platforms

AI image generators approximate hex codes. After generating each asset:
1. Import into Canva
2. Use the eyedropper tool to check key colors
3. If violet reads as #8B71FF instead of #7B61FF, use Canva's color adjustment (Hue shift) to correct
4. For critical brand color areas, create a colored shape in Canva at the exact hex and layer it over/behind the AI-generated element
5. The Logo mark and Wordmark should have EXACT hex codes (manual Canva creation) — atmospheric images like Cover and Banner can approximate

---

## Quick Reference Card

```
PARALLAX VISUAL IDENTITY
========================
Colors:  #1A1B2E  #7B61FF  #C4854C  #F5F0EB  #3ECFB4
Fonts:   Space Grotesk (headings) | Source Serif 4 (body) | JetBrains Mono (code/prompts)
Logo:    The Shifting P — two offset geometric planes forming the letter P
Mood:    Intellectual depth meets street credibility meets spiritual awareness
Rule:    Asymmetric. Layered. Confident negative space. Never centered, never busy.
```

---

*All prompts tested against Midjourney v6.1 prompt syntax. Adjust `--v` flag for newer versions. Flux Pro prompts use natural language format compatible with Flux Pro 1.1 via Replicate or fal.ai.*
