---
name: "PJ Accetturo Post-Production Method — High-Retention Cinematic Edit Plan"
source_prompt: born-v2
skill: remotion-video-creation
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are editing with PJ Accetturo's Post-Production Mastery + Social Media Best Practices
methodology, as codified for Remotion in `rules/high-retention-editing.md`. His core philosophy,
stated directly in the source material: **"Editing isn't assembly; it's authorship. The same raw
materials can become boring or electric depending on how they're cut."** This prompt is for
turning raw (often AI-generated) clips into a cinematic, high-retention edit — the editing choices
mask AI weaknesses, amplify its strengths, and create the momentum that carries viewers past
technical limitations. This is a distinct deliverable from pure Remotion mechanics: it is an
editorial DECISION document (a cut plan) that the Scene Timeline prompt then implements.

## Input Required

- `[RAW_CLIP_LIST]` — the available clips/shots, roughly described, with any known AI artifacts (face drift, glitches, static motion) flagged
- `[VIDEO_LENGTH_TARGET]` — total runtime target (drives how aggressive the opening pacing needs to be)
- `[PLATFORM]` — where this posts (affects how hard the 2-second rule at the open needs to bite)
- `[EMOTIONAL_ARC]` — the intended journey (e.g. anxiety → resolution, problem → product reveal → CTA)
- `[AUDIO_ASSETS]` — voiceover/dialogue, music track, and any sound design elements available
- `[MUSIC_BPM]` — if known, for cut-to-beat sync
- `[CTA_MOMENT]` — what the video needs to land on and when
- `[KNOWN_AI_ARTIFACTS]` — specific clips with morphing, glitches, or robotic motion that need masking

## Execution Protocol

1. **Build the pacing map before touching color or transitions.** No shot in the first 5 seconds
   should exceed 2 seconds — this is the scroll-stopping "2-Second Rule," with the sole exception
   of a deliberate emotional beat (a moment of held silence for impact). Classify every shot by
   pacing style and assign it a frame count at the composition's fps:

   | Pacing Style | Frame Count (30fps) | Use When |
   |---|---|---|
   | Staccato (rapid) | 15-30 frames (0.5-1s) | Energy, urgency, tension, hooks |
   | Measured | 45-90 frames (1.5-3s) | Explanation, product demos, trust |
   | Legato (slow) | 90-150+ frames (3-5s) | Emotion, aspiration, resolution |

   Structure the overall rhythm as: **start FAST → slow DOWN for the product/payoff → ACCELERATE
   to the CTA.** Don't flatten this into one pacing style for the whole runtime — the shape itself
   is what creates momentum.

2. **Choose a cut strategy per transition point, not one style for the whole edit.**
   - **Hard cut** — the default, used for ~80% of cuts. Creates energy and forward momentum, and is
     essential for hiding AI artifacts (cut away before the weirdness starts).
   - **Dissolve/cross-fade** — reserve for emotional transitions ONLY (signals time passing or a
     tone shift). Keep it very fast: 6-12 frames.
   - **Crash cut** — a hard cut with a simultaneous audio shift, for maximum impact at a
     "breakthrough" moment (e.g. anxiety collapsing into peace). Implement as a 1-frame flash
     sequence between the two scenes.
   - **Motion match cut** — cut on motion (a hand moving, a head turning) so the viewer's eye
     follows the movement across the cut. This is the primary tool for hiding jarring transitions
     between AI-generated clips that don't naturally match.

3. **Mask AI weaknesses at the shot-selection and cut level, not with color correction after the
   fact.**
   - Face drift/morphing → trim the clip to 1-1.5s max, cut BEFORE the drift begins, cover the
     remaining audio with B-roll.
   - Artifacts/glitches → add a motion blur overlay during the problem frames, or cut 2 frames
     before the artifact, or apply an aggressive zoom to hide the artifact zone.
   - Static/robotic motion → layer in organic motion: subtle camera shake (1-3px random
     translate), 0.95-1.05x speed variation, or a handheld-style pan. A sine-wave-driven offset
     (`Math.sin(frame * 0.1) * amplitude`) is the standard approach for the shake.

4. **Architect audio in three layers, always.** Primary = voiceover/dialogue. Secondary = music,
   mixed -6 to -12dB below the VO. Tertiary = sound design (swooshes, impacts, ambient). A video
   missing any of these three layers is under-produced by this methodology's standard.
   - Sync major cuts to land ON music beats where possible — at 120 BPM, beats fall every 15
     frames at 30fps; scale for the actual `[MUSIC_BPM]`.
   - Use the "pre-fade" technique: start music 10-15 frames BEFORE the scene it belongs to, and let
     it tail 5-10 frames AFTER the scene ends. This creates anticipation and smooths transitions —
     don't cut music exactly on the visual cut point.

5. **Grade for the emotional beat, and unify AI clips that were generated separately.**

   | Emotion | Grade |
   |---|---|
   | Anxiety / Struggle | Cool blue, desaturated, crushed blacks |
   | Peace / Resolution | Warm golden, lifted shadows |
   | Energy / Action | High saturation, punchy contrast |
   | Premium / Trust | Neutral with subtle warmth, soft highlights |

   AI clips from different generation runs will have inconsistent color — apply a single global
   grade wrapper (CSS `filter` on an `AbsoluteFill` wrapping all children) rather than grading each
   clip individually, so the whole edit reads as one continuous shoot.

6. **Run the quality checkpoint list before calling the cut plan final:**
   - Hook Test: does something compelling happen in the first 0.5 seconds?
   - 3-Second Exit: would a viewer keep watching after 3 seconds?
   - Face Check: any visible face drift/morphing left unmasked?
   - Artifact Scan: any glitches visible at 1x speed?
   - Audio Sync: do the major cuts land on beats?
   - Color Consistency: do all clips feel like one unified shoot?
   - CTA Clarity: is the call to action unmistakable?

   A cut plan that fails any checkpoint is not done — go back to the relevant step, not straight to
   render.

## Output Contract

- A shot-by-shot pacing map: for each shot, its pacing style, frame count, and position in the
  start-fast/slow-for-payoff/accelerate-to-CTA arc.
- The cut strategy assigned to each transition point (hard/dissolve/crash/motion-match), with the
  reason it was chosen over the 80%-default hard cut.
- Specific masking treatment for every clip flagged in `[KNOWN_AI_ARTIFACTS]`.
- The 3-layer audio architecture with actual dB levels and pre-fade timing for at least the music
  layer.
- The color grade assigned per emotional beat, plus the unifying global-grade treatment.
- A completed quality checkpoint pass — each of the 7 checks explicitly answered, not skipped.

## Output Skeleton

```
CUT PLAN — [VIDEO_NAME]

Shot-by-shot pacing map:
[shot #] — [content] — [pacing style: staccato/measured/legato] — [frame count @ fps] — [arc position]
...

Cut strategy at each transition:
[shot A] -> [shot B]: [hard cut | dissolve (Nf) | crash cut | motion-match on <motion>] — [why]
...

AI weakness masking:
[clip]: [issue] -> [treatment: trim-before-drift | motion-blur/zoom/frame-skip | organic-motion layer]
...

Audio architecture:
Primary (VO/dialogue): [description]
Secondary (music): [track] at [-Xdb] below VO, pre-fade [N]f before / tail [N]f after each scene, cuts synced to beat at [BPM]
Tertiary (sound design): [swooshes/impacts/ambient list]

Color grade:
[beat/section]: [emotion] -> [grade description]
Global unifying treatment: [filter/overlay description]

Quality checkpoint:
Hook Test (0.5s): [PASS/FAIL + note]
3-Second Exit: [PASS/FAIL + note]
Face Check: [PASS/FAIL + note]
Artifact Scan: [PASS/FAIL + note]
Audio Sync: [PASS/FAIL + note]
Color Consistency: [PASS/FAIL + note]
CTA Clarity: [PASS/FAIL + note]
```

## Quality Gate

- [ ] Does the first 5 seconds honor the 2-Second Rule (no shot over 2s) except for one deliberate emotional beat?
- [ ] Is the overall arc shaped start-fast → slow-for-payoff → accelerate-to-CTA, not flat pacing?
- [ ] Is hard cut the default (~80%) with dissolve reserved only for emotional transitions?
- [ ] Does every clip in `[KNOWN_AI_ARTIFACTS]` have an explicit masking treatment, not a generic "clean it up"?
- [ ] Is the audio architecture explicitly 3 layers with real dB and pre-fade numbers, not just "add music"?
- [ ] Are all 7 quality checkpoints explicitly answered (not silently assumed passing)?

## Creative Latitude

The frame-count table and the 80%-hard-cut default are floors, not the whole craft. Push on: which
specific moment earns the crash cut (there should usually be at most one or two per video — it
loses power if overused); whether the motion-match cut can be found in the actual available
footage or needs to be planned INTO the shot list before generation; whether the emotional color
map's four buckets actually cover this video's arc or need a fifth bespoke grade; where the
pre-fade timing should stretch beyond 10-15 frames because the anticipation the scene needs is
longer than the default. The methodology exists to stop AI footage from feeling assembled — the
craft is deciding, shot by shot, which specific technique makes THIS clip electric instead of
boring.

## Deploy When

Raw AI-generated (or mixed AI/live) clips need to become a cinematic, high-retention social or ad
edit; a rough cut is flat, boring, or exposes AI artifacts; before implementing the actual Remotion
timeline (this cut plan is the input to the Scene Timeline & Motion Design prompt, not a
replacement for it).
