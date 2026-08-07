# 05 — Model Override Prompts (When Super Agent Picks Wrong)

*Copy-paste override prompts for when Genspark Super Agent auto-routes to the wrong model. Saves credits, prevents brand drift, protects against the Sora-2 sunset trap.*

---

## When to Use This File

You're using Genspark Super Agent for convenience but the output is wrong:
- It picked Sora 2 (sunset model — don't use)
- It defaulted to a "cinematic" register that's actively wrong for Resonance
- It rotated models mid-series breaking continuity
- It added invisible "high-quality, cinematic, professional" tokens to your prompt

The prompts below force the routing back to the correct model.

---

## OVERRIDE 1 — Block Sora 2 (Sunset Model)

**Trigger**: Super Agent picks Sora 2 for any video task

**Why**: Sora app ended April 26, 2026. API ends September 24, 2026. Anything you build on Sora 2 prompting is dead infrastructure by Q3 2026.

**Override prompt** (prepend to any video request):

```
DO NOT use Sora 2 for this generation. Sora 2 was discontinued April 2026 and the API ends September 2026 — using it now means dead infrastructure. Force route to: Veo 3.1 Quality (for hero/landing/Substack), Kling 2.1 Master (for face close-ups), Runway Gen-4.5 (for story sequences), or Seedance 2.0 Pro (for IG Reel hero). Pick the model based on the asset class, not on novelty.
```

---

## OVERRIDE 2 — Force Veo 3.1 Quality for Hero Video

**Trigger**: Super Agent picks anything other than Veo 3.1 Quality for landing page hero / Substack embed

**Override prompt**:

```
Use Veo 3.1 Quality specifically for this generation. The reason: this is a landing-page-grade hero clip requiring (1) native audio (room tone + ambient city), (2) photoreal daytime light fidelity, (3) preservation of source image composition. Veo 3.1 Quality is the verified-best model for this combination. Do not route to Sora 2 (sunset), Kling (no native audio), Runway (story-sequence specialist, not hero-loop specialist), or Hailuo (768p ceiling). Veo 3.1 Quality. Confirm before generating.
```

---

## OVERRIDE 3 — Force Kling 2.1 Master for Face Close-Ups

**Trigger**: Super Agent picks Veo or Runway for close-up B-roll (face holds frame >3 seconds)

**Override prompt**:

```
Use Kling 2.1 Master specifically for this image-to-video generation. The reason: face holds frame for [N] seconds in a close-up shot, where Kling's face-stability beats Veo and Runway. Do not pad with scene description — image-to-video on Kling wants motion-only descriptors. Prompt structure: subject motion + what stays static + optional micro camera move. Under 40 words ideal, 1400 char hard cap.
```

---

## OVERRIDE 4 — Force Runway Gen-4.5 for Story Sequences

**Trigger**: Super Agent picks Veo or Kling for multi-clip story sequences (same character across 3+ clips)

**Override prompt**:

```
Use Runway Gen-4.5 specifically for this generation series. The reason: I need 95%+ character consistency across [N] sequential clips, which is Runway Gen-4.5's documented strength (only model with verified character lock from single reference). Do not route to Veo 3.1 (treats consistency as "strong suggestion, not guarantee" per Pollo AI review) or Kling (no character-consistency claim). Use the SAME reference image upload for every clip in the sequence — do not switch references mid-series.
```

---

## OVERRIDE 5 — Force Nano Banana Pro for Brand Stills (Continuity)

**Trigger**: Super Agent rotates models between brand still calls, breaking visual continuity

**Override prompt** (start every Resonance still generation with):

```
Use Nano Banana Pro for this generation AND for all subsequent Resonance brand stills this session. Lock to this model. The reason: visual continuity across the launch wave requires the same model rendering register. Switching models between stills (e.g., Nano Banana Pro → Flux 2 Pro → Ideogram V3) produces inconsistent brand register, recognizable to viewers even at thumbnail scale. Lock: Nano Banana Pro. Do not rotate.
```

---

## OVERRIDE 6 — Suppress Auto-Added "Cinematic, Professional, High-Quality" Tokens

**Trigger**: Super Agent invisibly adds "cinematic, professional, high-quality" to your prompt

**Override prompt** (append to any generation):

```
Do not add "cinematic, professional, high-quality, stunning, beautiful, breathtaking, award-winning, ultra-realistic, hyper-detailed" or similar magazine-cover marketing-photo tokens to this prompt. These tokens push the output toward generic AI-cinematic register that fails the Resonance brand standard (anti-club, anti-marketing-photo, documentary register). Strip them. Use only the descriptors I provided.
```

---

## OVERRIDE 7 — Force Daylight Light Source (Block Golden-Hour Drift)

**Trigger**: Output drifts toward golden-hour color grade despite negative prompts

**Override prompt** (prepend to lighting description in any prompt):

```
CRITICAL LIGHTING DIRECTIVE: The light source is "west-facing Chicago window, overcast October afternoon, 2pm." This is NOT "golden hour," "magic hour," "sunset," "warm light," or "sun-kissed." It is honest, slightly cool, overcast diffuse daylight. Color temperature: ~5200K (overcast daylight), NOT 3200K (tungsten/golden). Saturation: low. Shadows: soft and neutral, not warm-orange. If the model defaults to golden-hour grade despite this directive, reject and regenerate.
```

---

## OVERRIDE 8 — Force Documentary Register (Block Marketing-Photo Aesthetic)

**Trigger**: Output drifts toward Pinterest / Instagram-marketing / brand-deck aesthetic

**Override prompt** (prepend to style description):

```
STYLE DIRECTIVE: This is documentary photography, NOT marketing photography. Reference register: Hou Hsiao-hsien daylight interior scenes, Sofia Coppola loft interiority, Brian Welsh's Beats (2019) embrace shots, Wong Kar-wai with Christopher Doyle, Cuarón/Lubezki Y Tu Mamá También party scenes. NOT: Pinterest aesthetic, Instagram brand-deck, marketing campaign photo, stock photography, "lifestyle brand" register. The image must look SHOT, not generated, and must feel like a still from a film, not an ad.
```

---

## OVERRIDE 9 — Block Club-Coded Output from Seedance

**Trigger**: Seedance 2.0 drifts toward EDM/club energy despite explicit daytime prompt

**Override prompt** (always include in Seedance generations):

```
Seedance bias correction: Seedance 2.0 is trained heavily on dynamic motion and tends to drift toward club/festival energy. Counter this explicitly:
- BPM range: 95-110 ONLY (downtempo electronica, lo-fi house, NOT EDM)
- Reference: Roy Ayers, Sade, 90s deep house, NOT festival mainstage
- Crowd energy: small group conversational, 40-50 people max, NOT stadium
- Lighting: window daylight, NOT stage lighting
- Body language: recognition + slow motion, NOT raised-arms peak-time
- Wardrobe: linen, cotton, considered daywear, NOT clubwear, NOT festival fits

If output drifts club-coded despite this, regenerate at lower motion intensity OR switch to Veo 3.1 Fast (cheaper than Veo Quality, less likely to drift than Seedance).
```

---

## OVERRIDE 10 — Force Multi-Cultural Cast Specificity

**Trigger**: Output defaults to "generic-diverse" cast (everyone-looks-similar-brown)

**Override prompt** (always include for human-in-scene generations):

```
CAST DIRECTIVE: Resonance attendees are multicultural with SPECIFIC named ethnicities, not "generic diversity":
- Latina woman in her mid-30s (Costa Rican OR Colombian OR Mexican features — brown skin, dark hair, NOT "olive")
- Black man in his late 30s (mixed-Caribbean OR African-American — natural hair OR short fade, athletic build)
- White man with Polish-Italian features (architect posture, lean, NOT "generic white")
- Filipino woman in her early-30s (mature face, NOT 20-something Asian stereotype)
- Korean man in his mid-30s (architect glasses, considered restraint)

Mixed naturally in the frame — not pose-arranged for "diversity checkbox" tells. Ages 30-38 consistently. NO twenty-somethings, NO 45+, NO "ambiguously brown."
```

---

## OVERRIDE 11 — Force 9:16 Vertical for IG Reels

**Trigger**: Super Agent defaults to 16:9 horizontal for an IG Reel request

**Override prompt**:

```
This is an IG Reel — output must be 9:16 vertical (1080x1920), NOT 16:9. If your default is horizontal, override to vertical. Composition: subjects in vertical center, with safe-zone for IG UI (avoid bottom 200px and top 100px where captions/profile UI overlays).
```

---

## OVERRIDE 12 — Force 16:9 Horizontal for Landing Page Video

**Trigger**: Super Agent defaults to 9:16 vertical for a landing-page hero request

**Override prompt**:

```
This is a landing-page hero video — output must be 16:9 horizontal (1920x1080), NOT 9:16. The landing page hero block is widescreen; vertical video letterboxes badly. Override to horizontal.
```

---

## Universal Override (Use At Start of Every Resonance Session)

When opening Genspark for any Resonance work, paste this at the top of your first message:

```
RESONANCE SESSION OVERRIDE — apply to ALL generations this session:

1. NEVER use Sora 2 (sunset model — API dies Sept 2026)
2. Default routing matrix:
   - Brand stills → Nano Banana Pro (locked)
   - Stills with text → GPT Image 2
   - Landing/Substack hero video → Veo 3.1 Quality
   - IG Reel hero → Seedance 2.0 Pro
   - Face close-up B-roll → Kling 2.1 Master
   - Story sequence (3+ clips, same character) → Runway Gen-4.5
3. Universal lighting: West-facing Chicago window, overcast October 2pm. NOT golden hour. NOT magic hour. ~5200K color temperature.
4. Universal register: Documentary photography. Hou Hsiao-hsien / Sofia Coppola / Brian Welsh's Beats / Cuarón Y Tu Mamá También. NOT marketing photography. NOT Pinterest. NOT brand deck.
5. Universal negative tail (append to every prompt): no nightclub, no neon, no UV blacklight, no laser, no strobe, no crowd, no champagne pop, no slow-mo confetti, no golden hour, no fisheye, no shaky cam, no AI-blur on hands, no club lighting, no EDM stage, no festival, no smile-for-camera, no posed.
6. Universal cast specificity: Latina (Costa Rican/Mexican/Colombian) + Black (mixed-Caribbean/African-American) + Polish-Italian white + Filipino + Korean. Ages 30-38. No twenty-somethings.
7. Do NOT add "cinematic, professional, high-quality, stunning, beautiful, breathtaking" tokens invisibly. Strip them if you would otherwise.

Confirm you've absorbed this override before generating anything. Ask which model I want before generating if uncertain.
```

---

## When Overrides Don't Work (Last Resort)

If Genspark continues misrouting despite overrides:

1. **Switch to direct model calls** outside Genspark:
   - Veo 3.1 Quality via Google's Vertex AI ($0.50-0.75/sec)
   - Kling 2.1 Master via Kie.ai / Fal ($1.40-1.75/8s clip)
   - Runway Gen-4.5 via Runway directly (subscription)
   - Nano Banana Pro via Google AI Studio (Gemini 2.5 Flash Image)

2. **Use Higgsfield direct** for photoreal people (per `feedback_visual-tool-routing.md`)

3. **Document the misrouting** in `RISKS.md` so the routing matrix can be re-verified

Genspark is the convenience layer. When the convenience breaks the brand, leave the layer.

---

## Source: Why These Overrides Exist

Each override above traces to a specific observed failure mode:

- Override 1 (Sora 2): [OpenAI Discontinuation Notice](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)
- Override 2 (Veo for hero): [Curious Refuge Veo 3.1 Review](https://curiousrefuge.com/blog/veo-31-quality-ai-video-generator-review)
- Override 3 (Kling for close-up): [302.AI Kling vs Veo](https://medium.com/@302.AI/kling-2-6-vs-veo-3-1-pro-who-is-the-best-ai-video-generator-12769979b229)
- Override 4 (Runway for sequences): [Runway Gen-4 Research](https://runwayml.com/research/introducing-runway-gen-4)
- Override 5 (Nano Banana lock): Direct observation — multi-model rotation produces visual drift
- Override 6 (Strip cinematic tokens): Direct observation — auto-added tokens push to generic AI-cinematic register
- Override 7 (Daylight enforcement): Project-specific failure mode (Resonance posters drifted golden hour in v1)
- Override 8 (Documentary register): Project-specific failure mode (v2 hero shots drifted marketing-photo)
- Override 9 (Seedance club bias): Direct observation — Seedance training bias
- Override 10 (Cast specificity): `feedback_visual-tool-routing.md` — Andrea's brand requires named ethnicities, not generic diversity
- Override 11/12 (Aspect ratio): Genspark's auto-routing doesn't always match the deployment surface

---

*This completes the 6-file Genspark deployment pack. Use `README.md` as the index. Re-verify the catalog quarterly — the model landscape changes monthly.*
