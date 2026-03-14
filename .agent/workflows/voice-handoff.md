---
description: "Package voice mastery into a transferable format for teams, VAs, or AI systems"
---

# /voice-handoff — Voice Handoff Kit

Package your voice mastery into a portable briefing that enables another writer, VA, or AI system to write in the client's voice at 80%+ fidelity.

## Usage

```
/voice-handoff [client name]
```

## Steps

### 1. Load the Skill
// turbo
Read `skills/sean-mabry-voice-mastery/genius.md`.

### 2. Load the Prompt
// turbo
Read `skills/sean-mabry-voice-mastery/references/prompts/voice-handoff-kit.md`.

### 3. Gather Input
Ask the user:
- **Client**: Whose voice is being packaged?
- **Voice Document**: Existing voice reference (from `/voice-document`)
- **Edit history**: Examples of client corrections to past content
- **Recipient**: Who will use this? (junior writer, VA, content team, AI tool)
- **Content scope**: What types of content will they produce?

### 4. Execute
1. Extract concrete Do/Don't rules from Voice Document and edit history
2. Build Before/After Edit Library (5-10 real examples)
3. Create Story Deployment Guide
4. Simplify Controversy Line Map to traffic-light format
5. Design Voice Calibration Test with answer keys
6. If AI recipient: generate system prompt version

### 5. Deliver
Present the Voice Handoff Kit, customized for the recipient type.

## Chain Compatibility
- **Follows**: `/voice-document`, `/voice-audit`
- **Enables**: Team scaling without voice quality degradation
