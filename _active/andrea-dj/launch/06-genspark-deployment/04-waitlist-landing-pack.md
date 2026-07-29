# 04 — Waitlist Post + Landing Page Asset Pack

*Production-ready prompts for the pre-launch waitlist deployment + the assets that drop into `launch/waitlist-landing-page.html` (the 940-line landing page already built). Routes Veo 3.1 Quality for hero video + Nano Banana Pro for og:image + section heroes + email confirmation imagery.*

---

## Strategy in One Paragraph

The landing page exists (`launch/waitlist-landing-page.html`). The waitlist post is the pre-launch IG/Substack/LinkedIn content that drives traffic TO it. This pack generates: (1) the **landing page hero video** that replaces the static hero image with a 6-second ambient loop, (2) the **og:image** (the social-share preview when the landing URL is pasted on IG/Twitter/LinkedIn), (3) the **section hero images** for each landing page section, (4) the **waitlist post visuals** for IG + Substack + LinkedIn, (5) the **post-application email confirmation** hero image.

---

## ASSET 1 — Landing Page Hero Video

**Format**: 6-second ambient loop, native audio
**Model**: Veo 3.1 Quality
**Cost**: ~$6-7.50 (with audio)
**Aspect**: 16:9 horizontal 1920×1080 (matches landing page hero block)

### Reference image
The winning variant's strongest two-body recognition shot. If Andrea picks Variant B (likely): `variant-b-hero-shots-v3/B1-v1-3ef7ce7c.png`.

### The prompt
**Use the exact prompt from `01-image-to-video-prompts.md` ASSET 1 (Landing Page Hero Loop)**. Don't rewrite — copy verbatim from that file. Single source of truth.

### Deployment into landing page
Replace this block in `launch/waitlist-landing-page.html`:
```html
<img src="hero.jpg" alt="Resonance hero" class="hero-image" />
```
With:
```html
<video autoplay muted loop playsinline class="hero-video" poster="hero.jpg">
  <source src="resonance-hero-loop.mp4" type="video/mp4">
</video>
```
(The `poster="hero.jpg"` fallback uses the original v3 still while the video loads. Critical for slow connections.)

CSS adjustment: update the `.hero-image` class in the existing HTML's CSS block to `.hero-video` with `object-fit: cover; width: 100%; height: 100%;`.

---

## ASSET 2 — og:image (Social Share Preview)

**Format**: Static image, 1200×630 (standard og:image)
**Model**: Nano Banana Pro
**Cost**: FREE on Pro
**Aspect**: ~1.91:1 horizontal

### Why this matters
When anyone pastes the landing page URL into IG, Twitter, LinkedIn, iMessage, Slack — the preview card uses og:image. If it's wrong or missing, the link looks amateur. If it's perfect, the link itself becomes a piece of brand surface area.

### The prompt

```
1200x630 horizontal. Real photography: two adults (Latina woman + Black man, both mid-30s) mid-conversation in a daytime Chicago loft. Their bodies are oriented toward each other but the frame is wide enough to show the room — west-facing window light pouring across wood floor, terracotta brick wall in background, vintage DJ booth visible in soft mid-distance focus, no people-looking-at-camera.

35mm film grain, Hou Hsiao-hsien daylight register, documentary photography. Late-afternoon Chicago overcast, NOT golden hour.

Composition: subjects in left two-thirds, negative space right third (where social preview text overlay will appear from IG/Twitter algorithms).

The image should feel like a still from a film, NOT a marketing photograph. Real, lived, considered.

Negative: no AI faces, no smile-for-camera, no posed, no club, no neon, no golden hour, no festival, no stadium, no Pinterest aesthetic, no marketing-photo register.
```

### Deployment
Update `<meta property="og:image" content="..." />` in landing page `<head>` block. Host the image at the same domain as the landing page (Beehiiv, Carrd, custom domain).

---

## ASSET 3 — Landing Page Section Hero Images

The landing page has multiple sections. Each could use a section-specific photo background or accent image. Most should remain typographic (the landing page's design system favors restraint), but 2-3 photo accents add warmth.

### Section "What Resonance Is" — accent image

**Format**: 800×600 horizontal, section-level accent
**Model**: Nano Banana Pro
**Cost**: FREE

```
800x600 horizontal. Real photography: a single moment from a Chicago loft daytime — a hand on a turntable fader, west-facing window light from camera-left, wood DJ booth, cream wall in soft out-of-focus background. NO face, NO full body — just hand + booth + light.

35mm film grain, documentary photography. Late-afternoon Chicago overcast.

Composition: hand + fader in center-right, negative space upper-left.

Negative: no faces, no full body, no neon, no golden hour, no club, no Pinterest, no AI-shine.
```

### Section "The Mechanic" — accent image

**Format**: 800×600
**Model**: Nano Banana Pro

```
800x600 horizontal. Real photography: an empty Chicago loft floor at 2pm daylight, west-facing window casting a single diagonal of light across the wood. Vintage DJ booth visible in deep focus background. No people in frame. 35mm film, documentary.

Composition: empty room positioned in right two-thirds, negative space left third.

Negative: no people, no faces, no neon, no golden hour, no club, no Pinterest aesthetic.
```

### Section "The Application" — accent image

**Format**: 800×600
**Model**: Nano Banana Pro

```
800x600 horizontal. Real photography: a notebook open on a wood surface in late-afternoon Chicago daylight, real handwriting partially visible (text doesn't need to be legible — texture matters), a small ceramic cup beside it (matcha-green or terracotta glaze). 35mm film grain, documentary photography.

Composition: notebook in center, negative space left and right.

The image evokes Andrea reading applications by hand — concrete, lived.

Negative: no faces, no laptop (notebook only), no Pinterest aesthetic, no marketing-photo style, no AI-shine.
```

### Deployment
Add as `<img>` blocks within the existing landing page sections. Pair each photo with a `loading="lazy"` attribute for performance.

---

## ASSET 4 — Waitlist Post Variants (IG / Substack / LinkedIn)

These are the posts that drive traffic TO the landing page. Each format gets its own visual prompt.

### Waitlist Post — IG Single Image

**Format**: 1080×1080 (1:1)
**Model**: GPT Image 2 (text rendering) OR Nano Banana Pro (photo-with-overlay)

**Variant A — Typographic (use this first)**

```
Square 1080x1080. Cream #FBF7F0 background.

Centered serif GT Sectra terracotta #B8492E, 64px (top half):

"A daytime, sober, 
curated dance room.

Chicago. July 2026."

Below in serif midnight #0F1A2E, 36px (bottom half):

"For adults trying 
to meet a partner.

Waitlist open.

Link in bio."

Generous whitespace. Editorial register.

Negative: no logo, no decoration.
```

**Variant B — Photo-with-overlay (for accounts already familiar with the brand)**

```
Square 1080x1080. Real photography: a small group of adults mid-conversation in a Chicago loft daytime — west-facing window light, wood floor, terracotta brick in background. Multicultural cast (Latina, Black, white, Filipino). 35mm film grain, documentary.

Composition: group in lower two-thirds, negative space upper third for text overlay.

Cream typography overlay upper third in serif terracotta:

"A daytime, sober, 
curated dance room.

Chicago. July 2026."

Smaller cream Inter at bottom:

"Waitlist open. Link in bio."

Negative: no AI faces, no club, no neon, no golden hour, no smile-for-camera, no posed, no Pinterest.
```

### Waitlist Post — Substack Note

**Format**: 1456×819 hero image at top of Note
**Model**: Nano Banana Pro
**Cost**: FREE

```
Wide 1456x819. Real photography: a vintage DJ booth with two turntables in late-afternoon Chicago daylight, west-facing window light cutting across the wood booth surface, a hand mid-gesture on the fader (slightly blurred from real movement), cream wall in soft out-of-focus background. 35mm film grain, documentary photography. NOT staged.

Composition: hand + fader in lower-right third, negative space upper-left.

Negative: no faces, no full body, no club, no neon, no golden hour, no Pinterest, no marketing-photo aesthetic, no AI-shine.
```

The Substack Note copy (text below the image) handles the actual pitch. Image is the recognition trigger.

### Waitlist Post — LinkedIn

**Format**: 1200×627 (LinkedIn-optimized) or 1080×1080 (square cross-post from IG)
**Model**: GPT Image 2 or Nano Banana Pro

**LinkedIn typographic variant**:

```
1200x627 horizontal. Cream #FBF7F0 background.

Centered serif GT Sectra terracotta #B8492E, 56px (left half):

"I'm building a daytime
sober dance party
in Chicago.

For adults who want
to meet a partner."

Right half has typography in serif midnight, 28px:

"Why daytime? 
The room can't hide.

Why sober? 
The music does the work.

Why curated? 
The agreement makes the room.

First event July 2026. 
Waitlist link in bio.

— Andrea"

Editorial broadsheet layout. Two-column.

Negative: no logo, no decoration, no LinkedIn corporate aesthetic.
```

LinkedIn posts perform better with typographic / first-person founder voice. This variant treats the post as an editorial column, not a marketing card.

---

## ASSET 5 — Application Confirmation Email Hero

**Format**: 1456×819 hero image for the Beehiiv confirmation email
**Model**: Nano Banana Pro
**Cost**: FREE

### The prompt

```
Wide 1456x819. Real photography: an empty Chicago loft floor at 2pm daylight, west-facing window casting a single diagonal of warm-but-overcast light across warm hardwood. NO people. Architectural study — the room is the subject.

Vinyl record on a turntable visible in soft mid-distance focus. Cream wall behind. 35mm film grain, documentary photography. Hou Hsiao-hsien daylight register.

Composition: window light pattern in center, negative space upper-right.

The image evokes "the room is ready, waiting for you to arrive."

Negative: no people, no faces, no club, no neon, no golden hour, no Pinterest, no marketing-photo, no decorative styling.
```

### Where it deploys
Embedded at top of the Beehiiv "Application received" email confirmation that goes out after each Tally application submit. The email body uses copy from voice-document.md register; this image is the visual rest.

---

## ASSET 6 — Application Acceptance Email Hero ("You're in")

**Format**: 1456×819
**Model**: Nano Banana Pro
**Cost**: FREE

### The prompt

```
Wide 1456x819. Real photography: a small group of adults in a Chicago loft daytime, mid-conversation, the room visible around them — west-facing window light, wood floor, terracotta brick in background. Multicultural cast aged 30-38. Bodies oriented toward each other, NOT looking at camera. 35mm film, documentary, Cercle Adana Twins Palais Longchamp register.

Composition: group in middle two-thirds, negative space top + bottom for email layout.

The image evokes "you'll be in this room on July 18."

Negative: no AI faces (subjects are recognizable as bodies-in-room, not posed portraits), no club, no neon, no golden hour, no smile-for-camera, no Pinterest, no marketing-photo aesthetic.
```

### Where it deploys
Embedded at top of the Beehiiv "You're in for July 18" acceptance email. Sent within 1 week of application submission for accepted attendees.

---

## ASSET 7 — Application Decline Email Hero ("Not this round")

**Format**: 1456×819
**Model**: Nano Banana Pro

### The prompt

```
Wide 1456x819. Real photography: a quiet wide shot of an empty Chicago street in late-afternoon daylight, NOT a sad register — just a real street, real light. Could be Logan Square, Pilsen, Wicker Park. NO people, NO drama. 35mm film grain, documentary.

Composition: street in middle, light in upper third.

The image evokes "the next event might be your room" — NOT rejection, just honest scheduling.

Negative: no Pinterest aesthetic, no Instagram filter, no golden hour, no sad-girl mood-board aesthetic, no neon, no club.
```

### Where it deploys
Embedded at top of the Beehiiv "Not this round" decline email. Andrea adds the specific-reason line in the copy (per voice-document Section 4 decline scripts).

---

## ASSET 8 — Waitlist-Specific Visual ("You're on the list")

**Format**: 1080×1080 for IG sharable + 1456×819 for landing page section
**Model**: Nano Banana Pro

### The prompt (IG square version)

```
Square 1080x1080. Cream #FBF7F0 background with a very subtle photographic layer at 10% opacity (Chicago loft daytime, wood floor, no people, defocused).

Centered serif GT Sectra terracotta #B8492E, 80px:

"You're on the list."

Below in smaller serif midnight #0F1A2E, 28px:

"I'll send applications
to your email when
they open.

You're in early, on purpose.

— Andrea"

Negative: no logo, no decoration, no Pinterest, no AI-shine.
```

### Where it deploys
The visual that auto-attaches to the waitlist-signup confirmation email and can be screenshot-shared by signers if they want to publicly co-sign.

---

## Cost Summary (Waitlist + Landing Page Asset Wave)

| Asset | Model | Cost |
|---|---|---|
| Landing page hero video | Veo 3.1 Quality | ~$7.50 |
| og:image | Nano Banana Pro | FREE |
| Section heroes (3 images) | Nano Banana Pro | FREE |
| Waitlist post IG variants (2 options) | GPT Image 2 / Nano Banana Pro | FREE |
| Waitlist post Substack hero | Nano Banana Pro | FREE |
| Waitlist post LinkedIn variant | GPT Image 2 | FREE |
| Application confirmation email hero | Nano Banana Pro | FREE |
| Application acceptance email hero | Nano Banana Pro | FREE |
| Application decline email hero | Nano Banana Pro | FREE |
| Waitlist "you're on the list" graphic | Nano Banana Pro | FREE |
| **WAITLIST + LANDING TOTAL** | | **~$7.50** |

The hero video is the only paid asset. Everything else uses free image generation on Pro tier.

---

## Deployment Sequence (this week)

### Thu 5/28 (today)
1. Generate landing page hero video via Veo 3.1 Quality (~$7.50)
2. Replace static hero image in `launch/waitlist-landing-page.html` with video block
3. Generate og:image via Nano Banana Pro
4. Update og:image meta tag in landing page

### Fri 5/29 (Andrea sign-off pending)
5. Generate 3 section accent images
6. Generate waitlist post variants for IG + Substack + LinkedIn
7. Pre-stage application confirmation + acceptance + decline email hero images

### Mon 6/1 onward
8. Deploy waitlist post to IG + Substack Note + LinkedIn (cross-post)
9. Watch waitlist signups in Beehiiv

### Wed 6/3 (Phase 1 launch day)
10. The door carousel goes live (per `01-announcement-package/README.md`)
11. Bio link in IG points to landing page
12. Landing page hero video carries the brand impression

---

## Critical Failure Modes (and recovery)

1. **Veo 3.1 hero video drifts club-coded**: regenerate with stronger negative tail. If still wrong after 2 retries, fall back to Seedance 2.0 with tighter prompt — register might be tighter at slightly cheaper cost.

2. **og:image renders too dark / loses readability at IG preview size**: regenerate with lighter cream background or move subjects closer to center. Test on actual IG paste before deploying.

3. **Substack Note image gets cropped wrong in feed**: Substack auto-crops to ~16:9 — make sure key subject is in middle horizontal third, not edges.

4. **LinkedIn typographic post performs poorly**: pivot to Variant B (photo-with-overlay). LinkedIn audience often responds better to faces; but for Resonance brand integrity, lead with typographic.

5. **Email confirmation hero drifts marketing-photo**: that's the failure mode that makes the email feel like a brand-deck. Re-emphasize `"NOT marketing photograph, NOT Pinterest aesthetic"` in negative tail.

---

## Voice + Visual Integrity

Same checklist as `02-social-media-prompt-pack.md` Section Voice Integrity. Every asset must pass voice-document Section 7 before deploying.

---

*Next: `05-model-overrides.md` for when Genspark Super Agent picks the wrong model.*
