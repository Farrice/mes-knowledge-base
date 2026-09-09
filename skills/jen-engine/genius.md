# Jen Engine — Execution Patterns & Gate Frameworks

> **Role of this file:** Documents how each stage fires, what each gate decides, error recovery patterns, and the quality bar for each deliverable. This is the practitioner's reference for "what does success look like at each step?"

---

## Stage 1: Brain Load → Gate 1 Approval

### What Happens

1. **Jen completes the async intake questionnaire** (22 questions across 3 sections: Voice, Market & Business, Boundaries & Logistics)
   - Source: Google Doc `16-sygvIU2ZMzDmEvbUisa7OAwDIUmqsBt2jWVTNVMCs`
   - Format: Her raw answers, in her voice (voice notes, fragments, bullet points all OK)

2. **Distill answers into two locked files:**
   - `VOICE.md` — her voice profile, locked registers, signature phrases, words she uses, what makes her cringe, CTA phrasing she owns
   - `BRAIN.md` — her business context, farm neighborhoods ranked, typical client questions, business goals, team roster, ICP refinement

### Gate 1 Decision Framework

**Jen approves both VOICE.md + BRAIN.md** if:

- [ ] **Voice lock passes the live-read test:** Read a section from VOICE.md out loud. Does it sound like Jen explaining how she talks? (Not describing herself, actually exemplifying her voice)
- [ ] **Registers are clear:** FTHB/everyday register (<$1.5M, warm-friend) vs luxury register (≥$2M, "Quiet Flex Elite Advisor") are both explicit with examples
- [ ] **CTA phrasing she owns:** Is there a way she would actually end a video without cringing? (She rejected "DM me KEYS" as cheesy; this should be her authentic ask)
- [ ] **Farm neighborhoods are ranked:** Top 5 neighborhoods with brief stock notes (age, typical size, price band)
- [ ] **ICP is calibrated:** From her answers, not from generic FTHB profiles; does it match her actual clients?
- [ ] **Team roster is accurate:** Names, roles, permissions for appearing in content (her call, not baked-in)

### Quality Bar — VOICE.md

Must include:
- **Two registers** (explicit, with 2–3 example lines each)
- **Signature phrases** ("what people tease her about saying") — verbatim from her answers
- **Cringe list** (phrases she hates in competitors) — quoted exactly
- **CTA phrasing** (how she actually wants to ask for DMs, referrals, lead intros)
- **Anti-patterns** (what she doesn't do — no urgency manufacturing, no jargon, no "as a top 1% agent")
- **Emotion mapping** (how she sounds excited vs protective vs serious)

### Quality Bar — BRAIN.md

Must include:
- **Farm neighborhoods** (top 5 ranked with housing stock notes)
- **Typical buyer questions** (3+ from her actual practice, in client voice, not cleaned up)
- **Typical seller questions** (3+ same)
- **Business goal** (90-day win, in her words)
- **ICP refinement** (does her "typical buyer" match or diverge from the generic FTHB profile?)
- **Team** (names, roles, permissions for featuring)

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| VOICE.md sounds too polished / not enough her | Rewrite with more fragments, more her actual phrases; ask her to read a section out loud and record it |
| Registers are unclear (muddled warm/authority) | Run her through the luxury listing test: she saw a $2.5M home — does the VOICE.md register feel different when she talks about it? |
| CTA phrasing is still cheesy or too sales-y | Ask her: "How would you text a friend who asked for a realtor intro?" Start there. |
| Team roster is incomplete | Check whether she wants any team members appearing in content at all — sometimes the answer is "no, just me" and that's the lock |

---

## Stage 2: Demand Research (No Gate; Research Produces Facts)

### What Happens

Input: BRAIN.md market context + specific market/listing address

**Load `/sf-research` workflow from `jen-shortform-carousel-engine`:**
- Google/YouTube search suggestions (LA-specific)
- People-also-ask, Reddit (r/LosAngeles + neighborhood subs)
- Facebook/Nextdoor themes
- LA Times/LAist housing coverage
- Zillow/Redfin trends
- Current-event triggers (rates, insurance, new construction)

**Output: DEMAND-REPORT.md**
- BUYER SEARCHES (5–7 exact phrases, evidence, worry, difficulty)
- SELLER SEARCHES (5–7 same structure)
- RELOCATION SEARCHES (5–7 same)
- **Top 5 QUESTIONS NOBODY IS ANSWERING** (ranked by potential reach + difficulty; include "the worry" in each buyer's voice)
- **PRODUCE FIRST flags** (top 3 items for quick wins; highest reach + lowest difficulty)

### Quality Bar — DEMAND-REPORT.md

Every entry must:
- ✅ **Traceable source:** "Exact phrase observed in X [Reddit thread / YouTube suggestions / Zillow description] on [date]"
- ✅ **Speakable by Jen:** Does the worry sound like a real person's midnight fear, in their voice? (Not your paraphrase of the fear — their actual words)
- ✅ **Ranked by difficulty:** LOW (she can answer in <90s), MED (3–5 min video), HIGH (needs research or expertise)
- ✅ **Zero invention:** If you can't point to where you found it, it doesn't ship

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| Demand sources are light / only one channel | Add 2–3 more channels (Reddit + Nextdoor + LA Times usually fill the gaps) |
| Worry feels like analyst jargon, not a real person's voice | Re-source to find the actual buyer's words; if it's all analyst-speak in the source, find a different topic |
| PRODUCE FIRST flags are too generic ("first-time home buying") | Narrow to specificity: "is $800K enough for SFV?" is more producible than "how do I buy a home?" |
| Difficulty ratings seem off | Ask: how would Jen answer this on a 30s Reel? If she can, it's LOW; if she needs a 2-min explainer, it's MED; if she needs research, it's HIGH |

---

## Stage 3: Video Plan → Gate 2 Approval

### What Happens

Input: DEMAND-REPORT.md + VOICE.md + BRAIN.md

**Load `/sf-plan` workflow from `jen-shortform-carousel-engine`:**
- Convert demand into 4-week, 20-video Production Calendar (Mon–Fri theming)
- Each entry: number + title + demand source + format + hook line + beat outline + CTA + recording note
- Flag ★ VISUAL-worthy ideas (target ≥10 for carousels)
- FILM THESE THREE FIRST batch set
- Batch-filming appendix (group by location for 2–3 shoot sessions)

**Output: PRODUCTION-CALENDAR.md**

### Gate 2 Decision Framework

**Jen approves the Production Calendar** if:

- [ ] **Themes match her voice (VOICE.md):** Does week 1 feel like her teaching-friend energy? Does a luxury-property week feel like her authority POV if she's covering that?
- [ ] **Locations are feasible:** Can she shoot at these locations (her home, a coffee shop, a client's listing, etc.) without added logistics?
- [ ] **Batch filming is realistic:** Can she realistically film 5–6 videos in one afternoon at Location A? (Check: props, wardrobe, setup time)
- [ ] **FILM THESE THREE FIRST are true quick wins:** Can she shoot them tomorrow if needed? (No green-screen, no complex setup, established location)
- [ ] **No fair-housing violations:** Scan for "great for families," "safe neighborhood," school references, demographic descriptors
- [ ] **CTAs rotate naturally:** Are the CTAs varied (comment-keyword, DM, referral ask) or repetitive?

### Quality Bar — PRODUCTION-CALENDAR.md

Must include:
- **4-week structure** with Mon/Wed/Fri themes (strongest hook Monday, educational save Wed, story/timely Fri)
- **20 total videos** (5 per week)
- Each entry contains:
  - Video number + working title
  - Source demand (exact phrase from DEMAND-REPORT.md + the worry)
  - Format (Reel / Story / Carousel-video / Educational / Story-arc)
  - **Hook line written out** (must sound speakable)
  - **Beat outline** (3–5 beats for the narrative)
  - **CTA** (one per entry, rotated across week: comment-keyword / DM / referral / direct ask)
  - **Recording note** (location + props + estimated minutes)
- **★ VISUAL flags** on ≥10 entries (carousel-worthy: can this be 5–7 slides, one idea per slide?)
- **FILM THESE THREE FIRST** with same-day micro-plan (estimated shoot time, location, wardrobe, props)
- **Batch-filming appendix** (reorder by location: all Location A videos grouped together)

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| Calendar feels thin / doesn't have enough hook variety | Revisit DEMAND-REPORT.md; are there other questions that could yield different hook angles? |
| Batch-filming locations seem to overlap too much | Regroup by actual locations she frequents (her office, a local coffee shop, a client listing, her home); logistics win here |
| FILM THESE THREE FIRST are too ambitious | Swap for simpler ones: "me at coffee shop talking about buyers' fears" beats "full property tour with multiple rooms" |
| Fair-housing scan flags language | Rewrite the worry/hook for that entry; what's the real question under the demographic steering? (usually it's about budget, not "safe neighborhood") |
| CTAs are all "DM me" | Vary: Week 1 "comment YOUR biggest fear," Week 2 "DM for free SFV guide," Week 3 "know someone looking to buy? Tag them," Week 4 "save this for later" |

---

## Stage 4: Script Pack (No Gate; Scripts Are Press-Ready)

### What Happens

Input: PRODUCTION-CALENDAR.md + VOICE.md

**Load `/sf-scripts` workflow from `jen-shortform-carousel-engine`:**

For each of the 20 planned videos:
- **(A) 3 hook variants** [pattern-interrupt] / [stakes] / [specificity] — one marked RECOMMENDED
- **(B) Full word-for-word script** (90–150 spoken words, 30–60s)
  - Structure: hook → one-breath context → 3 payoff beats → CTA
  - Written for the mouth with [stage directions]
- **(C) Bullet version** (hook verbatim + 3 beat cues ≤6 words + CTA verbatim)
- **(D) THREE separately optimized captions:**
  - Instagram (hook-first line, 2–4 value lines, comment-keyword CTA, 3–5 hashtags, no walls)
  - TikTok (shorter, question-forward, 2–3 hashtags)
  - YouTube Shorts (keyword-front-loaded searchable title + description with search phrase verbatim + tags)
- **(E) On-screen text plan** (3–5 overlays with timing — assume she's watching muted)
- **Recording run sheet** (all 20 videos in shoot order, call times, props checklist, wardrobe notes)

**Output: SCRIPT-PACK.md**

### Quality Bar — SCRIPT-PACK.md

Each script must pass:
- ✅ **The mouth test:** Read it out loud. Does it sound like Jen speaking, not a teleprompter? (Listen for: natural contractions, pauses, "like," dropped syllables — the real her)
- ✅ **Hook is hooked:** Does it stop the scroll? (Test: would YOU stop on this?)
- ✅ **Beats are payoff-forward:** Does each beat answer something? (Not filler, not repetition)
- ✅ **CTA is her CTA:** Uses phrasing from VOICE.md (not "click the link," not "subscribe")
- ✅ **Fair-housing clean:** Full lint run on spoken + on-screen text (no safe/family/schools, no demographics)
- ✅ **Captions are independently useful:** Can someone read only the IG caption and understand the idea? (Test: would it get a save/share if they never watch the video?)
- ✅ **Recording run sheet is shoot-ready:** A brand-new PA could pick up the sheet and know exactly what to shoot

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| Scripts sound too written / not enough her voice | Rewrite with fragments, more "um/like," more conversational pauses; record yourself reading a section of VOICE.md, then read this script — compare |
| Hooks are good but beats feel empty | Review the source demand (DEMAND-REPORT.md); are you answering the actual worry or just describing the property? |
| Fair-housing lint flags steering language | Common in SFV content: "safe," "great for families," "good schools." Rewrite as housing-stock facts ("built 1985, 2.5 bath, yard") or commute facts ("15 min to DTLA") |
| Captions feel tacked-on to scripts | Write captions FIRST from the hook, then build the script around delivering on that promise |
| Recording run sheet is too vague ("film at coffee shop") | Add: exact location (Coffee Spot on Ventura), wardrobe (the blue blazer from video 3), props (laptop, notes), estimated time (12 min for 3 videos) |

---

## Stage 5: Carousel Specs → Design Brief (Approval Sample Carousel)

### What Happens

Input: SCRIPT-PACK.md + ★ VISUAL flags from PRODUCTION-CALENDAR.md + VOICE.md + brand system

**Load `/sf-carousels` workflow from `jen-shortform-carousel-engine`:**

- Select 10 strongest visual ideas from ★ VISUAL flags (strongest = clearest single visual concept per slide)
- Spec each carousel at 5–7 slides, 1080×1350:
  - Slide 1: HOOK typographic (≤12 words, legible at 150px thumbnail)
  - Middle slides: ONE idea per slide (≤25 words, stats as visual elements not sentences)
  - Final slide: CTA + @realestatewithjing lockup
- Enforce banlist: no stock photos, no emojis, no gradients, no drop shadows, no clip art
- **APPROVAL GATE:** Build ONE sample carousel (choose strongest idea from the 10), get Jen approval, lock visual system

**Output: CAROUSEL-SPECS.md** (portable design brief) + **CAROUSEL-BATCH/** (PNGs/PDFs if built here)

### Approval Sample Decision

**Which carousel should be the sample?**

Pick the entry that:
- ✅ Has the **clearest visual metaphor** (one thing, one idea, one visual)
- ✅ Answers a **high-reach demand question** (from PRODUCE FIRST or top 5)
- ✅ Is **brand-safe** for both registers (doesn't require register-specific tweaks)
- ✅ Uses **existing assets** Jen has (photos from listings, her on-camera, props she owns)

**Sample carousel must show:**
1. Slide 1 (HOOK typographic) — no photo, just type
2. Slide 2 (data/stat as visual) — graph, comparison, numeral (not a sentence)
3. Slide 3 (concept slide) — illustration, diagram, visual metaphor
4. Slide 4 (proof/example) — photo, screenshot, testimonial
5. Slide 5 (CTA) — @realestatewithjing + DM button / comment keyword / link

**Gate Decision:** Jen approves the sample if:
- [ ] The visual metaphor is clear (could someone understand the idea in mute mode, seeing just one slide?)
- [ ] The colors & type match her brand (consistent with what she posts)
- [ ] The CTA feels natural (not cheesy, not sales-y)

### Quality Bar — CAROUSEL-SPECS.md

Each carousel entry must have:
- ✅ **Slide-by-slide breakdown** (title, copy, visual concept for each slide)
- ✅ **Source demand** (which question from DEMAND-REPORT.md does this answer?)
- ✅ **Visual system locked** (font, color palette, grid structure identical across all 10)
- ✅ **Caption pairing** (which script-pack caption goes with this carousel? — for Stage 7 export)
- ✅ **Banlist verified** (no stock photos, no emojis, no gradients, no drop shadows, no clip art)

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| Sample carousel is too cluttered (more than one idea per slide) | Rewrite: what is the ONE thing this carousel teaches? Remove everything else. |
| Slide 1 hook is too long (doesn't read at 150px) | Tighten to ≤12 words. Test: squint at the slide on your phone. Can you read it? |
| Visual metaphor is abstract / not clear | Use a concrete visual concept instead (bar graph, numbered list, side-by-side comparison) |
| CTA feels out of place (doesn't match rest of carousel) | Use CTA from Script Pack that pairs with this carousel; let the script context carry it |
| Colors / fonts don't match her posted content | Check her actual Instagram grid; pull colors/fonts from posts she's made; mirror those exactly |

---

## Stage 6: Design Execution (Render the Batch)

### What Happens

Input: CAROUSEL-SPECS.md (sample locked) + caption pairing list + VOICE.md + brand system

**Render in Claude Design (or Canva):**
- Use locked visual system from sample carousel
- Build siblings, not clones (variations that feel related, not identical)
- Render all 10 carousels to PNGs/PDFs
- Generate Instagram copy for each (from caption pairing list)

**Output: CAROUSEL-BATCH/** (10 PNGs/PDFs) + Instagram captions (text file pairing each carousel to its caption)

### Quality Bar — Final Carousels

Each carousel PNG/PDF must:
- ✅ **Pass mute-mode test:** Could someone understand the idea with sound off? (No text-only explanations)
- ✅ **Be legible on mobile:** Type is ≥18pt for body copy, ≥24pt for headlines, ≥12pt for small print
- ✅ **One visual idea per slide:** No competing graphics or concepts
- ✅ **Consistent visual system:** Fonts, colors, grid structure match the sample carousel exactly
- ✅ **Stats sourced & dated:** If it says "X% of buyers," the source appears on-slide in small print

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| Rendered carousel looks too different from sample | Compare side-by-side with sample; check fonts, colors, alignment, spacing; regenerate this carousel |
| Text is not legible on mobile | Increase font size; reduce words per slide; test by taking a screenshot and viewing on phone at arm's length |
| Visual idea is unclear (too abstract or decorative) | Add a concrete visual element (comparison bar, list, photo, diagram) that explains the idea directly |

---

## Stage 7: Export (Send Package)

### What Happens

Input: All prior stages complete + carousel PDFs + captions + scripts

**Load listing-package workflow from `jen-santulan-listing-content`:**
- If listing-tied: generate send package (hooks + scripts + captions + forwardable text)
- If demand-driven: generate sendable content package (scripts + carousels + captions + posting calendar)

**Output: SEND-PACKAGE.md** (one-click-sendable format for Slack/email)

### SEND-PACKAGE.md Structure

Must include:
- **Listing info** (if applicable): address, MLS #, price, beds/baths, link
- **Quick overview:** "20 videos, 10 carousels, 4-week production plan"
- **FILM THESE THREE FIRST:** The batch-set with shoot time + location + props
- **4-week content calendar:** What posts to Instagram on what days
- **Script pack links:** All 20 scripts (for press-record reference)
- **Carousel PDFs:** All 10 carousel files (downloadable or Google Drive link)
- **Instagram captions:** All captions paired to carousels/videos (copy-paste ready)
- **Posting calendar:** Exact dates + times for maximum reach (typically Tue–Thu 6–9am LA time for real estate)
- **CTAs summary:** Review all CTAs across the package (should be varied, not repetitive)
- **Fair-housing checklist:** "All content screened for demographics, steering, unsafe language — PASS"

### Quality Bar — SEND-PACKAGE.md

Must be:
- ✅ **Forwardable:** Jen can copy-paste to Slack / email and share with her team or post to her scheduling tool
- ✅ **Complete:** Someone brand-new could start shooting from the FILM THESE THREE FIRST section today
- ✅ **Scheduled:** Exact posting times included (not just "post Tuesday")
- ✅ **CTA-reviewed:** Jen has seen all 20 CTAs; they don't feel repetitive or sales-y
- ✅ **Fair-housing clean:** Final audit before ship

### Recovery Patterns

| Issue | Recovery |
|-------|----------|
| Posting calendar is too packed (multiple posts same day) | Space them out across 4 weeks; real estate content works better posted 1x per day |
| Scripts are missing for a few videos | Backfill from SCRIPT-PACK.md; if a video is missing entirely, revisit PRODUCTION-CALENDAR.md |
| Captions feel disconnected from scripts | Review script-to-carousel pairing; captions should preview the script's main idea |
| CTAs are repetitive ("DM for more" 8 times) | Review CTA rotation in PRODUCTION-CALENDAR.md; diversify to comment-keywords, referral asks, saves |

---

## Cross-Stage Patterns & Anti-Patterns

### ✅ DO

- **Trace every claim to a source:** Demand research, demand report entries, carousel stats — all of it should be checkable
- **Write for Jen's mouth:** Scripts, hooks, captions — read them out loud; if you stumble, so will she
- **One idea per slide/video:** A carousel slide should teach ONE thing; a video hook should promise ONE benefit
- **Use her actual language:** Phrases from VOICE.md, not paraphrased versions; keep the specificity
- **Plan the batch-filming upfront:** Don't wait until Stage 7 to realize all 20 videos need different locations

### ❌ DON'T

- Invent demand (just because it feels true doesn't mean a buyer is actually searching for it)
- Blend her two registers (FTHB vs luxury) in the same calendar; separate by property tier
- Write sales-copy (urgency, scarcity, FOMO) — her voice is trust-first, not pressure-driven
- Use generic real-estate language (Jen hates this: "amazing," "beautiful," "breathtaking") — replace with specific details
- Include fair-housing violations (schools, safe neighborhoods, family-friendly, demographics) — lint everything

### 🔄 Recovery Loops

**If Gate 1 rejection (voice/brain not approved):**
- Jen didn't feel represented in VOICE.md? → Re-ask her 2–3 of the voice questions; listen for the new details
- BRAIN.md neighborhoods feel off? → Review her actual past listings; what neighborhoods does she actually work?
- CTA phrasing still feels wrong? → Ask her to write the CTA herself; you transcribe it exactly

**If Gate 2 rejection (calendar not approved):**
- Themes don't match her voice? → Pull the VOICE.md register for each week's theme; rewrite hook lines through that lens
- Filming is unrealistic? → Pick actual locations she frequents; reorder the calendar to batch by location
- Fair-housing language crept in? → Rewrite the worry/hook to focus on housing stock, commute time, or financial programs (HOP80/120, LIPA) instead of demographics

**If output at any stage doesn't match spec:**
- Demand Report missing sources? → Go back to original research channels; find the exact phrase and source
- Scripts don't sound like Jen? → Compare to VOICE.md examples; rewrite shorter, more fragments, more her
- Carousel banlist violations? → Identify the violation (stock photo? emoji? gradient?); replace with system-appropriate visual or remove

---

## Files

- `SKILL.md` — Overview of all 7 stages + 2 gates
- `genius.md` — This file (execution patterns, gate frameworks, quality bars, recovery loops)
- `workflows/01-full-pipeline.md` — Step-by-step walkthrough of running a full jen-engine pipeline
- `references/brain-load-distill-template.md` — Template for turning Jen's intake answers into VOICE.md + BRAIN.md
- `references/gate-1-checklist.md` — Gate 1 approval checklist
- `references/gate-2-checklist.md` — Gate 2 approval checklist
