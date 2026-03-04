---
description: "Voice-First Content Pipeline — topic research → prompt sets → voice capture → writer's room → editor pass → final review → publish"
---

# /voice-first-content — Voice-First LinkedIn Content Pipeline

Your voice goes in. Masterful posts come out. Every piece of content starts from YOUR words, YOUR stories, YOUR psychology — never from AI-generated drafts.

## Usage

```
/voice-first-content research    — Research trending topics for the coaching audience
/voice-first-content prompts     — Create prompt sets for voice capture
/voice-first-content ghostwrite  — Take raw voice input and run through writer's room
/voice-first-content edit        — Run editor pass on drafted posts
/voice-first-content full        — Run entire pipeline end to end
```

---

## The Pipeline

```
TOPIC RESEARCH → PROMPT SET → VOICE CAPTURE → WRITER'S ROOM → EDITOR PASS → FARRICE FINAL PASS → PUBLISH
     (AI)          (AI)        (FARRICE)        (AI+Experts)     (AI)          (FARRICE)
```

### Stage 1: Topic Research (AI)

Research fresh topics that are psychologically resonant for the coaching audience RIGHT NOW.

**Process:**
1. Web search: LinkedIn trends, coaching industry conversations, algorithm changes
2. Filter for topics where **psychology IS the argument** (not tips with psychology sprinkled in)
3. Score each topic on: timeliness, psychological depth, Farrice's unique angle
4. Rank and present top 5-7 for the batch

**Output:** Topic research document saved to `_active/linkedin-launch/research/[date]-topic-research.md`

**Principle:** Topics must pass the **Psychology-First Test**: Is the psychological insight the CORE of the post, with tactics emerging naturally from it? If the psychology is decorative, reject the topic framing.

---

### Stage 2: Prompt Set Creation (AI)

For each selected topic, create a set of 5-7 talking point prompts designed to draw out Farrice's genuine perspective.

**Prompt Design Principles:**
- Questions pull STORIES, not opinions ("Tell me about a time..." not "What do you think about...")
- Questions target the PSYCHOLOGY LENS ("What's really happening in that person's nervous system when...")
- Questions draw out METHODOLOGY ("Walk me through exactly what you do when a client...")
- Questions surface BELIEFS ("What does everyone in this space get wrong about...")
- Questions invite the PERSONAL ("Have you experienced this yourself? What did it feel like?")

**Anti-Patterns (never do these):**
- Generic questions anyone could answer ("What's your advice for...")
- Leading questions that contain the answer ("Don't you think coaches should...")
- Questions that produce tip lists ("What are your top 3...")

**Output:** Prompt sets saved to `_active/linkedin-launch/prompt-sets/batch-[N]/[topic-slug].md`

---

### Stage 3: Voice Capture (FARRICE)

Farrice talks through each prompt set. Raw, unpolished, real.

**Formats (any of these work):**
- Voice notes (preferred — captures natural speech patterns, rhythm, energy)
- Typed stream of consciousness
- Video responses
- Voice-to-text transcription

**Instructions for Farrice:**
- Don't try to write a post. Just TALK.
- If a prompt doesn't land, skip it. The ones that light you up are the gold.
- Tangents are good. The unexpected connections are what makes YOUR take unique.
- Name the client. Name the moment. Name the feeling. Specificity is everything.
- If you feel your energy shift on a topic — lean into that. That's the post.

**Output:** Raw voice capture saved to `_active/linkedin-launch/voice-captures/batch-[N]/[topic-slug].md`

---

### Stage 4: Writer's Room (AI + Expert Ensemble)

Multiple expert lenses applied to Farrice's raw voice to shape it into a LinkedIn post. They don't write separately and merge — they inform a SINGLE ghostwrite.

**The Expert Table:**

| Expert | Lens | What They Do |
|--------|------|-------------|
| **Mitch Albom** | Emotional prose | Where to linger, where to race. Gravedigger technique — small moments that illuminate big truths. Humility voice — marveling, not lecturing. |
| **Shaan Puri** | Storytelling | Find the 5-Second Moment in Farrice's stories. Frame > Hook. Low-status opening when appropriate. |
| **Jeremy Miner** | Psychology architecture | Identity claims, consequence stacking, pre-framing. Reader should claim a positive identity by the end. |
| **Joanna Wiebe** | Invisible persuasion | Keep System 2 asleep. Remove toll booths. Money words from audience vocabulary. Level 5 = can't detect the persuasion. |
| **Harry Dry** | Tightness | Every word earns its place. Three Rules Test. One Mississippi Test. Falsifiability Filter. |
| **Donald Miller** | Zero cognitive load | Jargon as authority markers — used once, placed precisely, grounded immediately. Sound bite reduction. |

**Writer's Room Rules:**
1. Farrice's voice is the CONSTRAINT. Every sentence must sound like him talking.
2. Psychology is the SPINE. The psychological insight is the post. Tactics emerge from it.
3. Personal history is WOVEN, not inserted. Never "I spent X years..." as a standalone credential.
4. Training/coaching jargon is used as AUTHORITY MARKERS — placed at peak impact, grounded instantly.
5. Each post needs a SCREENSHOTABLE SENTENCE — one line that compresses the thesis into a feeling.

**Post Architecture (Psychology-First):**
```
HOOK — Pattern interrupt or recognition moment (2-3 lines max)
RECOGNITION — Reader feels seen (the psychology of what's happening to them)
MECHANISM — Why this happens (the insight, the clinical pattern, the human truth)
BRIDGE — The tactic/framework that emerges naturally from understanding the mechanism
CTA — Identity move ("become the type of coach who...") not tool download
```

**Output:** Drafted posts saved to `_active/linkedin-launch/drafts/batch-[N]/[topic-slug].md`

---

### Stage 5: Editor Pass (AI + LinkedIn Experts)

Platform-specific optimization without losing the voice.

**Editor Table:**

| Expert | Role |
|--------|------|
| **Lara Acosta** | 8-Word Rehook, F-shape formatting, mobile cutoff optimization |
| **Jasmin Alic** | Trapdoor hooks, rhythmic asymmetry, comment laboratory CTA |
| **Tommy Clark** | "How I" framing, AI saturation floor check |
| **Kallaway** | Dopamine Ladder verification (all 6 levels), curiosity loop check |

**Editor Checklist:**
- [ ] Hook fits in mobile "see more" cutoff (8 words max per line)
- [ ] F-shape reading pattern (1-line sentences, double line breaks)
- [ ] No AI-sounding phrases (check against AI saturation floor)
- [ ] CTA keyword is clear and simple
- [ ] First comment strategy defined (link to prompt kit or resource)
- [ ] Factual safety — zero unverifiable claims, no fabricated cultural references
- [ ] Post length: 800-1500 words (LinkedIn sweet spot for expertise content)
- [ ] Dopamine Ladder: Stimulation → Captivation → Anticipation → Validation → Affection → Revelation

**Output:** Edited posts saved to `_active/linkedin-launch/posts/[post-number]-[slug].md`

---

### Stage 6: Farrice Final Pass (FARRICE)

Farrice reads each post and adjusts anything that doesn't sound like him.

**Review Prompts:**
- Read it aloud. Does it sound like you talking to a friend who coaches?
- Is there any sentence where you think "I'd never say it that way"? Flag it.
- Does the psychology feel right? Is the mechanism accurate to what you've observed?
- Would you be comfortable if a client read this? A colleague?
- Is there anything that could be challenged or called out?

**Output:** Final approved posts, ready for publishing schedule.

---

## Batch Cadence

- **Research** fresh topics every 2-4 weeks (or when a cultural moment hits)
- **Prompt sets** for 5-7 topics per batch
- **Voice capture** at Farrice's pace — can batch multiple topics in one session
- **Writer's room through publish** runs in 1-2 sessions per batch

---

## File Structure

```
_active/linkedin-launch/
├── research/              — Topic research documents
├── prompt-sets/           — Prompt sets organized by batch
│   ├── batch-01/
│   │   ├── expertise-trap.md
│   │   ├── afraid-of-being-seen.md
│   │   └── ...
├── voice-captures/        — Farrice's raw voice input
│   ├── batch-01/
├── drafts/                — Writer's room output (pre-edit)
│   ├── batch-01/
├── posts/                 — Final published posts
└── prompt-kits/           — Audience-facing prompt kit deliverables
```

---

## Key Principle

> **Your voice goes in. Masterful posts come out.**
>
> The psychology is YOURS. The stories are YOURS. The lens is YOURS.
> We add craft, structure, and platform optimization.
> We never add ideas, positions, or experiences you didn't provide.

---

## Chain Compatibility

- **Pairs with** `/ghostwrite` — this pipeline IS the self-ghostwriting version of the GVE service
- **Feeds into** Substack newsletter, prompt kits, digital products
- **Research stage** can use `/research-topic` or `/hunt-trends` for deeper dives
- **Writer's room** can invoke `/roundtable` for complex multi-expert synthesis
