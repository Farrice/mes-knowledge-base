# Design Brief: The Authenticity Trap — LinkedIn Carousel

## Asset Type & Platform

- **Type**: LinkedIn carousel (PDF upload — native swipeable format)
- **Dimensions**: 1080 x 1080px (square — optimal for mobile LinkedIn feed)
- **Slide Count**: 8 slides
- **Format**: PDF export
- **Platform**: LinkedIn organic feed
- **Structure**: Hook → Problem → Insight → Framework → Proof → CTA

---

## Mood & Direction

**Mood Words**: Authoritative, Refined, Strategic, Warm, Commanding

**Aesthetic Reference**: Premium management consulting slide deck meets editorial magazine layout. Think McKinsey meets Monocle — not tech-startup blue, not influencer-flashy. This should feel like it came from someone who charges $5K/month, not someone who wants followers.

**Emotional Target**: The viewer (an executive coach making $200K-$500K) should feel *seen* — like someone finally articulated the tension they've been living with. Then they should feel *relieved* — there's a clear path forward. Then *curious* — who is this person and how do I learn more?

**Anti-Targets**: No LinkedIn-blue. No gradient mesh backgrounds. No "guru energy." No all-caps motivational quotes. No stock photography of people in suits shaking hands.

---

## Typography System

**Rationale**: Executive coaches live in a world of refined authority — boardrooms, keynotes, high-ticket proposals. The typography must signal "I belong in your world" without trying too hard. Applying Kittl Pattern 2 (Serif/Sans Mood Mapping): Authoritative + Refined = Serif-first. Applying Tacit 1 (90s Serif Secret): "Timeless but not stuffy" maps perfectly to the coaching ICP.

```
PRIMARY FONT: DM Serif Display — Regular/Italic
  Used for: Headlines, display text, key phrases, slide titles
  Why: High-contrast transitional serif with 90s elegance. Warm authority
  without stuffiness. Signals "I've been in premium rooms."

SECONDARY FONT: Inter — Regular (400) / Medium (500) / SemiBold (600)
  Used for: Body text, labels, supporting copy, slide numbers
  Why: Ultra-clean geometric sans. Professional legibility at small sizes.
  Pairs naturally with DM Serif via height-width contrast (Kittl Pattern 3).

TYPE SCALE:
- Display/Hero:     48px, DM Serif Display Regular, tracking -30, line-height 1.05
- Slide Title:      36px, DM Serif Display Regular, tracking -20, line-height 1.10
- Subtitle:         20px, Inter SemiBold, tracking +40, line-height 1.30, UPPERCASE
- Body:             18px, Inter Regular, tracking 0, line-height 1.55
- Label/Caption:    13px, Inter Medium, tracking +120, line-height 1.40, UPPERCASE
- Slide Number:     72px, DM Serif Display Italic, tracking -20, line-height 1.00

PAIRING RATIONALE:
- Height-Width Contrast (Pattern 3): DM Serif's tall, condensed strokes vs.
  Inter's open, wide letterforms create immediate visual hierarchy
- Letter Spacing as Mood (Pattern 4): Headlines tight (-20 to -30) for
  editorial authority. Labels loose (+120) for sophistication and breathing room
- Line Spacing Compression (Pattern 5): Display text at 1.05 — lines nearly
  touching for intentional, designed feel
- Gray Hierarchy (Pattern 11): Primary = full color, secondary = 55% opacity
```

---

## Color Palette

**Rationale**: LinkedIn feeds are dominated by white backgrounds and corporate blue. This palette deliberately avoids both — using deep warm charcoal as the base to stop the scroll, with a copper accent that signals premium warmth. The viewer's subconscious reads "this isn't another LinkedIn post — this is a consulting artifact."

```
PALETTE:
- Background:       #1C2030  (Deep charcoal-navy — rich, distinctive, premium)
- Card Surface:     #252B3B  (Slightly lighter — for content card layering)
- Primary Text:     #F0ECE4  (Warm off-white — not clinical white, feels human)
- Secondary Text:   #8A8F9E  (Cool muted gray — 55% hierarchy, body/supporting)
- Accent:           #C4956A  (Warm copper — sophistication signal, CTA highlight)
- Accent Light:     #D4B08C  (Lighter copper — for subtle emphasis, borders)
- Highlight:        #E8DFD0  (Soft cream — for callouts, key phrases)

MOOD RATIONALE:
- Dark background = pattern interrupt in LinkedIn's white feed
- Copper accent = warm authority (not cold corporate blue)
- Off-white text = approachable expertise (not sterile)
- The palette says "premium consultancy" not "tech startup"

GRADIENT (slide backgrounds):
  #1C2030 → #252B3B, 135° diagonal, subtle linear
  (Creates depth without distraction)

TEXTURE NOTE:
  Subtle paper grain overlay at 3-5% opacity on dark backgrounds
  (Adds tactile warmth per Kittl Tacit 5 — prevents "flat digital" feel)
```

---

## Content (Per Slide)

### SLIDE 1 — Cover/Hook
```
Label:    CONTENT STRATEGY FOR EXECUTIVE COACHES
Title:    Your Best Insights
          Are Dying in
          Private Rooms
Subtitle: (And Your LinkedIn Is a Ghost Town)

Psychology note:
  Hook uses Kallaway Pattern 3 (Curiosity Loop) — "dying in private rooms"
  creates a gap between what coaches KNOW about their expertise and what
  their LinkedIn SHOWS. Pattern 16 (Avatar Language): "private rooms" is
  exactly how coaches describe their work environment. The parenthetical
  subtitle adds a vulnerability twist that makes it personal.
```

### SLIDE 2 — The Problem
```
Number:   01
Title:    The Paradox
Body:     You transform Fortune 500 executives behind closed doors.

          Your frameworks reshape how leaders think.

          But on LinkedIn? You posted once last month.
          A quote graphic. Maybe a "Happy Monday."

          The coaches half as talented as you
          are getting the speaking gigs. The book deals.
          The inbound calls.

Psychology note:
  Kallaway Pattern 6 (Pain-Solution-Trust Triangle) — hits the Pain vertex
  with specific, identity-level language. "Coaches half as talented" triggers
  competitive awareness without being aggressive. This is their internal
  monologue played back to them.
```

### SLIDE 3 — The Trap Named
```
Number:   02
Title:    The Authenticity Trap
Body:     You've tried. ChatGPT gave you something that
          sounded like every other coach on the platform.

          Taplio felt like wearing someone else's suit.

          So you stopped. Because the one thing you refuse
          to compromise is your authenticity.

          Here's the irony: silence isn't authentic either.

Psychology note:
  Kallaway Pattern 3 (Curiosity Loop) — "silence isn't authentic either"
  is the head-fake. They expected validation for NOT posting. Instead,
  the content subverts their core belief. This creates cognitive dissonance
  that demands resolution on the next slide.
```

### SLIDE 4 — The Reframe
```
Number:   03
Title:    Authenticity Isn't
          DIY. It's Articulation.
Body:     Your clients don't think less of you because
          you have a designer for your slide decks.

          They don't question your expertise because
          someone else formats your proposals.

          Content is the same. The voice is yours.
          The articulation is the craft.

Psychology note:
  Kallaway Pattern 11 (Transformation vs. Information) — this slide doesn't
  give tips. It REFRAMES how they think about the problem. After this slide,
  they can never go back to "doing it myself = authentic" without
  remembering the designer/proposal analogy. Identity shift, not advice.
```

### SLIDE 5 — The Method (How)
```
Number:   04
Title:    Voice-First.
          Not Template-First.
Body:     It starts with how you actually talk.

          A 20-minute voice note about a client breakthrough.
          A rant about what the industry gets wrong.
          A story you told at dinner last week.

          Your words. Your frameworks. Your perspective.
          Translated into thought leadership that sounds
          exactly like you — because it started as you.

Psychology note:
  Kallaway Pattern 6 — Solution vertex. Demonstrates the MECHANISM, not just
  the result. "Voice note" is concrete and low-friction — it answers the
  unstated objection "but I don't have time to write." Pattern 19 (Validation
  Paradox): gives the full method openly, which signals expertise so deep
  they can share freely.
```

### SLIDE 6 — The Proof / Social Proof
```
Number:   05
Title:    What Changes
Body:     Instead of posting once a month when guilt hits,
          your LinkedIn becomes a client acquisition channel.

          3 posts per week that sound like you wrote them
          (because you basically did — with a voice note).

          Discovery calls from people who already trust you
          before the first handshake.

Callout:  "The content didn't just sound like me —
           it captured things I think but hadn't
           articulated yet."

Psychology note:
  Kallaway Pattern 7 (Buyer Journey) — moves from Solution Education to
  Product Education. The callout functions as social proof even as a
  hypothetical voice. The specific outcome "discovery calls from people
  who already trust you" is the exact business result coaches want.
```

### SLIDE 7 — The Offer
```
Number:   06
Title:    The Proof Run
Body:     5 LinkedIn posts from one voice capture session.
          Delivered in 48 hours.

          If they don't sound exactly like you,
          you pay nothing.

          $250. One time. Zero risk.

Label:    CURRENTLY ACCEPTING 5 COACHES PER MONTH

Psychology note:
  Scarcity (5/month) + risk reversal (pay nothing guarantee) + specificity
  ($250, 48 hours, 5 posts). The "Proof Run" name itself implies "I'm so
  confident I'll let you test me." This is Kallaway Pattern 19 — abundance
  positioning. The full method was given freely; the offer is to have it
  done FOR you.
```

### SLIDE 8 — CTA Close
```
Title:    Your insights deserve
          more than a private room.
Body:     DM me "PROOF" or comment below
          to reserve your Proof Run spot.

Label:    FARRICE CAIN — CONTENT STRATEGIST FOR EXECUTIVE COACHES

Psychology note:
  Callback to the opening hook ("private rooms") creates narrative closure —
  Kallaway Pattern 3 (close the curiosity loop). Single-word DM trigger
  ("PROOF") reduces friction to near-zero. The label establishes positioning
  without being salesy.
```

---

## Layout & Composition Spec

### Global Rules
```
- Canvas: 1080 x 1080px, square
- Margins: 80px all sides (safe zone for mobile crop)
- Content area: 920 x 920px
- Background: #1C2030 base with subtle 135° gradient to #252B3B
- Texture: Paper grain overlay, 3-5% opacity, multiply blend mode
- Slide numbers: 72px DM Serif Italic, #C4956A at 30% opacity,
  bottom-left corner (positioned at x:80, y:940)
- Consistent element: Thin horizontal copper line (#C4956A, 1px)
  spanning 120px, positioned top-right as a recurring motif
```

### SLIDE 1 — Cover
```
Layout: Vertical, center-aligned
Primary element: Title text (3 lines, stacked tight, DM Serif 48px)
Secondary: Label above (13px, uppercase, copper #C4956A, tracked +120)
Tertiary: Subtitle below title (18px, Inter, secondary gray #8A8F9E)
Spacing: Label → 24px → Title → 16px → Subtitle
Decorative: Thin copper horizontal rule (120px) centered below subtitle
Background: Solid #1C2030 with paper grain
Alignment: Everything centered vertically and horizontally in content area
```

### SLIDES 2-6 — Content Slides
```
Layout: Vertical, left-aligned
Primary element: Title (DM Serif 36px, warm off-white #F0ECE4)
Secondary: Body text (Inter 18px, secondary #8A8F9E, 1.55 line-height)
Tertiary: Slide number (DM Serif Italic 72px, copper at 30%, bottom-left)
Spacing: Number label (13px "01") → 16px → Title → 24px → Body
Max body width: 760px (prevents lines from running too long)
Decorative: Copper accent line (1px, 120px) top-right corner
Background: Subtle gradient #1C2030 → #252B3B at 135°

SLIDE 6 VARIATION (has callout):
  Callout block: #252B3B card with 1px copper left border
  Callout text: DM Serif Italic 16px, cream #E8DFD0
  Card padding: 24px
  Positioned below body text with 32px gap
```

### SLIDE 7 — Offer
```
Layout: Vertical, center-aligned
Primary element: Title "The Proof Run" (DM Serif 36px, centered)
Secondary: Offer details (Inter 18px, body text, center-aligned)
Tertiary: Price "$250" rendered large (DM Serif 48px, copper #C4956A)
Accent: Scarcity label in a subtle card (#252B3B, rounded corners)
  "CURRENTLY ACCEPTING 5 COACHES PER MONTH" — 13px, copper, tracked +120
Spacing: Title → 24px → Body → 32px → Price → 24px → Scarcity card
Background: Slightly deeper variation #181C2A for visual distinction
```

### SLIDE 8 — CTA
```
Layout: Vertical, center-aligned
Primary element: Title callback (DM Serif 36px, center)
Secondary: DM instruction (Inter 20px SemiBold, copper #C4956A)
  "DM me 'PROOF' or comment below"
Tertiary: Positioning label (13px, uppercase, tracked +120, #8A8F9E)
Spacing: Title → 24px → DM instruction → 40px → Label
Decorative: Copper horizontal rule (200px) centered between instruction and label
Background: Match slide 1 (solid #1C2030) for bookend feel
```

---

## AI Imagery Prompts

No AI-generated imagery for this carousel. The design is typography-dominant — a deliberate choice:

1. **Typography-forward carousels signal expertise** on LinkedIn (vs. stock photo carousels that signal amateur)
2. **Dark background + serif + copper accent** creates enough visual distinction to stop scrolls without imagery
3. **The content IS the design** — executive coaches respect substance over decoration

If imagery is desired for future iterations:
- Abstract geometric shapes (copper wireframe cubes, minimal) as subtle background elements
- Never: headshots, stock photos, AI faces, office imagery

---

## CEV Pre-Check

### Composition: 8.5/10
Strong left-aligned grid system with consistent margins and spacing rhythm. The copper accent line provides visual continuity across slides. Slide number as watermark creates depth without clutter. The bookend structure (Slides 1 and 8 both centered, content slides left-aligned) creates satisfying narrative architecture.

*Minor note*: Watch for body text running long on Slides 2-3. May need to trim to stay within the 920px content area without feeling cramped.

### Effectivity: 9/10
This carousel is engineered to convert, not just engage:
- **Scroll-stop**: Dark background is a pattern interrupt in LinkedIn's white feed
- **Message clarity**: Each slide has one idea, legible in <3 seconds
- **CTA mechanics**: "DM me PROOF" is zero-friction, single-word trigger
- **Save-worthy**: The authenticity reframe (Slide 4) is the kind of insight people screenshot
- **Shareability**: "Your best insights are dying in private rooms" is quotable and tag-worthy

*The carousel hits all 3 vertices of Kallaway's Pain-Solution-Trust triangle.*

### Vibes: 8/10
The palette + typography combination creates "premium consulting artifact" energy — exactly right for executive coaches who spend their days in high-ticket environments. The copper accent adds warmth without being flashy. The serif headlines signal "I'm a peer, not a vendor."

*One concern*: The dark background might feel too "designer" for some coaches who prefer safe/clean aesthetics. This is a feature, not a bug — it signals taste and differentiates from the sea of white-background carousels. But worth noting.

### CEV Summary
```
C: 8.5/10 | E: 9/10 | V: 8/10
Overall: 8.5/10 — PASS

The brief is production-ready. Strongest dimension is Effectivity —
every slide is engineered for the specific conversion goal (Proof Run
DMs). The authenticity reframe on Slide 4 is the carousel's secret
weapon — it's the kind of belief-shifting content that gets saved and
shared, extending reach beyond the initial post.
```

---

## Handoff Notes for Pencil / Design Execution

1. **Font loading**: DM Serif Display + Inter are both Google Fonts (free, widely available)
2. **PDF export**: Each slide = one page in the PDF. LinkedIn auto-converts to swipeable carousel.
3. **Mobile-first**: All text sized for thumb-scrolling readability. Nothing below 13px.
4. **The paper grain texture** is subtle but critical — it prevents the dark background from feeling "digital/flat" and adds a tactile quality that signals craftsmanship.
5. **The copper accent line** (top-right, every slide) is the visual thread that creates carousel cohesion. Don't skip it.
6. **Slide 4 is the most important slide** — it's the belief-shift moment. Give it the most breathing room.
