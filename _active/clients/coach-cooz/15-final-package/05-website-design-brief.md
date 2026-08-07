# COACH COOZ WEBSITE DESIGN BRIEF
## Premium aesthetic modeled on Ultimate Performance, voiced for The Resurrection Coach
## Date: 2026-04-08

> **Purpose**: Squarespace rebuild brief for Coach Cooz's site during Ignition Phase
> **Reference model**: ultimateperformance.com (visual architecture)
> **Brand source**: `14-ignition-plan/THE-IGNITION-PLAN.md` Section 7 + VOICE-GUIDE.md
> **Evolution target**: eventual transition to Dan Go-style application-gated funnel post-Scale Phase

---

# PART A — THE DESIGN BRIEF

## 1. Hero Layout Spec

The hero is the single most important square foot of the site. Ultimate Performance uses a background video — Cooz does not. A video demands celebrity presence, a gym crew, and professional cinematography Cooz doesn't have during Ignition. One large still photograph carries more weight at zero production cost.

**Layout**:
- Full-viewport-height section on desktop (min 760px, max 860px), 90vh on mobile.
- Single large photograph occupying the right two-thirds of the composition on desktop. On mobile it drops behind the text as a full-width backdrop with a dark gradient overlay.
- Headline stack pinned to the left third, vertically centered, with generous left padding (min 80px on desktop, 24px on mobile).
- One CTA button below the headline stack. Nothing else.

**Photo treatment**:
- Subject: Cooz, environmental portrait, inside his Burbank gym, natural side-lit window light, shallow depth of field. Not posed. Not flexing. Not pointing at the camera. He's working — mid-protocol, mid-thought, half-turned.
- Color grade: muted earth tones matching the brand palette. Shadows push toward Soil Brown `#3A2A1F`, highlights push toward Dawn Linen `#F3EEE3`. No crushed blacks, no blown highlights.
- Overlay: 20% Cathedral Black `#0E0E0C` gradient from the left edge fading to transparent at the photo's center — this is what lets the headline hold contrast without letterboxing the image.

**Headline stack** (top to bottom):
- Small all-caps kicker (Syne 700, 14px, letter-spacing 0.12em): `[THE RESURRECTION COACH]`
- Display headline (Fraunces 900, 64px desktop / 40px mobile, line-height 1.05, tracking -0.02em): `[I was coached. / Now I coach the men who were where I was.]` — left-aligned, two to three lines max
- Subhead (Fraunces 400 italic, 22px desktop / 17px mobile, line-height 1.4): `[12 weeks. One-on-one. Body-first. For the man whose body stopped letting him do his work.]`
- Single CTA (Syne 700 all-caps, 14px, letter-spacing 0.08em): `[BOOK THE TRIAGE AUDIT →]` — solid Ember Gold `#C08A3E` button with Cathedral Black text, 56px tall, 32px horizontal padding

**What NOT to include in the hero**:
- No background video. Static image only.
- No parallax scroll effects. They look dated and break on Safari mobile.
- No sliders, no carousels, no rotating testimonials.
- No stats bar inside the hero ("97% success rate" etc.). Cooz doesn't have 97% anything yet. The stats moment comes later, on the Meet Cooz page, honest to his current state.
- No secondary CTA. One button. One decision.
- No floating animated elements, no chat widget popups, no cookie bar at the top.

The hero does one job: convey seriousness in the first half-second and give the reader exactly one action.

---

## 2. Typography System

The visual packaging system in `12-expert-package/04-visual-packaging-system.md` already locks this. Reproducing it here in web-implementation form:

**Display font**: **Fraunces** (Google Fonts, variable weight, free)
- Hero headline: 900 weight, 64px desktop / 40px mobile, line-height 1.05, tracking -0.02em
- H1 (page titles): 800 weight, 52px desktop / 36px mobile, line-height 1.1, tracking -0.015em
- H2 (section headers): 700 weight, 36px desktop / 28px mobile, line-height 1.15, tracking -0.01em
- H3 (subsection): 700 weight, 24px desktop / 20px mobile, line-height 1.25
- Pull quotes: 300 italic, 28px desktop / 22px mobile, line-height 1.4, tracking 0

**Body font**: **Inter** (Google Fonts, free) — used ONLY where Fraunces would be overkill
- Body paragraphs (long-form): Fraunces 400, 18px desktop / 17px mobile, line-height 1.6
- Body paragraphs (UI / navigation / forms): Inter 400, 16px, line-height 1.5
- Buttons / labels / nav: Inter 600, 14px
- Meta text / captions / dates: Inter 400, 13px, color Stone Gray

**Accent font**: **Syne** (Google Fonts, free)
- Kickers and category tags: Syne 700 all-caps, 12-14px, letter-spacing 0.08em-0.12em
- Case study metadata labels: Syne 700 all-caps, 11px, letter-spacing 0.1em

**Fallback stacks**:
- Display: `"Fraunces", Georgia, "Times New Roman", serif`
- Body: `"Inter", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif`
- Accent: `"Syne", "Helvetica Neue", Arial, sans-serif`

**Typographic rules (from the visual packaging system, non-negotiable)**:
- Never more than three font weights visible on any single screen.
- Body copy line-height: 1.45–1.6 only.
- All-caps requires letter-spacing minimum 0.08em.
- Never center-align body paragraphs. Only headlines, pull quotes, and single-line statements center.
- Long-form body prose prefers Fraunces 400; Inter is the UI backup.

---

## 3. Color Palette

From `12-expert-package/04-visual-packaging-system.md` Section 1.2 — these are the only six colors. No exceptions, no trending accents, no gradient experiments beyond the pre-approved recipes.

| Role | Name | Hex | Web Usage | Contrast Notes |
|---|---|---|---|---|
| Primary Dark | Cathedral Black | `#0E0E0C` | Dominant background. Nav bar. Footer. Dark sections. Headline text on light surfaces. | 17.2:1 against Dawn Linen (AAA). 4.8:1 against Ember Gold (AA large text only). |
| Primary Light | Dawn Linen | `#F3EEE3` | Default page background. Body copy surfaces. Button text on dark buttons. | 17.2:1 against Cathedral Black (AAA). 3.1:1 against Ember Gold (fails body text, passes large display). |
| Secondary Warm | Soil Brown | `#3A2A1F` | Photo overlay gradients. Card frames on light backgrounds. Hover states on dark buttons. | 11.8:1 against Dawn Linen (AAA). |
| Secondary Cool | Stone Gray | `#5B5B55` | Body copy on light backgrounds when Cathedral Black is too heavy. Meta text, captions, form labels. | 6.9:1 against Dawn Linen (AA, passes body). |
| Accent 1 | Ember Gold | `#C08A3E` | Primary CTA button fill. The one emphasized word in a headline. Horizontal rule dividers in case studies. Max 5% of any composition. | 3.1:1 against Dawn Linen — use ONLY for large display text (20px+ bold) or as fill color behind Cathedral Black text. Never for body copy on light. |
| Accent 2 | Blood Rust | `#6B2B1D` | Reserved for emotional weight moments: the Resurrection Chronicles badge on case studies, the risk reversal callout on the offer page. Use 2-3 places per site maximum. | 9.4:1 against Dawn Linen (AAA). |

**Pre-approved gradient recipes** (from the visual system):
- Dawn Wash: `#0E0E0C` → `#3A2A1F` — used for photo bottom overlays behind text
- Cathedral Light: `#F3EEE3` → `#C08A3E` at 10% opacity — for Dawn Linen backgrounds that need atmospheric depth
- Soil Fade: `#3A2A1F` → `#0E0E0C` — for dark section transitions

**Accessibility note**: Default body copy on Dawn Linen backgrounds is Cathedral Black (17.2:1) or Stone Gray (6.9:1) — both pass AA. Ember Gold is display-only. Pure black on pure white is explicitly rejected — it's the wrong emotional temperature and it's what every other fitness coach defaults to.

---

## 4. Photography Direction

Stock photography is banned. Every image on the site is shot by Cooz (or Farrice with Cooz's iPhone) in his actual gym, on his actual body, with his actual clients. This is the single biggest defensible moat against the 10,000 identical online coaches — they all use Unsplash. Cooz doesn't.

**Photo Type 1 — The Hero Environmental Portrait (1 needed)**
- Subject: Cooz alone in his Burbank gym, working. Mid-protocol, not staged.
- Framing: 3/4 angle, medium shot, subject on the right third of the frame leaving left-third negative space for headline overlay.
- Lighting: Single natural window light source from camera-left, side-lit. No fill light, no ring light. Deep shadows on the right side of his face are correct.
- Time of day: Golden hour (first 90 minutes after sunrise or last 90 minutes before sunset). Shoot 2-3 times if first attempt doesn't hit.
- Wardrobe: Plain dark tee or tank, no logos, no branding. Not shirtless. Shirtless reads as influencer.
- Expression: Looking down at a barbell, a clipboard, or his hands. Not at the camera. Not smiling.
- Color target: Shadows around Soil Brown `#3A2A1F`, highlights around Dawn Linen `#F3EEE3`.

**Photo Type 2 — Cooz Working With A Client (3-5 needed, used across Meet Cooz and case study pages)**
- Subject: Cooz and a client in mid-coaching moment — spotting a lift, checking form, taking a measurement, reviewing the TrueCoach app on a phone.
- Framing: Wide environmental shots that show the gym context. Not tight on faces.
- Lighting: Natural gym light, no flash.
- Faces: Client's face is optional but consent-bound. Body shots, hands, backs of heads all work. Release form is signed before shoot.
- Use case: Interstitial breathers between text blocks on the Meet Cooz page, and as context photos inside case study pages.

**Photo Type 3 — The Gym Itself, Empty (3-4 needed)**
- Subject: Cooz's Burbank gym space. No people. Early morning, before anyone arrives.
- Framing: Wide environmental shots. Barbell on the floor. Empty racks. Chalk dust in a shaft of light.
- Lighting: Dawn light through whatever windows exist. Volumetric light if possible.
- Mood keywords from the visual system: *cinematic, masculine, restrained, dawn light, empty space, quiet*.
- Use case: Section dividers. Full-bleed hero images on sub-pages. The Path of the Parable visual metaphor — empty spaces that get filled.

**Photo Type 4 — Case Study Baseline and Exit Photos (4 per client, protocol from Section 4 of the Ignition Plan)**
- Subject: The client, in compression shorts, no shirt, neutral stance.
- Framing: Four fixed angles — front, back, left side, right side — standardized for every client.
- Lighting: Same time of day, same lighting conditions, same spot in the gym, every time. This is the most important rule. Inconsistent lighting on before/after destroys the credibility of the transformation.
- Background: Plain wall, Cooz's gym. Not a hotel mirror. Not a client bathroom selfie.
- Camera: Cooz's iPhone on a tripod, no filters, no edits except light-level normalization in post.
- Use case: The case study page magazine layout. Four photo sets per page (baseline / week 6 / week 12 / final), arranged as side-by-side before/after grids.

**Photo Type 5 — The Honest Detail Shot (2-3 needed, used on Meet Cooz and as texture)**
- Subject: Hands holding a notebook. A worn weight belt. A TrueCoach screen. Cooz's own face in profile, unguarded, close up.
- Framing: Tight. Shallow depth of field. Only one thing in focus.
- Lighting: Same natural window light, same golden hour discipline.
- Use case: Breakers between long text blocks on Meet Cooz. These are the details-that-prove-the-story photos. They do not have to be technically perfect — they have to be real.

Every photo gets run through a single Lightroom preset calibrated to the brand color targets (Soil Brown shadows, Dawn Linen highlights, desaturated earth-tone midtones). Farrice builds the preset once, Cooz applies it to every upload.

---

## 5. Case Study Page Template Spec

This is modeled directly on UP's Georgios page (`ultimateperformance.com/testimonial/georgios-lost-11kg-24lbs-in-just-13-weeks-to-banish-his-low-self-esteem`), adapted for Cooz's voice and the Ignition Plan Section 4 case study mechanism.

**Sections in order (top to bottom)**:

1. **Hero strip** — Full-width hero photo (Photo Type 4, front-facing before/after composite OR a hero environmental photo of the client mid-training). Cathedral Black overlay gradient from the bottom up. Headline stack overlaid on the bottom third: Syne kicker (`[CASE STUDY Nº 01]`), Fraunces 900 headline (`[Brian lost 31 lbs and rebuilt his squat in 12 weeks]`), Fraunces 400 italic subhead one sentence.

2. **Metrics bar** — Horizontal strip, Dawn Linen background, Cathedral Black text. Four metrics in equal columns: Weight change / Body fat or measurement change / Strength benchmark change / Duration. Each metric label in Syne 700 all-caps 11px, each number in Fraunces 900 48px. Below the bar, a single line: `[Age 38 · Small business owner · Burbank, CA]`.

3. **Pull quote lead** — The single strongest sentence from the exit interview, set large. Fraunces 300 italic, 36px, centered, max 20 words, Ember Gold quote marks. No attribution below (the whole page is the attribution).

4. **Opening narrative block** — 150-200 word paragraph introducing the client in Cooz's voice (I-led, diagnostic). Who they were before. The trigger event. Why they showed up. Fraunces 400, 18px, left-aligned, max-width 680px centered on the page.

5. **Full-width interstitial photo** — Photo Type 2 or Type 4, wide shot. No caption.

6. **Section 1 — "What was happening in your body before we started?"** — H2 header in Fraunces 700, then 200-300 words of client answer pulled from the exit interview transcript. This is the client's voice, not Cooz's. Italic indent or blockquote styling distinguishes client voice from Cooz's frame.

7. **Photo set A — Baseline four-angle grid** — 2×2 grid of the Week 1 photos. Small Syne caption below: `[WEEK 1 — BASELINE]`.

8. **Section 2 — "What made you actually pull the trigger on this?"** — H2 header. 200-300 words. Client's answer on the trigger event.

9. **Full-width interstitial photo** — Photo Type 2 (Cooz working with the client, or the client mid-lift).

10. **Section 3 — "What was the hardest part of the 12 weeks?"** — H2 header. 300-400 words. This is where the honesty lives. What didn't work, what hurt, what they wanted to quit.

11. **Pull quote mid-page** — Second strongest sentence, same treatment as the lead pull quote.

12. **Section 4 — "What changed in your body that you can point to specifically?"** — H2 header. 300-400 words. Hard specifics — the lifts, the weight, the way their clothes fit.

13. **Photo set B — Week 12 four-angle grid** — 2×2 grid of the Week 12 photos alongside the baseline photos from Set A as before/after pairs.

14. **Section 5 — "What changed in your life outside the gym?"** — H2 header. 300-400 words. The relational, occupational, psychological downstream changes.

15. **Section 6 — "Who is this work for?"** — H2 header. 150-200 words. Client's answer on who they'd send this to. This is the organic referral mechanism baked into the page.

16. **Embedded video block** — 60-90 second intercut of the Week 1 selfie and the exit interview. Cathedral Black frame, play button in Ember Gold. None of UP's case studies have embedded video. This is the moat from Ignition Plan Section 4.

17. **Cooz's closing frame** — 100-150 words in Cooz's I-led voice. What he learned from coaching this client. Named in a small Syne kicker above: `[COOZ'S NOTES]`. This is the only place Cooz's voice shows up in the narrative; everywhere else the page belongs to the client.

18. **Single CTA block** — Dawn Linen background, centered. Fraunces 800 headline: `[If this is the work you need, the door opens the same way it did for Brian.]`. Syne kicker above: `[NEXT STEP]`. Ember Gold button: `[BOOK THE TRIAGE AUDIT →]`.

19. **More results grid** — 3 related case study cards at the bottom. Same card format as the Case Study Index page.

**URL slug convention** (mirroring UP): `/results/[firstname]-lost-[weight]-in-[duration]-to-[outcome-phrase]`. Example: `/results/brian-lost-31lbs-in-12-weeks-to-rebuild-his-squat`. This pulls the outcome into the SEO metadata and the narrative hook in one move.

---

## 6. Case Study Index Spec

The index lives at `/results`. Not `/case-studies` — `/results` is shorter, more direct, matches UP, and works as a bare noun in Cooz's voice.

**Page header**:
- Syne kicker: `[THE PROOF STACK]`
- Fraunces 900 headline: `[Every man named here agreed to be documented in full.]`
- Fraunces 400 italic subhead: `[No avatars. No cropped shots. No anonymous quotes.]`
- Below the subhead, a small honest-state disclosure (Ignition Phase only): `[As of [date], the published proof stack holds [N] cases. New cases ship as clients complete the 12 weeks.]`

**Week 1 empty-shelf state** (CRITICAL — what `/results` looks like with zero case studies):
- Do NOT publish `/results` until at least 1 case study exists. An empty results page is worse than no results page.
- Instead, during Weeks 1-4, the CTA everywhere points to the Triage Audit booking, not to `/results`.
- When Brian's case study publishes (target: Week 4), `/results` goes live with one card and the honest-state disclosure: "As of [date], the published proof stack holds 1 case. New cases ship as clients complete the 12 weeks."
- The page grows organically — 1 card in Week 4, 2-3 by Week 8, 4+ by Week 13. Premium brands never show empty shelves.

**Filter bar** (sticky at top of grid when scrolling on desktop):
- Three filters, matching UP's structure exactly:
  1. **Sex** — All / Male / Female
  2. **Age** — 30s / 40s / 50+
  3. **Duration** — 12 weeks / 6+ months (Ignition has only 12-week results at launch; filter future-proofs for when extended protocols exist)
- Plus one "Clear filters" link on the far right

**Card grid**:
- Desktop: 3 columns. Tablet: 2. Mobile: 1.
- Gap between cards: 32px desktop, 20px mobile.

**Each card contains** (top to bottom):
- Full-bleed photo at top (Photo Type 4, the Week 12 front shot, 4:5 aspect ratio)
- Cathedral Black caption bar below the photo, 24px padding:
  - Syne 700 kicker (10px, letter-spacing 0.1em, Stone Gray): `[MALE · 38 · 12 WEEKS]`
  - Fraunces 800 (22px, Dawn Linen): `[Brian lost 31 lbs and rebuilt his squat]`
  - Single headline metric line (Inter 400, 14px, Stone Gray): `[—31 LBS · +95 LB SQUAT · 12 WEEKS]`
  - Syne link at bottom (12px, Ember Gold, letter-spacing 0.08em): `[READ BRIAN'S STORY →]`
- Entire card is clickable; hover state: Cathedral Black frame darkens by 10%, photo subtly zooms 1.03x.

**Launch state note**: At Ignition Phase launch the grid will hold 1-2 cards (Brian + 1 female case). That is honest and acceptable — Sheedy and Dan Go publish effectively zero real case studies, so 2 published Cooz case studies at the UP narrative depth puts him ahead of both immediately. The page is built to scale to 20+ cards without redesign.

---

## 7. "Meet Cooz" Authority Page Spec

Per Ignition Plan Section 7, Cooz's advantage is that the team is just him. This converts the About page into the authority page. It is the single most important written page on the site — more important than the Ignition offer page, because it's what makes the offer believable.

**Sections in order**:

1. **Hero strip** — Full-width Photo Type 1 (the environmental portrait). Syne kicker overlay: `[MEET THE COACH]`. Fraunces 900 headline overlay: `[I was coached before I was anyone else's coach.]` No subhead — the headline carries it.

2. **The McBroom lineage block** — H2: `[The lineage]`. 200-300 words, Cooz's I-led voice, on being Cody McBroom's client before becoming a coach. Specific dates, specific protocols, specific moments. This is the authority transfer mechanism. A small photo right-aligned inside the text block: Cooz and McBroom if one exists, or Cooz during his own transformation if one doesn't.

3. **The lived transformation block** — H2: `[What I was]`. 300-400 words. Cooz's own pre-coach body, the trigger event, the 12 weeks with McBroom, what changed. First-person, specific, the same honesty standard the case study pages hold clients to. Paired with 1-2 Photo Type 5 detail shots.

4. **The philosophy block** — H2: `[The protocol is the philosophy]`. 300-400 words on the body-first thesis. Why hardware before software. Why infrastructure before purpose. Pulls language from the voice guide ("fix the hardware, then the software runs"). This section is the only place on the site where Cooz argues his worldview directly.

5. **The 8 Tenets framework preview** — H2: `[The eight things I teach]`. Not the full framework (that's inside the offer), just the eight names and one-line definitions each. This is teaser content that signals depth without giving the whole curriculum away. Set as a numbered list, Fraunces 700 numbers in Ember Gold, Fraunces 400 body.

6. **What I don't do** — H2: `[What this isn't]`. 150-200 words listing what Cooz does NOT do (therapy, life coaching, business strategy, medical work, labs). This exclusion list is a seriousness signal — it says the work is contained and definable.

7. **Full-width photo break** — Photo Type 3 (empty gym at dawn) with a pull quote overlaid: `[You're not broken. You're dormant. There's a difference.]` Fraunces 300 italic 32px, centered, Dawn Linen.

8. **The Triage Audit invitation** — H2: `[How to find out if this is for you]`. 100 words explaining what the Triage Audit is, how long it takes, what happens in it, who it's for. Single CTA button below: `[BOOK THE TRIAGE AUDIT →]`.

9. **Footer contact block** — Small "Based in Burbank, CA. Coaching online." line with three social links (Instagram, YouTube, LinkedIn). No phone number, no email — the Triage Audit booking page is the only contact mechanism during Ignition.

---

## 8. Ignition Offer Page Spec

From Ignition Plan Section 3, the 11-section offer architecture, translated into layout. Page lives at `/the-ignition`.

**Sections in order** (numbered to match Section 3 of the Ignition Plan):

1. **Hero: I-led declaration** — Full-viewport hero. Photo Type 1 or Photo Type 2 in the background with a Dawn Wash gradient. Fraunces 900 headline, 72px desktop, max 12 words. Example placeholder: `[Twelve weeks. One coach. Your body as the proof.]`. Syne kicker above: `[THE IGNITION]`.

2. **Sub: The McBroom lineage line** — Immediately under the hero, Dawn Linen band, Fraunces 400 italic centered: `[I was Cody McBroom's client before I built this.]` Stone Gray meta line below: `[Body-first coaching for men whose bodies stopped letting them do their work.]`

3. **The promise** — H2: `[The promise]`. One paragraph, 80-120 words, Cooz's voice. No bullet points here — this is the prose section, the emotional frame.

4. **Who this is for** — H2: `[Who this is for]`. Five bullet points, psychological not demographic. Each bullet set in Fraunces 700 22px with a small Ember Gold square bullet marker. Example placeholder bullets structured as: `[You're [psychological state], and [specific lived condition].]`

5. **Who this is NOT for** — H2: `[Who this isn't for]`. Five bullet points, explicit disqualifiers. Same visual treatment as section 4 but with Blood Rust `#6B2B1D` square bullet markers to signal "exclusion, not inclusion."

6. **The 12-week structure (the 8 Tenets phases)** — H2: `[The twelve weeks]`. Three-phase visual block. Each phase is a horizontal card: Syne kicker (`[PHASE 1 — WEEKS 1-4]`), Fraunces 800 phase name (`[Stabilization]`), Fraunces 400 100-word phase description, bulleted list of the tenets covered. Three phases stacked vertically on desktop, tap-to-expand accordion on mobile.

7. **What you get** — H2: `[What's included]`. Two-column list on desktop (single column mobile) of the 8 delivery elements from Ignition Plan Section 3 (intake call, TrueCoach program, nutrition framework, weekly video calls, Voxer coaching, weekly check-in, mid-point strategy call, exit interview session). Each item: Syne 700 kicker label, Fraunces 400 one-line description.

8. **What you don't get** — H2: `[What's not included]`. Single column list of the 8 exclusions. Smaller type, Stone Gray, meant to be skimmed. The exclusion list is doing real work here — it's the seriousness signal.

9. **The risk reversal** — Full-width Blood Rust `#6B2B1D` band section. Fraunces 700 Dawn Linen headline: `[The risk reversal]`. 100-word explanation of the half-money-back guarantee at week 6. This is the only place Blood Rust appears on the offer page.

10. **Three price options** — H2: `[The price ladder]`. Three-column price card layout. Each card:
    - Syne kicker (`[FOUNDING]` / `[LIST]` / `[POST-PROOF]`)
    - Fraunces 900 price (`[$1,997]` / `[$2,997]` / `[$4,000]`)
    - Syne meta line (`[FIRST 3 CLIENTS]` / `[CLIENTS 4-5]` / `[CLIENT 6+]`)
    - One-paragraph explanation of who that rung is for
    - A visible availability counter on the Founding rung only: `[2 of 3 founding spots available]`
    - The Founding rung card is framed in Ember Gold; the other two are framed in Stone Gray.
    - This visible pricing is the differentiation move against Sheedy/Dan Go who gate everything. Do not gate. Do not hide behind "book a call to learn pricing."

11. **Single CTA** — Dawn Linen section, centered. Fraunces 800 headline: `[The front door is a 90-minute Triage Audit.]` Stone Gray one-line explainer on what the Triage Audit is. Single Ember Gold button: `[BOOK THE TRIAGE AUDIT →]`. No secondary CTA. No "download the PDF" alternative. One action.

**Footer note on this page**: Add a small italic Stone Gray paragraph at the bottom, 14px, 3-4 lines: the "proof is the discount" language — founding clients agree in writing to case study documentation, that's what the $1,997 rate is trading for. This is the most important piece of small print on the page.

---

## 9. Navigation Architecture

**Top navigation** (sticky, Cathedral Black background, Dawn Linen text):
- Logo / wordmark on the left: `THE RESURRECTION COACH` set in Fraunces 800 all-caps or, if a proper logotype exists, the logotype SVG. Clicks through to home.
- Nav items on the right, Inter 600 14px letter-spacing 0.02em:
  1. `Results` — goes to `/results` (the case study index)
  2. `Meet Cooz` — goes to `/about`
  3. `The Ignition` — goes to `/the-ignition`
  4. `Journal` — goes to `/journal` (the blog, where long-form posts live; optional for launch)
  5. `Podcast` — goes to `/podcast` or external (Resurrection Series)
- CTA button on the far right: `[BOOK TRIAGE AUDIT]` in Ember Gold, matching the hero button treatment but 44px tall instead of 56px.

**Nav rules**:
- Maximum 5 text nav items plus the CTA. No dropdown menus (UP uses them; they add complexity Squarespace handles poorly and the site is small enough to not need them).
- Sticky on scroll with a subtle 4px shadow to separate from content.
- On scroll past 80% of viewport, the nav bar's background opacity drops to 90% for a soft transparency effect.

**Mobile navigation**:
- Hamburger icon (Dawn Linen, 24px) on the right.
- Tap opens a full-screen Cathedral Black overlay with the same 5 items stacked vertically in Fraunces 800 36px, one per line, generous 32px vertical spacing. The Triage Audit CTA is at the bottom of the stack as a full-width Ember Gold button.
- Close button (X) top-right.

**Footer** (Cathedral Black background, Dawn Linen text, 80px vertical padding):
- Top row: wordmark on the left, Instagram / YouTube / LinkedIn icon row on the right
- Middle row: three columns — "The Site" (Results / Meet Cooz / The Ignition / Journal / Podcast), "The Work" (Triage Audit / 8 Tenets / Resurrection Series), "The Details" (Privacy / Terms / Contact)
- Bottom row: `© [year] The Resurrection Coach. Based in Burbank, CA.` in Inter 400 12px Stone Gray
- No newsletter signup form in the footer during Ignition Phase. The site is not a newsletter funnel yet — it's a Triage Audit funnel. One CTA discipline.

---

## 10. The Evolution Path

The site launches in Ignition Phase configuration: open visibility, published pricing, published case studies, single Triage Audit CTA. It evolves toward Scale Phase configuration: application-gated, pricing hidden, case studies as social proof for the gate rather than the primary funnel.

**When to flip the switch** — the trigger conditions for moving from Ignition to Scale configuration:
1. Six or more published case studies in the proof stack
2. First month of $15K+ MRR from online-only clients (not hybrid, not local)
3. Inbound Triage Audit bookings exceed Cooz's delivery capacity for 2 consecutive months
4. At least one of the three price rungs has been walked through completely (i.e. Cooz has closed clients at $4,000 post-proof rate without any founding-rate language)

All four conditions must be met. The evolution is one-way — once gated, reversing back to open is a credibility hit.

**What changes when the switch flips**:
- The Ignition offer page (`/the-ignition`) gets archived or redirected. In its place: an `/apply` page gated behind a Typeform or Squarespace form. Pricing disappears from public view.
- The home hero CTA changes from `[BOOK TRIAGE AUDIT]` to `[APPLY TO WORK WITH ME]`.
- The nav item `The Ignition` becomes `Apply` or disappears entirely (application link only reachable from the case study pages and the home CTA).
- Case study pages stay exactly as they are — they become the primary social proof for the gate, exactly as UP uses them.
- The Meet Cooz page gains a new section at the top: `[Current availability: accepting [N] clients this quarter.]` This is the Priestley oversubscribed signal.
- The footer stays the same; the Triage Audit language transitions to "Discovery call" or "Strategy call" language.

**What does NOT change**:
- The visual system (colors, typography, photo direction, layout patterns) stays identical. The brand doesn't rebrand when it gates — it just changes the transaction mechanism.
- The case study format and depth stays identical. These are the moat; they don't get thinner when the funnel tightens.
- The Meet Cooz page stays mostly intact. Only the availability line is added.

**Timeline estimate**: The switch flips approximately 6-12 months into the Scale Phase, which itself begins after the first 3 founding clients complete and at least 2 published case studies exist. Realistic earliest flip date: Q4 2026. More likely: Q1-Q2 2027.

---

# PART B — ASCII WIREFRAMES

Monospace approximate layout for the 5 critical pages. Mobile stacking order noted below each wireframe.

## Wireframe 1 — HOME

```
+=============================================================================+
| [LOGO] THE RESURRECTION COACH    Results  Meet Cooz  The Ignition  Journal  |
|                                              Podcast    [BOOK TRIAGE AUDIT] |
+=============================================================================+
|                                                                             |
|                          |                                                  |
|   [THE RESURRECTION]     |                                                  |
|                          |          [  FULL-BLEED                   ]       |
|   I was coached.         |          [  HERO PHOTO                   ]       |
|   Now I coach the men    |          [  Cooz mid-work,              ]       |
|   who were where I was.  |          [  golden-hour side light,     ]       |
|                          |          [  shallow depth of field,     ]       |
|   Twelve weeks. One-on-  |          [  dark gradient from left     ]       |
|   one. Body-first.       |                                                  |
|                          |                                                  |
|   [BOOK THE TRIAGE       |                                                  |
|    AUDIT →]              |                                                  |
|                          |                                                  |
+=============================================================================+
|                                                                             |
|                    [ PHOTO TYPE 3 — EMPTY GYM AT DAWN ]                     |
|                                                                             |
|   [THE WORK]                                                                |
|   I don't rebuild mindsets. I rebuild the hardware                          |
|   the mindset runs on. [One short paragraph, 60 words,                      |
|   prose in Fraunces 400 18px, max-width 680px]                              |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [THE PROOF STACK]                                                         |
|   Every man named here agreed to be documented in full.                     |
|                                                                             |
|   +--------------+    +--------------+    +--------------+                  |
|   | [PHOTO]      |    | [PHOTO]      |    | [PHOTO]      |                  |
|   | Brian / 12wk |    | [Case 02]    |    | [Case 03]    |                  |
|   | -31 lbs      |    | [metrics]    |    | [metrics]    |                  |
|   | READ →       |    | READ →       |    | READ →       |                  |
|   +--------------+    +--------------+    +--------------+                  |
|                                                                             |
|                         [ SEE ALL RESULTS → ]                               |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [THE COACH]                                                               |
|   +----------+                                                              |
|   | [PORTRAIT|    I was Cody McBroom's client                               |
|   |  PHOTO]  |    before I built this. The lineage                          |
|   |          |    is real. The story is real.                               |
|   +----------+    The protocol came from the work.                          |
|                                                                             |
|                         [ MEET COOZ → ]                                     |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [ FULL-WIDTH BLOOD RUST BAND ]                                            |
|   The front door is a 90-minute Triage Audit.                               |
|   [ BOOK THE TRIAGE AUDIT → ]                                               |
|                                                                             |
+=============================================================================+
| FOOTER — Cathedral Black                                                    |
| [LOGO]                                             IG  YT  LI               |
| The Site       The Work         The Details                                 |
| Results        Triage Audit     Privacy                                     |
| Meet Cooz      8 Tenets         Terms                                       |
| ...            ...              ...                                         |
| (c) 2026 The Resurrection Coach. Based in Burbank, CA.                      |
+=============================================================================+
```

**Mobile stack order** (Home): Hero (photo backdrops headline) → The Work prose → Proof Stack cards (1 col) → Meet Cooz block → Triage Audit band → Footer

---

## Wireframe 2 — CASE STUDY INDEX (`/results`)

```
+=============================================================================+
| [LOGO]  Results  Meet Cooz  The Ignition  Journal  Podcast  [TRIAGE AUDIT]  |
+=============================================================================+
|                                                                             |
|   [THE PROOF STACK]                                                         |
|   Every man named here agreed to                                            |
|   be documented in full.                                                    |
|                                                                             |
|   No avatars. No cropped shots. No anonymous quotes.                        |
|                                                                             |
|   As of [date], the published proof stack holds [N] cases.                  |
|                                                                             |
+=============================================================================+
|                                                                             |
|   SEX:  [ ALL ] [ MALE ] [ FEMALE ]                                         |
|   AGE:  [ 30s ] [ 40s ] [ 50+ ]                                             |
|   DUR:  [ 12 WEEKS ] [ 6+ MONTHS ]             [ Clear filters ]            |
|                                                                             |
+=============================================================================+
|                                                                             |
|   +---------------+   +---------------+   +---------------+                 |
|   |               |   |               |   |               |                 |
|   |   [PHOTO]     |   |   [PHOTO]     |   |   [PHOTO]     |                 |
|   |   4:5 ratio   |   |   4:5 ratio   |   |   4:5 ratio   |                 |
|   |               |   |               |   |               |                 |
|   +---------------+   +---------------+   +---------------+                 |
|   | MALE·38·12WK  |   | [META]        |   | [META]        |                 |
|   | Brian lost    |   | [Headline     |   | [Headline     |                 |
|   | 31 lbs and    |   |  line]        |   |  line]        |                 |
|   | rebuilt his   |   |               |   |               |                 |
|   | squat         |   |               |   |               |                 |
|   | -31LB·+95SQT  |   | [metrics]     |   | [metrics]     |                 |
|   | READ STORY →  |   | READ STORY →  |   | READ STORY →  |                 |
|   +---------------+   +---------------+   +---------------+                 |
|                                                                             |
|   +---------------+   +---------------+   +---------------+                 |
|   |   [ CARD ]    |   |   [ CARD ]    |   |   [ CARD ]    |                 |
|   |      ...      |   |      ...      |   |      ...      |                 |
|   +---------------+   +---------------+   +---------------+                 |
|                                                                             |
|                         [ LOAD MORE ]                                       |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [Single CTA strip: "Want to be here? Book the Triage Audit →"]            |
|                                                                             |
+=============================================================================+
| FOOTER                                                                      |
+=============================================================================+
```

**Mobile stack order** (Index): Nav hamburger → Page header → Filter bar (horizontal scroll) → Cards (1 col) → Load More → CTA strip → Footer

---

## Wireframe 3 — SINGLE CASE STUDY (Brian placeholder)

```
+=============================================================================+
| [LOGO]  Results  Meet Cooz  The Ignition  Journal  Podcast  [TRIAGE AUDIT]  |
+=============================================================================+
|                                                                             |
|         [ FULL-BLEED HERO PHOTO — Photo Type 4 composite ]                  |
|         [ Cathedral Black gradient from bottom 40% ]                        |
|                                                                             |
|   [CASE STUDY Nº 01]                                                        |
|   Brian lost 31 lbs and rebuilt his squat in 12 weeks.                      |
|   A 38-year-old small business owner who stopped recognizing himself        |
|   in photos.                                                                |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WEIGHT       |   BODY FAT    |   SQUAT       |   DURATION                 |
|   -31 LBS      |   -7%         |   +95 LBS     |   12 WEEKS                 |
|   (241→210)    |   (28→21)     |   (225→320)   |                            |
|                                                                             |
|   Age 38 · Small business owner · Burbank, CA                               |
|                                                                             |
+=============================================================================+
|                                                                             |
|                 " [The single strongest sentence from                       |
|                    the exit interview, 18 words, set                        |
|                    in Fraunces 300 italic 36px] "                           |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [Opening narrative block — Cooz's I-led voice, 200 words,                 |
|    max-width 680px, Fraunces 400 18px]                                      |
|                                                                             |
+=============================================================================+
|            [ FULL-WIDTH INTERSTITIAL PHOTO — Photo Type 2 ]                 |
+=============================================================================+
|                                                                             |
|   WHAT WAS HAPPENING IN YOUR BODY BEFORE WE STARTED?                        |
|                                                                             |
|   [ 250 words of Brian's answer, pulled from exit interview,                |
|     set as blockquote with Ember Gold left border bar ]                     |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [WEEK 1 — BASELINE]                                                       |
|   +--------+  +--------+    +--------+  +--------+                          |
|   | FRONT  |  | BACK   |    | LEFT   |  | RIGHT  |                          |
|   +--------+  +--------+    +--------+  +--------+                          |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WHAT MADE YOU ACTUALLY PULL THE TRIGGER ON THIS?                          |
|   [ 300 words of client's trigger-event answer ]                            |
|                                                                             |
+=============================================================================+
|            [ FULL-WIDTH INTERSTITIAL PHOTO — Photo Type 2 ]                 |
+=============================================================================+
|                                                                             |
|   WHAT WAS THE HARDEST PART OF THE 12 WEEKS?                                |
|   [ 400 words — the honesty section ]                                       |
|                                                                             |
|                 " [Mid-page pull quote, same treatment                      |
|                    as the lead pull quote] "                                |
|                                                                             |
|   WHAT CHANGED IN YOUR BODY SPECIFICALLY?                                   |
|   [ 400 words — the hard specifics ]                                        |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [WEEK 12 — EXIT vs. WEEK 1 — BASELINE SIDE BY SIDE]                       |
|   +--------+  +--------+    +--------+  +--------+                          |
|   | BEFORE |  | AFTER  |    | BEFORE |  | AFTER  |                          |
|   +--------+  +--------+    +--------+  +--------+                          |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WHAT CHANGED IN YOUR LIFE OUTSIDE THE GYM?                                |
|   [ 400 words ]                                                             |
|                                                                             |
|   WHO IS THIS WORK FOR?                                                     |
|   [ 200 words — client's referral answer ]                                  |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [ EMBEDDED VIDEO BLOCK — 90-second intercut, Ember Gold play button ]     |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [COOZ'S NOTES]                                                            |
|   [ 150 words in Cooz's I-led voice — what he learned from                  |
|     coaching Brian. The only Cooz-voice block in the whole page. ]          |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [Dawn Linen CTA block]                                                    |
|   If this is the work you need, the door opens the                          |
|   same way it did for Brian.                                                |
|                                                                             |
|                   [ BOOK THE TRIAGE AUDIT → ]                               |
|                                                                             |
+=============================================================================+
|                                                                             |
|   MORE RESULTS                                                              |
|   +--------+   +--------+   +--------+                                      |
|   | CARD   |   | CARD   |   | CARD   |                                      |
|   +--------+   +--------+   +--------+                                      |
|                                                                             |
+=============================================================================+
| FOOTER                                                                      |
+=============================================================================+
```

**Mobile stack order** (Case Study): Hero (photo + headline overlay) → Metrics bar (2×2 grid) → Lead pull quote → Opening narrative → Interstitial photo → Each Q&A section stacked → Baseline photo grid (2×2) → Midpage pull quote → Before/after grid → Closing sections → Video → Cooz's Notes → CTA → More Results (horizontal scroll carousel) → Footer

---

## Wireframe 4 — MEET COOZ

```
+=============================================================================+
| [LOGO]  Results  Meet Cooz  The Ignition  Journal  Podcast  [TRIAGE AUDIT]  |
+=============================================================================+
|                                                                             |
|         [ FULL-BLEED HERO — Photo Type 1 environmental portrait ]           |
|         [ Dawn Wash gradient from left ]                                    |
|                                                                             |
|   [MEET THE COACH]                                                          |
|   I was coached before                                                      |
|   I was anyone else's coach.                                                |
|                                                                             |
+=============================================================================+
|                                                                             |
|   THE LINEAGE                                                               |
|                                                                             |
|   [ 300 words on the McBroom coaching ]          +------------+             |
|   [ relationship, Cooz's I-led voice,  ]         | [PHOTO of  |             |
|   [ specific dates, specific protocols ]         |  Cooz and  |             |
|                                                  |  McBroom OR|             |
|                                                  |  Cooz mid- |             |
|                                                  |  transform]|             |
|                                                  +------------+             |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WHAT I WAS                                                                |
|   [ 400 words on Cooz's pre-coach body, trigger event,                      |
|     12 weeks with McBroom, what changed. First person. ]                    |
|                                                                             |
|   +--------+           +--------+                                           |
|   | DETAIL |           | DETAIL |                                           |
|   | PHOTO  |           | PHOTO  |                                           |
|   +--------+           +--------+                                           |
|                                                                             |
+=============================================================================+
|                                                                             |
|   THE PROTOCOL IS THE PHILOSOPHY                                            |
|   [ 400 words. Body-first thesis. Hardware before software.                 |
|     Infrastructure before purpose. ]                                        |
|                                                                             |
+=============================================================================+
|                                                                             |
|   THE EIGHT THINGS I TEACH                                                  |
|                                                                             |
|   01  [Tenet 1 name]        [one-line definition]                           |
|   02  [Tenet 2 name]        [one-line definition]                           |
|   03  [Tenet 3 name]        [one-line definition]                           |
|   04  [Tenet 4 name]        [one-line definition]                           |
|   05  [Tenet 5 name]        [one-line definition]                           |
|   06  [Tenet 6 name]        [one-line definition]                           |
|   07  [Tenet 7 name]        [one-line definition]                           |
|   08  [Tenet 8 name]        [one-line definition]                           |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WHAT THIS ISN'T                                                           |
|   • [Exclusion 1]                                                           |
|   • [Exclusion 2]                                                           |
|   • [Exclusion 3]                                                           |
|   • [Exclusion 4]                                                           |
|   • [Exclusion 5]                                                           |
|                                                                             |
+=============================================================================+
|                                                                             |
|    [ FULL-WIDTH PHOTO — empty gym at dawn, Photo Type 3 ]                   |
|                                                                             |
|         " You're not broken. You're dormant.                                |
|           There's a difference. "                                           |
|                                                                             |
+=============================================================================+
|                                                                             |
|   HOW TO FIND OUT IF THIS IS FOR YOU                                        |
|   [ 100 words on the Triage Audit ]                                         |
|                                                                             |
|                   [ BOOK THE TRIAGE AUDIT → ]                               |
|                                                                             |
|   Based in Burbank, CA. Coaching online.                                    |
|   IG · YT · LI                                                              |
|                                                                             |
+=============================================================================+
| FOOTER                                                                      |
+=============================================================================+
```

**Mobile stack order** (Meet Cooz): Hero → Lineage (photo stacks below text) → What I Was → Detail photos (1 col) → Philosophy → 8 Tenets list → What This Isn't → Full-width photo with pull quote overlay → Triage Audit invite → Footer

---

## Wireframe 5 — THE IGNITION (`/the-ignition`)

```
+=============================================================================+
| [LOGO]  Results  Meet Cooz  The Ignition  Journal  Podcast  [TRIAGE AUDIT]  |
+=============================================================================+
|                                                                             |
|         [ FULL-VIEWPORT HERO — Photo Type 1 or 2, Dawn Wash ]               |
|                                                                             |
|   [THE IGNITION]                                                            |
|   Twelve weeks. One coach.                                                  |
|   Your body as the proof.                                                   |
|                                                                             |
+=============================================================================+
|                                                                             |
|   I was Cody McBroom's client before I built this.                          |
|   Body-first coaching for men whose bodies stopped                          |
|   letting them do their work.                                               |
|                                                                             |
+=============================================================================+
|                                                                             |
|   THE PROMISE                                                               |
|   [ 100 words prose, Cooz's voice ]                                         |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WHO THIS IS FOR            |   WHO THIS ISN'T FOR                         |
|   ■ [Psychological bullet 1] |   ■ [Disqualifier 1]                         |
|   ■ [Psychological bullet 2] |   ■ [Disqualifier 2]                         |
|   ■ [Psychological bullet 3] |   ■ [Disqualifier 3]                         |
|   ■ [Psychological bullet 4] |   ■ [Disqualifier 4]                         |
|   ■ [Psychological bullet 5] |   ■ [Disqualifier 5]                         |
|   (Ember Gold markers)       |   (Blood Rust markers)                       |
|                                                                             |
+=============================================================================+
|                                                                             |
|   THE TWELVE WEEKS                                                          |
|                                                                             |
|   +----------------------------------------------------------------+        |
|   | PHASE 1 — WEEKS 1-4                                            |        |
|   | STABILIZATION                                                  |        |
|   | [100 words describing Phase 1 from the 8 Tenets framework]     |        |
|   | • [Tenet]  • [Tenet]  • [Tenet]                                |        |
|   +----------------------------------------------------------------+        |
|                                                                             |
|   +----------------------------------------------------------------+        |
|   | PHASE 2 — WEEKS 5-8                                            |        |
|   | INSTALLATION                                                   |        |
|   | [100 words]                                                    |        |
|   | • [Tenet]  • [Tenet]  • [Tenet]                                |        |
|   +----------------------------------------------------------------+        |
|                                                                             |
|   +----------------------------------------------------------------+        |
|   | PHASE 3 — WEEKS 9-13                                           |        |
|   | INTEGRATION                                                    |        |
|   | [100 words]                                                    |        |
|   | • [Tenet]  • [Tenet]  • [Tenet]                                |        |
|   +----------------------------------------------------------------+        |
|                                                                             |
+=============================================================================+
|                                                                             |
|   WHAT'S INCLUDED                     WHAT'S NOT INCLUDED                   |
|   • Intake call (60 min)              • 24/7 messaging access               |
|   • TrueCoach program                 • Lifetime program access             |
|   • Flexible nutrition framework      • Labs / biomarkers / hormones        |
|   • Weekly 1:1 video (13 total)       • Therapy / life coaching             |
|   • Daily Voxer (9a-6p PT weekdays)   • In-person sessions                  |
|   • Weekly check-in form              • Community / Discord                 |
|   • Week 6 strategy call (90 min)     • Travel / retreats                   |
|   • Week 12 exit interview session    • Partner integration calls           |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [ BLOOD RUST BAND — the only place Blood Rust appears ]                   |
|                                                                             |
|   THE RISK REVERSAL                                                         |
|   [ 100 words — half-money-back guarantee at week 6 ]                       |
|                                                                             |
+=============================================================================+
|                                                                             |
|   THE PRICE LADDER                                                          |
|                                                                             |
|   +==============+   +--------------+   +--------------+                    |
|   | [FOUNDING]   |   | [LIST]       |   | [POST-PROOF] |                    |
|   |              |   |              |   |              |                    |
|   |   $1,997     |   |   $2,997     |   |   $4,000     |                    |
|   |              |   |              |   |              |                    |
|   | FIRST 3      |   | CLIENTS 4-5  |   | CLIENT 6+    |                    |
|   | CLIENTS      |   |              |   |              |                    |
|   |              |   |              |   |              |                    |
|   | [Paragraph   |   | [Paragraph]  |   | [Paragraph]  |                    |
|   |  explaining] |   |              |   |              |                    |
|   |              |   |              |   |              |                    |
|   | 2 of 3 spots |   |              |   |              |                    |
|   | available    |   |              |   |              |                    |
|   +==============+   +--------------+   +--------------+                    |
|   (Ember Gold frame)   (Stone Gray)      (Stone Gray)                       |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [Dawn Linen CTA block]                                                    |
|                                                                             |
|   The front door is a 90-minute Triage Audit.                               |
|   [ one-line explainer on what the Triage Audit is ]                        |
|                                                                             |
|                   [ BOOK THE TRIAGE AUDIT → ]                               |
|                                                                             |
+=============================================================================+
|                                                                             |
|   [Small italic Stone Gray text, 3-4 lines]                                 |
|   Founding clients agree, in writing, to participate in case                |
|   study documentation. The proof is the discount.                           |
|                                                                             |
+=============================================================================+
| FOOTER                                                                      |
+=============================================================================+
```

**Mobile stack order** (Ignition): Hero → Lineage line → Promise → Who For → Who Not For → 3 Phases (accordion-collapsed) → Included (1 col) → Not Included (1 col) → Risk Reversal band → Price cards (1 col, Founding first) → CTA block → Small print → Footer

---

# PART C — SQUARESPACE IMPLEMENTATION NOTES

Squarespace is a constraint, not a choice. Cooz already lives there and migrating to Webflow during Ignition is a distraction from proof manufacturing. The design has to work inside Squarespace's limits.

**Template family recommendation**: **Brine family** (specifically Rally, Foster, or Miller). Brine is the most flexible template family Squarespace ships — it supports custom font uploads via CSS, index pages that can be repurposed as case study landing pages, multi-column stacked sections, and it handles typography override better than the newer Squarespace 7.1 templates. The newer 7.1 Fluid Engine is more WYSIWYG but strips more custom CSS control; for a typography-first design, 7.0 Brine gives more headroom. If Cooz is already on 7.1, stay there — migration is not worth it, and the design below works on 7.1 with Section-based layout and Custom CSS injection.

**Known Squarespace limitations the design works around**:
1. **No true filtered grids out of the box.** The filterable case study index on `/results` has to be built as a Squarespace Summary Block (Grid variant) with category tags, combined with a custom JavaScript filter snippet. Summary Blocks natively accept category filters via URL parameters — the filter buttons at the top of the page can be simple link buttons that append `?category=male` etc. to the URL. This is the cleanest path. Alternatively, each case study is tagged in the blog post editor (Male / Female, 30s / 40s / 50+, 12-weeks / 6-months) and the Summary Block auto-filters. Do NOT try to build a real JavaScript-reactive filter — too brittle on Squarespace.
2. **No native before/after image sliders.** Use a side-by-side image grid (Gallery Block, Grid variant, 2 columns) instead. Static comparison reads more honest than a slider anyway.
3. **Typography overrides are CSS-only.** Squarespace's style editor doesn't expose Fraunces/Inter/Syne as native fonts — you add them via Custom CSS Injection using Google Fonts `@import`. This is standard, well-documented.
4. **Sticky navigation opacity on scroll requires custom CSS.** Doable with a few lines of `position: sticky` and `backdrop-filter: blur(8px)`.
5. **Accordion sections on mobile need the Squarespace Accordion Block** (ships natively in 7.1) or an Index Page with Stack sections that collapse via CSS on mobile. Keep the 3-phase visual block on The Ignition page simple — if accordion is fighting the design, three stacked full-width bands works fine.

**Custom CSS snippets needed** (paste into Design → Custom CSS):

```css
/* --- Typography: Google Fonts import --- */
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,700;0,9..144,800;0,9..144,900;1,9..144,300;1,9..144,400&family=Inter:wght@400;600&family=Syne:wght@700&display=swap');

/* --- Brand color variables --- */
:root {
  --cathedral-black: #0E0E0C;
  --dawn-linen: #F3EEE3;
  --soil-brown: #3A2A1F;
  --stone-gray: #5B5B55;
  --ember-gold: #C08A3E;
  --blood-rust: #6B2B1D;
}

/* --- Headlines: Fraunces --- */
h1, h2, h3, .sqs-block-html h1, .sqs-block-html h2 {
  font-family: 'Fraunces', Georgia, serif !important;
  letter-spacing: -0.015em;
}
h1 { font-weight: 900; line-height: 1.05; }
h2 { font-weight: 700; line-height: 1.15; }

/* --- Body: Fraunces 400 preferred, Inter fallback --- */
body, p, .sqs-block-html p {
  font-family: 'Fraunces', Georgia, serif;
  font-weight: 400;
  font-size: 18px;
  line-height: 1.6;
  color: var(--cathedral-black);
}

/* --- Nav and buttons: Inter --- */
nav, .sqs-block-button-element {
  font-family: 'Inter', -apple-system, sans-serif;
  font-weight: 600;
  letter-spacing: 0.02em;
}

/* --- Kickers / all-caps labels: Syne --- */
.kicker, .meta-label {
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 12px;
}

/* --- Primary CTA button: Ember Gold --- */
.sqs-block-button-element--primary {
  background-color: var(--ember-gold) !important;
  color: var(--cathedral-black) !important;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  border-radius: 2px;
  padding: 16px 32px;
}

/* --- Site background: Dawn Linen default --- */
#siteWrapper {
  background-color: var(--dawn-linen);
}

/* --- Sticky nav with backdrop blur --- */
.header-announcement-bar-wrapper {
  position: sticky;
  top: 0;
  backdrop-filter: blur(8px);
  background-color: rgba(14, 14, 12, 0.92);
}
```

**How to implement the case study page template on Squarespace**:
- Build it as a **Squarespace Blog Post** using the `Results` blog. Each case study = one blog post. Category tags: Sex (Male/Female), Age bucket, Duration. The magazine-style layout is built inside the blog post body using alternating Text blocks, Image blocks (full-bleed setting), Gallery blocks (for the 4-angle grid), and Quote blocks (for pull quotes). The Summary Block on `/results` pulls from this blog and auto-populates the card grid.
- Alternative: build each case study as a **Custom Page** with section-based layout. More visual control but harder to scale to 20+ case studies and no native filter/tagging support. Recommendation: blog posts, not custom pages.

**How to build the filterable grid on Squarespace**:
1. Create a new Blog called `Results` (or `Case Studies`).
2. In each post's settings, apply categories: `Male` or `Female` · age bucket · duration.
3. On `/results` page, place a **Summary Block → Grid variant**, configured to pull from the Results blog, display 12 items, show thumbnail + title + excerpt + primary metadata.
4. Above the Summary Block, place **Button Blocks** styled as filter chips. Each button URL is the page URL with a category query parameter: `/results?category=male`, `/results?category=30s`, etc. Squarespace Summary Blocks respect the `?category=` URL param and auto-filter. This is the native, brittle-free approach.
5. For the "Clear Filters" button, link to bare `/results` (no params).

**SEO slug recommendations** (mirror UP's pattern):
- Format: `/results/[firstname]-lost-[weight]-in-[duration]-to-[outcome-phrase]`
- Example: `/results/brian-lost-31lbs-in-12-weeks-to-rebuild-his-squat`
- Set the slug manually in Squarespace's post settings → URL slug. Don't let it auto-generate from the post title.
- Meta title: `[First name] · [Age] · [Headline metric] — The Resurrection Coach`
- Meta description: 155 chars max, Cooz's voice, leading with the trigger event. Example: `Brian was 38, running a small business, and couldn't squat his own bodyweight. 12 weeks later he'd lost 31 lbs and added 95 lbs to his squat.`
- Open Graph image: The case study hero photo (Photo Type 4 front composite), 1200×630 px.

**One Squarespace gotcha to watch**: the Fraunces font is large (variable weight, optical size). Loading the full variable axis can slow mobile page loads. The `@import` above subsets to only the weights the site uses (300, 400, 700, 800, 900 plus italic 300/400). Do not add more weights to the import without reason.

**Launch checklist before going live**:
- [ ] All photos shot and processed through the brand Lightroom preset
- [ ] Fraunces/Inter/Syne loading correctly on all 5 page templates (test Safari iOS, Chrome desktop, Firefox)
- [ ] Color contrast verified on hero headline + CTA button pairs
- [ ] The Ignition price card Founding rung shows `2 of 3 founding spots available` (manually updated — no dynamic counter)
- [ ] At least 1 published case study live at `/results`
- [ ] Meet Cooz page complete with all 9 sections
- [ ] Triage Audit booking link works on every CTA button site-wide (single source of truth)
- [ ] Mobile nav hamburger tested on real iPhone, not just the Squarespace preview
- [ ] Open Graph images set for all 5 pages
- [ ] Case study URL slugs match the outcome-phrase convention
- [ ] No emoji anywhere on the site (site-wide Cmd+F sanity check)
