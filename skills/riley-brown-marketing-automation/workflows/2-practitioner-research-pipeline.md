# Workflow: /riley-research-to-skill-pipeline

**Tier**: Practitioner  
**Complexity**: High  
**Time**: 20-60 minutes  
**Cost**: $30-100 (full stack: ScrapeCreators + Claude extra-high + Notion)  
**APIs**: All 7 core APIs  
**Output**: End-to-end: Research topic → Find creators → Extract skills → Generate content → Schedule

---

## Pre-Flight Gate

**When to Use**:
- You want to research a market, find top creators, and extract their playbook in one shot
- You're building content on a new topic and need patterns to follow
- You're launching into a new niche and need rapid competitive intelligence

**Prerequisites**:
- ScrapeCreators API key
- Claude API key (for extra-high reasoning)
- Notion workspace + integration token
- Gmail + Cal.com (for scheduling)

**Don't Use When**:
- You have limited budget (full stack = $30-100 per research)
- Topic is too niche (may not find 5+ creators)
- You need real-time data (API data is ~48h stale)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — All sections (overview of entire system)
2. `SKILL.md` — Full document (workflow table + stacking guide)
3. All referenced workflows (foundation + practitioner)

**Key Concepts**:
- Research topic → Query to find creators → Scrape → Analyze → Extract patterns → Generate content → Schedule
- Each step feeds into the next (no manual hand-offs)
- Notion is the hub (all outputs link back to DB)
- Output: Callable skill + generated content ready to publish

---

## Execution

### Step 1: Define Research Topic

```
Topic: [e.g., "AI tools for solopreneurs"]
Target Audience: [who should care?]
Angle: [unique perspective, if any]
Content Goals: [what do you want to create?]
Platforms: [LinkedIn, Substack, Twitter, etc.]
```

### Step 2: Find Creators in Topic (Manual or Semi-Automated)

Use research tools to identify 5-10 creators in this space:

```
Approach 1: Manual search
- Google "[topic] YouTube"
- Browse YouTube channels
- Note channel names + follower counts

Approach 2: Semi-automated (using Perplexity or similar)
- Query: "Who are the top 10 creators discussing [topic]?"
- Extract channel names + platforms

Selected creators:
  1. [Creator A] — YouTube, [follower count]
  2. [Creator B] — YouTube, [follower count]
  3. [Creator C] — TikTok, [follower count]
  (etc., aim for 5-10)
```

### Step 3: Scrape Creator Databases

For each creator, run `/riley-social-scraper`:

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

creators = ["Creator A", "Creator B", "Creator C", ...]

for creator in creators:
    # Call /riley-social-scraper API
    # (This is a separate workflow; calls ScrapeCreators)
    scraper_result = riley_social_scraper(creator_name=creator, limit=10)
    
    # scraper_result includes:
    # - Notion database ID
    # - Number of videos scraped
    # - Engagement scores
    
    print(f"✓ Scraped {creator}: {scraper_result['video_count']} videos")
```

### Step 4: Analyze All Creators (Comparative)

Use `/riley-creator-profile-analyzer` on each database:

```python
# For each creator's database, run analyzer
for creator in creators:
    creator_db_id = get_database_id(creator)
    
    # Call /riley-creator-profile-analyzer
    # (This is a separate workflow)
    analysis = riley_creator_profile_analyzer(database_id=creator_db_id)
    
    # analysis includes:
    # - Audience demographics
    # - Topic clusters
    # - Persuasion formula
    # - Recommended angles
    
    print(f"✓ Analyzed {creator}: {analysis['topic_clusters']}")
```

### Step 5: Extract Common Patterns Across All Creators

Use Claude to identify meta-patterns:

```
You are analyzing 5-10 creators in the "[topic]" space.

For each creator:
[Creator A]
  - Audience: [demographics]
  - Topics: [clusters]
  - Persuasion: [hook + CTA]
  - Strength: [what makes them unique?]

[Creator B]
  [same structure]

...

Analyze and return a JSON object with:

1. meta_patterns:
   - [Common pattern 1]: [Which creators share this?]
   - [Common pattern 2]: [Why does this pattern work?]
   - (etc., 3-5 meta-patterns)

2. audience_synthesis:
   - Unified audience profile: [Who is the core audience for this topic?]
   - Key pain points: [What problems unite them?]
   - What they want: [What outcomes do they seek?]

3. topic_synthesis:
   - Core topics: [What must be covered?]
   - Emerging subtopics: [What's underexplored?]
   - Topic hierarchy: [How topics relate to each other]

4. persuasion_synthesis:
   - Winning hook pattern: [What works across creators?]
   - Winning CTA pattern: [What resonates?]
   - Proof strategy: [What builds credibility in this space?]

5. content_formula:
   - Ideal structure: [Hook → Problem → Solution → Proof → CTA]
   - Tone: [What tone resonates?]
   - Format: [Video, essay, thread, etc.?]
   - Length: [Optimal length?]

6. your_angle:
   - Differentiation: [What could YOU do differently from these creators?]
   - Niche within niche: [Any subaudience not served?]
   - Unique perspective: [What could only you bring?]

Return ONLY valid JSON, no explanation.
```

### Step 6: Extract or Create Skill

Use `/riley-skill-extractor` to turn meta-patterns into a callable skill:

```python
# Option A: If one creator dominates, extract their skill directly
skill_id = riley_skill_extractor(database_id=top_creator_db_id)

# Option B: Create a composite skill from meta-patterns
meta_skill = create_composite_skill(
    topic=research_topic,
    meta_patterns=analysis,
    creators=creators,
    skill_name=f"{topic_slug}-content-formula"
)
```

### Step 7: Generate Content Using Extracted Skill

Use the extracted skill to generate 5-10 content pieces:

```python
# Use the extracted skill to generate content
generated_content = []

for i in range(5):
    # Call skill to generate content
    content = call_skill(
        skill_id=skill_id,
        topic_angle=[angle for angle in emerging_angles][i % len(emerging_angles)],
        platform="LinkedIn",  # or adapt per piece
        voice="extracted"
    )
    
    generated_content.append(content)

print(f"✓ Generated {len(generated_content)} content pieces")
```

### Step 8: Add to Content Calendar & Schedule

Use `/riley-content-calendar-orchestrator`:

```python
# Add generated content to calendar
for i, content in enumerate(generated_content):
    client.pages.create(
        parent={"database_id": calendar_db_id},
        properties={
            "Post Title": {"title": [{"text": {"content": content['title']}}]},
            "Creator/Source": {"select": {"name": "Research Synthesis"}},
            "Platform": {"select": {"name": content['platform']}},
            "Content": {"rich_text": [{"text": {"content": content['body']}}]},
            "Scheduled Date": {"date": {"start": (datetime.now() + timedelta(days=i*3)).isoformat()}}
        }
    )

# Send review emails
for content in generated_content:
    send_review_email(
        title=content['title'],
        body=content['body'],
        reviewer="Farrice",
        deadline=(datetime.now() + timedelta(hours=24)).isoformat()
    )

print(f"✓ Scheduled {len(generated_content)} pieces + sent review emails")
```

### Step 9: Create Research Summary Document

Link everything together in Notion:

```python
research_page = client.pages.create(
    parent={"database_id": "RESEARCH_PROJECTS_DB_ID"},
    properties={
        "Project": {"title": [{"text": {"content": f"Research: {research_topic}"}}]},
        "Date": {"date": {"start": datetime.now().isoformat()}},
        "Creators Analyzed": {"rich_text": [{"text": {"content": ', '.join(creators)}}]},
        "Meta Patterns": {"rich_text": [{"text": {"content": str(meta_patterns)}}]},
        "Audience Profile": {"rich_text": [{"text": {"content": audience_synthesis}}]},
        "Content Formula": {"rich_text": [{"text": {"content": str(content_formula)}}]},
        "Skill Generated": {"select": {"name": "Yes" if skill_id else "No"}},
        "Content Pieces": {"number": len(generated_content)},
        "Status": {"select": {"name": "Complete"}}
    }
)

return research_page['id']
```

---

## Output Requirements

**End-to-End Deliverables**:
- ✓ 5-10 creator databases scraped and populated
- ✓ Creator profile analyses completed
- ✓ Meta-patterns extracted across all creators
- ✓ Skill created or extracted (callable)
- ✓ 5-10 content pieces generated
- ✓ Content calendar populated + review emails sent
- ✓ Research summary document created

**Quality Gate**:
- ✓ All creator databases have 10+ videos
- ✓ Meta-patterns repeat across ≥3 creators (signal, not noise)
- ✓ Extracted skill is replicable (replicability_score ≥5/10)
- ✓ Generated content reflects meta-patterns (sanity check)
- ✓ Content calendar has realistic scheduling (3-5 day spacing)

**Next Workflows**:
- Monitor content performance after publishing
- Refine skill based on results
- Use skill for ongoing content generation

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Fewer than 5 creators analyzed (insufficient sample)
- [ ] Meta-patterns appear in only 1-2 creators (not meta)
- [ ] Generated content doesn't reflect extracted patterns
- [ ] Skill replicability is <5/10 (too hard to use)
- [ ] Content calendar is missing review emails or deadlines

**Validation Checklist**:
1. Count creator databases; verify ≥5
2. Review meta-patterns; verify each appears in ≥3 creator analyses
3. Read one generated content piece; verify it follows the extracted formula
4. Check skill page; verify replicability_score ≥5/10
5. Scan calendar; verify all pieces have scheduled dates + review deadlines

**Anti-Patterns**:
- Do NOT include creators with <5k followers (too small, data too noisy)
- Do NOT assume meta-patterns are universal (only claim patterns that repeat)
- Do NOT generate content without review gates (quality suffers)
- Do NOT skip the research summary (makes iteration impossible)

---

## Troubleshooting

**"Can't find 5 creators in the topic"**
→ Topic may be too niche. Broaden scope or use adjacent creators (e.g., "AI marketing" if "AI micro-segmentation" is too narrow).

**"Meta-patterns contradict each other"**
→ Creators may be targeting different sub-audiences. Identify segments and note in skill.

**"Generated content feels generic"**
→ Meta-patterns may be too generic. Re-run Claude analysis with more specific instructions: "Find patterns that differentiate these creators from each other."

**"Skill replicability is too low"**
→ Creators' styles may be too personal. Consider creating separate skills for each creator instead of a composite skill.

---

## Next Steps After Completion

1. **Validate** research summary (spot-check 2-3 creator analyses)
2. **Monitor** generated content performance (engagement, feedback)
3. **Iterate** on skill based on results (if content underperforms, adjust formula)
4. **Use** skill for ongoing content generation (monthly research cycle)
5. **Archive** research project when complete

**Downstreams**: Content publishing, skill library, ongoing content generation

