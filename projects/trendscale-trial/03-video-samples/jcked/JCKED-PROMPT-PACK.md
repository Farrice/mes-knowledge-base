# JCKED — Multi-Format Prompt Pack
Law: `research/AI-VIDEO-REALISM-RESEARCH.md` (canonical) + `JCKED-VIDEO-KIT.md` (VO/visual) + `skills/marketing-studio-director/SKILL.md` (Higgsfield format). VO verbatim throughout. No age markers, no antislop, no em-dashes.

**Flag codes (cited by tag on cards):** F1 subtitle guard is LIKELY-mitigation only, no official Google fix. F2 i2v may suppress on-camera dialogue, UNCONFIRMED. F3 Scene Builder Extend has a Veo-3-quality/audio version-drift contradiction — verify live. F4 Sora 2 excluded, short-runway risk (LIKELY). F5 Portable JSON is model-agnostic, not Veo input — prose is canonical, JSON-superiority UNCONFIRMED. F6 talking-human ranking (Kling/Veo/Sora) is LIKELY/directional — test per shot.

**NARR** (paste verbatim wherever `NARR` appears — satisfies the Q4 repeat-full-description-every-clip rule as a token to hold the word budget): *the lean, unpolished-faced presenter, dark stubble, charcoal crewneck, no branding, neutral matte-cabinet kitchen, warm light one side of his face and deep navy shadow the other, hands still with correct anatomy, no smile.*

`<<<image_1>>>` = JCKED bottle, real product photography, PDP `https://jcked.com/products/liquid-l-carnitine-4000mg`, label/cap/proportions exact, never restyled.

Audio rule, VO clips (H3, B1-B4, Teaser-H3): generate silent (SFX/ambient only); the single ElevenLabs narrator voice (Narrator Card) lays in post — native per-clip Veo audio won't match across a shared-voice sequence (Q5).

---

## H1 — Hook 1 (Variant A)

**Routing:** primary Kling 2.6/3.0 Omni (talking-human winner, F6) → fallback Veo 3.1 (single ≤8s beat) → start frame: GPT Image 2 narrator portrait, Ingredients/identity ref both routes.

**START FRAME — GPT Image 2**
```
Cinematic editorial portrait of NARR, mid-shot, matte dark cabinetry, shallow
depth of field, muted warm-and-navy palette, film-photograph texture, eyes direct
to camera, flat unsmiling expression.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: handheld phone-native selfie, eye-level. Subject: NARR.
[00:00-00:03] Stands still, warm light on one side of his face, begins: "You can
do everything right and still carry the same fat for years."
[00:03-00:08] Continues flat, no smile: "The effort was never the problem. That
fat is locked," hard cut on the last word to a closed amber-lit steel vault gate.
Ambient noise: quiet kitchen room tone, faint street sound.
Negative: natural pore texture, no plastic sheen, hands
still with no extra fingers.
NO SUBTITLES. No captions. No on-screen text. ⚠F1
Style: muted warm-and-navy, authentic handheld micro-shake, not cinematic.
Image-to-video: start frame attached (Ingredients: narrator face). ⚠F2
9:16, 1080×1920, 8s.
```

**KLING (talking-human route)**
```
Identity: NARR, held via the GPT Image 2 start frame.
Shot 1 (0-3s, handheld eye-level, kitchen): stands still, warm light one side of
face, says "You can do everything right and still carry the same fat for years."
Shot 2 (3-8s, same framing): "The effort was never the problem. That fat is
locked," flat, no smile, hard cut to the closed amber vault gate.
Shared audio timeline: his voice only, no music, room tone under the line.
```

**HIGGSFIELD**
A phone-native handheld take at eye level in a neutral kitchen, warm light across one side of his face, deep navy shadow on the other. The presenter stands still, hands at his sides with correct natural anatomy, and says to camera, "You can do everything right and still carry the same fat for years. The effort was never the problem. That fat is locked," flat, no smile, hard cut on the last word to a closed amber-lit steel gate filling the frame. Muted warm-and-navy color, handheld micro-shake, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H1","duration_s":8,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":3,"visual":"stands still, split light","camera":"handheld eye-level","audio":"line 1"},
{"t_start":3,"t_end":8,"visual":"hard cut to closed vault gate","camera":"handheld hard cut","audio":"line 2, silence"}],
"subject":"NARR","environment":"matte-cabinet kitchen","lighting":"warm one side/navy shadow other",
"dialogue":"You can do everything right and still carry the same fat for years. The effort was never the problem. That fat is locked.",
"vo_verbatim":"You can do everything right and still carry the same fat for years. The effort was never the problem. That fat is locked.",
"on_screen_text":"That fat is locked.","negatives":["no plastic skin","no hand warping"],
"start_frame_ref":"assets/stills/H1-start.png","product_ref":null}
```

---

## H2 — Hook 2 (bench, built not cut)

**Routing:** primary Kling 2.6/3.0 Omni → fallback Veo 3.1 → start frame: GPT Image 2 tighter medium close-up of same narrator.

**START FRAME — GPT Image 2**
```
NARR, tighter medium close-up, same kitchen, warm light one side of face, quiet
direct expression, no smile, hands out of frame.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: closer handheld than H1, eye-level. Subject: NARR.
[00:00-00:03] Stands still, same kitchen, begins quietly: "You train. The fat
sits there."
[00:03-00:07] "Same gut you have fought since you turned thirty-five, and it
will not move," flat, no smile, hands still.
Ambient noise: faint kitchen room tone.
Negative: frame free of clutter beyond the counter edge,
hands still with natural anatomy.
NO SUBTITLES. No captions. No on-screen text. ⚠F1
Style: muted warm-and-navy, handheld micro-shake.
Image-to-video: start frame attached (Ingredients: narrator face). ⚠F2
9:16, 1080×1920, 7s.
```

**KLING (talking-human route)**
```
Identity: NARR, tighter framing than H1, same reference still.
Shot 1 (0-7s, closer handheld, kitchen): stands still, says quietly "You train.
The fat sits there. Same gut you have fought since you turned thirty-five, and
it will not move," flat, no smile.
Shared audio timeline: his voice only, faint room tone, no music.
```

**HIGGSFIELD**
Closer handheld than H1, same kitchen, warm light on one side of his face. He stands still and says quietly to camera, "You train. The fat sits there. Same gut you have fought since you turned thirty-five, and it will not move," flat, no smile, hands still with natural anatomy. Handheld micro-shake, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H2","duration_s":7,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":7,"visual":"close medium, still","camera":"closer handheld eye-level","audio":"full line"}],
"subject":"NARR","environment":"matte-cabinet kitchen","lighting":"warm one side/navy shadow other",
"dialogue":"You train. The fat sits there. Same gut you have fought since you turned thirty-five, and it will not move.",
"vo_verbatim":"You train. The fat sits there. Same gut you have fought since you turned thirty-five, and it will not move.",
"on_screen_text":"It will not move.","negatives":["no plastic skin","no hand warping"],
"start_frame_ref":"assets/stills/H2-start.png","product_ref":null}
```

---

## H3 — Hook 3 (Variant B, vault only, no on-camera speech)

**Routing:** primary Veo 3.1 (cinematic-product winner) → fallback Kling 3.0 storyboard → start frame: GPT Image 2 vault-gate still. Audio: silent + ElevenLabs (see Audio rule above).

**START FRAME — GPT Image 2**
```
Cinematic wide shot, dark navy cell, bare steel walls fading to shadow, a single
closed vault gate glowing dim amber at center. No figures, cool navy ambient
light, one warm amber source, shallow haze, film-photograph texture.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: slow controlled dolly push, no cuts. Subject: closed vault gate,
no figures.
[00:00-00:04] Pushes forward through the dark navy cell, bare steel walls
receding into shadow.
[00:04-00:08] Amber glow sharpens as the gate fills more of the frame, cool navy
ambient light at the edges.
Ambient noise: low ambient hum, no music, no on-camera dialogue.
Negative: steel free of fingerprints or glare, no
reflections, push holds steady with no handheld shake.
NO SUBTITLES. No captions. No on-screen text.
Image-to-video: start frame attached. Generate silent. VO ("One enzyme decides
whether your stored fat gets burned or stays locked away. It has a name, and
most men never hear it.") is ElevenLabs, laid in post.
9:16, 1080×1920, 8s.
```

**HIGGSFIELD**
A composed shot inside a dark navy cell-like space, bare steel walls receding into shadow, a closed vault gate glowing dim amber at center frame. The camera pushes slowly forward on a controlled dolly, the amber glow sharpening as the gate fills more of the frame, cool navy ambient light holding the edges in shadow. Deliberate, unhurried movement, no cuts, brand-first mood, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H3","duration_s":8,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":4,"visual":"dolly through dark cell","camera":"slow controlled dolly","audio":"low hum"},
{"t_start":4,"t_end":8,"visual":"amber gate fills frame","camera":"dolly continues","audio":"hum, VO in post"}],
"subject":"closed amber vault gate, no figures","environment":"dark navy steel cell","lighting":"cool navy ambient, warm amber source",
"dialogue":null,
"vo_verbatim":"One enzyme decides whether your stored fat gets burned or stays locked away. It has a name, and most men never hear it.",
"on_screen_text":"One enzyme decides.","negatives":["no reflections on steel","no handheld shake"],
"start_frame_ref":"assets/stills/H3-start.png","product_ref":null}
```

---

## H4 — Hook 4 (Variant C)

**Routing:** primary Kling 2.6/3.0 Omni → fallback Veo 3.1 → start frame: GPT Image 2 bolder wider narrator portrait.

**START FRAME — GPT Image 2**
```
NARR, bolder slightly wider frame, same kitchen, leaning a touch forward, direct
unsmiling gaze, warm light catching one side of his face, a touch more contrast.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: handheld phone-native, more contrast/pace than H1/H2. Subject:
NARR, leaning slightly forward.
[00:00-00:03] Leans slightly forward, more edge, begins: "You took the right
supplement at the wrong dose."
[00:03-00:07] "Five hundred milligrams. The research that worked went up to
four thousand," flat, no smile, hands still.
Ambient noise: kitchen room tone, closer mic presence.
Negative: natural pore texture, no plastic sheen, hands
still with correct anatomy.
NO SUBTITLES. No captions. No on-screen text. ⚠F1
Style: muted warm-and-navy, more contrast, handheld micro-shake.
Image-to-video: start frame attached (Ingredients: narrator face). ⚠F2
9:16, 1080×1920, 7s.
```

**KLING (talking-human route)**
```
Identity: NARR, bolder wider frame, more contrast/pace than H1/H2.
Shot 1 (0-7s, handheld eye-level, kitchen): leans slightly forward, says with
edge "You took the right supplement at the wrong dose. Five hundred
milligrams. The research that worked went up to four thousand," flat, no smile.
Shared audio timeline: his voice only, closer mic presence, no music.
```

**HIGGSFIELD**
A phone-native handheld take, eye level, same neutral kitchen, warm light on one side of his face, a touch more contrast and quicker pace than the quieter hooks. The same presenter leans slightly forward and says to camera with more edge, "You took the right supplement at the wrong dose. Five hundred milligrams. The research that worked went up to four thousand," flat through the line, no smile, hands still with correct anatomy. Muted warm-and-navy color, handheld micro-shake, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"H4","duration_s":7,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":3,"visual":"leans forward, more contrast","camera":"handheld eye-level","audio":"line 1"},
{"t_start":3,"t_end":7,"visual":"holds edge in posture","camera":"handheld continuous","audio":"line 2"}],
"subject":"NARR (leaning forward, more contrast)","environment":"matte-cabinet kitchen","lighting":"warm one side, more contrast",
"dialogue":"You took the right supplement at the wrong dose. Five hundred milligrams. The research that worked went up to four thousand.",
"vo_verbatim":"You took the right supplement at the wrong dose. Five hundred milligrams. The research that worked went up to four thousand.",
"on_screen_text":"Right supplement. Wrong dose. 500mg.","negatives":["no plastic skin","no extra fingers"],
"start_frame_ref":"assets/stills/H4-start.png","product_ref":null}
```

---

## B1 — Body: the lock (shared)

**Routing:** primary Veo 3.1 → fallback Kling 3.0 → start frame: GPT Image 2 padlock macro still. Audio: silent + ElevenLabs. ⚠F3 — kit's "Part B" continuation for full ~20s VO relies on Scene Builder Extend; re-describe the full scene on the Part B prompt (Q4).

**START FRAME — GPT Image 2**
```
Cinematic close-up, heavy steel padlock on a plain dark vault door, lock face
engraved CPT-1, dim and matte under low directional light. Deep navy shadow
behind, one cool light raking the surface, shallow depth of field,
film-photograph texture.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: extremely slow push toward the lock face. Subject: steel padlock
engraved CPT-1.
[00:00-00:04] Holds still, dim matte steel, deep navy shadow behind, one cool
light raking the surface.
[00:04-00:08] Drifts in an extremely slow push, the CPT-1 engraving sharpening.
(Part B, re-describe scene in full: continue the identical push for VO
coverage past 8s.) ⚠F3
Ambient noise: low ambient hum, no music, no on-camera dialogue.
Negative: lock face dim and matte with no glare or
fingerprints, no hands or other objects, no reflections.
NO SUBTITLES. No captions. No on-screen text.
Image-to-video: start frame attached. Generate silent. VO ("That fat is locked
behind one door. The lock is an enzyme called CPT-1, and it sits between your
stored fat and where it gets burned. Without the key, the door does not open,
and the fat stays where it is. The one key that fits is a nutrient called
L-carnitine.") is ElevenLabs, laid in post.
9:16, 1080×1920, 8s (+ Part B extension for full ~20s VO).
```

**HIGGSFIELD**
A composed close-up of a heavy steel padlock on a plain dark vault door, lock face engraved CPT-1, dim and matte under one cool directional light, deep navy shadow behind. The camera holds still, then drifts in an extremely slow push toward the lock face, the CPT-1 engraving sharpening. No hands, no other objects, brand-first stillness, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B1","duration_s":20,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":10,"visual":"padlock CPT-1, holds still","camera":"locked close-up","audio":"low hum"},
{"t_start":10,"t_end":20,"visual":"slow push, engraving sharpens (Part B)","camera":"slow push, Extend","audio":"hum, VO in post"}],
"subject":"steel padlock engraved CPT-1","environment":"plain dark vault door","lighting":"one cool raking light, deep navy shadow",
"dialogue":null,
"vo_verbatim":"That fat is locked behind one door. The lock is an enzyme called CPT-1, and it sits between your stored fat and where it gets burned. Without the key, the door does not open, and the fat stays where it is. The one key that fits is a nutrient called L-carnitine.",
"on_screen_text":"Your fat is locked","negatives":["no fingerprints or glare","no hands or objects in frame"],
"start_frame_ref":"assets/stills/B1-start.png","product_ref":null}
```

---

## B2 — Body: proof (shared)

**Routing:** primary Veo 3.1 → fallback Kling 3.0 → start frame: GPT Image 2 key-entering-lock macro. Audio: silent + ElevenLabs. ⚠F3 — same Part-B/Extend flag as B1, for the ~23s VO span.

**START FRAME — GPT Image 2**
```
Cinematic macro, brass key beginning to enter a steel lock reading CPT-1, teeth
catching a thin line of warm light against cool navy shadow. Sharp focus on key
and lock, everything else soft dark, film-photograph texture.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: macro, key turning then match cut to a wider angle. Subject:
brass key and CPT-1 lock.
[00:00-00:04] Key turns with a slow mechanical rotation, vault door begins to
crack open along its seam, a thin warm line of light spilling from inside.
[00:04-00:08] Match cut wider as the gap widens, bold contrast between cool
exterior and warm interior glow. (Part B, re-describe in full: continue
widening the crack for VO coverage past 8s.) ⚠F3
SFX: a low mechanical creak.
Ambient noise: quiet studio room tone, no music, no on-camera dialogue.
Negative: no hands in frame, key and lock free of glare
or smudging, no reflections on brass or steel.
NO SUBTITLES. No captions. No on-screen text.
Image-to-video: start frame attached. Generate silent. VO ("This is the
rate-limiting step of fat burning, confirmed in 2023. A review of thirty-seven
trials and more than two thousand people found the doses that worked ran up to
four thousand milligrams a day, the top of the studied range. Even in men near
seventy, the door still opened, and fat burning went up about twenty percent.")
is ElevenLabs, laid in post.
9:16, 1080×1920, 8s (+ Part B extension for full ~23s VO).
```

**HIGGSFIELD**
A macro shot of a brass key sliding into a steel lock engraved CPT-1, warm light catching the key's teeth against deep navy shadow. The key turns with a slow mechanical rotation, and the vault door begins to crack open along its seam, a thin warm line of light spilling from inside. Match cut to a wider angle as the gap widens further, bold contrast between the cool exterior and warm interior glow, no hands in frame, beat-driven pacing, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B2","duration_s":23,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":11,"visual":"key turns, door cracks a sliver","camera":"macro, mechanical rotation","audio":"mechanical creak"},
{"t_start":11,"t_end":23,"visual":"match cut, gap widens (Part B)","camera":"wider angle, Extend","audio":"creak, VO in post"}],
"subject":"brass key entering CPT-1 lock","environment":"vault door seam","lighting":"warm interior glow vs cool navy exterior",
"dialogue":null,
"vo_verbatim":"This is the rate-limiting step of fat burning, confirmed in 2023. A review of thirty-seven trials and more than two thousand people found the doses that worked ran up to four thousand milligrams a day, the top of the studied range. Even in men near seventy, the door still opened, and fat burning went up about twenty percent.",
"on_screen_text":"37 trials. Up to 4,000mg.","negatives":["no hands in frame","no glare on brass or steel"],
"start_frame_ref":"assets/stills/B2-start.png","product_ref":null}
```

---

## B3 — Body: the right key (shared, product clip)

**Routing:** primary Veo 3.1 → fallback Kling 3.0 / Seedance v1.5 Pro (I2V identity-preservation lead, Q7d) → start frame: GPT Image 2 two-key composition, `<<<image_1>>>` baked in so the label never renders in video. Audio: silent + ElevenLabs.

**START FRAME — GPT Image 2**
```
<<<image_1>>>. Composed shot, two brass keys side by side on dark steel under
cool directional light, a short stub engraved 500, a full-length key engraved
JCKED matching the bottle's label from <<<image_1>>>. Full key visibly longer
and more substantial. Deep navy background, shallow depth of field,
film-photograph texture.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: hold, then slow push onto the JCKED key. Subject: two brass
keys, stub engraved 500 vs full-length engraved JCKED.
[00:00-00:04] Holds on the pair on dark steel, cool directional light, deep
navy shadow behind.
[00:04-00:08] Slow push in until only the JCKED key fills the frame, a sharp
warm highlight along its edge.
Ambient noise: quiet studio room tone, no music, no on-camera dialogue.
Negative: no hands in frame, engravings sharp and
legible since text lives in the start frame, no reflections on brass or steel.
NO SUBTITLES. No captions. No on-screen text.
Image-to-video: start frame attached, label baked in per Q2/Q7c, never
re-rendered. VO ("Most carnitine products stop near five hundred milligrams.
A fraction of a key. That is why the bottle in your cabinet never moved
anything. JCKED carries the real dose, the size the studies used. It is the
key, cut to your lock.") is ElevenLabs, laid in post.
9:16, 1080×1920, 8s.
```

**HIGGSFIELD**
`<<<image_1>>>` = JCKED bottle (label and cap exactly as shown, never restyled). A composed shot of two brass keys side by side on a dark steel surface under cool directional light, deep navy shadow behind. The stub key is engraved 500 and clearly undersized; the full-length key is engraved JCKED, proportions matching `<<<image_1>>>`. The camera holds on the pair, then pushes in slowly until only the JCKED key fills the frame, a sharp warm highlight along its edge. No hands, deliberate pacing, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B3","duration_s":16,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":4,"visual":"two keys, stub 500 vs full JCKED","camera":"locked hold","audio":"quiet studio tone"},
{"t_start":4,"t_end":8,"visual":"slow push onto JCKED key","camera":"slow push","audio":"tone, VO in post"}],
"subject":"two brass keys: stub 500, full-length JCKED","environment":"dark steel, deep navy background","lighting":"cool directional, warm highlight on JCKED key",
"dialogue":null,
"vo_verbatim":"Most carnitine products stop near five hundred milligrams. A fraction of a key. That is why the bottle in your cabinet never moved anything. JCKED carries the real dose, the size the studies used. It is the key, cut to your lock.",
"on_screen_text":"Most stop at 500mg","negatives":["no hands in frame","label baked into still"],
"start_frame_ref":"assets/stills/B3-start.png","product_ref":"assets/product/jcked-bottle-pdp.jpg"}
```

---

## B4 — Body: close, bottle reveal (shared, product clip)

**Routing:** primary Veo 3.1 → fallback Kling 3.0 → start frame: GPT Image 2 open-vault hero still, `<<<image_1>>>` baked in. Audio: silent + ElevenLabs; money-back line plays over a held extension of this shot in edit.

**START FRAME — GPT Image 2**
```
<<<image_1>>>. Wide shot, heavy steel vault door standing open onto warm amber
light spilling from inside, dark navy exterior giving way to a glowing
interior. The bottle from <<<image_1>>> sits centered on a dark pedestal
inside the doorway, lit from the side by the interior glow. Shallow depth of
field, film-photograph texture.
```

**VEO 3.1 / FLOW — timestamped**
```
Cinematography: slow dolly forward, settling into a composed hero shot.
Subject: JCKED bottle on a pedestal inside the open vault doorway.
[00:00-00:04] Dollies slowly toward the open vault door, warm amber interior
light spilling into the dark navy exterior.
[00:04-00:08] Settles on the JCKED bottle centered on its pedestal, the vault
frame holding steady, deep navy shadow at the edges.
Ambient noise: a sparse low pulse fading to silence on the last word, no music.
Negative: label sharp and legible since it lives in the
start frame, no reflections in steel or glass, no camera shake once settled.
NO SUBTITLES. No captions. No on-screen text.
Image-to-video: start frame attached, label baked in per Q2/Q7c. VO ("First
bottle is forty-nine ninety-five, backed by a full year. Three hundred
sixty-five days to get every dollar back, even if the bottle is empty, no
questions asked. The lock has a key now. Go open it.") is ElevenLabs, laid in
post, and "Go open it" lands as the pulse fades to silence.
9:16, 1080×1920, 8s (held extension in edit covers the full ~14s VO).
```

**HIGGSFIELD**
`<<<image_1>>>` = JCKED bottle (label, cap, and proportions exactly as shown, never restyled). A wide shot of a heavy steel vault door standing open, warm amber light spilling from the dark navy exterior into a glowing interior. The JCKED bottle sits centered on a dark pedestal inside the doorway, catching the warm light along its label. The camera dollies slowly forward and settles in a composed hero shot, the vault frame holding steady around it, deep navy shadow at the edges, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"B4","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":4,"visual":"dolly toward open vault, amber spill","camera":"slow dolly","audio":"low pulse"},
{"t_start":4,"t_end":8,"visual":"settles on bottle hero shot","camera":"held composed frame","audio":"pulse fades on final word"}],
"subject":"JCKED bottle on pedestal, open vault doorway","environment":"steel vault door, dark navy exterior, amber interior","lighting":"warm amber spill vs deep navy shadow",
"dialogue":null,
"vo_verbatim":"First bottle is forty-nine ninety-five, backed by a full year. Three hundred sixty-five days to get every dollar back, even if the bottle is empty, no questions asked. The lock has a key now. Go open it.",
"on_screen_text":"365-day money-back guarantee","negatives":["no invented label text","no reflections in steel or glass"],
"start_frame_ref":"assets/stills/B4-start.png","product_ref":"assets/product/jcked-bottle-pdp.jpg"}
```

---

## Hook-Teaser Cards (12-15s, first sends)

Single-render, multi-beat clips: narrator/vault hook → key-turning mechanism → bottle reveal. Higgsfield TV Spot is the fastest finished sample; Veo/Kling below chain the same beats for a second pass.

### Teaser 1 (Hook 1 lineage)

**Routing:** primary Kling 3.0 Omni multi-shot storyboard (native shared-audio handling of talking + object cuts, Q4) → fallback Veo 3.1 Scene Builder (chain 2 hops ~7s each, full re-description per hop, Q4) → start frame: GPT Image 2 narrator still + `<<<image_1>>>` for the closing beat.

**VEO 3.1 / FLOW — timestamped (chained, describe fully each hop)**
```
Cinematography: handheld selfie opening, hard cuts to macro/wide product beats.
Subject: NARR, then a brass key, then the JCKED bottle.
[00:00-00:03] NARR stands still, warm light one side of face, says: "You can
do everything right and still carry the same fat for years."
[00:03-00:07] "The effort was never the problem. That fat is locked," flat, no
smile, hard cut to a brass key turning inside a CPT-1 lock, warm light
spilling as the door cracks open.
[00:07-00:14] (Scene Builder hop, re-describe in full) Cut to the door
standing fully open, the JCKED bottle from `<<<image_1>>>` centered on a dark
pedestal in the amber doorway, camera settling on a composed hero push.
Ambient noise: kitchen tone under dialogue, mechanical creak on the key turn,
quiet studio tone on the bottle beat.
Negative: no reflections in the sequence, label exactly
as baked into the still, hands still with correct anatomy.
NO SUBTITLES. No captions. No on-screen text. ⚠F1 ⚠F3
9:16, 1080×1920, ~14s across chained hops.
```

**HIGGSFIELD**
`<<<image_1>>>` = JCKED bottle (real product photography, label and cap exact). A composed shot opens on the lean, unpolished-faced presenter in a charcoal crewneck in a neutral kitchen, warm light on one side of his face, saying to camera, "You can do everything right and still carry the same fat for years. The effort was never the problem. That fat is locked," flat, no smile. Hard cut to a brass key turning inside a steel lock engraved CPT-1 on a dark vault door, warm light spilling as the door cracks open. Cut to the door standing fully open, the JCKED bottle from `<<<image_1>>>` centered on a dark pedestal in the amber doorway, camera settling on a composed hero push, deep navy framing, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"TEASER-H1","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":7,"visual":"NARR hook, hard cut to key turning in CPT-1 lock","camera":"handheld then macro cut","audio":"dialogue, mechanical creak"},
{"t_start":7,"t_end":14,"visual":"vault open, JCKED bottle hero push","camera":"composed dolly push","audio":"quiet studio tone"}],
"subject":"NARR, then brass key/CPT-1 lock, then JCKED bottle","environment":"kitchen then vault interior","lighting":"warm/navy split then amber interior",
"dialogue":"You can do everything right and still carry the same fat for years. The effort was never the problem. That fat is locked.",
"vo_verbatim":"You can do everything right and still carry the same fat for years. The effort was never the problem. That fat is locked.",
"on_screen_text":"That fat is locked.","negatives":["no reflections","label baked into still"],
"start_frame_ref":"assets/stills/TEASER-H1-start.png","product_ref":"assets/product/jcked-bottle-pdp.jpg"}
```

### Teaser 3 (Hook 3 lineage, VO only, no on-camera narrator)

**Routing:** primary Veo 3.1 Scene Builder (chain, full re-description) → fallback Kling 3.0 storyboard → start frame: GPT Image 2 vault-gate still + `<<<image_1>>>` for closing beat. Audio: silent + ElevenLabs (sixth clip sharing the one narrator voice, Q5).

**VEO 3.1 / FLOW — timestamped (chained, describe fully each hop)**
```
Cinematography: slow dolly push opening, hard cuts to macro/wide product
beats. Subject: closed vault gate, then brass key, then JCKED bottle.
[00:00-00:04] Pushes slowly toward a closed vault gate glowing dim amber in a
dark navy cell.
[00:04-00:07] Hard cut to a brass key turning inside the CPT-1 lock, warm
light spilling as the door cracks open.
[00:07-00:14] (Scene Builder hop, re-describe in full) Cut to the door
standing fully open, the JCKED bottle from `<<<image_1>>>` centered on a dark
pedestal in the doorway, camera settling on a hero push.
Ambient noise: low ambient tone throughout, mechanical creak on the key turn,
a sparse low pulse under the final hold.
Negative: no reflections in the sequence, steel and
glass free of glare, label exactly as baked into the still.
NO SUBTITLES. No captions. No on-screen text.
Image-to-video: start frames attached per beat. Generate silent. VO ("One
enzyme decides whether your stored fat gets burned or stays locked away. It
has a name, and most men never hear it.") is ElevenLabs, laid in post. ⚠F3
9:16, 1080×1920, ~14s across chained hops.
```

**HIGGSFIELD**
`<<<image_1>>>` = JCKED bottle (label exact). A composed shot opens inside a dark navy cell, camera pushing slowly toward a closed vault gate glowing dim amber. Hard cut to a brass key turning inside the CPT-1 lock, warm light spilling as the door cracks open. Cut to the door standing fully open, the JCKED bottle from `<<<image_1>>>` centered on a dark pedestal in the doorway, camera settling on a hero push. Native audio: a calm male voiceover states, "One enzyme decides whether your stored fat gets burned or stays locked away. It has a name, and most men never hear it," low ambient tone, a sparse low pulse under the final hold, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"TEASER-H3","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":7,"visual":"vault gate amber glow, hard cut to key turning","camera":"slow dolly then macro cut","audio":"ambient tone, creak"},
{"t_start":7,"t_end":14,"visual":"vault open, JCKED bottle hero push","camera":"composed hero push","audio":"low pulse under final hold"}],
"subject":"closed vault gate, then brass key/CPT-1 lock, then JCKED bottle","environment":"dark navy steel cell then vault interior","lighting":"cool navy ambient then amber interior",
"dialogue":null,
"vo_verbatim":"One enzyme decides whether your stored fat gets burned or stays locked away. It has a name, and most men never hear it.",
"on_screen_text":"One enzyme decides.","negatives":["no reflections","no glare on steel or glass"],
"start_frame_ref":"assets/stills/TEASER-H3-start.png","product_ref":"assets/product/jcked-bottle-pdp.jpg"}
```

### Teaser 4 (Hook 4 lineage)

**Routing:** primary Kling 3.0 Omni multi-shot storyboard → fallback Veo 3.1 Scene Builder chain → start frame: GPT Image 2 bolder narrator still + `<<<image_1>>>` for closing beat.

**VEO 3.1 / FLOW — timestamped (chained, describe fully each hop)**
```
Cinematography: handheld selfie opening, more contrast/pace, hard cuts to
macro/wide product beats. Subject: NARR leaning forward, then two brass keys,
then the JCKED bottle.
[00:00-00:04] NARR leans slightly forward, more edge, says: "You took the
right supplement at the wrong dose. Five hundred milligrams. The research
that worked went up to four thousand."
[00:04-00:07] Hard cut to two brass keys side by side on dark steel: a stub
engraved 500, a full-length key engraved JCKED, camera pushing onto the
full-length key.
[00:07-00:14] (Scene Builder hop, re-describe in full) Cut to the vault door
standing open, the JCKED bottle from `<<<image_1>>>` centered in the amber
doorway, camera settling on a hero push, deep navy framing.
Ambient noise: kitchen tone under dialogue, quiet studio tone on the key beat,
low pulse on the bottle beat.
Negative: no reflections in the sequence, hands still
with correct anatomy, key engravings and label exactly as baked into their
stills.
NO SUBTITLES. No captions. No on-screen text. ⚠F1 ⚠F3
9:16, 1080×1920, ~14s across chained hops.
```

**HIGGSFIELD**
`<<<image_1>>>` = JCKED bottle (label exact). A composed shot opens on the same presenter, warm light on one side of his face, more contrast and pace, leaning slightly forward and saying with edge, "You took the right supplement at the wrong dose. Five hundred milligrams. The research that worked went up to four thousand." Hard cut to two brass keys side by side on dark steel: a stub engraved 500 beside a full-length key engraved JCKED, camera pushing onto the full-length key. Cut to the vault door standing open, the JCKED bottle from `<<<image_1>>>` centered in the amber doorway, camera settling on a hero push, deep navy framing, no reflections.

Generate: https://higgsfield.ai/s/general-higgsfieldai-vKnfpx

**PORTABLE JSON**
```json
{"clip_id":"TEASER-H4","duration_s":14,"aspect":"9:16",
"beats":[{"t_start":0,"t_end":7,"visual":"NARR hook with edge, hard cut to two keys","camera":"handheld then push cut","audio":"dialogue, studio tone"},
{"t_start":7,"t_end":14,"visual":"vault open, JCKED bottle hero push","camera":"composed dolly push","audio":"low pulse"}],
"subject":"NARR, then two brass keys, then JCKED bottle","environment":"kitchen then vault interior","lighting":"warm/navy split, more contrast, then amber interior",
"dialogue":"You took the right supplement at the wrong dose. Five hundred milligrams. The research that worked went up to four thousand.",
"vo_verbatim":"You took the right supplement at the wrong dose. Five hundred milligrams. The research that worked went up to four thousand.",
"on_screen_text":"Right supplement. Wrong dose. 500mg.","negatives":["no reflections","no hand warping"],
"start_frame_ref":"assets/stills/TEASER-H4-start.png","product_ref":"assets/product/jcked-bottle-pdp.jpg"}
```
