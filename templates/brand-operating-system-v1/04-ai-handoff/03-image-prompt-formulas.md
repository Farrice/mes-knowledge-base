# 03 — Image Prompt Formulas (Midjourney / Sora / Runway / Generative Video)

*Daytime-locked prompt scaffolds tuned for {{BRAND_NAME}}'s anchor aesthetic: editorial broadsheet left in actual sunlight. Every prompt below produces output that passes the 11pm test.*

*Last updated: 2026-05-04. Status: canonical.*

---

## The Spine Reminder

> *{{BRAND_NAME}} is heart encounters, not head encounters — a daytime, sober dance party in {{CITY}} for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is {{SUCCESS_METRIC}}.*

---

## What This File Is For

The {{BRAND_NAME}} brand is photography-led. Real photographs of real moments are always the first choice — see `01-visual/photography-rules.md`. AI image generation is **tertiary use only** (textures for IG story backgrounds, mood-board internal references, content blocks where no real photo exists yet, pre-Event-#1 hero placeholders).

This file gives {{FOUNDER_NAME}} the prompt scaffolds to generate AI imagery that doesn't betray the brand. Every formula below has been pressure-tested against the photography rules. Every prompt produces output that:

1. Reads as obviously daytime — the 11pm test passes.
2. Doesn't read as a wellness retreat (the second-most-common AI image failure).
3. Honors the body-centered, decentered-composition discipline.
4. Avoids identifiable AI faces (faces are forbidden in public {{BRAND_NAME}} use).

The single most important rule: **never use AI imagery for the front-of-house hero of an event flyer or web hero**. Those are real-photographer territory. AI lives in the supporting tiers.

---

## Section 1 — The Base Formula Structure

Every {{BRAND_NAME}} AI image prompt obeys the same skeleton:

```
[SUBJECT/SCENE] +
[REAL DAYLIGHT MARKER] +
[REAL ROOM/LOCATION CONTEXT] +
[BODY DIVERSITY MARKER] +
[COMPOSITION DIRECTION] +
[STYLE DIRECTION] +
[BANNED-TOKEN GUARD]
```

### Slot-by-slot breakdown

| Slot | Examples |
|---|---|
| **Subject/Scene** | "two adults dancing together" / "hands at a water station" / "DJ at decks" / "bodies mid-laugh in a converted loft" |
| **Real daylight marker** | "real afternoon daylight" / "south-facing window light at 2pm" / "warm directional sunlight on a wood floor" / "overcast {{CITY}} afternoon" / "sun through a curtain" |
| **Real room/location context** | "converted {{CITY}} loft" / "a 1970s warehouse studio with exposed brick" / "wood floor, cream walls, {{CITY}} window architecture" / "a Pilsen storefront at corner sunset" |
| **Body diversity marker** | "mixed-race adults aged 30 to 40, varied body types, varied gender presentation" / "a Black man in his early 30s" / "a Latina woman mid-30s in a leather jacket" |
| **Composition direction** | "tight crop on hands and gestures" / "decentered framing, subject in the right third" / "candid documentary style, slight motion blur" / "no faces visible" |
| **Style direction** | "documentary photography style" / "minimal color grading" / "Sandro-portrait aesthetic" / "1970s editorial broadsheet feel" |
| **Banned-token guard** | "no flash, no club lighting, no neon, no phones in frame, no alcohol" |

### The single most important slot

**The real daylight marker.** Without it, AI defaults to "moody atmospheric" lighting, which produces 11pm-coded imagery 80% of the time. Always include 2-3 daylight markers.

---

## Section 2 — Banned Prompt Vocabulary (NEVER USE)

These tokens, in any combination, drag the output toward 11pm-coded or wellness-coded imagery. Banned across every {{BRAND_NAME}} prompt:

### Lighting bans (instant 11pm-trigger)

- **"neon"** — instant nightclub
- **"glow"** — instant artificial-light
- **"club"** — instant club register
- **"nightlife"** — instant night
- **"cinematic dark"** — instant night
- **"moody"** — instant low-light
- **"low-key lighting"** — instant night
- **"dramatic lighting"** — instant night-or-stage
- **"ethereal"** — instant wellness-retreat
- **"atmospheric"** — instant low-light
- **"intimate atmosphere"** — instant wellness-or-bar
- **"golden hour"** *as a stylized filter* — produces faked late-afternoon warmth, not real daylight (real golden-hour-on-{{CITY}} at 4pm in May is fine; "golden hour aesthetic" is not)
- **"sunset glow"** — same problem
- **"twilight"** / **"dusk"** — these are not daytime; banned
- **"candlelit"** — banned
- **"firelit"** — banned
- **"backlit"** *without specifying daylight as the source* — banned

### Subject bans (these produce wrong-register output)

- **"nightclub"** / **"dance club"** / **"discotheque"**
- **"bar"** / **"cocktail party"** / **"happy hour"**
- **"singles party"** / **"singles event"** / **"mixer"**
- **"wellness retreat"** / **"yoga studio"** / **"meditation room"**
- **"sacred container"** / **"ceremony"** / **"ritual"** *as setting descriptors*
- **"festival"** *unless specifically daytime + non-neon*
- **"rave"**
- **"VIP"** / **"luxury experience"**

### Style bans (these produce stock/generic output)

- **"professional"** *(in the corporate sense — "professional photography" produces stock-feel)*
- **"perfect"** *(produces overly retouched skin)*
- **"flawless"** *(same)*
- **"glamorous"** / **"glam"**
- **"editorial fashion"** *(without specifying documentary intent)*
- **"vibrant"** *(produces over-saturated output)*
- **"colorful"** *(same)*
- **"high contrast"** *(moves output toward dramatic; we want gentle)*

When in doubt: if the token implies night, low light, ceremony, luxury, or glamour, kill it.

---

## Section 3 — Lighting Language (USE THESE)

The opposite of the banned list — these tokens reliably produce real-daylight output:

### Daylight tokens (always include 2-3 per prompt)

- **"real afternoon daylight"**
- **"south-facing window light"**
- **"north-facing window light"** (cooler, overcast {{CITY}} register)
- **"window light at 2pm"** *(the literal time anchors the model)*
- **"window light at 3pm"**
- **"warm directional sunlight"**
- **"daylight on a hardwood floor"**
- **"sun through a curtain"**
- **"sun through the front window"**
- **"overcast {{CITY}} afternoon"**
- **"flat overcast daylight"**
- **"diffused window light"**
- **"natural light only"**
- **"no flash, no studio lighting"**
- **"shot at f/2.8 on a warm afternoon"**

### Style tokens (anchor documentary register)

- **"documentary photography style"**
- **"Sandro Miller portrait sensibility"** ({{CITY}} photographer; sometimes useful)
- **"slight motion blur from movement"**
- **"minimal color grading"**
- **"candid, not posed"**
- **"1970s editorial broadsheet feel"**
- **"warm cream and midnight blue palette"**
- **"35mm film aesthetic, real grain"**

---

## Section 4 — 12 Named Scene Types With Complete Prompts

### Scene 1 — Dance Floor In Daylight (anchor scene)

```
A mixed-race group of adults aged 30 to 40 dancing together in a converted {{CITY}}
loft at 2pm. South-facing window light pouring across a hardwood floor. Bodies in
mid-gesture, slight motion blur from real movement, varied body types and gender
presentation. Documentary photography style, candid not posed, no faces directly
toward camera. Tight crop on hands and torsos. Warm cream walls, {{CITY}} window
architecture in soft background, no phones in frame, no alcohol, no flash, no
neon, no club lighting. Minimal color grading, real daylight color temperature.
1970s editorial broadsheet aesthetic. --ar 4:5 --stylize 100
```

**Use for**: IG feed background block, web hero placeholder (pre-Event-#1 only — replace with real photography post-Event-#1), email newsletter inline.

---

### Scene 2 — Record On Turntable (atmosphere shot)

```
A vintage soul record on a Technics 1200 turntable, daylight from a south-facing
window catching the vinyl grooves. Tight macro crop. The record label visible but
not centered. A hand entering frame from the side, fingers near the platter.
Documentary photography, real daylight, slight 35mm film grain, warm cream and
wood-floor tones in the negative space. No artificial light, no studio setup, no
neon, no flash. Composition decentered, vinyl in lower-right third.
--ar 4:5 --stylize 100
```

**Use for**: behind-the-DJ-booth content, IG story background, mood-board hero.

---

### Scene 3 — {{FOUNDER_NAME}}-Style DJ At Decks Daytime (placeholder for real photography)

```
A woman in her early 30s standing at a DJ setup with two turntables and a mixer,
head tilted slightly down, focused on the music, hand on a fader. Real afternoon
daylight from a window behind her, warm directional light hitting the side of her
face and the equipment. No identifiable face, slight back-three-quarter angle.
Tight medium crop on hands and equipment. Documentary photography, candid, real
moment of work. Wood floor, cream-painted walls, {{CITY}} loft architecture in
the background. No flash, no club lighting, no fog machine, no neon, no LED
panels, no laser. Minimal color grading. 35mm aesthetic.
--ar 4:5 --stylize 100
```

**Use for**: founder-portrait placeholder ONLY when no real {{FOUNDER_NAME}} photo exists (event #1 first edition). Replace with real photography immediately after Event #1.

**Critical rule**: {{FOUNDER_NAME}} is photographed by humans. AI {{FOUNDER_NAME}} is a placeholder, never a final image, never used in press.

---

### Scene 4 — Pilsen Sunset Corner ({{CITY}} atmosphere)

```
A Pilsen storefront on 18th Street at 5:30pm in late spring, real golden afternoon
sun on a brick wall, the corner of a coffee shop sign visible, a bike chained to a
post. No people in frame OR a single person walking past in soft focus, mid-30s,
hood up. Documentary street photography, 35mm aesthetic, minimal color grading.
The light is real, not stylized. No filter, no faux-bokeh, no lens flare.
--ar 16:9 --stylize 75
```

**Use for**: {{CITY}}-anchor content blocks, the city-context image in a press one-sheeter, IG story location-establishing shot.

---

### Scene 5 — Hands At A Water Station (sober mechanic visualization)

```
A close-up of two hands at a water station, one pouring water from a glass pitcher
into a clay tumbler. Real daylight from a side window catches the water mid-pour.
No labels, no branded glassware, no alcohol of any kind. Wooden table surface,
cream wall in background. Tight macro crop, only hands and forearms visible.
Documentary style, no flash, no filter, slight 35mm grain. Warm and natural.
--ar 4:5 --stylize 100
```

**Use for**: visualizing the no-bar mechanic in content, IG story when discussing the protocol, email newsletter inline image.

---

### Scene 6 — Phones In A Basket (phones-off mechanic)

```
A wicker basket on a small table near an entryway, half-full of smartphones face
down. Real afternoon daylight from a window above, soft shadow cast across the
table. No labels, no logos visible on the phones, no faces, no people. Tight
top-down crop. Documentary still life aesthetic, real and unbranded. Cream wall
background, warm wood table, slight grain, minimal color grading.
--ar 4:5 --stylize 100
```

**Use for**: visualizing the phones-off-the-floor mechanic in content, the protocol-explanation image in pre-event emails.

---

### Scene 7 — Two Bodies Listening (the witness moment)

```
Two adults aged 30-40 standing close to each other in a converted {{CITY}} loft,
not facing camera, listening to music together. Real 2pm daylight from a south-
facing window. Their bodies are close but not touching. One is mid-laugh. Mixed
race, varied body types. Documentary photography, candid, no posed direction,
faces partially obscured (cropped, in profile, or in motion). Slight motion
blur on one body. Wood floor, cream walls, {{CITY}} window architecture.
No flash, no club lighting, no neon. Minimal grading.
--ar 4:5 --stylize 100
```

**Use for**: the heart-vs-head visualization, IG feed lead image, manifesto excerpt card background.

---

### Scene 8 — A Wood Floor In Real Light (texture / atmosphere)

```
An empty hardwood floor in a converted {{CITY}} loft, warm 2pm daylight pouring
across the boards from a tall window out of frame. Real shadows from window
mullions stretching across the wood. Cream walls visible at the edges. Documentary
still life, no people, no objects, just the room about to be filled. Tight low
angle on the floor, light direction obvious. Minimal grading, warm tones, real
afternoon daylight, no studio setup.
--ar 16:9 --stylize 75
```

**Use for**: hero block backgrounds, content texture references, video establishing shot.

---

### Scene 9 — Coffee Cup On A Window Sill ({{ICP_PROFILE_1_NAME}}'s register)

```
A pour-over coffee cup on a window sill in a Pilsen apartment, real morning
daylight slanting through. Mid-30s woman's hand wrapped around the cup,
visible from wrist to fingertips, no face. A leather jacket in the background
on a chair. Documentary still life, candid, real moment. Warm tones, minimal
grading, 35mm grain. No flash, no filter.
--ar 4:5 --stylize 100
```

**Use for**: the {{ICP_PROFILE_1_NAME}}-profile-anchored content (essays about ICP), email newsletter that targets Profile #1 specifically.

---

### Scene 10 — A Record Store Aisle ({{ICP_PROFILE_3_NAME}}'s register)

```
A man in his early 30s standing in a record store aisle, flipping through vinyl
in the soul section. Real Saturday afternoon daylight from front windows of the
store. He is in the right third of the frame, three-quarter back angle, no
identifiable face. Slight motion blur on his hand. Documentary street/portrait
aesthetic, 35mm. Black man, casual but considered clothing, books in his other
hand. Real {{CITY}} record store interior — wood floor, cream walls, vinyl
visible in soft focus background. No flash, no filter, minimal grading.
--ar 4:5 --stylize 100
```

**Use for**: Profile #3 ({{ICP_PROFILE_3_NAME}}) content, the "I have no idea how to do this anymore" moment essay, the quiet-man-targeted content piece.

---

### Scene 11 — A Therapist's Sunday Morning ({{ICP_PROFILE_2_NAME}}'s register)

```
A woman in her mid-30s sitting on a hardwood floor with her back against a
couch, a cup of coffee on the floor beside her, a fiddle-leaf fig in the
corner. Real Sunday morning daylight from a south-facing window. Mid-Caribbean
or Black, wrapped in a long sweater. Three-quarter back angle, no face visible.
Documentary still life with figure, candid, real moment of pause. Soft light,
minimal grading, 35mm. Warm cream and midnight palette. No flash, no filter.
--ar 4:5 --stylize 100
```

**Use for**: Profile #2 ({{ICP_PROFILE_2_NAME}}) content, the "I don't have it in me to perform first-date energy" essay, the wellness-tourist-rejection content piece.

---

### Scene 12 — A Single Crystallized Phrase In Real Daylight (text-on-photo)

```
A single sentence in elegant serif typography, set against a real photograph of
late-afternoon daylight on a wood floor. The text reads "[INSERT MANIFEST LINE]"
in a 1970s editorial serif, midnight blue color, lower-third placement.
The photograph behind it is a real moment — a hand entering frame from the
side, a body in soft focus mid-gesture, real shadow on the wood. Documentary
photography aesthetic with minimal type overlay. No filter on the photograph,
no shadow behind the type. Warm cream and midnight palette.
--ar 1:1 --stylize 75
```

**Use for**: IG feed text-on-photo posts (manifesto excerpts), Story sequence frames, email newsletter inline.

**Critical**: do NOT use AI for the manifest line itself — use the verbatim line from the manifesto. AI generates the visual; the type is set in the brand system.

---

## Section 5 — Negative Prompt Templates (For Models That Support Them)

For Midjourney v6+ and Stable Diffusion based models, append a negative prompt to push against banned tokens. {{BRAND_NAME}}'s negative prompt baseline:

```
--no neon, club, nightlife, bar, alcohol, glass of wine, cocktail, beer,
flash, studio lighting, fluorescent, club lighting, gobos, lasers, fog
machine, smoke, lens flare, glow, moody, dark, low-key, cinematic dark,
ethereal, glamorous, perfect skin, retouched, oversaturated, vibrant
gradient, neon gradient, sparkle, bokeh balls, faux film burn, crowd of
people, large crowd, posed group photo, stock photography, AI faces,
identifiable faces, plastic skin, generated faces
```

For Sora and other video models without explicit negative prompts: bake the negatives into the positive description with constraint phrases — "no flash, no club lighting, no neon, no faces visible, no alcohol in frame."

---

## Section 6 — Five Complete Example Prompts (Tested + Compliant)

### Example 1 — Pre-Event-#1 web hero placeholder

```
Photograph of three mixed-race adults in their early 30s dancing together in
a converted {{CITY}} loft at 2pm on a Saturday. South-facing window light
pours across a worn hardwood floor. Bodies are mid-gesture in real motion,
slight blur from a long shutter. Documentary candid photography, no faces
directly toward camera, no posed group shot. Tight medium crop. Cream-painted
brick walls, exposed-beam ceiling, {{CITY}} industrial window architecture in
soft background. No phones in frame, no alcohol, no flash, no club lighting,
no neon. Minimal color grading, warm afternoon daylight color temperature.
35mm film aesthetic with real grain. 1970s editorial broadsheet feel.
--ar 16:9 --stylize 100 --v 6
```

### Example 2 — IG Story atmospheric block (the wood floor)

```
Late afternoon {{CITY}} daylight pouring through a tall warehouse window onto
a worn hardwood floor in an empty converted loft. Real shadows from the
window mullions stretching across the boards. Cream-painted walls visible
at the edges of frame. Documentary still life, no people, no objects, just
the empty room. Low angle on the floor, light direction obvious. Minimal
grading, warm afternoon tones, real shadows. No filter, no faux-bokeh.
--ar 9:16 --stylize 75 --v 6
```

### Example 3 — Behind-the-decks atmosphere (record-on-turntable macro)

```
Macro photograph of a vintage soul vinyl record on a Technics SL-1200
turntable. Real 3pm daylight from a south-facing window catches the grooves
of the record. The label is visible in the lower-right third, slightly out
of focus. A hand entering frame from the left, fingers approaching the
platter. Warm wood platform around the turntable. Documentary photography,
35mm aesthetic, real grain, minimal color grading. No artificial light,
no studio setup, no neon, no flash. Composition decentered.
--ar 4:5 --stylize 100 --v 6
```

### Example 4 — Sober mechanic visualization (water station)

```
Close-up of two hands at a water station — one pouring water from a clay
pitcher into a small clay tumbler. Real afternoon daylight from a side
window catches the water mid-pour. Wooden table surface, cream wall in
background. Tight macro crop, only hands and forearms visible. No labels,
no branded glassware, no alcohol anywhere in frame. Documentary still life,
warm and natural, minimal grading, slight 35mm grain.
--ar 4:5 --stylize 100 --v 6
```

### Example 5 — Phones-in-basket protocol image

```
Top-down photograph of a wicker basket on a small wooden table near an
entryway, half-filled with smartphones placed face down. Real 2pm afternoon
daylight from a window above, soft natural shadow cast across the table.
No logos visible on the phones, no faces, no people. Tight crop on the
basket. Documentary still life aesthetic. Cream wall background, warm wood
table, slight 35mm grain, minimal color grading. No flash, no filter,
no faux-warmth.
--ar 1:1 --stylize 100 --v 6
```

---

## Section 7 — Iteration Protocol

If the first generation doesn't pass the 11pm test:

1. **Strengthen the daylight markers**. Add "shot at 2pm" / "real Saturday afternoon daylight" / "south-facing window" — anchor the literal time.
2. **Add specific {{CITY}} context**. "{{CITY}} loft" / "Pilsen storefront" / "Wicker Park warehouse" — geography pulls the model away from generic "club" defaults.
3. **Cut adjective-heavy phrases**. "Atmospheric, intimate, beautiful, captivating" — these all drift the output toward stylized warmth that reads as faked light.
4. **Reduce stylization**. Lower `--stylize` to 50-75 from default 100. Less stylization = closer to actual photography.
5. **Iterate banned-token guards**. If output still drifts night-coded, add specifically: "no flash, no club lighting, no neon, no glow, no moody atmosphere, no cinematic dark."

If after 3 iterations the output still fails: **do not ship the AI image**. The brand fails forward into "we needed a photographer." Wait for a real shot.

---

## Section 8 — When Not To Use AI Imagery (the discipline)

AI imagery is **forbidden** for these surfaces:

- **Front-of-house event flyers** (digital or print). Real photography only.
- **Web hero (post-Event-#1)**. Real photography from the actual room only.
- **Press one-sheeter founder portrait**. {{FOUNDER_NAME}} is photographed by humans.
- **Press one-sheeter event imagery**. Real photography only.
- **Founder portraits of {{FOUNDER_NAME}} anywhere, ever**. AI {{FOUNDER_NAME}} is forbidden across the entire system.
- **Identifiable faces of attendees**. Faces are forbidden in AI imagery for public {{BRAND_NAME}} use, full stop.
- **Couples-formed story imagery**. Couples are real or they are not — AI cannot fabricate their existence.

AI imagery is **allowed** (with the formulas above) for:

- IG story atmospheric blocks where no real photo exists.
- Mood-board internal references.
- Pre-Event-#1 web hero placeholder (replace immediately after Event #1).
- Texture and atmosphere in content blocks (wood-floor light, hands-not-faces, record-on-turntable macros).
- Tertiary surface backgrounds.

The discipline is: real moments are the brand. AI is a placeholder for moments that haven't happened yet.

---

## Section 9 — Voice Test For AI Image Prompts

Before sending any prompt to the model, run this 4-point check:

1. **Daytime markers present** — at least 2 daylight tokens?
2. **Real-room context named** — converted loft, {{CITY}} window architecture, etc.?
3. **Body diversity specified** — mixed-race, varied bodies, varied gender presentation?
4. **Banned tokens absent** — zero instances of neon, club, glow, moody, ethereal, golden-hour-as-filter, cinematic dark, atmospheric, intimate-atmosphere?

If any check fails: rewrite the prompt before sending. Each model token costs cycles; iterate the prompt before the spend, not after.

---

## Source Citations

- `01-visual/DESIGN.md` Appendix — Photography Direction (binding summary)
- `01-visual/photography-rules.md` §6 — AI Image Generation, Daytime-Locked Prompting (the canonical rules this file expands)
- `01-visual/aesthetic-references.md` — the visual register this file's prompts produce toward
- `00-foundation/02-icp-master.md` Sections 2-4 — profile-specific scene direction
- `00-foundation/05-non-negotiables.md` Lines 1, 2, 8 (daytime, sober, phones-off) — the mechanics this file's scenes visualize
- `04-ai-handoff/00-ai-brain-master.md` — the cold-start that should accompany any AI session producing imagery
- `04-ai-handoff/02-prompt-library.md` Prompt 16 — the meta-prompt that uses this file as a reference
