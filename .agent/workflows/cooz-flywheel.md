---
description: Cooz-specific content flywheel — voice memos in, authentic multi-platform drafts out
---

# `/cooz-flywheel` — The Resurrection Coach Content Flywheel

Takes a raw voice memo from Coach Cooz (Acusio Bivona / The Resurrection Coach) and produces a complete weekly content package: LinkedIn post, blog post, podcast episode topic outline, Instagram carousel, Instagram reel script. Every output passes through the Cooz Voice Profile so the drafts sound like Cooz, not like AI doing a Cooz impression.

***This workflow is a fork of `/ip-flywheel` specifically tuned for Cooz's voice DNA, The Man in the Valley archetype, and the 5-asset Ignition-Phase content cadence.***

## When to Use
- Cooz sends Farrice a voice memo (5-10 minutes of raw thinking, client session reflections, gym moments, book chapter material, spiritual reading, contrarian takes)
- Farrice needs to turn that raw material into the week's published content across 5 platforms
- OR Farrice wants to start from a weekly trending-topic prompt and get Cooz's contrarian take

## Usage

```
/cooz-flywheel [path to voice memo transcript OR trending topic]
/cooz-flywheel --verbose [same]
```

### Flags

| Flag | Effect |
|------|--------|
| `--verbose` | Show each pipeline stage's raw output inline |
| `--topic-first` | Start from a trending topic prompt instead of a voice memo |
| `--lane-a-only` | Generate only Lane A (grounded practical M/W/F) content |
| `--lane-b-only` | Generate only Lane B (mythic Sunday) content |

---

## Step 1: Load the Cooz Context Stack

Read these files in order:

1. **Cooz Voice Profile** — `_active/coach-cooz/15-final-package/03-cooz-voice-profile.md` — machine-readable voice DNA
2. **The Man in the Valley Playbook** — `_active/coach-cooz/15-final-package/02-man-in-the-valley-playbook.md` — unified ICP + content pillars + pain points bank
3. **The Ignition Plan Section 5** — `_active/coach-cooz/14-ignition-plan/THE-IGNITION-PLAN.md` (sections 5, 7 for content engine rules and brand calibration)
4. **Voice guide** — `_active/coach-cooz/05-offers-and-frameworks/VOICE-GUIDE.md` — phrases to use / phrases to never use
5. **The 8 Tenets framework** — `_active/coach-cooz/05-offers-and-frameworks/8-TENETS-FRAMEWORK.md` — curriculum spine, use for Lane A educational posts
6. **WS1.6 voice rule** — `_active/coach-cooz/03-research/WS1.6-voice-validation-and-data-recovery.md` — Sheedy 6-step template

---

## Step 2: Parse the Input

Input is one of two types:

### Type A — Raw voice memo transcript
A 5–10 minute transcript of Cooz thinking out loud. Pull out:
- **The specific moment** — one scene, one client session, one conversation, one training session
- **The honest feeling** — what Cooz was actually feeling in that moment (not the clean version)
- **The insight** — what he noticed or realized
- **The would-have-been-denied** — the thing he would have refused to hear three years ago
- **Any language that sounds like Cooz** — verbatim phrases to preserve

### Type B — Trending topic prompt
A topic from the masculine development / fitness / recovery / small business space that's trending this week. Pull out:
- **The dominant take** — what everyone is saying about this topic
- **The contrarian angle** — where Cooz's perspective would diverge
- **The Man in the Valley hook** — how this topic lands for Cooz's specific buyer (NOT for founders, NOT for optimizers)

---

## Step 3: Generate the Master Creative Brief (Cooz version)

This is the approval gate. Build the brief in Cooz's framework, not a generic content framework.

**The Brief must include:**

1. **The Specific Moment** — one concrete scene the content anchors in (from the voice memo) or one recognizable moment the contrarian take inverts (from the topic prompt)
2. **The Man in the Valley Hook** — which of the 5 core pains this content hits: fumes / silence / clock you can't see / failure graveyard / mirror he avoids (per the Sabri Suby pain amplification sequence)
3. **The I-Led Confession** — one sentence Cooz says about HIMSELF that earns the right to the you-pivot later
4. **The Turning Point** — the moment in the piece where the shift happens ("The true moment happened when…" / "I finally admitted that…")
5. **The You-Pivot** — max 2 sentences, the universal takeaway. Named in advance so the drafts don't bury it.
6. **The Anti-Optimization Move** — how this piece inverts the optimization frame (per Dan Koe framework finding: integration > optimization is Cooz's highest-leverage content move)
7. **The Voice Mode** — diagnostic / confessional / framework (per voice guide)
8. **Lane Assignment** — Lane A (grounded practical M/W/F) or Lane B (mythic Sunday)
9. **The 5-Asset Plan** — what each asset will do with this material (LinkedIn post, blog post, podcast outline, Instagram carousel, Instagram reel)

**Present this Creative Brief to Farrice (not Cooz).**

> [!IMPORTANT]
> **HALT EXECUTION.** Explicitly ask Farrice: "Does this Creative Brief match Cooz's actual voice memo? Do you want to tweak the moment, the turning point, or the you-pivot before I generate the 5-asset package?" Wait for explicit GO.

---

## Step 4: Generate the 5-Asset Package

Only after the Creative Brief is approved, generate each asset strictly from the brief, strictly through the Cooz Voice Profile.

### Asset 1: LinkedIn Post (3 variants)

**Format**: Sheedy 6-step structure from WS1.6
1. One-line I-declaration
2. Specific expansion in I (2-3 concrete details from the moment)
3. Turning point in I
4. One-line public declaration (optional)
5. You-pivot, max 2 sentences
6. Short closer (symbol, brand line, period)

**Word count**: 120-300 for Lane A, 200-500 for Lane B (Sunday)

**Rhythm**: Apply Cooz's sentence cadence from the voice profile — SHORT (3-5) / SHORT (4-6) / SHORT (3-5) / MEDIUM (15-20) / SHORT (5-7) for Lane A; slightly slower for Lane B

**3 variants**:
- **Variant A** — "Specificity-heavy" — leans on the concrete moment, minimal abstraction
- **Variant B** — "Witness-voice" — written slightly third-person per the WS1.5 witness voice finding ("I know a guy…")
- **Variant C** — "Framework-embedded" — drops a named Tenet or the McBroom lineage mid-story

Each variant differs only in the ending and the opening angle. Core moment stays constant.

### Asset 2: Blog Post / Substack

**Length**: 800-1500 words. Newsletter style.

**Structure**:
1. Personal opening (the moment from the brief, extended)
2. The industry problem (what everyone else is saying about this / the optimization trap)
3. The Cooz reframe (specific to this piece)
4. One framework drop (a Tenet, a protocol element, or a McBroom lineage story)
5. The universal takeaway (you-pivot territory, but longer)
6. The soft CTA (Triage Audit link, no hard sell)

**Voice**: slightly less punchy than LinkedIn. More room to breathe. Still I-led. Still one specific moment.

### Asset 3: Podcast Episode Topic Outline

**Format**: outline for a Resurrection Series episode (15-20 min solo or interview), NOT the full script

**Sections**:
- **The Hook (60 sec)** — Cooz opens with the specific moment, in his voice
- **The Setup (2 min)** — what he's going to talk about, why it matters
- **The Story (5-8 min)** — the main body, usually 2-3 concrete moments strung together
- **The Framework (3-5 min)** — the lesson, the Tenet, the principle
- **The Turn (2 min)** — the universal, the thing every Man in the Valley needs to hear
- **The Close (1 min)** — symbol, prayer, brand line, CTA

**NOT written word-for-word.** Outline only. Cooz improvises in his voice from the outline.

### Asset 4: Instagram Carousel (5-7 slides)

**Format**: text-on-image carousel, designed for thumb-stop + save

**Slides**:
- **Slide 1**: One-line hook, large type, minimal background (the I-declaration)
- **Slides 2-5**: The story beats, 1-3 sentences per slide
- **Slide 6**: The turn / universal takeaway
- **Slide 7**: Brand line + CTA ("DM 'Resurrection' for the Triage Audit")

**Aesthetic reference**: per the Cooz website design brief — charcoal/bone/oxblood/brass palette, display serif for headlines, no emoji, no motion graphics

### Asset 5: Instagram Reel Script (45-90 sec)

**Format**: camera-to-face, Cooz talking, minimal b-roll, no background music doing heavy lifting

**Script structure**:
- **0-5 sec**: Hook line (the I-declaration, delivered looking straight at the camera)
- **5-40 sec**: The story (the specific moment, 2-3 beats)
- **40-70 sec**: The turn (the universal)
- **70-90 sec**: The close (brand line, no hard CTA — CTA lives in the caption)

**Caption**: the Sheedy 6-step LinkedIn post (copy Asset 1 Variant A), trimmed to Instagram character limit

---

## Step 5: Pass Every Asset Through the Voice Profile Filter

Before output, scan each asset against the Cooz Voice Profile ban list. Reject and rewrite if ANY asset contains:

- "Here's what" / "Here's why" / "Here's how" as an opener
- "Founder" / "executive" / "creator" / "C-suite" / "high performer" / "CEO"
- "Rock bottom" / "broken" / "damaged" / "wellness journey"
- "Amazing" / "incredible" / "game-changer" / "crush it" / "level up"
- Em dashes beyond 1-2 per piece
- Any emoji
- Sustained second-person scene narration ("You walk to your car. You sit in the driveway. You…")
- Generic AI coaching voice ("In today's demanding corporate landscape…")
- Motivational speaker voice ("Are you READY to UNLOCK…")
- Therapy speak ("Honor your journey. Healing is not linear.")

**This filter is non-negotiable. Any asset that fails the scan gets rewritten, not shipped.**

---

## Step 6: Output Format

```markdown
# COOZ FLYWHEEL — Weekly Content Package
## Week of [DATE]
## Source: [voice memo transcript filename OR trending topic]
## Lane: [A or B]

## THE SPECIFIC MOMENT
[The one concrete scene the content anchors in]

## THE APPROVED CREATIVE BRIEF
[Full brief from Step 3]

---

## ASSET 1: LINKEDIN POST — 3 Variants

### Variant A — Specificity-heavy
[Full post, 120-300 words, Sheedy 6-step structure]

### Variant B — Witness-voice
[Full post]

### Variant C — Framework-embedded
[Full post]

---

## ASSET 2: BLOG POST / SUBSTACK
[Full article, 800-1500 words]

---

## ASSET 3: PODCAST EPISODE OUTLINE
[Outline only, not full script]

---

## ASSET 4: INSTAGRAM CAROUSEL (7 slides)
[Slide-by-slide text]

---

## ASSET 5: INSTAGRAM REEL SCRIPT (45-90 sec)
[Camera-to-face script + caption]

---

## VOICE PROFILE SCAN
- [ ] No banned phrases detected
- [ ] No em dash overuse
- [ ] No founder language
- [ ] No sustained you-narration
- [ ] Cooz rhythm fingerprint applied
- [ ] One specific moment in every asset
- [ ] You-pivot only once per asset, max 2 sentences

## PUBLISHING SCHEDULE RECOMMENDATION
- **LinkedIn**: [Variant X — why this one for this week]
- **Blog/Substack**: [recommended day]
- **Podcast**: [if recording this week, when]
- **Instagram carousel**: [day]
- **Instagram reel**: [day]
```

---

## Step 7: Deliver to Farrice

Farrice reviews the full package. Cooz never sees the drafts until Farrice has approved them. Farrice either:
- Ships directly to Cooz for final voice edit + post
- Sends back to the flywheel with specific feedback
- Uses a different variant than the one the flywheel recommends

**Cooz always has the final cut. The flywheel is a draft engine, not a publishing engine.**

---

## Feedback Loop (after publishing)

When a piece of content is published, log the result:

1. **Engagement data**: likes, comments, DMs received, profile visits
2. **Conversion data**: Triage Audit bookings attributed to this post
3. **Voice check**: Did Cooz heavily edit it or ship close to the draft? (If heavy edit, the flywheel needs voice profile tuning)

Posts that land become positive training data. Posts that don't become anti-patterns. Over time the flywheel tunes to Cooz's actual voice more precisely.

**Weekly review** (Farrice, 15 min): look at the last 5 posts, note what worked, tune the voice profile if a pattern emerges.

---

## Lead Magnet Generator (secondary output)

Every 4-6 weeks, the flywheel produces a free lead magnet as a side output from accumulated content:

- **Format options**: a short PDF guide (1 of the 8 Tenets, deep-dive), a free audio series (3 episodes of the Resurrection Series packaged), a free Loom audit template
- **Use**: DM lead magnet to anyone who engages, warm-network follow-up, podcast guest appearance offer
- **Trigger**: when the flywheel has accumulated 10+ shipped posts in one content pillar, package the best material into a lead magnet

---

## Notes

- The flywheel is NOT a scheduling tool. Cooz or Farrice still posts manually.
- The flywheel is NOT an analytics tool. Use existing Notion / Google Sheets for tracking.
- The flywheel IS a voice-preservation draft engine. Its one job is making AI drafts sound like Cooz instead of sounding like AI.
- The flywheel assumes Cooz is sending 1-2 voice memos per week. Without voice memos, the flywheel falls back to trending-topic mode but quality drops noticeably.
- **Trend-prompt quality control**: trending topics fed into the flywheel should come from masculine development / fitness / recovery / small business spaces — NOT startup Twitter, NOT creator economy, NOT biohacker culture. The topic scanning phase is where Farrice's taste matters most.

---

## Related Workflows

- `/ip-flywheel` — the generic version, for other clients or Farrice's own content
- `/ghostwrite` — captures voice DNA, used to generate the Cooz Voice Profile upstream
- `/voice-first-content` — pure voice-memo-to-content pipeline (simpler than this, no Creative Brief approval gate)
- `/daily-flywheel` — journal-entry-to-content pipeline, use for Cooz's book chapter material

## Related Assets

- Cooz Voice Profile: `_active/coach-cooz/15-final-package/03-cooz-voice-profile.md`
- Man in the Valley Playbook: `_active/coach-cooz/15-final-package/02-man-in-the-valley-playbook.md`
- Ignition Plan: `_active/coach-cooz/14-ignition-plan/THE-IGNITION-PLAN.md`
- 8 Tenets: `_active/coach-cooz/05-offers-and-frameworks/8-TENETS-FRAMEWORK.md`
- Voice Guide: `_active/coach-cooz/05-offers-and-frameworks/VOICE-GUIDE.md`
