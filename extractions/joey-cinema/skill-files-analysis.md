# Joey's Skill Files v3.0 — Deep-Read Analysis (Forge-Tier Extraction Input)

**Analyst pass date:** 2026-07-13
**Source:** unzipped at `/private/tmp/claude-501/-Users-farricecain-Google-Antigravity/4b8ffb83-2cf6-409e-b23d-3ed9f279b3c1/scratchpad/joey-skills/`
**Files read (complete):**
- `banana-pro-director-30/banana-pro-director-30/SKILL.md` (1,117 lines)
- `cinema-worldbuilder-pro-30/cinema-worldbuilder-pro-30/SKILL.md` (524 lines)
- `story-bible-builder/story-bible-builder/SKILL.md` (200 lines) + `character-interview.md` (137) + `character-section-format.md` (55) + `example-bible-excerpts.md` (115)

---

# 1. PER-SKILL INVENTORY

## 1.1 `banana-pro-director-3.0` — Image Asset Builder (Higgsfield stills)

**Purpose.** The locked image-prompt grammar for photorealistic Higgsfield stills across three image models — Banana Pro (Nano Banana), Soul Cinema, and Higgsfield GPT-2. Produces character identity assets (face locks, outfit references, character sheets) and cinematic scene plates. The skill's job "ends at the code block" — it is a prompt director, not a generator (no API calls, no aspect ratios, no `@image` placeholders; all attachment happens in the Higgsfield UI).

**Modes (strict order, enforced):**

| Mode | What | Tool routing |
|---|---|---|
| **0 — Face lock** (new characters only) | Canonical identity reference. Two stages: text spec (mirrored back, iterated, locked) → build. Tool fork: **0.A Banana Pro single-pass (default)**, **0.B GPT-2 single-pass** (highest fidelity, chest-up only, more credits), **0.1+0.2 Soul Cinema two-pass** (cheap exploration → Banana Pro 3:4 lock). Locked baseline wardrobe: plain black thin-strap camisole (women) / plain black ribbed tank (men) — no jewelry, logos, styling. One-and-done per character. | Banana Pro / GPT-2 / Soul Cinema→Banana Pro |
| **1 — Single-image character outfit** (base outfit reference) | First image of any character/outfit pairing. **1A Banana Pro** (full styling written from prompt — simpler outfits) or **1B Soul Cinema two-step** (Step 1B.1 outfit on a bland slim neutral model on gray; Step 1B.2 composite outfit ref + character ref). User picks at a mandatory fork question. | Banana Pro or Soul Cinema |
| **2 — Character sheet** | Only after an approved Mode 1 base. **2A 3-panel is the locked default** (headless full-body front / full-body rear head attached / tight chest-up face lock). **2B 6-panel is legacy, explicit-request-only, never proposed** — one resolution warning, then build on go-ahead. | Banana Pro |
| **3 — Scene plates** | 3A character-in-environment, 3B pure environment. Never proposed proactively. Written in the **cinema-prose register** (five unlabeled paragraphs), the only mode with directional lighting. Output feeds Seedance video. | Banana Pro |
| **4 — GPT-2 detail** | Chest-up/face-detail only, explicit request only, credit-cost warning once per conversation. Classical beauty lighting allowed here. | GPT-2 |
| **5 — Outfit replacement** | Two-reference swap: @image1 = outfit/pose source, @image2 = character/identity source (order fixed, reversing breaks the swap). Single locked lean prompt, character/IP-agnostic, no per-character modifiers. | Banana Pro |

### LOCKED defaults and rules

**18% gray seamless + flat shadowless grade (locked default for ALL character work — Modes 0/1/2/4/5).** Pure white is the explicit-request exception (finished standalone deliverable stills only); even then **the flat grade stays** — "Flatness never comes off."

*Why (stated):* "Pure white (and pure black) seamless creates maximum subject-to-background contrast. Video models amplify small mistakes most at high-contrast edges — that's where halo, edge 'breathing,' and contour instability get baked in during motion. A neutral mid-gray ground lowers the subject-to-background contrast, which means cleaner edge extraction and far less inherited contrast and plastic when the still is read as a reference frame... Because virtually all character plates eventually seed downstream video work, gray is the correct standing default."

*Why flat / zero lighting information (stated):* "These plates are references, not finished frames. Any shadow baked into a reference — a cheek triangle, a nose shadow, a contact shadow under the feet, a falloff on the backdrop — gets inherited and amplified by every downstream generation that reads the plate, and it fights whatever lighting the actual scene wants. So the character plate carries **zero lighting information**... the scene plate or video prompt does all the lighting later."

**The three non-negotiables of every flat close:** (1) flat backdrop — one uniform 18% gray value, no seam/gradient/hotspot/vignette/falloff; (2) shadowless illumination — huge frontal source, matched fill L/R/above/below, no key-and-fill ratio, no rim/hair light/kicker/specular hotspot; (3) zero cast shadow — no background shadow, no contact shadow, no ambient occlusion. "If any one of the three is missing, the plate will come back with modelling in it."

**Verbatim — the LOCKED FLAT GRADE close (gray plate lighting close):**

```
Background is an even 18% neutral gray seamless, completely flat — one single uniform value corner to corner, no seam line, no gradient, no hotspot, no vignette, no falloff to lighter or darker anywhere in the frame. Relight from scratch overriding any reference lighting: completely flat shadowless illumination — one enormous soft frontal source at camera position wrapping the subject evenly, matched equal fill from camera-left and camera-right at identical intensity, matched fill from above and below, so both sides of the face read at exactly the same brightness. No key-and-fill ratio, no modelling, no shadow side, no cheek triangle, no nose shadow, no under-chin shadow, no rim light, no hair light, no kicker, no specular hotspot. Zero shadow cast onto the background — the backdrop stays clean flat gray behind the entire figure. No contact shadow, no drop shadow, no ambient occlusion anywhere in the frame. Extremely low contrast, even, milky, catalogue-flat. Form is described by bone structure, hair strands, and fabric folds alone, not by light and shadow. Skin reads matte and velvety — zero shine on forehead, nose bridge, cheekbones, temples, and chin, no oily T-zone. Skin renders at its true natural skin tone and wardrobe at its true natural color, warmth preserved and natural against the neutral gray, never pale or washed-out or cool-shifted by the background. Real peach fuzz at the jaw and hairline, real soft fine even pore texture, subsurface scattering reading as semi-translucent biology, never plastic, never waxy AI render, never glass-skin, never harsh — fine flattering texture that keeps the face looking good, no acne, no blemishes, no rough pores. Photographed on a 50mm prime, even sharpness, soft natural film grain. Photographed not generated.
```

*Companion rule:* "The background stays neutral; the character does not" — the gray must never cool/wash the subject; skin and wardrobe render at true natural color, held by the "Relight from scratch" + "warmth preserved" clauses.

**Verbatim — THE CINEMA STACK (locked; documented for Mode 3 and the white-card standalone exception; NEVER appended to flat character plates):**

```
Real human skin captured on a real cinema camera — refined and real, peach fuzz catching light along the jawline and hairline, real natural pore texture soft fine and even, subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed reading as semi-translucent biology never opaque plastic. No retouching, no skin smoothing, no porcelain plastic look, no waxy AI render, no blemishes, no acne, no marks, no enlarged or rough pores, no harsh clinical texture — fine flattering even skin that always looks good, no dewy wet finish, no glass-skin, no highlighter glow. Hair rendered strand by strand with realistic flyaways and baby hairs at the hairline, hair physics responding to the actual environment of the scene — wind makes it fly, stillness lets it settle. Fabric with real weave detail, real weight, real drape. Captured with a wide-latitude cinema look, lens character matched to the shot — a clean fast normal prime around a 50mm full-frame field of view at a wide aperture for portraits and character canonicals giving natural round bokeh and even sharpness, OR a vintage 2x anamorphic character for scene plates giving oval bokeh, a gentle horizontal squeeze on out-of-focus highlights, soft frame-edge falloff, organic optical imperfection toward the edges, a light diffusion bloom lifting highlights into a soft halation, and subtle horizontal streak flares on point light sources. Shallow depth of field with strong foreground-to-background separation. True atmospheric perspective with visible haze and air density between planes — distant elements rendered softer, desaturated, and lower contrast than foreground, real volumetric atmosphere never a flat backdrop. Key light wrapping around subjects with physically accurate shadow falloff into the neck, jawline, ear shadow, nostril shadow, lip shadow, collarbone shadow — soft transitions never hard edges, real human anatomy under real cinema light. Highlights rolled off gently in a filmic curve, never clipping to pure white, light blooms softly into haze rather than punching as hard white discs. Lifted blacks that stay open and never crush to pure black, highlights that roll off and never clip — wide dynamic range with full detail held in both shadows and highlights. Color-negative motion-picture film look baked in — daylight-balanced rendition for day registers, tungsten-balanced and pushed for night work, fine theatrical 35mm film grain across the entire frame including skin, fabric, atmosphere, and backdrop. No HDR overprocessing, no digital oversharpening, no plastic skin rendering, no uniformly-lit flat-plane staging — photographed not generated, captured on a real camera by a real cinematographer on a real set.
```

The skill names its own five most powerful phrases and why each earns its place:
- "atmospheric perspective with visible haze and air density between planes" — forces multi-plane depth; biggest fix for the "video game" look
- "shadow falloff into the neck, jawline, ear shadow, nostril shadow" — fights the AI uniform-lit face
- "subsurface scattering at ear edges, nostrils, and around the eye sockets with warm undertone bleed" — fights plastic skin at the biological level
- "highlights rolled off gently in a filmic curve, never clipping to pure white" — fights the blown-bright digital highlight
- "photographed not generated, captured on a real camera by a real cinematographer on a real set" — "surprisingly strong negative signal against AI uniformity at the language level"

For pure environment plates: drop human-skin/hair/SSS/anatomy-shadow lines, keep lens character + atmospheric perspective + light physics + log curve + grain + closing realism clause.

**Verbatim — NIGHT CINEMA REGISTER (target: Justin Lin / James Wan / Greig Fraser — Tokyo Drift, Fast 5, Furious 7, The Batman, John Wick):**

Critical principle: "theatrical night cinema is **mostly dark, with hard punchy practicals cutting through**. NOT saturated-teal-everywhere. NOT bright-night." Two modes:

- **A. Exterior canyon / open night:** "Light comes EXCLUSIVELY from practical sources in the scene (headlights, brake lights, dash glow leaking out doors, distant city glow). No ambient moonlight, no ambient sky lift. The sky and surroundings are committed to deep crushed near-black darkness... Atmospheric haze suspended in air catches headlight beams as visible warm white volumetric god rays... Everything outside the headlight throws and their immediate backscatter falls into deep crushed near-black shadow. The cars themselves read primarily as silhouettes against the night sky with their headlight glow defining their forward edges."
- **B. Interior / urban / lit night:** practical-driven — sodium-vapor, fluorescent, neon, dash glow, brake lights; "Teal-amber color split can read here because practical sources motivate it."
- Universal night rules: deep contrast where "shadows are deep but hold information, highlights are hot but don't clip into mush"; "Practicals punch hard... Light HITS the scene with purpose, not softly diffused into mush"; volumetric haze catching beams; rim/edge definition ("Never silhouettes that disappear, never flat-lit faces"); "Skin reads warm against cool ambient... Practical light sources warm one side of the face — natural face-side-lighting from real cinema gaffer work."

**The flattering-realism ceiling (LOCKED, every face, every mode).** "Full skin realism is always on — visible pore texture, peach fuzz... But realism never means *unflattering*... no acne, no blemishes, no prominent spots, no scarring, no enlarged or cratered pores... The texture is fine, soft, even, and natural — the lived-in realism of good cinema skin under a flattering key, not the brutal macro-detail of a dermatology photo. Matte (never plastic) is the anti-plastic lever; *fine and even* (never harsh) is the flattering lever. Both are always on together. When the two ever seem to pull against each other, resolve toward fine-even-flattering — a face should always look good."

**Pre-prompt confirmation rule (universal).** Every prompt gets a short bulleted "here's what I'm about to prompt, sound good?" check before delivery. *Why (stated):* "Long prompts are expensive in attention and copy-paste effort, and the user shouldn't have to wait on a wall of text only to discover it missed the mark." Format: clean bullets only, one opening line, **references listed FIRST always** — "this confirms back to the user that every reference image they uploaded is being read and accounted for... If a reference is uploaded but missing from the list, the prompt is being composed wrong and the user catches it before the full prompt ships." Order: References → Character → Outfit → Backdrop → Framing (if non-default), close with "Sound good?" **Exception:** minor iteration on a just-approved prompt in the same thread (composition tweak, pose change, lighting nudge, single wardrobe swap) skips the check — "Re-confirming on tiny deltas creates friction." Still triggers a check: new character, full outfit swap, new mode, new environment, or user asks.

**Lean-prompt / reference-trust doctrine.** "The references show the model what things LOOK like. The prompt tells the model how to FRAME them." One distinguishing visual handle per subject; "A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time"; "Banana Pro reads the front of the prompt most heavily; loading the front with composition + pose + light gets better results than burying those decisions under visual description." Rule of thumb: "if a sentence in the prompt re-describes something that's already visible in an attached reference, cut it unless it's load-bearing for the composition or action."

**Identity-hygiene rules (all CRITICAL/locked):**
- **Naming rule:** "Never use proper names in the prompt output... Higgsfield does not know names. Visual descriptors survive across prompts; names do not."
- **Brand name rule:** never real brands/protected IP in prompt output — "black three-stripe athletic sneakers not specific brand names." Chat can name brands; the prompt must be brand-neutral.
- **Age-blind rule:** never *boy, girl, child, kid, young, teen, little, middle-aged, elderly, old* — describe by role, build, clothing.
- **No-invention rule:** never invent wardrobe/styling not in the reference or request; ask before composing.
- No teeth-showing smiles unless requested (default "model face-card neutral, subtle controlled, slight closed-lip smirk at most").
- No negative-prompt blocks (Higgsfield doesn't use them); no aspect ratios in prompt body (set in UI); no `@image` placeholders except Mode 5's locked prompt; no internal production context ("matching the previous scene"); single fenced code block delivery; English prompt output.

**Mode 2A 3-panel rationale (verbatim):** "the sheet is one image with a fixed pixel budget. Six cells splits that budget six ways, and the face — the one thing the sheet exists to lock — lands in cells too small to hold real identity detail. Three cells give each panel roughly double the resolution."

**The headless cut — two variants by garment:** Variant A ghost mannequin (structured/closed necklines — collar holds shape, "empty dark hollow looking down into the inside of the garment," inner back of fabric faintly visible); Variant B clean neck cut (strapless/halter/plunging — neck "terminates in a clean, flat, sharply defined horizontal edge at the base of the throat, exactly like a headless dress-form mannequin"). Both ship with the same suppression stack: "not blurred, not faded, not dissolving, no wisps, no smoke, no ghosting, no transparency in the body, no stump, no anatomy detail at the cut, no blood, no gore." Hair goes with the head. Full headroom preserved ("This is not a crop. The head is *removed from the body*"). *Why headless:* "The panel exists to isolate the garment, the silhouette, and the body proportions with zero facial data competing for the model's attention." **Skin-tone consistency clause is mandatory on sheets:** "Rear panels drift darker/tanner without it."

**Mode 3 cinema-prose register (locked, non-negotiable).** "Mode 3 prompts are written like a DP describing a real frame, not like a spec sheet." Five-paragraph structure (unlabeled): (1) opening shot sentence — medium, framing register, subject at high level, camera position, mood; (2) character block (references carry identity: "carrying identically from the attached character reference"); (3) world as ambience not architecture; (4) subject anchor (the focal element); (5) camera spec + finish ending in the mandatory closing realism clause: "Real photographic frame captured on a real cinema camera, real anamorphic lens, real fabric, real human subject, real concrete and haze — no CGI, no rendered look, no digital cleanliness, no plastic surfaces, no AI smoothness, no skin smoothing, no glow, no halation bloom that reads as artificial, no glossy highlights." *Why negations at the end:* "it tells the model what NOT to lean toward, and it does so AFTER all the positive description, where the model handles it as a quality filter rather than a conflicting instruction." *Why prose beats coordinates (stated):* "The model responds to confident scene description, not coordinate grids... Over-specification creates conflicting instructions; the model trusts plain language more than rule-blocks." The old labeled-block/X-Y-coordinate grammar is explicitly deprecated: "It made the model overcorrect and confuse spatial relationships." The 6-bucket checklist (Shot DNA / Subject+placement / Visible detail / World / Light / Camera+finish) and the X/Y rule-of-thirds library survive as SILENT planning tools with a coordinate→prose translation table.

**Resolution-aware detail rule (locked).** "Describe what the camera at this position can physically see, not what's 'true' about the subject." Three silent diagnostics: would this lens at this distance resolve it? would it read at this motion blur? would it be visible at this lighting? "Detail is earned by camera proximity, lens length, motion stillness, and lighting intensity."

**Verbatim — Mode 5 locked prompt (do not modify):**

```
Replace the character in @image1 with the character in @image2. Keep the outfit and pose from @image1 exactly. Match the face, bone structure, body type, skin tone, and hair from @image2. Clean mid-gray seamless studio background, even neutral mid-gray with no seam line, soft large-source studio lighting, skin and outfit rendering at their true natural tone against the neutral gray, natural film grain, full body framing.
```

*Why locked/lean:* "adding texture stack language on top of a swap operation creates conflicting instructions and degrades the identity transfer. The lean prompt structure is the entire point of this mode. Trust the references."

**Quality gates:** the Inventory Extraction Checklist (run silently before composing — 20+ items: mode + rationale, every reference catalogued, Mode-0-before-Mode-1 dependency, 2A default enforcement, headless variant picked from garment, skin-tone clause present, resolution-aware pass, five-paragraph structure, flat-grade close, references-first confirmation). "If anything needed for composition is missing from the user input, ask before writing."

**Mode 1A variation strategy:** when building a series of bases, keep gray backdrop locked and vary ONE parameter per shot (pose / framing / expression / lighting direction); "Don't vary face, skin, or core identity markers. Those stay locked."

*(Internal inconsistency noted for the forge pass: a few v2 remnants survive — the Mode 0 "Goal" line still says "a clean, locked face on white background," and Mode 0/1B pre-prompt checks list "soft soft natural light from camera-left/right" while the actual locked prompt bodies specify flat shadowless matched-fill light. The locked prompt text and Rule 12 are unambiguous — gray + flat wins — but an install should not propagate the stale lines.)*

## 1.2 `cinema-worldbuilder-pro-30` — Seedance Video Director

**Purpose.** Locked cinematography grammar for Seedance video prompts (run inside the Higgsfield UI): picks a cinema mode, maps the frame, locks every subject to screen position/state, choreographs motion as observable action, fixes the closing composition, outputs a production-ready block-structured prompt with diegetic audio only. "A great prompt is a production document, not a beautiful sentence."

**Core philosophy.** Same anti-plastic creed as Banana Pro: "No plastic. No commercial gloss. No LED-panel-rendered-on-a-soundstage energy. No Instagram-ad sharpness. Every frame reads as captured on a camera that has lived a little." Five modes share one capture register; "Differences live in **movement, diffusion, grade, palette, and texture** — not in capture register or lens family."

**Density rule:** 280–400 words single-shot, up to 600 multi-shot. "Every word does work. Trust references to carry visual identity."

**WRITE THE VISIBLE (core principle).** "Seedance is a physics engine, not a mood board. It renders things it can see and count. Mood words evaporate." Measurables Seedance actually reads:
- **Speed in km/h** (never "fast"); **atmosphere in % density + meter visibility** ("haze 30%, readable to 40 meters"); **scale by stacking humans** ("as tall as three humans standing on each other's shoulders" — never "three meters tall"); **direction from the camera's POV**; **emotion rendered in muscle** ("jaw sets, breath quickens, knuckles blanch" — never "sad" without a body cue); **environmental contact rendered physically** (snow gathering on the shoulder, rain darkening fabric).
- Final test: "Read the prompt back as if watching the shot... If a word doesn't produce a visible pixel, cut it."

**POSITIVE PHRASING (locked).** "State what happens. Do not state what shouldn't. Negative language weakens the signal — the model sees the noun and rounds toward it." E.g. ❌ "the camera doesn't shake" → ✅ "locked-off tripod, zero operator drift, frame edges rock-steady." Sanctioned exceptions only: on-screen text suppression at the close of Last Frame, specular-kill/anti-plastic phrasing inside Capture Realism, "no music, no dialogue" in Sound Bed.

**Element tags (new in 3.0).** User-supplied `@tag` names replace `@image1–9` indices: lowercase underscore, `_ref` suffix for characters, `_plate` for environments, descriptive noun for props ( `@sol_ref`, `@berlin_bunker_plate`, `@white_camaro`). "Never invent tag names on the user's behalf" — ask in pre-prompt check; once locked, tags carry across the session. **Canonical-over-plate rule (HARD LOCK):** "Every named subject... gets its canonical reference tagged separately — even if that subject is also visible in the rendered environment plate... The plate carries the world (location, weather, light, set dressing); canonical references carry identity (face, body, livery, markings, silhouette)."

**Session opener — character gate.** First Seedance prompt of a session: "Any recurring characters in this batch? ...already built (reference locked) or do we need to develop them first?" Needs-developing branch explicitly "kick[s] to a character build skill (Banana Pro director or equivalent). Return to Seedance once locked." Ask once per session.

**Pre-prompt confirmation:** mandatory for every NEW scene; bullets ordered Tags → Mode → Scene → Subjects → Frame Map → Camera → Cuts → Runtime. "Why tags first: they confirm the reference set. Why runtime last: most important spec to lock, sits right above 'Sound good?' for eye-catch." **Never assume runtime — ask.** Skip only on iterations, pre-confirmed batches, or explicit "skip."

**Block order (locked, delivered as bolded title + one fenced code block):**
`Scene & Mood → Frame Map → Subject Lock(s) → Cross-Frame Rules → Movement → Last Frame → World Plate → Sound Bed → Capture Realism → Camera Capture`

Key block rules:
- **Subject Lock** — one discrete block per subject; identity tag + orientation + pose + state + gaze + contact points + state-changes the reference can't carry (damp, torn) + lock-down line ("face, hair, wardrobe, and silhouette identical throughout"). Wardrobe visible in reference NOT re-described.
- **Cross-Frame Rules** — "*@tag1 and @tag2 never swap positions, never cross center, never change depth. Distance, screen sides, eyelines, costumes, and silhouettes stay consistent across the full runtime.*"
- **Movement** — four layers in order: character motion (km/h, per-beat timestamps) / micro-motion (breath, hair, fabric, jewelry) / environmental motion (% density, meters) / camera. "Each named explicitly, even when the layer is 'nothing else moves.' Saying nothing moves is a directive; absence is not."
- **Last Frame** — exact closing composition + mandatory suppression line: "*No on-screen text, no captions, no signage typography, no rendered text in the frame.*"
- **Sound Bed** — diegetic only; "Never: song names, lyrics, 'music plays,' score descriptors, genre cues." Mode 2 silent-capture opt-in only.
- **Camera Capture** — the ONLY camera/grade/stock language in the whole prompt, single line, bottom position. **Default camera energy is handheld** ("Lived-in operator presence is part of the cinema register"); locked-off tripod is OPT-IN only.

**DISTRIBUTED STYLE (locked).** "No style header at the top of the prompt. Style isn't a single object — it splits across many aspects, and each aspect belongs inside the block that carries it. Putting a style prefix on the prompt scatters the model's attention; anchoring each aspect to its home block concentrates it." Full aspect→home-block table (lighting→World Plate/Movement/Last Frame; color→World Plate + Camera Capture, "attach every color to a fabric, surface, or light source... never a bare palette list"; skin→Capture Realism; composition→Frame Map; continuity→Cross-Frame Rules; grain/fps→Camera Capture).

**FOV DEGREE TABLE (new in 3.0 — the lens anchor).** "Seedance latches onto FOV in degrees as a snap value... Millimeters read as suggestion; degrees read as instruction. Multishot sequences that only name mm drift lens character between beats. Degrees hold." Discrete ladder only — 180° fisheye / 107° (14–16mm) / 84° (20–24mm) / 63° (28–35mm) / 47° (40–50mm) / 29° (75–85mm) / 18° (100–135mm) / 12° (180–200mm) / 8° (300–400mm). "Never write a non-anchor value — 23° is not on the ladder." Written as `47° (50mm) eye-level neutral`. Camera block sits 3rd-from-end: "Bottom position holds the FOV lock. At the top of the prompt, FOV fights identity data; buried mid-body, it fades."

**Cuts & timing precision scale.** Four registers: oner / sequential untimed cuts (`CUT 1…`) / timed multishot (second values + explicit `HARD CUT`) / freestyle b-roll (rare, explicit only). Door-closing line whenever cuts are specified: "*the camera does not add any additional cuts, edits happen only at the marks written above.*" Recognized cut vocabulary: HARD/SMASH/MATCH/INSERT/REVERSE/WHIP CUT. Whip pans need ≥0.8s "to render as a blur; anything shorter renders as a hard cut." Speed changes: "put a hard cut at every speed change. Never blend speed inside a single continuous shot."

**Five modes:** M1 Narrative (anamorphic, handheld breath, teal-amber, color-negative daylight film) / M2 Studio (clean spherical, locked tripod + optional push, saturated editorial, intentional specular bloom on chrome/rhinestone — the one mode where controlled specular is intentional) / M3 Action (handheld shaky throughout, heavier low-light grain, dusty haze, optional 96fps intercut) / M4 Performance (pit-photographer + orbital, streak flares, volumetric haze, real sweat sheen) / M5 Atmospheric (locked-off or extremely slow push, hex-specified palette, "No humans, environment is the subject"). Locked Camera Capture template lines per mode, all `24fps 180° shutter`. Stacking modes: per-shot Camera Capture specs inline — "Don't blend modes into one averaged grade. The cut between modes is the visual punch; collapsing kills the contrast."

**Verbatim — canonical Capture Realism block (the real-footage engine, second-to-last, ships on every prompt unless glossy register requested):**

```
Capture Realism: [Foreground subject] sits inside real depth — [thin/light/heavy] atmosphere suspended in the air between camera, subject, and [the far background element], the background rendered softer, desaturated, and lower-contrast than the foreground so the figure sits within the air rather than pasted on a flat plane. [IF WET: Slight moisture has settled on every surface — damp matte hair, slight moisture on skin holding fully matte with no beading and no wet sheen, [wet ground with muted reflection / damp matte fabric], moisture that mutes and deepens without a single specular hotspot.] Skin reads true cinematic matte — zero shine on forehead, nose bridge, cheekbones, temples, chin, and collarbones, real peach fuzz catching light at the jaw and hairline, real soft fine even pore texture, light absorbed like true subsurface scattering, warmth preserved and natural, slightly desaturated but never pale or washed-out or cool-shifted, never plastic, never doll-skin, never AI-rendered, and never harsh — no acne, no blemishes, no enlarged or rough pores, fine flattering texture that keeps the face looking good. Low-contrast curve — shadows lifted gently holding texture, highlights rolled off softly never clipping to white, nothing crushed to black. All specular highlights surgically removed from skin, hair, fabric, and surrounding surfaces, every pixel reading matte and diffuse. Slightly desaturated grade with warmth preserved.
```

Four mechanics, tuned per scene: (1) depth via suspended atmosphere between planes; (2) moisture-without-shine (wet scenes only — "damp, not beaded; wet but not glossy"); (3) per-zone specular kill on skin + the flattering ceiling (same lock as Banana Pro); (4) **contrast curve stated three ways** — tonal curve + specular removal + grade — "Three statements is what holds it." "Names the *physics* — the Camera Capture line names the *gear*."

**Optical techniques (named patterns):** Voyeur/long-lens observation (three simultaneous ingredients: 20–30% out-of-focus foreground obstruction + suspended atmosphere in % + 8°/12° lens far from subject; "never zoom-in on a voyeur shot"); Broadcast press-box (8° with "a small 1–2cm hunting tremor"); Foreground-loaded wide/macro-in-a-wide (84° inches from object); Wide portrait (63–84° close face, room stays legible); Compressed atmosphere column ("a thick vertical column of suspended dust visible between the operator and the figure").

**Special protocols:** Extreme-FOV multishot stack (8°/107° drift fastest — four locks in combination: anchor reference + opening lens declaration per beat + closing lens declaration per beat + every hue tied to surface/light-source/purpose; "Drop any one of these four and the sequence starts drifting on beat three"). Pressure fracture/impactless breaks (origin as "edge stress or slow pressure, never a point-of-strike"; fracture moves edge-inward; asymmetric timing; crowds "push forward as a mass under its own weight, no strike, no throw").

**Universal rules (22)** including: no character names (tag + visual description), no platform/tool names in output, age-blind, one main idea per shot ("If more, split"), trust-the-reference for wardrobe, canonical-never-substituted-by-plate, English only in code block.

**Quality gates:** 26-item silent PRE-DELIVERY PASS checklist + a named repair pass ("Too poetic → rewrite Scene & Mood as physical visual instructions... Word count over → trim Subject Lock and Movement first").

**Optional handoffs (explicit cross-skill wiring):** "Story bible pairing — pull character Movement/Stillness descriptors into Subject Lock, pull Speech into Sound Bed for dialogue, pull the aesthetic era block into the grade half of Camera Capture, pull production rules into the Universal Prompt Rules layer. The bible is the identity/context source; this skill is the cinematography grammar." "Banana Pro handoff — ask which cinema mode the plate used and lock the matching grammar. The two skills share the five-mode framework."

## 1.3 `story-bible-builder` — Canon Compiler (meta-skill)

**Purpose.** Interview-driven skill that turns a user's story world into ONE dense canon SKILL.md the user installs as their own custom skill — "instead of burning memory slots on world context, or re-explaining the story every chat." Output is "a locked, opinionated, prompt-ready canon doc. Not a template. Not a workbook. A **bible**." One file, not modular, under 500 lines.

**Two usage modes engineered into every bible:** (1) standalone canon reference; (2) **context source for a video prompt director skill** — "The director skill reads uploaded reference images for wardrobe, hair, and identity. It cannot read *voice*, *movement quality*, *stillness*, *what era's aesthetic applies*, or *what production rules are locked for this world*. Those come from the bible." Feed map when paired: character voice → Sound Bed; movement/stillness → Subject Lock; aesthetic era locks → World Plate/grade; production rules → cross-frame rules and locked traits; ensemble dynamics → Cross-Frame Rules. Quality bar: "If a descriptor in the bible can't be pasted verbatim into a Seedance Sound Bed or Subject Lock block, it's written wrong."

**12-section output structure:** one-line premise / thesis (the question every scene answers) / world timeline / **aesthetic era differentiation** (palette-lighting-texture-grain per era — "what keeps future image prompts consistent") / factions / locations (visual tags, three to seven words) / world rules / characters (deepest section) / relationships & ensemble dynamics / structural engines (recurring chapter *shapes*, stackable) / production rules / "when this skill is active" (instructions to future Claude for both modes).

**Build flow:** Step 0 scope check (title, character count, genre refs, existing-vs-scratch, **which prompt tools future scenes use** — Seedance, Banana Pro, Midjourney, Suno, ElevenLabs) → spine → factions/locations/rules → characters (**one at a time, never batch**; iterate each to lock) → ensemble → engines → production rules → assembly.

**Character section format (per `character-section-format.md`):** `### NAME — *Role tag*` then **Visual** (one dense line, not bullets), **Function** (before backstory — "Function is what future Claude uses to write scenes. Backstory is context."), **Backstory** (push for "one formative detail that's specific and small... 'she used to fix the sink in their apartment herself at 3am because the plumber would have asked questions'"), **Present-tense psychology** ("what makes the bible feel alive"; push for "the internal contradiction — the thing the character is doing versus the thing they're actually feeling. That gap is where the drama lives."), and four quoted prompt-ready descriptors: **Speech** (register/texture/cadence/volume/vocabulary/signature moves as one quoted string), **Movement**, **Stillness** ("Often more revealing than movement"), **Suno** (music scope only — "Never use artist names or song references in Suno prompts — that gets rejected"). Rule 2: "**Never use the character's name inside the quoted descriptors**... Names drift models. Names live in the header only."

**House principles:** (1) Density over prose — "The user should be able to grep this doc"; (2) **Never invent** — "[TBD]" and move on; "Invented canon becomes locked canon becomes prompt drift"; (3) Push on the vague — "'Dark and moody' isn't an aesthetic lock"; (4) **Locks exclude as much as they include** — "'Warm fair skin — never pale porcelain, never tan.' The 'never' clause is what stops model drift over hundreds of future renders."; (5) depth > count — "three deep characters [beat] eight shallow ones"; (6) the user's voice, verbatim.

**Baked production-rule defaults for AI-filmmaker users:** no character names in prompts, every prompt standalone, code-block output, no aspect ratio in prompt body, locked physical traits restated verbatim in every prompt — exactly Banana Pro Director's universal rules, seeded into every generated bible.

**Quality gate (the universal signal):** "could a stranger who has never heard of this story write a scene in it, using only this bible, and get it right?"

*(Install note: SKILL.md references `references/character-interview.md` etc., but the zip has the three reference files FLAT next to SKILL.md. On install they must move into a `references/` subdirectory or the pointers break. Also: the bible's Step 7 saves to `/mnt/user-data/outputs/` — a claude.ai path that must be repointed to a repo path on install. It cross-references `cinema-worldbuilder-pro-20` by version-stamped name; update to the installed name.)*

---

# 2. CROSS-SKILL ARCHITECTURE

**The three compose as a three-layer production pipeline: CANON → STILL ASSETS → MOTION.**

```
story-bible-builder            (once per world — canon: identity, voice, movement,
        │                       stillness, era palettes, production rules, "never" clauses)
        ▼
banana-pro-director-3.0        (per character/asset — stills, in strict order:
        │                       Mode 0 face lock → Mode 1 outfit base → Mode 2A sheet
        │                       → Mode 3 scene plates; Modes 4/5 as gated utilities)
        ▼
cinema-worldbuilder-pro-3.0    (per shot — Seedance video prompts consuming the
                                canonical refs + plates as @tags and the bible's
                                quoted descriptors as block payloads)
```

**Intended order is explicit in the docs, from both ends:**
- Worldbuilder's session character gate: "needs developing → kick to a character build skill (Banana Pro director or equivalent). Return to Seedance once locked."
- Worldbuilder's "Optional Handoffs": bible = identity/context source, worldbuilder = cinematography grammar; Banana Pro plates carry the environment ("ask which cinema mode the plate used and lock the matching grammar").
- Bible's Mode 2: director skill pulls voice → Sound Bed, movement/stillness → Subject Lock, era → World Plate/grade, ensemble dynamics → Cross-Frame Rules.
- Banana Pro's Mode 3: "Output becomes a Higgsfield reference asset that can feed Seedance for video generation. Camera language matches the cinema mode the eventual video will use."

**Shared conventions across all three (the house grammar):**
1. **The five-mode framework (M1–M5)** is shared verbatim between Banana Pro Mode 3 and the Worldbuilder — same capture register, same lens characters, same grade language, so a still plate and its video shot match.
2. **Name-blind / brand-blind / age-blind prompt output** — identical rules in Banana Pro and Worldbuilder; the bible bakes them into every generated canon file as default production rules.
3. **References carry identity, prompts carry the moment** — Banana Pro's lean-prompt doctrine ≡ Worldbuilder's "Trust the reference for wardrobe" + canonical-over-plate ≡ the bible's quoted descriptors existing precisely because references *can't* carry voice/movement/stillness.
4. **Pre-prompt confirmation with a fixed bullet order and an iteration exception** — same contract, adapted per skill (references first in Banana Pro; tags first / runtime last in Worldbuilder).
5. **The flattering-realism ceiling, matte-skin specular kill, peach fuzz + SSS biology cues, lifted-blacks/rolled-highlights curve, 35mm-grain film register** — the identical anti-AI-look physics, expressed as the cinema stack / flat grade (stills) and Capture Realism (video).
6. **Single fenced code block delivery; no aspect ratio in prompt body; every prompt standalone; end negations only as closing quality filters.**
7. **Locked defaults with explicit-request exceptions** as the universal control pattern (gray-not-white, 3-panel-not-6, diegetic-not-music, handheld-not-tripod, Banana-Pro-not-GPT-2).

**Division of labor, stated cleanly:** the bible owns WHO (and never drifts), Banana Pro owns WHAT THEY LOOK LIKE (canonical pixels), the Worldbuilder owns WHAT HAPPENS ON SCREEN (framing, motion, cut grammar, physics). Nothing is duplicated: the worldbuilder refuses to re-describe wardrobe the reference shows; Banana Pro refuses to bake lighting the video will re-do; the bible refuses to hold cinematography.

---

# 3. GENIUS PATTERNS (transferable principles)

1. **References carry identity; prompts carry framing.** Text re-describing what a reference already shows creates "double-weight prompts" that dilute direction. One visual handle per subject; put prompt tokens where they're load-bearing (composition, pose, light, the moment). Transfers to every ref-conditioned model — and to context engineering generally: don't restate what an attached artifact already asserts.

2. **Reference plates carry ZERO lighting information.** Any shadow baked into a reference is "inherited and amplified by every downstream generation" and fights the scene's lighting. So identity assets are catalogue-flat — form described "by bone structure, hair strands, and fabric folds alone" — and lighting is applied exactly once, at the final render. This is separation of concerns applied to light: bake nothing upstream you'll want to override downstream.

3. **Lower subject-background contrast for downstream edge stability.** Gray beats white because "video models amplify small mistakes most at high-contrast edges — that's where halo, edge 'breathing,' and contour instability get baked in during motion." Choose asset defaults for the *next* stage's failure modes, not this stage's aesthetics.

4. **The flattering-realism ceiling.** Two levers, always both on: matte (anti-plastic) and fine-and-even (anti-ugly); "when the two ever seem to pull against each other, resolve toward fine-even-flattering." Realism prompts without a flattering ceiling produce dermatology photos; the ceiling is a taste constraint expressed as a tie-breaking rule — a resolvable priority, not a vibe.

5. **Write the visible — abstractions to measurables.** Speed in km/h, atmosphere in % + meters, scale in stacked humans, emotion in muscle ("knuckles blanch"), danger in light sources and standing water. "If a word doesn't produce a visible pixel, cut it." The general form: convert intent into the units the executing system actually parses.

6. **Positive phrasing except sanctioned end-position negations.** "The model sees the noun and rounds toward it" — so prohibitions become descriptions of what IS. The exception is deliberate: known-failure suppression lists placed AFTER all positive description, "where the model handles it as a quality filter rather than a conflicting instruction." Negation is a tool with a correct position, not a banned move.

7. **Discrete anchors beat continuous suggestions.** The FOV degree ladder: "Millimeters read as suggestion; degrees read as instruction... Degrees hold." Snap values the model latches onto (with off-ladder values forbidden) prevent drift across beats. Same insight behind timed cuts, hex palettes in M5, and the "contrast curve stated three ways" redundancy — quantized, repeated instructions hold; analog ones decay.

8. **Position in the prompt is part of the instruction.** Camera block at the bottom "holds the FOV lock. At the top... FOV fights identity data; buried mid-body, it fades." Banana Pro: "reads the front of the prompt most heavily" — composition loads the front. Distributed style: no top-of-prompt style prefix, each aspect anchored to its home block because "putting a style prefix on the prompt scatters the model's attention."

9. **Resolution-aware detail — describe what the camera can see, not what's true.** Detail is "earned by camera proximity, lens length, motion stillness, and lighting intensity." Kills the AI tell of impossible detail (readable decals on a car 200 feet away at 120 mph). Broader form: describe at the fidelity the observation channel supports.

10. **Pixel-budget economics.** 3-panel beats 6-panel because a sheet is one image with a fixed budget and the face panel is the whole point; the headless front panel exists to give garment/silhouette a panel with "zero facial data competing for the model's attention." Attention and resolution are budgets — allocate them to the asset's single purpose.

11. **Names drift; descriptions survive.** No character names, no brand names, no ages, no platform names in any prompt — identity lives in references and visual descriptors ("Higgsfield does not know names"). The bible extends it: names live in headers only, never inside the quoted descriptors.

12. **Locks exclude as much as they include — the "never" clause.** "Warm fair skin — never pale porcelain, never tan." Ask what the wrong-answer drift would be and write it into the lock. A lock without its failure directions doesn't hold "over hundreds of future renders."

13. **Absence is not a directive — name the null.** Movement's four layers are each stated "even when the layer is 'nothing else moves.' Saying nothing moves is a directive; absence is not." Same with the cut door-closer ("the camera does not add any additional cuts") and the Last Frame text-suppression line.

14. **Canonical-over-plate.** World context and identity are separate channels even when they overlap visually: "The plate carries the world... canonical references carry identity" — every named subject gets its own reference slot even when visible in the plate. Never let context assets double as identity assets.

15. **Confirmation as a cheap error-catching contract, with a friction budget.** The pre-prompt check exists because long prompts are expensive to discover-wrong; references listed first so a missing ref is caught before the prompt ships; but minor iterations skip it because "re-confirming on tiny deltas creates friction." Gates scale with blast radius.

16. **Prompt-ready quoted payloads — data formatted for its consumer.** Bible descriptors are engineered to paste verbatim into named downstream slots (Speech → Sound Bed, Movement/Stillness → Subject Lock, Suno → vocal casting): "If a descriptor... can't be pasted verbatim... it's written wrong." Upstream artifacts should be written in the downstream system's input format.

17. **Fidelity-tiered tool forks with cost honesty.** Banana Pro default / GPT-2 highest-fidelity-highest-credits / Soul Cinema cheap iteration — the user picks per job, the credit warning fires exactly once per session. Escalation is explicit, gated, and never proposed proactively.

18. **Never invent — [TBD] beats plausible.** "Invented canon becomes locked canon becomes prompt drift." Hallucinated detail in a canon document compounds; a marked gap doesn't.

19. **The stranger test as the density gate.** "Could a stranger who has never heard of this story write a scene in it, using only this bible, and get it right?" — a falsifiable doneness criterion for any context document.

20. **Silent structure, prose surface.** The Mode 3 six-bucket checklist and X/Y coordinate library are kept as internal planning tools but never appear in output — coordinates translate to positional prose because "the model responds to confident scene description, not coordinate grids." Rigor in the thinking, naturalness in the artifact.

---

# 4. INTEGRATION MAP vs THE EXISTING SYSTEM

## 4.1 What already exists (surveyed)

| Existing asset | Role today |
|---|---|
| `skills/fantastic-posters/SKILL.md` | 38-style stylized image gen via **Fal GPT Image 2** (`generate.js`), edits/masks/rembg, poster→video bridge via **Fal Seedance 2.0** + Kling v3 Pro wrappers, budget-guarded (`fal_budget_guard.py`, seedance-1080p HARD-BLOCKED) |
| `/fantastic-studio` (`.agent/workflows/fantastic-studio.md` + `workflows/00-studio.md`, stages 01–08) | Concept-first pipeline: reference-ground → art-direct (Satori) → divergence → **model route** → prompt compile → generate → critique → format pack |
| `skills/higgsfield-creative-studio/SKILL.md` | Routing/stacking layer for Higgsfield ads: routes stills → `gpt-image-2-director`, video ads → `marketing-studio-director`; budget-gated via `higgsfield_budget_guard.py`; uses `<<<image_n>>>` labels; already age-blind for avatars |
| `skills/gpt-image-2-director/SKILL.md` | OpenAI GPT Image 2.0 prompt director (JSON layout / cinematic prose / meta-prompt). Explicitly states "Cinematic photorealism is its weakness. Human faces often go plasticky." |
| `skills/marketing-studio-director/` | Higgsfield Marketing Studio video-ad paragraphs |
| `execution/creative_router.py` | Keyword→service routing table (first match wins): `portrait/person/face/character reference → higgsfield-soul`; `quick/draft/iterate → higgsfield-nano`; `cinematic → higgsfield-cinema`; short clip → `fal-seedance-720p`; posters → `fal-poster` |
| `.agent/workflows/higgsfield-studio.md` | Higgsfield front-door workflow |
| Higgsfield MCP (claude.ai connector) | `generate_image`, `generate_video`, `show_characters`, `show_reference_elements`, media upload — the actual execution surface Joey's prompts paste into |

## 4.2 Overlaps

- **Photoreal character stills.** Joey's banana-pro-director vs the router's `higgsfield-soul` lane and higgsfield-creative-studio's still lane. Joey's skill is far deeper on character *pipelines* (face lock → base → sheet) than anything in the system; existing assets only have "character sheet" as a keyword (routed to gpt-image-2-director's JSON format — a much weaker, non-photoreal treatment).
- **Seedance video prompts.** cinema-worldbuilder-pro vs `fantastic-posters/workflows/seedance-cinematic.md` + `fal_video_seedance.py` (Fal Seedance) and the router's `fal-seedance-720p` / `higgsfield-cinema` lanes. Joey's grammar (blocks, FOV ladder, @tags, Capture Realism) is a full prompt OS; the existing Seedance workflow is a thin wrapper prompt.
- **Character canon.** story-bible-builder overlaps conceptually with the brand-bible/DESIGN.md pattern and `bw-character-canvas`/`hawley-voice-bible` writing skills — but nothing in the system produces *installable* visual-canon skills for AI filmmaking. Net-new capability.
- **Anti-AI-look language.** The cinema stack overlaps in intent with fantastic-studio's anti-slop critique stage and satori anti-AI-slop — but at the render-physics level rather than the design level. Complementary, not duplicate.

## 4.3 Conflicts / contradictions (flag before install)

1. **"GPT-2" naming collision (highest confusion risk).** Joey's skills use "GPT-2" to mean *Higgsfield's* GPT-2 image model (highest-fidelity FACE model, chest-up detail king). The existing `gpt-image-2-director` means *OpenAI* GPT Image 2.0 (via Fal or Higgsfield) and states the exact opposite: "Cinematic photorealism is its weakness. Human faces often go plasticky." These are different models with opposite face verdicts. Routing text, workflow prose, and the router registry must disambiguate: **Higgsfield GPT-2 (faces, credits-heavy) ≠ OpenAI GPT Image 2 (layout/typography king, weak faces)**.
2. **creative_router.py face routing.** Current rule: portraits/faces/character-consistency → `higgsfield-soul`, with note "Nano Banana as fallback if Soul over-stylizes." Joey's doctrine inverts this: **Banana Pro (Nano Banana) is the DEFAULT for face locks**, Soul Cinema is the cheap-iteration/outfit-compositing path, GPT-2 the fidelity escalation. The router's people-lane reason/notes should be updated to match the deeper doctrine (or at minimum point at the new skill for character *builds* as opposed to one-off people shots).
3. **Backdrop default conflict (soft).** Nothing in the existing system mandates a backdrop, but gpt-image-2-director's character-sheet JSON examples and fantastic-posters styles assume white/styled grounds. Joey's LOCKED default for all character work is 18% gray + flat grade. Rule: any asset that will seed video follows Joey's gray-flat lock; standalone posters/deliverables keep their own art direction. Don't let fantastic-studio's critique stage "improve" a flat gray plate by adding lighting — the flatness is the feature.
4. **Seedance surface split.** cinema-worldbuilder targets Seedance *inside the Higgsfield UI* (element tags, references uploaded under tag names). `fal_video_seedance.py` targets Seedance *via Fal API* — no @tag support there. The worldbuilder's prompts are still excellent for the Fal path minus tags, but the tag mechanics only work on the Higgsfield surface. Workflows must say which surface they're driving; Fal-path use strips tags to prose descriptors.
5. **Cost-gate compatibility (no conflict, but must be stated).** All three Joey skills are prompt-only — "The skill's job ends at the code block" — so the cost gate never fires on them. The moment prompts are executed via Higgsfield MCP or Fal wrappers, existing gates apply unchanged (`higgsfield_budget_guard.py`, `fal_budget_guard.py`, seedance-1080p hard block). GPT-2's "more credits" warnings compose cleanly with the guard.
6. **Negative-prompt-style closers vs positive-phrasing doctrine (internal, resolved).** The cinema stack and flat grade are dense with "no X" language while the worldbuilder locks positive phrasing. The set resolves it itself (negations sanctioned only as end-position quality filters), but anyone editing these blocks must not "fix" the closers into positive phrasing or scatter them upward.
7. **Stale v2 remnants inside banana-pro-director** (white-background "Goal" line in Mode 0; "soft soft natural light from camera-left/right" bullets in Mode 0/1B pre-prompt checks contradicting the flat shadowless prompt bodies). Locked text wins (gray + flat); fix or annotate on install so the pre-prompt checks don't mislead.
8. **story-bible-builder path + version-stamped cross-refs.** Saves output to `/mnt/user-data/outputs/` (claude.ai sandbox path) and references `cinema-worldbuilder-pro-20`. Repoint to a repo path (e.g. `projects/<world>/bible/` or `deliverables/`) and to the installed skill names.

## 4.4 Synergy points — specific files that should point at the new skills

| Existing file | Change |
|---|---|
| `execution/creative_router.py` | Update `higgsfield-soul` people rule notes → "Character BUILDS (face lock, outfit base, character sheet) → load `skills/banana-pro-director/SKILL.md` (Banana Pro default, GPT-2 fidelity escalation, Soul Cinema two-step)." Update `fal-seedance-720p` / `higgsfield-cinema` notes → "Seedance prompt grammar → `skills/cinema-worldbuilder-pro/SKILL.md`." Keep table+`directives/routing-bindings.md` in sync per CLAUDE.md. |
| `skills/higgsfield-creative-studio/SKILL.md` Router table | Add rows: "photoreal character build / face lock / character sheet / outfit swap → `banana-pro-director`"; "Seedance cinematic video prompt → `cinema-worldbuilder-pro`". Disambiguate Higgsfield GPT-2 vs OpenAI GPT Image 2 in the routing prose. |
| `skills/fantastic-posters/workflows/seedance-cinematic.md` + `poster-to-video.md` | Point prompt-construction at the worldbuilder grammar (blocks, FOV ladder, Capture Realism, write-the-visible), noting Fal-surface = no @tags. |
| `.agent/workflows/fantastic-model-route.md` + `fantastic-prompt-compile.md` | Model-route stage should list banana-pro-director as the compile grammar when a direction routes to Higgsfield photoreal people; prompt-compile should import the flat-grade close for reference plates. |
| `.agent/workflows/higgsfield-studio.md` | Add the three-skill pipeline (bible → banana-pro → worldbuilder) as the character/world production path. |
| `skills/gpt-image-2-director/SKILL.md` | One-line cross-pointer: "For photoreal faces/characters on Higgsfield, use `banana-pro-director` — this skill's face realism is weak by design." |
| `directives/higgsfield-usage-policy.md` | Note that banana-pro/worldbuilder are prompt-only (ungated) and generation through MCP/CLI remains guarded. |
| Higgsfield MCP flows (`show_characters`, `show_reference_elements`, `generate_video`) | The natural execution surface: banana-pro outputs become Higgsfield character/reference elements; worldbuilder @tags map onto reference elements. Worth a short workflow (`/joey-pipeline` or extend `/higgsfield-studio`) documenting the paste-and-attach loop. |
| New-bible outputs | Per repo convention, generated bibles should land under the owning project (`projects/<name>/` or `_active/<client>/`) and can be installed per-project — matching the per-client CLAUDE.md inheritance pattern. |

What the new set does NOT replace: fantastic-posters (stylized/typographic, Fal, 38 styles — different lane entirely), gpt-image-2-director (layout/text density), marketing-studio-director (Marketing Studio ad paragraphs), the studio pipeline (concept/divergence/critique brain — Joey's skills slot in as *compile grammars* at stage 04–05 for the photoreal-people and Seedance lanes).

---

# 5. INSTALL RECOMMENDATION

**Target directories (kebab-case, strip the ambiguous `-30` suffix — repo convention keeps version history in git, not dir names; cf. `higgsfield-creative-studio`, `gpt-image-2-director`):**

```
skills/banana-pro-director/
    SKILL.md                      ← from banana-pro-director-30/banana-pro-director-30/SKILL.md
skills/cinema-worldbuilder-pro/
    SKILL.md                      ← from cinema-worldbuilder-pro-30/cinema-worldbuilder-pro-30/SKILL.md
skills/story-bible-builder/
    SKILL.md
    references/
        character-interview.md    ← MOVE (zip has these flat beside SKILL.md;
        character-section-format.md   SKILL.md points at references/… — flat install breaks pointers)
        example-bible-excerpts.md
```

**Renames/edits required at install:**
1. Strip the double-nested `<name>-30/<name>-30/` zip structure.
2. YAML `name:` fields: `banana-pro-director-3.0` → `banana-pro-director` (dots in names are nonstandard); `cinema-worldbuilder-pro-30` → `cinema-worldbuilder-pro`; `story-bible-builder` unchanged.
3. story-bible-builder: create `references/` and move the three companion files in; repoint the `/mnt/user-data/outputs/` save path to a repo path; update `cinema-worldbuilder-pro-20` references to `cinema-worldbuilder-pro`.
4. cinema-worldbuilder-pro: its bible/Banana-Pro handoff paragraphs reference the other two by concept — update any version-stamped names.
5. Optional forge-pass cleanups in banana-pro-director: reconcile the stale white-background "Goal" line and the "soft soft light from camera-left/right" pre-prompt bullets with the locked gray+flat grade (locked prompt bodies already correct).
6. Frontmatter: no `routing: long-tail` — these should be default-routable for Higgsfield/Seedance/character-build intents; add front-door workflows only if Farrice wants `/face-lock`, `/character-sheet`, `/seedance-shot` style commands (the SKILL.md mode grammar is already self-routing).
7. After install: update `creative_router.py` + `directives/routing-bindings.md` together (repo rule), and add the cross-pointers in §4.4.
8. Consider `genius.md` per extraction convention — §3 of this analysis is the seed material.

**Credit/attribution:** header-note the source as "Joey's Skill Files v3.0" with harvest date, matching the fantastic-posters upstream-credit pattern.
