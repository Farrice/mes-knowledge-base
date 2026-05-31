# Canva Pro — Action Steps (Cold-to-Ship in 90 Minutes)

*Part of the Pre-Launch Command Center (see `00-command-center.md`).*
*Companion to `06-tools-stack-setup.md`. The deep system reference is at `brand-operating-system/04-ai-handoff/04-canva-component-spec.md` — this file is the action playbook that points to it.*

*Last updated: 2026-05-19.*

---

## TL;DR — 5 Stages, 90 Minutes Total, Day-1-Post Ready

| Stage | What you do | Time |
|---|---|---|
| **1** | Deploy Brand Kit (fonts, colors, logo) | 30 min |
| **2** | Train Brand Voice (paste voice doc patterns) | 10 min |
| **3** | Create folder structure (by Content Pillar) | 10 min |
| **4** | Star 12 base templates (the daily workhorses) | 15 min |
| **5** | Build Day 1 graphic + Magic Resize for Stories | 20 min |

**Pre-requisite**: logged into Canva Pro. Confirm the workspace shows "Canva Pro" in the top-left chip. If not, settings → upgrade.

---

## Stage 1 — Deploy Brand Kit (30 min)

**Open the full spec**: `brand-operating-system/04-ai-handoff/04-canva-component-spec.md`. That file has the exact font weights, color hex codes in order, logo placement rules, and substitute fonts if GT Sectra is unlicensed.

**The 5 sub-steps (each ~5 min):**

1. **Upload fonts** → Brand Hub → Brand Kit → Fonts → Upload Font. Upload GT Sectra Book + Medium (or Mortise / IBM Plex Serif as substitute), Inter Regular + SemiBold (free, Google Fonts), Caveat Regular (free, Google Fonts). Tag each with its role: "GT Sectra — Display", "Inter — Body", "Caveat — Signature only".

2. **Add the 10 brand colors** → Brand Hub → Brand Kit → Colors → Add Color. Add in this order so they display in this order in the picker: Cream 100 `#F5EFE3`, Cream 50 `#FBF7F0`, Midnight 900 `#0F1A2E`, Ink 900 `#1A1814`, Ink 700 `#3A332B`, Terracotta 600 `#B8492E`, Terracotta 700 `#9A3A22`, Slate 500 `#7A6F62`, Gold 600 `#8C6526`, Border Hairline `#E1D6C2`.

3. **Upload logos** → Brand Hub → Brand Kit → Logos → Upload. If no final logo yet, upload a typography-only wordmark created from GT Sectra Medium in Midnight 900 on Cream 50. (Canva can render this — File → New design → 1000x1000 → type "Resonance" in GT Sectra Medium, color it Midnight 900, background Cream 50, export PNG, upload as logo placeholder.)

4. **Set the default font pairing** → Brand Hub → Brand Kit → Default text styles. Heading: GT Sectra Medium 56pt Midnight 900. Subheading: Inter SemiBold 24pt Midnight 900. Body: Inter Regular 18pt Ink 700. Caption: Inter Regular 13pt Slate 500.

5. **Lock photo treatment defaults** → Brand Hub → Photo Filters → save a custom filter "Resonance Daytime" with: warmth +8, shadows +12, highlights -10, vibrance -5 (subtle warm cast, never saturated). Apply to any iPhone candid before posting.

**Verification**: Open File → New design → 1080x1080. Hit "T" to add text. Type "Test." It should default to GT Sectra Medium 56pt Midnight 900 on the Cream 50 background. If yes, Brand Kit is live.

---

## Stage 2 — Train Brand Voice (10 min)

Canva Pro's **Brand Voice** is the AI feature that makes Magic Write match your voice. Untrained, it writes generic. Trained on Resonance's voice doc, it writes captions and copy that sound like Andrea.

**Steps:**

1. **Brand Hub → Brand Voice → Get started.**
2. **Paste 8-10 voice patterns** from `brand-operating-system/00-foundation/03-voice-document.md` Section 4 (Voice Examples). Specifically paste the GOOD examples — Canva learns FROM what you give it, not what you tell it to avoid.

Recommended 8 paste-in patterns (copy these verbatim into Brand Voice):

```
Heart encounters, not head encounters. Daytime. Sober. Curated. Chicago.

A daytime room for people serious about meeting a partner. We're not a brunch with a DJ. We're not a wellness mixer with branded kombucha. We're not your friend's birthday party with extra steps.

The room is small on purpose. Hell-yes only. The address goes out the morning of.

I'm Andrea — Costa Rican, Chicago-based, a DJ who grew up inside the kind of curated music rooms that change you.

The music does the introducing.

The room I came to Chicago looking for.

If sponsorship requires drift, the sponsorship is wrong.

Couples. Not followers.
```

3. **Add 5 phrases to AVOID** → Brand Voice → Phrases to avoid. Type each one and add: *vibes, community, intentional, container, sacred, conscious singles, manifest, energy, journey, soul, embodied, game-changing, unforgettable, transformative, authentic connection, like-minded.*

4. **Set the tone sliders** (if Canva offers them at the time of setup): Formality → moderate (not casual, not formal); Energy → calm; Specificity → high.

5. **Save and test** → New design → Magic Write → prompt: "Write a 30-word IG caption announcing a daytime sober singles event in Chicago." If the output sounds like Andrea (concrete, declarative, no banned words), Brand Voice is trained. If it returns "vibes" or "community" — clear those phrases again, re-train.

---

## Stage 3 — Folder Structure (10 min)

Folders prevent the "where did I save that?" hunt. Organize by Content Pillar — every post you make belongs to one of 7 categories.

**Steps:**

1. **Home → Folders → New folder.** Create 7 folders, in this order:
   - `01 — Spine` (brand intro, manifesto, format mechanics posts)
   - `02 — Story` (Andrea's founder origin, Costa Rica, music school, orchestra)
   - `03 — Curation` (room mechanics, "small on purpose", hell-yes filter)
   - `04 — Singles Reality` (recognition content, "you've been hungry for this")
   - `05 — Music` (DJ identity, vinyl, set notes, music history)
   - `06 — Chicago` (place-anchored content, Logan Square, lakefront, neighborhood)
   - `07 — Founder` (Andrea voice posts beyond the origin story)

2. **Add a "Week 1 — Active Builds" folder** at the top for the current week's in-progress designs. Move to pillar folder after posting.

3. **Add a "Templates — Starred" folder** for the 12 templates you'll star in Stage 4.

4. **Add an "Archive — Posted" folder** for everything that's gone live (monthly cleanup move).

**Verification**: 10 folders total, in this order:
- Week 1 — Active Builds
- Templates — Starred
- 01 — Spine
- 02 — Story
- 03 — Curation
- 04 — Singles Reality
- 05 — Music
- 06 — Chicago
- 07 — Founder
- Archive — Posted

---

## Stage 4 — Star 12 Base Templates (15 min)

You'll reuse these 12 templates 80% of the time. Star them once; never hunt for templates again.

### Template Selection Doctrine (read before searching)

The Canva template library is structurally hostile to the Resonance system. Most templates ship pre-poisoned with the visual grammar of the enemy: pink-purple gradients, hot saturation, all-caps sans headlines screaming MEET YOUR MATCH, faux-cinematic dark lighting, wellness-pastel mood boards. The work in Stage 4 is not "find 12 good templates." It is **find 12 templates whose bones (typography hierarchy + layout grid + negative space discipline) survive a full brand-kit recolor and font swap.** Bones first. Skin second. If the bones are wrong, no recolor saves it.

The three visual features that separate usable templates from poisoned ones, in priority order:

1. **Typography hierarchy**: one large display element + one or two supporting tiers. If every text block is the same size, the template is decoration, not editorial.
2. **Negative space discipline**: at least 35% of the canvas reads as breathing room. Crowded templates read as event-promoter design no matter what colors you swap in.
3. **Single-accent restraint**: one color carries the heat, the rest stay neutral. Templates with three competing accent colors fail the system on contact.

**How to star**: Hover on a template → click the star icon → it lands in your starred templates panel. Save each starred template to the `Templates — Starred` folder so they're one click away.

**Apply Brand Kit to each before saving**: open the template → Brand Kit panel → "Apply brand styles" → confirm template colors swap to your 10-color palette and fonts swap to GT Sectra + Inter. If "Apply brand styles" leaves any default Canva color or font behind, manually replace it before saving. The Brand Kit is not advisory; it is binding.

### The 12 Named Templates

---

**Template 1: Minimal Serif Quote Post (Spine pillar, manifesto pull-quote)**
- **Use for**: Spine pillar feed posts that carry a single manifesto line as the entire visual. Headline-led, photo-absent compositions. Day 1 post lives here.
- **Why this one**: The manifesto register is declarative-staccato (per voice doc §2 Pattern 3). A single serif line on cream, centered, with breathing room, is the visual analog of *"Daytime. Sober. Curated. Chicago."* The typography does the entire job; any decoration breaks the discipline.
- **Find it via**: Canva search `minimalist serif quote square` filtered to Square Post (1080×1080), Free + Pro. The three visual features that mark a good result: (a) one serif headline at 48pt+ as the only major element, (b) at least 40% blank space around it, (c) no decorative borders, no stock illustrations, no graphic flourishes.
- **Customize for brand**: Swap default serif for GT Sectra Medium 56pt in Midnight 900. Background to Cream 50. Add a thin 1px Terracotta 600 hairline 8px above and 8px below the quote. Remove every author credit, attribution badge, or decorative element the template shipped with.
- **Brand fit score**: 9/10. The bones match the manifesto register exactly. Most failures here are template-pollution (designer added a flourish), not template-structure.

---

**Template 2: Editorial Spread Layout (Spine pillar, format mechanics announcement)**
- **Use for**: Spine pillar posts that carry mechanic-as-sentence content like "doors at 2pm, no bar, eighty people, application open June 1." Layouts that read as a magazine page, not a flyer.
- **Why this one**: The format-mechanics posts need to land as editorial design: confident, body-text-led, no decoration. Per the aesthetic references doc, this is the *Gentlewoman / Fantastic Man* layout register. A single serif headline + a single column of well-set body type + one piece of restraint per spread.
- **Find it via**: Canva search `editorial magazine layout post` filtered to Square Post. The three features that distinguish a usable result: (a) headline-plus-body two-tier hierarchy (no third decorative tier), (b) the body text holds at a 12-line block or shorter, (c) a single hairline rule or single accent line, never two.
- **Customize for brand**: Headline in GT Sectra Medium 44pt Midnight 900. Body in Inter Regular 17pt Ink 700 with 1.55 line-height. Cream 50 background. The single accent: a thin Terracotta 600 hairline above the headline. Strip any pull-quote graphics, decorative initials, or designer flourishes.
- **Brand fit score**: 8/10. Strong bones, but most templates in this category over-decorate. Be ruthless about stripping.

---

**Template 3: Founder Origin Carousel Cover (Founder pillar, story carousel)**
- **Use for**: Slide 1 of any carousel that opens Andrea's founder origin material (Costa Rica, music school, the National Youth Orchestra, the room she came to Chicago looking for). The cover slide that earns the swipe.
- **Why this one**: Origin-story carousels need a memoir-grade first slide. The voice doc Section 4 example, *"At sixteen, I auditioned into a national youth orchestra,"* set in serif, on cream, with negative space around it, IS the visual. Photo-absent on the cover (the photo lives on slide 2). The cover is type-led the way a book's first page is type-led.
- **Find it via**: Canva search `book cover serif minimalist` filtered to Square Post. Templates from book-cover and editorial-essay categories outperform "carousel cover" search results. The three features that mark a good result: (a) a single serif headline that occupies the upper-third or lower-third (never centered for a cover), (b) optional subtitle in small caps tracking-extended sans, (c) zero illustrations, zero photos, zero decorative elements on slide 1.
- **Customize for brand**: GT Sectra Medium 56-64pt for the opening line, Midnight 900 on Cream 50. Optional subtitle in Inter SemiBold 12pt all-caps letter-spacing 0.12em in Slate 500: `ORIGIN · ONE` or `CHAPTER 1` register. Place the headline in the lower-third; let the upper two-thirds breathe.
- **Brand fit score**: 9/10. Book-cover templates carry the literary register the founder story requires. Resist the urge to add a photograph to slide 1; the photograph lives on slide 2.

---

**Template 4: Founder Portrait + Quote Overlay (Founder pillar, photoshoot deployment)**
- **Use for**: Posts that pair a single founder portrait from the Week 2 photoshoot with one line of founder voice (*"The room I came to Chicago looking for"* or *"I'm building rooms like that one ever since."*). Deploys when the photoshoot lands.
- **Why this one**: The photoshoot brief specifies decentered portraiture (subject in the right third, negative space carrying the left). The template that holds this discipline lets the quote sit in the negative-space quadrant without competing with the face. Per DESIGN.md §Layout: *"Headlines never compete with the focal subject of the photo."*
- **Find it via**: Canva search `editorial portrait quote overlay` filtered to Square Post. The three features that mark a usable result: (a) the portrait occupies 60-70% of the canvas with a clear negative-space quadrant, (b) the text overlay sits in the negative-space quadrant, never across the face, (c) no text-box backgrounds, no semi-transparent overlays, no gradient masks dimming the photo.
- **Customize for brand**: Replace stock portrait with the Annie-Leibovitz-Joan-Didion-reference shot from the photoshoot (per `05-photoshoot-brief.md` Shot 1). Quote in GT Sectra Medium 32pt Cream 50 if the negative-space quadrant is in shadow, Midnight 900 if it's in light. No overlay shading. The negative space in the photograph IS the type's canvas.
- **Brand fit score**: 8/10. The risk here is the template wanting to add a dimming overlay; refuse it. The photograph's own light is the lighting.

---

**Template 5: Singles-Reality Recognition Card (Singles Reality pillar, one-line save signal)**
- **Use for**: The single-line recognition posts (*"You've stopped going out altogether and called it self-care."* / *"I want to be in a room where I am not the diversity of the room."* per `recognition-map.md` Section B). The save-signal posts that get screenshotted to a folder the reader never names.
- **Why this one**: Per recognition-map.md, the save signal for Marcus / Nora / Daniel is *"a line in serif font on cream that says something his grandmother would say."* The post is one line, set with the dignity of a book epigraph. Decoration kills the recognition; restraint amplifies it.
- **Find it via**: Canva search `serif epigraph quote card` or `book quote design cream` filtered to Square Post. The three features of a usable result: (a) the quote sits in the visual center with at least 50% blank space around it, (b) no quotation marks rendered as decorative giant punctuation (no oversized curly quotes), (c) no author byline, no attribution badge, no "follow for more" sticker.
- **Customize for brand**: GT Sectra Book or Medium at 36-44pt in Ink 900 (slightly warmer than Midnight for the literary register), Cream 100 background (one step warmer than Cream 50 for the page-warmth feel). Optional: a single Gold 600 underline beneath the most load-bearing word, used sparingly, once per ten posts. No quotation marks.
- **Brand fit score**: 9/10. This is the template that does the most work for the brand. Master it first.

---

**Template 6: "Small On Purpose" Mechanic Card (Curation pillar, room-mechanic announcement)**
- **Use for**: Posts that name the curation mechanics (*"The room is fifty people."* / *"Hell-yes only."* / *"The address goes out the morning of."*). The operational-specificity posts that prove competence (per recognition-map.md save signal #4).
- **Why this one**: Mechanic posts need to read like a broadside, not a brochure. The visual register is *broadsheet announcement*: a clean line of type, a hairline rule, the smallest possible second tier carrying context. Per DESIGN.md, this is the Reid-Miles / Blue Note-Records discipline applied to a single mechanic fact.
- **Find it via**: Canva search `announcement card minimal serif` or `editorial broadsheet typography` filtered to Square Post. The three features of a usable result: (a) one large headline tier + one small caption tier, no body paragraph, (b) a hairline rule between the tiers or above the headline, (c) at least 45% blank space.
- **Customize for brand**: Headline in GT Sectra Medium 48pt Midnight 900. Caption in Inter SemiBold 12pt all-caps letter-spacing 0.12em in Slate 500: `RESONANCE · CHICAGO · 2026` register. Hairline rule in Border Hairline `#E1D6C2` at 1px. Cream 50 background. Strip every flourish.
- **Brand fit score**: 9/10. The broadsheet register is exactly what the curation mechanic needs.

---

**Template 7: Vinyl + Set Notes (Music pillar, photography-led with caption)**
- **Use for**: Music pillar posts that pair a photograph from the vinyl shot list (records on a wood surface, hands on a turntable, the needle drop) with one line of curatorial point-of-view. Photo carries 75% of the post; type captions the photograph.
- **Why this one**: Per DESIGN.md §Photography, type captions photographs; type does not replace them. The template that holds this discipline puts the photo full-bleed across the top two-thirds and reserves the lower third for a single line of caption, never a paragraph. Reid Miles Blue Note covers are the spiritual ancestor.
- **Find it via**: Canva search `editorial photo caption layout` or `vinyl record post template` filtered to Square Post. The three features: (a) photograph occupies the upper 65-75% of the canvas at full bleed, (b) caption is a single line in the lower third, (c) no overlay text on the photo, no border, no frame.
- **Customize for brand**: Photo region must be a real photograph from the shoot, specifically Shot 6 (vinyl needle drop) or Shot 7 (album cover collage) from `05-photoshoot-brief.md`. Caption in GT Sectra Book 24pt Ink 900 on Cream 50, single line, left-aligned, sitting 32px below the photo. Date stamp in Inter SemiBold 12pt all-caps Slate 500 above the caption.
- **Brand fit score**: 9/10. This is the template the brand was designed around. Use it often.

---

**Template 8: Chicago Place-Anchored Photo (Chicago pillar, environmental context)**
- **Use for**: Chicago pillar posts that pair a place-anchored daytime photograph (Lake Michigan at golden hour, a Logan Square wood floor, the Milwaukee Ave record store light) with one line of place-as-character text. The shots that say Chicago is the room behind the brand.
- **Why this one**: Per voice doc Rule 7: *"Chicago stays in the mouth. Don't over-reference the city, but when you do, mean it."* The visual analog is the same: the photograph carries Chicago, the type carries the line, neither announces the relationship. Vivian Maier's Chicago street work and Saul Leiter's color work are the references.
- **Find it via**: Canva search `place photography editorial post` or `landscape photography quote overlay` filtered to Square Post. The three features: (a) photograph occupies the full canvas with a clear negative-space quadrant in the upper-left or lower-left (sky / wall / floor), (b) text sits in the negative-space quadrant, never on the focal point, (c) no compass-rose graphics, no location-pin icons, no "Chicago, IL" badges.
- **Customize for brand**: Photograph from Shot 4 (lakefront walking) or Shot 8 (empty room with window light) per the shoot brief. Caption in GT Sectra Medium 28pt Cream 50 if the negative-space quadrant is dark, Midnight 900 if it's light. No icons. The city is the proof.
- **Brand fit score**: 8/10. Risk: most templates in this category want to add a "destination" graphic; strip it.

---

**Template 9: Text-Only Sense-Detail Story (Stories format, single-line sensory anchor)**
- **Use for**: Story frames that carry one line of sense-detail anchoring (*"11:47 on a Sunday. The phone is face-down on the kitchen counter."* / *"Coffee at my grandmother's house."* / *"The song that shifted the room."*). The breathing-room moments between heavier Story content.
- **Why this one**: Stories live at 1080×1920 vertical. The sense-detail Stories are the conversational-register punctuation between the more polished feed posts. They want one line of type holding the entire vertical canvas, with negative space doing the rest. Per voice doc §1, the conversational register lives in *"sense-detail anchoring (coffee at my grandma's, empanadas at the cafeteria, the song that shifted the room)."*
- **Find it via**: Canva search `typography only story` or `minimal quote story template` filtered to Story (1080×1920). The three features of a usable result: (a) one type element occupying the center or lower-third, no other graphic content, (b) at least 60% blank space, (c) no Instagram stickers, no swipe-up graphics, no UI-element overlays.
- **Customize for brand**: GT Sectra Book 36-44pt for the line itself in Ink 900 on Cream 50. Place the line in the lower-third so the upper two-thirds breathe. Optional: a single Caveat 24pt signature line two inches below the type, used only for Andrea-first-person Stories, never for general brand Stories.
- **Brand fit score**: 9/10. The Story format rewards restraint more than any other surface; this template honors that.

---

**Template 10: Carousel-to-Story Quote Pull (Stories format, feed-post extension)**
- **Use for**: Story frames that pull one line from a published feed post: taking the day's manifesto post and surfacing one quote-line as a Story 12 hours later. The continuity move that keeps a single thought alive across the day's content.
- **Why this one**: Stories are where feed content gets its second life. Per the Sunday-batch ritual, every feed post should have a paired Story version that surfaces the load-bearing line. The template that holds this is a vertical version of the feed quote card: same typography discipline, repositioned for 9:16.
- **Find it via**: Magic Resize from Template 1 (Minimal Serif Quote Post) → Stories format. Or search `vertical quote story serif` for native Stories templates. The three features: (a) the quote occupies the center of the canvas with at least 30% breathing room above and 30% below (IG's UI eats the top 220px and bottom 250px), (b) no template watermark, no "swipe up" badges, no decorative borders, (c) single serif headline as the only text element.
- **Customize for brand**: GT Sectra Medium 48-56pt in Midnight 900 on Cream 50, centered. Strip any platform-specific stickers the template shipped with. Add a single optional Caveat 18pt attribution line at the very bottom (`from the manifesto` or `Andrea, founder`), only when the quote needs anchoring.
- **Brand fit score**: 9/10. Pairing a feed post with a Story version doubles the surface area of every Sunday batch.

---

**Template 11: Event Date + Format Announcement (Event announcement, when Event #1 locks)**
- **Use for**: The Event #1 announcement post when the date and format details lock. Deploys once per event. Single use, high stakes, becomes the screenshot that gets sent to friends. *"June 14, 2026. 2pm. Chicago. Fifty people."*
- **Why this one**: Event announcement is the highest-pressure visual the brand makes. The wrong template here looks like a wedding invitation or a club flyer. The right one looks like the announcement of a curated cultural event: the New Yorker Festival, a 92Y reading, a Pitchfork programming announcement. Editorial broadsheet, type-led, photo-optional.
- **Find it via**: Canva search `editorial event announcement serif` or `book launch announcement minimal` filtered to Square Post. The three features: (a) the date is the largest element on the canvas, typographically dominant over the event name, (b) a hairline rule structures the layout into 2-3 horizontal tiers, (c) zero confetti graphics, zero balloon icons, zero "save the date" decorative scripts.
- **Customize for brand**: Date in GT Sectra Medium 72pt Midnight 900: `JUNE 14 · 2026`. Event name in Inter SemiBold 14pt all-caps letter-spacing 0.14em in Slate 500: `RESONANCE · CHICAGO · ROOM ONE`. Format facts in Inter Regular 16pt Ink 700 in a single-line block: `2PM-5PM · WOOD FLOOR · NO BAR · FIFTY PEOPLE`. Hairlines in Border Hairline. Cream 50 background. The post is type-led: no photo, no logo, no flourish.
- **Brand fit score**: 9/10. The broadsheet announcement is the right register for the highest-stakes visual the brand makes.

---

**Template 12: Newsletter Signup / Application-Gate CTA (Newsletter signup, application gate)**
- **Use for**: Posts that move IG followers to the newsletter waitlist or the application gate: the bridge from public-facing brand to private-list opt-in. Mid-pre-launch deployment (Weeks 3-5).
- **Why this one**: Application-gate copy needs to filter, not hype. Per voice doc §2 Pattern 5 (Hell-Yes Filter): invite + filter, two sentences. The visual analog is two stacked type blocks separated by a hairline: the invite on top, the filter underneath. Restrained CTA in Terracotta 600 as the only color heat.
- **Find it via**: Canva search `minimal call to action card serif` or `newsletter signup editorial` filtered to Square Post. The three features: (a) two-tier headline + subhead stack with a hairline between them, (b) the CTA is a typographic element, not a button graphic, (c) at least 35% blank space; the post should read as a letter, not a flyer.
- **Customize for brand**: Top tier (the invite) in GT Sectra Medium 36pt Midnight 900: *"The room is small on purpose."* Hairline rule. Bottom tier (the filter) in Inter Regular 16pt Ink 700: *"If you're a hell-yes, the application is open. resonance.chicago/apply."* The URL alone shifts to Terracotta 600 as the single accent. Cream 50 background.
- **Brand fit score**: 9/10. The voice doc's hell-yes filter is the conversion engine; this template renders it visually intact.

---

### Brand-Fit Verification Pass (run before closing Stage 4)

After all 12 templates are starred and recolored, open each one in sequence and run a three-question check:

1. *Does the recolored template still pass the daytime test?* If anything in the design reads as night-coded (deep shadows, neon-adjacent gradients, club typography), kill the template and find a replacement.
2. *Does the typography hierarchy survive the brand-kit swap?* If GT Sectra at the headline size looks visually weaker than the original template's sans, the template's structural hierarchy was built around a sans display face; replace it.
3. *Would Andrea send this to a friend with the message "this is the brand"?* If no, the template is decoration. Replace it.

Templates that fail any of the three get unstarred and replaced before Stage 4 closes. The 12 you keep are the 12 you live with for the next 10 weeks.

---

## Stage 5 — Build Day 1 Graphic + Magic Resize (20 min)

Day 1 post (Mon 5/26 7am) is "Brand Intro — Manifesto Excerpt." Copy lives in `04-ig-profile-and-first-week-content.md` Post 1. Build it now so it's ready to schedule.

**Steps:**

1. **Open a starred template** from `Templates — Starred` folder. Pick "minimal serif quote post" or "editorial typography post" — whichever matches your taste.

2. **Replace the placeholder text** with Post 1 copy. The full Post 1 caption is in file 04. The graphic itself should carry the **manifesto pull-quote** only — not the full caption. Recommended pull-quote (or pick your own from manifesto):

   > *"Heart encounters, not head encounters. Daytime. Sober. Curated. Chicago."*

3. **Set hierarchy:**
   - Pull-quote: GT Sectra Medium 56pt Midnight 900, centered, line-height 1.2
   - Sub-line below: Inter Regular 16pt Slate 500, "Resonance · First event July 2026"
   - Background: Cream 50 `#FBF7F0`

4. **Add one accent**: a thin 1px terracotta horizontal line above and below the pull-quote (8px from edges). Use Terracotta 600 `#B8492E`. Keep it subtle.

5. **No logo on this post** — the bio carries the brand name. Resist the urge to add a watermark.

6. **Export** → top right → Share → Download → PNG → 1080×1080 → "For social media."

7. **Magic Resize for Stories** → top right → Resize → Stories (1080×1920). Canva regenerates the design at the new aspect ratio. Spot-check that the pull-quote is centered with breathing room (Stories add visual room top + bottom for IG's UI). Export PNG.

**Verification**: Two files on your desktop — `post-1-square.png` and `post-1-story.png`. Both on Cream 50 background. Both pull-quote in GT Sectra Medium Midnight 900. Both with the thin terracotta accent.

You now have Day 1's feed post + Day 1's Stories preview ready to schedule. Repeat Stage 5 for Posts 2-5 in the **Sunday-night-batch ritual** below.

---

## Quick-Reference Card (Pin to Tab)

### Magic Write Caption Prompts — 3 Templates (calibrated for 9+ output on first run)

The default Magic Write prompt produces on-voice-but-flat copy because it has no reasoning constraint and no calibration anchor. The three prompts below carry a worked example of a 9+ output, a worked example of a failure, and an explicit pre-write reasoning step that forces Magic Write to identify scene, register, and close-strategy before drafting. The output ends with a self-audit line so Andrea can verify voice-match in three seconds.

Paste each prompt into Magic Write inside any Canva design, swap the bracketed parts.

---

**Prompt 1: Caption Opener Mode (the hook, 1-2 sentences)**

```
You are writing the opening 1-2 sentences of an Instagram caption for Resonance — a daytime, sober, curated dance party in Chicago for adults 30-42 who want to meet a partner. The reader has tried apps. The reader has tried bars. The reader has stopped going out and called it self-care.

BEFORE WRITING, identify three things in your head (do not output them):
1. The SCENE the reader recognizes themselves in. A specific time of day + object + posture + light. Not "tired of dating" — but "11:47 on a Sunday, phone face-down on the kitchen counter, you're not depressed, you're tired in a specific way."
2. The REGISTER. Polished (manifesto-staccato, period-stacked) or Conversational (sense-detail, autobiographical, run-on). Match register to topic: brand-mechanic topics use Polished; founder-story or recognition topics use Conversational.
3. The LANDING. Where the second sentence puts the reader. Not "you're not alone" — but a sharper diagnostic line that names something they have felt but never had named for them.

CALIBRATION EXAMPLE — 9+ HOOK (study this):
Topic: "people who have stopped going out"
Hook: "11:47 on a Sunday. The phone is face-down on the kitchen counter. You're not depressed. You're tired in a specific way."
Why this works: scene-anchored (time + object + posture), register-matched (polished, period-stacked), landing line names a feeling the reader has never had named ("tired in a specific way" — the specificity is the recognition).

CALIBRATION EXAMPLE — FAILURE (never write like this):
Topic: same
Hook: "Tired of formats that don't lead anywhere? You're not alone."
Why this fails: zero scene-anchor, "tired of formats" is brand-deck language not friend-language, "you're not alone" is the cliché signoff for every dating-event ever made.

CONSTRAINTS:
- Never open with "Here's what...", "Here's why...", "It's not X. It's Y.", "What if I told you...", "In a world of...", or any rhetorical question that reads as marketing.
- Never use these words: vibes, community, intentional, container, sacred, manifest, energy, soul, embodied, like-minded, holistic, mindful, conscious, transformative, authentic connection, level up.
- Em-dash count: zero in this hook. Use periods.
- If polished register: lean on period-stacked short sentences. If conversational register: lean on one longer breath with autobiographical specifics.

NOW WRITE. Topic: [TOPIC]

Output format — exactly two options, each followed by a one-line self-audit:

OPTION A:
[two-sentence hook]
[Self-audit: Scene anchor used = (object + time + light + posture, name them) | Register = polished or conversational | Banned vocab = none | Em-dashes = 0]

OPTION B:
[two-sentence hook in a different register or with a different scene-anchor]
[Self-audit: Scene anchor used = (object + time + light + posture, name them) | Register = polished or conversational | Banned vocab = none | Em-dashes = 0]
```

---

**Prompt 2: Caption Middle Mode (the 80-100 word body)**

```
You are writing the middle 80-100 words of an Instagram caption for Resonance — a daytime, sober, curated dance party in Chicago for adults seeking a partner. The caption opens with: "[OPENER GOES HERE]"

BEFORE WRITING, identify three things in your head (do not output them):
1. The MOVE this middle is doing. Pick ONE: (a) recognition-deepening (the opener named the scene; the middle deepens it with one more specific detail), (b) frame-then-sharpen (the opener established a frame; the middle names 2-3 specific enemies that sharpen what Resonance is NOT), (c) mechanic-as-sentence (the opener earned the reader's attention; the middle names one mechanic — daytime, sober, curated, phones off — in a sentence that carries the reason, never a feature bullet).
2. The REGISTER continuity. The middle must continue the register the opener established. If the opener was period-stacked polished, do not collapse into a wellness-brand run-on. If the opener was conversational sense-detail, do not stiffen into manifesto-mode.
3. The HANDOFF to the close. Leave the reader on a line that opens space for one of three close-types: (a) hell-yes filter ("if this is you, the room is open"), (b) operational specificity ("doors at 2pm, first event June 2026"), (c) concrete image ("dance with someone new").

CALIBRATION EXAMPLE — 9+ MIDDLE (study this):
Topic: "people who have stopped going out"
Opener: "11:47 on a Sunday. The phone is face-down on the kitchen counter. You're not depressed. You're tired in a specific way."
Middle (94 words):
"You're tired of formats that don't lead anywhere. The apps where everyone is auditioning. The bars where the only permission slip the city gives you starts at 11pm and requires three drinks. The wellness mixer where everyone is pretending the branded kombucha is the point. You stopped going out because you couldn't tell anymore which rooms were for the version of you who wants to meet someone and which rooms were for the version of you who has given up on the idea. Resonance is a daytime room. The music does the warming."
Why this works: frame-then-sharpen move (three named enemies — apps, bars, wellness mixer — each rendered as a specific scene, not a category). Register stays polished. Final line is mechanic-as-sentence ("the music does the warming") that hands off cleanly to a close.

CALIBRATION EXAMPLE — FAILURE (never write like this):
Middle: "We get it. Dating in 2026 is hard. That's why we built Resonance — a community for intentional singles who value authentic connection. Our daytime, sober events create the perfect space for meaningful conversations to unfold organically. Come join us and discover what it feels like to truly connect."
Why this fails: "we get it" is therapist-voice not friend-voice, "community" is banned, "intentional singles" is wellness-brand slop, "perfect space for meaningful conversations to unfold organically" is the exact paragraph every singles-event ever has written.

CONSTRAINTS:
- Banned vocabulary (zero hits): vibes, community, intentional, container, sacred, manifest, energy, soul, embodied, like-minded, holistic, mindful, conscious, transformative, authentic connection, like-minded, level up, journey, optimize, premium, aspirational, curated experience.
- Banned structural moves (zero hits): "It's not X. It's Y." reveals, twin-sentence aphoristic endings, triple-beat anaphora without a fourth landing line, italicized mid-paragraph aphorisms, "Here is the part nobody tells you" framing.
- Em-dash count: maximum 1 in the middle. Prefer periods or ellipses.
- The middle must carry one specific scene or named enemy. Abstract benefit-language fails.

NOW WRITE. Opener: "[OPENER]". Topic context: [TOPIC]

Output format — one option (80-100 words exactly), followed by self-audit:

[80-100 word middle]

[Self-audit:
- Move used = (recognition-deepening / frame-then-sharpen / mechanic-as-sentence)
- Register = (polished / conversational)
- Named enemies or specific scenes = (list them)
- Banned vocab = none
- Banned moves = none
- Em-dash count = N
- Handoff line = (the last sentence, which opens which close-type)]
```

---

**Prompt 3: Caption Close Mode (the CTA + closer, 1-2 lines)**

```
You are writing the closing 1-2 lines of an Instagram caption for Resonance — a daytime, sober, curated dance party in Chicago. The caption so far is:

"[FULL CAPTION TEXT TO THIS POINT]"

BEFORE WRITING, identify two things in your head (do not output them):
1. The CLOSE-TYPE the caption is asking for. Pick ONE of four:
   (a) Hell-yes filter — invite + filter, two sentences. "If you're a hell-yes, the room is open. If you're not sure, this isn't your event yet."
   (b) Operational specificity — concrete fact that proves competence. "First event June 2026. Application opens June 1. Fifty people, hell-yes only."
   (c) Concrete image close — one-line image that lands the post on a visual moment. "Dance with someone new." / "Come home with a number you'll actually call."
   (d) Bookend admission — a one-line tonal echo of the opener that names what the post was about underneath. Used rarely. Used right, it lands hard.
2. The CADENCE the close needs. If the body was period-stacked polished, the close stays short and declarative. If the body was conversational sense-detail, the close can carry one longer breath, but never a paragraph.

CALIBRATION EXAMPLE — 9+ CLOSE (study these):
- Hell-yes filter: "First event June 2026. Hell-yes only."
- Operational specificity: "Doors at 2pm. No bar. Fifty people. Application opens June 1."
- Concrete image: "Dance with someone you wouldn't have noticed an hour ago."
- Bookend admission: "It's a Sunday at 11:47. The phone is still face-down. The room is being built."

Why these work: each one is a complete thought that earns the post's end. No CTA-language ("click the link!"). No manufactured urgency ("spots filling fast!"). No question signoff.

CALIBRATION EXAMPLE — FAILURE (never write like this):
- "Click the link in bio to RSVP!" (CTA from someone else's brand)
- "Tag a friend who needs this." (stock IG closer)
- "What's your version of this?" (cheap question signoff — BANNED)
- "Who was it for?" (cheap question signoff — BANNED)
- "DM us 'YES' to learn more!" (lazy ritual, signals nothing)
- "Don't miss out — spots are filling fast!" (manufactured urgency, breaks brand discipline)

CONSTRAINTS:
- NEVER end with a generic question. The banned list: "What's your version?", "Who was it for?", "Anyone else feel this?", "Drop a 🌹 if...", "Tag a friend who needs this.", "What do you think?". These are cheap-question signoffs. They optimize for comment-count, not recognition.
- Earned questions (questions that advance the specific argument of THIS caption and could only land on THIS caption) are allowed, sparingly. If you cannot articulate why the question is non-transferable, do not use it.
- Banned vocabulary: vibes, community, intentional, container, sacred, manifest, energy, soul, embodied, like-minded, holistic, transformative, authentic connection, level up.
- Em-dash count: maximum 1 across all close options combined.
- The close must end on a concrete image, a specific operational fact, a hell-yes filter, or a bookend admission. Never on an abstraction.

NOW WRITE. The caption to this point: [PASTE]. Topic: [TOPIC]

Output format — exactly three options across DIFFERENT close-types (do not repeat type across options), each followed by a one-line self-audit:

OPTION A — [close-type name]:
[1-2 line close]
[Self-audit: Close-type = X | Concrete element = (the image / fact / filter named) | Banned vocab = none | Em-dashes = N | Earned question? = N/A or (why non-transferable)]

OPTION B — [different close-type name]:
[1-2 line close]
[Self-audit: same format]

OPTION C — [third close-type name]:
[1-2 line close]
[Self-audit: same format]
```

---

**How Andrea uses these prompts (the 90-second workflow)**

1. Open the design in Canva. Magic Write panel.
2. Paste Prompt 1 with the topic filled in. Get two opener options.
3. Pick the stronger opener. Paste Prompt 2 with the opener + topic filled in. Get one middle.
4. Paste Prompt 3 with the full caption-so-far + topic filled in. Get three closes.
5. Pick the close that matches the energy of the opener + middle.
6. Read the self-audit lines. If any audit flags a violation, regenerate that section only.

Total time per caption: 90 seconds to 3 minutes. The self-audits make the voice-check automatic.

**When the output still fails:** the most common failure is that Magic Write reverts to its default copywriter voice on the third or fourth use within a single session. Canva's voice-conditioning weakens with use. Fix: refresh the Brand Voice settings (Stage 2) once per week. If output is still flat, switch to Claude with the AI Brain Master (per `06b-claude-pro-action-steps.md`) and paste the result back into Canva. Claude holds voice across longer sessions.

### iPhone Photo Color-Grading Workflow (90 seconds per photo)

1. Open Canva → upload iPhone photo
2. Click photo → Edit Photo → Filters tab
3. Apply your saved custom filter **"Resonance Daytime"** (set up in Stage 1)
4. If photo is still too cool: bump Warmth +5, Shadows +5
5. If photo is too saturated: Vibrance -5, Saturation -5
6. Crop if needed (1:1 for feed, 9:16 for Stories)
7. Export → PNG → For social media

**Rule of thumb**: if a photo could have been taken at 11pm under fluorescent lights, it fails. Add warmth until it reads 2pm-by-a-window. (Per `01-visual/photography-rules.md`.)

### Weekly Batch Workflow — The Sunday Night Ritual (90 min)

Block 90 min every Sunday evening. Produce the entire next week's content at once.

| Block | Time | What |
|---|---|---|
| **Block 1** | 20 min | Open file `04-ig-profile-and-first-week-content.md` (or this week's content plan). Read all 5 feed posts + 7 Stories ideas. |
| **Block 2** | 50 min | Build 5 feed posts in Canva. ~10 min each — open template, swap copy, color-check, export. |
| **Block 3** | 10 min | Magic Resize each post → Stories format for the day-of preview Story. |
| **Block 4** | 10 min | Schedule everything in Content Planner (see below). |

After Block 4: week is done. Andrea posts ~10 min/day Mon-Fri (just the Story copy + replies + engagement). The heavy lifting is one Sunday session.

### Content Planner Setup (Schedule from Canva)

1. **Canva → Content Planner → Connect Social Account → Instagram**
2. Authenticate the `@resonance.chicago` IG account (must be a Business account, not Personal — switch in IG app: Settings → Account → Switch to Professional)
3. After connection: every design has a "Schedule" button on the Share menu
4. Click Schedule → pick date + time → write caption (paste from file 04) → add hashtags → confirm
5. Canva posts on the scheduled time, no manual upload needed

**Time saved**: 5-10 min/day vs manual upload. Cumulative: ~50 min/week back.

**Note**: Stories cannot be scheduled from Canva (IG limitation). Stories still get manually posted from the IG mobile app each morning. But Stories take 60 sec each.

---

## Common Issues + Fixes

| Issue | Fix |
|---|---|
| Brand Kit doesn't apply to a downloaded template | Click Brand Kit panel → "Apply brand styles" → confirm the toggle is on |
| Magic Write returns generic copy | Brand Voice not trained (Stage 2) or banned phrases not added; retrain |
| Photo looks "too AI-filtered" | Reduce saturation in the custom filter. The look is *light through a window*, not *Instagram filter pack* |
| Canva crashes or design won't save | Browser issue — switch to Chrome (Canva works best in Chrome); check internet |
| Magic Resize crops important text | Open the resized version, manually re-position the text; save as separate file |
| Hashtags get rejected on schedule | Some hashtags are flagged on IG (e.g., #dating). Remove + replace with a less-shadow-banned alternative |

---

## What This File Replaces / Supersedes

This file is the **action playbook**. It does NOT replace `brand-operating-system/04-ai-handoff/04-canva-component-spec.md` — that file remains the canonical *system reference* (exact specifications, locked variations, design tokens). If anything in this file contradicts the spec, the spec wins.

---

*Action playbook ends. After Stage 5: open `04-ig-profile-and-first-week-content.md` and build Posts 2-5 + Stories. Or open `06b-claude-pro-action-steps.md` to set up Andrea's Claude Pro Project as the caption-generation co-pilot.*
