# Workflow: /riley-social-scraper

**Tier**: Foundation  
**Complexity**: Low  
**Time**: 2-5 minutes  
**Cost**: $10-50 (ScrapeCreators) + $0 (Notion)  
**APIs**: ScrapeCreators, Notion  
**Output**: Notion database with videos, transcripts, engagement metrics

---

## Pre-Flight Gate

**When to Use**:
- You want to extract patterns from 1+ creators (any platform)
- You need video transcripts + engagement data in a structured format
- You're building a creator intelligence database

**Prerequisites**:
- ScrapeCreators API key (free tier or paid)
- Notion workspace + integration token
- Creator name(s) and platform(s) (YouTube, Instagram, TikTok, etc.)

**Don't Use When**:
- Creator is private or gated (API can't access)
- You only need <3 data points (patterns too noisy)
- You need real-time engagement (API data is ~48h stale)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "The Scrape→DB→Analyze Loop"
2. `SKILL.md` — Quick Reference: `/riley-social-scraper`
3. `references/api-integration-guide.md` — Section: "1. ScrapeCreators API"
4. `references/notion-schema-templates.md` — Section: "Template 1: Creator Video Database"

**Key Concepts**:
- ScrapeCreators returns video URLs, native transcripts (95%+ accuracy), engagement metrics
- Notion schema emerges from API response shape (don't pre-design; let data lead)
- Engagement ranking: likes + 2×comments + 5×shares (composite score)
- Sponsored content is marked; filter for authentic-only analysis later

---

## Execution

### Step 1: Prep ScrapeCreators Request

```
Input:
  - Creator name: [e.g., "Kallaway"]
  - Platform: [YouTube|Instagram|TikTok|LinkedIn]
  - Limit: 10 (best videos by engagement)
  - Data types: videos, transcripts, engagement
```

### Step 2: Call ScrapeCreators API

```bash
curl -H "Authorization: Bearer YOUR_SCRAPECREATORS_KEY" \
  "https://api.scrapecreators.com/v1/search?creator=Kallaway&platform=youtube&limit=10"
```

**Response fields to capture**:
- `video_id`, `title`, `url`, `platform`
- `transcript` (native captions)
- `engagement`: likes, comments, shares, views
- `metadata`: upload_date, duration, thumbnail_url
- `is_sponsored` (boolean)

### Step 3: Create Notion Database (or use existing)

**If new database**:

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Create database
db = client.databases.create(
    parent={"page_id": "PARENT_PAGE_ID"},
    title=f"{creator_name} Video Database",
    properties={
        "Creator": {"title": {}},
        "Platform": {"select": {"options": [
            {"name": "YouTube"}, {"name": "Instagram"}, 
            {"name": "TikTok"}, {"name": "LinkedIn"}
        ]}},
        "Video Title": {"rich_text": {}},
        "URL": {"url": {}},
        "Transcript": {"rich_text": {}},
        "Likes": {"number": {}},
        "Comments": {"number": {}},
        "Shares": {"number": {}},
        "Views": {"number": {}},
        "Engagement Score": {"formula": {"expression": "prop(\"Likes\") + prop(\"Comments\") * 2 + prop(\"Shares\") * 5"}},
        "Upload Date": {"date": {}},
        "Duration (seconds)": {"number": {}},
        "Hook Style": {"select": {"options": [
            {"name": "Story"}, {"name": "Question"}, 
            {"name": "Statistic"}, {"name": "Emotion"}
        ]}},
        "Is Sponsored": {"checkbox": {}},
        "Rank": {"number": {}}
    }
)

return db['id']
```

### Step 4: Populate Notion with Videos

```python
# Sort by engagement (ScrapeCreators API may return sorted, but verify)
videos_sorted = sorted(videos, 
    key=lambda v: v['likes'] + 2*v['comments'] + 5*v['shares'], 
    reverse=True)

# Add each video as a page
for rank, video in enumerate(videos_sorted, 1):
    client.pages.create(
        parent={"database_id": db_id},
        properties={
            "Creator": {"title": [{"text": {"content": creator_name}}]},
            "Platform": {"select": {"name": video['platform']}},
            "Video Title": {"rich_text": [{"text": {"content": video['title']}}]},
            "URL": {"url": video['url']},
            "Transcript": {"rich_text": [{"text": {"content": video['transcript'][:2000]}}]},  # Truncate if needed
            "Likes": {"number": video['likes']},
            "Comments": {"number": video['comments']},
            "Shares": {"number": video['shares']},
            "Views": {"number": video['views']},
            "Upload Date": {"date": {"start": video['upload_date']}},
            "Duration (seconds)": {"number": video['duration']},
            "Is Sponsored": {"checkbox": video['is_sponsored']},
            "Rank": {"number": rank}
        }
    )

print(f"✓ Added {len(videos_sorted)} videos to Notion")
```

### Step 5: Create Views for Analysis

**View 1: "Top 10"** (sort by Engagement Score DESC, limit 10)
**View 2: "Authentic Only"** (filter: Is Sponsored = false)
**View 3: "By Hook Style"** (group by Hook Style)

---

## Content Type Adaptations

### YouTube
- Transcripts: Use native captions (ScrapeCreators includes these)
- Engagement: Views > Likes > Comments (YouTube's metric hierarchy)
- Metadata: Include channel subscriber count if available

### Instagram Reels / TikTok
- Transcripts: ScrapeCreators auto-transcribes video audio
- Engagement: Shares + Saves weight higher than Likes
- Metadata: Include trending audio/hashtags

### LinkedIn
- Transcripts: Less common; may require fallback to manual note-taking
- Engagement: Comments > Reactions (LinkedIn conversation depth > volume)
- Metadata: Include connection count of author

---

## Output Requirements

**Notion Database**:
- ✓ Minimum 5 videos (to avoid pattern noise)
- ✓ All fields populated (no gaps)
- ✓ Engagement Score formula working
- ✓ Top 10 view sorted correctly
- ✓ Authentic Only view filtering properly

**Paper Integration** (optional):
```
Paper doc summarizing:
- Creator name + platform
- Date range of videos
- Average engagement score
- Top hook style observed
```

**Next Workflow**:
- Feed this database to `/riley-skill-extractor` (extract patterns)
- Feed to `/riley-creator-profile-analyzer` (comparative analysis)

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Transcripts are empty or placeholder (API returned no captions)
- [ ] Engagement metrics are all zeros (API not returning data)
- [ ] Is Sponsored field not populated (skipped filtering step)
- [ ] Database has <3 videos (too noisy for pattern extraction)
- [ ] Engagement Score formula errors (Notion formula syntax issue)

**Validation Checklist**:
1. Open database in Notion; click "Top 10" view
2. Verify top 3 videos have highest Engagement Scores
3. Click "Authentic Only" view; count videos marked Is Sponsored = true (should be few)
4. Read one transcript end-to-end; assess quality (full? readable?)
5. Check Upload Date range (should span last 2-3 months if creator is active)

**Anti-Patterns**:
- Do NOT cherry-pick videos manually; let engagement rank them
- Do NOT skip is_sponsored; it corrupts voice extraction later
- Do NOT truncate transcripts to <1000 chars; lose context
- Do NOT use paid tier for 1-2 test creators; start free
- Do NOT re-scrape same creator weekly; refresh monthly at most

---

## Troubleshooting

**"ScrapeCreators rate limit exceeded"**
→ Free tier is 1 request/day. Wait 24h or upgrade to paid.

**"Notion API returns 'invalid_property'"**
→ Database property name doesn't match schema. Re-check spelling (case-sensitive).

**"Transcripts come back empty"**
→ Creator's platform doesn't embed captions, or video is too new. Fallback: use YouTube API directly or manual transcript from YouTube CC download.

**"Engagement Score formula shows #ERROR"**
→ One of the number fields is empty. Add default value (0) or re-check Notion formula syntax.

---

## Next Steps After Completion

1. **Validate** the database in Notion (spot-check 3 videos)
2. **Feed to** `/riley-skill-extractor` to turn patterns into callable skill
3. **Or feed to** `/riley-creator-profile-analyzer` for comparative analysis
4. **Archive** if using as historical reference (don't re-scrape same creator for 30 days)

**Downstreams**: `/riley-skill-extractor`, `/riley-creator-profile-analyzer`, `/riley-research-to-skill-pipeline`

