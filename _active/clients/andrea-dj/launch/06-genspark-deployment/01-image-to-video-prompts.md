# 01 — Image-to-Video Prompts (Hero Shots → Motion)

*Production-ready I2V prompts for turning Resonance v3 hero shots into video clips. Three primary models — Veo 3.1 Quality, Kling 2.1 Master, Runway Gen-4.5. Verified May 2026.*

---

## How to use this doc

1. **Andrea picks the variant** (per `05-andrea-decisions.md`) — A / B / C
2. **Open the winning variant's v3 folder** — pick the hero shot you want to animate
3. **Upload that shot to Genspark** as reference image
4. **Find your asset surface below** (Landing hero / IG Reel / Substack embed / Story sequence)
5. **Copy the exact prompt** for the model assigned to that surface
6. **Paste into Genspark, attach the reference image, generate**

**Default reference shots** (best two-body recognition register):
- Variant A: `A1-v1-650362a0.png` or `A1-v2-e8fc1b96.png`
- Variant B: `B1-v1-3ef7ce7c.png` or `B1-v2-8dc32d1f.png`
- Variant C: `C1-v1-77e1a73d.png` or `C2-v1-2526407b.png`

---

## ASSET 1 — Landing Page Hero Loop (5-8s ambient, native audio)

**Model: Veo 3.1 Quality**
**Cost: ~$6-7.50 with audio**
**Aspect: 16:9 horizontal (matches existing landing-page HTML hero block)**
**Output: 1080p+ MP4 with native ambient room tone**

### The prompt (copy verbatim, paste into Genspark)

```
Aspect ratio: 16:9. Duration: 6 seconds. Image-to-video preservation: maintain source image composition, palette, and subject identity throughout.

Camera move: slow, subtle dolly-in 18mm equivalent, 3% scale increase over 6 seconds. No pan. No tilt.

Subject action: She turns her head slightly toward him, soft half-laugh, eyes crinkle. His head tilts in real listening, micro-nod. Her hand on his forearm shifts 1cm. Nothing dramatic — a moment that resolves rather than escalates.

Lighting: hold the source image lighting exactly. West-facing window-left, overcast Chicago afternoon, no flicker, no shadow movement beyond what the bodies make.

Audio: ambient low room tone, faint distant Chicago L train at 0:04, no music, no dialogue, no footsteps, no glass clinks. Quiet enough that a landing-page viewer with audio off doesn't notice loss, audio-on viewer hears city breath.

Style: 35mm film grain, handheld but locked, Hou Hsiao-hsien daylight register, In the Mood for Love interior intimacy. Documentary not stylized.

Negative prompts (suppress at end): no nightclub, no neon, no UV blacklight, no laser, no strobe, no crowd, no champagne pop, no slow-mo confetti, no golden hour, no fisheye, no shaky cam, no AI-blur on hands, no club lighting, no EDM stage, no festival, no smile-for-camera, no posed.
```

### Where it deploys
Drop into `launch/waitlist-landing-page.html` hero block as background video. Existing CSS class `.hero-image` becomes `.hero-video` with `<video autoplay muted loop playsinline>` wrapper. Muted-autoplay is the default; native audio activates if user unmutes.

### Iteration plan (if first generation drifts)
- **If end-of-clip morphs** (face shift, hand glitch): reduce duration to 5s, add `"hold subject stable, end on the same gesture started"` to prompt
- **If light drifts golden**: re-emphasize `"overcast Chicago afternoon, NOT golden hour, NOT magic hour, NOT sunset"` at the top of negative tail
- **If motion too aggressive**: cut camera move to "static frame, no dolly," let only the subjects move

---

## ASSET 2 — IG Reel Hero (10s vertical, joint audio-video)

**Model: Seedance 2.0 Pro**
**Cost: ~$1.20-1.50**
**Aspect: 9:16 vertical (1080×1920)**
**Output: 1080p+ MP4 with native audio**

### The prompt (copy verbatim)

```
Aspect ratio: 9:16. Duration: 10 seconds. Image-to-video: preserve source composition.

Shot list (3 beats over 10 seconds):
- 0:00-0:03: hold source image. Subjects in recognition pose. She mid-laugh, he listening. Camera static.
- 0:03-0:07: she leans 5cm closer, her hand shifts on his forearm, his head nods once. A small song moment lands — a piano chord, a vocal sample.
- 0:07-0:10: she pulls back, half-smile remains. Camera makes a 2% dolly-out, sound of a record needle finding the next groove. End on stillness.

Lighting: hold the source image. West-facing window-left, overcast Chicago 2pm. No light shift across the 10 seconds.

Audio: a single 95-110 BPM downtempo electronica track plays at low volume in background — think Roy Ayers "Everybody Loves the Sunshine" energy, NOT EDM, NOT club. Faint room tone underneath. No dialogue. The music carries the moment.

Style: 35mm film grain, locked frame, daytime interior, Cercle Adana Twins Palais Longchamp Oct 2019 daylight courtyard register. Brian Welsh's Beats (2019) embrace shot energy. NOT stadium, NOT festival, NOT EDM.

Negative prompts (suppress): no nightclub, no neon, no UV, no laser, no strobe, no crowd, no champagne, no slow-mo, no golden hour, no fisheye, no shaky cam, no AI-blur, no club lighting, no EDM stage, no festival, no smile-for-camera.
```

### Where it deploys
- Phase 1 Reel 1 (Wed 6/3 carousel companion)
- Phase 2 Reel 4 (Day 0 9am announcement Reel)
- Phase 3 Reel 6 (Mon 7/13 silent room reel — strip audio for that one)

### Critical Seedance flag
Seedance trained on dynamic motion. Without the BPM + "downtempo" callouts, it drifts to club energy. **Always include the "95-110 BPM, NOT EDM, NOT club" anchor.**

---

## ASSET 3 — IG Reel B-Roll Close-Up (8s, face holds frame)

**Model: Kling 2.1 Master**
**Cost: ~$1.40-1.75**
**Aspect: 9:16 vertical**
**Output: 1080p 30fps, no native audio (add in post or leave silent)**

### The prompt (copy verbatim — Kling-optimized, motion-only)

```
A small laugh begins at her mouth; his eyes hold hers. Hair shifts in the soft window light. Hand stays on forearm. Static frame, no camera move.

Negative: cluttered, neon, glitch, distortion, plastic skin, AI smoothing, club, nightclub, EDM, strobe, golden hour, fisheye.
```

**Note**: Kling I2V wants 15-40 words, motion-only. Don't pad with scene description — the source image owns that. Padding degrades motion quality.

### Where it deploys
- Phase 1 Reel 2 (Fri 6/12 founder origin — use for the "hand-on-record" beat or the close-face B-roll between voiceover lines)
- Phase 2 Reel 4 (Day 0 9am announcement Reel — between Andrea's on-camera + B-roll)
- Phase 3 Reel 5 (Wed 7/8 set preview — for the "hand on notebook writing a track name" beat)

### Kling-specific iteration
- **If face morphs at end**: shorten to 5s, add `"face stable throughout"` to prompt
- **If hand glitches**: regenerate; Kling occasionally loses hand fidelity on 8s+ clips. Falling back to 6s usually fixes it
- **If motion too subtle**: increase to `"laugh fully arrives, eyes crinkle deepens, shoulders rise 2cm"`

---

## ASSET 4 — Substack Post Embed (8-10s with audio)

**Model: Veo 3.1 Quality**
**Cost: ~$6-7.50 with audio**
**Aspect: 16:9 horizontal (Substack default)**
**Output: 1080p+ MP4**

### Why Veo here
Substack autoplays muted by default — but Veo's native audio means you don't have to source + sync audio separately later. When a reader chooses to unmute (which Substack readers do more than IG readers, per platform behavior), the room tone makes the embed feel "shot, not generated."

### The prompt (copy verbatim)

```
Aspect ratio: 16:9. Duration: 8 seconds. Image-to-video: preserve source composition.

Camera move: slow 2% dolly-in over 8 seconds. No pan. No tilt.

Subject action: She turns toward him, eyes find his. Half-laugh begins at second 3, lands at second 5. He smiles back at second 6 — quiet, the half-smile of someone who just heard something that landed. Her hand on his forearm doesn't move. Nothing escalates.

Lighting: hold the source image lighting. West-facing window-left, overcast Chicago afternoon. No shadow shift, no flicker.

Audio: faint distant Chicago city ambience (low traffic, an L train far off, no specific dialogue, no music). The room is quiet enough that the laugh lands without competition. Hold ambient low room tone underneath the entire 8 seconds.

Style: 35mm film, Hou Hsiao-hsien, In the Mood for Love loft intimacy. Documentary. NOT performance.

Negative: no nightclub, no neon, no UV, no laser, no strobe, no crowd, no champagne, no slow-mo, no golden hour, no fisheye, no shaky cam, no AI-blur, no club, no EDM, no festival.
```

### Where it deploys
- Phase 1 Substack Note 2 (Thu 6/4 trailer — "The most-asked question I get") — use as hero image at top of Note
- Phase 1 Substack Note 3 (Sat 6/13 Origin Wound + Bridge) — same
- Phase 1 Substack Note 4 (Sat 6/20 Public Reckoning) — same
- Phase 2 Day 0 5pm Email — embed at top of founder note

---

## ASSET 5 — Story Sequence (3-5 clips, same character across)

**Model: Runway Gen-4.5**
**Cost: $5-15 for full sequence ($1-3 per clip)**
**Aspect: 9:16 vertical (IG Stories) OR 16:9 (landing page sequence)**
**Output: 720p/1080p, 5-10s per clip**

### Why Runway here
Gen-4.5 is the only model with 95%+ character consistency from a single reference image. For a 5-frame Story sequence (Sat 6/13 "Day-in-the-Life" or Day 0 announcement Story carousel), you need the same Latina woman + Black man to appear identically across all 5 frames. Veo and Kling can't guarantee this.

### Sequence example: Phase 2 Day 0 Stories (5 frames at announcement)

**Reference image to upload**: pick ONE shot from the winning variant — the same shot for all 5 prompts. Runway locks to it.

**Frame 1 — Announcement (Story 13, "July 18.")**
```
Static frame, 4 seconds. Subjects hold pose from reference image. Slow 1% dolly-in. No subject movement except natural breathing and tiny eye shifts. Window-left overcast Chicago light, no shift.

Negative: morph, glitch, fisheye, motion blur on faces.
```

**Frame 2 — "Tap to read" (Story 14, 10am)**
```
4 seconds. She tilts her head 5° toward him. He listens. Light unchanged. Hand on forearm unchanged. Camera static.

Negative: morph, glitch, fisheye.
```

**Frame 3 — "Fifty seats" (Story 15, 12pm)**
```
4 seconds. He leans 3cm closer to her. Small smile lands on his face. She's mid-laugh from reference image. Camera static. Light unchanged.

Negative: morph, glitch, fisheye.
```

**Frame 4 — "Application open" (Story 16, 2pm)**
```
5 seconds. She laughs more — head tips back 3°, neck visible, recovery to half-smile. He shakes his head once in recognition of the joke. Hand unchanged. Camera static. Light unchanged.

Negative: morph, glitch, fisheye, neck distortion.
```

**Frame 5 — "Eighteen applications" (Story 17, 6pm)**
```
6 seconds. She glances away off-frame right (someone called her name, off-camera). Her hand finally lifts from his forearm — slow, natural. He watches her go. Window light shifts 2° warmer (late afternoon). Camera static.

Negative: morph, glitch, fisheye, harsh shadow.
```

### Where it deploys
All 5 Day 0 IG Stories per the Phase 2 calendar. Reuse the same character reference image across all 5 generations → 95% character consistency = the audience reads it as ONE Saturday documented in real-time.

### Iteration plan
- **If Frame 4's neck distorts** (Runway weak spot): regenerate Frame 4 with `"neck stays natural, no morph, no warp"` added
- **If Frame 5's hand lift glitches**: regenerate at 5s instead of 6s
- **If character drift between frames**: re-upload the reference image for each generation (don't rely on prior-clip character lock)

---

## ASSET 6 — T-7 Set Preview Reel (20s silent, room-led)

**Model: Veo 3.1 Quality (no audio)** or **Veo 3.1 Fast (cheaper)**
**Cost: $6-7.50 (Quality) or $0.15-0.40 (Fast)**
**Aspect: 9:16 vertical**

### The prompt

```
Aspect ratio: 9:16. Duration: 20 seconds. Image-to-video: use ambient daytime loft interior reference.

Shot list (5 beats):
- 0:00-0:04: stack of 10-15 vinyl on wood in 2pm daylight, hand pulls one
- 0:04-0:08: record placed on turntable, tight on needle
- 0:08-0:12: wider, hand on a notebook writing a track name (real handwriting feel, not staged)
- 0:12-0:16: close on a different record label half-visible, track shifts implied by music swell
- 0:16-0:20: pull back to stack now smaller, selected pile beside notebook

Camera: 5 separate static frames cut to in post, OR continuous slow camera moves between beats. Static cuts preferred — more documentary, less AI-video tell.

Lighting: 2pm overcast Chicago daylight, west-facing window cuts diagonal across wood floor. Hold consistent across all 5 beats.

Audio: silent (will be added in post with actual Andrea-curated music)

Style: 35mm film grain, documentary, Hou Hsiao-hsien stillness, NOT performance.

Negative: no nightclub, no neon, no glow, no people-in-frame except hands, no faces, no posed shots, no club lighting, no EDM, no festival.
```

### Where it deploys
Phase 3 Wed 7/8 IG Reel 5 (per calendar).

### Why no audio
The Phase 3 calendar specifies "20s silent" — Andrea adds her real curated music in post (the actual set track). Don't generate music with Veo for this; let Andrea soundtrack it.

---

## ASSET 7 — T-2 Room-Ready Reel (15s, ambient quiet)

**Model: Veo 3.1 Quality (no music, ambient only)**
**Cost: ~$6-7.50**
**Aspect: 9:16 vertical**

### The prompt

```
Aspect ratio: 9:16. Duration: 15 seconds. Image-to-video: empty Chicago loft daytime interior.

Shot list (4 beats):
- 0:00-0:04: the room from low angle in morning daylight, empty floor, glass of water on folded towel by the decks
- 0:04-0:08: turntable mid-setup, cables visible, record sleeve face-down
- 0:08-0:11: closed door, daylight pouring through, dust visible
- 0:11-0:15: pull back to a wider view from angle Andrea will see it from at the decks

Camera: slow static-to-static cuts. NO subject in frame. The room IS the subject.

Lighting: 2pm overcast Chicago. Hold consistent. NO shadow shift.

Audio: ambient low room tone, very faint distant city, no music, no dialogue. A needle drop sound at 0:14, music begins to swell but doesn't fully arrive (cuts at video end).

Style: 35mm film, documentary, Brian Welsh's Beats (2019) opening loft register. Empty rooms with weight.

Negative: no nightclub, no neon, no people (intentional — empty room), no glow, no club lighting, no EDM, no posed.
```

### Where it deploys
Phase 3 Tue 7/14 IG Reel 6 (per calendar). Shoot at venue if access permits; otherwise this AI generation fills the gap.

---

## Iteration & Override Doctrine

If a Genspark generation doesn't pass taste:

1. **First retry**: Same prompt, same model, different seed. Cheap.
2. **Second retry**: Same prompt, different model from the matrix (e.g., Veo → Kling for close-ups). Different model often catches what one missed.
3. **Third action**: Edit the prompt — usually the failure mode is one of these:
   - **Light drift**: re-emphasize physical light source, add 2-3 negative golden-hour callouts
   - **Motion too aggressive**: cut duration by 2s, change "she leans 5cm closer" to "she breathes"
   - **Face morph at end**: shorten duration, add "hold subject stable, end where they began"
   - **AI-blur on hands**: increase negative-prompt weight on `"no AI-blur on hands, no finger merging"`
4. **Fourth action**: regenerate the source still in Higgsfield Soul (direct, not Genspark) — sometimes the I2V failure is because the source still has a subtle issue Soul doesn't have

---

## Cost Summary (full launch wave)

| Asset | Model | Quantity | Cost |
|---|---|---|---|
| Landing page hero loop | Veo 3.1 Quality | 1 (+ 1 retry budget) | ~$15 |
| IG Reel hero (3 reels) | Seedance 2.0 | 3 (+ 1 retry each) | ~$8 |
| IG Reel B-roll (4 close-ups) | Kling 2.1 Master | 4 (+ 1 retry each) | ~$14 |
| Substack embeds (3 Notes) | Veo 3.1 Quality | 3 (+ 1 retry each) | ~$45 |
| Day 0 Story sequence | Runway Gen-4.5 | 5 frames (+ 1 retry budget) | ~$15 |
| T-7 Set preview | Veo 3.1 Fast | 1 (+ 1 retry) | ~$1 |
| T-2 Room-ready | Veo 3.1 Quality | 1 (+ 1 retry) | ~$15 |
| **TOTAL** | | | **~$113** |

**Reality check**: ~$113 for full launch video wave. ~0.7% of one-quarter Resonance revenue projection. **Cheap insurance** against the "look bad, lose the brand" failure mode the prior session caught with the 0/10 posters.

---

## Spike Test Before Locking (Mandatory)

Before generating the full $113 wave, run the spike from `00-capabilities-map.md` Section 8:
1. ONE hero shot
2. SAME prompt across Veo Quality + Kling Master + Runway Gen-4.5
3. Score on 5 dimensions
4. Lock the winner
5. Update this file with the spike results

**Budget**: ~$15 for the spike. **Time**: 30 min.

If Veo wins as expected, proceed with the full wave. If Kling or Runway win, reroute the matrix accordingly.

---

*Next: `02-social-media-prompt-pack.md` for daily/weekly social content prompts.*
