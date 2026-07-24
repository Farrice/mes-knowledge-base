# Notion Schema Templates: Riley Brown Marketing Automation

**Purpose**: Replicable Notion database schemas for each Riley workflow. Copy these templates and modify for your use case.

---

## Template 1: Creator Video Database (Foundation)

**Used By**: `/riley-social-scraper`  
**Fields**: 13  
**Example Data**: Kallaway Instagram videos  

### Schema Definition

```json
{
  "title": "Creator Videos",
  "properties": {
    "Creator": {
      "type": "title",
      "description": "Creator name (primary key)"
    },
    "Platform": {
      "type": "select",
      "options": [
        {"name": "YouTube", "color": "red"},
        {"name": "Instagram", "color": "pink"},
        {"name": "TikTok", "color": "gray"},
        {"name": "LinkedIn", "color": "blue"}
      ]
    },
    "Video Title": {
      "type": "rich_text",
      "description": "Full video title"
    },
    "URL": {
      "type": "url",
      "description": "Direct link to video"
    },
    "Video Embed": {
      "type": "file",
      "description": "Downloaded video or embed link"
    },
    "Transcript": {
      "type": "rich_text",
      "description": "Full video transcript or captions"
    },
    "Upload Date": {
      "type": "date",
      "description": "When video was published"
    },
    "Likes": {
      "type": "number",
      "description": "Engagement metric"
    },
    "Comments": {
      "type": "number",
      "description": "Engagement metric"
    },
    "Shares": {
      "type": "number",
      "description": "Engagement metric"
    },
    "Views": {
      "type": "number",
      "description": "Total views (if available)"
    },
    "Engagement Score": {
      "type": "formula",
      "formula": "prop(\"Likes\") + prop(\"Comments\") * 2 + prop(\"Shares\") * 5",
      "description": "Composite score: likes + 2×comments + 5×shares"
    },
    "Rank": {
      "type": "formula",
      "formula": "rank(prop(\"Engagement Score\"))",
      "description": "Auto-rank by engagement (1 = highest)"
    },
    "Hook Style": {
      "type": "select",
      "options": [
        {"name": "Story"},
        {"name": "Question"},
        {"name": "Statistic"},
        {"name": "Emotion"},
        {"name": "Contradiction"},
        {"name": "Mystery"}
      ],
      "description": "Opening hook type"
    },
    "Hook Text": {
      "type": "rich_text",
      "description": "First 30 seconds of transcript"
    },
    "Script Pattern": {
      "type": "rich_text",
      "description": "Overall structure (e.g., 'Story → Problem → Solution → CTA')"
    },
    "Audience Segment": {
      "type": "select",
      "options": [
        {"name": "Beginners"},
        {"name": "Intermediate"},
        {"name": "Advanced"},
        {"name": "General"}
      ],
      "description": "Target skill level"
    },
    "Main Topic": {
      "type": "select",
      "options": [
        {"name": "Education"},
        {"name": "Entertainment"},
        {"name": "How-to"},
        {"name": "Personal Story"},
        {"name": "Marketing"}
      ]
    },
    "Is Sponsored": {
      "type": "checkbox",
      "description": "Filter out #ad, #sponsored content"
    },
    "Quality Rating": {
      "type": "select",
      "options": [
        {"name": "5 - Exemplary"},
        {"name": "4 - Strong"},
        {"name": "3 - Good"},
        {"name": "2 - Fair"},
        {"name": "1 - Poor"}
      ],
      "description": "Manual quality assessment"
    },
    "Notes": {
      "type": "rich_text",
      "description": "Any additional observations"
    }
  }
}
```

### Recommended Views

**View 1: All Videos (Default)**
```
Sort: Engagement Score (descending)
Filter: Is Sponsored = false
```

**View 2: Top 10**
```
Sort: Engagement Score (descending)
Filter: Is Sponsored = false
Limit: 10
```

**View 3: By Hook Style**
```
Group By: Hook Style
Sort: Engagement Score (descending within each group)
```

**View 4: Authentic Only**
```
Filter: Is Sponsored = false
Sort: Engagement Score (descending)
```

---

## Template 2: Competitor Ad Database (Foundation)

**Used By**: `/riley-competitor-scraper`  
**Fields**: 16  
**Example Data**: Quad.ai, Replit, Claude ads from Foreplay  

### Schema Definition

```json
{
  "title": "Competitor Ads",
  "properties": {
    "Ad ID": {
      "type": "title",
      "description": "Unique Foreplay ad ID"
    },
    "Competitor": {
      "type": "select",
      "options": [
        {"name": "Quad.ai"},
        {"name": "Replit"},
        {"name": "Claude"},
        {"name": "ChatGPT"},
        {"name": "Perplexity"}
      ],
      "description": "Competitor company"
    },
    "Ad Type": {
      "type": "select",
      "options": [
        {"name": "Static Image"},
        {"name": "Video"},
        {"name": "Carousel"},
        {"name": "Story"}
      ]
    },
    "Platform": {
      "type": "select",
      "options": [
        {"name": "Facebook"},
        {"name": "Instagram"},
        {"name": "TikTok"},
        {"name": "LinkedIn"},
        {"name": "Twitter"}
      ]
    },
    "Duration (Months)": {
      "type": "number",
      "description": "How long ad has been running (proxy for success)"
    },
    "Start Date": {
      "type": "date",
      "description": "When ad first seen"
    },
    "Last Seen": {
      "type": "date",
      "description": "Most recent sighting"
    },
    "Copy": {
      "type": "rich_text",
      "description": "Full ad copy text"
    },
    "Hook": {
      "type": "rich_text",
      "description": "First line or opening visual"
    },
    "Visual": {
      "type": "file",
      "description": "Ad image(s) or video thumbnail"
    },
    "CTA Text": {
      "type": "rich_text",
      "description": "Call-to-action button text"
    },
    "CTA Type": {
      "type": "select",
      "options": [
        {"name": "Sign Up"},
        {"name": "Download"},
        {"name": "Learn More"},
        {"name": "Buy Now"},
        {"name": "View More"},
        {"name": "Try Free"}
      ]
    },
    "Hook Pattern": {
      "type": "select",
      "options": [
        {"name": "Question"},
        {"name": "Statistic"},
        {"name": "Emotion"},
        {"name": "Social Proof"},
        {"name": "Pain Point"},
        {"name": "Story"}
      ],
      "description": "Opening technique"
    },
    "Copy Strategy": {
      "type": "rich_text",
      "description": "Why this copy works (from analysis)"
    },
    "Success Pattern": {
      "type": "rich_text",
      "description": "What makes this ad perform"
    },
    "Estimated Quality": {
      "type": "select",
      "options": [
        {"name": "Elite (9+ months)"},
        {"name": "Strong (6-9 months)"},
        {"name": "Good (3-6 months)"},
        {"name": "Testing (1-3 months)"},
        {"name": "New (<1 month)"}
      ],
      "description": "Based on duration"
    },
    "Notes": {
      "type": "rich_text",
      "description": "Analysis or observations"
    }
  }
}
```

### Recommended Views

**View 1: Longest Running (Default)**
```
Sort: Duration (Months) (descending)
Filter: None
```

**View 2: By Competitor**
```
Group By: Competitor
Sort: Duration (Months) (descending within group)
```

**View 3: Video Only**
```
Filter: Ad Type = Video
Sort: Duration (Months) (descending)
```

**View 4: Elite Performers**
```
Filter: Estimated Quality = "Elite"
Sort: Duration (Months) (descending)
Group By: Competitor
```

---

## Template 3: Creator Profile Analysis (Practitioner)

**Used By**: `/riley-creator-profile-analyzer`  
**Fields**: 18  
**Example Data**: Analysis of Kallaway audience, patterns, recommendations  

### Schema Definition

```json
{
  "title": "Creator Profiles",
  "properties": {
    "Creator Name": {
      "type": "title",
      "description": "Creator profile name"
    },
    "Platform": {
      "type": "select",
      "options": [
        {"name": "YouTube"},
        {"name": "Instagram"},
        {"name": "TikTok"},
        {"name": "LinkedIn"},
        {"name": "Twitter"}
      ]
    },
    "Follower Count": {
      "type": "number",
      "description": "Last known follower/subscriber count"
    },
    "Avg Engagement Rate": {
      "type": "number",
      "description": "% (e.g., 3.5)"
    },
    "Content Category": {
      "type": "select",
      "options": [
        {"name": "Education"},
        {"name": "Entertainment"},
        {"name": "Business"},
        {"name": "Fitness"},
        {"name": "Lifestyle"},
        {"name": "Tech"}
      ]
    },
    "Audience Demographic": {
      "type": "rich_text",
      "description": "Target audience description (age, interests, pain points)"
    },
    "Audience Sentiment": {
      "type": "select",
      "options": [
        {"name": "Highly Engaged"},
        {"name": "Engaged"},
        {"name": "Neutral"},
        {"name": "Declining"},
        {"name": "Disengaged"}
      ]
    },
    "Top 3 Topics": {
      "type": "rich_text",
      "description": "Most popular content themes"
    },
    "Posting Frequency": {
      "type": "select",
      "options": [
        {"name": "Daily"},
        {"name": "3-5x/week"},
        {"name": "2-3x/week"},
        {"name": "Weekly"},
        {"name": "Sporadic"}
      ]
    },
    "Signature Hook Style": {
      "type": "select",
      "options": [
        {"name": "Story"},
        {"name": "Question"},
        {"name": "Statistic"},
        {"name": "Emotion"},
        {"name": "Contradiction"}
      ],
      "description": "Primary opening technique"
    },
    "Persuasion Formula": {
      "type": "rich_text",
      "description": "Extracted script structure (e.g., 'Story → Problem → Solution → CTA')"
    },
    "Avg Video Length": {
      "type": "select",
      "options": [
        {"name": "<1 min"},
        {"name": "1-3 min"},
        {"name": "3-10 min"},
        {"name": "10-20 min"},
        {"name": ">20 min"}
      ]
    },
    "Time to Hook": {
      "type": "select",
      "options": [
        {"name": "<5 seconds"},
        {"name": "5-10 seconds"},
        {"name": "10-30 seconds"},
        {"name": ">30 seconds"}
      ],
      "description": "How fast they capture attention"
    },
    "Unique Voice Elements": {
      "type": "rich_text",
      "description": "Distinctive phrases, mannerisms, humor style"
    },
    "Recommended Content Angles": {
      "type": "rich_text",
      "description": "How to adapt their style to your brand"
    },
    "Replication Difficulty": {
      "type": "select",
      "options": [
        {"name": "Easy (formulaic)"},
        {"name": "Moderate (requires practice)"},
        {"name": "Hard (highly personal)"},
        {"name": "Very Hard (unique talent)"}
      ]
    },
    "Overall Quality Rating": {
      "type": "select",
      "options": [
        {"name": "5 - Exemplary"},
        {"name": "4 - Strong"},
        {"name": "3 - Good"},
        {"name": "2 - Fair"},
        {"name": "1 - Poor"}
      ]
    },
    "Analysis Date": {
      "type": "date",
      "description": "When this profile was analyzed"
    },
    "Notes": {
      "type": "rich_text",
      "description": "Additional insights or concerns"
    }
  }
}
```

### Recommended Views

**View 1: By Engagement Rate (Default)**
```
Sort: Avg Engagement Rate (descending)
```

**View 2: By Category**
```
Group By: Content Category
Sort: Avg Engagement Rate (descending within group)
```

**View 3: Easiest to Replicate**
```
Filter: Replication Difficulty = "Easy" or "Moderate"
Sort: Avg Engagement Rate (descending)
```

---

## Template 4: Content Calendar (Practitioner)

**Used By**: `/riley-content-calendar-orchestrator`  
**Fields**: 14  
**Example Data**: Scheduled content across multiple creators/platforms  

### Schema Definition

```json
{
  "title": "Content Calendar",
  "properties": {
    "Title": {
      "type": "title",
      "description": "Content piece title"
    },
    "Creator/Voice": {
      "type": "select",
      "options": [
        {"name": "Kallaway"},
        {"name": "Original"},
        {"name": "Lara"},
        {"name": "Luke"}
      ],
      "description": "Which creator style/voice"
    },
    "Platform": {
      "type": "select",
      "options": [
        {"name": "LinkedIn"},
        {"name": "YouTube"},
        {"name": "TikTok"},
        {"name": "Instagram"},
        {"name": "Email"},
        {"name": "Substack"}
      ]
    },
    "Publish Date": {
      "type": "date",
      "description": "When to post"
    },
    "Publish Time": {
      "type": "rich_text",
      "description": "Specific time (e.g., 9am PT)"
    },
    "Status": {
      "type": "select",
      "options": [
        {"name": "Drafted"},
        {"name": "In Review"},
        {"name": "Approved"},
        {"name": "Scheduled"},
        {"name": "Published"},
        {"name": "Archived"}
      ]
    },
    "Content Type": {
      "type": "select",
      "options": [
        {"name": "Video"},
        {"name": "Carousel"},
        {"name": "Text Post"},
        {"name": "Essay"},
        {"name": "Thread"}
      ]
    },
    "Hook Style": {
      "type": "select",
      "options": [
        {"name": "Story"},
        {"name": "Question"},
        {"name": "Statistic"},
        {"name": "Emotion"}
      ]
    },
    "Reviewer": {
      "type": "text",
      "description": "Who approves before publishing"
    },
    "Copy/Draft": {
      "type": "rich_text",
      "description": "Full content or link to draft"
    },
    "Media Assets": {
      "type": "file",
      "description": "Images, video, thumbnails"
    },
    "Engagement Target": {
      "type": "number",
      "description": "Expected engagement (e.g., likes/views)"
    },
    "Notes": {
      "type": "rich_text",
      "description": "Any special instructions"
    }
  }
}
```

### Recommended Views

**View 1: Calendar Timeline (Default)**
```
Group By: Publish Date (calendar view)
Sort: Publish Time
Filter: Status ≠ Archived
```

**View 2: By Status**
```
Group By: Status
Sort: Publish Date (ascending within group)
```

**View 3: Ready to Review**
```
Filter: Status = "In Review"
Sort: Publish Date (ascending)
```

---

## Template 5: Ad Performance Audit (Practitioner)

**Used By**: `/riley-ad-performance-auditor`  
**Fields**: 15  
**Example Data**: Analysis of competitor ads with success factors  

### Schema Definition

```json
{
  "title": "Ad Audits",
  "properties": {
    "Audit Title": {
      "type": "title",
      "description": "Name of audit (e.g., 'Quad.ai Q3 2026')"
    },
    "Competitor": {
      "type": "select",
      "options": [
        {"name": "Quad.ai"},
        {"name": "Replit"},
        {"name": "Claude"},
        {"name": "ChatGPT"},
        {"name": "Perplexity"}
      ]
    },
    "Audit Date": {
      "type": "date",
      "description": "When analysis was performed"
    },
    "Ads Analyzed": {
      "type": "number",
      "description": "How many ads reviewed"
    },
    "Sample Ad Links": {
      "type": "rich_text",
      "description": "URLs or references to ads (from Foreplay)"
    },
    "Avg Runtime": {
      "type": "number",
      "description": "Average months running (proxy for success)"
    },
    "Hook Pattern (Dominant)": {
      "type": "select",
      "options": [
        {"name": "Question"},
        {"name": "Statistic"},
        {"name": "Emotion"},
        {"name": "Social Proof"},
        {"name": "Mixed"}
      ]
    },
    "Copy Strategy": {
      "type": "rich_text",
      "description": "Key approach (e.g., 'Problem → Solution → Urgency')"
    },
    "Key Success Factors": {
      "type": "rich_text",
      "description": "Why these ads are working (bullet points)"
    },
    "CTA Most Common": {
      "type": "select",
      "options": [
        {"name": "Sign Up"},
        {"name": "Download"},
        {"name": "Try Free"},
        {"name": "Learn More"}
      ]
    },
    "Vulnerabilities": {
      "type": "rich_text",
      "description": "Gaps or weaknesses to exploit"
    },
    "Recommended Actions": {
      "type": "rich_text",
      "description": "What to do with this intel"
    },
    "Confidence Level": {
      "type": "select",
      "options": [
        {"name": "High (10+ ads)"},
        {"name": "Medium (5-10 ads)"},
        {"name": "Low (<5 ads)"}
      ]
    },
    "Overall Assessment": {
      "type": "select",
      "options": [
        {"name": "Elite - Copy our approach"},
        {"name": "Strong - Learn key elements"},
        {"name": "Moderate - Some tactics worth testing"},
        {"name": "Weak - Differentiate from them"}
      ]
    },
    "Next Steps": {
      "type": "rich_text",
      "description": "Follow-up actions"
    }
  }
}
```

---

## How to Set Up (Step-by-Step)

### For Each Template:

1. **Create Database in Notion**
   - Click "New" → "Database"
   - Choose "Table"
   - Name: (use template name)

2. **Add Properties**
   - Click "+" next to property names
   - For each property in schema:
     - Name: (exact name from schema)
     - Type: (select from schema)
     - Options: (if select, add options)

3. **Create Formulas** (e.g., Engagement Score)
   ```
   Click property → "Formula" → Copy formula from schema
   ```

4. **Create Views**
   - Click "Add a view" for each recommended view
   - Set filters, sorts, grouping as specified

5. **Add Sample Data**
   - Populate 1-2 sample rows
   - Test formulas and views

6. **Share/Integrate**
   - Invite team members to database
   - Connect Notion API for automated ingestion

---

## Field Type Reference

| Type | Use Case | Example |
|------|----------|---------|
| Title | Primary key (name, title) | "Creator: Kallaway" |
| Text | Short text, names | "John Doe" |
| Rich Text | Long-form content | Full transcript |
| Number | Metrics, counts | Views: 1000 |
| Select | Single choice from list | Platform: YouTube |
| Multi-Select | Multiple choices | Topics: Education, Entertainment |
| Date | Calendar dates | "2026-08-01" |
| URL | Web links | "https://youtube.com/..." |
| File | Media, documents | Video file, image |
| Checkbox | Boolean | Is Sponsored: true/false |
| Formula | Calculated value | Engagement Score = likes + 2×comments |
| Relation | Link to other database | Creator → Profile |

---

## Common Formulas

**Engagement Score** (most important):
```
prop("Likes") + prop("Comments") * 2 + prop("Shares") * 5
```

**Rank by Score**:
```
rank(prop("Engagement Score"))
```

**Days Since Post**:
```
dateBetween(now(), prop("Upload Date"), "days")
```

**Engagement Rate %**:
```
round(prop("Engagement Score") / prop("Views") * 100, 1)
```

---

## Tips for Success

1. **Start Simple**: Use Template 1 first. Add complexity as needed.
2. **Name Consistency**: Use exact field names so automation scripts can find them.
3. **Test Formulas**: Add 3-5 rows before deploying full automation.
4. **Archive Old Data**: Use Status/Is Archived checkbox to hide completed rows.
5. **Share View URLs**: Share specific views (not full database) with clients/reviewers.
6. **Use Covers/Icons**: Add emoji covers to databases for visual organization.

---

**Master Doc**: SKILL.md (workflow table)  
**Implementation**: `/riley-social-scraper` workflow (first database creation)
