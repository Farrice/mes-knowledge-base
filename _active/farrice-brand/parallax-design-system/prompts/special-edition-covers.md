# Parallax — AI Image Prompts for Special-Edition Covers

**Version:** 1.0 (2026-04-27)
**Use:** Only for special editions where the content demands a specific visual metaphor (manifestos, deep theme pieces). Default editions use the typographic-only edition cover template — see [assets/edition-cover-template.html](../assets/edition-cover-template.html).

---

## The Rule

The creative rebrief is explicit: **AI image generation is the seasoning, never the main course.** When you do reach for it:

1. The image goes in the bottom-right corner at 20-30% opacity
2. Typography (edition number + title) is the primary visual; the AI image is texture
3. Image describes a **concrete physical object in specific lighting** — never a concept
4. Generate, screenshot, then composite under the typographic edition cover template

If a special edition warrants a full atmospheric image (the manifesto, a theme piece), the image takes the full frame at 60-80% opacity with the wordmark + edition number on top. Reserve this for ~1 in 10 editions maximum. Most editions ship typographic-only.

---

## Prompt Formula (proven)

The rebrief identified why the old AI-image attempts failed: they described abstract concepts ("translucent planes receding into atmospheric haze"). AI generators produce their best work given **concrete physical objects in specific lighting conditions on real surfaces**, photographed in a specific film stock or photographic style.

**Working formula:**

```
[Concrete physical subject], [specific lighting direction and color temperature],
[specific real-world surface or environment], [specific camera/lens or film stock reference],
editorial still-life photography, shallow depth of field, [mood],
no text, no logos, no humans
--ar 1:1 --s 200 --v 6.1
```

Use this formula on Midjourney v6 / Flux Pro / Higgsfield (still). Adjust `--ar` per asset target.

---

## Aesthetic Constants (every prompt carries these)

These are non-negotiable across all Parallax AI images. Add them to every prompt:

- **Color tonality:** Warm neutral palette. Concrete grays, warm whites, deep ink shadows. **Subtle violet accent only when natural** (e.g., light through a prism, twilight sky). Never primary violet hits — that's the wordmark's job.
- **Lighting:** Single directional source — window light, harsh sun, single Edison bulb. No multi-source studio lighting. Long shadows.
- **Surfaces:** Concrete, raw wood, matte paper, plaster, fabric. Real materials. Never glass-and-chrome tech aesthetic.
- **Reference film stocks:** Kodak Portra 400 (color), Kodak Tri-X (B&W). Never digital "VSCO" or "Instagram" looks.
- **What to exclude:** No people. No faces. No tech products. No screens. No branded objects. No text. No logos.

---

## Prompt Library by Edition Theme

### Identity / Polymath / Multi-Interest editions

```
A glass prism resting on raw concrete surface, harsh directional sunlight from upper left
casting a single rainbow refraction band across the concrete, faint dust visible in the
light beam, shot on Kodak Portra 400, editorial still-life photography, shallow depth of field,
quiet morning mood, no text, no logos, no humans --ar 1:1 --s 200 --v 6.1
```

```
Three identical white ceramic objects (a cup, a stone, an egg) arranged on weathered oak,
single window light from camera-right, warm afternoon, deep shadows, shot on Hasselblad,
editorial still life, contemplative, no text, no logos, no humans --ar 1:1 --s 150 --v 6.1
```

### Suppression / Identity-Breaking editions

```
A hairline crack in a concrete wall with thin violet light bleeding through from behind,
overcast diffuse lighting, weathered concrete texture visible, shot on Kodak Portra 400,
editorial documentary photography, quiet defiance mood, no text, no logos, no humans
--ar 1:1 --s 200 --v 6.1
```

```
A single sealed cardboard box on a polished concrete floor, hard window light raking
across from low angle, long shadow, dust particles in the light, shot on Tri-X 35mm
black and white, editorial reportage, quiet tension, no text, no logos, no humans
--ar 1:1 --s 100 --v 6.1
```

### Father / Domestic / Quiet-Time editions

```
A child's wooden building block on a worn linen tablecloth, soft morning window light
from camera-left, blurred kitchen interior in deep background, shot on Kodak Portra 800,
editorial documentary, tender domestic mood, no text, no logos, no humans
--ar 1:1 --s 150 --v 6.1
```

```
An empty rocking chair in the corner of a softly lit room, late afternoon golden light,
hardwood floor, faint indication of an open book on the chair seat, shot on Hasselblad,
editorial still life, contemplative, no text, no logos, no humans
--ar 1:1 --s 150 --v 6.1
```

### AI / Systems / Building editions

```
A single mechanical typewriter key resting alone on a sheet of weathered paper,
single window light from upper-right, warm shadow falling across the page,
shot on Kodak Portra 400, editorial still-life photography, shallow depth of field,
intimate scale, no text, no logos, no humans --ar 1:1 --s 200 --v 6.1
```

```
A circuit board fragment partially buried in raw concrete, daylight from above,
single shadow cast, weathered industrial texture, shot on Tri-X black and white,
editorial documentary, brutalist mood, no text, no logos, no humans
--ar 1:1 --s 100 --v 6.1
```

### Reckoning / Confrontation editions

```
A single glass of water on a bare wooden table, harsh directional sunlight from upper-left,
high-contrast shadow falling diagonally across the table, dust particles visible in the light,
shot on Kodak Portra 400, editorial still life, quiet intensity, no text, no logos, no humans
--ar 1:1 --s 200 --v 6.1
```

```
A worn leather notebook, closed, resting on raw concrete with a single brass pen across it,
hard side window light, deep shadow, shot on Hasselblad, editorial still life,
contemplative seriousness, no text, no logos, no humans --ar 1:1 --s 150 --v 6.1
```

---

## Manifesto / Foundational-Edition Prompts (full-frame use)

These are the rare cases the image takes the full edition cover frame, with wordmark + edition number layered on top at high opacity. Reserve for the manifesto (Edition 01 if reshooting), milestone editions (every 10th edition), or the year-in-review piece.

```
A vast empty room with a single Tadao Ando concrete wall, one window casting a sharp
rectangle of light onto the polished concrete floor, late afternoon, deep shadow at right,
shot on large-format film, architectural editorial photography, quiet monumentality,
no text, no logos, no humans --ar 1:1 --s 200 --v 6.1
```

```
An abandoned amphitheater carved into raw stone, single overhead beam of sunlight
illuminating the center stone, deep shadows in the perimeter, shot on medium format film,
editorial landscape photography, ancient quiet, no text, no logos, no humans
--ar 1:1 --s 200 --v 6.1
```

---

## Higgsfield Cinematic Prompts (for video Notes / promo clips)

For motion content (rare — Notes are mostly text), the same aesthetic translates to short cinematic clips. Higgsfield Cinema Studio 3.0 prompt formula:

```
[CONCRETE SUBJECT in specific physical state] + [SLOW SUBTLE MOTION — drift, sway, settle,
fall — never zoom-bombing or fast pans] + [SAME LIGHTING as still photography prompts above]
+ [CAMERA: locked-off or very slow dolly, 50mm-85mm equivalent, shallow DOF]
+ [MOOD: contemplative, quiet defiance, settled] + [DURATION: 5-8 seconds]
```

**Example clip prompt:**
```
A single drop of water falling from a copper faucet onto raw concrete, cinematic slow-motion,
single window light from camera-left, shallow depth of field, locked-off camera at 50mm,
quiet morning mood, 8 seconds, editorial cinematography
```

These run on Higgsfield. Output stays in the brand register.

---

## Quality Gate Before Use

Before publishing any AI-generated image as part of a Parallax edition:

1. **Place the image at 20-30% opacity in the bottom-right of the edition cover template.** Does it disappear into texture, or fight the typography? If it fights, kill it.
2. **At full opacity (manifesto-only), does the image have a single readable subject in 0.3 seconds?** If the eye has to hunt, the image fails.
3. **Does it carry one of the brand's emotional tones — quiet defiance, contemplative, settled?** Or does it carry a generic AI-image tone (everything-glowing, hyper-detailed-fantasy, fashion-editorial-shine)? If generic, regenerate with simpler prompts.
4. **Are there any AI-generation tells?** Extra fingers (no people allowed anyway), warped objects, illegible-text artifacts, telltale gradient blobs, oversaturated hero-light. If yes, regenerate or kill.
5. **Does it match the warm-neutral palette?** If the image is teal/orange/cinematic-LUT-graded, it's wrong. Regenerate or grade-correct in post.

If 4 of 5 don't pass, ship the typographic-only cover. The default cover is always good enough.

---

## Update Cadence

This prompt library evolves. Add new prompts when:
- A new edition theme emerges that the existing prompts don't cover
- A specific image worked exceptionally well — capture the working prompt for reuse
- An aesthetic anchor shifts (highly unlikely; the brand is locked at "Muji × Madlib")

Date-stamp additions in this file's header. Never delete working prompts; mark them `(deprecated)` if they stop working with future model updates.

---

## See Also

- [DESIGN.md](../DESIGN.md) — token system the imagery sits inside
- [photography-direction.md](../photography-direction.md) — when to shoot real instead of AI
- [parallax-creative-rebrief.md](../../content/parallax-creative-rebrief.md) — original AI-as-seasoning decision
