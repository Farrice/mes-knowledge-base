# Workflow: /riley-farrice-parallax-pipeline

**Tier**: Stacking (Riley + Farrice Voice + Satori + Parallax)  
**Complexity**: Very High  
**Time**: 30-90 minutes  
**Cost**: $50-150 (full stack: Riley $30 + Farrice $10 + Satori $5 + Parallax $5+)  
**APIs**: All Riley APIs + Farrice voice, Satori design, Parallax publishing  
**Output**: End-to-end: Research → Extract patterns → Write essay → Design → Schedule → Distribute

---

## Pre-Flight Gate

**When to Use**:
- You want to research a market, extract patterns, write a deep essay, design it, and distribute it
- You're launching a new series on Substack or LinkedIn with high-polish content
- You're combining Farrice's voice with Riley's research depth

**Prerequisites**:
- All Riley prerequisites (ScrapeCreators, Notion, Claude)
- Farrice's voice loaded (`/voice-os` with BLEND mode)
- Satori design skill loaded (`/satori-frontend-flow`)
- Parallax publishing platform set up
- Substack + LinkedIn distribution channels

**Don't Use When**:
- You need quick turnaround (<4 hours) - this workflow is deliberate
- Topic is too niche (can't find research)
- You're not ready to distribute widely (polish requires audience)

---

## Skill Acquisition

**Read First**:
1. `SKILL.md` — Section: "Tier 3 (Stacking) Integrated Workflows" → "Full Parallax Pipeline"
2. `/riley-research-to-skill-pipeline` workflow (Steps 1-6)
3. Farrice voice documentation (load `FARRICE.md` + `VOICE-CARD.md`)
4. Satori design skill (`/satori-frontend-flow`)
5. Parallax publishing skill (`/parallax`)

**Key Concepts**:
- Research + Extract (Riley) → Write + Design (Farrice + Satori) → Publish + Distribute (Parallax)
- Farrice's voice: show > tell, no forced jargon, reader-as-protagonist
- Satori brings visual hierarchy (doesn't just decorate, it guides reading)
- Parallax handles multi-platform distribution (Substack → Twitter/X → LinkedIn)

---

## Execution

### Step 1: Define Essay Topic & Research Scope

```
Topic: [e.g., "AI tools for solopreneurs"]
Research Angle: [e.g., "What I learned from interviewing 10 solopreneurs using AI"]
Audience: [Who should read this?]
Platforms: [Substack, LinkedIn, Twitter/X]
Format: [Long essay 1500-2500 words]
Visual Style: [Reference: minimalist, data-driven, illustrative?]
Deadline: [Publication date]
```

### Step 2: Research Market (Riley Pipeline)

Run `/riley-research-to-skill-pipeline` (Steps 1-5):

```python
# Step 1: Find 5-10 creators in the space
research_topic = "AI tools for solopreneurs"
creators = find_creators(research_topic)  # Manual or semi-automated

# Step 2: Scrape creator databases
for creator in creators:
    riley_social_scraper(creator_name=creator, limit=10)

# Step 3: Analyze creators
for creator in creators:
    riley_creator_profile_analyzer(database_id=creator_db_id)

# Step 4: Extract meta-patterns
claude_meta_patterns = extract_meta_patterns(
    all_creator_analyses=analyses,
    topic=research_topic
)

# Returns:
# - meta_patterns (3-5 patterns)
# - audience_synthesis (unified audience profile)
# - topic_synthesis (core topics + hierarchy)
# - persuasion_synthesis (winning hook + CTA patterns)
# - content_formula (ideal structure)
# - your_angle (differentiation opportunity)

return claude_meta_patterns
```

### Step 3: Create Essay Outline (Farrice's Voice)

Using research + Farrice's voice, create structure:

```
ESSAY OUTLINE: [Topic]

HERO MOVE (The Reason to Read):
- [What makes this essay different?]
- [Why does Farrice have authority on this?]
- [What will reader know they didn't before?]

SETUP (Draw Them In):
- Hook: [specific moment or question that makes them nod]
- Context: [what's changed that makes this timely?]
- Why it matters: [to THEM, not abstract]

ACT 1: THE PROBLEM (Show the Real Tension)
- [Real challenge solopreneurs face]
- [Why existing solutions don't work]
- [What costs them today]

ACT 2: THE EXPLORATION (Show Your Thinking)
- [Tool A: What it does, how it fits]
- [Tool B: Where it shines, where it doesn't]
- [Tool C: The surprising take on it]
- [Pattern emerging: What unites the wins?]

ACT 3: THE INSIGHT (The Payoff)
- [What you realized]
- [Why this changes how we think about X]
- [The real play going forward]

CLOSING (Make Them Believer)
- [Why this matters to Farrice]
- [One thing to try this week]
- [Invitation to engage]
---

VOICE GUARDRAILS:
- ✓ Show > Tell (use specific examples, not abstractions)
- ✓ Reader-as-protagonist (they discover, not I tell them)
- ✓ Conversational, not academic
- ✓ Vulnerability + payoff (don't leave them hanging)
```

### Step 4: Write Essay (Farrice's Voice)

Using outline + meta-patterns from research:

```python
# Invoke Farrice voice in BLEND mode
essay_prompt = f"""
Write an essay for Farrice's Substack using the outline above.

RESEARCH INSIGHTS:
{claude_meta_patterns}

KEY MOVES TO INCLUDE:
- [meta-pattern 1]
- [meta-pattern 2]
- [meta-pattern 3]

VOICE DIAL: BLEND
- Show specific examples (don't say "many solopreneurs use AI"; say "Sarah built a $50k/year business with Claude + Zapier")
- Reader-as-protagonist (they discover the insight, not I hand it to them)
- Conversational tone (friend-on-shoulder, not guru-from-on-high)

TARGET: 1800-2200 words
Structure: Follow outline exactly
Deadline: [publication date]

Write first draft for review.
"""

# Call Farrice voice skill
farrice_output = invoke_skill(
    skill_name="voice-os",
    mode="BLEND",
    context="substack_essay",
    prompt=essay_prompt
)

# Returns:
# - essay (full text, 1800+ words)
# - metadata: hooks, structure summary, tone check
```

### Step 5: Add to Notion + Send for Review

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Add essay to Notion
essay_page = client.pages.create(
    parent={"database_id": "CONTENT_DB_ID"},
    properties={
        "Title": {"title": [{"text": {"content": essay_topic}}]},
        "Status": {"select": {"name": "Draft - Writing Review"}},
        "Platform": {"select": {"name": "Substack"}},
        "Content Type": {"select": {"name": "Essay"}},
        "Voice": {"select": {"name": "Farrice"}},
        "Essay Text": {"rich_text": [{"text": {"content": farrice_output['essay']}}]},
        "Research Topic": {"rich_text": [{"text": {"content": research_topic}}]},
        "Scheduled Date": {"date": {"start": publication_date.isoformat()}}
    }
)

# Send to Farrice for review
review_email = f"""
Hi Farrice,

Essay draft ready for review: {essay_topic}

Draft: [NOTION_LINK]

Review checklist:
□ Voice feels authentic (show > tell, reader-as-protagonist)
□ Research insights are woven in (not just dumped)
□ Hook lands in first paragraph
□ Structure flows (follows outline)
□ Payoff is clear (reader knows what changed)
□ No forced jargon or abstract talk
□ Tone is friend-on-shoulder, not guru

Feedback: Approve, request changes, or rewrite.

Timeline: [review deadline]

---

Farrice
"""

send_email(to="farrice.cain@gmail.com", subject=f"Review: {essay_topic}", body=review_email)
```

### Step 6: Design Essay (Satori)

Once essay is approved, send to design:

```python
# Export essay to Satori
satori_brief = {
    "title": essay_topic,
    "body": farrice_output['essay'],
    "format": "Substack essay (web-optimized, long-form)",
    "visual_style": "minimalist, data-driven",
    "accent_color": "farrice's brand color",
    "imagery": "optional illustration (not required)",
    "purpose": "Read-maximizing design (flow, hierarchy, pacing)"
}

# Call Satori design workflow
satori_output = invoke_skill(
    skill_name="satori-frontend-flow",
    brief=satori_brief,
    purpose="essay_web_layout"
)

# Returns:
# - layout (web-optimized HTML/Markdown)
# - visual_hierarchy (where eyes go first)
# - pacing (where to add white space, breaks)
# - imagery (if any)
```

### Step 7: Create Parallax Distribution Plan

Set up multi-platform distribution:

```
PARALLAX DISTRIBUTION PLAN

PRIMARY: Substack Essay
- Title: [essay topic]
- Length: [word count]
- Visual: [Satori design]
- Publication: [date + time]

SECONDARY: LinkedIn Adaptation
- Format: 5-10 connected posts (thread)
- Length: 100-200 words per post
- Hook: [LinkedIn-native hook]
- Cadence: Post 1 per day, 5 posts total

TERTIARY: Twitter/X Thread
- Format: 15-20 tweet thread
- Hook: [hook for Twitter]
- Cadence: Live tweet thread or scheduled

ENGAGEMENT SEQUENCE:
1. Publish essay on Substack
2. Email list sees it (Substack native)
3. LinkedIn: Post thread starting next morning
4. Twitter: Tweet thread day after
5. Monitor engagement: replies, shares, new subscribers
```

### Step 8: Invoke Parallax for Publishing

```python
# Call Parallax publishing skill
parallax_output = invoke_skill(
    skill_name="parallax",
    essay_title=essay_topic,
    essay_html=satori_output['html'],
    distribution_plan={
        "substack": {
            "date": publication_date,
            "time": "08:00",
            "title": essay_topic
        },
        "linkedin": {
            "format": "thread",
            "num_posts": 8,
            "cadence": "1 per day"
        },
        "twitter": {
            "format": "thread",
            "num_tweets": 15,
            "cadence": "live"
        }
    }
)

# Returns:
# - substack_url (published essay)
# - linkedin_posts (8 scheduled posts)
# - twitter_thread (ready to post)
```

### Step 9: Monitor Performance & Close Loop

```python
# Track:
# - Substack: new subscribers, read time, shares
# - LinkedIn: engagement rate, follower growth
# - Twitter: retweets, quote tweets, replies
# - Referer tracking: which platform drives traffic back to Substack

# Update Notion with performance data
metrics_update = {
    "Status": "Published",
    "Substack Subscribers": "[number]",
    "Engagement Rate": "[percentage]",
    "Most Engaging Platform": "[LinkedIn|Twitter|Direct]",
    "Next Steps": "[Ideas for follow-up content]"
}

client.pages.update(page_id=essay_page['id'], properties=metrics_update)
```

---

## Output Requirements

**End-to-End Deliverables**:
- ✓ Research complete (5-10 creators analyzed, meta-patterns extracted)
- ✓ Essay drafted + approved (1800-2200 words in Farrice's voice)
- ✓ Essay designed (Satori layout, web-optimized)
- ✓ Substack essay published + live
- ✓ LinkedIn thread created (8 posts scheduled)
- ✓ Twitter thread created (15 tweets scheduled)
- ✓ Performance tracked + documented

**Quality Gate**:
- ✓ Essay voice is authentic (Farrice, not AI-generic)
- ✓ Research insights are woven in (not dumped)
- ✓ Satori design enhances reading (visual hierarchy)
- ✓ LinkedIn thread flows (not just essay snippets)
- ✓ Twitter thread is native (not essay regurgitated)
- ✓ All platforms linked + trackable

**Next Workflows**:
- Monitor performance across platforms
- Iterate based on engagement
- Use successful essay as model for future pieces

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Essay doesn't sound like Farrice (voice extraction failed)
- [ ] Research insights are top-level or absent (Riley failed)
- [ ] Satori design doesn't enhance reading (just decorative)
- [ ] LinkedIn posts are just essay excerpts (no adaptation)
- [ ] Twitter thread reads like article chunks (not Twitter-native)
- [ ] No performance tracking (can't iterate)

**Validation Checklist**:
1. Read essay opening (first 3 paragraphs); does voice feel like Farrice? (show > tell, reader-as-protagonist)
2. Spot a research insight; is it woven in smoothly or dumped? (should feel native)
3. Look at Satori design; does visual hierarchy guide reading? (does it feel like more than decoration?)
4. Read first LinkedIn post; could it stand alone? (yes = adaptation; no = failure)
5. Scan Twitter thread; do tweets feel native to platform? (not just essay snippets)

**Anti-Patterns**:
- Do NOT write essay then adapt (research should inform writing from the start)
- Do NOT skip Farrice's voice review (even strong essay needs voice calibration)
- Do NOT use generic Substack formatting (Satori should enhance, not replace)
- Do NOT force essay into LinkedIn/Twitter (adapt and remix, don't regurgitate)
- Do NOT publish without performance tracking (can't iterate without data)

---

## Troubleshooting

**"Essay doesn't sound like Farrice"**
→ Voice brief may be too sparse. Load VOICE-CARD.md + add specific examples to prompt.

**"Research insights are too academic"**
→ Research was extracted as patterns; need to translate to Farrice's voice (show, not tell).

**"Satori design looks over-designed"**
→ Satori can overcomplicate. Brief: "Minimize visual flourish; maximize readability."

**"LinkedIn adaptation feels forced"**
→ You forced essay into LinkedIn format. Instead: rewrite as LinkedIn-native thread (different structure).

**"Twitter thread isn't engaging"**
→ Twitter-native means hooks in tweets 1, 3, 5, etc. (not just information). Re-thread with engagement points.

---

## Next Steps After Completion

1. **Publish** on schedule (Substack → LinkedIn → Twitter)
2. **Monitor** performance (track subscribers, engagement, traffic)
3. **Iterate** (If essay underperforms, analyze why + refine approach)
4. **Re-run** quarterly (build momentum with themed essay series)
5. **Compound** (Link essays together; build narrative arc over time)

**Downstreams**: Substack subscriber growth, LinkedIn authority building, Twitter reach expansion, newsletter revenue

---

## Timeline Example

```
Day 1: Research phase (4-6 hours)
  - Find 5-10 creators
  - Scrape databases
  - Analyze profiles
  - Extract meta-patterns

Day 2-3: Writing phase (4-6 hours)
  - Create outline
  - Draft essay (Farrice voice)
  - Review + revise
  - Approve for design

Day 4-5: Design + publish phase (2-4 hours)
  - Satori designs layout
  - Finalize essay
  - Schedule on Substack
  - Create LinkedIn thread
  - Create Twitter thread

Day 6+: Distribution + monitoring
  - Publish on schedule
  - Monitor engagement
  - Report results
```

**Total Time: 30-90 minutes active work (research + writing + design + publishing)**

