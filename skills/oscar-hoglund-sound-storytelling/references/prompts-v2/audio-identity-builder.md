---
name: "Audio Identity Builder"
source_prompt: "skills/oscar-hoglund-sound-storytelling/references/prompts/audio-identity-builder.md"
skill: oscar-hoglund-sound-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Audio Identity Builder

Create comprehensive sonic brand identity for content or business.

## Role

You architect complete audio identities that create instant brand recognition.

## Required Input

- **[BRAND/CREATOR]**: Who this is for
- **[EMOTIONAL_GOALS]**: How should audience feel
- **[CONTENT_TYPES]**: Where audio will be used

## Execution Protocol

### Step 1: Emotional Core
Define the 3-5 core emotions this brand evokes

### Step 2: Sonic Palette
Select sounds that convey those emotions

### Step 3: Application Guidelines
How to use across different contexts

## Output Contract

Deliverable: a complete audio identity document covering emotional DNA, sonic palette, application guidelines per content type actually listed in CONTENT_TYPES, mood variations, and a 5-point scoring checklist for any future track selection.

## Output Skeleton

```markdown
# AUDIO IDENTITY: [Brand/Creator Name]

## Emotional DNA
**Core emotions**: [Primary], [Secondary], [Tertiary]
**Described in one sentence**: [Sentence]
**Spectrum position**: [Where on the frequency → meaning spectrum]

## Sonic Palette

### Primary Sounds
| Element | Description | Emotion Conveyed |
|---------|-------------|------------------|
| Intro stinger | [Description] | [Emotion] |
| Background bed | [Description] | [Emotion] |
| Transition | [Description] | [Emotion] |
| Outro | [Description] | [Emotion] |

### Instruments & Textures
**Lead elements**: [Instruments/sounds]
**Supporting texture**: [Elements]
**Avoid**: [What doesn't fit]

### Tempo & Energy
**Default BPM range**: [X-X]
**Energy curve**: [How it moves]

## Application Guidelines

### Video Content
**Intro**: [X seconds, energy level]
**Background during talk**: [Volume, type]
**Emphasis moments**: [How to punctuate]
**Outro**: [Duration, fade type]

### Podcast/Audio
**Theme music**: [Specs]
**Transition sounds**: [Specs]
**Background bed**: [When to use/not use]

### Short-Form (TikTok/Reels)
**Hook sound**: [Description]
**Throughout**: [Approach]
**Ending**: [Approach]

## Mood Variations

### High Energy Version
**When to use**: [Situation]
**Adjustments**: [What changes]

### Intimate Version
**When to use**: [Situation]
**Adjustments**: [What changes]

### Celebratory Version
**When to use**: [Situation]
**Adjustments**: [What changes]

## Music Selection Criteria

For any new track, must score 4/5 on:
- [ ] Matches core emotional DNA
- [ ] Fits spectrum position
- [ ] Within tempo range
- [ ] Complements voice (doesn't compete)
- [ ] Works with established sonic palette
```

## Quality Gate

- [ ] Emotional DNA names 2-3 specific emotions, not generic terms like "positive" or "engaging"
- [ ] Every sonic palette element (stinger, bed, transition, outro) is tied to a stated emotion
- [ ] Application guidelines are specified separately for each content type actually listed in CONTENT_TYPES
- [ ] Any candidate track could be scored against the 5-point Music Selection Criteria without ambiguity
