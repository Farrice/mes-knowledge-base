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

## Prompt

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

## Output Structure

### Digital Presence Score

| Channel | Status | Quality /10 | Activity | Notes |
|---------|--------|-------------|----------|-------|
| Website | | | | |
| LinkedIn (Company) | | | | |
| LinkedIn (Founder) | | | | |
| Instagram | | | | |
| Twitter/X | | | | |
| YouTube | | | | |
| TikTok | | | | |
| Podcast (own) | | | | |
| Podcast (guest) | | | | |

**Overall Score: __ / 10**

### SEO Signals

- **Domain Authority Signal:** (based on link presence, mentions)
- **Content Volume:** (number of indexed pages, blog activity)
- **Keyword Presence:** (do they rank for obvious terms?)
- **Technical Signals:** (site speed, mobile-friendly if observable)

### Reputation Analysis

#### Review Platforms

| Platform | Rating | # Reviews | Key Themes |
|----------|--------|-----------|------------|
| Google | | | |
| G2/Capterra | | | |
| Trustpilot | | | |
| BBB | | | |
| Industry-specific | | | |

#### Sentiment Summary
- **Positive Themes:** What do happy customers mention?
- **Negative Themes:** What do unhappy customers mention?
- **Response Pattern:** Does the business respond to reviews?

### Content Distribution

- **Primary Channel:** Where are they most active?
- **Content Frequency:** How often do they publish?
- **Engagement Level:** Do people interact with their content?
- **Content Type:** (educational, promotional, entertainment, mixed)

### Authority Signals

- **Press Coverage:** Any media mentions?
- **Speaking/Podcasts:** Founder visibility?
- **Partnerships:** Any notable affiliations?
- **Awards/Recognition:** Any third-party validation?

### Digital Presence Gaps

1. **Missing Channels:** Where should they be but aren't?
2. **Underutilized Channels:** Where are they present but inactive?
3. **Reputation Gaps:** Where is social proof weak?
4. **Authority Gaps:** Where is credibility missing?

### Recommendations

Prioritized by impact:

1. **[Channel/Area]:** [Specific action] → [Expected outcome]
2. **[Channel/Area]:** [Specific action] → [Expected outcome]
3. **[Channel/Area]:** [Specific action] → [Expected outcome]
```

---

## Expected Output

A digital presence map that:
- Shows exactly where the business is visible (and invisible)
- Identifies reputation risks or opportunities
- Prioritizes channel investments

---

## Tools Used

- `search_web` for external research
- `read_url_content` for social profiles
- `browser_subagent` for interactive platforms
