---
description: "Score any ghostwritten content against voice fidelity markers — find and fix every voice break"
---

# /voice-audit — Voice Accuracy Audit

Score any ghostwritten content against voice fidelity markers. Line-by-line analysis with break classification and prescriptive rewrites.

## Usage

```
/voice-audit [paste content or provide file path]
```

## Steps

### 1. Load the Skill
// turbo
Read `skills/sean-mabry-voice-mastery/genius.md`.

### 2. Load the Prompt
// turbo
Read `skills/sean-mabry-voice-mastery/references/prompts/voice-accuracy-audit.md`.

### 3. Gather Input
Ask the user:
- **Content to audit**: The ghostwritten draft (paste or file path)
- **Voice reference**: Voice Document, or 3+ client content samples
- **Content format**: Email, LinkedIn post, book chapter, sales page?

### 4. Execute
1. Extract voice fingerprint from reference material
2. Line-by-line fidelity scan (✅ on-voice / ⚠️ close but off / ❌ voice break)
3. Classify every break (vocabulary drift, rhythm violation, authority mismatch, etc.)
4. Calculate accuracy score (90-100% = publish, 75-89% = fix, below 75% = re-immerse)
5. Prescriptive rewrite for every break

### 5. Deliver
Present the Voice Accuracy Report with score, break analysis, and rewrites.

## Chain Compatibility
- **Follows**: `/voice-document` (uses voice reference)
- **Pairs with**: `/voice-handoff` (audit is the QA layer for team output)
