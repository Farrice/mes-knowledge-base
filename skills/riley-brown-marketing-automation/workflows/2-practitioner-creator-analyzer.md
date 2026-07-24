# Workflow: /riley-creator-profile-analyzer

**Tier**: Practitioner  
**Complexity**: Medium  
**Time**: 5-15 minutes  
**Cost**: $20-50 (Claude extra-high reasoning)  
**APIs**: Claude, Notion  
**Output**: Creator profile card (audience, topic clusters, persuasion formula, recommended angles)

---

## Pre-Flight Gate

**When to Use**:
- You have a Notion database from `/riley-social-scraper` (10+ videos)
- You want to understand WHO is watching, WHY they watch, HOW to reach them
- You're building a creator replication strategy or targeting plan

**Prerequisites**:
- Notion database with video transcripts + engagement metrics
- Claude API key
- Top 10 videos ranked by engagement (from database)

**Don't Use When**:
- You have <5 videos (patterns too noisy for audience inference)
- Creator's topic mix is too broad (no coherent audience)
- You need real demographic data (API gives linguistic inference only)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "The Scrape→DB→Analyze Loop"
2. `genius.md` — Section: "Comparative Analysis: The Audit Frame"
3. `SKILL.md` — Quick Reference: `/riley-creator-profile-analyzer`
4. `references/api-integration-guide.md` — Section: "7. Claude/GPT-5.6 API" (Extra-High Reasoning)
5. `references/notion-schema-templates.md` — Section: "Template 3: Creator Profile Analysis"

**Key Concepts**:
- Audience inference: What questions are answered? What problems solved? → Infer audience
- Topic clusters: Group videos by subject (not platform) to find coherence
- Persuasion formula: Hook + problem + solution + proof + CTA pattern
- Recommended angles: Which topics/platforms would resonate? Which won't?

---

## Execution

### Step 1: Export Top 10 Videos from Notion

Query the Notion database (authenticated, sponsored filtered):

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Query database, sorted by Engagement Score DESC, limit 10, filter non-sponsored
results = client.databases.query(
    database_id="DB_ID",
    filter={
        "property": "Is Sponsored",
        "checkbox": {"equals": False}
    },
    sorts=[{"property": "Engagement Score", "direction": "descending"}],
    page_size=10
)

videos = []
for page in results['results']:
    props = page['properties']
    videos.append({
        "title": props['Video Title']['rich_text'][0]['text']['content'],
        "transcript": props['Transcript']['rich_text'][0]['text']['content'],
        "engagement_score": props['Engagement Score']['formula']['number'],
        "platform": props['Platform']['select']['name'],
        "upload_date": props['Upload Date']['date']['start']
    })

return videos
```

### Step 2: Build Claude Prompt (Extra-High Reasoning)

```
You are analyzing 10 videos from creator [CREATOR_NAME]. Your task: infer their audience and persuasion formula.

VIDEOS:
[For each video, numbered 1-10:]
Video {N}: {title}
Engagement Score: {engagement_score}
Platform: {platform}
Date: {upload_date}

Transcript excerpt:
{first 500 chars of transcript}

---

Analyze and return a JSON object with:

1. audience_demographics:
   - age_range: (estimated, e.g., "25-45")
   - expertise_level: (beginner|intermediate|advanced)
   - pain_points: [list 3-5 main pain points being solved]
   - psychographics: [what values/desires do they hold?]

2. topic_clusters:
   - [Topic A]: [list video titles that cover this]
   - [Topic B]: [list video titles that cover this]
   - (etc., 3-5 clusters)

3. persuasion_formula:
   - hook_type: [Story|Question|Statistic|Emotion|Other]
   - problem_statement: [How is problem framed?]
   - solution_approach: [How is solution presented? Incremental? Revolutionary?]
   - proof_mechanism: [Personal anecdote? Data? Social proof? Results?]
   - urgency_level: [How much urgency is created? (Low|Medium|High|Very High)]

4. audience_sentiment: [How does audience feel after watching? (Empowered|Educated|Entertained|Guilty|Motivated)]

5. recommended_content_angles:
   - strong: [What topics/angles should they DOUBLE DOWN on?]
   - emerging: [What topics/angles are underexplored but fit their voice?]
   - avoid: [What topics would alienate their audience?]

6. replication_readiness: [1-10, how easily can someone adopt this creator's style?]

7. key_insights: [2-3 surprising patterns about this creator's audience or messaging]

Return ONLY valid JSON, no explanation.
```

### Step 3: Call Claude API (Extra-High Reasoning)

```python
import anthropic

client = anthropic.Anthropic(api_key="YOUR_CLAUDE_KEY")

response = client.messages.create(
    model="claude-opus-4-1",  # or "claude-3-7-sonnet" for extra-high
    max_tokens=2000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # Extra-high reasoning budget
    },
    messages=[
        {
            "role": "user",
            "content": prompt  # From Step 2
        }
    ]
)

# Parse JSON (extract from thinking + text blocks)
import json
analysis = json.loads(response.content[-1].text)  # Last block is usually JSON
```

### Step 4: Validate Analysis

```python
required_fields = [
    "audience_demographics", "topic_clusters", "persuasion_formula",
    "audience_sentiment", "recommended_content_angles", "replication_readiness", "key_insights"
]

for field in required_fields:
    assert field in analysis, f"Missing: {field}"
    assert analysis[field] not in [None, "", {}], f"Empty: {field}"

# Sanity check: replication_readiness should be 1-10
assert 1 <= analysis['replication_readiness'] <= 10
```

### Step 5: Create Creator Profile Card in Notion

Add a new database for Creator Profiles (or add to existing):

```python
# Create new page in Creator Profiles DB (or inline in videos DB)
profile_page = client.pages.create(
    parent={"database_id": "PROFILES_DB_ID"},
    properties={
        "Creator": {"title": [{"text": {"content": creator_name}}]},
        "Platform": {"select": {"name": videos[0]['platform']}},
        "Audience Age": {"rich_text": [{"text": {"content": analysis['audience_demographics']['age_range']}}]},
        "Pain Points": {"rich_text": [{"text": {"content": '; '.join(analysis['audience_demographics']['pain_points'])}}]},
        "Psychographics": {"rich_text": [{"text": {"content": str(analysis['audience_demographics']['psychographics'])}}]},
        "Topic Clusters": {"rich_text": [{"text": {"content": str(analysis['topic_clusters'])}}]},
        "Hook Type": {"select": {"name": analysis['persuasion_formula']['hook_type']}},
        "Problem Statement": {"rich_text": [{"text": {"content": analysis['persuasion_formula']['problem_statement']}}]},
        "Solution Approach": {"rich_text": [{"text": {"content": analysis['persuasion_formula']['solution_approach']}}]},
        "Proof Mechanism": {"select": {"name": analysis['persuasion_formula']['proof_mechanism']}},
        "Audience Sentiment": {"select": {"name": analysis['audience_sentiment']}},
        "Strong Angles": {"rich_text": [{"text": {"content": str(analysis['recommended_content_angles']['strong'])}}]},
        "Emerging Angles": {"rich_text": [{"text": {"content": str(analysis['recommended_content_angles']['emerging'])}}]},
        "Avoid": {"rich_text": [{"text": {"content": str(analysis['recommended_content_angles']['avoid'])}}]},
        "Replication Readiness": {"number": analysis['replication_readiness']},
        "Key Insights": {"rich_text": [{"text": {"content": str(analysis['key_insights'])}}]}
    }
)

return profile_page['id']
```

### Step 6: Generate Summary Document (Optional Paper Export)

```
Creator Profile: [CREATOR_NAME]

AUDIENCE
Age Range: [age_range]
Expertise Level: [expertise_level]
Pain Points:
  - [pain point 1]
  - [pain point 2]
  - [pain point 3]

Psychographics: [values, desires]

TOPICS & THEMES
[For each topic cluster:]
  [Topic]: [list of videos]

PERSUASION FORMULA
Hook Type: [hook_type]
Problem Statement: [problem_statement]
Solution Approach: [solution_approach]
Proof Mechanism: [proof_mechanism]
Urgency Level: [urgency_level]
Audience Sentiment After Watching: [sentiment]

CONTENT RECOMMENDATIONS
Double Down On:
  - [angle 1]
  - [angle 2]

Explore (Emerging):
  - [angle 3]
  - [angle 4]

Avoid:
  - [angle 5]
  - [angle 6]

REPLICATION READINESS: [score]/10

KEY INSIGHTS
1. [insight 1]
2. [insight 2]
3. [insight 3]
```

---

## Content Type Adaptations

### YouTube Long-Form (10+ minutes)
- Audience: Deep learners, willing to sit through longer narratives
- Hook: Story or data-driven, first 30 seconds critical
- CTA: Often soft ("check out the course") or survey-oriented

### TikTok / Instagram Reels (15-60 seconds)
- Audience: Trend-following, quick attention span, entertainment-seeking
- Hook: Immediate (first 1 second)
- CTA: Share, follow, link in bio (mobile-optimized)

### LinkedIn (text + video)
- Audience: Professional, career-oriented, authority-seeking
- Hook: Contrarian statement or valuable tip
- CTA: Comment (start discussion), connection

---

## Output Requirements

**Creator Profile Card**:
- ✓ All demographic fields populated
- ✓ Topic clusters identified and labeled
- ✓ Persuasion formula broken down into 5+ components
- ✓ Recommended angles are specific (not generic)
- ✓ Replication readiness scored 1-10

**Quality Gate**:
- ✓ Audience demographics feel realistic (not overly broad or narrow)
- ✓ Topic clusters are non-overlapping (coherent categories)
- ✓ Persuasion formula can be tested against source videos
- ✓ Recommended angles are differentiated from current content
- ✓ Key insights reveal something non-obvious

**Next Workflows**:
- Feed to `/ghostwrite` (Lara uses for LinkedIn content)
- Feed to `/parallax` (Farrice uses for Substack)
- Feed to `/riley-skill-extractor` (voice extraction)

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Audience demographics are generic (e.g., "25-55, interested in business")
- [ ] Topic clusters overlap significantly (lack of coherence)
- [ ] Persuasion formula doesn't match source videos (sanity check failed)
- [ ] Recommended angles are already covered in the videos
- [ ] Replication readiness <3/10 (voice too idiosyncratic)
- [ ] Key insights are surface-level ("They like storytelling")

**Validation Checklist**:
1. Read the audience demographics; ask: "Would I recognize someone who fits this description?"
2. Pick one topic cluster; verify 2+ videos actually cover that topic
3. Review persuasion formula; re-read a source video transcript; does it match?
4. Take one "strong angle" (recommended); check if it's already heavily covered in the 10 videos
5. Read key insights; are they surprising? (If you already knew them, they're not insights)

**Anti-Patterns**:
- Do NOT generalize from 10 videos to "all audiences" (sample is small)
- Do NOT assume topic clusters are isolated (audience may cross-over)
- Do NOT over-index on emotion if data is reason-driven
- Do NOT recommend angles that contradict creator's voice
- Do NOT skip the replication readiness score (it gates downstream use)

---

## Troubleshooting

**"Claude API returns generic analysis"**
→ Prompt may be too sparse. Add more context from transcripts (include longer excerpts, not just summaries).

**"Audience demographic conflicts between videos"**
→ Topic cluster analysis may be revealing sub-audiences. Add a note: "This creator serves 2 distinct audiences; recommend separate content streams."

**"Topic clusters are too granular or too broad"**
→ Re-run with explicit instruction: "Cluster into 3-5 themes, not 10+. Topics should be broad enough to span multiple videos."

**"Replication readiness score comes back <5/10"**
→ This creator's voice is too idiosyncratic or persona-dependent. Consider whether to proceed with skill extraction or document as "reference only."

---

## Next Steps After Completion

1. **Validate** profile card in Notion (does audience description feel right?)
2. **Cross-check** recommended angles against source videos (no overlap)
3. **Feed to** `/ghostwrite` (Lara) for LinkedIn content generation
4. **Or feed to** `/parallax` (Farrice) for Substack essay generation
5. **Iterate** on replication readiness after testing generated content

**Downstreams**: `/ghostwrite` (Lara Acosta), `/parallax` (Farrice voice), `/riley-skill-extractor`, `/riley-research-to-skill-pipeline`

