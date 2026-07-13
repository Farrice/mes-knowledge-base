<!-- $0 budget. No generation calls made producing this file. VO verbatim throughout, sourced from PURAVITA-VIDEO-KIT.md, never rewritten. Refines v1 Higgsfield paragraphs per AI-VIDEO-REALISM-RESEARCH.md; UNCONFIRMED research claims carry their flag, never silently trusted. -->

# Puravita "The Battery You Can't See" - Prompt Pack v2

11 cards: 8 clips (H1, H3, H4, B1-B5) + 3 hook-teasers. PDP for all product clips: `https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex`.

## GLOBAL FLAGS (apply to every card, not repeated below)

- ⚠ Image-to-video dialogue is UNCONFIRMED to render reliably; Veo has historically suppressed speech from a start frame. If audio drops, fall back to silent output + ElevenLabs VO overlay, never rewrite the line.
- ⚠ Kling vs Veo 3.1 for talking-human is UNCONFIRMED as an absolute ranking - test both before committing budget.
- ⚠ Higgsfield's break-points (reflections, >2 humans, location swap) are UNCONFIRMED folklore; every card avoids all three regardless.
- ⚠ Scene Builder / multi-still chaining across a hard cut is UNCONFIRMED (version drift) - verify live before finalizing H4, B1, B2, B3, B5, Teaser 1, Teaser 3.
- Portable JSON is pipeline/asset-index data, not the recommended Veo format - Google's canonical format is prose; JSON superiority is itself UNCONFIRMED.
- Standing law: phones flat and square to lens, hand only, never a face; one bold screen graphic; no glass reflections; no age markers; no disease/treatment language; no urgency; VO verbatim; no em-dashes in prompt text; no antislop vocabulary.

---

## H1 - Hook 1, battery analogy

**Routing:** Primary **Veo 3.1** (Q7b) | Fallback **Kling 3.0** | Start frame: **Yes** - bakes the 5% icon (Q2).

**START FRAME - GPT Image 2**
```
A 35mm film photograph of a hand reaching toward a phone lying flat on a wood nightstand at dawn, screen facing straight up with no glare, a bold minimal battery icon at five percent pulsing soft red baked into the display, no app clutter. Cool pre-dawn light, warm lamp glow at the edge. No face or body beyond the hand.
```

**VEO 3.1 / FLOW (8s, 9:16, image-to-video from start frame)**
```
[00:00-00:03] Per start frame: hand settles beside the phone, screen up, no glare.
[00:03-00:06] Slow push-in from above, the five-percent icon pulses once, soft red.
[00:06-00:08] Hold on the settled hand and glowing icon.
A calm male voice says (no on-screen speaker), "Your phone warns you when it drops to five percent. Your body never does."
Ambient noise: quiet room tone, faint street sound. Style: correct hand anatomy, no extra fingers.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
A composed shot of a nightstand at dawn, cool light crossing the wood as a hand enters and settles beside a phone lying flat, screen facing straight up, a five-percent battery icon pulsing once in soft red, no glare. Slow, steady push-in from slightly above, the phone staying flat throughout, correct hand anatomy. A quiet male voiceover reads, "Your phone warns you when it drops to five percent. Your body never does," landing as the hand settles. No face or body beyond the hand.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H1","duration_s":7,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:03","visual":"hand settles beside phone, screen up","camera":"static, above","audio":"room tone"},
{"t_start":"00:03","t_end":"00:08","visual":"battery icon pulses once soft red, then holds","camera":"slow push-in then static","audio":"VO plays, resolves"}],
"subject":"hand and phone only, no face","environment":"wood nightstand, dawn bedroom","lighting":"cool pre-dawn, warm lamp edge",
"dialogue":null,"vo_verbatim":"Your phone warns you when it drops to five percent. Your body never does.",
"on_screen_text":"The battery you can't see.","negatives":["no glare","no UI chrome","correct hand anatomy","no subtitle overlay"],
"start_frame_ref":"assets/images/H1_start.png","product_ref":null}
```

---

## H3 - Hook 3, partner-POV (on-camera narrator)

**Routing:** Primary **Kling 2.6/3.0 Omni** (Q7a) | Fallback **Veo 3.1** | Start frame: **Yes** - portrait locks face/wardrobe, not text.

**START FRAME - GPT Image 2**
```
A cinematic editorial portrait of a man with a weathered complexion and gray-flecked hair at the temples, at a kitchen table in warm morning light, charcoal knit sweater, hands still. Direct, calm eye line to camera, no smile. Film-photograph texture.
```

**VEO 3.1 / FLOW (8s, 9:16 - fallback route)**
```
[00:00-00:04] Static medium shot, warm kitchen, the man from the start frame sits in a charcoal sweater, hands still, no smile, soft window light, one side brighter.
[00:04-00:08] Minimal handheld breathe, no cuts, delivery continues to close.
He says, "My wife says she misses me. I'm sitting right next to her," plain delivery, small pause before the second sentence.
Ambient noise: quiet kitchen ambience. Style: natural skin texture, no plastic skin.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING (talking-human route, primary)**
```
Shot 1 (0:00-0:08, single continuous take): medium shot, warm kitchen, the man from the start frame, charcoal knit sweater, hands still and flat, direct eye line, no smile, soft window light, one side brighter, natural handheld breathe.
Dialogue: "My wife says she misses me. I'm sitting right next to her," plain delivery, small pause before the second sentence, natural micro-expressions, no robotic gesture.
Audio timeline: single shared track, quiet kitchen room tone under the line.
Identity lock: hold face and wardrobe per the start-frame reference. No subtitles burned into the take.
```

**HIGGSFIELD**
A quiet, phone-native medium shot in a warm kitchen, a man with a weathered complexion and gray-flecked hair at the temples sits still at the table in a charcoal sweater, hands flat, looking directly into the lens with no smile. He says to camera, "My wife says she misses me. I'm sitting right next to her," plainly, a small pause before the second sentence. Soft window light, single continuous take, minimal natural handheld breathe.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H3","duration_s":7,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:04","visual":"narrator seated, direct eye line, no smile","camera":"static medium shot","audio":"dialogue begins"},
{"t_start":"00:04","t_end":"00:08","visual":"finishes line, minimal breathe","camera":"handheld breathe","audio":"dialogue resolves"}],
"subject":"male narrator, weathered complexion, gray-flecked hair, charcoal sweater","environment":"warm kitchen, wood table","lighting":"soft window light, one side brighter",
"dialogue":"My wife says she misses me. I'm sitting right next to her.","vo_verbatim":"My wife says she misses me. I'm sitting right next to her.",
"on_screen_text":"I'm sitting right next to her.","negatives":["no smile","no plastic skin","no subtitle overlay","no upspeak"],
"start_frame_ref":"assets/images/H3_start.png","product_ref":null}
```

---

## H4 - Hook 4, loud control

**Routing:** Primary **Veo 3.1** (Q7b) | Fallback **Kling 3.0** | Start frame: **Yes, three stills (A/B/C)**, one per text card. ⚠ v1 asked one generation to render two text changes; refined (Q2) to chain three pre-rendered stills via Scene Builder instead.

**START FRAME - GPT Image 2 (three stills)**
```
A: A 35mm film photograph of a phone screen filling the frame, held flat by a steadying hand, bold white text on black reading "STOP BLAMING YOUR AGE." Cooler, higher-contrast light, no reflections, no face.
B: Same phone, hand, and lighting as A, screen now reading "8 HOURS. STILL TIRED."
C: A corner of a printed lab report in soft shadow, one small green check mark catching light, no hand, no face, same contrast grade as A/B.
```

**VEO 3.1 / FLOW (8s across 3 chained segments, 9:16)**
```
[00:00-00:03] Seeded from Still A: phone reads "STOP BLAMING YOUR AGE," hand steady, no movement.
[00:03-00:06] Hard cut, seeded from Still B: same phone/hand, now reads "8 HOURS. STILL TIRED."
[00:06-00:08] Hard cut, seeded from Still C: lab report corner, check mark holds steady.
A brisk calm male voice says (no on-screen speaker), "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why," each sentence landing on its cut.
Ambient noise: quiet room tone per cut. Style: higher contrast than the rest of the ad, no reflections.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
A faster-cut sequence, cooler and higher contrast than the rest of the ad: a phone held flat to camera reading "STOP BLAMING YOUR AGE" in bold white on black, hard cut to the same phone reading "8 HOURS. STILL TIRED," hard cut to a lab report corner with one small green check mark. A brisk male voiceover reads the full line ("Stop blaming your age... never built to catch why," verbatim per the shot-list), each sentence on its cut. No reflections, no face throughout.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H4","duration_s":9,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:03","visual":"phone reads STOP BLAMING YOUR AGE","camera":"static","audio":"VO sentence 1"},
{"t_start":"00:03","t_end":"00:08","visual":"phone reads 8 HOURS. STILL TIRED, then lab report check mark","camera":"two hard cuts","audio":"VO sentences 2-3"}],
"subject":"phone in hand, then lab report corner, no face","environment":"high-contrast neutral surface","lighting":"cooler, higher contrast",
"dialogue":null,"vo_verbatim":"Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why.",
"on_screen_text":"STOP BLAMING YOUR AGE / 8 HOURS. STILL TIRED / (checkmark, no text)","negatives":["no reflections","no face","no subtitle overlay"],
"start_frame_ref":"assets/images/H4_stillA.png;H4_stillB.png;H4_stillC.png","product_ref":null}
```

---

## B1 - The felt problem

**Routing:** Primary **Veo 3.1** | Fallback **Kling 3.0** | Start frame: **Yes** - no baked text, locks lighting/framing across passes.

**START FRAME - GPT Image 2**
```
A 35mm film photograph of a phone face-up on a nightstand in a dim pre-dawn bedroom, screen blinking awake once with a low glow, then fading, no alarm graphic. Muted blue-gray light, soft shadow on the wood. No body or face.
```

**VEO 3.1 / FLOW (two 8s passes, 9:16)**
```
Pass 1 (0:00-0:08): [00:00-00:04] Locked-off, phone blinks awake once, low glow, beginning to fade, no alarm. [00:04-00:08] Glow continues fading toward dark.
A calm male voice says (no on-screen speaker), opening, "So you do everything right. Eight hours down, and you wake up like you never slept."
Pass 2 (0:00-0:08, seeded from Pass 1's final frame): same locked frame, glow settled low, held.
Voiceover finishes: "The coffee stops working by ten. Your wife asks if you're okay, and you say you're fine, because you do not have a better word for it. You are running dim, and you have been for a while."
Ambient noise: quiet room tone. Style: muted blue-gray light, no reflections, no body or face.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
A locked-off shot of a phone lying face-up on a nightstand in a dim pre-dawn bedroom, screen blinking awake once with a low glow before fading slowly, no alarm sound or graphic. No camera movement, letting the dimming read as the entire event. A quiet male voiceover reads the full line ("So you do everything right... you have been for a while," verbatim per the shot-list). No face or body.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B1","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:08","visual":"phone blinks awake, low glow, fades toward dark","camera":"locked-off","audio":"VO opens, continues"},
{"t_start":"00:08","t_end":"00:14","visual":"glow settled low, held","camera":"static hold","audio":"VO resolves"}],
"subject":"phone only, no body or face","environment":"dim pre-dawn bedroom, nightstand","lighting":"muted blue-gray",
"dialogue":null,"vo_verbatim":"So you do everything right. Eight hours down, and you wake up like you never slept. The coffee stops working by ten. Your wife asks if you're okay, and you say you're fine, because you do not have a better word for it. You are running dim, and you have been for a while.",
"on_screen_text":"You're running dim.","negatives":["no alarm graphic","no reflections","no body or face","no subtitle overlay"],
"start_frame_ref":"assets/images/B1_start.png","product_ref":null}
```

---

## B2 - The hidden battery

**Routing:** Primary **Veo 3.1** | Fallback **Kling 3.0** | Start frame: **Yes** - bakes the amber battery icon.

**START FRAME - GPT Image 2**
```
A 35mm film photograph, extreme close-up of a phone screen held flat to camera, one large minimal battery icon glowing low amber, no UI chrome, dimming at the edges. No reflections, no hand or face, dark vignette.
```

**VEO 3.1 / FLOW (two 8s passes, 9:16)**
```
Pass 1 (0:00-0:08): [00:00-00:04] Extreme close-up per start frame, amber icon glowing low. [00:04-00:08] Slow, almost imperceptible push-in, glow dims further.
A calm male voice says (no on-screen speaker), opening, "There is a battery inside you that you have never seen. It runs hundreds of quiet jobs you never notice, day and night."
Pass 2 (0:00-0:08, seeded from Pass 1's final frame): glow continues dimming at the same rate, push-in holds.
Voiceover finishes: "Magnesium powers over six hundred reactions in your body. When it runs low, nothing alarms you. No five percent warning. Everything just runs at half power. And you call it getting older."
Ambient noise: quiet ambient hum. Style: dark vignette, no reflections, no hand or face.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
An extreme close-up filling the frame with a phone screen held flat to camera, one large minimal battery icon glowing amber and low, no chrome. Slow, almost imperceptible push-in as the glow dims further, no reflections, no hand or face. A quiet male voiceover reads the full line ("There is a battery inside you... you call it getting older," verbatim per the shot-list).

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B2","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:08","visual":"amber icon glowing low, extreme close-up, slow push-in","camera":"static then slow push-in","audio":"VO opens, continues"},
{"t_start":"00:08","t_end":"00:14","visual":"glow continues dimming, push-in holds","camera":"push-in hold","audio":"VO resolves"}],
"subject":"phone screen only, no hand or face","environment":"dark vignette, no defined room","lighting":"low amber glow",
"dialogue":null,"vo_verbatim":"There is a battery inside you that you have never seen. It runs hundreds of quiet jobs you never notice, day and night. Magnesium powers over six hundred reactions in your body. When it runs low, nothing alarms you. No five percent warning. Everything just runs at half power. And you call it getting older.",
"on_screen_text":"The battery you can't see.","negatives":["no UI chrome","no reflections","no hand or face","no subtitle overlay"],
"start_frame_ref":"assets/images/B2_start.png","product_ref":null}
```

---

## B3 - Why the test missed it

**Routing:** Primary **Veo 3.1** | Fallback **Kling 3.0** | Start frame: **Yes** - no baked text (check mark is a graphic mark, not rendered words).

**START FRAME - GPT Image 2**
```
A 35mm film photograph of a printed lab report on a kitchen table, shot straight-down, most of the page in soft shadow, one small green check mark near the top catching window light, the rest soft and unreadable. No hand or face.
```

**VEO 3.1 / FLOW (two 8s passes, 9:16)**
```
Pass 1 (0:00-0:08): [00:00-00:04] Top-down per start frame, check mark catching light. [00:04-00:08] Slow push-in toward the check mark, rest of page stays soft.
A calm male voice says (no on-screen speaker), opening, "You're thinking your bloodwork was fine. It was. And it told you almost nothing. A standard blood test sees under one percent of the magnesium in your body."
Pass 2 (0:00-0:08, seeded from Pass 1's final frame): push-in continues at the same rate.
Voiceover finishes, Huberman/Attia sentence exact: "The other ninety-nine percent sits in bone and muscle, off the panel. Your number reads normal while the part that actually runs you reads low. Huberman points people to magnesium before sleep. Attia takes close to a gram a day. They are not guessing."
Ambient noise: quiet room tone. Style: soft shadow, no reflections, no hand or face.
NO SUBTITLES. No captions. No spoken-line text overlay.
```
⚠ A name-free swap for the Huberman/Attia line exists on record as an available fallback; not written here, do not substitute without instruction.

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
A top-down shot of a printed lab report on a kitchen table, most of the page in soft shadow, one small green check mark catching window light. Slow, steady push-in toward the check mark, the rest of the page staying soft and unreadable. A quiet male voiceover reads the full line ("You're thinking your bloodwork was fine... They are not guessing," Huberman/Attia sentence exact, per the shot-list). No hand or face.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B3","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:08","visual":"lab report top-down, check mark catching light, slow push-in begins","camera":"static then push-in","audio":"VO opens, continues"},
{"t_start":"00:08","t_end":"00:14","visual":"push-in continues, page stays soft","camera":"push-in hold","audio":"VO resolves, Huberman/Attia line"}],
"subject":"printed lab report only, no hand or face","environment":"kitchen table","lighting":"window light, soft shadow",
"dialogue":null,"vo_verbatim":"You're thinking your bloodwork was fine. It was. And it told you almost nothing. A standard blood test sees under one percent of the magnesium in your body. The other ninety-nine percent sits in bone and muscle, off the panel. Your number reads normal while the part that actually runs you reads low. Huberman points people to magnesium before sleep. Attia takes close to a gram a day. They are not guessing.",
"on_screen_text":"The test sees under 1%.","negatives":["no reflections","no hand or face","no subtitle overlay","no diagnosis language"],
"start_frame_ref":"assets/images/B3_start.png","product_ref":null}
```

---

## B4 - The answer (product enters)

**Routing:** Primary **Veo 3.1** (Q7b) | Fallback **Seedance v1.5 Pro / Kling 3.0** (Q7d, bottle label identity lock) | Start frame: **Yes** - real bottle photo attached, label never invented.

**START FRAME - GPT Image 2**
```
<<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label, PDP: https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex).
A 35mm film photograph, close-up of a phone at the edge of frame showing a dim amber glow, beside it on the wood surface the referenced bottle being set down, label exact, no invented text, morning light warming as the glow climbs brighter.
```

**VEO 3.1 / FLOW (8s, 9:16)**
```
<<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label).
[00:00-00:04] Close-up 3/4 angle, hand setting the referenced bottle down beside the phone, label facing camera, unaltered.
[00:04-00:08] Light warms cool to gold, glow climbs a shade brighter, bottle held steady.
A calm male voice says (no on-screen speaker), "So a single cheap form of magnesium was never enough. Your body uses a different form in different places, and one pill covers one of them. Puravita carries all twelve. You are refilling the battery the chart cannot even see."
Ambient noise: quiet morning ambience. Style: correct hand anatomy, no reflections, label unaltered.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, label and cap exactly as photographed). A close-up of a phone at the edge of frame with a dim amber glow, a hand setting `<<<image_1>>>` down on the wood beside it, light warming cool to gold as the glow climbs a shade brighter. Slow 3/4 angle, steady, no whip or orbit. A quiet male voiceover reads the full line ("So a single cheap form of magnesium... the chart cannot even see," verbatim per the shot-list). Bottle label faces camera, unaltered.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B4","duration_s":11,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:08","visual":"hand sets referenced bottle beside phone, glow warms brighter","camera":"close-up 3/4, steady","audio":"VO plays"},
{"t_start":"00:08","t_end":"00:11","visual":"held final frame for edit timing","camera":"static hold","audio":"VO tail"}],
"subject":"hand, phone, referenced Puravita bottle","environment":"wood surface, morning light","lighting":"cool to gold shift",
"dialogue":null,"vo_verbatim":"So a single cheap form of magnesium was never enough. Your body uses a different form in different places, and one pill covers one of them. Puravita carries all twelve. You are refilling the battery the chart cannot even see.",
"on_screen_text":"Twelve forms. One battery.","negatives":["no reflections","no invented label text","correct hand anatomy","no subtitle overlay"],
"start_frame_ref":"assets/images/B4_start.png","product_ref":"https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex"}
```

---

## B5 - Close (CTA)

**Routing:** Primary **Veo 3.1** (Q7b) | Fallback **Seedance v1.5 Pro / Kling 3.0** (Q7d) | Start frame: **Yes** - real bottle photo attached.

**START FRAME - GPT Image 2**
```
<<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label).
A 35mm film photograph of a phone screen glowing full and steady amber on a wood surface in soft morning light, beside it the referenced bottle, label exact, both warmly lit, camera level and still. Calm and settled, no hand or face.
```

**VEO 3.1 / FLOW (8s, 9:16)**
```
<<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label).
[00:00-00:04] Level, still shot per start frame, phone glowing full steady amber beside the bottle, warm gold light.
[00:04-00:08] Very slow push-in, no cuts, both objects holding steady.
A calm male voice says (no on-screen speaker), "The label asks for six to eight weeks. That is how long a real recharge takes. So do not grab the small bottle and quit in week two. Start the ninety-day, and give it the runway. And somewhere around week six, you wake up before the alarm, and your wife looks at you over the coffee the way she used to. That is the battery coming back. Start the ninety-day today," voice easing down on the last four words.
Ambient noise: quiet room tone fading toward silence. Style: warm morning gold, no reflections, label legible.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A final shot of a phone screen glowing full and steady amber on a wood surface in warm morning light, `<<<image_1>>>` resting beside it, both catching the same gold light. Level, still camera, a very slow final push-in over the full duration, no cuts. A quiet male voiceover reads the full line ("The label asks for six to eight weeks... Start the ninety-day today," verbatim per the shot-list), voice easing down on the last four words. Bottle label legible, unaltered.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B5","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:08","visual":"phone glowing full amber beside bottle, warm gold, slow push-in","camera":"level, still, slow push-in","audio":"VO opens, continues"},
{"t_start":"00:08","t_end":"00:14","visual":"held final frame, silence closing the ad","camera":"static hold","audio":"VO eases down, then silence"}],
"subject":"phone and referenced Puravita bottle, no hand or face","environment":"wood surface, morning light","lighting":"warm morning gold",
"dialogue":null,"vo_verbatim":"The label asks for six to eight weeks. That is how long a real recharge takes. So do not grab the small bottle and quit in week two. Start the ninety-day, and give it the runway. And somewhere around week six, you wake up before the alarm, and your wife looks at you over the coffee the way she used to. That is the battery coming back. Start the ninety-day today.",
"on_screen_text":"Start the 90-day today.","negatives":["no reflections","no invented label text","no hand or face","no subtitle overlay","no music under the final line"],
"start_frame_ref":"assets/images/B5_start.png","product_ref":"https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex"}
```

---

## Teaser 1 - Hook 1, ~12s (first send)

**Routing:** Primary **Veo 3.1** (Q7b) | Fallback **Seedance v1.5 Pro / Kling 3.0** (Q7d) | Start frame: **Yes** - real bottle photo attached, single continuous scene.

**START FRAME - GPT Image 2**
```
<<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label).
A 35mm film photograph of a hand settling a phone flat on a nightstand at dawn, screen reading a five-percent battery icon in soft red, cool light. No face.
```

**VEO 3.1 / FLOW (two 8s passes chained, 9:16)**
```
Pass 1 (0:00-0:08): [00:00-00:03] Hand settles phone per start frame, five-percent icon in soft red. [00:03-00:08] Cut to extreme close-up, icon glowing amber and dimming.
A calm male voice says (no on-screen speaker), "Your phone warns you when it drops to five percent. Your body never does."
Pass 2 (0:00-0:04, seeded from Pass 1's final frame): <<<image_1>>> = product reference. Cut to the referenced bottle set beside the phone, glow climbing toward full, warm morning light, slow push-in.
Voiceover continues, "There is a battery inside you that you have never seen. Start the ninety-day today."
Ambient noise: quiet room tone. Style: cool dawn to warm gold, no reflections, no face.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A hand settles a phone flat on a nightstand at dawn, screen reading a five-percent battery icon in soft red, cut to an extreme close-up of the icon glowing amber and dimming, cut to `<<<image_1>>>` set beside the phone as its glow climbs toward full in warm morning light, slow push-in throughout. A quiet male voiceover reads the full line ("Your phone warns you... Start the ninety-day today," verbatim per the shot-list), each sentence on its cut. No reflections, no face.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"TEASER1","duration_s":12,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:08","visual":"hand settles phone at five percent, cut to icon glowing amber then dimming","camera":"static, then cut to close-up","audio":"VO sentence 1, sentence 2 begins"},
{"t_start":"00:08","t_end":"00:12","visual":"referenced bottle beside phone, glow climbing to full","camera":"cut, slow push-in","audio":"VO closes with CTA"}],
"subject":"hand, phone, referenced Puravita bottle, no face","environment":"nightstand at dawn to warm morning","lighting":"cool dawn to warm gold",
"dialogue":null,"vo_verbatim":"Your phone warns you when it drops to five percent. Your body never does. There is a battery inside you that you have never seen. Start the ninety-day today.",
"on_screen_text":"The battery you can't see.","negatives":["no reflections","no face","no invented label text","no subtitle overlay"],
"start_frame_ref":"assets/images/TEASER1_start.png","product_ref":"https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex"}
```

---

## Teaser 2 - Hook 3, ~12s (first send)

**Routing:** Primary **Kling 2.6/3.0 Omni** (Q7a, narrator beat) + **Veo 3.1** (Q7b, b-roll close) | Fallback **Veo 3.1** whole-clip | Start frame: **Yes** - portrait for narrator, bottle photo for close.

**START FRAME - GPT Image 2**
```
A (narrator): A cinematic editorial portrait of a man with a weathered complexion and gray-flecked hair at the temples, at a kitchen table in warm morning light, charcoal knit sweater, hands still, direct eye line, no smile.
B (product close): <<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label). A phone at the edge of frame with a dim amber glow, the referenced bottle beside it in the same warm light.
```

**VEO 3.1 / FLOW (fallback whole-clip route, two 8s passes chained, 9:16)**
```
Pass 1 (0:00-0:04, seeded from Still A): static medium shot, warm kitchen, narrator says, "My wife says she misses me. I'm sitting right next to her," plain delivery, small pause before the second sentence, no smile.
Pass 2 (0:00-0:08, seeded from Still B): <<<image_1>>> = product reference. Extreme close-up, phone battery icon glows amber and dims, cut to the referenced bottle set down as glow climbs toward full.
Voiceover continues, "There is a battery inside you that you have never seen. Start the ninety-day today."
Ambient noise: quiet kitchen tone, then quiet room tone. Style: soft window light, then warm gold, no reflections.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING (talking-human route, primary, opening beat only)**
```
Shot 1 (0:00-0:04): narrator from Still A, warm kitchen light, direct to camera, "My wife says she misses me. I'm sitting right next to her," plain delivery, small pause before the second sentence, hands still, no smile.
Audio timeline: shared track, quiet kitchen tone under the line.
Identity lock: face and wardrobe held per Still A.
Remaining beats (battery icon dimming, bottle set down) are separate Veo generations per the block above, edited in.
```

**HIGGSFIELD**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A man with a weathered complexion and gray-flecked hair at the temples, seated at a kitchen table in warm light, says to camera, "My wife says she misses me. I'm sitting right next to her," cut to an extreme close-up of a phone battery icon glowing amber and dimming, cut to `<<<image_1>>>` set down in the same warm light as the glow climbs toward full, voiceover continuing, "There is a battery inside you that you have never seen. Start the ninety-day today." No reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"TEASER2","duration_s":12,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:04","visual":"narrator direct to camera, no smile","camera":"static medium shot","audio":"dialogue"},
{"t_start":"00:04","t_end":"00:12","visual":"cut to icon glowing amber then dimming, then referenced bottle set down, glow to full","camera":"cut to close-up, then static","audio":"VO plays, closes with CTA"}],
"subject":"narrator (kitchen beat), then phone and referenced bottle (product beat)","environment":"warm kitchen, then wood surface","lighting":"soft window light, then warm gold",
"dialogue":"My wife says she misses me. I'm sitting right next to her.","vo_verbatim":"My wife says she misses me. I'm sitting right next to her. There is a battery inside you that you have never seen. Start the ninety-day today.",
"on_screen_text":"I'm sitting right next to her.","negatives":["no smile","no reflections","no invented label text","no subtitle overlay"],
"start_frame_ref":"assets/images/TEASER2_stillA.png;TEASER2_stillB.png","product_ref":"https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex"}
```

---

## Teaser 3 - Hook 4, ~14s (first send)

**Routing:** Primary **Veo 3.1** (Q7b) | Fallback **Kling 3.0** (b-roll) / **Seedance v1.5 Pro** (Q7d, bottle beat) | Start frame: **Yes, three stills (A/B/C)**, same fix as H4.

**START FRAME - GPT Image 2 (three stills)**
```
A: A 35mm film photograph of a phone screen filling the frame, held flat, bold white text on black reading "STOP BLAMING YOUR AGE," higher contrast, no reflections, no face.
B: A corner of a printed lab report in soft shadow, one small green check mark catching light, no hand, no face, same contrast grade as A.
C: <<<image_1>>> = product reference (real Puravita Magnesium Complex bottle, exact label). A phone with a low amber battery glow, the referenced bottle beside it, light easing cool to warm gold.
```

**VEO 3.1 / FLOW (14s across 3 chained segments, 9:16)**
```
[00:00-00:05] Seeded from Still A: phone reads "STOP BLAMING YOUR AGE," higher contrast, no reflections, no face.
[00:05-00:09] Hard cut, seeded from Still B: lab report corner, green check mark holds steady.
[00:09-00:14] Hard cut, seeded from Still C: <<<image_1>>> = product reference. Referenced bottle beside a phone whose glow climbs low to full, warm morning light.
A brisk male voice says (no on-screen speaker), "Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why. No five percent warning. Start the ninety-day today," each sentence timed to its cut.
Ambient noise: quiet room tone, easing toward warmth on the final cut. Style: higher-contrast opening easing to warm gold, no reflections.
NO SUBTITLES. No captions. No spoken-line text overlay.
```

**KLING:** n/a (not a narrator clip).

**HIGGSFIELD**
`<<<image_1>>>` = product (real Puravita Magnesium Complex bottle, exact label). A phone held flat to camera reads "STOP BLAMING YOUR AGE" in bold white on black, cut to a lab report corner with one small green check mark, cut to `<<<image_1>>>` set beside a phone whose battery glow climbs from low to full in warm morning light. A brisk male voiceover reads the full line ("Stop blaming your age... Start the ninety-day today," verbatim per the shot-list), each sentence timed to its cut. Higher contrast opening, easing to warm gold by the close.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"TEASER3","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":"00:00","t_end":"00:09","visual":"phone reads STOP BLAMING YOUR AGE, cut to lab report check mark","camera":"static, hard cut","audio":"VO opens, continues"},
{"t_start":"00:09","t_end":"00:14","visual":"referenced bottle beside phone, glow low to full","camera":"hard cut","audio":"VO closes with CTA"}],
"subject":"phone, lab report, referenced Puravita bottle, no face","environment":"high-contrast surface to warm wood surface","lighting":"higher contrast to warm gold",
"dialogue":null,"vo_verbatim":"Stop blaming your age. You sleep a full night and still wake up tired. The blood test that cleared you was never built to catch why. No five percent warning. Start the ninety-day today.",
"on_screen_text":"Stop blaming your age.","negatives":["no reflections","no face","no invented label text","no subtitle overlay"],
"start_frame_ref":"assets/images/TEASER3_stillA.png;TEASER3_stillB.png;TEASER3_stillC.png","product_ref":"https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex"}
```
