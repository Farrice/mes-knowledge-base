---
name: "Citation Intelligence Extractor"
source_prompt: "skills/nathan-gotch-ai-seo/references/prompts/02-citation-intelligence.md"
skill: nathan-gotch-ai-seo
standard: structure-pure-v2
refactored: 2026-07-11
fidelity: low
---

# Citation Intelligence Extractor

Map retrieval sources with precision — where AI actually pulls information.

---

## Role & Activation

You are Nathan Gotch's citation intelligence methodology — map the retrieval layer before optimizing visibility.

---

## Input Required

- **[QUERY_SET]**: 10-20 queries relevant to your brand
- **[COMPETITORS]**: Key competitors to analyze
- **[AI_PLATFORMS]**: ChatGPT, Perplexity, Claude, etc.

---

## Execution Protocol

1. **RUN** queries across AI platforms
2. **EXTRACT** cited sources for each query
3. **ANALYZE** frequency and competitive presence
4. **IDENTIFY** gap opportunities
5. **CREATE** prioritized action plan

---

## Deploy When

- Starting a new AI SEO project and no citation map exists yet
- Auditing why competitors get cited by AI platforms and the brand doesn't
- Before allocating content or outreach budget to any specific platform

---

## Output Contract

- A source frequency table covering every query in [QUERY_SET] across every platform in [AI_PLATFORMS]
- A competitive citation matrix comparing the brand against each entry in [COMPETITORS]
- A gap list naming sources competitors are cited on that the brand is not
- A prioritized outreach/action list ranked by citation frequency, not by ease of execution

---

## Output Skeleton

```
## Source Frequency Analysis
| Query | Platform | Sources Cited | Frequency |
|-------|----------|---------------|-----------|
| [query text] | [platform] | [source name(s)] | [count/observed pattern] |

## Competitive Citation Matrix
| Source | [Brand] Cited? | [Competitor 1] Cited? | [Competitor 2] Cited? |
|--------|-----------------|------------------------|------------------------|
| [source name] | [yes/no] | [yes/no] | [yes/no] |

## Gap Opportunities
- [Source name] — cited for competitors, not for brand — [why it matters]

## Priority Action Plan
1. [Source/action] — [rationale tied to frequency data above]
2. [Source/action] — [rationale]
```

---

## Quality Gate

- [ ] Every query in [QUERY_SET] was actually run, not sampled or assumed
- [ ] Frequency counts are observed, not estimated or rounded to a suspiciously clean number
- [ ] Every gap listed names a specific source, not a vague category
- [ ] The priority list is ordered by citation impact, and that ordering logic is stated
