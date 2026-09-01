---
name: jen-engine-full-pipeline
description: "End-to-end execution of Jen's 7-stage content pipeline — from intake answers through export. Entry point for full runs; stage-specific workflows available separately."
---

# Jen Engine — Full Pipeline Execution

> **Role:** This workflow walks through all 7 stages + 2 gates in a single orchestrated run. For stage-specific work, see `/jen-research`, `/jen-plan`, `/jen-scripts`, `/jen-design`, `/jen-export`.

---

## Pre-Pipeline: Brain Load Collection (Async)

### Step 0: Send Jen the Intake Questionnaire

**File:** `jen-voice-brain-intake.html` (or Google Doc: `16-sygvIU2ZMzDmEvbUisa7OAwDIUmqsBt2jWVTNVMCs`)

**What to send:**
- The HTML intake questionnaire (22 questions across 3 sittings)
- Set expectations: "No wrong answers. Messier is better. Voice notes, bullets, fragments all work. Three sittings if easier."
- Timeline: "Take your time. Return whenever ready."

**What Jen returns:**
- Raw answers in her voice (voice notes transcribed, bullet points, sentence fragments — all as-is)
- Answers might skip questions ("that doesn't apply," etc.) — that's OK
- If she records voice notes, transcribe them verbatim (capture filler words, pauses, everything)

### Step 1: Distill Brain Load into VOICE.md + BRAIN.md

**Input:** Jen's raw intake answers

**Load:** `skills/jen-engine/references/brain-load-distill-template.md` (structured template for synthesis)

**Process:**

#### VOICE.md Synthesis
From Jen's raw answers, distill:
- **Two registers** (FTHB/everyday vs luxury) — pull her actual phrasing from answers; add 2–3 example lines for each
- **Signature phrases** — extract words/phrases she says repeatedly ("what do people tease you about saying")
- **Cringe list** — exact phrases she hates competitors using (quote her directly)
- **CTA phrasing** — how she actually wants to ask for DMs, referrals, leads (her words, not sales language)
- **Tone mapping** — "when you're excited vs protective vs serious" (from her answers)
- **Anti-patterns** — what she explicitly doesn't do (from Q4, Q20)

**Result: VOICE.md** (locked voice profile, ~1.5 pages, ready for downstream stages)

#### BRAIN.md Synthesis
From Jen's raw answers, distill:
- **Farm neighborhoods ranked** — top 5 from her answers, with stock notes she provided
- **Typical buyer questions** — 3+ from Q9, in client voice (not cleaned up)
- **Typical seller questions** — 3+ from Q10, in client voice
- **ICP profile** — Q16 answer refined with Jen's actual buyer details (age, income, current rent, emotional state)
- **Business goal** — 90-day win from Q15 (her goal, not generic)
- **Team** — from Q14, names + roles + permissions for featuring in content

**Result: BRAIN.md** (locked business context, ~2 pages, ready for downstream stages)

---

## Gate 1: Brain Load Approval

**Decision point:** Does Jen approve VOICE.md + BRAIN.md as locked?

**Load:** `skills/jen-engine/references/gate-1-checklist.md`

### Gate 1 Checklist

- [ ] **VOICE.md passes live-read test:** Read section aloud — does it sound like Jen explaining how she talks?
- [ ] **Two registers are explicit:** Examples provided for both FTHB/warm vs luxury/authority POV?
- [ ] **CTA phrasing she owns:** Is there a way to end a video that feels authentic to her (not sales-y, not cheesy)?
- [ ] **Farm neighborhoods ranked:** Top 5 with stock notes (age, typical size, price band)?
- [ ] **ICP is Jen's actual buyer:** Does it match her real clients or generic FTHB profiles?
- [ ] **Team roster accurate:** Names, roles, permissions for featuring?
- [ ] **Fair-housing ready:** Any demographic language in VOICE.md that needs to go? (should only be housing-stock descriptors)

**Jen's decision:**
- **APPROVED:** Proceed to Stage 2
- **NEEDS CHANGES:** Go back to raw answers; specific rewrite request, re-distill, re-check

### If Changes Needed

Common feedback:
- "VOICE.md doesn't sound enough like me" → Include more fragments, more "um/like," pull exact phrases she uses
- "The CTA phrasing feels off" → Ask her to write it herself; transcribe exactly as she says it
- "Team roster is wrong" → Check which team members she actually wants appearing in content (sometimes answer is "just me")

Re-check and re-approve before proceeding.

---

## Stage 2: Demand Research

**Trigger:** Gate 1 approved ✅

**Command:** `/jen-research <market | listing-address>`

**Input:** BRAIN.md (market context, neighborhoods, typical questions)

**Load:** `jen-shortform-carousel-engine` workflow 01-research

### Stage 2 Execution

**Research Channels:**

1. **Google Search suggestions** — type "[neighborhood] [buyer question]" into Google, capture suggestions
2. **YouTube search suggestions** — same approach on YouTube
3. **People-also-ask** — scroll Google results for "People also ask" sections
4. **Reddit** — r/LosAngeles, r/AskLosAngeles, neighborhood-specific subs (r/SanFernandoValley, etc.)
5. **Facebook/Nextdoor** — search for similar questions in community groups
6. **LA Times / LAist** — housing coverage, recent articles on rates, insurance, construction trends
7. **Zillow / Redfin** — description trends, what buyers are searching (price ranges, size, locations)
8. **Current-event triggers** — rate changes, insurance updates, new construction in the area

**Output: DEMAND-REPORT.md**

Structure:
```
# Demand Report — [Market/Neighborhood]

## BUYER SEARCHES (7–10 exact phrases)
- Phrase 1: "[exact search phrase]"
  Evidence: Observed in [source, date]
  The worry (in their voice): [buyer's actual fear/concern]
  Difficulty: LOW / MED / HIGH

[repeat for each phrase]

## SELLER SEARCHES (7–10 same structure)

## RELOCATION SEARCHES (7–10 same structure)

## Top 5 QUESTIONS NOBODY IS ANSWERING (ranked by reach + difficulty)
1. Question: [exact phrasing]
   Evidence: [source]
   Why it matters: [the underlying fear]
   Difficulty: LOW / MED / HIGH

[repeat for 5 questions]

## PRODUCE FIRST (top 3 by reach + low difficulty)
1. [Question/phrase]
2. [Question/phrase]
3. [Question/phrase]
```

### Stage 2 Quality Check

Before moving to Stage 3:
- ✅ Every phrase/question is traceable to a source (if you can't point to it, it doesn't ship)
- ✅ Worry is in the buyer's/seller's voice, not analyst jargon
- ✅ Difficulty ratings make sense (could Jen answer this in <90s = LOW)
- ✅ PRODUCE FIRST are truly producible (not too broad or complex)

---

## Stage 3: Video Plan (Production Calendar)

**Trigger:** Stage 2 complete + DEMAND-REPORT.md

**Command:** `/jen-plan`

**Input:** DEMAND-REPORT.md + VOICE.md + BRAIN.md

**Load:** `jen-shortform-carousel-engine` workflow 02-plan

### Stage 3 Execution

**Build: PRODUCTION-CALENDAR.md**

Structure:
```
# Production Calendar — 4 Weeks, 20 Videos

## Week 1 Theme: [Theme from demand Qs]

### Monday — Strongest Hook
- **Video 1:** [Title]
  - Source demand: [Phrase from DEMAND-REPORT] + the worry
  - Format: Reel / Story / Carousel-video
  - Hook line: [Written-out hook, <15 words, speakable]
  - Beat outline: 
    1. [Beat 1]
    2. [Beat 2]
    3. [Beat 3]
  - CTA: [comment-keyword / DM / referral / direct]
  - Recording note: Location, props, ~X minutes
  - ★ VISUAL: [Yes/No] — if Yes, carousel-worthy concept

### Wednesday — Educational / Save-Worthy
- **Video 2:** [Title]
  [same structure]
  
### Friday — Story / Timely
- **Video 3:** [Title]
  [same structure]

[Repeat Week 1 structure for Weeks 2–4, 5 videos per week]

## FILM THESE THREE FIRST (Batch Set)
- **Video [X]:** [Title]
  - Location: [Exact location]
  - Wardrobe: [What she's wearing]
  - Props: [What's needed]
  - Estimated shoot time: ~X minutes
  - Shoot with videos [X], [Y], [Z] (batch at same location)

## BATCH-FILMING APPENDIX
Group all 20 videos by location for 2–3 shoot sessions:

### Session 1: Location A (estimate 1.5 hours)
- Video [X]: [Title]
- Video [Y]: [Title]
- Video [Z]: [Title]

### Session 2: Location B (estimate 1 hour)
[Videos at Location B]

### Session 3: Location C (estimate 45 min)
[Videos at Location C]
```

### Gate 2: Production Calendar Approval

**Decision point:** Does Jen approve the shoot plan + calendar?

**Load:** `skills/jen-engine/references/gate-2-checklist.md`

### Gate 2 Checklist

- [ ] **Themes match her voice:** Does each week feel like authentic Jen (per VOICE.md register)?
- [ ] **Locations are feasible:** Can she shoot at these locations without added logistics?
- [ ] **Batch-filming is realistic:** Can she really shoot 5–6 videos in one afternoon?
- [ ] **FILM THESE THREE FIRST are quick wins:** Doable today if needed (no complex setup)?
- [ ] **Fair-housing screened:** No "safe," "family-friendly," school references, demographic steering?
- [ ] **CTAs rotate:** Varied across weeks, not repetitive?

**Jen's decision:**
- **APPROVED:** Proceed to Stage 4
- **NEEDS CHANGES:** Specific revisions (rewrite hook, move location, different theme, etc.), re-check

---

## Stage 4: Script Pack

**Trigger:** Gate 2 approved ✅

**Command:** `/jen-scripts`

**Input:** PRODUCTION-CALENDAR.md + VOICE.md

**Load:** `jen-shortform-carousel-engine` workflow 03-scripts

### Stage 4 Execution

**Build: SCRIPT-PACK.md**

For each of the 20 videos in PRODUCTION-CALENDAR.md, create:

```
## Video [Number]: [Title]

### Hook Variants (3 options; recommend one)
- [Pattern-Interrupt] Hook: "[Hook line option 1]" ← RECOMMENDED
- [Stakes] Hook: "[Hook line option 2]"
- [Specificity] Hook: "[Hook line option 3]"

### Full Script (word-for-word, ~90–150 words, 30–60s)
[HOOK]

[One-breath context]

[BEAT 1: explanation/story/proof]
[BEAT 2: expansion/deeper insight]
[BEAT 3: takeaway/application]

[CTA — from PRODUCTION-CALENDAR]

[Stage directions in brackets: "look at camera," "lean in," "on-screen text: '$800K'"]

### Bullet Version (for teleprompter / reference)
- Hook: [Hook verbatim]
- Beat 1 cue: [≤6 words]
- Beat 2 cue: [≤6 words]
- Beat 3 cue: [≤6 words]
- CTA: [CTA verbatim]

### Instagram Caption
[Hook-first line]

[2–4 value lines, one idea per line]

[Comment-keyword CTA or DM ask]

#realestatewithjing #SFVRealEstate [3–5 niche hashtags]

### TikTok Caption
[Shorter version, more question-forward]

[1–2 hashtags]

### YouTube Shorts Caption
**Title (keyword-front-loaded, searchable):** [Exact search phrase from DEMAND-REPORT]

Description:
[Search phrase verbatim, first line]
[2–3 value lines]
[Link / channel mention]

Tags: [3–5 tags matching search phrase]

### On-Screen Text Plan
- Slide 1 (0–5s): "[Text] — position: top-center, sans-serif, white, 28pt"
- Slide 2 (15–25s): "[Numeral/stat] — position: center, bold, 48pt"
- Slide 3 (end): "[CTA text] — position: bottom, @realestatewithjing"
```

Repeat for all 20 videos.

**End with: RECORDING RUN SHEET**

```
## Recording Run Sheet (All 20 Videos)

Shoot in this order (per BATCH-FILMING APPENDIX):

### Session 1: Location A
- **Video [X]:** [Title]
  - Wardrobe: [what she's wearing]
  - Props: [list]
  - Approx time: 8 min
- **Video [Y]:** [Title]
  [same]
- **Video [Z]:** [Title]
  [same]

**Batch 1 total: ~25 min setup + shoot**

### Session 2: Location B
[Same structure]

### Session 3: Location C
[Same structure]

---

**Wardrobe Checklist:**
- [Item 1]
- [Item 2]
[etc.]

**Props Checklist:**
- [Item 1]
[etc.]

**Call Time Notes:**
- Expect to wrap by [time]
- Weather contingency: [alternate location or date]
```

### Stage 4 Quality Check

Before moving to Stage 5:
- ✅ Scripts pass mouth-test (read aloud, sounds like Jen?)
- ✅ Hooks are hooked (would you stop scrolling?)
- ✅ Beats answer the promise of the hook (not filler)
- ✅ CTAs are from VOICE.md (not generic "click link")
- ✅ Fair-housing lint clean (no demographics, schools, safe language)
- ✅ Captions are independently useful (someone could understand from caption alone)
- ✅ Recording run sheet is shoot-ready (brand-new PA could execute)

---

## Stage 5: Carousel Specs (Design Brief)

**Trigger:** Stage 4 complete + ★ VISUAL-flagged videos from PRODUCTION-CALENDAR.md

**Command:** `/jen-design`

**Input:** SCRIPT-PACK.md + PRODUCTION-CALENDAR.md + VOICE.md

**Load:** `jen-shortform-carousel-engine` workflow 04-carousels (brief mode)

### Stage 5 Execution

**Step 1: Select 10 Strongest Visual Ideas**

From ★ VISUAL flags in PRODUCTION-CALENDAR.md, pick 10 with:
- Clearest single visual concept per carousel
- High-reach demand questions
- Existing assets (her photos, herself on camera, props she has)

**Step 2: Build ONE Sample Carousel**

Pick the strongest idea and build it in full:

```
# Sample Carousel: [Title / Concept]

## Slide 1 — HOOK (Typographic)
Content: "[Hook text, ≤12 words, legible at 150px]"
Visual: White/cream background, sans-serif type, no photo
Design: [Font name/size, color, alignment]

## Slide 2 — Data / Stat (Visual)
Content: "[Stat/numeral]"
Visual: Bar graph / comparison / oversized number, no text-heavy sentence
Source/date: "[Source in small print]"
Design: [Visual metaphor — graph bar? comparison chart?]

## Slide 3 — Concept (Illustration / Photo / Metaphor)
Content: "[Single idea, ≤25 words]"
Visual: [Diagram / photo / illustration supporting the idea]
Design: [Visual approach]

## Slide 4 — Proof / Example (Photo or Testimonial)
Content: "[Brief quote or fact, ≤25 words]"
Visual: [Photo from listing / screenshot / testimonial]
Design: [How it's presented]

## Slide 5 — CTA
Content: "@realestatewithjing 💬 [comment-keyword] or DM for [offer]"
Visual: Lockup of her handle + button/CTA element
Design: Brand colors, clean, professional

---

## Visual System (Locked)
- Font family: [Sans-serif name], [Serif name]
- Color palette: [Primary color hex], [Secondary hex], [White/cream], [Accent]
- Grid: [Layout structure — left/right, center, etc.]
- Spacing: [Consistent margins, padding]
- Graphic elements: [Allowed elements — bars, dots, dividers; no emojis, no gradients]
```

**Step 3: Get Approval**

Gate decision: Does Jen approve this sample carousel?
- [ ] Visual metaphor is clear (mute mode = still understand)?
- [ ] Colors/fonts match her brand?
- [ ] CTA feels natural (not sales-y)?

**Step 4: Lock Visual System & Spec Remaining 9 Carousels**

Once sample is approved, document the locked system and apply it to the other 9:

```
# Carousel Specs — 10 Carousels (Locked Visual System)

[Sample carousel details as locked template above]

---

## Carousel 2: [Title]
- Source demand: [Q from DEMAND-REPORT]
- Slide 1 hook: "[Text, ≤12 words]"
- Slide 2: [Concept / stat]
- Slide 3: [Expansion]
- Slide 4: [Proof]
- Slide 5: [CTA]
- Paired script caption: [IG caption from SCRIPT-PACK.md video X]

## Carousel 3: [Title]
[Same structure, apply locked visual system]

[Repeat for Carousels 4–10]

---

## Caption Pairing List
| Carousel | Script Video | Instagram Caption |
|----------|-----------|----------|
| Carousel 1 | Video [X] | [Caption text] |
| Carousel 2 | Video [Y] | [Caption text] |
[etc.]
```

### Stage 5 Output: CAROUSEL-SPECS.md

Portable design brief (ready for Claude Design handoff) or ready-to-build in Canva:
- 10 carousel specs with locked visual system
- Caption pairing list (carousel to Instagram caption)
- Visual assets reference (brand colors, fonts, grid, allowed elements)
- Banlist verification (no stock photos, no emojis, no gradients, no drop shadows)

---

## Stage 6: Design Execution (Render Batch)

**Trigger:** Stage 5 complete + CAROUSEL-SPECS.md approved

**Command:** Load Claude Design or Canva + CAROUSEL-SPECS.md

**Input:** CAROUSEL-SPECS.md + locked visual system + caption pairing list

### Stage 6 Execution

**In Claude Design (or Canva):**

1. Create 10 carousel designs (1080×1350 each, 5–7 slides per carousel)
2. Apply locked visual system (fonts, colors, grid, spacing)
3. Build siblings, not clones (variations that feel related, not identical)
4. Verify: mute-mode understanding, mobile legibility, banlist clean
5. Export to PNG/PDF for each carousel

**Output:**
- `CAROUSEL-BATCH/` folder with 10 carousel PNGs/PDFs
- Instagram captions (text file with all 10 captions paired to carousels)

---

## Stage 7: Export (Send Package)

**Trigger:** All prior stages complete + CAROUSEL-BATCH/ PDFs ready

**Command:** `/jen-export`

**Input:** All stages complete (VOICE.md, BRAIN.md, DEMAND-REPORT.md, PRODUCTION-CALENDAR.md, SCRIPT-PACK.md, CAROUSEL-SPECS.md, carousel PDFs)

### Stage 7 Execution

**Build: SEND-PACKAGE.md**

Structure:
```
# Content Package — [Market/Listing/Topic]

## Quick Overview
- **Duration:** 4 weeks
- **Content:** 20 Reels/videos + 10 carousels
- **Format:** Press-record + copy-paste ready

---

## Quick Start: FILM THESE THREE FIRST

[From PRODUCTION-CALENDAR batch set]

Video [X]: [Title]
- Location: [Address/place]
- Wardrobe: [Item]
- Props: [List]
- Shoot time: ~8 min
- Batch with Videos [Y], [Z] at same location

[Repeat for top 3]

---

## 4-Week Content Calendar (Posting Schedule)

### Week 1
**Monday, [Date], 7am:** Post Video 1 (Reels)
- Caption: [From IG SCRIPT-PACK caption]
- CTA: [DM / Comment keyword / Referral ask]

**Wednesday, [Date], 8am:** Post Carousel 1
- Caption: [From caption pairing list]
- CTA: [DM / Save this / Comment]

**Friday, [Date], 7:30am:** Post Video 2 (Reels)
- Caption: [IG caption]
- CTA: [Rotated CTA]

[Repeat pattern for Weeks 2–4, staggering Reels + Carousels]

---

## Scripts & Recording Run Sheet

See `SCRIPT-PACK.md` for:
- Full word-for-word script for each of 20 videos
- Bullet versions (for teleprompter)
- On-screen text plans
- Batch-filming appendix (group by location)
- Wardrobe + props checklist

[Link to SCRIPT-PACK.md file or inline the full pack here]

---

## Carousel PDFs

All 10 carousels ready to download + post:
- [Carousel 1.pdf] — [Title]
- [Carousel 2.pdf] — [Title]
[etc.]

---

## Instagram Captions (All 20 Videos + 10 Carousels)

### Video Captions
[From SCRIPT-PACK.md, IG captions for all 20 videos]

### Carousel Captions
[From caption pairing list, IG captions for all 10 carousels]

---

## CTAs Review

Review for repetition + variety:
- Week 1: 2× "Comment YOUR biggest fear," 1× "DM for free guide," 1× "Tag someone looking to buy"
- Week 2: [Vary CTAs]
[etc.]

**CTA Rotation Target:** No single CTA appears more than 2–3 times in 4 weeks

---

## Fair-Housing Audit

✅ All content screened for:
- No demographics (age, race, family size, disability)
- No steering language (safe, family-friendly, good schools)
- No demographic targeting
- Housing-stock, price, commute, amenities only

**Result: PASS**

---

## Next Steps

1. Download all carousel PDFs
2. Review scripts (especially FILM THESE THREE FIRST)
3. Block out shoot dates on calendar
4. Film Videos 1–3 (batch at [Location A])
5. Post Video 1 on [exact date/time]
6. Batch carousel prep (all PDFs ready to drag-drop into Meta Business Suite)

---

## Questions / Edits

- Need to swap out a video? Reference PRODUCTION-CALENDAR.md; suggest a replacement from that list
- Want to change a caption? Edit in caption pairing list; ensure fair-housing compliance
- Carousel needs redesign? Reference CAROUSEL-SPECS.md; request specific slide/carousel number
```

### Stage 7 Quality Check

Before final delivery:
- ✅ SEND-PACKAGE is forwardable (can be Slack/email copy-paste)
- ✅ All scripts included (someone new could press record)
- ✅ Carousel PDFs are downloadable
- ✅ Posting calendar is exact (dates + times)
- ✅ CTAs reviewed (not repetitive)
- ✅ Fair-housing final audit: PASS

---

## Completion

**Final Deliverable: SEND-PACKAGE.md**

Forward to Jen or her team. They now have:
- 4-week production plan
- 20 scripts (press-record ready)
- 10 carousel designs (copy-paste to Instagram)
- Exact posting calendar + CTAs
- Fair-housing verification

**Ready to ship.**

---

## Reference Files

- `references/brain-load-distill-template.md` — Template for VOICE.md + BRAIN.md synthesis
- `references/gate-1-checklist.md` — Gate 1 approval criteria
- `references/gate-2-checklist.md` — Gate 2 approval criteria
- `../SKILL.md` — Overview of all 7 stages + 2 gates
- `../genius.md` — Execution patterns, quality bars, recovery loops
