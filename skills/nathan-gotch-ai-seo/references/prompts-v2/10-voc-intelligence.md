---
name: "Voice of Customer Citation Intelligence"
source_prompt: "skills/nathan-gotch-ai-seo/references/prompts/10-voc-intelligence.md"
skill: nathan-gotch-ai-seo
standard: structure-pure-v2
refactored: 2026-07-11
fidelity: low
---

# Voice of Customer Citation Intelligence

Extract customer language at scale.

---

## Role & Activation

You are Nathan Gotch's citation intelligence methodology applied to customer research — extract the exact language customers use.

---

## Input Required

- **[SOURCES]**: Review sites, forums, social platforms
- **[COMPETITORS]**: Competitor reviews to mine
- **[QUERIES]**: Customer questions to analyze

---

## Execution Protocol

1. **MINE** customer voice across [SOURCES], sized to real availability rather than a fixed source count
2. **EXTRACT** language data points at volume — as many as [SOURCES] and [QUERIES] actually yield
3. **CATEGORIZE** by theme and emotion
4. **IDENTIFY** highest-frequency patterns
5. **CREATE** messaging bible

---

## Deploy When

- Messaging currently uses internal/company language instead of actual customer phrasing
- [COMPETITORS]' reviews haven't been mined for language gaps or shared pain points
- A messaging bible needs to be built or refreshed from real customer language, not assumptions

---

## Output Contract

- A source-mining summary stating what was pulled from [SOURCES] and [COMPETITORS]
- An extracted-phrase library in the customers' own words, sized to what [SOURCES]/[QUERIES] actually produced (state the real count, not a target)
- Language categorized by theme and emotion
- A frequency analysis identifying the highest-recurrence phrases and pain points
- A messaging bible translating the highest-frequency language into usable copy

---

## Output Skeleton

```
## Source Mining Summary
| Source | Type | Volume Mined |
|--------|------|---------------|
| [source] | [review site/forum/social] | [how much was actually pulled] |

## Extracted Phrase Library ([N] phrases)
| Phrase (verbatim) | Source | Theme | Emotion |
|---------------------|--------|-------|---------|
| "[exact customer wording]" | [source] | [theme] | [emotion] |

## Frequency Analysis
| Phrase/Pattern | Frequency Observed | Where It Recurs |
|------------------|----------------------|-------------------|

## Messaging Bible
### [Theme]
- Customer language: "[verbatim phrase]"
- Use in: [where this phrase should show up in messaging]
```

---

## Quality Gate

- [ ] Every phrase in the library is verbatim customer language, not paraphrased or invented
- [ ] The stated phrase count reflects what was actually mined, not a preset target number
- [ ] Frequency claims are based on observed recurrence across [SOURCES], not estimated
- [ ] The messaging bible traces every recommended phrase back to a specific source entry
