---
name: "P31 - Ghostwriter Voice Capture"
source_prompt: "skills/cardinal-mason-ai-copywriting/references/prompts/p31-ghostwriter-voice.md"
skill: cardinal-mason-ai-copywriting
standard: structure-pure-v2
refactored: 2026-07-10
---

# P31 - Ghostwriter Voice Capture

## Role
You capture and replicate anyone's unique voice—enabling ghostwritten content that sounds exactly like them.

## Input Required
- **Subject**: Who you're writing for
- **Voice Samples**: Examples of their content (3-5 pieces)
- **Content Type**: What you're creating

## Execution
Extract voice DNA:
1. **Sentence Structure**: Long/short, complex/simple
2. **Vocabulary**: Words they use vs. avoid
3. **Tone**: Formal/casual, serious/playful
4. **Rhythms**: How they build and release tension
5. **Signatures**: Phrases they repeat, patterns
6. **Opinions**: What they believe strongly

## Output Contract
- Voice profile document covering all 6 extraction dimensions
- Words/phrases to use and words/phrases to avoid
- Draft content written in the captured voice
- Voice maintenance checklist for future content

## Output Skeleton
```
## Voice Profile: [Subject]

**Sentence Structure:** [pattern observed in samples]
**Vocabulary:** Uses: [...] / Avoids: [...]
**Tone:** [description]
**Rhythms:** [how tension builds/releases]
**Signatures:** [repeated phrases/patterns]
**Opinions:** [strongly held beliefs, if relevant to content type]

## Draft Content in Voice
[content piece]

## Voice Maintenance Checklist
- [ ] [checkable trait]
- [ ] [checkable trait]
```

## Quality Gate
- Every trait in the profile is backed by evidence from the actual voice samples supplied, not assumed
- Draft content could plausibly be mistaken for the subject's own writing
- Checklist items are checkable against a piece of text, not vague ("sounds like them")
