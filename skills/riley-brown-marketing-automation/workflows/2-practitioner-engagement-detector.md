# Workflow: /riley-engagement-trend-detector

**Tier**: Practitioner  
**Complexity**: Medium  
**Time**: 5-10 minutes  
**Cost**: $5-10 (Claude standard reasoning)  
**APIs**: Claude, Notion, YouTube API (optional)  
**Output**: Engagement trend analysis (rising/falling patterns, format pivots, timing optimization)

---

## Pre-Flight Gate

**When to Use**:
- You want to spot which content formats/topics are gaining/losing momentum
- You're identifying opportunities to pivot (e.g., shift from long-form to shorts)
- You need to time your content launches based on audience engagement cycles

**Prerequisites**:
- Notion database from `/riley-social-scraper` with 10+ videos and engagement metrics
- Claude API key
- (Optional) YouTube API key for historical analytics

**Don't Use When**:
- Data spans <2 months (too little historical signal)
- Creator posts inconsistently (sporadic uploads = noisy data)
- You need real-time metrics (data is ~48h stale)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "Hidden Knowledge: Comparative Analysis Needs Context"
2. `SKILL.md` — Quick Reference: `/riley-engagement-trend-detector`
3. `references/api-integration-guide.md` — Section: "7. Claude/GPT-5.6 API"

**Key Concepts**:
- Engagement trends reveal audience interest shifts (what's hot, what's cooling)
- Format pivots (long-form → shorts, text → video) often precede audience migration
- Timing patterns (when posts are most effective) vary by platform
- Notion database provides the time-series data needed for trend detection

---

## Execution

### Step 1: Export Videos with Dates & Engagement

Query Notion ordered by upload date (ascending):

```python
import notion_client
import datetime

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Query database, sorted by Upload Date ASC to see progression
results = client.databases.query(
    database_id="DB_ID",
    filter={"property": "Is Sponsored", "checkbox": {"equals": False}},
    sorts=[{"property": "Upload Date", "direction": "ascending"}],
    page_size=30  # Get 30+ videos for trend analysis
)

videos = []
for page in results['results']:
    props = page['properties']
    videos.append({
        "title": props['Video Title']['rich_text'][0]['text']['content'],
        "upload_date": props['Upload Date']['date']['start'],
        "engagement_score": props['Engagement Score']['formula']['number'],
        "hook_style": props['Hook Style']['select']['name'] if props['Hook Style']['select'] else "Unknown",
        "duration_sec": props.get('Duration (seconds)', {}).get('number', 0),
        "views": props['Views']['number']
    })

return videos
```

### Step 2: Build Claude Prompt (Standard Reasoning)

```
You are analyzing video engagement trends for creator [CREATOR_NAME].

Here are videos in chronological order (oldest to newest):

[For each video:]
Date: {upload_date}
Title: {title}
Engagement Score: {engagement_score}
Hook Style: {hook_style}
Duration: {duration_sec} seconds
Views: {views}

---

Analyze and return a JSON object with:

1. engagement_trend:
   - overall_direction: ["Rising" | "Falling" | "Stable" | "Volatile"]
   - strength: [1-10 confidence]
   - inflection_point: [date when trend changed, if any]
   - explanation: [Why is engagement changing?]

2. format_effectiveness:
   - [Hook Style 1]: {avg_engagement_score}
   - [Hook Style 2]: {avg_engagement_score}
   - (etc., ranked by effectiveness)

3. duration_impact:
   - short_form: {<5 min avg engagement}
   - medium_form: {5-20 min avg engagement}
   - long_form: {>20 min avg engagement}
   - recommendation: [Which format resonates most?]

4. timing_pattern:
   - best_day_of_week: [Mon-Sun, if data supports]
   - upload_frequency: [daily|weekly|biweekly|monthly]
   - optimal_cadence: [Recommend frequency]

5. emerging_opportunities:
   - format_pivot: [Should creator shift formats?]
   - topic_expansion: [What new topics should they explore?]
   - timing_optimization: [Change upload schedule?]

6. risk_signals:
   - declining_formats: [What's losing momentum?]
   - audience_fatigue: [Any signs of burnout?]
   - recovery_path: [If declining, what could fix it?]

Return ONLY valid JSON, no explanation.
```

### Step 3: Call Claude API (Standard Reasoning)

```python
import anthropic
import json

client = anthropic.Anthropic(api_key="YOUR_CLAUDE_KEY")

response = client.messages.create(
    model="claude-opus-4-1",  # Standard reasoning (not extra-high)
    max_tokens=1500,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# Parse JSON
analysis = json.loads(response.content[0].text)
```

### Step 4: Validate Analysis

```python
required_fields = [
    "engagement_trend", "format_effectiveness", "duration_impact",
    "timing_pattern", "emerging_opportunities", "risk_signals"
]

for field in required_fields:
    assert field in analysis, f"Missing: {field}"
    assert analysis[field] not in [None, "", {}], f"Empty: {field}"
```

### Step 5: Create Trend Report in Notion

Add analysis as a new page:

```python
trend_page = client.pages.create(
    parent={"database_id": "TREND_REPORTS_DB_ID"},
    properties={
        "Creator": {"title": [{"text": {"content": creator_name}}]},
        "Analysis Date": {"date": {"start": datetime.datetime.now().isoformat()}},
        "Engagement Trend": {"select": {"name": analysis['engagement_trend']['overall_direction']}},
        "Trend Confidence": {"number": analysis['engagement_trend']['strength']},
        "Most Effective Format": {"rich_text": [{"text": {"content": max(analysis['format_effectiveness'], key=analysis['format_effectiveness'].get)}}]},
        "Best Duration": {"select": {"name": analysis['duration_impact']['recommendation']}},
        "Upload Cadence": {"select": {"name": analysis['timing_pattern']['upload_frequency']}},
        "Recommended Changes": {"rich_text": [{"text": {"content": f"Format Pivot: {analysis['emerging_opportunities']['format_pivot']}; Timing: {analysis['timing_pattern']['optimal_cadence']}"}}]},
        "Risk Signals": {"rich_text": [{"text": {"content": str(analysis['risk_signals'])}}]},
        "Status": {"select": {"name": "Analysis Complete"}}
    }
)

return trend_page['id']
```

### Step 6: Generate Summary Report

```
# Engagement Trend Analysis: [CREATOR_NAME]

## Engagement Trend
Direction: [overall_direction]
Confidence: [strength]/10
Inflection Point: [date]
Explanation: [why]

## Format Effectiveness Ranking
1. [Format 1]: [avg engagement score]
2. [Format 2]: [avg engagement score]
3. [Format 3]: [avg engagement score]

## Duration Impact
- Short-Form (<5 min): Avg engagement [score]
- Medium-Form (5-20 min): Avg engagement [score]
- Long-Form (>20 min): Avg engagement [score]
- RECOMMENDATION: [best format]

## Timing Pattern
- Best Day: [day of week]
- Upload Frequency: [current cadence]
- Optimal Cadence: [recommended cadence]

## Emerging Opportunities
- Format Pivot: [should they shift formats?]
- Topic Expansion: [new topics to explore?]
- Timing Optimization: [change upload schedule?]

## Risk Signals
- Declining Formats: [what's losing momentum?]
- Audience Fatigue: [signs of burnout?]
- Recovery Path: [if declining, what could fix it?]

## Action Items
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

---

## Content Type Adaptations

### YouTube Long-Form (10+ minutes)
- Engagement typically higher with narrative-driven content
- Timing: Publish Thursday evening or Friday morning (weekend watching)

### TikTok / Instagram Reels (15-60 seconds)
- Engagement peaks with trending audio + quick hooks
- Timing: Publish 7-9am or 6-9pm (peak scroll times)

### LinkedIn
- Engagement highest on Tuesday-Thursday mornings (professional browsing time)
- Format: Mixed (text + image posts get comments, videos get shares)

---

## Output Requirements

**Trend Report**:
- ✓ Engagement direction identified (rising/falling/stable)
- ✓ Format effectiveness ranked (not generic)
- ✓ Duration impact quantified with data
- ✓ Timing pattern includes specific recommendations
- ✓ Emerging opportunities are actionable

**Quality Gate**:
- ✓ Trend analysis matches visual inspection of data
- ✓ Format rankings are based on engagement scores (not subjective)
- ✓ Duration recommendations are specific (not "varies by content")
- ✓ Risk signals are grounded in data
- ✓ Action items are concrete and testable

**Next Workflows**:
- Use findings to guide `/riley-skill-extractor` (focus on winning formats)
- Feed to content creation workflows (apply format + timing recommendations)
- Monitor results and iterate

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Engagement trend doesn't match data pattern (sanity check failed)
- [ ] Format effectiveness ranking is generic or obvious
- [ ] Duration recommendations lack supporting data
- [ ] Risk signals are vague ("audience is bored")
- [ ] Action items are not testable

**Validation Checklist**:
1. Plot engagement scores vs. dates (mental scatter plot); does the trend match Claude's analysis?
2. Rank formats by engagement manually; compare to Claude's ranking (should align)
3. Calculate median engagement for each duration bucket; verify recommendations
4. Review risk signals; ask: "Could we test this?" (if not, it's not actionable)
5. Pick one action item; ask: "Could I implement this next week?" (if not, it's vague)

**Anti-Patterns**:
- Do NOT assume trends are linear (look for curves, inflection points)
- Do NOT over-index on single outlier (one viral video skews average)
- Do NOT recommend format changes without data (only if clear pattern)
- Do NOT ignore platform differences (TikTok ≠ YouTube)
- Do NOT skip seasonality (some topics are seasonal)

---

## Troubleshooting

**"Claude analysis doesn't match my intuition"**
→ Claude is data-driven; intuition can be biased. Ask Claude to explain the reasoning for its recommendation.

**"Trend is 'Volatile' and not helpful"**
→ Creator may be experimenting. Zoom in on specific time periods to find sub-trends.

**"Risk signals feel like false alarms"**
→ Monitor next 2-3 uploads to confirm. Some decline is noise, not a trend.

**"Recommendations are too conservative"**
→ Ask Claude to increase confidence threshold for recommendations (e.g., "only suggest format pivots if confidence >8/10").

---

## Next Steps After Completion

1. **Validate** trend analysis against source data (spot-check plots)
2. **Share** with creator or content team
3. **Test** one recommendation (e.g., shift to recommended format)
4. **Monitor** results over 2-3 weeks
5. **Re-run** analysis monthly to track changes

**Downstreams**: Content creation workflows, format selection, scheduling decisions

