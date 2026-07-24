# SKILL: Riley Brown's AI-Native Marketing Automation

**Tier**: Deep (Forge-Grade)  
**Domain**: Marketing automation, competitive intelligence, creator extraction, Notion data ops  
**Author/Source**: Riley Brown (Codex Workflow Demonstration, 2026)  
**Last Updated**: 2026-07-24  
**Status**: Production-Ready (Tier 1 foundations shipped; Tier 2-3 extensible)

---

## Quick Reference

**Goal**: Build marketing automation workflows that scrape creators/competitors → ingest into Notion → extract callable patterns → generate content in learned voice.

**Core Loop**: Scrape → Database → Analyze → Extract → Extend

**Key APIs**: ScrapeCreators ($10-50/creator), Foreplay ($175-458/mo), Firecrawl ($0-99/mo), Notion, Gmail, Paper

**Average Cost Per Workflow**: $10-100 (varies by scale)

**Output Types**: Notion databases, callable skills (voice generators), competitive audit reports, structured pattern libraries

---

## Workflow Table (12 Workflows Across 3 Tiers)

| Tier | Workflow | Description | APIs | Time | Cost | Downstream |
|------|----------|-------------|------|------|------|------------|
| **Foundation** | `/riley-social-scraper` | Scrape any creator (Instagram/YouTube/TikTok) → Notion DB + transcripts + videos | ScrapeCreators, Notion | 2-5 min | $10-50 | Extractor, Analyzer |
| Foundation | `/riley-skill-extractor` | Turn creator DB → callable skill (voice generator) | Claude/GPT-5.6, Notion | 3-10 min | $5-20 | Any content workflow |
| Foundation | `/riley-competitor-scraper` | Foreplay API → longest-running competitor ads → Notion | Foreplay, Notion | 1-3 min | $0 (monthly) | Ad Auditor, Analyzer |
| **Practitioner** | `/riley-creator-profile-analyzer` | Who's winning, why (patterns), HOW to copy | Claude (extra-high), Notion | 5-15 min | $20-50 | Voice generator, Copy engine |
| Practitioner | `/riley-ad-performance-auditor` | Competitor ads + written analysis (success factors, hooks, CTAs) | Foreplay, Claude (extra-high), Notion | 5-20 min | $10-30 | Ad network, Copywriting |
| Practitioner | `/riley-brand-asset-scraper` | Firecrawl → extract logos, colors, fonts, brand patterns | Firecrawl, Notion | 2-5 min | $0-10 | Design workflows, Brand audit |
| Practitioner | `/riley-content-calendar-orchestrator` | Notion + Cal.com + Gmail drafts → auto-schedule content + send to reviewers | Notion, Gmail, Cal.com, Claude | 10-30 min | $5-15 | Publishing, Distribution |
| Practitioner | `/riley-engagement-trend-detector` | Video transcript + comment analysis → spot rising/falling engagement patterns over time | YouTube API, Claude, Notion | 5-10 min | $5-10 | Timing optimization, Format pivot |
| Practitioner | `/riley-research-to-skill-pipeline` | Research topic → find creators → extract skills → generate content → schedule | All (full stack) | 20-60 min | $30-100 | Publishing, Ad deployment |
| **Stacking** | `/riley-lara-amplifier` | Find LinkedIn examples (research) + schedule via Lara voice (copy) + deploy | Riley + Lara Acosta skill | 15-30 min | $20-40 | LinkedIn content hub |
| Stacking | `/riley-luke-copy-auditor` | Competitor ads + Luke Iha persuasion checklist (copywriting lens) | Riley + Luke Iha skill | 10-20 min | $15-35 | Copy refinement, Testing |
| Stacking | `/riley-farrice-parallax-pipeline` | Research → scrape → design (Satori) → schedule (Parallax) → distribute | Riley + Farrice voice + Satori + Parallax | 30-90 min | $50-150 | Substack, LinkedIn, Twitter |

---

## Stacking Guide (Multi-Expert Workflows)

### Tier 2 (Practitioner) Extensions

**Riley + Lara Acosta (LinkedIn Growth)**:
- Use `/riley-creator-profile-analyzer` to find LinkedIn creators in fitness/coaching
- Export profiles to Lara's `/ghostwrite` workflow
- Lara generates LinkedIn content in their voice
- Schedule via `/riley-content-calendar-orchestrator`

**Riley + Luke Iha (Copywriting)**:
- Use `/riley-ad-performance-auditor` to surface competitor ad copy
- Feed copy samples to Luke's `/luke-iha-vicious-hooks` or `/luke-iha-vsl-leads`
- Luke audits for persuasion gaps
- Refine + re-test

**Riley + Nathan Gotch (SEO)**:
- Use `/riley-research-to-skill-pipeline` to identify high-traffic content creators
- Export to Nathan's `/nathan-gotch` workflow for keyword mapping
- Discover long-tail content opportunities

### Tier 3 (Stacking) Integrated Workflows

**Full Parallax Pipeline** (`/riley-farrice-parallax-pipeline`):
1. Research a market (e.g., "AI tools for solopreneurs")
2. `/riley-research-to-skill-pipeline`: Find top creators in that space
3. Extract patterns → Notion database
4. Use Farrice voice (`/voice-os` BLEND mode) to write Substack essay
5. Export to Satori (`/satori-frontend-flow`) for visual design
6. Schedule via Parallax (`/parallax` workflow)
7. Distribute across LinkedIn + Twitter via Farrice brand

**System Monitor** (`/riley-system-monitor`):
- Track API costs, usage, execution time across all Riley workflows
- Monthly spend summary
- Alert if Foreplay/ScrapeCreators costs spike
- Optimization recommendations

---

## When to Use Riley (Pre-Flight Gate)

**Use Riley when**:
- ✅ You need to extract patterns from 1+ creators (any platform)
- ✅ You want to spy on competitor ads (Foreplay)
- ✅ You need a structured Notion database of content + metadata
- ✅ You want to generate content in a creator's learned voice
- ✅ You're building a content calendar across multiple creators
- ✅ You need a "who's winning" competitive analysis
- ✅ You want to automate creator research (vs. manual scrolling)

**Don't use Riley when**:
- ❌ You need *real-time* social media metrics (engagement API limits apply)
- ❌ You're analyzing private/gated content (API scraping won't access)
- ❌ You need to extract patterns from <3 data points (too noisy)
- ❌ Your creators are primarily on platforms without API support (some niche platforms)
- ❌ You need licensed competitor data (Foreplay is crowdsourced; not guaranteed accuracy)

---

## Quick Workflow Reference

### Foundation Tier (Copy-Paste Ready)

#### 1. `/riley-social-scraper`
```
Prompt: "Please scrape [Creator Name] on [Platform]. Get the best 10 videos. Return transcripts, engagement metrics, and create a Notion database."

Expected Output: 
- Notion database with 10 videos, ranked by engagement
- Video embeds + native captions
- Engagement metrics (likes, comments, shares)
```

#### 2. `/riley-skill-extractor`
```
Prompt: "Using the Notion database from /riley-social-scraper, extract the key patterns from [Creator Name]'s top 5 videos. Turn this into a callable skill template."

Expected Output:
- Skill definition in `/skills/[creator-name]-voice/SKILL.md`
- Workflow template for generating content in that voice
- Pattern tags (hook style, pacing, CTA type, etc.)
```

#### 3. `/riley-competitor-scraper`
```
Prompt: "Using Foreplay API, scrape the longest-running ads from [Competitor A], [Competitor B], [Competitor C]. Create a Notion database ranked by duration."

Expected Output:
- Notion database with competitor ads, sortable by duration
- Video/image embeds
- Copy excerpts
```

### Practitioner Tier (Requires Setup)

#### 4. `/riley-creator-profile-analyzer`
```
Requires: Notion database from /riley-social-scraper

Prompt: "Analyze [Creator Name]'s profile. Who are their viewers? What topics drive engagement? What's their persuasion formula? Generate a profile card."

Uses: Claude (extra-high reasoning), Notion

Expected Output:
- Creator profile: audience demographics, topic clusters, persuasion style
- Top 3 hooks (extracted from videos)
- Audience sentiment analysis
- Recommended content angles for replication
```

#### 5. `/riley-ad-performance-auditor`
```
Requires: Notion database from /riley-competitor-scraper

Prompt: "These ads have been running for [9 months / 6 months / etc.]. Analyze the winning copy, hooks, and CTAs. What makes them work? Provide actionable patterns."

Uses: Foreplay, Claude (extra-high), Notion

Expected Output:
- Structured ad analysis: Hook Pattern, Body Copy Strategy, CTA Mechanism
- Comparative breakdown (what competitors do, why it works)
- Recommendations for your own ads
```

#### 6. `/riley-brand-asset-scraper`
```
Prompt: "Using Firecrawl, scrape [Company Domain]. Extract: logo, primary colors (hex), fonts, imagery style, brand tone. Create a brand asset database."

Uses: Firecrawl, Notion

Expected Output:
- Notion brand kit: logo (image), colors (palette), fonts (names), tone voice
- Visual examples from website
- Design guidelines extracted from site
```

### Stacking Tier (Multi-Skill)

#### 10. `/riley-lara-amplifier`
```
Requires: /riley-creator-profile-analyzer output + Lara Acosta skill

Workflow:
1. Riley finds top LinkedIn creators in [niche]
2. Extract their voice/style
3. Hand off to Lara's /ghostwrite workflow
4. Lara generates LinkedIn posts in that style
5. Schedule via /riley-content-calendar-orchestrator

Cost: ~$25-40 (Riley $15 + Lara $10-25)
Time: 15-30 min
Output: 5-10 scheduled LinkedIn posts
```

---

## Notion Schema Templates (Copy These)

See `references/notion-schema-templates.md` for full schemas. Quick examples:

### Template 1: Creator Video Database
```
Fields:
- Creator (text)
- Platform (select: YouTube, Instagram, TikTok)
- Video Title (text)
- URL (url)
- Video Embed (file)
- Transcript (rich text)
- Engagement Score (formula: likes + 2*comments + 5*shares)
- Rank (number, auto-sort by Engagement Score DESC)
- Hook Style (select: Story, Question, Statistic, Emotion)
- Hook Text (text)
- Scripting Pattern (text)
- Audience Segment (text)
- Is Sponsored (checkbox)

Views:
- All Videos (default)
- Authentic Only (filter: Is Sponsored = false)
- Top 10 (sort: Engagement Score DESC, limit 10)
```

### Template 2: Competitor Ad Database
```
Fields:
- Competitor (select: list of competitors)
- Ad ID (Foreplay ID)
- Ad Type (select: Static, Video, Carousel)
- Platform (select: Facebook, Instagram, TikTok, LinkedIn)
- Duration (number: months running)
- Copy (text)
- Hook (text, extracted)
- Visual (image embed)
- CTA Text (text)
- CTA Type (select: Sign Up, Download, View More, Buy)
- Success Pattern (text)
- Last Seen (date)

Views:
- All Ads (default)
- Longest Running (sort: Duration DESC)
- By Competitor (group by Competitor)
- Video Only (filter: Ad Type = Video)
```

---

## API Integration Summary

| API | Cost | Rate Limit | Purpose | Fallback |
|-----|------|-----------|---------|----------|
| **ScrapeCreators** | $10-50/creator | 10 creators/day | Scrape social media + transcripts | Manual research |
| **Foreplay** | $175-458/mo | Unlimited within plan | Scrape competitor ads | Basic competitor research |
| **Firecrawl** | $0-99/mo | Varies by tier | Extract brand assets from websites | Manual download |
| **Notion API** | Included | 3 req/sec | Create/update databases, properties | CSV export |
| **Gmail API** | Included | 250 req/sec | Send draft schedules to reviewers | Manual email |
| **Cal.com API** | Free tier available | Varies | Schedule content calendar | Manual calendar |
| **Claude/GPT-5.6** | $0.03-0.10 per 1K tokens (varies by model) | 50 req/min | Pattern extraction, analysis | Use cheaper model |

---

## Common Questions

**Q: How do I know if a pattern extraction is good?**  
A: Use the Quality Rubric in `genius.md`. Score on 8 dimensions (Fidelity, Scalability, API Clarity, etc.). Aim for composite >7/10.

**Q: Can I extract from just 1 creator?**  
A: Yes, but patterns are noisier. 3+ creators give better signal. 10+ creators give strong patterns.

**Q: How often should I re-run extractions?**  
A: Monthly for active creators, quarterly for stable ones. Patterns degrade as creators evolve.

**Q: What if the creator has sponsored content?**  
A: Filter it out (`is_sponsored = false`). Sponsored delivery corrupts authentic voice.

**Q: Can I combine patterns from multiple creators?**  
A: Yes. Use `/riley-creator-profile-analyzer` on a cohort (e.g., top 5 fitness YouTubers), then identify *common* patterns across all 5.

**Q: What's the cheapest way to run all 12 workflows?**  
A: Foundation tier only (~$20-50/mo). Tier 2 adds $50-100/mo. Tier 3 (stacking) scales with usage.

**Q: Can I use this without Notion?**  
A: Not recommended. Notion is core to Riley's approach (data warehouse + UI). You'd need a custom DB + dashboard.

**Q: Do I need ScrapeCreators? Can I use YouTube API directly?**  
A: YouTube API works for public videos but lacks transcripts + ranking. ScrapeCreators includes native captions (higher quality). Use ScrapeCreators if budget allows.

---

## What's Next (Extensions Not Yet Built)

- **Predictive Analysis**: Train model on past Foreplay data to predict which ads will run long
- **Platform-Specific Variations**: Separate extraction logic for YouTube vs. TikTok hooks (different pacing)
- **Multi-Creator Synthesis**: Automatically identify meta-patterns across 10+ creators
- **Feedback Loop**: Create mechanism to validate extracted patterns against held-out test set
- **Cost Optimization**: Auto-select cheaper model when high reasoning isn't needed

---

## File Structure

```
skills/riley-brown-marketing-automation/
├── SKILL.md                          (this file)
├── genius.md                         (patterns, exemplars, rubric)
├── workflows/
│   ├── 1-foundation-social-scraper.md
│   ├── 1-foundation-skill-extractor.md
│   ├── 1-foundation-competitor-scraper.md
│   ├── 2-practitioner-creator-analyzer.md
│   ├── 2-practitioner-ad-auditor.md
│   ├── 2-practitioner-brand-scraper.md
│   ├── 2-practitioner-content-calendar.md
│   ├── 2-practitioner-engagement-detector.md
│   ├── 2-practitioner-research-pipeline.md
│   ├── 3-stacking-lara-amplifier.md
│   ├── 3-stacking-luke-auditor.md
│   └── 3-stacking-system-monitor.md
└── references/
    ├── api-integration-guide.md
    └── notion-schema-templates.md
```

---

## For Experts Integrating Riley

**If you're Lara** (LinkedIn ghostwriting):
- Input: Creator profile from `/riley-creator-profile-analyzer`
- Use to understand audience + voice
- Generate LinkedIn posts in that creator's style
- Export: `/ghostwrite` workflow feeds into `/riley-content-calendar-orchestrator`

**If you're Luke** (Copywriting):
- Input: Competitor ad copy from `/riley-ad-performance-auditor`
- Audit for persuasion gaps (hooks, proof, urgency, clarity)
- Export: Recommendations back to `/riley-ad-performance-auditor` for refinement

**If you're Nathan** (SEO):
- Input: High-traffic creators from `/riley-research-to-skill-pipeline`
- Keyword mapping + opportunity identification
- Export: Content calendar updates to Notion

**If you're Farrice** (Brand voice, strategy):
- Input: Market research from Riley scraper
- Voice calibration (BLEND mode from `/voice-os`)
- Output: Parallax pipeline (`/riley-farrice-parallax-pipeline`)

---

**Master Document**: `genius.md` (read first for deep context)  
**Entrypoint**: `/riley-social-scraper` (start here to build your first creator database)  
**Stacking Hub**: This SKILL.md (navigate multi-expert workflows)
