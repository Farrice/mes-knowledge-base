---
description: "Build the foundational voice reference document for writing in any client's voice"
---

# /voice-document — Voice Document Builder

Build a comprehensive, reusable voice reference document that enables any writer (human or AI) to write in the client's voice.

## Usage

```
/voice-document [client name]
```

## Steps

### 1. Load the Skill
// turbo
Read `skills/sean-mabry-voice-mastery/genius.md` — load the core voice patterns.

### 2. Load the Prompt
// turbo
Read `skills/sean-mabry-voice-mastery/references/prompts/voice-document-builder.md` — the full voice document workflow.

### 3. Gather Input
Ask the user:
- **Client name**: Who is the client?
- **Existing voice data**: Voice Calibration Report (from `/voice-calibrate`), content samples, podcast transcripts, or prior voice notes?
- **Primary content format**: What's the main content type this document will support?
- **Team usage**: Will other writers use this document, or just you?

### 4. Execute
Follow the prompt to build a structured voice reference covering:
- Speech patterns and cadence
- Values hierarchy
- Controversy Line Map
- Story bank (with Hidden Gems if available)
- Industry jargon mapping
- Do/Don't writing rules with examples

### 5. Deliver
Save the Voice Document and present for review. Recommend: "Run `/voice-audit` on a sample piece to test the document's accuracy."

## Chain Compatibility
- **Follows**: `/voice-calibrate`
- **Leads to**: `/voice-audit`, `/voice-handoff`
