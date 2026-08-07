# Coach Cooz Authority Flywheel — Workflow SOP
## The Weekly Operational Engine | April 2026

> **What this is**: The end-to-end workflow that turns Cooz's raw voice memos into polished, multi-channel content that hits a 9/10 quality bar. This document is for FARRICE — it's the operator manual.
>
> **What Cooz sees**: A weekly creative brief he records against, then polished content delivered back to him.
> **What Farrice runs**: This workflow.

---

## The Core Insight

Pre-generating content for Cooz failed for the same reason his Gemini deep research failed: **we were guessing what he should say instead of capturing what he actually thinks.**

The flywheel only works when fueled by his raw voice. Everything else is speculation. The job of this workflow is to:
1. **Make recording effortless** for him (give him a brief, not a blank page)
2. **Make production effortless** for us (the agent swarm handles transcription → translation → atomization)
3. **Make posting effortless** for him (output is 90% ready, he does final 10%)

---

## The 5-Phase Weekly Cycle

```
PHASE 1: CREATIVE BRIEF       (Sun/Mon — Farrice, 30 min + 1 agent run)
   ↓
PHASE 2: VOICE MEMO CAPTURE   (Mon/Tue — Cooz, 20 min)
   ↓
PHASE 3: FLYWHEEL PROCESSING  (Tue/Wed — Farrice + agents, 1-2 hours)
   ↓
PHASE 4: 4-CHANNEL OUTPUT     (Wed — Farrice delivers to Cooz)
   ↓
PHASE 5: COOZ EDITS + POSTS   (Wed-Sun — Cooz, ~30 min total)
```

---

## PHASE 1: Creative Brief Generation

**Owner**: Farrice (with research agent assist)
**When**: Sunday evening or Monday morning
**Time**: 30 min orchestration + 1 background agent run (~10 min)
**Output**: `week-N-creative-brief.md` delivered to Cooz

### Step 1.1 — Launch the Trending Research Agent

Run a background agent that scrapes:

| Source | What | Tool |
|--------|------|------|
| **Reddit** | Founder/entrepreneur posts in last 7 days touching burnout, body, family, mental health | `apify_client.py reddit` |
| **Instagram** | Top 5 recent posts from Sheedy, Dan Go, Soraya Zidane (engagement data) | `apify_client.py instagram` |
| **Web search** | Cultural moments this week — tech news, viral discussions, TV/entertainment that touches the founder psyche | WebSearch |
| **YouTube** | Top performing "founder health" / "executive burnout" videos last 7 days | `apify_client.py youtube` |

**Budget**: ~$0.30 per weekly run. ~$1.20/month total Apify spend for the flywheel — well under cap.

### Step 1.2 — The Brief Format (Send This to Cooz)

```markdown
# Creative Brief — Week of [Date]
## For: Coach Cooz | From: Farrice

## What's hot in your ICP's world this week (3 topics)
1. [Trending topic + 1-sentence why it matters + angle]
2. [Trending topic + 1-sentence why it matters + angle]  
3. [Trending topic + 1-sentence why it matters + angle]

## What's working from your competitors (2-3 examples)
- **Sheedy** posted [verbatim hook] — got [engagement]. Why it worked: [pattern]
- **Dan Go** posted [verbatim hook] — got [engagement]. Why it worked: [pattern]

## 3 voice memo questions (pick one)
**Question A**: [specific prompt]
- Why this now: [trending context]
- Sub-prompts: [3 things to talk about]

**Question B**: [...]
**Question C**: [...]

## My recommendation
Record [Question X] this week. Here's why: [2-3 sentences on leverage + ease]

## How to send the recording
1. Open Voice Memos app (or Otter)
2. Hit record. Talk for 15-20 minutes.
3. Don't edit. Don't perform. Just talk like you're at a kitchen table.
4. Send the file to me however works best (text, email, AirDrop)

That's it. I'll have your week's content back within 48 hours.
```

### Step 1.3 — Send to Cooz Sunday Night
Drop the brief in his inbox or text. Make it feel like a peer briefing, not a content task.

---

## PHASE 2: Voice Memo Capture

**Owner**: Cooz
**Time for him**: 15-20 minutes
**Input from Farrice**: The Creative Brief
**Output**: Raw audio file (m4a, mp3, or wav)

### What Cooz Does
1. Reads the brief (5 min)
2. Picks one question
3. Records 15-20 minutes of raw, unedited talking
4. Sends the file to Farrice

### Tools for Cooz
- iPhone Voice Memos (default)
- Otter.ai (auto-transcribes)
- Voice Memo app of his choice
- Loom audio mode

### Coaching for Cooz (in his README)
- Don't perform. Don't try to be educational.
- Tangents are gold — follow them.
- Get specific. "I had a client last week who..." beats "I always see..."
- Stop when you've said everything, even if it's only 12 minutes.
- If you go past 20, fine — but don't pad.
- Send the raw file. We don't need polish, we need YOU.

---

## PHASE 3: Flywheel Processing

**Owner**: Farrice (orchestrating the agent swarm)
**Time**: 1-2 hours of orchestration, agents do the heavy lifting
**Input**: Raw voice memo
**Output**: 4-channel polished content

### Step 3.1 — Transcribe the Memo
Tool options:
- Otter.ai (best for long-form, free tier covers this)
- Whisper API (most accurate)
- macOS built-in dictation (free, decent)

Save transcript to: `_active/clients/coach-cooz/voice-memos/2026-MM-DD-week-N-transcript.md`

### Step 3.2 — Run the Extraction Agent
Launch a background agent with this prompt structure:

```
You are extracting raw insights from a Coach Cooz voice memo for content production.

Input: [transcript path]
Background: [creative brief that informed the memo]

Tasks:
1. Extract 5-10 raw insights/stories/quotes from the memo
2. Identify the 2-3 strongest narrative threads
3. Cross-reference each thread with the trending topics from the brief
4. Note any moments of unintentional brilliance (the unscripted "gold")
5. Flag any moments that need fact-checking or softening

Output: extraction-week-N.md
```

### Step 3.3 — Run the Translation Agent
Launch a second agent (or chain to first) with:

```
You are translating Coach Cooz's extracted insights into 4-channel polished content.

Voice rules (NON-NEGOTIABLE):
- I-led story. You-pivot at universal moment only. Max 2 "you" sentences total.
- Specificity in I → universality (Sheedy template)
- "Brave choice" / "do it scared" close (his actual signature)
- Brand-jack ONLY when there's a current cultural reference that lands
- Loop architecture: open → close → re-open for re-engagement
- 320 words max for LinkedIn

Frameworks to apply:
- Kallaway's hook archetypes (Personal Confession, Contrarian, Fortuneteller)
- Cole Schafer first-person rule
- Sheedy 6-step I-Perspective Formula
- Dakota Robertson "How I" not "How to"

Output 4 deliverables with editing notes:
1. LinkedIn post (250-350 words)
2. Blog post (800-1500 words)  
3. Podcast script (10-15 min talk track)
4. YouTube script (5-10 min talk track)

Each deliverable should include a "Cooz Edit Notes" section flagging where he should personalize, add a story, or change a phrase to match his voice.
```

### Step 3.4 — Quality Gate (Farrice Reviews)
Before sending to Cooz, check each deliverable against:

| Check | Pass Criteria |
|-------|--------------|
| I/you ratio | "You" appears <5 times, all in final 2 paragraphs |
| Specificity | At least 3 concrete sensory details (time, place, object) |
| Cooz signature | Closes with "brave choice" voice or natural Cooz tag |
| Loop architecture | At least 1 open loop closed mid-post |
| Universal pivot | Pivot sentence arrives AFTER the I-story earns it |
| Length | LinkedIn 250-350 words, blog 800-1500, scripts under 15 min |
| Editing burden | Cooz should be able to publish with 5 min of edits max |

If any deliverable fails, regenerate that section. Don't ship anything below 8/10.

---

## PHASE 4: 4-Channel Output Delivery

**Owner**: Farrice
**When**: Wednesday (target 48 hours after voice memo)
**Output**: One file delivered to Cooz with all 4 channels

### File Format
```markdown
# Week N Content Pack — [Date]
## From the voice memo on [topic]

## LinkedIn Post (Ready to Publish)
[Post body]

**Cooz Edit Notes**:
- Line 4 — feel free to swap the [specific thing] for whatever felt most true in your memo
- Closing — change "brave choice" to "do it scared" if it lands better
- Estimated edit time: 3-5 min

---

## Blog Post (Ready to Publish)
**Title**: [Title]
**Subtitle**: [Subtitle]

[Full body]

**Cooz Edit Notes**: [...]

---

## Podcast Script (10-12 min talk track)
**Episode title**: [Title]
**Hook (0:00-0:30)**: [Opening]
**Main beats**: [...]
**Close (10:00-10:30)**: [...]

**Cooz Edit Notes**: [...]

---

## YouTube Script (5-7 min talk track)
**Video title**: [Title]
**Thumbnail concept**: [Visual]
**Hook (0:00-0:15)**: [Opening]
**Beats**: [...]
**Close**: [...]

**Cooz Edit Notes**: [...]

---

## What Hit Different (Insights from Your Memo)
[2-3 bullet points calling out the moments of unintentional brilliance from the voice memo. This builds Cooz's awareness of what's working in his own voice.]
```

---

## PHASE 5: Cooz Edits + Posts

**Owner**: Cooz
**Time for him**: 30-45 min total across the week
**Output**: 4 pieces of content live across his channels

### Recommended posting cadence (start small)
- **Wednesday**: LinkedIn post goes live
- **Thursday**: Blog post published (Substack/personal site)
- **Friday**: Podcast episode goes live
- **Saturday or Monday following**: YouTube video goes live

### What Cooz does
1. Read each piece (10 min)
2. Make 5-min edits to personalize (per the Edit Notes)
3. Schedule/publish

That's it. The flywheel handles everything else.

---

## The Agent Roster (Who Does What)

The flywheel uses these agents weekly:

| Agent | Phase | Role | Tools |
|-------|-------|------|-------|
| **Trending Research Agent** | 1 | Scrape Reddit + competitor posts + cultural moments | Apify, WebSearch |
| **Extraction Agent** | 3 | Pull 5-10 raw insights from voice memo transcript | Read, Grep |
| **Translation Agent** | 3 | Convert extraction to 4-channel content using validated voice rules | Voice rules, expert frameworks |
| **Quality Gate (Farrice)** | 3-4 | Final review against 7-point checklist | Manual |

---

## The Voice Rules (Non-Negotiable, From WS1.6 Validation)

These are baked into every output:

### The Governing Rule
> **I-led story, you-pivot at the universal moment. Never sustained you-narration.**

### The 6-Step I-Perspective Formula
1. **Opening line** (first-person, declarative, specific): *"I [verb] [specific object]" / "For [time period] I [behavior]" / "[Time marker] ago, I was [state]"*
2. **Specific expansion** (2-4 short paragraphs, all I): Name 2-3 concrete sensory details. Specificity collapses into universality.
3. **Internal turning point** (in I): *"I finally admitted that..." / "The moment happened when..."*
4. **Public declaration line** (optional, in I): *"This is what I do now."*
5. **The you-pivot** (max 2 sentences, first time "you" appears): One universal-condition sentence the reader recognizes.
6. **Close**: Cooz signature ("brave choice"), question, or silence. Never a stacked CTA.

### When "you" Is Allowed (3 narrow contexts)
1. **POV one-liner hook** ("POV: you stopped starting over")
2. **Imperative one-liner** ("Pay attention to what you feed")  
3. **Universal-pivot sentence** (the Sheedy Easter post template)

### When "you" Is Forbidden
- Sustained scene narration
- Projected inner monologue
- Narrated emotion
- Narrated history

### The 4-Voice Rotation
| Voice | % of posts | Perspective |
|-------|-----------|-------------|
| **Confession** | 40% | Pure I |
| **Reframe** | 25% | I with maxim pivot |
| **Witness** | 20% | Third-person peer ("I know a guy...") |
| **Proof** | 15% | I about a client |

---

## Brand-Jacking Strategy

**Use sparingly. ~30% of posts. Never forced.**

Cultural figures/moments that resonate with the founder ICP (Spring 2026):
- Bryan Johnson (longevity industry)
- Severance (work-self/home-self split)
- Liver King exposed (fake authenticity)
- The 4 AM Wake-Up Club (Mel Robbins/Hal Elrod era)
- Andrew Huberman (optimization industry)
- Recent tech layoffs
- AI productivity discourse (Sora 2, ChatGPT-5)
- Joe Rogan / Naval / Modern Wisdom guests of the week

**Rule**: Brand-jack only when it lands a universal contrarian punch in <3 lines and you can pivot to "I" by line 4.

---

## Failure Modes to Watch For

### "You-narration creep"
Symptom: A piece of content has more than 5 "you/your" instances outside the pivot paragraph.
Fix: Run the Red Pen pass — circle every "you" and rewrite as "I" or remove.

### "Generic universalism"
Symptom: The story could be about anyone. No proper nouns, no times, no places.
Fix: Force at least 3 sensory specifics (time of day, exact phrase someone said, physical detail).

### "Therapy-speak creep"
Symptom: Phrases like "embrace the journey," "honor your truth," "lean into discomfort."
Fix: Replace with Cooz's actual voice ("brave choice," "do it scared," direct talk).

### "Stacked CTA close"
Symptom: Post ends with a sales pitch or "DM me to apply."
Fix: Replace with question, signature, or silence. Trust the content to do the work.

### "Too polished"
Symptom: Reads like AI wrote it. No tangents, no rough edges.
Fix: Add back one of Cooz's natural verbal tics from the original voice memo. Keep one sentence intentionally rough.

---

## Quality Bar

Every piece of content shipped through this flywheel should hit:
- **9/10 on voice authenticity** (sounds like Cooz, not like AI)
- **9/10 on specificity** (concrete, sensory, projectable)
- **8/10 on universality** (reader sees themselves voluntarily)
- **8/10 on compelling hook** (forces a "wait, what?" reaction)
- **7/10 on cultural relevance** (lands in the current moment)

If any piece scores below this, regenerate before sending to Cooz.

---

## How This Scales

Week 1-4: Cooz records 1 memo per week → 1 content cycle per week
Week 5-8: Add a second weekly memo for Witness-voice content (lower lift)
Week 9-12: Pull from podcast guest appearances as additional memo material
Month 4+: Cooz has 30+ pieces of authentic content live, the flywheel proves itself with engagement data, and pricing/positioning can scale

The flywheel is the engine. Cooz is the fuel. Farrice is the operator.

---

*Workflow version: 1.0 | Created April 2026 | Validated against WS1.6 voice research data*
