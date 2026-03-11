# Content Sprint Workflow

> **Invocation**: `/content-sprint` | `@content-sprint` | "run content-sprint"
> **Purpose**: Take Farrice from zero to publication-ready LinkedIn post + lead magnet concept in 30 minutes of his time.
> **When**: Whenever Farrice wants to create a new piece of content. This is the default content creation workflow.

---

## Prerequisites

- Farrice available for ~30 minutes (two touchpoints: topic selection + final edit)
- Voice captures loaded at `_active/linkedin-launch/voice-captures/` for tone reference
- ICP context: `_active/linkedin-launch/service-architecture.md`

---

## Quick Start

```
/content-sprint                    # Full workflow — research → draft → edit
/content-sprint --quick            # Skip research — Farrice already has topic
/content-sprint --serial           # Chapter in ongoing arc (loads Fresh Voice System)
/content-sprint --quick --serial   # Both: known topic + serial chapter
```

---

## The Mission (Read This First)

Farrice is the guru's guru. He helps brilliant, invisible experts — coaches, consultants, service professionals, founders — translate their genius into visibility so they can make the impact they're supposed to make.

Every post must make readers think: **"I never thought about it like that before."**

The goal is mind-shift. Genuine insight that shifts perspective. Through that, trust and authority flow naturally. Revenue is a byproduct of transformation, not a target per post.

His profile IS the proof of concept. The content demonstrates the service by being the service.

---

## Phase 1: Intake (2 min Farrice time)

Ask Farrice ONE question:

> "What's on your mind? Give me a topic, an angle, a rant, a question from a client — anything. Or say 'surprise me' and I'll bring you options."

**If `--quick` flag**: Skip to Phase 3. Farrice already has his topic.

**Capture**:
- Topic/angle (if provided)
- Any raw context (client story, observation, frustration)
- Format preference if stated (text post, carousel outline, narrative)

---

## Phase 2: Topic Menu (0 min Farrice time — AI parallel research)

> Skip this phase if `--quick` flag is set or Farrice already provided a specific topic.

### Research Stack (run in parallel):

1. **Trending signals** — Use WebSearch to scan:
   - LinkedIn trending topics in ghostwriting, content strategy, personal branding
   - Recent posts getting traction from competitors/adjacent creators
   - Industry news affecting Farrice's ICP (consultants, coaches, founders losing to visibility)

2. **ICP pain point cross-reference** — Load:
   - `_active/linkedin-launch/service-architecture.md` (ICP profile + pain points)
   - `_active/linkedin-launch/mini-briefs/concept-dossier.md` (13 validated concept seeds)

3. **Gap check** — Scan `_active/linkedin-launch/arcs/` to avoid repeating recent topics.

### Output: Present 5 topics as a numbered menu:

```
TOPIC MENU — Pick one (or give me yours):

1. [Topic] — [Angle in 8 words] — [Why now: 1 sentence]
2. [Topic] — [Angle] — [Why now]
3. [Topic] — [Angle] — [Why now]
4. [Topic] — [Angle] — [Why now]
5. [Topic] — [Angle] — [Why now]

Or: "None of these. Here's what I'm thinking: ___"
```

**Wait for Farrice to pick or provide his own.**

---

## Phase 3: Raw Take (5-10 min Farrice time)

Once topic is selected, prompt Farrice:

> "Give me your raw take on this. Don't edit yourself. Stream of consciousness, bullet points, voice note transcript — whatever comes out. What do you actually think about this? What would you say to a client sitting across from you asking about this?"

**Capture everything.** This is the "ethos seed" — the authentic perspective that makes the post HIS, not generic content.

**If Farrice gives bullets**: Great. That's the skeleton.
**If Farrice gives a rant**: Even better. Extract the 2-3 core convictions.
**If Farrice gives a story**: Best case. Build the post around it.

---

## Phase 4: Expert Draft (0 min Farrice time — AI work)

### Load expert stack based on content type:

**For LinkedIn text posts (default)**:
- `skills/lara-acosta-linkedin-mastery/genius.md` — F-shape structure, mobile cutoff hooks, engagement architecture
- `skills/nicolas-cole-sentence-craft/genius.md` — Terminal word power, compression, 4th-grade vocabulary anchoring

**Add if `--serial` flag**:
- `skills/fresh-voice-system/genius.md` — Serial narrative standard, open loops, chapter continuity

**For narrative/story-driven posts**:
- `skills/mitch-albom-writing-mastery/genius.md` — Theme-first, tight cut, first/last marriage
- `skills/jonathan-franzen-storytelling/genius.md` — Minimal detail maximum impact, want-collision

**Always load for emotional/psychological layer** (applied in Phase 5 but inform drafting):
- `skills/erica-mallet-brand-magnetism/genius.md` — Enemy Effect, belief architecture, tribal belonging
- `skills/joanna-wiebe-persuasion-mastery/genius.md` — Authority craft, bucket brigades, anti-hype
- `skills/robert-mack-comedy-writing/genius.md` — Tension-relief, vivid specificity, comedy beats

### Build the draft:

1. **Start with Farrice's raw take** — his words, his perspective, his stories
2. **Apply expert structural patterns** — F-shape, hook architecture, section breaks
3. **Identify the enemy** (Erica) — what force does this piece fight? Build the narrative around it.
4. **Plant the belief** (Erica) — what should readers believe after reading? Package it in story, not statements.
3. **Format for LinkedIn** — single/double line breaks, mobile-first, short paragraphs
4. **Reference voice captures** from `_active/linkedin-launch/voice-captures/` — match his actual speaking patterns, not a template voice

### Voice calibration:
- Warm, direct, coaching-conversation tone
- Psychology-first: the insight IS the post
- Specific over general — real numbers, real scenarios, real consequences
- No corporate, no guru, no motivational speaker

---

## Phase 5: Writers' Room + Anti-Slop Filter (0 min Farrice time — AI work)

### Run `/writers-room` treatment (6 experts, 2 layers):

Execute the full writers' room workflow (`.agent/workflows/writers-room.md`):

**Layer 1 — Structure & Compression** (runs first):
- **Mitch Albom** — Theme-first, tight cut, uncle vs aunt, first/last marriage
- **Jonathan Franzen** — Minimal detail maximum impact, trust the reader
- **Nicolas Cole** — Terminal word power, three-pass compression, opening sentence power

**Layer 2 — Emotion, Psychology & Entertainment** (runs second, on the compressed draft):
- **Erica Mallet** — Enemy Effect, belief architecture, vegetable-in-cake packaging, tribal belonging
- **Joanna Wiebe** — Authority craft, stealing thunder, anti-hype engine, bucket brigades, catchy phrasing
- **Robert Mack** — Tension-relief architecture, skewed perspective, vivid specificity, naming mastery, comedy beats

**Process**: Diagnose (12 questions) → Layer 1: Compress (target 40-50%) → Layer 2: Inject (tension, wit, belief, authority) → Validate (14-point checklist)

### Anti-AI-Slop Filter (MANDATORY — run on every draft)

**Banned phrases** (search and destroy):
- "Let's dive in" / "Let's unpack this" / "Here's the thing"
- "In today's fast-paced..." / "In an era of..."
- "Game-changer" / "Transformative" / "Innovative" / "Cutting-edge"
- "I'm thrilled/delighted/excited to share"
- "Let's have an honest conversation about..."
- "What are your thoughts?" (as a generic closer)
- "Masterclass in..." / "Deep dive into..."
- "Stakeholder" / "Ecosystem" / "Synergy" / "Paradigm"
- "Crushing it" / "Rockstar" / "Purpose-driven"
- "Moreover" / "Furthermore" / "In addition" / "It's worth noting"
- "Leverage" / "Optimize" / "Navigate" / "Landscape"
- "Delve" / "Tapestry" / "Nuance" (as filler)

**Banned structural patterns**:
- Green checkmark emoji (✅) bullet lists
- "It's not X. It's Y." repeated as structural device (once is fine, pattern is AI tell)
- Life events reframed as generic business lessons
- Numbered lists of "lessons learned" without specific stories
- Engagement bait CTAs ("Comment YES if you agree" / "Like for part 2")
- Excessive em-dashes (1-2 per post max)
- Hashtag spam (3 max, relevant only)
- Every sentence balanced and polished (real writing has texture and imperfection)
- Calm, balanced, remarkably earnest cadence throughout (AI's default tone)

**Required anti-slop markers** (must be present):
- [ ] At least one detail so specific it couldn't be fabricated
- [ ] An opinion that could alienate someone (real point of view)
- [ ] Vocabulary that matches Farrice's actual speaking voice
- [ ] Emotional texture beyond "inspired/grateful/humbled"
- [ ] Imperfect sentence structure somewhere (not every line a polished gem)

**The screenshot test**: If someone screenshot this post and said "this is AI" — could they make a case? If yes, it fails. Rewrite until the answer is no.

---

## Phase 6: Voice Pass + Farrice Edit (10-15 min Farrice time)

Present the treated draft to Farrice with:

1. **The draft** (ready to paste into LinkedIn)
2. **Change notes**: What was built from his raw take, what expert patterns were applied, what was cut
3. **Anti-slop report**: Confirm all banned phrases eliminated, all required markers present
4. **One flag**: If there's a weak spot you see but kept, call it out

**Farrice reads, edits for voice authenticity, approves or requests adjustments.**

One revision round max. If major issues, diagnose what's wrong and apply targeted fixes — don't start over.

---

## Phase 7: Lead Magnet + Publish Prep (0 min Farrice time — AI work)

### Generate lead magnet concept

Using Stockton Walbeck's taxonomy (`skills/stockton-walbeck-lead-magnets/genius.md`):

| Type | What it does | Example |
|------|-------------|---------|
| **Clarifier** | Helps them understand where they are | "The Invisible Expert Diagnostic: 5 questions that reveal your visibility gap" |
| **Sampler** | Gives a taste of your methodology | "3 Translation Exercises: Turn your best client conversation into a LinkedIn post" |
| **Starter** | Gets them started on the transformation | "The Expert's First 5 Posts: A framework for going from ghost to visible" |
| **Shortcut** | Saves them time on something tedious | "The LinkedIn Profile Rewrite Template for Experts Who Hate Writing About Themselves" |

Pick the type that connects most naturally to the post's topic. Provide:
- Title
- Format (PDF, Notion template, video, email sequence)
- 3-bullet description
- Which service tier it leads to (Proof Run $500-750, The Voice $2,500/mo, The Engine $3,500/mo)

### Save and log

1. Save post to `_active/linkedin-launch/arcs/[appropriate-arc]/[post-name].md`
2. Save lead magnet concept to `_active/linkedin-launch/lead-magnets/[name].md`
3. Log sprint performance:
   ```bash
   python execution/log_performance.py log "Content Sprint: [topic]" --skill content-sprint --type linkedin-post --quality [SCORE] --status Keep
   ```

---

## Serial Narrative Mode (`--serial`)

When the `--serial` flag is set, also load:
- `skills/fresh-voice-system/genius.md` — Serial narrative standard
- Current arc files from `_active/linkedin-launch/arcs/[current-arc]/`

Additional rules:
- Include an open loop that pulls readers into the next chapter
- Reference previous chapters naturally (callbacks, not recaps)
- No CTA on serial chapters — the open loop IS the engagement mechanism
- Maintain character/theme continuity across the arc

---

## Time Budget

| Phase | Farrice time | AI time |
|-------|-------------|---------|
| 1. Intake | 2 min | — |
| 2. Topic Menu | — | 3-5 min |
| 3. Raw Take | 5-10 min | — |
| 4. Expert Draft | — | 3-5 min |
| 5. Writers' Room + Anti-Slop | — | 3-5 min |
| 6. Voice Pass + Edit | 10-15 min | 2-3 min |
| 7. Lead Magnet + Save | — | 2-3 min |
| **Total** | **17-27 min** | **13-21 min** |

---

## Expert Pairing Reference

For quick reference when selecting expert stacks in Phase 4:

| Content Type | Primary Experts | Add-ons |
|-------------|----------------|---------|
| LinkedIn text post | Lara Acosta + Nicolas Cole | — |
| Narrative/story post | Mitch Albom + Franzen | — |
| Serial chapter | + Fresh Voice System | Arc files |
| Carousel outline | Lara Acosta + Cole | Visual structure |
| Sales/conversion | Cardinal Mason or Jeremy Miner | Conversion architecture |
| Voice authenticity | Load `FARRICE.md` + voice captures | — |

---

## What This Workflow Does NOT Do

- **Write without Farrice's perspective.** Every post starts from his raw take. No take = no post.
- **Merge with existing workflows.** This invokes `/writers-room`, references skill genius files, and uses existing tools — but the pipeline is its own thing.
- **Optimize for vanity metrics.** No engagement bait, no "hack the algorithm" tactics. Transformation drives trust. Trust drives reach.
- **Hide AI usage.** Farrice is transparent about his process. But the content must pass the screenshot test — indistinguishable from a human who lived it, because a human DID live it. The AI translates; it doesn't fabricate.

---

*Created: 2026-03-10*
*Origin: Farrice's vision for a 30-minute content pipeline — editing, not writing*
