---
name: "X-Ray Reading Protocol"
source_prompt: skills/dan-wang-literary-analysis/references/prompts/xray-reading-protocol.md
skill: dan-wang-literary-analysis
standard: structure-pure-v2
refactored: 2026-07-11
---

# X-Ray Reading Protocol

Read faster with equal or better comprehension by identifying animated vs. obligated writing.

## Role

You are applying Dan Wang's reading acceleration methodology — developing the "x-ray vision" to see when authors are writing because they WANT to vs. when they're fulfilling genre obligations.

## Required Input

- **BOOK/DOCUMENT**: The material to be processed
- **READING GOAL**: What you need to extract from this reading

## Execution

1. **Genre Constraint Identification**: What does this format (trade book, academic paper, industry report) typically require that isn't actually valuable? Table of contents → identify obligatory sections.

2. **Animated vs. Obligated Scan**: As you read, continuously ask: "Did the author WANT to write this or HAVE to?" Skip obligated sections.

3. **Fire Detection**: Where is the author on fire? These sections—often marked by more specific examples, stronger opinions, unexpected tangents—contain the real insight.

4. **Potted History Skip**: "Background" and "History" sections in most books are obligatory padding. Skim for any genuinely surprising claims, otherwise skip.

5. **Conclusion-First Reading**: Read conclusion/final chapter first. If the synthesis is clear, you can read supporting chapters selectively.

6. **Quote Extraction**: Capture the sentences where the author's voice is strongest. These are the transferable insights.

## Output Contract

- **Key Insights**: 5-10 core takeaways drawn specifically from the animated ("fire") sections, not from skimmed obligatory sections
- **Skip Report**: Which sections were identified as obligatory/genre-padding, for reference on similarly-structured material
- **Fire Sections**: The specific sections/page ranges where the author was most engaged, with what marked them as animated (specific examples, strong opinion, unexpected tangent)
- **Quotable Sentences**: 3-5 sentences where the author's voice was strongest, captured verbatim from the source
- **Reading Time**: An honest estimate of time spent vs. what full linear reading would have taken, tied to the actual sections skipped — not an assumed multiplier

## Output Skeleton

```
## Key Insights (5-10)
1. [insight] — source: [fire section it came from]
2. [...]

## Skip Report
- [section name]: skipped — [why it was identified as obligatory/genre-padding]
- [...]

## Fire Sections
- [section/page range]: [what marked it as animated — specific example / strong opinion / unexpected tangent]
- [...]

## Quotable Sentences (3-5, verbatim from source)
1. "[sentence]" — [location]
2. [...]

## Reading Time
- Sections read fully: [list]
- Sections skipped: [list]
- Estimated time saved vs. full linear read: [honest estimate tied to the actual skip list, not an assumed ratio]
```

## Quality Gate

- Is each key insight traced to a specific fire section rather than asserted generically?
- Does the skip report name the actual sections skipped and the specific reason (genre convention, not just "boring")?
- Are the quotable sentences verbatim from the source material, not paraphrased or invented?
- Is the reading-time estimate grounded in the actual sections read/skipped for this specific document, rather than a stock ratio applied without basis?
- Was the conclusion read first, and does that inform which supporting sections were selected for full reading?
