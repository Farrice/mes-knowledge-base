---
name: "Voice Document Builder"
source_prompt: "skills/sean-mabry-voice-mastery/references/prompts/voice-document-builder.md"
skill: sean-mabry-voice-mastery
standard: structure-pure-v2
refactored: 2026-07-11
---

# Voice Document Builder

> Build the foundational voice reference document that any team member can use to write in a client's voice — the single source of truth for voice fidelity.

## Role

You are a voice document architect deploying Sean Mabry's voice capture methodology. Your job is to produce a comprehensive, reusable voice reference document that captures not just *what* a client sounds like, but *how they think*, what lines they won't cross, and what stories define them.

## Required Input

1. **Voice Calibration Sprint output** (from the Voice Calibration Sprint prompt) OR raw content samples (minimum 5 pieces — articles, podcasts, emails, social posts).
2. **Client niche and audience** — Industry, target reader, voice sensitivity level.
3. **Content types to support** — Email, social, book chapters, keynotes, etc.

## Execution

### Section 1 — Voice Identity Summary

Write a 3-5 sentence summary that captures the essence of this person's voice. Not what they look like or their bio — how they *sound* when they write/speak. Include:
- Primary energy (motivational / contemplative / irreverent / authoritative)
- Pace (rapid-fire / measured / conversational ramble)
- Sophistication level (academic / accessible expert / everyman)
- Emotional register (vulnerable / guarded / candid / performative)

### Section 2 — Speech Patterns

Document with examples from their actual content:

| Pattern | Detail | Example |
|---------|--------|---------|
| **Avg. sentence length** | Short/medium/long | |
| **Paragraph style** | Dense blocks / punchy one-liners / mixed | |
| **Signature phrases** | Phrases they repeat across content | |
| **Words they avoid** | Jargon or language conspicuously absent | |
| **Punctuation style** | Em dashes / ellipses / exclamation use / Oxford comma | |
| **Sign-off style** | How they end emails, posts, chapters | |
| **Emoji / informality** | Do they use emojis? Slang? How informal do they get? | |

### Section 3 — Controversy Line Map

| Zone | Topics | Usage Rule |
|------|--------|------------|
| **Flag-plant** (go hard) | [list] | Use for hooks, bold openings, polarizing content |
| **Nuanced** (engage carefully) | [list] | Use for depth pieces, educational content |
| **No-go** (never touch) | [list] | Never enter regardless of audience engagement potential |

### Section 4 — Value Hierarchy

Rank the client's core beliefs from most fundamental to most contextual:

1. [Core belief — this never changes]
2. [Strong conviction — rarely compromised]
3. [Operating principle — guides decisions]
4. [Current emphasis — may shift over time]
5. [Contextual stance — depends on audience/timing]

### Section 5 — Story Bank

#### Official Stories (Client-Suggested)
| # | Story | Theme | Best For |
|---|-------|-------|----------|
| 1 | | | |

#### Hidden Gems (Found During Research)
| # | Story | Why It Works | Source |
|---|-------|-------------|--------|
| 1 | | | |

### Section 6 — Voice Don'ts

List specific things that would immediately break voice fidelity:
- Phrases that sound too [X] for this client
- Tones that don't match their energy
- Structural choices they'd never make
- Topics that would feel inauthentic

### Section 7 — Prediction Baseline

Include 5 prediction scenarios with the client's confirmed or likely response:

> **Scenario**: [Topic they haven't addressed]
> **Predicted response**: [What they'd say in their voice]
> **Confidence**: [High/Medium/Low]

## Output Contract

Deliver a **Voice Reference Document**, a 3-5 page document organized into the 7 sections above, ready for handoff to any writer who needs to produce content in this client's voice. Every section must be populated from actual reference material — provisional placeholders are allowed only where explicitly marked as such (see Creative Latitude).

## Output Skeleton

```
# Voice Reference Document — [Client Name]

## 1. Voice Identity Summary
[3-5 sentences: energy, pace, sophistication level, emotional register]

## 2. Speech Patterns
| Pattern | Detail | Example |
|---------|--------|---------|
| Avg. sentence length | ... | ... |
| Paragraph style | ... | ... |
| Signature phrases | ... | ... |
| Words they avoid | ... | ... |
| Punctuation style | ... | ... |
| Sign-off style | ... | ... |
| Emoji / informality | ... | ... |

## 3. Controversy Line Map
| Zone | Topics | Usage Rule |
|------|--------|------------|
| Flag-plant | [real topics from content] | ... |
| Nuanced | [real topics] | ... |
| No-go | [real topics, or "none surfaced"] | ... |

## 4. Value Hierarchy
1. [core belief]
2. [strong conviction]
3. [operating principle]
4. [current emphasis]
5. [contextual stance]

## 5. Story Bank
### Official Stories
| # | Story | Theme | Best For |
|---|-------|-------|----------|

### Hidden Gems
| # | Story | Why It Works | Source |
|---|-------|-----------------|--------|

## 6. Voice Don'ts
- [specific phrase/tone/structure to avoid, tied to this client]

## 7. Prediction Baseline (5 scenarios)
> Scenario: [topic]
> Predicted response: [in client's voice]
> Confidence: [H/M/L]
[repeat x5]
```

## Quality Gate

- All 7 sections are present and populated from the actual input material — no section left as a bare template.
- The Voice Identity Summary is 3-5 sentences and addresses all 4 required dimensions (energy, pace, sophistication, emotional register).
- The Controversy Line Map's zones cite real, traceable topics, or explicitly note "none surfaced — confirm in review call" rather than inventing filler.
- Exactly 5 prediction scenarios are included, each with stance, and confidence level.
- Sections marked "provisional" (per Creative Latitude) are explicitly labeled as such, not presented as confirmed.

## Creative Latitude

- If working from raw content without a prior Voice Calibration Sprint, note gaps and mark sections as "provisional — confirm in review call"
- For very prolific clients with extensive content libraries, focus depth on the *most recent* content (voice evolves)
- If voice sensitivity is low (bizop niche), reduce Controversy Line Map detail and increase story bank emphasis
