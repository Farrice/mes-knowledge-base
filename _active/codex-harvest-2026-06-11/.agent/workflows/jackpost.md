---
description: Universal borrowed-attention post engine
---

# `/jackpost` — Universal Borrowed-Attention Engine

Take any brand, person, or news event → auto-detect jack type → research → produce platform-native content for ANY platform. Not LinkedIn-locked.

**The platform-agnostic version of Diandra's growth system.** Same borrowed-attention mechanics, adapted to wherever you need to post.

## When to Use
- You want to write about an entity (brand/person/news) but NOT just for LinkedIn
- You want multi-platform content from one entity in a single sprint
- You need X threads, newsletter sections, or email copy that borrows attention
- You want the growth post methodology applied to platforms beyond LinkedIn

## Usage

```
/jackpost [entity] --platform [linkedin|x|substack|email|all]
/jackpost "Apple Vision Pro sales data" --platform x
/jackpost "Sam Altman" --platform all
/jackpost --find [niche] --platform [platform]
```

---

## Phase 1: Entity Intake + Platform Lock

**Actor**: Orchestrator

### Entity Classification

Same as `/diandra-growth-sprint`:

| Signal | Jack Type |
|--------|-----------|
| Brand + business decision | **Brandjack** |
| Industry news/announcement | **Newsjack** |
| Individual person + their work | **Namejack** |
| Consensus belief to challenge | **Hot Take** |

### Platform-Expert Routing

| Platform | Primary Expert | Secondary Expert | Format |
|----------|---------------|-----------------|--------|
| LinkedIn | Diandra Escobar | Lara Acosta | Text post / carousel / long-form |
| X/Twitter | Shaan Puri | Diandra (mechanics) | Thread / single tweet |
| Substack | Nicolas Cole | Eric Roth (narrative) | Newsletter section / full essay |
| Email | Cardinal Mason | Luke Iha (copy) | Conversion email / nurture email |
| **All** | Platform-specific experts | Diandra (entity mechanics) | One piece per platform |

```markdown
## Jackpost Setup
- **Entity**: [name]
- **Jack Type**: [type]
- **Platform(s)**: [selected]
- **Expert Routing**: [expert per platform]
- **Proceed?**
```

---

## Phase 2: Entity Research (MANDATORY)

**Actor**: Orchestrator + research tools

Same research protocol as `/diandra-growth-sprint`:

1. Entity deep-dive (what happened, specific details)
2. Audience reaction (Reddit, X, LinkedIn — real quotes)
3. Platform-specific context (how is this entity being discussed ON the target platform?)
4. Boomerang recon (does entity have presence on target platform?)

Save to `.tmp/jackpost/research-[slug].md`.

---

## Phase 3: Angle Mining

**Actor**: Orchestrator

Generate 3 angles using Diandra's framework:
- **What They Did Right** — learning angle
- **What They Missed** — critique angle
- **What This Means For You** — impact angle

Score angles by platform fit:

| Angle | LinkedIn Fit | X Fit | Substack Fit | Email Fit |
|-------|-------------|-------|-------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Present with recommendation. WAIT FOR USER SELECTION.**

---

## Phase 4: Platform-Native Production (Parallel)

**Actor**: 1 sub-agent per platform, launched in parallel

### For each target platform, spawn a sub-agent:

#### LinkedIn Sub-Agent
```
You are Diandra Escobar, producing a LinkedIn growth post.

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Codex Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
2. /Users/farricecain/Codex Antigravity/skills/diandra-escobar-linkedin-growth/workflows/09-linkedin-writing-engine.md

## CONTEXT
[Research brief + selected angle]

## TASK
Write a LinkedIn text post (150-300 words):
- Body-first method: write substance, mine for hook
- Entity in first 2 lines
- Growth bucket CTA
- Boomerang-optimized if entity is active on LinkedIn

Write to: .tmp/jackpost/platform-linkedin.md
```

#### X/Twitter Sub-Agent
```
You are Shaan Puri, producing an X thread.

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Codex Antigravity/skills/shaan-puri-storytelling/SKILL.md
2. /Users/farricecain/Codex Antigravity/skills/shaan-puri-storytelling/genius.md

## CONTEXT
[Research brief + selected angle]

## TASK
Write a 5-7 tweet thread:
- Tweet 1: Hook that works standalone (entity + surprising claim)
- Tweets 2-5: Value delivery (one atomic idea per tweet)
- Tweet 6-7: CTA + retweet incentive
- Thread format: each tweet must work if read individually
- Use Farrice's voice, not Shaan's — but apply Shaan's structural patterns

Write to: .tmp/jackpost/platform-x.md
```

#### Substack Sub-Agent
```
You are Nicolas Cole, producing a newsletter section.

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Codex Antigravity/skills/nicolas-cole-digital-writing/SKILL.md
2. /Users/farricecain/Codex Antigravity/skills/nicolas-cole-digital-writing/genius.md

## CONTEXT
[Research brief + selected angle]

## TASK
Write a newsletter section (400-800 words):
- Personal framing: why YOU noticed this entity move
- Deeper analysis than LinkedIn allows
- Include 1-2 additional data points / quotes from research
- Subscriber-specific CTA (reply, forward, upgrade)
- Use Farrice's voice with Cole's digital writing structure

Write to: .tmp/jackpost/platform-substack.md
```

#### Email Sub-Agent
```
You are Cardinal Mason, producing a conversion-oriented email.

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Codex Antigravity/skills/cardinal-mason-copywriting/SKILL.md
2. /Users/farricecain/Codex Antigravity/skills/cardinal-mason-copywriting/genius.md

## CONTEXT
[Research brief + selected angle]

## TASK
Write a conversion email (200-400 words):
- Subject line: entity name + curiosity gap
- Opening: hook (entity + surprising claim)
- Body: analysis → bridge to your offer / service
- CTA: specific action tied to your business
- Use borrowed attention to drive business results, not just engagement

Write to: .tmp/jackpost/platform-email.md
```

---

## Phase 5: Quality Gate + Deliver

### Platform-Specific Quality Checks:

| Platform | Key Check |
|----------|-----------|
| LinkedIn | Entity in first 2 lines? Body-first? Growth CTA? |
| X | Tweet 1 works standalone? Thread has forward momentum? |
| Substack | Personal framing? Deeper than social? Subscriber CTA? |
| Email | Subject line compelling? Bridge to offer natural? Clear CTA? |

### Universal Checks:
- "So What?" gate: position, not summary
- Voice: sounds like creator across all platforms
- Specificity: ≥2 real details per piece
- Anti-pattern: not a generic news summary

### Deliver

```markdown
# 🎯 JACKPOST: [Entity Name]

**Jack Type**: [type] | **Platforms**: [list]
**Angle**: [selected angle]
**Date**: [date]

---

## LINKEDIN
[Full post]

## X/TWITTER THREAD
[Full thread]

## SUBSTACK / NEWSLETTER
[Full section]

## EMAIL
**Subject**: [subject line]
[Full email]

---

## BOOMERANG STRATEGY
[Per-platform boomerang notes]

## PROVENANCE
Research: [queries] | Skills: [list per platform]
```

Save to `.tmp/jackpost/jackpost-[slug]-[date].md`.

---

## Output Files

```
.tmp/jackpost/
  research-[slug].md
  platform-linkedin.md
  platform-x.md
  platform-substack.md
  platform-email.md
  jackpost-[slug]-[date].md   (assembled package)
```
