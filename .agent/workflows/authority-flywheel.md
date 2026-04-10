---
description: Authority Flywheel
---

# /authority-flywheel — The Authority Flywheel Engine

Transform a coach's raw voice memo into a polished newsletter edition + atomized LinkedIn posts through parallel research enrichment, angle development, and creative briefing.

## Usage

```
/authority-flywheel [client-name] [voice-memo-transcript or topic]
/authority-flywheel demo [topic]  — Run on Farrice's own content for proof-of-concept
```

**Examples:**
- `/authority-flywheel coach-marcus` — Process Marcus's latest voice memo into newsletter + posts
- `/authority-flywheel demo "force-velocity profiling"` — Demo run: produce newsletter + posts on this topic
- `/authority-flywheel demo` — Demo run using a raw voice memo or rant from Farrice

---

## The Flywheel (5 Steps — Each Feeds the Next)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   1. CAPTURE ─→ 2. ENRICH ─→ 3. ANGLE ─→ 4. DRAFT ─→ 5. ATOMIZE
│       │                                                 │
│       └─────────── FEEDBACK LOOP ───────────────────────┘
│       (audience response informs next voice memo topic)
└─────────────────────────────────────────────────────────┘
```

**Step 1: CAPTURE** — Coach sends voice memo (5-15 min)
**Step 2: ENRICH** — Parallel research validates, fortifies, and elevates the raw content
**Step 3: ANGLE** — 3-5 unique content angles with mini-briefs
**Step 4: DRAFT** — Newsletter edition (the anchor asset)
**Step 5: ATOMIZE** — Break newsletter into 3-5 LinkedIn posts

---

## Execution

### Step 1: CAPTURE — Voice Memo Intake

**Input:** Raw voice memo transcript, topic rant, coaching session insight, or post-session brain dump.

**Process:**
1. Transcribe (if audio file provided, or accept pasted transcript)
2. Extract the core thesis — what is the coach ACTUALLY saying underneath the ramble?
3. Identify:
   - **Core claim** (the main insight or position)
   - **Supporting evidence** (stories, athlete examples, data points mentioned)
   - **Emotional charge** (what does the coach feel strongly about here?)
   - **Audience trigger** (what would make their ideal client stop scrolling?)
   - **Knowledge gaps** (what's asserted but not backed? what needs research?)
4. If client has a Voice Profile (`_active/clients/[name]/voice-profile.md`), load it

**Output:** Voice Memo Brief — 1-page summary of thesis, evidence, charge, and gaps.

---

### Step 2: ENRICH — Parallel Research Sprint

**This is the moat.** While a normal ghostwriter just rewrites the voice memo, the Authority Flywheel ENRICHES it with real research that makes the coach sound like they read everything.

**Process:**
1. Launch parallel research on 3 dimensions simultaneously:

   **Dimension A — Trending Context:**
   - What's trending in the coach's sport/niche RIGHT NOW?
   - Recent studies, conference talks, viral posts, industry debates
   - Use: `search_web` (primary) + `read_url_content` (for top results) + `mcp_perplexity-ask_perplexity_ask` (budget-gated per `directives/perplexity-usage-policy.md`)

   **Dimension B — Contrarian Validation:**
   - What's the mainstream take on this topic? Where does the coach's position DIFFER?
   - Find the "everyone says X, but actually Y" angle
   - Search for data/examples that support the coach's contrarian position

   **Dimension C — Adjacent Insight:**
   - What related insight from OUTSIDE their domain adds unexpected depth?
   - Cross-pollination: biomechanics insight applied to leadership, psychology research applied to athlete development, business framework applied to coaching
   - This is the "how does this coach know about THAT?" factor

2. Compile into an Enrichment Dossier:
   - 3-5 research nuggets (stats, studies, quotes, trends) that ELEVATE the voice memo
   - 1-2 contrarian angles that sharpen the coach's unique position
   - 1 adjacent insight that adds unexpected depth
   - Flag any claims from the voice memo that need qualification or correction

**Output:** Enrichment Dossier — research backing that makes the coach's raw thought 10x more authoritative.

---

### Step 3: ANGLE — Content Mini-Briefs

**Process:**
1. Combine Voice Memo Brief + Enrichment Dossier
2. Generate 3-5 unique content angles, each a different way to frame the same core insight:

**For each angle, produce a mini-brief:**

```markdown
## Angle [#]: [Title]

**Format:** [Newsletter deep-dive / Hot take / Story-led / Framework breakdown / Before-after case study]
**Hook concept:** [1 sentence — the opening that stops the scroll]
**Thesis:** [1 sentence — what the reader will believe after reading]
**Emotional trigger:** [Recognition / Status threat / Curiosity gap / Competence signal / Relief]
**Proof elements:** [Which research nuggets from the Enrichment Dossier to deploy]
**Estimated strength:** [1-10 — based on hook power + proof density + audience relevance]
```

3. Rank the angles by estimated strength
4. Present to the user for selection (or auto-select top 2 if running in demo mode)

**Output:** 3-5 ranked content angle mini-briefs.

---

### Step 3.5: TWO RULES GATE — Newsletter Flywheel Validation

**Before drafting, validate the newsletter concept against Cole's Two Rules.**

**Process:**
1. Load: `skills/nicolas-cole-newsletter-flywheel/genius.md` (Two Rules, Tangible Faucet)
2. Run the Two Rules gate on the planned newsletter edition:
   - **Rule 1**: Is this edition a chapter in a book the reader wishes never ended?
   - **Rule 2**: Does this edition deliver a tangible, saveable, shareable ASSET (not just an essay)?
3. Run the Wine Club Test: "It's like a _____ club but for _____." If the blank can't be filled → the edition needs a tangible component.
4. If either rule fails → redesign the edition angle to include a tangible deliverable (checklist, template, framework, prompt) alongside the narrative content.

**This prevents the authority flywheel from producing essay-only newsletters that miss Cole's retention architecture.**

---

### Step 4: DRAFT — Newsletter Edition (The Anchor Asset)

**This is the core deliverable.** The newsletter is the OWNED asset. Everything else is derived from it.

**Process:**
1. Load expert skills:
   - Read `skills/ghostwriting-voice-engine/genius.md` (voice matching)
   - Read `skills/lara-acosta-content-system/SKILL.md` (content architecture)
   - Read `skills/kallaway-content-psychology/SKILL.md` (hook psychology + engagement)
   - If proof-heavy angle: Read `skills/luke-iha-proof-ladder/genius.md` (proof weaving)

2. Draft the newsletter edition using the selected angle:
   - **Length:** 800-1,200 words
   - **Structure:** Hook → Setup → Core insight → Supporting evidence (from enrichment) → Application → Open loop to next edition
   - **Voice:** Must match the coach's voice profile (if exists) or Farrice's voice (for demos)
   - **Proof weaving:** Research nuggets woven into narrative momentum, not inserted as footnotes
   - **"Country Club" aesthetic:** Sophisticated vocabulary, clean structure, data-driven credibility

3. Run quality checks:
   - [ ] Does the opening hook create a curiosity gap or recognition moment?
   - [ ] Is the enrichment research WOVEN into the narrative (not bolted on)?
   - [ ] Would the coach say "this sounds like me on my sharpest day"?
   - [ ] Is there an open loop that makes the reader want the next edition?
   - [ ] Does this demonstrate the coach's expertise WITHOUT being a lecture?

**Output:** Newsletter edition (800-1,200 words), ready for Beehiiv/Substack/ConvertKit.

---

### Step 5: ATOMIZE — LinkedIn Post Breakdown

**Process:**
1. Load expert skills:
   - Read `skills/lara-acosta-linkedin-mastery/SKILL.md` (LinkedIn optimization)
   - Read `skills/kallaway-content-psychology/SKILL.md` (scroll-stopping hooks)

2. Break the newsletter into 3-5 LinkedIn posts:

   **Post Type A — The Hook Post (from the opening):**
   - Extract the newsletter's strongest hook
   - Expand into a standalone post (200-300 words)
   - End with engagement prompt (question, poll, or "what would you do?")

   **Post Type B — The Framework Post (from the core insight):**
   - Distill the main insight into a numbered framework or listicle
   - 150-250 words, high scannability
   - End with "save this" or "share with a coach who needs to hear this"

   **Post Type C — The Story Post (from a supporting example):**
   - Pull out one story or case study from the newsletter
   - Tell it as a standalone micro-narrative (200-350 words)
   - End with the lesson, not a pitch

   **Post Type D — The Hot Take (from the contrarian angle):**
   - Lead with the controversial position
   - 100-200 words, punchy, direct
   - End with "agree or disagree?" to drive comments

   **Post Type E — The Proof Post (from the enrichment data):**
   - Lead with a surprising stat or research finding
   - Connect it to the coach's methodology
   - 150-250 words, authority-building

3. For each post:
   - Optimize for LinkedIn algorithm (no external links in body, 3 hashtags max, hook above the fold)
   - Include scheduling note (which day of the week, what time slot)
   - Run voice authenticity check if Voice Profile exists

**Output:** 3-5 LinkedIn posts with scheduling recommendations.

---

## Output Package (Complete Deliverable)

```markdown
# Authority Flywheel Output — [Client/Topic] — [Date]

## Voice Memo Brief
[Core thesis, evidence, emotional charge, knowledge gaps]

## Enrichment Dossier
[Research nuggets, contrarian angles, adjacent insights]

## Content Angles (Ranked)
[3-5 mini-briefs with hook, thesis, trigger, proof elements]

## Newsletter Edition
[800-1,200 word newsletter, ready to publish]

## LinkedIn Posts (3-5)
[Each post with format label, word count, scheduling recommendation]

## Publishing Calendar
| Asset | Platform | Publish Date | Status |
|-------|----------|-------------|--------|
| Newsletter | Beehiiv/Substack | [Day] | Draft |
| Post A (Hook) | LinkedIn | [Day + 1] | Draft |
| Post B (Framework) | LinkedIn | [Day + 3] | Draft |
| Post C (Story) | LinkedIn | [Day + 5] | Draft |
| Post D (Hot Take) | LinkedIn | [Day + 7] | Draft |
```

---

## Demo Mode

When running `/authority-flywheel demo [topic]`:
- Use Farrice's voice and S&C expertise
- Topic can be raw (a rant about why coaches don't post) or specific (force-velocity profiling for the uninitiated)
- Output serves dual purpose: (1) proof of concept for outreach, (2) portfolio piece
- Save demos to `_active/demos/flywheel/[topic-slug]/`
- Each demo IS the sales pitch — "this is what your content system produces every week"

---

## Client Mode

When running `/authority-flywheel [client-name]`:
1. Check for Voice Profile: `_active/clients/[client-name]/voice-profile.md`
2. If no profile: "No Voice Profile found. Run `/ghostwrite capture [client-name]` first, or provide a voice memo and I'll work from raw input."
3. If profile exists: load it as the voice constraint for Steps 4-5
4. Save output to `_active/clients/[client-name]/flywheel/[date]/`

---

## Dependencies

| Asset | Path | Required By |
|-------|------|-------------|
| Cole Newsletter Genius | `skills/nicolas-cole-newsletter-flywheel/genius.md` | Step 3.5 (Two Rules gate) |
| GVE Genius | `skills/ghostwriting-voice-engine/genius.md` | Step 4 (voice matching) |
| Lara Acosta Content | `skills/lara-acosta-content-system/SKILL.md` | Steps 4-5 (content architecture) |
| Kallaway Psychology | `skills/kallaway-content-psychology/SKILL.md` | Steps 4-5 (hook + engagement) |
| Luke Iha Proof Ladder | `skills/luke-iha-proof-ladder/genius.md` | Step 4 (proof weaving, when applicable) |
| Lara LinkedIn Mastery | `skills/lara-acosta-linkedin-mastery/SKILL.md` | Step 5 (LinkedIn optimization) |
| Perplexity Budget | `directives/perplexity-usage-policy.md` | Step 2 (research, budget-gated) |

---

## Chain Compatibility

- **Standalone**: Run on any voice memo or topic
- **Feeds from**: `/ghostwrite capture` (voice profile) → `/authority-flywheel` (production)
- **Feeds into**: Newsletter platform (Beehiiv/Substack) + LinkedIn scheduling (Buffer/Taplio)
- **Demo → Outreach**: `/authority-flywheel demo` → package as proof of concept → DM prospects

---

## The Flywheel Logic (Why This Compounds)

```
Week 1: Coach sends voice memo → You produce newsletter + 3 posts
Week 2: Posts generate engagement → You see what resonates → Next voice memo is sharper
Week 3: Newsletter subscribers grow → More data on what audience wants
Week 4: Coach gets first DM from content → PROOF the system works → Retention locked
Month 2: Voice memo quality improves (coach thinks in "content moments") → Output quality rises
Month 3: Coach has a media entity → Reduces in-person hours → Attributes to the flywheel
```

Each cycle makes the next cycle better. The coach's voice memos get sharper. The research gets more targeted. The audience grows. The proof compounds. This is not a content calendar — it's a momentum machine.

---

## Quality Gate

- [ ] Voice memo brief captures the REAL thesis (not just the surface topic)?
- [ ] Enrichment research genuinely ELEVATES the content (not filler)?
- [ ] Content angles offer meaningfully different approaches (not slight variations)?
- [ ] Newsletter would make the coach say "I wish I'd written this"?
- [ ] LinkedIn posts are standalone pieces (not just excerpts)?
- [ ] Each post has a specific hook optimized for the feed?
- [ ] The output package could be used as a demo for prospect outreach?
