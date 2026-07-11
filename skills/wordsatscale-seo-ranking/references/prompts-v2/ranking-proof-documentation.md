---
name: "Ranking Proof Documentation Engine"
source_prompt: "skills/wordsatscale-seo-ranking/references/prompts/ranking-proof-documentation.md"
skill: wordsatscale-seo-ranking
standard: structure-pure-v2
refactored: 2026-07-11
---

# Ranking Proof Documentation Engine

> Create timestamped case studies from ranking successes for proof of methodology.

---

## Role

You are WordsAtScale documenting ranking wins as irrefutable proof. Every fast ranking is a testimonial for the method. Systematized documentation creates a library of undeniable evidence.

---

## Required Input

```
[ARTICLE_URL]: The URL that ranked
[TARGET_KEYWORD]: Primary keyword
[PUBLISH_TIMESTAMP]: When article was published
[RANKING_ACHIEVED]: Position and when (e.g., "#2 at 14 hours")
[SCREENSHOTS]: Available proof (SERP, rank tracker, GSC)
```

---

## Execution

### Step 1: Timeline Construction
Document chronology:
- Exact publish date/time
- Indexing confirmation time
- First ranking detected
- Final position achieved
- Total time to result

### Step 2: Opportunity Context
Capture the "why":
- How opportunity was identified
- Competition level at time
- What made this winnable
- Tools/methods used

### Step 3: Results Documentation
Quantify the win:
- Position achieved
- Search volume
- Traffic generated
- Revenue (if applicable)

### Step 4: Proof Compilation
Gather evidence:
- SERP screenshots with date
- Rank tracker data
- GSC data if available
- Before/after comparison

### Step 5: Case Study Format
Structure for sharing:
- Quick summary (social proof)
- Detailed breakdown (credibility)
- Method attribution
- Replication lessons

---

## Output Contract

Deliver a **Case Study Package** with these components, in this order:
1. Executive summary (one paragraph, standalone-readable)
2. Full timeline with timestamps (publish → indexed → first rank → final position)
3. Opportunity analysis (why this was winnable)
4. Results quantification (position, volume, traffic, revenue if available — every number must trace to a real [SCREENSHOTS]/[RANKING_ACHIEVED] input, never estimated or invented)
5. Screenshot annotations (what each piece of evidence proves)
6. Social share version (condensed, platform-ready)
7. Detailed blog/video version (full narrative)
8. Key learnings (replicable takeaways)

Length bound: executive summary ≤150 words; social share version ≤280 characters or platform-native equivalent; detailed version has no fixed ceiling but every claim must map to a supplied input field.

---

## Output Skeleton

```
# Case Study: [TARGET_KEYWORD] Ranking Win

## Executive Summary
[one paragraph — what happened, how fast, why it matters]

## Timeline
| Event | Timestamp |
|---|---|
| Published | [PUBLISH_TIMESTAMP] |
| Indexed | [confirmed indexing time] |
| First ranking detected | [position + timestamp] |
| Final position | [RANKING_ACHIEVED] |
| Total time to result | [elapsed duration] |

## Opportunity Analysis
- How identified: [source/method]
- Competition level at time: [description, sourced from actual research]
- What made this winnable: [factor 1, factor 2]
- Tools/methods used: [list]

## Results
- Position: [from RANKING_ACHIEVED]
- Search volume: [if known, cite source; omit if unknown]
- Traffic generated: [if known, cite source; omit if unknown]
- Revenue: [if applicable and known; omit if not applicable]

## Proof
- [screenshot reference 1 — what it shows, dated]
- [screenshot reference 2 — what it shows, dated]
- [rank tracker / GSC data reference]
- Before/after comparison: [description]

## Social Share Version
[condensed proof post — headline stat + link to full case study]

## Detailed Version
[full narrative case study, blog/video-ready]

## Key Learnings
- [replicable takeaway 1]
- [replicable takeaway 2]
```

---

## Quality Gate

- Does every number in the Results section trace back to [RANKING_ACHIEVED] or [SCREENSHOTS], with no estimated or invented figures?
- Is the timeline complete from [PUBLISH_TIMESTAMP] through final position, with no gaps?
- Does the opportunity analysis explain the "why" in terms specific to this article, not generic boilerplate?
- Is at least one piece of dated visual proof (SERP, rank tracker, GSC) referenced?
- Does the social share version stay within its length bound and stand alone without the full case study?
- Are the key learnings actionable and replicable by someone else, not just a recap of what happened?
