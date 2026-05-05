---
description: V5 cross-platform content flywheel for Coach Cooz — voice memo in, LinkedIn + IG carousel + IG reel + YouTube + blog out
---

# `/cooz-flywheel-v5` — The Resurrection Coach Cross-Platform Engine (V5)

Takes a raw voice memo from Coach Cooz (Acusio Bivona / The Resurrection Coach) and produces a full weekly content package: **LinkedIn post + Instagram carousel + Instagram reel + YouTube long-form + blog post**. Every output passes through the V5 voice register so the drafts sound like Cooz texting a friend, not Cooz performing for an audience.

## Why this fork exists (V3 → V5)

The V3 cooz-flywheel pointed to voice docs with banned vocabulary (substrate / biological infrastructure / cognitive throttle / operator / operating system / "founder, executive, C-suite, high-performer" triple-list / "Man in the Valley" archetype). That register tested at zero engagement.

V5 voice is the **testimonials-backstory register** — specific, story-led, slightly self-deprecating, warm, peer-to-peer, slightly funny when warranted, anchored in **real long-arc clients** (Mike 9 yrs, Robin 8 yrs, Sammy 4+ yrs, Corey 4 yrs, Carron 3 yrs, Sam 2.5 yrs, Buzz 1 yr, Mari 3 mo) and the **Brave Choice methodology** (Cooz's proprietary frame, named verbatim by Robin).

This workflow points exclusively at V5 voice docs. Do not load V3-era files even if referenced upstream.

## When to use

- Cooz sends Farrice a voice memo (5-10 minutes — a real client moment, a session reflection, a gym scene, a Brave Choice moment, a podcast topic seed)
- Farrice needs the week's content across all 5 platforms produced from that one input
- OR Farrice needs to backfill a week with no fresh voice memo (fall back to V5-TESTIMONIAL-LIBRARY anchors)

## Usage

```
/cooz-flywheel-v5 [path to voice memo transcript]
/cooz-flywheel-v5 --no-memo [pulls from V5-TESTIMONIAL-LIBRARY]
/cooz-flywheel-v5 --linkedin-only [skip IG/YouTube/blog]
```

### Flags

| Flag | Effect |
|------|--------|
| `--no-memo` | Backfill mode — pull anchor from V5-TESTIMONIAL-LIBRARY when no voice memo |
| `--linkedin-only` | Generate only LinkedIn (skip IG carousel, IG reel, YouTube, blog) |
| `--cross-platform-only` | Generate IG + YouTube + blog (skip LinkedIn — use V5-LINKEDIN-CONTENT-SYSTEM templates instead) |
| `--lane-1` / `--lane-2` / `--lane-3` | Force a specific lane (Body-First / Transformation Architecture / Case Study) |

---

## Step 1 — Load the V5 Context Stack

Read these files in order. **DO NOT load V3-era voice docs.** If you find a `_DEPRECATED/` path or `15-final-package/` path, that's V3 — skip it.

1. **V5-NOTEBOOK-KNOWLEDGE** — `_active/coach-cooz/16-may-2026-pivot/V5-NOTEBOOK-KNOWLEDGE.md` (the canonical knowledge document — voice rules, 5-voice rotation, 3-lane spec, vocabulary banks, banned moves, 6-point quality gate)
2. **V5-COOZ-TRUE-VOICE** (internal) — `_active/coach-cooz/16-may-2026-pivot/_internal/V5-COOZ-TRUE-VOICE.md` (deeper voice DNA + jargon-to-real-voice translation guide)
3. **V5-TESTIMONIAL-LIBRARY** (internal) — `_active/coach-cooz/16-may-2026-pivot/_internal/V5-TESTIMONIAL-LIBRARY.md` (the proof spine — 18 verified testimonials, deployable phrases, anchor verbatims)
4. **V5-WINNING-MECHANISMS** (internal) — `_active/coach-cooz/16-may-2026-pivot/_internal/V5-WINNING-MECHANISMS.md` (6 durable structural mechanisms + Cooz's unique angle on each — for hook + structure variation)
5. **V5-COOZ-HANDOFF** — `_active/coach-cooz/16-may-2026-pivot/V5-COOZ-HANDOFF.md` (brand frame in one line, pricing pathways, hard rules)
6. **V5-CROSS-PLATFORM-ENGINE** — `_active/coach-cooz/16-may-2026-pivot/V5-CROSS-PLATFORM-ENGINE.md` (platform role hierarchy + repurposing rules per platform)

---

## Step 2 — Parse the Input

### Type A — Voice memo transcript

Pull out:
- **The specific moment** — one scene, one client, one session, one Brave Choice instance Cooz actually witnessed or experienced
- **The named real client** (if present) — Mike, Robin, Carron, Sam, Corey, Sammy, Buzz, Mari, Cody McBroom, Mariano, or a client mentioned by initials
- **The honest feeling** — the unhedged emotion in Cooz's voice (not the cleaned-up version)
- **The insight** — what Cooz noticed, named, or realized
- **Verbatim Cooz phrases** — phrases to preserve word-for-word (these become the hook in 60% of posts)
- **The lane** — Lane 1 (Body-First Foundation) / Lane 2 (Transformation Architecture) / Lane 3 (Case Study)

### Type B — `--no-memo` backfill

Pull from V5-TESTIMONIAL-LIBRARY:
- Pick one of the 5 long-arc anchors (Mike, Robin, Carron, Corey, Sam) — rotate so no anchor used twice in 2 weeks
- Anchor in their backstory verbatim
- Run the same Step 3 brief generation as Type A

### Anti-pattern guard

If the input has no specific moment, no named real client, and no Cooz verbatim phrasing — **HALT and request a voice memo.** Do not generate from generic prompts. Per V5-NOTEBOOK rule: "If the input isn't anchored to a real moment Cooz actually experienced or witnessed, return: NEEDS COOZ VOICE MEMO — cannot generate without anchor."

---

## Step 3 — Generate the V5 Creative Brief (one brief, all 5 platforms)

This is the approval gate. Brief must include:

1. **The Specific Moment** — one concrete scene
2. **The Named Real Client** (or initials) — Mike (M.G.), Robin, Carron (C.W.), etc.
3. **The Lane** — 1 / 2 / 3
4. **The Voice** — Scene · Confession · Reframe · Witness · Proof (V5 5-voice rotation)
5. **The I-Led Opening** — first sentence in I, in scene, or with named real client (NEVER opens in "you")
6. **The Brave Choice Moment** (if applicable) — does this hit one of the 3 Brave Choice questions?
7. **The Mechanism Repositioned** — which of the 6 winning mechanisms is being deployed (from V5-WINNING-MECHANISMS) and what's Cooz's unique angle on it this time
8. **The You-Pivot** — max 2 sentences, late in the piece, identity-level not behavioral
9. **The Closer** — V5-verified ("That's the work." / "They look like themselves again." / "I rebuild the body that built the life." / etc.) OR a Cooz-aligned identity question
10. **The CTA** — pulled from V5-NOTEBOOK CTA rotation (Question / Confession / Challenge / Soft Invite / Direct / No-CTA) — never repeat the same CTA twice in a row

**Present the Brief to Farrice (not Cooz).**

> [!IMPORTANT]
> **HALT EXECUTION.** Ask Farrice: "Does this Brief match Cooz's actual voice memo? Are the named clients accurate? Is the lane right? Confirm GO or send back tweaks."

Wait for explicit GO before generating Step 4.

---

## Step 4 — Generate the 5-Platform Package

Only after Brief approved. Each output is generated **independently from the Brief** (not by repurposing the LinkedIn post — that flattens the platform-specific voice).

### ASSET 1 — LinkedIn Post

**Format**: V5-LINKEDIN-CONTENT-SYSTEM template structure (Lara Acosta Pattern 20 + Sheedy 6-step + V5 5-voice rotation)

**Word count**: 120-300 for Lane 1 · 200-450 for Lane 2 · 200-300 for Lane 3 single-image (or 800-1500 for Lane 3 carousel caption)

**Structure** (V5 default — Sheedy + Pattern 20):
1. Opening line in I, in scene, or with named real client (NEVER "you")
2. 2-3 specific expansion sentences (the moment, the detail, the number)
3. The turn — what Cooz noticed / what changed / what the client said
4. (Optional) The methodology callout — Brave Choice / Tenet / specific protocol
5. The you-pivot — max 2 sentences, late, identity-level
6. The closer — V5-verified phrase

**Outbound link**: ALWAYS in first comment, never in body. (V5-NOTEBOOK engagement rule #1.)

**Voice fidelity check** — run V5 6-point quality gate before shipping:
- [ ] Opens in I / scene / named client (not "you")
- [ ] Contains exactly ONE specific moment Cooz experienced or observed
- [ ] You-pivot ≤ 2 sentences, late
- [ ] No banned vocabulary
- [ ] No banned AI structural moves
- [ ] Closer is V5-verified

**3 variants** (rotate by week — each variant uses a different V5 voice):
- **Variant A — Scene** (35% rotation default) — opens with a scene, slowest entry
- **Variant B — Confession** (20%) — Cooz I-led admission, vulnerable but not victim
- **Variant C — Reframe / Witness / Proof** (40% combined) — depending on the moment

### ASSET 2 — Instagram Carousel (7 slides)

**Format**: Brock Johnson shareworthy mechanics + V5 voice. Text-heavy carousel designed for save + share.

**Slides**:
- **Slide 1 — The Hook**: One-line, large type, off-white on cinematic black. The recognition moment. Pattern interrupt that makes the thumb stop. (e.g., *"She pulled 200+ pounds in rhinestoned go-go boots."* — Sam case study Lane 3 hook)
- **Slide 2 — The Specific**: 2-3 sentences expanding the scene. Real client. Real number. Real detail.
- **Slide 3 — The Turn**: What Cooz noticed. The mechanism. The realization.
- **Slide 4 — The Proof Stack**: Numbers, arc length, verifiable specifics (e.g., "*9 years. Mike. 33 yr executive.*")
- **Slide 5 — The Methodology** (if Brave Choice applies): One of the 3 Brave Choice questions, isolated, large type.
- **Slide 6 — The Universal Takeaway**: The you-pivot version, 1-2 sentences.
- **Slide 7 — The Close**: V5-verified closer + soft CTA ("Triage Audit link in bio" — never aggressive).

**Visual**:
- Text-first carousel. Photos from V5-PHOTO-INVENTORY allocated to lane (Lane 1 = Photo 04 kettlebell B-roll; Lane 2 = Photo 12 lifestyle / Photo 09 gym crouching; Lane 3 = relevant photo)
- Palette per V5-VISUAL-BRAND-BRIEF (cinematic black + amber accent + brown warmth)
- Typography per V5-VISUAL-BRAND-BRIEF (Editorial New / Inter Display headlines, Inter body)
- NO emoji. NO motion. NO branded watermarks beyond a small Cooz logotype on Slide 7.

**Caption**: Short — 2-3 sentence version of the Brief's moment + named client + close. Hashtags: max 5, tasteful (#strengthtraining #executivefitness #burbankcoach — NOT #fitfam #grindset).

### ASSET 3 — Instagram Reel (45-90 sec, talking head + B-roll)

**Format**: Camera-to-face Cooz, minimal B-roll, no music doing heavy lifting.

**Script structure**:
- **0-5 sec — Hook**: The I-declaration or scene opener. Looking straight at camera. (Pattern: same opening line as the LinkedIn post for cross-platform recognition.)
- **5-40 sec — The Story**: The specific moment. 2-3 beats. Real client name when applicable.
- **40-70 sec — The Turn**: What Cooz noticed. The mechanism. The Brave Choice if applicable.
- **70-90 sec — The Close**: V5-verified closer. CTA in caption only — NOT in spoken script.

**B-roll specs**:
- Action shots: gym training, kettlebell mid-swing, deadlift form, Cooz coaching a real client
- Cinematic darkness aesthetic per V5-VISUAL-BRAND-BRIEF
- Subtitles burned in (V5 brand typography) — 80% of IG reels watch with sound off
- Cover frame: Photo 02 (pointing CTA) for direct-CTA reels OR Photo 11 (gym pointing) — use sparingly (intense)

**Caption**: Same as IG carousel caption (Asset 2). DO NOT paste the LinkedIn post into the IG reel caption — different platforms, different reading rhythms.

### ASSET 4 — YouTube Long-Form (8-12 min, talking head)

**Format**: Caleb Ralston personal-brand structure. Cooz on camera, single-take or lightly edited, real conversation feel.

**Why YouTube ≠ podcast**: Podcast (Resurrection Series) is for long-form deep dives (30-60 min) — different show, different cadence. YouTube long-form is for **8-12 min weekly explainers** that double as the blog post script (Asset 5). One recording, two outputs.

**Script outline** (NOT word-for-word — Cooz improvises from the outline):

| Section | Duration | Content |
|---|---|---|
| **Cold open** (0-15 sec) | The hook — same opening as LinkedIn + IG | Pattern: scene-led, named client, specific number |
| **Title card + brand intro** (15-30 sec) | "I'm Cooz. The Resurrection Coach. I rebuild the body that built the life." | Bookmarked — visual brand frame |
| **The setup** (30 sec - 2 min) | Why this matters. The problem named. | Lane-specific (1 / 2 / 3) |
| **The story / the work** (2-7 min) | The named client, the moment, the mechanism, the arc | Real specifics — never invented |
| **The methodology callout** (7-9 min) | Brave Choice / Tenets / specific protocol | Surface the proprietary frame |
| **The you-pivot** (9-10 min) | The universal takeaway | Identity-level, not behavioral |
| **The CTA + close** (10-12 min) | Triage Audit link in description, V5-verified closer, brand sign-off | Description has all links + chapter timestamps |

**Production specs**:
- Single 16:9 widescreen camera, eye-level, full-frame mirrorless preferred
- Lighting per V5-VISUAL-BRAND-BRIEF: warm gold rim, deep darks, controlled cinematic
- Audio: lavalier or shotgun mic (NOT camera-mic — quality floor for YouTube authority)
- Title format: *"Specific moment-led title — never clickbait. Pattern: [Named client] / [the work] / [9 years] / [a moment that proves it]"*
- Thumbnail: Photo 10 (gym coaching gesture) or Photo 02 (pointing CTA) + bold text headline (Editorial New, off-white on black)
- Description: Chapter timestamps + V5 brand statement + Triage Audit link + 3 hashtags

### ASSET 5 — Blog Post (1500-2500 words, coachcooz.com)

**Format**: Adam Enfroy SEO + V5 voice anchor. The blog is the SEO foundation — long-form depth, keyword-targeted, doubles as YouTube transcript when post-edited.

**Why blog ≠ Substack**: Cooz's blog lives at coachcooz.com (his domain — owns the SEO compounding). Substack would be a separate publication (not currently in scope; V5 does not include a Substack). The blog is the SEO + email-capture foundation.

**Structure**:
1. **The hero scene** (200-300 words) — extended version of the LinkedIn opening. Specific moment. Named client. Real number.
2. **The problem named** (300-400 words) — Lane-specific external + internal + philosophical problem (StoryBrand 3-level)
3. **What's actually happening** (400-600 words) — the mechanism. The diagnostic. The protocol or Brave Choice frame applied.
4. **The proof spine** (300-500 words) — 1-2 of the 5 long-arc anchors (Mike / Robin / Carron / Corey / Sam) backstory verbatim
5. **The reframe** (200-300 words) — Cooz's unique angle on the mechanism (per V5-WINNING-MECHANISMS)
6. **The CTA + close** (100-200 words) — Triage Audit conditional resolution (Donald Miller GP8 — "If you're [X], booking the Triage Audit is the right call"), V5-verified closer

**SEO layer (Enfroy method)**:
- One target keyword per post (e.g., "Burbank executive coach," "executive fitness coach Los Angeles," "long-term personal trainer Burbank," "high-performing professional fitness," "Brave Choice methodology")
- 1,500+ words minimum (Enfroy: 70% of long-form posts ranking #1 are 1,500-3,000 words)
- H2/H3 structure with the keyword in 2-3 H2s
- Internal links: minimum 3 to other coachcooz.com posts; outbound links: 2-3 to authoritative sources (Cody McBroom, peer-reviewed studies if cited)
- Schema markup: Article + Person + Organization (handled at the site level, but content has to be structured to match)
- Email capture: Brave Choice methodology lead-magnet pop-up at 50% scroll OR end-of-post

**Voice fidelity**: blog allows slightly slower cadence than LinkedIn (longer paragraphs, more breath). Still V5 register — testimonials-backstory voice, not strategist register. Run the 6-point quality gate.

---

## Step 5 — Cross-Platform Voice Consistency Scan

Before output, run this scan across ALL 5 assets:

| Check | Pass criteria |
|---|---|
| **Same anchor moment** | All 5 assets reference the SAME specific moment / named client / real number from the Brief |
| **Same V5 voice register** | Specific · story-led · slightly self-deprecating · warm · peer-to-peer · slightly funny when warranted |
| **No banned vocabulary** | Zero substrate / biological infrastructure / cognitive throttle / operator / operating system / "Here's what" openers (V5-NOTEBOOK ban list) |
| **No banned AI structural moves** | Zero "It's not X. It's Y." reveals / twin-sentence aphoristic endings / triple-beat anaphora / italicized aphorisms / "Here is the part nobody..." framing / mic-drop+deflation / cross-piece rhythm repetition / triple-list audience naming |
| **Pronoun architecture** | 60-70% I · 5-10% you (one pivot, late) · 15-25% he/she/[client name] · we almost never |
| **Real testimonial fidelity** | Any quoted client language matches V5-TESTIMONIAL-LIBRARY verbatim. No paraphrase. No invention. |
| **Cross-platform variation** | Each asset adapts to its platform's reading rhythm — NOT just the LinkedIn post pasted into IG/YouTube/blog |

**If ANY check fails on ANY asset, regenerate that asset.** Do not ship a 5-platform package where 4 assets pass and 1 fails — the failing asset undermines the rest.

---

## Step 6 — Output Format

```markdown
# COOZ FLYWHEEL V5 — Weekly Cross-Platform Package
## Week of [DATE]
## Source: [voice memo filename OR --no-memo backfill anchor]
## Lane: [1 / 2 / 3] · Voice: [Scene / Confession / Reframe / Witness / Proof]
## Anchor client: [name + arc length]
## Mechanism: [V5-WINNING-MECHANISMS reference + Cooz's unique angle this time]

---

## THE BRIEF (approved by Farrice)
[Full V5 Brief from Step 3]

---

## ASSET 1 — LinkedIn Post (3 variants)
### Variant A — Scene
[Full post]

### Variant B — Confession
[Full post]

### Variant C — Reframe / Witness / Proof
[Full post]

**Recommended for this week**: [Variant X — why]

**First-comment outbound link**: [exact URL or "no outbound link this week"]

---

## ASSET 2 — Instagram Carousel (7 slides)
### Slide 1 — Hook
[1 line + visual spec reference]

### Slide 2 — Specific
[Text + visual spec]

### Slide 3 — Turn
[Text + visual spec]

### Slide 4 — Proof
[Text + visual spec]

### Slide 5 — Methodology / Brave Choice
[Text + visual spec]

### Slide 6 — Universal
[Text + visual spec]

### Slide 7 — Close + Soft CTA
[Text + visual spec]

**Caption**: [2-3 sentence caption + max 5 hashtags]
**Cover image (Slide 1)**: [Photo allocation per V5-VISUAL-BRAND-BRIEF]

---

## ASSET 3 — Instagram Reel Script (45-90 sec)
[Full talking-head script + B-roll cues + cover frame allocation]
**Caption**: [Same as IG carousel]

---

## ASSET 4 — YouTube Long-Form (8-12 min outline)
[Section-by-section outline with timestamps + production notes]
**Title**: [final title]
**Thumbnail**: [Photo allocation + headline overlay text]
**Description**: [first 3 lines + chapter timestamps + Triage Audit link + 3 hashtags]

---

## ASSET 5 — Blog Post (1500-2500 words, coachcooz.com)
[Full post with H1/H2/H3 structure]
**Target keyword**: [keyword]
**Internal links**: [3+ coachcooz.com URLs]
**Email-capture position**: [50% scroll / end of post]

---

## VOICE FIDELITY SCAN — All 5 Assets
- [ ] Same anchor moment across all 5
- [ ] V5 voice register fidelity (testimonials-backstory voice)
- [ ] No banned vocabulary
- [ ] No banned AI structural moves
- [ ] Pronoun architecture compliant (60-70% I)
- [ ] Real testimonial fidelity (verbatim from V5-TESTIMONIAL-LIBRARY)
- [ ] Cross-platform variation (not LinkedIn pasted everywhere)

## PUBLISHING SCHEDULE — This Week
- **LinkedIn**: [day, recommended variant]
- **Instagram carousel**: [day]
- **Instagram reel**: [day]
- **YouTube long-form**: [recording day + publish day]
- **Blog post (coachcooz.com)**: [publish day]
```

---

## Step 7 — Deliver to Farrice

Farrice reviews the full 5-platform package. Cooz never sees drafts until Farrice approves. Farrice either:
- Ships to Cooz for final voice edit + post
- Sends back to flywheel with feedback
- Picks a different LinkedIn variant than recommended
- Rejects an asset entirely if it fails the Step 5 scan

**Cooz always has the final cut.** The flywheel is a draft engine, not a publishing engine.

---

## Feedback Loop (post-publish)

After publishing, log per asset:

1. **Engagement data per platform** — LinkedIn impressions/comments/saves; IG likes/saves/shares; YouTube views/watch time/subs gained; blog organic traffic + email captures
2. **Conversion data** — Triage Audit bookings attributed to which asset
3. **Voice check** — Did Cooz heavily edit the asset before posting? Heavy edit signals voice profile drift; light edit signals the V5 register is locked

**Weekly review** (Farrice, Friday 30 min): which platform carried the most weight this week? Which asset had voice drift? Tune V5-NOTEBOOK if a pattern emerges (e.g., 3 weeks in a row of Lane 2 outperforming Lane 1 → adjust the rotation).

**Quarterly review** (Farrice + Cooz, every 90 days): is the cross-platform engine producing measurable Triage Audit bookings? Which platform is the highest-leverage? Reallocate effort accordingly.

---

## Hard Rules (don't break — locked from V5-NOTEBOOK + V5-COOZ-HANDOFF)

1. **Outbound links go in first comment on LinkedIn, never in body.** Single biggest reach lever.
2. **3 lanes only on LinkedIn for 90 days.** Body-First Foundation · Transformation Architecture · Case Studies. Off-lane goes to book/podcast/blog.
3. **No banned vocabulary in any asset on any platform.** The ban list is universal — what's banned on LinkedIn is banned on IG / YouTube / blog. Same voice across surfaces.
4. **Voice memo input on a real client moment minimum 2x/week.** No voice memo → fall back to V5-TESTIMONIAL-LIBRARY anchor → if both unavailable, HALT — do NOT generate from generic prompts.
5. **First 60 minutes after LinkedIn post**: respond to every comment. Algorithm weights early-engagement velocity heavily.
6. **Run the 6-point V5 quality gate on every LinkedIn post before publish.** No exceptions.
7. **Every asset references THE SAME anchor moment.** No multi-thread chaos across platforms.
8. **Real testimonial verbatim — no paraphrase.** If the V5-TESTIMONIAL-LIBRARY says Mike's been with Cooz 9 years, post says 9 years. Not 8, not "almost a decade," not "many years." Verbatim.
9. **Cooz has final cut.** Farrice doesn't ship without Cooz's voice edit pass on each asset for the first 4 weeks.

---

## Anti-Pattern Guard (V3 mistakes V5 must NOT repeat)

- **Loading V3-era voice docs** (`_DEPRECATED/` paths, `15-final-package/` paths). Don't.
- **Generating from generic trending topics** when no voice memo exists. The V3 fallback to "trending topic mode" produced flat content. V5 fallback is V5-TESTIMONIAL-LIBRARY anchors only.
- **Pasting the LinkedIn post into IG / YouTube / blog as-is.** Each platform has different reading rhythm. Same anchor moment, different platform-shape.
- **Using "Man in the Valley" archetype.** Killed in V5. The buyer is "the high-performing professional running on fumes" (coachcooz.com hero language) — gender-neutral.
- **Using "operator" / "operating system" / "substrate" / "biological infrastructure" / "cognitive throttle".** All banned. See V5-NOTEBOOK ban list.
- **Triple-list audience naming** ("entrepreneurs, founders, professionals"). Banned move #8.
- **Inferring client specifics.** Every named client claim must trace to V5-TESTIMONIAL-LIBRARY verbatim. No invention.

---

## Related V5 Assets

- V5-COOZ-HANDOFF: `_active/coach-cooz/16-may-2026-pivot/V5-COOZ-HANDOFF.md`
- V5-NOTEBOOK-KNOWLEDGE: `_active/coach-cooz/16-may-2026-pivot/V5-NOTEBOOK-KNOWLEDGE.md`
- V5-LINKEDIN-CONTENT-SYSTEM: `_active/coach-cooz/16-may-2026-pivot/V5-LINKEDIN-CONTENT-SYSTEM.md`
- V5-LINKEDIN-PROFILE: `_active/coach-cooz/16-may-2026-pivot/V5-LINKEDIN-PROFILE.md`
- V5-CROSS-PLATFORM-ENGINE: `_active/coach-cooz/16-may-2026-pivot/V5-CROSS-PLATFORM-ENGINE.md`
- V5-VISUAL-BRAND-BRIEF: `_active/coach-cooz/16-may-2026-pivot/V5-VISUAL-BRAND-BRIEF.md`
- V5-TESTIMONIAL-LIBRARY (internal): `_active/coach-cooz/16-may-2026-pivot/_internal/V5-TESTIMONIAL-LIBRARY.md`
- V5-COOZ-TRUE-VOICE (internal): `_active/coach-cooz/16-may-2026-pivot/_internal/V5-COOZ-TRUE-VOICE.md`
- V5-WINNING-MECHANISMS (internal): `_active/coach-cooz/16-may-2026-pivot/_internal/V5-WINNING-MECHANISMS.md`

## DO NOT load these (V3-era — superseded by V5)

- ~~`_active/coach-cooz/15-final-package/03-cooz-voice-profile.md`~~
- ~~`_active/coach-cooz/15-final-package/02-man-in-the-valley-playbook.md`~~
- ~~`_active/coach-cooz/14-ignition-plan/THE-IGNITION-PLAN.md`~~
- ~~`_active/coach-cooz/05-offers-and-frameworks/VOICE-GUIDE.md`~~
- ~~`_active/coach-cooz/05-offers-and-frameworks/8-TENETS-FRAMEWORK.md`~~
- ~~`_active/coach-cooz/03-research/WS1.6-voice-validation-and-data-recovery.md`~~
- ~~`_active/coach-cooz/_DEPRECATED/...`~~ (anything in this path)

V5 is the source of truth. V3-era docs contain banned vocabulary and outdated archetypes.
