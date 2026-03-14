---
description: "Conduct multi-round interviews that extract what the client doesn't know they know"
---

# /client-interview — Client Interview Engine

Design and execute multi-round interview sessions that push past rehearsed answers into discovery territory — the material a thought leader didn't know they had.

## Usage

```
/client-interview [client name] [project type: book|series|brand]
```

## Steps

### 1. Load the Skill
// turbo
Read `skills/sean-mabry-voice-mastery/genius.md`.

### 2. Load the Prompt
// turbo
Read `skills/sean-mabry-voice-mastery/references/prompts/client-interview-engine.md`.

### 3. Gather Input
Ask the user:
- **Client**: Who is being interviewed?
- **Project type**: Book, content series, or brand story?
- **Interview count**: How many sessions are planned? (minimum 2 recommended)
- **Existing material**: Voice Document, Hidden Gems bank, Controversy Line Map?

### 4. Execute
Build the multi-round interview package:
- Round 1 (Surface): 12-15 questions targeting planned stories
- Round 2 (Depth): Follow-up protocol pushing past rehearsed answers
- Round 3 (Discovery): Hypothetical reversals, legacy questions, dilemma digs
- Post-interview material triage framework

### 5. Deliver
Present the Interview Package with question sets per round.
After each interview round, help triage material into A/B/C tiers.

## Chain Compatibility
- **Follows**: `/voice-calibrate`, `/hidden-gems`
- **Leads to**: `/memoir-architect`, `/story-remix`
