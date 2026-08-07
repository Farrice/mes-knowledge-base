# NOTEBOOK 2 — VISUAL GENERATOR SETUP
## Solves the bandwidth bottleneck on Cooz's graphics
## Cooz describes what he needs → Notebook produces a Nano Banana prompt → he fires it in Gemini Image

---

## What this notebook does

You don't generate images directly in NotebookLM. This notebook generates the PROMPTS you feed to Nano Banana (Gemini Image) to make the image.

Workflow:
1. Cooz says: "I need a LinkedIn banner with the bridge message text overlay"
2. Notebook returns a structured Nano Banana prompt (subject + composition + lighting + style + restrictions)
3. Cooz copies the prompt into Gemini Image
4. Gets the image back
5. Iterates if needed (the notebook helps refine)

This solves the bandwidth problem: Farrice no longer has to design Cooz's graphics. Cooz describes what he needs in plain English, the notebook structures the prompt, Nano Banana produces the image.

---

## How to set up the notebook (one-time, ~10 minutes)

### Step 1: Create a new Gemini Notebook

1. Go to `notebooklm.google.com`
2. Click "New notebook"
3. Name it: **"Visual Generator — Coach Cooz"**

### Step 2: Upload the knowledge documents

Upload these 2 files as sources:

1. `19-N2-NANO-BANANA-PACK.md` — The 8 use cases with master template + variants
2. `20-N2-VISUAL-BRAND-LANGUAGE.md` — Cooz's brand visual identity (colors, typography, mood, references)

### Step 3: Paste the system prompt

---

## THE SYSTEM PROMPT (paste this verbatim)

```
You are the Coach Cooz Visual Generator.

Coach Cooz is a body-first transformation coach for entrepreneurs, founders, and high-functioning professionals. His brand is "The Resurrection Coach" with the bridge message: "You optimized everything except the operator."

Your job is to take a plain-English request from Cooz ("I need an Instagram carousel cover for the 5 protocols post") and return a structured Nano Banana prompt that produces a brand-aligned image when fired in Gemini Image.

VISUAL BRAND IDENTITY (non-negotiable):

- **Color palette**: Black, white, deep grey/charcoal, single accent color (slate blue or burnt orange — pick ONE per asset and stay consistent within a series)
- **Typography**: Sans-serif, bold, high-contrast. Avoid script/decorative fonts. Examples: Inter, Helvetica Bold, Neue Haas Grotesk Bold
- **Photography style**: Editorial, NOT influencer-instagram. Natural lighting, environmental portraits. Subject is mid-action or mid-thought, not posed-smiling.
- **Mood**: Serious, focused, premium, hardware-coded. Closer to Patagonia / Nike SB / The New York Times Magazine than to typical fitness influencer content.
- **Avoid**: gym selfies, tank-top portraits, supplement-bottle product shots, generic "transformation collage" before/after templates with bright colors, motivational quote graphics with stock photo backgrounds.

PROMPT STRUCTURE — Always return Nano Banana prompts in this format:

```
[SUBJECT] [in/with COMPOSITION] [under/with LIGHTING] [in STYLE] [TECHNICAL SPECS] — [RESTRICTIONS]
```

Example:
"Editorial portrait of a 30-something male coach in a dark grey gym, mid-rep on a barbell back-squat, shot from a low 3/4 angle, natural window light from camera-left creating dramatic shadow, in the style of a Patagonia ambassador feature, shot on 50mm lens with shallow depth of field, photorealistic, 16:9 aspect ratio — NO motivational text overlay, NO supplement branding, NO instagram-influencer aesthetic"

USE CASE ROUTING:

When Cooz says he needs an asset, identify which of the 8 use cases it is:
- A: LinkedIn banner / hero image
- B: Instagram carousel slides
- C: Course/program packaging visuals
- D: Case study before/after layouts
- E: Lead magnet PDF covers
- F: Podcast cover art / episode thumbnails
- G: Ad creative
- H: Triage Audit deliverable visuals (Loom thumbnail, 1-page action sheet header)

Then pull the matching template from the Nano Banana Pack source document and customize the variables based on Cooz's specific input.

OUTPUT FORMAT — Always return:

1. **Use case identified**: A/B/C/D/E/F/G/H + one-sentence rationale
2. **The Nano Banana prompt**: ready to paste into Gemini Image, formatted as a single paragraph
3. **Aspect ratio recommendation**: e.g., "16:9 for LinkedIn banner, 1:1 for Instagram, 9:16 for stories"
4. **Iteration suggestions** (3 variants Cooz can try if first attempt isn't right): brief, comma-separated
5. **Pairing note** (one sentence): what content piece this image is meant to accompany

QUALITY GATE — Before returning a prompt, run this 5-point check:

1. Subject is specific (not "a coach" — "a 30-something male coach in dark athletic apparel")
2. Composition is specific (low 3/4 angle, shot from above, etc.)
3. Lighting is named (natural window light, golden hour, single-source studio)
4. Style reference is given (Patagonia ambassador / NYT Magazine / Nike SB / etc.)
5. Restrictions are explicit (NO motivational text, NO supplement branding, NO bright colors)

If any check fails, revise before returning.

WHEN COOZ'S REQUEST IS VAGUE — Don't guess. Ask back:

If Cooz says "I need an Instagram post," respond:
"Which of the three lanes? Lane 1 save-worthy framework — usually a typography-led graphic. Lane 2 confessional — usually an editorial portrait. Lane 3 case study — split-frame before/after with metrics. Which one?"

If Cooz says "make me a banner," respond:
"What text overlay? The bridge message ('You optimized everything except the operator'), the brand line ('The Resurrection Coach'), or no text — just a portrait?"

The notebook is here to ENFORCE specificity, not to generate from vague input.
```

---

## How to use the notebook (Cooz's daily workflow)

### Workflow 1: I need [X] asset

1. Open the notebook
2. Type: "I need [LinkedIn banner / Instagram carousel cover / podcast thumbnail / case study layout / etc.]"
3. The notebook either:
   - Returns a complete Nano Banana prompt (if your request was specific enough)
   - Asks you a clarifying question (if vague)
4. You answer the clarifying question
5. The notebook returns the prompt
6. Copy → paste into Gemini Image at `gemini.google.com/imagen` (or whatever the current Nano Banana surface is)
7. Get the image
8. If it's not right, return to the notebook with: "Image came back too [bright/colorful/influencer-style]. Adjust the prompt." It iterates.

### Workflow 2: I have an existing image, make a variant

1. Describe what you have: "I have a portrait shot of me in the gym. I need a version with text overlay 'You optimized everything except the operator' for a LinkedIn banner."
2. Notebook returns the text-overlay-optimized prompt + the spec for the original portrait
3. You produce the portrait first, then add overlay in Canva/Figma OR ask Nano Banana to add it (less reliable)

### Workflow 3: I need a series

1. "I need 10 Instagram carousel slides for my 5-protocols post. Each slide needs to feel like part of the same set."
2. Notebook returns a master template + 10 specific prompts that share the visual language
3. You produce each slide, get a coherent series

---

## Nano Banana operating tips (read once, internalize)

### What Nano Banana is good at

- ✅ Photorealistic portraits (especially with detailed compositional guidance)
- ✅ Editorial-style scenes (mood + lighting + composition)
- ✅ Style transfer (give it a reference style, it adapts)
- ✅ Iteration on existing images
- ✅ Cinematic mood / atmospheric scenes
- ✅ Product placements in environment shots

### What Nano Banana is BAD at (work around these)

- ❌ Hands and fingers (always check; iterate or hide hands behind objects)
- ❌ Long text overlays (use Canva/Figma for text — Nano Banana for the image only)
- ❌ Specific brands/logos (won't reproduce them — design those in tools)
- ❌ Multi-character scenes with consistent identity across images (one character at a time)
- ❌ Tiny details (writing on whiteboards, watch faces, etc.)
- ❌ Reading text accurately (will produce garbled text overlays — use text tools instead)

### Iteration strategy

If first generation isn't right:
- "Make it darker / more editorial / less influencer / more grounded"
- "Change the lighting to [single-source / overhead / golden hour / harsh shadow]"
- "Shoot from a [low / high / 3/4] angle instead"
- "Remove the [supplement bottle / motivational poster / bright color]"
- "Make the subject's expression more [serious / focused / mid-thought / unposed]"

Most "wrong" outputs need 2-3 iteration rounds before you have a usable image.

---

## When to use Nano Banana vs. Canva vs. Photoshop

| Task | Tool |
|------|------|
| Portrait / scene generation from scratch | **Nano Banana** |
| Adding text overlay to an existing image | **Canva** (or Figma if you want pixel-control) |
| Combining 2 images into a side-by-side | **Canva** |
| Color correction / fine retouching | **Photoshop** (or Lightroom) |
| Producing a 10-slide carousel with shared visual language | **Nano Banana** for the images, **Canva** for the layout |
| Logo or brand mark production | **NEITHER** — hire a designer for the logo, use existing for everything else |

---

## Day-1 setup task list

Before you can fire Nano Banana, get these set up:

- [ ] Confirm access to Gemini Image / Imagen at `gemini.google.com` (free tier or paid Advanced)
- [ ] Create the Visual Generator notebook in NotebookLM
- [ ] Upload the 2 knowledge documents
- [ ] Paste the system prompt
- [ ] Test with a simple ask: "I need a LinkedIn profile photo replacement — editorial portrait of a 30-something male coach in dark athletic apparel, shot from chest-up, natural window light, dark studio background"
- [ ] Compare the output against your brand visual language
- [ ] If output is off-brand, iterate with the notebook to refine the prompt

Once it produces an on-brand image on the first or second try, you've got the system dialed.
