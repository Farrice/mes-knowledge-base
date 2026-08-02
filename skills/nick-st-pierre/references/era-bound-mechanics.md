# ERA-BOUND MECHANICS — VERIFY BEFORE USE

> **This file is quarantined on purpose.** Everything below is tool- and version-specific syntax
> from Nick St. Pierre's Midjourney-era teaching, dated 2023-02 to 2025-06. Models, parameters and
> defaults have moved since. **None of it is the craft.** The craft is in `SKILL.md` and
> `genius.md`; this file exists so the historical specimens stay readable without contaminating
> the durable layer.
>
> **Rule of use:** never copy a parameter from this file into a live prompt without checking the
> current tool's documentation first. Read it to understand *what decision* the parameter was
> standing in for, then find that decision's current control surface.

---

## 1. The 2023 Additive Prompting syntax — SUPERSEDED BY HIS OWN LATER GUIDANCE

**Dated 2023-02.** Comma-separated slots in a fixed order.

Base template (2023-02-04): `[Shot Type] photo of [Subject], shot on [Film Type]`

Grown across the series (2023-02-04 → 2023-02-07):
```
street style photo of a woman, shot on Kodak Gold 200 --q 2 --v 4
street style photo of a woman, [lighting], shot on Kodak Gold 200 --q 2 --v 4
street style photo of a woman, [shot type], [position], natural lighting, shot on Agfa Vista 200 --v 4 --ar 16:9
street style photo of a young woman wearing [designer], [color], [material], wide shot, natural lighting, soho, shot on Agfa Vista 200, 4k --ar 16:9
```

The interiors schema (2023-02-23, his highest-reach craft thread, 1.3M views) — slots in a fixed
order, with his ordering rules:

```
Editorial Style Photo, [Camera Angle], [Style] [Room Type], [Focal Point], [Material], [Material],
[Material], [Detail], [Palette], [Brand Reference], [Lighting], [Setting], [Time of Day],
[Mood], [Style Descriptor], [Style Descriptor], 4k --ar 16:9
```

Verbatim specimen: `Editorial Style Photo, Off-Center, Mid-Century Modern, Living Room, Eames
Lounge Chair, Wood, Leather, Steel, Graphic Wall Art, Bold Colors, Geometric Shapes, Design Within
Reach, Track Lighting, Condo, Morning, Playful, Mid-Century Modern, Iconic, 4k --ar 16:9`

His stated rules for it (all 2023-02-23):
- *"Notice the order of the variables remains consistent."* / *"The order of the variables does matter."*
- *"Front-load the prompt with the camera angle. You'll get more consistent results that way."*
- *"It's important to include at least 1 or 2 texture references like metal, linen, wood, etc."*
- *"Adding too many specific furniture items can sometimes confuse it. I try to limit myself to 3 max."*
- *"Brand references like 'Pottery Barn' help define style."*
- *"Adding 1 or 2 general descriptors at the [end] will help you define the look."*
- *"It doesn't need to be an 'Editorial Style Photo' but I find it helps."*
- *"Materials don't always need to be tied to an object. MJ figures it out."*
- Claimed result: *"90%+ coherence to the prompt"* (his claim, unverified here).
- Honest limit: *"The images aren't picture-perfect. They can be a bit blurry at times."*

**⚠️ SUPERSEDED.** On 2023-12-30 he listed under *Things to avoid*: **"Prompts that are just
comma-separated keywords."** The v6-and-later guidance is conversational sentences. What survives
from this section is **the slot inventory** (which decisions an interior shot needs) and **the
ordering discipline** — both promoted into `SKILL.md`. The comma syntax itself is dead.

---

## 2. Midjourney parameters he taught (2023–2025) — check current docs before use

| Parameter | Era | What he used it for | Durable decision underneath |
|---|---|---|---|
| `--v 4` / `--v 5` / `--v 6` / `--niji 6` / `--v 7` / `--v 8` | 2023-02 → 2026-03 | model selection | which engine's defaults you are directing against |
| `--q 2` | 2023-02 | quality | render budget |
| `--ar 16:9`, `--ar 2:1`, `--ar 3:2`, `--ar 3:4`, `--ar 4:3` | throughout | frame shape | **the single strongest "cinematic" lever** (see genius.md Pattern 4) |
| `--seed` | 2023-02 → | reproducibility across single-variable changes | a fixed random state so a sweep is a real comparison |
| image URL prefix (`https://s.mj.run/…`) | 2023-02 | image prompting / character lock | reference-driven direction |
| `--sref` (style reference) + `--sw` (style weight) | 2024-01 → | drive aesthetics from an image; dial its influence | style library + strength dial |
| `--cref` + `--cw` (character reference / weight) | 2024-03 | character consistency | cast-and-carry |
| `--style raw` | 2024-01 | more literal, more photographic interpretation | a "listen to me literally" mode |
| `--stylize` | 2024-03 | model's aesthetic opinion vs your instruction | how much the engine is allowed to editorialise |
| `--tile` (with `--ar 2:1`) | 2024-01 | 360º photos | seamless/wraparound output |
| `--weird`, `--no`, `--exp`, `--chaos` | 2024–2025 | oddness, exclusion, detail/dynamism, variety | deviation controls |
| Remix mode on/off; Vary (Region) | 2023–2024 | edit strength | *"remix mode results in more drastic changes, while regular variations are great for creating unique changes in things like clothing"* (2023-02-18) |
| Personalization, moodboards, style creator | 2025-12 → | visual-first aesthetic control | **the current centre of gravity** — see `SKILL.md` Pillar 4 |
| big-batch draft + `--sref random` | 2026-06 | *"explore style space 24x faster"* | the industrialised sweep |

His own framing of why parameters matter at all (2025-06-30): *"This is where a lot of the MJ
magic lives, and how you can start to really tune aesthetics and styles to your exact
preferences."* Read: parameters are **taste dials**, not settings.

---

## 3. The 2023 character-lock recipe (MJ v4/v5 era)

**Dated 2023-02-18.** Reproduced for the shape of the method, not the syntax.

1. Generate until you have a face worth casting. *"it seems to work best with a head and shoulders
   portrait photo."*
2. Capture its seed (react with ✉️, or set `--seed` while iterating).
3. New prompt = **image URL + the same prompt + the same seed**, then change one variable class
   at a time — clothing, camera perspective, lighting, or location.

Verbatim specimen chain:
```
1960s street style photo of a young woman, latina, dior, silk, diamonds, dress, wide shot, natural lighting, soho, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622
https://s.mj.run/YuSa9350SyA 1960s street style photo of a young woman, sitting, latina, dior, silk, diamonds, natural lighting, soho, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622
https://s.mj.run/YuSa9350SyA 1960s street style photo of a young woman, sitting, park bench, latina, dior, silk, diamonds, natural lighting, central park, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622
https://s.mj.run/YuSa9350SyA 1960s beach style photo of a young woman, sitting, latina, dior, silk, diamonds, side view, side angle shot, sunset, beach, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622
```

His notes (2023-02-18): distinct-looking faces lock better; keep variables close to the originating
prompt; the seed is helpful but not strictly required once you are feeding a reference image;
remix mode OFF for subtle wardrobe changes.

**Current status:** dedicated character-reference features and multi-image conditioning have
replaced the URL+seed trick on every major model. **The durable part is the sequence** — cast,
lock, then change exactly one variable class per shot — which is in `SKILL.md`.

---

## 4. The image-blending finding (2023-02-26)

Verbatim: *"Image blending in Midjourney & Realism… I tried most of the methods out there & it can
work, but it's not the most consistent or reliable."*

Two constraints he found, both of which are **physics, not MJ trivia, and still true on current
models**:
- *"I need the lighting in the source images to match to achieve realism"*
- *"I get locked into the perspective of my source images"*

And the strip-down rule when blending: *"I removed a lot of variables from the original prompts…
best results when only keeping the shot type, subject, pose, location style, lighting, and
descriptors. **The images fill in the rest.**"*

The finding that came out of it — character prompt + interior prompt = a cinematic shot — is
promoted into `SKILL.md` as Composite Direction.

---

## 5. Weighted prompting — he rejected it

**2023-02-26.** He ran ~50 variations with `::` weights and concluded it wasn't for him. His
reason, which is a taste position worth keeping (2023-02-27):

> "I just get frustrated prompting like that cause often times it feels totally out of my control
> and random."

**Durable principle:** prefer control surfaces you can reason about over ones that require
brute-force search. Keep this in mind before adopting any weighting/CFG-style dial.
