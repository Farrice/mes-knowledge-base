# API Integration Guide: Riley Brown Marketing Automation

**Purpose**: Document every API, cost, rate limit, and fallback for each Riley workflow.

---

## API Inventory (7 Core + 2 Optional)

### 1. ScrapeCreators API

**What It Does**: Scrapes social media content (videos, transcripts, engagement) from Instagram, YouTube, TikTok, and other platforms.

**Cost**:
- Free tier: 2 creators/month (limited data)
- Paid tier: $10-50 per creator (full data)
- Typical project: 10 creators = $100-500

**Rate Limits**:
- Free: 1 request/day
- Paid: 10 requests/day per API key

**Data Returned**:
- Video URLs + metadata
- Native captions (95%+ accuracy)
- Engagement metrics (likes, comments, shares, views)
- Video length, upload date, hashtags
- Creator profile info

**Authentication**: API key (obtain from ScrapeCreators dashboard)

**Codex Integration**:
```
/riley-social-scraper → [Calls ScrapeCreators] → Notion import
```

**Fallback (No API)**:
- Manual download via creator's channel
- Use YouTube/Instagram API directly (lower quality transcripts)
- Limit: 1-2 creators per month max

**Cost Justification**:
- $10-50 per creator is worth it if extracted patterns inform $5k+ in content spend
- Use free tier for 1 test creator first

**Rate Limit Handling**:
- Queue requests if hitting 10/day limit
- Batch 3-5 creators weekly (not all at once)

---

### 2. Foreplay API

**What It Does**: Scrapes competitor ads from Meta (Facebook + Instagram), TikTok, and other platforms. Returns longest-running ads, metadata, video/image files.

**Cost**:
- $175-458/month (tiered by ad volume)
- Cost is *flat* per month (unlimited queries within tier)
- Break-even: ~5 competitive analyses per month

**Rate Limits**:
- Tier 1 ($175): 100 ads/month
- Tier 2 ($300): 500 ads/month
- Tier 3 ($458): 2000 ads/month
- No daily limit (monthly allotment)

**Data Returned**:
- Ad copy (text)
- Ad creatives (images/video)
- Duration running (days/months)
- Platform + account info
- Engagement signals (implicit via runtime)
- *No* performance metrics (likes, clicks, ROI)

**Authentication**: API key (obtain from Foreplay dashboard)

**Codex Integration**:
```
/riley-competitor-scraper → [Foreplay API] → Notion import + ranking by duration
```

**Critical Limitation**:
- Duration is a *proxy* for performance (not ground truth)
- No actual ROI/CTR/conversion data
- Longer runtime = likely profitable, but not guaranteed

**Fallback (No API)**:
- Manual ad library search (Meta's Ad Library, TikTok Creator Fund)
- Limit: 3-5 competitors max, updated quarterly

**Cost Justification**:
- $175/mo for unlimited competitor intel is cheap if it informs $50k+ ad strategy
- Use for monthly competitive analysis (1-2 runnings per month)

**Rate Limit Handling**:
- Tier selection matters: start at Tier 1 ($175)
- If you hit monthly limit, upgrade tier mid-month (prorated)
- Archive old ads to avoid re-counting

---

### 3. Firecrawl API

**What It Does**: Scrapes websites and extracts structured data (text, images, metadata). Used for brand asset extraction (logos, colors, fonts).

**Cost**:
- Free tier: 100 pages/month
- Paid tier: $0.10-0.20 per page (scaled)
- Typical brand audit: 5-10 pages = $0.50-2.00

**Rate Limits**:
- Free: 1 request/second
- Paid: 5 requests/second

**Data Returned**:
- Page HTML + cleaned text
- Image URLs (extracted from page)
- Metadata (titles, descriptions, Open Graph tags)
- CSS styles (can extract colors, fonts)

**Authentication**: API key (obtain from Firecrawl dashboard)

**Codex Integration**:
```
/riley-brand-asset-scraper → [Firecrawl] → Extract logos, colors, fonts → Notion
```

**Typical Extraction**:
```python
import firecrawl

client = firecrawl.Client(api_key="YOUR_KEY")

# Scrape brand website
data = client.scrape_url("https://company.com")

# Extract color palette (from CSS)
colors = extract_colors_from_css(data['css'])

# Extract fonts
fonts = extract_fonts_from_css(data['css'])

# Save to Notion
notion.add_to_database("Brand Kit", {
    "Company": "Company Name",
    "Logo": data['images'][0],
    "Primary Colors": colors,
    "Fonts": fonts
})
```

**Fallback (No API)**:
- Manual brand guide download (often available as PDF)
- Screenshot colors from website
- Limit: 1-2 brand audits per project

**Cost Justification**:
- $2 for full brand asset extraction is cheap if it saves 30 mins of manual work
- Use for new competitor audits

---

### 4. Notion API

**What It Does**: Create/update Notion databases, add records, query data. Core to Riley's data warehouse approach.

**Cost**: Free (included with Notion subscription)

**Rate Limits**:
- 3 requests per second per API key
- Generous; rarely hit in practice

**Data Operations**:
- Create database: 1 request
- Add 100 records: 100 requests
- Update property: 1 request per property

**Authentication**: Integration API key (create in Notion Settings → Integrations)

**Codex Integration**:
```
All Riley workflows → [Notion API] → Database create/update/query
```

**Typical Workflow**:
```python
import notion_client

client = notion_client.Client(auth="YOUR_TOKEN")

# Create database
db = client.databases.create(
    parent={"page_id": "PAGE_ID"},
    title="Creator Video Database",
    properties={
        "Creator": {"title": {}},
        "Platform": {"select": {"options": [{"name": "YouTube"}, {"name": "Instagram"}]}},
        "URL": {"url": {}},
        "Engagement Score": {"number": {}}
    }
)

# Add records
for video in scrape_creators_output:
    client.pages.create(
        parent={"database_id": db['id']},
        properties={
            "Creator": {"title": [{"text": {"content": video['creator_name']}}]},
            "Platform": {"select": {"name": video['platform']}},
            "URL": {"url": video['url']},
            "Engagement Score": {"number": video['engagement']}
        }
    )
```

**Fallback (No API)**:
- Export data to CSV, import manually to Notion
- Limit: One-time use (loses automation)

**Cost Justification**:
- Free; use for all workflows
- Notion subscription ($8-10/mo) is core cost, not per-workflow

---

### 5. Gmail API

**What It Does**: Send emails (draft schedules to reviewers, send notifications).

**Cost**: Free (included with Google Workspace account)

**Rate Limits**:
- 250 requests per user per second
- Generous; rarely hit in practice

**Codex Integration**:
```
/riley-content-calendar-orchestrator → [Gmail API] → Send draft to reviewer
```

**Typical Workflow**:
```python
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

service = build('gmail', 'v1', credentials=creds)

# Send email
message = {
    'raw': base64.urlsafe_b64encode(email.as_bytes()).decode()
}

service.users().messages().send(userId='me', body=message).execute()
```

**Fallback (No API)**:
- Manual email (copy/paste draft)
- Limit: 1-2 per day max

**Cost Justification**:
- Free; use in all workflows that need notifications

---

### 6. Cal.com API

**What It Does**: Create/manage calendar events. Used for scheduling content across multiple dates.

**Cost**:
- Free tier: Basic scheduling
- Paid tier: $12-100/mo (pro features)

**Rate Limits**:
- Free: 100 events/month
- Paid: Unlimited

**Codex Integration**:
```
/riley-content-calendar-orchestrator → [Cal.com API] → Create calendar events
```

**Typical Workflow**:
```python
import requests

headers = {"Authorization": f"Bearer YOUR_API_KEY"}

# Create event
event = {
    "title": "Post LinkedIn content",
    "startTime": "2026-08-01T09:00:00Z",
    "endTime": "2026-08-01T10:00:00Z",
    "description": "Post Kallaway-style LinkedIn content"
}

response = requests.post(
    "https://api.cal.com/v1/events",
    json=event,
    headers=headers
)
```

**Fallback (No API)**:
- Manual calendar entry
- Limit: 1-2 per week max

**Cost Justification**:
- Free tier covers most projects; upgrade if >100 posts/month

---

### 7. Claude/GPT-5.6 API (LLM for Pattern Analysis)

**What It Does**: Analyze scraped content, extract patterns, generate summaries.

**Cost**:
- Claude: $0.03-0.10 per 1K input tokens, $0.15-0.30 per 1K output tokens (varies by model)
- GPT-5.6: $0.05 per 1K tokens (approx, pricing varies)
- Typical analysis: 10K tokens input + 5K tokens output = ~$0.50-1.00

**Reasoning Levels**:
- Standard: $0.50-1.00 per analysis
- Extra-high: $5-20 per analysis (10-20x more expensive)

**Use Extra-High When**:
- Analyzing 10+ competitor ads
- Synthesizing patterns across 5+ creators
- Predicting which content will perform

**Use Standard When**:
- Simple transcription → summary
- Tag extraction (hook type, CTA, etc.)
- Single-creator pattern extraction

**Rate Limits**:
- Claude: 5M tokens/min (typically no limit hit)
- GPT-5.6: 3.5M tokens/min (typically no limit hit)

**Codex Integration**:
```
/riley-creator-profile-analyzer → [Claude extra-high] → Notion insights
/riley-ad-performance-auditor → [Claude extra-high] → Notion analysis
```

**Typical Prompts**:

**Standard (single creator)**:
```
Analyze these 5 Kallaway YouTube video transcripts. Extract:
1. Hook formula (first 30 seconds)
2. Problem statement
3. Solution presentation
4. Call-to-action

Return as JSON.
```
Cost: ~$0.50

**Extra-High (comparative)**:
```
Compare these 15 competitor ads (Quad.ai, Replit, Claude, ChatGPT, Perplexity).
Analyze:
1. Success pattern (what makes each ad work)
2. Common elements across winners
3. Hook types (question, statistic, emotion, story)
4. CTA effectiveness
5. Predicted ROI ranking (longest-running first, then by pattern strength)

Return as detailed JSON with citations.
```
Cost: ~$10-15

**Fallback (No LLM)**:
- Manual pattern review (no automation)
- Limit: 1-2 creators per month

**Cost Justification**:
- $0.50-1.00 per analysis is cheap if it saves 30 mins of manual work
- Extra-high is worth it for competitive analysis ($10-15 × 4/month = $40-60/mo budget)

---

## Optional APIs (For Advanced Workflows)

### 8. YouTube API

**When to Use**: If you want additional YouTube-specific metrics (subscriber growth, monthly views over time)

**Cost**: Free (limited quota)

**Data**: Channel info, video statistics, comments (limited)

**Limitation**: No transcript access (use ScrapeCreators instead)

---

### 9. Paper API (Edge-Case Dashboard)

**When to Use**: If you want real-time dashboard of workflow execution

**Cost**: Free (included with Paper subscription)

**Integration**: Agent populates Paper doc as it executes (real-time UI)

---

## Monthly Budget Estimate

**Scenario 1: Solo Founder (Tier 1 Foundation)**
- ScrapeCreators: $0 (free tier, 1 creator)
- Foreplay: $0 (skip for now)
- Firecrawl: $2-5
- Notion: $8-10
- Claude: $10-20 (light pattern analysis)
- **Total: ~$20-35/month**

**Scenario 2: Small Team (Tier 2 Practitioner)**
- ScrapeCreators: $100-200 (10-20 creators)
- Foreplay: $175 (Tier 1, unlimited ads)
- Firecrawl: $5-10
- Notion: $8-10
- Claude: $50-100 (regular + extra-high)
- Gmail/Cal.com: Free
- **Total: ~$340-500/month**

**Scenario 3: Agency (Tier 3 Full Stack)**
- ScrapeCreators: $500-1000 (50-100 creators)
- Foreplay: $458 (Tier 3, 2000 ads/month)
- Firecrawl: $20-50
- Notion: $10 (team workspace)
- Claude: $300-500 (heavy analysis)
- Gmail/Cal.com: Free
- **Total: ~$1,300-2,000/month**

---

## Fallback Strategy (If APIs Are Unavailable)

| API | Primary | Fallback 1 | Fallback 2 | Time/Cost Impact |
|-----|---------|-----------|-----------|-----------------|
| ScrapeCreators | Automated scrape | YouTube/Instagram API | Manual download | +200% time, -cost |
| Foreplay | Competitor ads | Meta Ad Library (manual) | Manual research | +500% time, -cost |
| Firecrawl | Brand asset extraction | Manual screenshot | Brand guide PDF | +100% time, -cost |
| Notion | Database creation | CSV export | Google Sheets | -automation, +manual |
| Gmail | Send notifications | Manual email | Slack webhook | -cost, +manual |
| Cal.com | Schedule events | Google Calendar API | Manual entry | +time, -automation |
| Claude/GPT | Pattern analysis | Manual review | Cheaper model | +time, -quality |

---

## Security Best Practices

1. **API Keys**: Store in environment variables, never in code
   ```bash
   export SCRAPECREATORS_API_KEY="xxx"
   export FOREPLAY_API_KEY="xxx"
   ```

2. **Notion Integration**: Create dedicated integration (don't share org-wide key)

3. **Gmail/Cal.com**: Use OAuth2 with scoped permissions (not service account)

4. **Rate Limiting**: Implement exponential backoff for retries
   ```python
   import time
   
   for attempt in range(3):
       try:
           response = api_call()
           break
       except RateLimitError:
           wait_time = 2 ** attempt
           time.sleep(wait_time)
   ```

5. **Monitoring**: Log all API costs weekly to detect spikes

---

## Testing Your APIs

Before deploying a workflow, test each API:

```bash
# Test ScrapeCreators
curl -H "Authorization: Bearer YOUR_KEY" \
  "https://api.scrapecreators.com/v1/search?creator=kallaway&platform=instagram"

# Test Foreplay
curl -H "Authorization: Bearer YOUR_KEY" \
  "https://api.foreplay.co/v1/ads?competitor=quad.ai&limit=10"

# Test Firecrawl
curl -H "Authorization: Bearer YOUR_KEY" \
  "https://api.firecrawl.dev/v1/scrape?url=https://example.com"

# Test Notion
curl -H "Authorization: Bearer YOUR_KEY" \
  -H "Notion-Version: 2022-06-28" \
  "https://api.notion.com/v1/databases"

# Test Claude
curl -H "Authorization: Bearer sk-YOUR_KEY" \
  -X POST https://api.anthropic.com/v1/messages \
  -d '{"model": "claude-opus", "max_tokens": 100, "messages": [{"role": "user", "content": "Hello"}]}'
```

---

## Troubleshooting

**"ScrapeCreators rate limit exceeded"**
→ Wait 24 hours or upgrade plan. Use free tier to test first.

**"Foreplay API returns empty ads"**
→ Competitor may not be running ads in selected regions. Broaden date range.

**"Firecrawl fails to extract images"**
→ Website may block scraping (robots.txt). Use manual screenshot as fallback.

**"Notion import times out"**
→ Batch in smaller chunks (100 records at a time, not 1000).

**"Claude analysis is too expensive"**
→ Use standard reasoning, not extra-high. Or use cheaper model (GPT-3.5 instead of GPT-4).

---

**Master Guide**: SKILL.md (workflow overview)  
**Workflow Templates**: `workflows/*.md` (per-workflow API usage)
