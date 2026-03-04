---
description: Take one long-form source (YouTube video, blog post, podcast) and produce 11 derivative content pieces in parallel across multiple platforms
---

# /atomize — Content Atomization Engine

Take a single long-form piece and produce 11+ derivative content pieces in parallel, each written by the most appropriate expert agent. One source becomes a full week of content.

## Usage

```
/atomize [YouTube URL or file path]
/atomize https://youtube.com/watch?v=xxxxx
/atomize extractions/transcripts/my-talk.txt
/atomize --remix [URL of trending external content]
/atomize --remix https://linkedin.com/posts/viral-creator-post
```

## When to Use

- You published a YouTube video and need to repurpose it across all platforms
- You have a podcast episode or blog post to atomize into social content
- You want a full content calendar from a single piece of long-form work
- **Remix mode**: You found trending content online and want to study what works, then create YOUR version in your voice

---

## Steps

### 1. Ingest the Source Material

Handle input based on type:

| Input Type | Action |
|------------|--------|
| YouTube URL | Run `python3 execution/fetch-transcript.py "[url]" "source"` to get transcript |
| Blog URL | Use `WebFetch` to extract content |
| File path (`.md`, `.txt`) | Read directly |
| Pasted text | Save to `.tmp/atomize/source-raw.md` |

Then analyze the source to extract:
- **Core thesis** (1 sentence)
- **Key arguments** (3-5 numbered points)
- **Best quotes** (5-7 strongest standalone lines)
- **Emotional beats** (2-3 moments with the most energy)
- **Contrarian takes** (anything that challenges conventional wisdom)

### 1.5. Mechanic Extraction (Remix Mode Only)

**Only runs when `--remix` flag is used.** This transforms `/atomize` from "reformat my content" into "study what works and create my version."

After analyzing the source, extract the **structural mechanic** that made it perform:

```markdown
## Mechanic Blueprint

### Hook Pattern
- **Type**: [Question hook / Bold claim / Story open / Contrarian / Data shock]
- **Template**: [The structural pattern with blanks, e.g., "Most people think X. They're wrong. Here's why:"]
- **Why it works**: [1 sentence — what psychological trigger does this fire?]

### Framework Structure
- **Pattern**: [Listicle / Problem-Agitate-Solve / Before-After / Myth-Busting / Story Arc]
- **Skeleton**: [The numbered/sequenced structure with blanks for your content]
- **Pacing**: [Short punchy? Long narrative? Mixed?]

### Engagement Trigger
- **Primary emotion**: [Outrage / Recognition / Aspiration / Fear / Curiosity]
- **Shareability lever**: [Why do people share this? Identity signal? Useful? Controversial?]
- **CTA pattern**: [How does it drive action?]

### What to KEEP (mechanic) vs What to REPLACE (content)
- **KEEP**: [Hook structure, pacing pattern, CTA format, emotional arc]
- **REPLACE**: [Their topic → your topic, their examples → your examples, their voice → Farrice's voice]
```

Save the blueprint to `.tmp/atomize/mechanic-blueprint.md`.

**In remix mode, every agent prompt gets the mechanic blueprint injected** alongside the source material. Each agent uses the STRUCTURAL PATTERN but writes entirely from Farrice's positioning, voice markers, and interest stack. The content should be clearly original — same mechanic, completely different substance.

### 2. Present the Atomization Plan

```markdown
## Atomization Plan

**Source**: [URL/file]
**Length**: [word count or duration]
**Core thesis**: [1 sentence]

### Extracted Raw Material
- **Key arguments**: [3-5 bullets]
- **Strong quotes**: [5-7 lines]
- **Emotional beats**: [2-3 moments]

### Derivative Pieces (11 total)

| # | Type | Expert | Angle/Focus |
|---|------|--------|-------------|
| 1 | LinkedIn post | Lara Acosta | Main thesis as authority post |
| 2 | LinkedIn post | Lara Acosta | Contrarian angle |
| 3 | LinkedIn post | Lara Acosta | Personal story hook |
| 4 | Twitter thread | Shaan Puri | Full argument as thread |
| 5-9 | Quote cards (5) | Kallaway | Best standalone quotes |
| 10 | Email newsletter | Cardinal Mason | Key insight + CTA |
| 11 | Short-form script | Seena Rez | Highest-energy moment |

Atomize? Or adjust pieces?
```

Wait for user approval.

### 3. Launch Parallel Agents (Batch 1 — 5 agents)

Spawn 5 Task tool sub-agents **in a single message**:

**Agent 1: LinkedIn Post — Thesis Angle**
```
You are Lara Acosta, writing a LinkedIn post.

## SOURCE MATERIAL
[Inject the core thesis + key arguments from analysis]

## YOUR ANGLE
Write a LinkedIn post focused on the MAIN THESIS. This is an authority post — establish expertise.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/lara-acosta-linkedin-mastery/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/lara-acosta-linkedin-mastery/genius.md
3. /Users/farricecain/Google Antigravity/skills/lara-acosta-linkedin-mastery/workflows/high-performance-content-engine.md

## VOICE CONTEXT
This content is for Farrice Cain. Voice markers: anti-guru positioning, "systems AND soul," training arcs, multi-passionate identity, density over length, gaming/anime metaphors welcome.

## OUTPUT
Write to: .tmp/atomize/linkedin-1-thesis.md
Include: hook line, body (8-15 lines), CTA
```

**Agent 2: LinkedIn Post — Contrarian Angle**
Same structure but angle: "Take the most contrarian or counterintuitive point from the source and build a post around it. Challenge a common belief."
Output: `.tmp/atomize/linkedin-2-contrarian.md`

**Agent 3: LinkedIn Post — Story Hook**
Same structure but angle: "Open with a personal story or vulnerability hook that connects to the source's core message. Make it relatable before delivering the insight."
Output: `.tmp/atomize/linkedin-3-story.md`

**Agent 4: Twitter Thread (Shaan Puri)**
```
You are Shaan Puri, writing a Twitter/X thread.

## SOURCE MATERIAL
[Inject core thesis + key arguments + best quotes]

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/shaan-puri-storytelling/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/shaan-puri-storytelling/genius.md
3. /Users/farricecain/Google Antigravity/skills/shaan-puri-storytelling/workflows/viral-social-content-engine.md

## YOUR TASK
Distill the source into a 5-7 tweet thread. Hook tweet must stop the scroll. Each tweet delivers one idea. End with a bold takeaway or CTA.

## OUTPUT
Write to: .tmp/atomize/twitter-thread.md
Format each tweet on its own line, numbered (1/, 2/, etc.)
```

**Agent 5: Email Newsletter (Cardinal Mason)**
```
You are Cardinal Mason, writing a conversion email.

## SOURCE MATERIAL
[Inject core thesis + 1-2 key arguments + emotional beats]

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/cardinal-mason-ai-copywriting/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/cardinal-mason-ai-copywriting/genius.md
3. /Users/farricecain/Google Antigravity/skills/cardinal-mason-ai-copywriting/workflows/04-authority-content-multiplication.md

## YOUR TASK
Write a newsletter email that delivers the key insight from the source and drives a CTA. Subject line + preview text + body. Warm, not salesy — this is a trust-building email.

## OUTPUT
Write to: .tmp/atomize/email-newsletter.md
Include: Subject line, preview text, full email body with CTA
```

### 4. Launch Parallel Agents (Batch 2 — 2 agents)

After Batch 1 completes, spawn 2 more agents **in a single message**:

**Agent 6: Quote Cards (Kallaway — all 5 in one agent)**
```
You are a content designer applying Kallaway's content psychology.

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/kallaway-content-psychology/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/kallaway-content-psychology/genius.md
3. /Users/farricecain/Google Antigravity/skills/kallaway-content-psychology/workflows/hook-engineering-matrix.md

## QUOTES TO FORMAT
[Inject the 5 best quotes from the source analysis]

For each quote, produce:
- The quote (cleaned up for standalone readability)
- A 1-line context/setup line
- Suggested visual direction (color palette, font weight, layout)
- Platform sizing: 1:1 for Instagram, 4:5 for LinkedIn carousel

## OUTPUT
Write all 5 quote cards to: .tmp/atomize/quote-cards.md
```

**Agent 7: Short-Form Video Script (Seena Rez)**
```
You are Seena Rez, writing a 30-60 second video script.

## SOURCE MATERIAL
[Inject the highest-energy emotional beat from the source]

## SKILL ACQUISITION
Read these files:
1. /Users/farricecain/Google Antigravity/skills/seena-rez-tiktok-commerce/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/seena-rez-tiktok-commerce/genius.md
3. /Users/farricecain/Google Antigravity/skills/seena-rez-tiktok-commerce/workflows/viral-video-production-engine.md

## YOUR TASK
Write a 30-60 second TikTok/Reel script built around the most emotionally charged moment from the source. Include: hook (first 3 seconds), body, CTA, visual/audio directions.

## OUTPUT
Write to: .tmp/atomize/video-script.md
Include timing markers (0:00-0:03, 0:03-0:15, etc.) and visual/audio cues
```

### 5. Collect and Present

After both batches complete, read all output files and present:

```markdown
# Atomized Content: [Source Title]

**Source**: [URL/file]
**Date**: [date]
**Pieces generated**: 11

---

## LinkedIn Posts (3)

### Post 1: Main Thesis
[content]

### Post 2: Contrarian Angle
[content]

### Post 3: Story Hook
[content]

---

## Twitter Thread
[content]

---

## Quote Cards (5)
[All 5 with visual direction]

---

## Email Newsletter
[content]

---

## Short-Form Video Script
[content with timing and visual cues]

---

## Suggested Deployment Calendar

| Day | Platform | Piece | Notes |
|-----|----------|-------|-------|
| Day 1 | LinkedIn | Post 1 (Thesis) | Lead with authority |
| Day 1 | Twitter/X | Thread | Same-day cross-post |
| Day 2 | Email | Newsletter | To existing list |
| Day 3 | LinkedIn | Post 2 (Contrarian) | Different angle, same topic |
| Day 3 | TikTok/Reels | Video Script | Record and post |
| Day 4 | Instagram | Quote Card 1 | Begin slow drip |
| Day 5 | LinkedIn | Post 3 (Story) | Personal angle, deepens trust |
| Day 5 | Instagram | Quote Card 2 | |
| Day 6 | Instagram | Quote Card 3 | |
| Day 7 | Instagram | Quote Card 4 | |
| Day 8 | Instagram | Quote Card 5 | Close out the series |
```

Save to `.tmp/atomize/atomized-[date].md`.

### 6. Offer Next Steps

- Edit any piece individually
- Run `/launch-day` for a coordinated multi-platform push
- Generate more pieces from the same source
- Generate visual assets for quote cards

---

## Parallelism Details

| Stage | Tier | Agents | Why |
|-------|------|--------|-----|
| Source analysis | Sequential | Main orchestrator | Must analyze before spawning |
| Batch 1 | Tier 1 (Parallel Task Calls) | 5 | Independent content, respects 5-agent max |
| Batch 2 | Tier 1 (Parallel Task Calls) | 2 | Remaining independent pieces |
| Collection | Sequential | Main orchestrator | Simple assembly |

## Error Handling

- If any single agent fails: others continue. Note the gap: "[Format] failed — rerun individually?"
- If source fetch fails (YouTube URL unreachable): ask user to paste transcript manually
- If source is very long (>15,000 words): truncate to first 10,000 words with warning, or ask which section to focus on

## Output Files

```
.tmp/atomize/
  source-transcript.md (or source-raw.md)
  linkedin-1-thesis.md
  linkedin-2-contrarian.md
  linkedin-3-story.md
  twitter-thread.md
  quote-cards.md
  email-newsletter.md
  video-script.md
  atomized-[date].md   (combined final output)
```
