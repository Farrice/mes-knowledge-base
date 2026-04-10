---
description: Produce Parallax Substack editions — trending research, briefing, drafting, prompt packs, LinkedIn cross-promo. Full pipeline from zero to publish-ready.
---

# `/parallax` — The Parallax Production Engine (v1.0)

Produces publish-ready Substack editions for Parallax at will. Each run: trending topic research, Farrice briefing, edition drafting with expert stacks, prompt pack engineering, and LinkedIn cross-promotion assets.

## Quick Start

```
/parallax                          # Full pipeline — research → brief → draft → publish-ready
/parallax --topic "AI emotions"    # Skip research — Farrice already has a topic
/parallax --batch 3                # Produce 3 editions in one session
/parallax --quick                  # Skip research + briefing — Farrice provides raw take directly
```

---

## What This Produces (Per Edition)

1. **The Edition** — 800-1200 word essay, Parallax voice, anti-slop certified
2. **The Prompt Pack** — Single-prompt coaching session (Nate B. Jones / IP Flywheel standard)
3. **3 LinkedIn Posts** — Insight variant, prompt teaser, output screenshot concept
4. **Substack Notes** — 2-3 Notes per edition for platform discovery

---

## The Publication: Parallax

- **Name**: Parallax — "For people who see everything from more than one angle."
- **Author**: Farrice "Fresh" Cain
- **Audience**: Multi-passionate people, polymaths, nerds, gamers, fitness people
- **Core thesis**: Your interests aren't scattered. They're ingredients. Nobody told you the recipe yet.
- **Format**: Essay + prompt pack per edition. The essay creates the insight. The prompt pack creates the transformation.

---

## Phase 1: RESEARCH (Skip with `--topic` or `--quick`)

**Time**: 5-10 min (AI only, no Farrice time)

Scan the current zeitgeist for brandjack opportunities:

1. Deploy Perplexity (check budget at `.agent/perplexity-usage.json` first):
   - "trending topics [current week] personal development technology culture"
   - "what's viral on Substack this week"
   - "creator economy solopreneur news this week"
   - Any domain-specific trends (AI, gaming, fitness, spirituality, parenting)

2. Scan Substack trending, LinkedIn solopreneur/creator conversations

3. For each topic found, score on:
   - **Existing attention** (High/Medium/Low): Is there a conversation to jack?
   - **Polymath angle**: Can Farrice connect this to 2+ of his interest domains in a way nobody else is?
   - **Prompt pack potential**: What micro-transformation pairs with this topic?

4. Present **5-8 trending topics** as a concise briefing to Farrice:

```
TOPIC: [Name]
Why it's trending: [1-2 sentences]
The Parallax angle: [How Farrice uniquely sees this]
Prompt pack concept: [What the coaching session would do]
Brandjack potential: [High/Medium/Low]
```

**HALT. Wait for Farrice to select a topic (or topics if `--batch`).**

---

## Phase 2: BRIEFING + RAW TAKE (Skip with `--quick`)

**Time**: 5-10 min Farrice time

Once Farrice selects a topic:

1. Present a **concise but nuanced briefing** on the selected topic:
   - Key facts, data points, quotes worth referencing
   - What the mainstream conversation is saying
   - The angles nobody is taking (the Parallax opportunity)
   - Which of Farrice's interest domains intersect with this topic
   - Suggested edition arc position (Identity / Pain / Depth / Power / Permission)

2. Ask Farrice: **"What's your take? What do you want to say about this that nobody else is saying?"**

3. Capture his raw take (voice note, bullets, stream of consciousness — all valid)

**HALT. Wait for Farrice's raw take before drafting.**

---

## Phase 3: DRAFT THE EDITION

**Time**: 10-15 min (AI), 5-10 min Farrice review

### Expert Loading

Load based on topic domain (check Hot Context first):
- **Default stack**: Nicolas Cole (sentence craft) + Kallaway (dopamine ladder, hooks)
- **If AI/tech topic**: + Seth Godin (category creation)
- **If inner work/psychology**: + Steven Pressfield (narrative physics)
- **If gaming/anime**: Deploy tribal vocabulary from FARRICE.md
- **If spirituality**: Deploy Neville Goddard / Joe Dispenza frameworks from FARRICE.md
- **If fitness**: Deploy training science from Farrice's 18 years

### Drafting Rules

Read and enforce ALL of these:

**Voice DNA** (from FARRICE.md + memory):
- Show, never tell. Specific over general. Earned authority, not claimed.
- No guru energy. "What I discovered" not "what you should do"
- Comedy beats after heavy insights
- Imperfection IS the voice — not every sentence polished

**Anti-Slop Filter** (MANDATORY):
- Banned phrases: "Let's dive in," "game-changer," "transformative," "innovative," "moreover," "furthermore," "delve," "tapestry," "nuance" (as filler), "In today's fast-paced"
- Banned lead-ins: "Here's what happens when," "Because here's what nobody tells you about," any "Here's what/why/how..." paragraph opener, "Here's where..."
- Banned structural patterns: Green checkmark lists, "It's not X. It's Y." repeated, calm/balanced/earnest throughout
- Required markers: specific detail that couldn't be fabricated, opinion that could alienate, imperfect sentence structure, vocabulary matching Farrice's speaking voice

**AI Tell Prevention** (from memory/feedback_ai-writing-tells.md + feedback_writing-excellence-rules.md):
- Em dashes: max 1-2 per entire edition. Farrice doesn't use them naturally.
- Bridge phrases: NEVER repeat the same bridge across editions. Vary every time.
- Jargon: any technical term max 2-3 uses per edition, then switch to plain language
- Cross-edition trope audit: if producing multiple editions, search for repeated structures

**Quality Standards**:
- Hook grips cold readers immediately (standalone excellence — each piece works alone)
- Every word pulls its weight — no dead space, no drag
- Tightness pass before delivery — if a paragraph works in 2 sentences, cut to 2

### Edition Structure

```
Subject line: [6-10 words, curiosity-driven]
Preview text: [1 sentence complement]

[ESSAY — 800-1200 words]
- Opening: hook that creates tension requiring resolution
- Body: one core idea explored with depth, 2-3 sections
- Bridge: connect insight to reader's situation
- Prompt pack introduction: 2-3 sentences, links to pack
- Close: tease next edition + CTA (rotate: reply, share, forward)

Footer:
Written by Farrice Cain
Parallax — see everything from more than one angle.
```

### Delivery

Present draft to Farrice with:
1. The draft (ready to paste into Substack)
2. Anti-slop report: banned phrases eliminated, required markers present
3. Voice note: any lines rewritten for voice + why

**HALT. Wait for Farrice's approval or edits.**

---

## Phase 4: ENGINEER THE PROMPT PACK

**Time**: 10 min (AI)

### The Standard (IP Flywheel / Nate B. Jones quality)

Each prompt pack is a **single prompt** that runs a complete coaching session:

1. **Expert role**: AI given specific methodology, not generic advice
2. **Phase 1 — Excavation**: 2-3 questions asked one at a time (user just answers honestly)
3. **Phase 2 — Analysis**: AI does all pattern recognition and insight generation itself
4. **Output**: Structured, actionable, screenshot-worthy — clear headers, specific deliverables

### Prompt Pack Architecture

```
Expert Role: [Specific to this edition's domain — not generic]
Methodology: [Embed Farrice's actual coaching frameworks, not surface-level self-assessment]
Excavation Questions (3, asked sequentially):
  1. [Experiential question — describe a moment, not a category]
  2. [Probing question — goes deeper into what they revealed]
  3. [Contrast question — reveals the gap between current and ideal state]
Analysis Output (AI produces all of this):
  A. [Diagnostic map of current state]
  B. [Pattern identification — what they can't see about themselves]
  C. [Specific action architecture — not advice, a SYSTEM]
  D. [One thing to do tonight/tomorrow]
```

### Quality Gate for Prompt Packs

Every pack must pass:
1. **The Zero-Knowledge Test**: Would someone with NO AI experience get a transformational result?
2. **The Coaching Test**: Does this prompt do what Farrice would do in a 30-min coaching session?
3. **The Screenshot Test**: Is the output structured enough that someone would screenshot and share it?
4. **The Reuse Test**: Would they run this again in 3 months and get different, valuable results?

### File Format

Write to: `_active/farrice-brand/content/prompt-packs/[XX]-[slug].md`
Structure: Title + metadata → "How This Works" → The Prompt (code block) → "What to Expect" → "Commentary" → "Advanced Variation"

---

## Phase 5: GENERATE CROSS-PROMOTION ASSETS

**Time**: 5 min (AI)

For each edition, produce 3 LinkedIn post variants:

### Variant A: The Insight Post
Extract the core insight from the edition. Reframe for LinkedIn's broader audience. End with: "I broke this down deeper in my newsletter — link in first comment."

### Variant B: The Prompt Teaser
Show a preview of what the prompt pack does (not the full prompt). Describe the transformation: "I built a prompt that [does X]. Here's what happened when I ran it..." CTA: "Get the full prompt pack — link in first comment."

### Variant C: The Output Screenshot Concept
Describe what a screenshot of the prompt output would look like. Include the hook: "I ran this prompt and here's what came back..." (For actual posting, Farrice runs the prompt himself and screenshots the real output.)

### Also produce:
- 2-3 Substack Notes using tribal vocabulary ("Course graveyard" observations, "training arc" reflections, "alignment gap" insights — drawn from this edition's theme)

Write to: `_active/farrice-brand/content/linkedin-posts/parallax-[edition-number]/`

---

## Phase 6: FINALIZE

Run the chain finalization:

```bash
python3 execution/chain_runner.py finalize "Parallax Edition [X]: [title]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow parallax \
    --type Content \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "[what worked, what the edition covers]"
```

---

## Reference Files

**Voice & Standards**:
- `FARRICE.md` — identity, interests, tribal vocabulary, avatar, voice
- `memory/feedback_ai-writing-tells.md` — banned AI patterns (em dashes, lead-ins)
- `memory/feedback_writing-excellence-rules.md` — hooks, jargon, tightness, trope variance
- `memory/content-voice-calibration.md` — full voice rules

**Expert Skills** (load as needed):
- `skills/nicolas-cole-newsletter-flywheel/` — newsletter architecture, prompt-as-product
- `skills/kallaway-content-psychology/` — dopamine ladder, hooks, C.A.P. Fit
- `skills/steven-pressfield-narrative-mastery/` — manifesto engine, narrative physics
- `skills/seth-godin-ideavirus/` — virusworthiness, SVA, sneezer strategy

**Existing Editions** (for cross-edition trope audit):
- `_active/farrice-brand/content/substack-v2-drafts/` — all published editions
- `_active/farrice-brand/content/prompt-packs/` — all published prompt packs

**Strategy**:
- `_active/farrice-brand/content/substack-v2-strategy.md` — publication setup, growth tactics
- `research_outputs/substack-brandjack-trends-april-2026.md` — initial trending report

---

## Batch Mode (`--batch N`)

When producing multiple editions:
1. Run Phase 1 research ONCE, present all topics
2. Farrice selects N topics and gives raw takes for each
3. Draft all N editions, running cross-edition trope audit
4. Engineer N prompt packs
5. Generate N x 3 LinkedIn posts
6. Finalize all at once

This is the one-man-army mode. Research once, produce at scale.
