<!-- Prompt-only kit. $0 budget. No generation calls made in producing this file. VO lines are copied verbatim from rework-v2/MASTER-COPY.md BRIEF 2 - never rewritten, only selected/grouped by clip. -->

# Puravita "The Battery You Can't See" - Video Generation Kit

## 1. Header Card

- **Ad:** Puravita Magnesium Complex, "The Battery You Can't See"
- **Format:** 9:16, 1080x1920. Hero cut (below) runs ~100-110s at a natural pace - see runtime note.
- **Variant plan - 3 final cuts, one shared 5-beat body:**
  - **Cut A - Hook 1** (battery analogy): "Your phone warns you when it drops to five percent. Your body never does."
  - **Cut B - Hook 3** (partner-POV): "My wife says she misses me. I'm sitting right next to her."
  - **Cut C - Hook 4** (loud control): "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why."
  - **Hook 2 (bench, not built):** "Your bloodwork came back fine..." - available if a variant underperforms; do not render today.
- **Visual law:** the whole ad lives on two images - a phone you can read, and a body you cannot. Every clip returns to one of those two.
- **Register:** quiet, NYT Magazine restraint. No stock tired-person footage, no doctors, no disease language, no urgency. Sage highlight for on-screen callouts.
- **Runtime honesty note:** the approved body script, read verbatim at a natural 165 wpm, runs ~105s for all 5 beats plus a 5-10s hook - longer than the "~50s" spec line. Build the FULL hero cut today (it shows range, nothing trimmed). If a hard 50s cutdown is needed later, Body 3 (lab-report/Huberman-Attia beat) is the first candidate to shorten - it doesn't touch the hook or the CTA.

---

## 2. Shot-List Table

8 distinct clips cover all 3 variants (body generated once, reused in every cut).

| Clip | Beat | Duration | VO (verbatim) | On-screen text | Route |
|---|---|---|---|---|---|
| H1 | Hook 1, battery analogy | 6-8s | "Your phone warns you when it drops to five percent. Your body never does." | The battery you can't see. | HF TV Spot / Veo b-roll |
| H3 | Hook 3, partner-POV | 6-8s | "My wife says she misses me. I'm sitting right next to her." | I'm sitting right next to her. | HF UGC / Veo on-camera |
| H4 | Hook 4, loud control | 8-10s HF / 8s Veo, brisk | "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why." | Stop blaming your age. | HF TV Spot / Veo b-roll |
| B1 | Felt problem | 12-15s HF / 8s Veo x2 | "So you do everything right. Eight hours down, and you wake up like you never slept. The coffee stops working by ten. Your wife asks if you're okay, and you say you're fine, because you do not have a better word for it. You are running dim, and you have been for a while." | You're running dim. | HF TV Spot / Veo b-roll |
| B2 | Hidden battery | 12-15s HF / 8s Veo x2 | "There is a battery inside you that you have never seen. It runs hundreds of quiet jobs you never notice, day and night. Magnesium powers over six hundred reactions in your body. When it runs low, nothing alarms you. No five percent warning. Everything just runs at half power. And you call it getting older." | The battery you can't see. | HF TV Spot / Veo b-roll |
| B3 | Why the test missed it | 12-15s HF / 8s Veo x2 (Huberman/Attia line, keep exact) | "You're thinking your bloodwork was fine. It was. And it told you almost nothing. A standard blood test sees under one percent of the magnesium in your body. The other ninety-nine percent sits in bone and muscle, off the panel. Your number reads normal while the part that actually runs you reads low. Huberman points people to magnesium before sleep. Attia takes close to a gram a day. They are not guessing." | The test sees under 1%. | HF TV Spot / Veo b-roll |
| B4 | The answer, product enters | 10-12s HF / 8s Veo | "So a single cheap form of magnesium was never enough. Your body uses a different form in different places, and one pill covers one of them. Puravita carries all twelve. You are refilling the battery the chart cannot even see." | Twelve forms. One battery. | HF Unboxing / Veo b-roll, product visible |
| B5 | Close, CTA | 12-15s HF / 8s Veo | "The label asks for six to eight weeks. That is how long a real recharge takes. So do not grab the small bottle and quit in week two. Start the ninety-day, and give it the runway. And somewhere around week six, you wake up before the alarm, and your wife looks at you over the coffee the way she used to. That is the battery coming back. Start the ninety-day today." | Start the 90-day today. | HF TV Spot / Veo b-roll, product visible |

Edit order: **Cut A** = H1, B1-B5. **Cut B** = H3, B1-B5. **Cut C** = H4, B1-B5.

---

## 3. Per-Clip Generation Cards

**Standing rules:** phones shoot flat and square to lens, hand only, never a face, screen content one bold simple graphic, no reflections. Bottle clips (B4, B5): attach the real Puravita photo from the PDP (shoppuravita.com) as `<<<image_1>>>` - never let the model invent the label. **Long beats (B1, B2, B3, B5): the Veo prompt is one 8s pass on the beat's opening; generate it twice back-to-back (second pass holds the frame/glow/push-in a beat further) so the edit has footage to run the full VO from the shot-list.**

### H1 - Hook 1, battery analogy

**START FRAME (GPT Image 2):**
```
A 35mm film photograph of a hand reaching toward a phone lying flat on a wood nightstand at dawn, screen facing up, no glare, a bold minimal battery icon at five percent pulsing soft red, no app clutter. Cool pre-dawn light, warm lamp glow at the edge. No face or body beyond the hand.
```

**HIGGSFIELD (TV Spot):**
A composed shot of a nightstand at dawn, cool light crossing the wood as a hand enters and settles beside a phone lying flat, screen facing straight up, a five-percent battery icon pulsing once in soft red, no glare. Slow, steady push-in from slightly above, phone staying flat throughout. A quiet male voiceover reads, "Your phone warns you when it drops to five percent. Your body never does," landing as the hand settles. No face or body beyond the hand.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s):**
```
A still nightstand at dawn, cool light, a hand enters and settles beside a phone lying flat, screen facing the lens with no glare, a simple red battery icon at five percent pulsing once. Slow push-in from slightly above. Native audio: quiet room tone and a calm male voiceover (no on-screen speaker), "Your phone warns you when it drops to five percent. Your body never does."
```

### H3 - Hook 3, partner-POV (on-camera narrator)

**START FRAME (GPT Image 2):**
```
A cinematic editorial portrait of a man with a weathered complexion and gray-flecked hair at the temples, at a kitchen table in warm morning light, charcoal knit sweater, hands still. Direct, calm eye line to camera, no smile. Film-photograph texture.
```

**HIGGSFIELD (UGC, 13-word dialogue):**
A quiet, phone-native medium shot in a warm kitchen, a man with a weathered complexion and gray-flecked hair at the temples sits still at the table in a charcoal sweater, hands flat, looking directly into the lens with no smile. He says to camera, "My wife says she misses me. I'm sitting right next to her," plainly, a small pause before the second sentence. Soft window light, single continuous take, minimal natural handheld breathe.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s):**
```
A still medium shot in a warm kitchen, a man with a weathered complexion and gray-flecked hair at the temples sits at the table in a charcoal sweater, hands still, looking into the lens without smiling. Soft window light, minimal handheld breathe, no cuts. Native audio: quiet kitchen ambience under his line, "My wife says she misses me. I'm sitting right next to her," plain delivery, small pause between sentences.
```

### H4 - Hook 4, loud control

**START FRAME (GPT Image 2):**
```
A 35mm film photograph of a phone screen filling the frame, flat to camera, bold white text on black reading "STOP BLAMING YOUR AGE," a hand steadying the edge. Cooler, higher-contrast light than the other clips, no reflections, no face.
```

**HIGGSFIELD (TV Spot, brisk):**
A faster-cut sequence: a phone held flat to camera reading "STOP BLAMING YOUR AGE" in bold white on black, hard cut to the same phone reading "8 HOURS. STILL TIRED," hard cut to a lab report corner with one small green check mark. A brisk male voiceover reads, "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why," each sentence on its cut. Higher contrast, no reflections, no face.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s, brisk delivery):**
```
Three quick cuts: a phone reading "STOP BLAMING YOUR AGE" in bold white on black, cut to the same phone reading "8 HOURS. STILL TIRED," cut to a lab report corner with one small green check mark. Higher contrast, no reflections. Native audio: a brisk calm male voiceover (no on-screen speaker), "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why," timed to the cuts.
```

### B1 - the felt problem

**START FRAME (GPT Image 2):**
```
A 35mm film photograph of a phone face-up on a nightstand in a dim pre-dawn bedroom, screen blinking awake once with a low glow, then fading, no alarm graphic. Muted blue-gray light, soft shadow on the wood. No body or face.
```

**HIGGSFIELD (TV Spot):**
A locked-off shot of a phone lying face-up on a nightstand in a dim pre-dawn bedroom, screen blinking awake once with a low glow before fading slowly, no alarm sound or graphic. No camera movement, letting the dimming read as the entire event. A quiet male voiceover reads the full B1 line from the shot-list ("So you do everything right... you have been for a while"). No face or body.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s, pass 1 of 2):**
```
A locked-off shot of a phone lying face-up on a nightstand in a dim pre-dawn bedroom, screen blinking awake once with a low glow, beginning to fade. No alarm, no movement. Native audio: quiet room tone under a calm male voiceover (no on-screen speaker) opening, "So you do everything right. Eight hours down, and you wake up like you never slept." Pass 2: same locked frame, glow continuing to fade, voiceover finishes the B1 line per the shot-list.
```

### B2 - the hidden battery

**START FRAME (GPT Image 2):**
```
A 35mm film photograph, extreme close-up of a phone screen held flat to camera, one large minimal battery icon glowing low amber, no UI chrome, dimming at the edges. No reflections, no hand or face, dark vignette.
```

**HIGGSFIELD (TV Spot):**
An extreme close-up filling the frame with a phone screen held flat to camera, one large minimal battery icon glowing amber and low, no chrome. Slow, almost imperceptible push-in as the glow dims further, no reflections, no hand or face. A quiet male voiceover reads the full B2 line from the shot-list ("There is a battery inside you... you call it getting older").

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s, pass 1 of 2):**
```
An extreme close-up of a phone screen held flat to camera, one large minimal battery icon glowing amber and dimming slowly, no chrome, no reflections. Native audio: quiet ambient hum under a calm male voiceover (no on-screen speaker) opening, "There is a battery inside you that you have never seen. It runs hundreds of quiet jobs you never notice, day and night." Pass 2: same glow continuing to dim, voiceover finishes the B2 line per the shot-list.
```

### B3 - why the test missed it

**START FRAME (GPT Image 2):**
```
A 35mm film photograph of a printed lab report on a kitchen table, shot straight-down, most of the page in soft shadow, one small green check mark near the top catching window light, the rest soft and unreadable. No hand or face.
```

**HIGGSFIELD (TV Spot):**
A top-down shot of a printed lab report on a kitchen table, most of the page in soft shadow, one small green check mark catching window light. Slow, steady push-in toward the check mark, the rest of the page staying soft and unreadable. A quiet male voiceover reads the full B3 line from the shot-list ("You're thinking your bloodwork was fine... They are not guessing" - Huberman/Attia sentence exact). No hand or face.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s, pass 1 of 2):**
```
A top-down shot of a printed lab report on a kitchen table, most of the page in soft shadow, one small green check mark catching window light, slow push-in toward the check mark. Native audio: quiet room tone under a calm male voiceover (no on-screen speaker) opening, "You're thinking your bloodwork was fine. It was. And it told you almost nothing. A standard blood test sees under one percent of the magnesium in your body." Pass 2: same push-in continuing, voiceover finishes the B3 line, Huberman/Attia sentence exact, per the shot-list.
```

### B4 - the answer (product enters)

**START FRAME (GPT Image 2):**
```
A 35mm film photograph, close-up of a phone at the edge of frame showing a dim amber battery glow, beside it on the wood surface the real Puravita Magnesium Complex bottle (reference photo attached, label exact, no invented text) being set down, morning light warming as the glow climbs brighter.
```

**HIGGSFIELD (Unboxing):**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, label and cap exactly as photographed). A close-up of a phone at the edge of frame with a dim amber glow, a hand setting `<<<image_1>>>` down on the wood beside it, light warming cool to gold as the glow climbs a shade brighter. Slow 3/4 angle, steady, no whip or orbit. A quiet male voiceover reads the full B4 line from the shot-list ("So a single cheap form of magnesium... the chart cannot even see"). Bottle label faces camera, unaltered.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s):**
```
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A close-up 3/4 angle of a phone at the edge of frame with a dim amber glow, a hand setting the referenced bottle down beside it, light warming cool to gold, glow climbing brighter, label unaltered. Native audio: quiet morning ambience under a calm male voiceover (no on-screen speaker) reading the full B4 line from the shot-list ("So a single cheap form of magnesium... the chart cannot even see").
```

### B5 - close (CTA)

**START FRAME (GPT Image 2):**
```
A 35mm film photograph of a phone screen glowing full and steady amber on a wood surface in soft morning light, beside it the real Puravita Magnesium Complex bottle (reference photo attached, label exact, no invented text), both warmly lit, camera level and still. Calm and settled, no hand or face.
```

**HIGGSFIELD (TV Spot, closing):**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A final shot of a phone screen glowing full and steady amber on a wood surface in warm morning light, `<<<image_1>>>` resting beside it, both catching the same gold light. Level, still camera, a very slow final push-in over the full duration, no cuts. A quiet male voiceover reads the full B5 line from the shot-list ("The label asks for six to eight weeks... Start the ninety-day today"), voice easing down on the last four words. Bottle label legible, unaltered.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**VEO 3.1 / FLOW (8s):**
```
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A level, still final shot of a phone screen glowing full and steady amber beside the referenced bottle, both in warm morning gold light, a very slow push-in, no cuts. Native audio: quiet room tone fading toward silence under a calm male voiceover (no on-screen speaker) reading the full B5 line from the shot-list ("The label asks for six to eight weeks... Start the ninety-day today"), settled and unhurried, easing down on the last four words.
```

---

## 4. Narrator Card

- **Casting (appearance/wardrobe/delivery only, no age words):** male presenter, weathered complexion, gray-flecked hair at the temples, simple charcoal or navy sweater or overshirt, no logos. Warm kitchen light. Calm, unhurried, still hands. No smile through the partner-POV line.
- **HeyGen/Higgsfield-avatar casting prompt:**
  ```
  A man with a weathered complexion and gray-flecked hair at the temples, wearing a simple charcoal knit sweater, seated at a kitchen table in warm morning window light. Calm, composed demeanor, hands resting flat on the table, no jewelry, no logos. Neutral, unhurried expression, direct eye line to camera, no smile.
  ```
- **ElevenLabs voice direction:** calm low register, unhurried pace (130-145 wpm), warm timbre, faint low rasp, no upspeak. Pauses land after concrete facts (percentages, trial counts, "twelve forms"). Names the pattern without alarm, never clinical, never salesy. Volume eases down on the last line before the edit cuts to silence.
- **Full VO per variant, rough timestamps (165 wpm), beat text = shot-list above:**
  - **Cut A:** 0:00-0:05 H1. 0:05-0:25 B1. 0:25-0:45 B2. 0:45-1:11 B3. 1:11-1:26 B4. 1:26-1:52 B5.
  - **Cut B:** 0:00-0:05 H3, body identical from 0:05 on.
  - **Cut C:** 0:00-0:10 H4 (longer). Body shifts ~5s later: 0:10-0:30 B1, 0:30-0:50 B2, 0:50-1:16 B3, 1:16-1:31 B4, 1:31-1:56 B5.

---

## 5. Hook-Teaser Cards (fastest finished sample)

Each is ONE self-contained Marketing Studio generation, 12-15s, playing as a complete micro-ad: hook, one verbatim mechanism beat, bottle, close. Attach the real bottle photo as `<<<image_1>>>` in every teaser.

**Teaser 1 - Hook 1, ~12s:**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A hand settles a phone flat on a nightstand at dawn, screen reading a five-percent battery icon in soft red, cut to an extreme close-up of the icon glowing amber and dimming, cut to `<<<image_1>>>` set beside the phone as its glow climbs toward full in warm morning light, slow push-in throughout. A quiet male voiceover reads, "Your phone warns you when it drops to five percent. Your body never does. There is a battery inside you that you have never seen. Start the ninety-day today," each sentence on its cut. No reflections, no face.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**Teaser 2 - Hook 3, ~12s:**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A man with a weathered complexion and gray-flecked hair at the temples, seated at a kitchen table in warm light, says to camera, "My wife says she misses me. I'm sitting right next to her," cut to an extreme close-up of a phone battery icon glowing amber and dimming, cut to `<<<image_1>>>` set down in the same warm light as the glow climbs toward full, voiceover continuing, "There is a battery inside you that you have never seen. Start the ninety-day today." No reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**Teaser 3 - Hook 4, ~14s:**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A phone held flat to camera reads "STOP BLAMING YOUR AGE" in bold white on black, cut to a lab report corner with one small green check mark, cut to `<<<image_1>>>` set beside a phone whose battery glow climbs from low to full in warm morning light. A brisk male voiceover reads, "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why. No five percent warning. Start the ninety-day today," each sentence timed to its cut. Higher contrast opening, easing to warm gold by the close.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

---

## 6. Assembly Runbook

- **Edit order:** Cut A = H1, B1-B5. Cut B = H3, B1-B5. Cut C = H4, B1-B5. Body clips generated once, reused across all three timelines.
- **Captions:** burned-in, Inter Tight (or Sohne), bottom third, max 6 words per frame, manual placement (no auto-caption tool). Sage highlight reserved for callouts: "5%", "over 600 reactions", "under 1%", "twelve forms", "90-day".
- **Music:** sparse piano or low ambient bed at -18 dB under the full cut. Cut to silence under the final CTA line ("Start the ninety-day today.") - the silence is the close, do not fill it.
- **Export:** 1080x1920, 9:16, H.264, burned captions in the export (not a separate SRT). File name pattern `Puravita_BatteryYouCantSee_[CutA|CutB|CutC]_9x16.mp4`.
- **60-second pre-send QA checklist:**
  1. Bottle label in B4/B5 matches the real PDP photo exactly, no invented text.
  2. No age-marker words in on-screen text, captions, or prompts.
  3. No banned antislop vocabulary (breathtaking, elevate, unlock, game-changer, etc.).
  4. VO is verbatim against MASTER-COPY.md - no paraphrase, no dropped clauses.
  5. No diagnosing-the-viewer language - only what the phone/lab report can't see, never what's wrong with the viewer.
  6. No disease or treatment claims anywhere.
  7. No urgency stingers, countdowns, or scarcity language.
  8. Huberman/Attia line reads exactly as scripted, unmodified.
  9. Silence actually lands under the final CTA line in the export, not just the timeline.
