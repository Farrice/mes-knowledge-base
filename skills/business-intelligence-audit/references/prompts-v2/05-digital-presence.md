---
name: "Digital Presence Analysis"
source_prompt: "skills/business-intelligence-audit/references/prompts/05-digital-presence.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 05: Digital Presence Analysis

> Audit SEO, social, reviews, and traffic signals.

---

## Purpose

Evaluate the business's overall digital footprint—where they're visible, where they're invisible, and what the data reveals.

---

## Input Required

- **Company name and URL**
- **Social handles** (if known)

---

## Execution Protocol

```
You are conducting a digital presence audit as part of a consulting engagement.

Analyze the complete digital footprint of [COMPANY].

## Instructions

1. Use search_web to gather external signals
2. Extract social profiles and assess activity
3. Check review platforms for reputation signals
4. Synthesize into presence score and recommendations

## Research Queries

Run these searches:
- "[company name] reviews"
- "site:[domain] + [industry keywords]" (for SEO presence)
- "[company name] + [founder name]"
- "[company name] podcast" or "interview"
```

---

## Output Contract

- **Digital Presence Score table:** all nine channels assessed (Website, LinkedIn Company, LinkedIn Founder, Instagram, Twitter/X, YouTube, TikTok, Podcast own, Podcast guest) plus one overall score
- **SEO Signals:** domain authority signal, content volume, keyword presence, technical signals — each sourced from an actual search/extraction, not assumed
- **Reputation Analysis:** review platform table (five platforms) plus sentiment summary
- **Content Distribution:** primary channel, frequency, engagement level, content type
- **Authority Signals:** press, speaking/podcasts, partnerships, awards — each marked present/absent with source
- **Digital Presence Gaps:** four named categories
- **Recommendations:** prioritized by impact, each tied to a specific gap

---

## Output Skeleton

```
### Digital Presence Score

| Channel | Status | Quality /10 | Activity | Notes |
|---------|--------|-------------|----------|-------|
| Website | [present/absent] | [score] | [active/dormant] | [note] |
| LinkedIn (Company) | | | | |
| LinkedIn (Founder) | | | | |
| Instagram | | | | |
| Twitter/X | | | | |
| YouTube | | | | |
| TikTok | | | | |
| Podcast (own) | | | | |
| Podcast (guest) | | | | |

Overall Score: [x]/10

### SEO Signals
- Domain Authority Signal: [based on observed link presence/mentions]
- Content Volume: [indexed pages, blog activity — observed count or estimate with source]
- Keyword Presence: [do they rank for obvious terms — yes/no with the query used]
- Technical Signals: [site speed, mobile-friendly, if observable]

### Reputation Analysis

| Platform | Rating | # Reviews | Key Themes |
|----------|--------|-----------|------------|
| Google | | | |
| G2/Capterra | | | |
| Trustpilot | | | |
| BBB | | | |
| Industry-specific | | | |

Sentiment Summary:
- Positive Themes: [what happy customers mention]
- Negative Themes: [what unhappy customers mention]
- Response Pattern: [does the business respond to reviews]

### Content Distribution
- Primary Channel: [where they're most active]
- Content Frequency: [publishing cadence]
- Engagement Level: [do people interact]
- Content Type: [educational / promotional / entertainment / mixed]

### Authority Signals
- Press Coverage: [present/absent + source]
- Speaking/Podcasts: [founder visibility, present/absent + source]
- Partnerships: [notable affiliations, present/absent]
- Awards/Recognition: [present/absent]

### Digital Presence Gaps

1. Missing Channels: [where they should be but aren't]
2. Underutilized Channels: [present but inactive]
3. Reputation Gaps: [where social proof is weak]
4. Authority Gaps: [where credibility is missing]

### Recommendations

1. [Channel/Area]: [specific action] → [realistic expected outcome]
2. [Channel/Area]: [specific action] → [realistic expected outcome]
3. [Channel/Area]: [specific action] → [realistic expected outcome]
```

---

## Quality Gate

- [ ] All nine channels in the Presence Score table are assessed, not left blank for "not researched"
- [ ] Every SEO/Reputation/Authority claim cites the search query or source that produced it
- [ ] Digital Presence Gaps covers all four named categories
- [ ] Recommendations are prioritized by realistic impact, each tied to a named gap
- [ ] No traffic, ranking, or follower numbers are stated without a verifiable source

---

## Tools Used

- `search_web` for external research
- `read_url_content` for social profiles
- `browser_subagent` for interactive platforms
