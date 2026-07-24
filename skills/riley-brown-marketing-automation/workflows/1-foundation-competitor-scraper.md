# Workflow: /riley-competitor-scraper

**Tier**: Foundation  
**Complexity**: Low  
**Time**: 1-3 minutes  
**Cost**: $0 (monthly Foreplay cost, ~$175-458)  
**APIs**: Foreplay, Notion  
**Output**: Notion database with longest-running competitor ads, ranked by duration

---

## Pre-Flight Gate

**When to Use**:
- You want to spy on 3-5 competitor ads across platforms
- You need to identify what ads are "working" (proxy: longest runtime)
- You're building a competitive intelligence database

**Prerequisites**:
- Foreplay API key (requires paid subscription, Tier 1+)
- Notion workspace + integration token
- List of 3-5 competitor names or domains

**Don't Use When**:
- You need actual ROI data (Foreplay only gives runtime, not performance)
- Competitors are brand-new or just launched (limited ad history)
- You need real-time engagement metrics (data is ~48h stale)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "Longest-Running Ads as ROI Proxy Heuristic"
2. `genius.md` — Section: "Comparative Analysis: The Audit Frame"
3. `SKILL.md` — Quick Reference: `/riley-competitor-scraper`
4. `references/api-integration-guide.md` — Section: "2. Foreplay API"
5. `references/notion-schema-templates.md` — Section: "Template 2: Competitor Ad Database"

**Key Concepts**:
- Duration (days running) is a proxy for performance (not ground truth)
- Longer runtime = likely profitable, but not guaranteed
- Foreplay returns: ad copy, creatives (images/video), platform, account info
- Notion schema follows API response shape (ads as records, sorted by duration)

---

## Execution

### Step 1: Define Competitor List

```
Competitors to analyze:
  1. [Competitor A] (domain or name)
  2. [Competitor B]
  3. [Competitor C]
  ... (up to 5 for Tier 1)
```

### Step 2: Call Foreplay API

For each competitor:

```bash
curl -H "Authorization: Bearer YOUR_FOREPLAY_KEY" \
  "https://api.foreplay.co/v1/ads?competitor=CompetitorA&limit=50&sort=duration"
```

**Response fields to capture**:
- `ad_id` (Foreplay ID)
- `platform` (Facebook, Instagram, TikTok, LinkedIn)
- `ad_type` (Static Image, Video, Carousel)
- `copy` (ad text)
- `creative_url` (image or video embed)
- `duration_days` (how long ad has been running)
- `last_seen` (date)
- `account_name` (who's running the ad)

### Step 3: Create Notion Database (or use existing)

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Create database
db = client.databases.create(
    parent={"page_id": "PARENT_PAGE_ID"},
    title="Competitor Ad Database",
    properties={
        "Competitor": {"select": {"options": [
            {"name": competitor} for competitor in ["CompetitorA", "CompetitorB", "CompetitorC"]
        ]}},
        "Ad ID": {"rich_text": {}},
        "Platform": {"select": {"options": [
            {"name": "Facebook"}, {"name": "Instagram"}, 
            {"name": "TikTok"}, {"name": "LinkedIn"}
        ]}},
        "Ad Type": {"select": {"options": [
            {"name": "Static"}, {"name": "Video"}, {"name": "Carousel"}
        ]}},
        "Duration (days)": {"number": {}},
        "Copy": {"rich_text": {}},
        "Hook": {"rich_text": {}},
        "Visual": {"file": {}},
        "CTA Text": {"rich_text": {}},
        "CTA Type": {"select": {"options": [
            {"name": "Sign Up"}, {"name": "Download"}, 
            {"name": "View More"}, {"name": "Buy"}
        ]}},
        "Success Pattern": {"rich_text": {}},
        "Last Seen": {"date": {}},
        "Account Name": {"rich_text": {}}
    }
)

return db['id']
```

### Step 4: Populate Notion Database

```python
# Collect all ads from all competitors
all_ads = []
for competitor in competitors:
    response = foreplay_api.search(competitor, limit=50)
    all_ads.extend(response['ads'])

# Sort by duration DESC
all_ads_sorted = sorted(all_ads, 
    key=lambda a: a['duration_days'], 
    reverse=True)

# Add to Notion
for ad in all_ads_sorted:
    # Extract hook from first 1-2 sentences of copy
    hook = ad['copy'].split('.')[0][:100]
    
    client.pages.create(
        parent={"database_id": db_id},
        properties={
            "Competitor": {"select": {"name": ad['competitor']}},
            "Ad ID": {"rich_text": [{"text": {"content": ad['ad_id']}}]},
            "Platform": {"select": {"name": ad['platform']}},
            "Ad Type": {"select": {"name": ad['ad_type']}},
            "Duration (days)": {"number": ad['duration_days']},
            "Copy": {"rich_text": [{"text": {"content": ad['copy'][:1000]}}]},
            "Hook": {"rich_text": [{"text": {"content": hook}}]},
            "CTA Text": {"rich_text": [{"text": {"content": ad.get('cta_text', 'N/A')}}]},
            "Last Seen": {"date": {"start": ad['last_seen']}},
            "Account Name": {"rich_text": [{"text": {"content": ad['account_name']}}]}
        }
    )

print(f"✓ Added {len(all_ads_sorted)} ads from {len(competitors)} competitors")
```

### Step 5: Create Views for Analysis

**View 1: "Longest Running"** (sort by Duration DESC)
- Shows which ads have been running longest (assume better ROI)

**View 2: "By Competitor"** (group by Competitor)
- Organize ads by competitor for side-by-side analysis

**View 3: "Video Only"** (filter: Ad Type = Video)
- Focus on video ads (higher production = higher stakes)

**View 4: "Elite Performers"** (filter: Duration > 90 days)
- Only ads running 3+ months (strong performers)

---

## Content Type Adaptations

### Video Ads (Facebook, Instagram, TikTok)
- Hook: Visual + audio (often 1-3 seconds to grab attention)
- Copy: Short + punchy (30-90 seconds total)
- CTA: Often swipe-up, link, or comment

### Static Image Ads (Facebook, Instagram, LinkedIn)
- Hook: Image + first 1-2 words of copy (scroll-stopping)
- Copy: Moderate length (50-200 words)
- CTA: Explicit button (Learn More, Sign Up, Buy)

### Carousel Ads
- Hook: First image + text combo
- Copy: Sequential story across 3-5 cards
- CTA: Usually on last card

---

## Output Requirements

**Notion Database**:
- ✓ Minimum 10 ads (to identify patterns)
- ✓ All fields populated (no gaps, especially Hook + CTA)
- ✓ Sorted by Duration (longest-running first)
- ✓ "Longest Running" view filtered to 90+ days
- ✓ "By Competitor" grouped correctly

**Quality Gate**:
- ✓ Hooks extracted from copy (not generic)
- ✓ CTAs identified and categorized
- ✓ Ad types match platform (video on TikTok, static on LinkedIn, etc.)
- ✓ Duration data is realistic (not all 30+ days, not all 5 days)

**Next Workflows**:
- Feed to `/riley-ad-performance-auditor` (deep analysis via Claude)
- Feed to `/riley-competitor-auditor` (with Luke Iha copywriting lens)

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Hooks are empty or placeholder
- [ ] CTAs are missing or generic
- [ ] All ads have exactly same duration (data validation issue)
- [ ] Fewer than 10 ads total (too few for patterns)
- [ ] Platform field shows wrong platform (API data corruption)

**Validation Checklist**:
1. Open "Longest Running" view; click top ad
2. Read the copy; assess if it sounds like a winning ad (subjective)
3. Check Duration field (should be 30-180 days for active competitors)
4. Count ads per competitor (should be balanced, e.g., 10-20 per competitor)
5. Skim 3 random hooks; verify they're distinct (not all generic CTAs)

**Anti-Patterns**:
- Do NOT assume longest-running = best (could be zombie ad with momentum)
- Do NOT ignore platform differences (TikTok ads look nothing like LinkedIn ads)
- Do NOT oversimplify CTA types (many ads have multiple CTAs)
- Do NOT miss that "longest running" is a proxy, not ground truth
- Do NOT mix sponsored content with organic (Foreplay only gives ads, so this is automatic)

---

## Troubleshooting

**"Foreplay API returns empty ads"**
→ Competitor may not be running paid ads in your region, or name is misspelled. Try:
  - Broadening date range (last 90 days, not 30)
  - Checking competitor's Ad Library manually first
  - Using company domain instead of brand name

**"Duration field shows 1-2 days for all ads"**
→ API may be returning recent ads only. Check Foreplay API docs; may need to adjust `date_from` parameter.

**"Hook field is too long or includes full copy"**
→ Truncate to first 100 characters in extraction logic; re-run Notion populate step.

**"Can't determine CTA type"**
→ Some ads have implicit CTAs (no button). Mark as "Implicit" or leave blank; categorize manually later.

---

## Next Steps After Completion

1. **Validate** in Notion (spot-check 5 ads)
2. **Feed to** `/riley-ad-performance-auditor` for Claude analysis
3. **Or feed to** `/riley-luke-copy-auditor` (copywriting lens)
4. **Archive old ads** (>180 days) quarterly to avoid re-counting
5. **Re-run monthly** to catch new competitive moves

**Downstreams**: `/riley-ad-performance-auditor`, `/riley-luke-copy-auditor`, `/riley-research-to-skill-pipeline`

