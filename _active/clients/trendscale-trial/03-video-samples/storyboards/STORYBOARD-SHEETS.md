# Storyboard & Pre-Production Reference Sheets: JCKED + Puravita

Source: `gpt-image-2-director/SKILL.md` (Format A, structured JSON, used throughout: every sheet below has discrete labeled regions). Consistency logic from `AI-VIDEO-REALISM-RESEARCH.md` Q4/Q6: hold identity with reference-image ingredient workflows, repeat full description every clip, bake legible text into the still rather than the video model, unify grade/grain across models in the finishing pass. Shot lists, narrator looks, and palettes pulled verbatim from `JCKED-VIDEO-KIT.md` and `PURAVITA-VIDEO-KIT.md`. Each prompt below is self-sufficient, paste cold into GPT Image 2.

---

## JCKED: The Locked Vault

### 1. Narrator Character Sheet

```json
{
  "type": "actor character reference sheet, multi-view, labeled panels",
  "style": "cinematic editorial photography, muted warm-and-navy palette, film-photograph texture, shallow depth of field per panel, no plastic skin, natural skin texture, visible pores",
  "subject": "a lean, lived-in male presenter, weathered unpolished face, dark stubble, charcoal crewneck with no branding or logos, calm unsmiling expression, hands still, appearance and wardrobe only, no age indicated",
  "background": "flat neutral steel-gray studio strip behind every panel, no props, no reflections",
  "layout": {
    "top_left": {"label": "FRONT MID-SHOT", "content": "presenter facing camera direct, mid-shot from chest up, warm key light on left side of face, deep navy shadow on right side, flat unsmiling expression, eyes direct to lens"},
    "top_right": {"label": "3/4 VIEW", "content": "same presenter turned to a three-quarter angle, same warm-left navy-right lighting held, same charcoal crewneck, hands still at sides"},
    "bottom_left": {"label": "PROFILE", "content": "same presenter in full side profile, warm rim light along the front of the face, navy falloff behind, same wardrobe and stubble detail"},
    "bottom_right": {"label": "HANDS DETAIL", "content": "close-up of the presenter's still hands resting on a dark surface, same warm-left navy-right lighting, no jewelry, no visible tattoos, natural skin texture"}
  },
  "footer": "small caption strip reading JCKED NARRATOR CONSISTENCY REFERENCE in clean sans serif, steel gray text on a dark navy bar"
}
```

### 2. Environment Sheet

```json
{
  "type": "empty location reference plate sheet, two labeled panels, no actors or props",
  "style": "cinematic editorial photography, muted warm-and-navy palette, film-photograph texture, no people, no reflections",
  "layout": {
    "left_panel": {"label": "NEUTRAL KITCHEN (empty plate)", "content": "an empty neutral kitchen with matte dark cabinetry, warm light entering from camera left, deep navy shadow falling across camera right, no figures, no props, clean uncluttered counter"},
    "right_panel": {"label": "VAULT CELL (empty plate)", "content": "an empty dark navy cell-like space, bare steel walls fading into shadow, a single closed steel vault gate glowing dim amber at center frame, cool navy ambient light on the edges, warm amber light source only on the gate, shallow atmospheric haze, no figures"}
  },
  "footer": "small caption strip reading JCKED ENVIRONMENT PLATES LIGHTING LOCKED in clean sans serif on a dark navy bar"
}
```

### 3. Storyboard Contact Sheet

```json
{
  "type": "cinematic storyboard contact sheet, single 16:9 sheet containing a 2x5 grid of 9:16 panels, each panel is a key frame still with a camera annotation strip baked into the image directly beneath it",
  "style": "muted warm-and-navy cinematic palette matching JCKED brand grade, film-photograph texture, no plastic skin, consistent lighting logic across all ten panels",
  "background": "flat dark steel gray sheet background, thin white gutter lines separating panels, header bar at top reading JCKED THE LOCKED VAULT STORYBOARD in clean sans serif",
  "layout": {
    "grid": "2 rows of 5 panels each, read left to right, top row then bottom row, each panel framed 9:16 inside its cell",
    "panels": {
      "count": 10,
      "items": [
        {"label": "01 OPEN", "frame": "wide establishing shot of a dark navy vault cell, bare steel walls fading to shadow, a closed steel gate glowing dim amber at center, no figures", "annotation": "WS EYE LEVEL SLOW PUSH IN 3s"},
        {"label": "02 HOOK 1", "frame": "presenter mid-shot in neutral kitchen, warm light left side of face, navy shadow right side, flat unsmiling expression, mouth open mid-line", "annotation": "MS EYE LEVEL STATIC 8s"},
        {"label": "03 HOOK 2", "frame": "same presenter tighter medium close-up, same kitchen, quiet direct expression, hands out of frame", "annotation": "MCU EYE LEVEL STATIC 7s"},
        {"label": "04 HOOK 3", "frame": "dark navy vault cell, camera closer on the closed amber gate than panel 01, no figures", "annotation": "MS EYE LEVEL SLOW DOLLY IN 8s"},
        {"label": "05 HOOK 4", "frame": "same presenter bolder wider frame, leaning slightly forward, more contrast, direct unsmiling gaze", "annotation": "MS EYE LEVEL STATIC 7s"},
        {"label": "06 BODY 1", "frame": "close-up of a heavy steel padlock engraved CPT-1 on a plain dark vault door, one cool light raking across the surface", "annotation": "CU EYE LEVEL SLOW PUSH IN 20s VO"},
        {"label": "07 BODY 2", "frame": "macro shot of a brass key turning inside the CPT-1 lock, door cracking open along its seam, warm light spilling through the gap", "annotation": "ECU LOW ANGLE MATCH CUT 23s VO"},
        {"label": "08 BODY 3", "frame": "two brass keys on dark steel, a short stub engraved 500 beside a full-length key engraved JCKED, camera settling on the full key", "annotation": "CU EYE LEVEL SLOW PUSH IN 16s VO"},
        {"label": "09 BODY 4", "frame": "heavy steel vault door standing open onto warm amber light, the JCKED bottle centered on a dark pedestal inside the doorway", "annotation": "WS TO MS EYE LEVEL SLOW DOLLY IN 14s VO"},
        {"label": "10 CLOSE", "frame": "the open vault doorway held steady around the bottle, small steel-and-amber caption card reading 365 DAY MONEY BACK GUARANTEE", "annotation": "MS EYE LEVEL HOLD 4s"}
      ]
    }
  }
}
```

### 4. Style/Grade Sheet

```json
{
  "type": "brand style and color grade reference sheet, labeled swatches and texture panels",
  "style": "flat graphic reference board, clean white gutters, small sans serif labels under every swatch",
  "layout": {
    "top_bar": {"title": "JCKED THE LOCKED VAULT STYLE AND GRADE REFERENCE"},
    "palette_row": {
      "count": 4,
      "swatches": [
        {"label": "DEEP NAVY", "description": "near-black blue swatch, feels like #0B1220, dominant shadow color"},
        {"label": "STEEL", "description": "cool gray-blue swatch, feels like #6E7A83, secondary surfaces and metal"},
        {"label": "AMBER", "description": "warm gold-orange swatch, feels like #C98A2C, reserved for the vault glow and key light"},
        {"label": "OFF-WHITE TEXT", "description": "warm white swatch, feels like #EDE7DD, body caption color"}
      ]
    },
    "texture_panel": {"label": "FILM GRAIN REFERENCE", "content": "a close crop of fine 35mm film grain over a dark navy gradient, subtle, no banding, 2 to 3 percent visible noise"},
    "lighting_panel": {"label": "LIGHTING RATIO REFERENCE", "content": "a plain gray sphere lit from the left in warm amber and from the right in cool navy shadow, showing a hard 4:1 key to fill ratio, no fill bounce, one clean falloff line down the center"},
    "typography_panel": {"label": "CAPTION TYPOGRAPHY SPECIMEN", "content": "the word LOCKED set in Inter Tight bold caps in off-white on a dark navy bar, and the word CPT-1 set in the same font in amber on the same bar, showing the two caption colors side by side"}
  }
}
```

### 5. Prop/Product Sheet

```json
{
  "type": "product and prop reference sheet, three labeled panels",
  "style": "cinematic editorial photography, muted warm-and-navy palette, film-photograph texture, shallow depth of field, no reflections",
  "layout": {
    "panel_1": {"label": "CPT-1 PADLOCK", "content": "a heavy steel padlock on a plain dark vault door, lock face engraved CPT-1, dim and matte under one cool directional light, deep navy shadow behind"},
    "panel_2": {"label": "STUB KEY VS FULL KEY", "content": "two brass keys side by side on a dark steel surface under cool directional light, a short stub key engraved 500 on the left, a full-length key engraved JCKED on the right, the full key visibly longer and more substantial, deep navy background"},
    "panel_3": {"label": "BOTTLE PLACEMENT", "content": "<<<image_1>>> = JCKED bottle reference, real product photography from the PDP at https://jcked.com/products/liquid-l-carnitine-4000mg, label and cap exactly as shown, never restyled. The bottle from <<<image_1>>> centered on a dark pedestal inside an open vault doorway, warm amber light spilling from inside, deep navy exterior framing, no reflections"}
  },
  "footer": "small caption strip reading JCKED PROPS LABEL FIDELITY LOCKED in clean sans serif on a dark navy bar"
}
```

---

## Puravita: The Battery You Can't See

### 1. Narrator Character Sheet

```json
{
  "type": "actor character reference sheet, multi-view, labeled panels",
  "style": "cinematic editorial photography, warm morning light, film-photograph texture, shallow depth of field per panel, no plastic skin, natural skin texture, visible pores",
  "subject": "a man with a weathered complexion and gray-flecked hair at the temples, wearing a simple charcoal knit sweater, calm and unhurried demeanor, hands resting flat, no jewelry, no logos, appearance and wardrobe only, no age indicated",
  "background": "flat neutral warm-gray studio strip behind every panel, no props, no reflections",
  "layout": {
    "top_left": {"label": "FRONT MID-SHOT", "content": "presenter facing camera direct, mid-shot from chest up, warm window light from one side, soft shadow on the other, calm neutral expression, no smile, direct eye line to camera"},
    "top_right": {"label": "3/4 VIEW", "content": "same presenter turned to a three-quarter angle, same warm one-sided light held, same charcoal sweater, hands resting flat"},
    "bottom_left": {"label": "PROFILE", "content": "same presenter in full side profile, soft warm rim light along the front of the face, gentle falloff behind, same wardrobe and hair detail"},
    "bottom_right": {"label": "HANDS DETAIL", "content": "close-up of the presenter's still hands resting flat on a wood table, same warm one-sided lighting, no jewelry, no visible tattoos, natural skin texture"}
  },
  "footer": "small caption strip reading PURAVITA NARRATOR CONSISTENCY REFERENCE in clean sans serif, dark gray text on a paper-white bar"
}
```

### 2. Environment Sheet

```json
{
  "type": "empty location reference plate sheet, two labeled panels, no actors or props",
  "style": "cinematic editorial photography, quiet restrained register, warm and cool natural light, film-photograph texture, no people, no reflections",
  "layout": {
    "left_panel": {"label": "WARM KITCHEN (empty plate)", "content": "an empty kitchen with a wood table, warm morning window light crossing the surface from camera left, soft shadow falling right, no figures, no clutter, calm and settled"},
    "right_panel": {"label": "NIGHTSTAND AT DAWN (empty plate)", "content": "an empty wood nightstand in a dim bedroom at dawn, cool pre-dawn blue-gray light crossing the surface, a warm lamp glow entering softly from one edge, no phone, no hand, no figures"}
  },
  "footer": "small caption strip reading PURAVITA ENVIRONMENT PLATES LIGHTING LOCKED in clean sans serif on a paper-white bar"
}
```

### 3. Storyboard Contact Sheet

```json
{
  "type": "cinematic storyboard contact sheet, single 16:9 sheet containing a 2x5 grid of 9:16 panels, each panel is a key frame still with a camera annotation strip baked into the image directly beneath it",
  "style": "quiet restrained palette, warm morning gold and cool pre-dawn blue-gray, sage accent reserved for caption text only, film-photograph texture, no plastic skin",
  "background": "flat warm off-white sheet background, thin gray gutter lines separating panels, header bar at top reading PURAVITA THE BATTERY YOU CANT SEE STORYBOARD in clean sans serif",
  "layout": {
    "grid": "2 rows of 5 panels each, read left to right, top row then bottom row, each panel framed 9:16 inside its cell",
    "panels": {
      "count": 10,
      "items": [
        {"label": "01 OPEN", "frame": "phone lying flat on a wood nightstand at dawn, screen facing up showing a small red five percent battery icon, cool pre-dawn light, no hand, no face", "annotation": "CU TOP DOWN STATIC 3s"},
        {"label": "02 HOOK 1", "frame": "a hand entering frame and settling beside the phone on the nightstand, five percent battery icon pulsing once, warm lamp glow at the edge", "annotation": "CU SLIGHT HIGH ANGLE SLOW PUSH IN 8s"},
        {"label": "03 HOOK 3", "frame": "man with a weathered complexion and gray-flecked hair at the temples, seated at a kitchen table in warm morning light, charcoal sweater, hands flat, no smile", "annotation": "MS EYE LEVEL STATIC 8s"},
        {"label": "04 HOOK 4", "frame": "phone screen filling frame, flat to camera, bold white text on black reading STOP BLAMING YOUR AGE, a hand steadying the edge, higher contrast light", "annotation": "CU TOP DOWN HARD CUT 8s"},
        {"label": "05 BODY 1", "frame": "phone face up on a nightstand in a dim pre-dawn bedroom, screen blinking awake once with a low glow then fading, no alarm graphic", "annotation": "CU LOCKED OFF STATIC 12s VO"},
        {"label": "06 BODY 2", "frame": "extreme close-up of a phone screen, one large minimal battery icon glowing low amber, dimming at the edges, no chrome, no hand", "annotation": "ECU EYE LEVEL SLOW PUSH IN 12s VO"},
        {"label": "07 BODY 3", "frame": "printed lab report on a kitchen table shot straight down, most of the page in soft shadow, one small green check mark catching window light", "annotation": "CU TOP DOWN SLOW PUSH IN 12s VO"},
        {"label": "08 BODY 4", "frame": "phone at the edge of frame with a dim amber glow, a hand setting the Puravita bottle down on the wood beside it, light warming toward gold", "annotation": "CU 3/4 ANGLE STEADY 10s VO"},
        {"label": "09 BODY 5", "frame": "phone screen glowing full and steady amber beside the Puravita bottle, both in warm morning light, camera level and still", "annotation": "MS EYE LEVEL VERY SLOW PUSH IN 12s VO"},
        {"label": "10 CLOSE", "frame": "same final frame held, small sage caption card reading START THE 90 DAY TODAY", "annotation": "MS EYE LEVEL HOLD 4s"}
      ]
    }
  }
}
```

### 4. Style/Grade Sheet

```json
{
  "type": "brand style and color grade reference sheet, labeled swatches and texture panels",
  "style": "flat graphic reference board, warm off-white gutters, small sans serif labels under every swatch",
  "layout": {
    "top_bar": {"title": "PURAVITA THE BATTERY YOU CANT SEE STYLE AND GRADE REFERENCE"},
    "palette_row": {
      "count": 4,
      "swatches": [
        {"label": "WARM MORNING GOLD", "description": "soft warm gold swatch, feels like #E8C27A, dawn and lamp light"},
        {"label": "PRE-DAWN BLUE-GRAY", "description": "muted cool blue-gray swatch, feels like #5B6673, night and low-battery scenes"},
        {"label": "SAGE ACCENT", "description": "soft muted green swatch, feels like #9CAF88, reserved for caption callouts only"},
        {"label": "PAPER WHITE", "description": "warm off-white swatch, feels like #F3EFE6, lab report and background tone"}
      ]
    },
    "texture_panel": {"label": "FILM GRAIN REFERENCE", "content": "a close crop of fine 35mm film grain over a warm gold gradient, subtle, no banding, 2 to 3 percent visible noise"},
    "lighting_panel": {"label": "LIGHTING RATIO REFERENCE", "content": "a plain gray sphere lit from one side in soft warm window light and the other in muted cool shadow, showing a gentle 2:1 key to fill ratio, soft falloff, no hard edge"},
    "typography_panel": {"label": "CAPTION TYPOGRAPHY SPECIMEN", "content": "the phrase THE BATTERY YOU CANT SEE set in Inter Tight regular in dark gray on paper white, and the number 90-DAY set in the same font in sage green on the same background, showing both caption colors side by side"}
  }
}
```

### 5. Prop/Product Sheet

```json
{
  "type": "product and prop reference sheet, three labeled panels",
  "style": "cinematic editorial photography, warm and cool natural light, film-photograph texture, shallow depth of field, no reflections, hand-only where a hand appears, no face ever with the phone",
  "layout": {
    "panel_1": {"label": "PHONE SCREEN STATES", "content": "three small phone screens shown flat to camera in a row, each a bold simple graphic with no app clutter: left screen reads a red five percent battery icon on black, center screen reads a low dim amber battery icon on black, right screen reads a full steady amber battery icon on black, no hand, no face"},
    "panel_2": {"label": "LAB REPORT DETAIL", "content": "a printed lab report on a kitchen table shot straight down, most of the page in soft shadow, one small green check mark near the top catching window light, the rest of the page soft and unreadable, no hand, no face"},
    "panel_3": {"label": "BOTTLE PLACEMENT", "content": "<<<image_1>>> = Puravita Magnesium Complex bottle reference, real product photography from the PDP at https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex, label and cap exactly as shown, never restyled. The bottle from <<<image_1>>> resting on a wood surface beside a phone showing a full steady amber glow, both in warm morning gold light, a hand may rest near the bottle but never near the phone screen, no face in frame"}
  },
  "footer": "small caption strip reading PURAVITA PROPS LABEL FIDELITY LOCKED in clean sans serif on a paper-white bar"
}
```

---

## USAGE MAP

**Narrator character sheet** feeds the talking-human model: crop the front mid-shot panel as the single reference image for Higgsfield Soul ID training (front + 3/4 + profile crops together for a stronger lock), and as one of Veo 3.1's 3 Ingredient images alongside the product. Drives every on-camera hook (JCKED H1/H2/H4, Puravita H3) so the face holds across the shared body.

**Environment sheet** empty plates become the composited background under the narrator crop when building each brand's GPT Image 2 start frames, and are used directly as the start frame for hooks/body beats with no narrator on camera (JCKED H3 and B1-B4; Puravita B1-B3 and the open/close beats).

**Storyboard contact sheet**: crop each of the 10 panels individually as the literal GPT Image 2 start frame for that clip, fed into Higgsfield or Veo 3.1 image-to-video (Frames-to-Video / First-and-Last-Frame). The baked camera annotation is the shot list: shot size and movement carry straight into the Higgsfield/Veo prose prompts already written in the video kits. Crop the annotation strip off before the frame becomes a video input.

**Style/grade sheet** is the Remotion finishing-pass reference: match white balance and grain percentage across every clip regardless of source model (Higgsfield vs Veo vs GPT Image 2 stills) so the cut doesn't betray model-switching. The typography panel is the exact caption spec for the burned-in captions.

**Prop/product sheet** crops feed directly as `<<<image_1>>>` reference attachments in every bottle-bearing clip, and as the UI-graphic reference for any screen, lock, or key close-up.
