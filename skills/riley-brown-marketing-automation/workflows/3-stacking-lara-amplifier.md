# Workflow: /riley-lara-amplifier

**Tier**: Stacking (Riley + Lara Acosta)  
**Complexity**: Medium  
**Time**: 15-30 minutes  
**Cost**: $25-40 (Riley $15 + Lara $10-25)  
**APIs**: All Riley APIs + Lara's ghostwriting skill  
**Output**: 5-10 LinkedIn posts in extracted creator's voice, scheduled

---

## Pre-Flight Gate

**When to Use**:
- You want to generate LinkedIn content in a creator's voice
- You're combining Riley's extraction with Lara's LinkedIn expertise
- You're scaling LinkedIn content production

**Prerequisites**:
- Notion database from `/riley-social-scraper` (LinkedIn creators preferred)
- Lara Acosta skill loaded (`/ghostwrite` or `/lara-acosta-linkedin-ghostwriter`)
- LinkedIn content calendar set up

**Don't Use When**:
- Creator's voice is not LinkedIn-appropriate (e.g., pure TikTok creator)
- You need platform-specific expertise beyond LinkedIn
- Audience is too niche for generic LinkedIn distribution

---

## Skill Acquisition

**Read First**:
1. `SKILL.md` — Section: "Tier 2 (Practitioner) Extensions" → "Riley + Lara Acosta"
2. `/riley-skill-extractor` workflow (step 6+)
3. Lara Acosta skill documentation (load via `/ghostwrite`)

**Key Concepts**:
- Lara specializes in LinkedIn ghostwriting + growth
- Riley provides voice extraction + creator profiles
- Handoff: Riley's extracted voice → Lara's LinkedIn formula
- Output: Authentic voice on LinkedIn platform

---

## Execution

### Step 1: Extract Creator Voice via Riley

Run `/riley-skill-extractor` on creator database (LinkedIn-focused):

```python
# Use Riley workflow to extract voice
voice_signature = riley_skill_extractor(
    database_id=creator_db_id,
    filter_platform="LinkedIn"  # Optional: focus on LinkedIn videos/posts
)

# voice_signature includes:
# - hook_formula
# - cta_mechanism
# - audience_assumption
# - signature_moves
# - etc.
```

### Step 2: Create Lara Briefing Document

Prepare input for Lara's ghostwriting workflow:

```
CREATOR VOICE BRIEF FOR LARA

Creator: [Creator Name]
Audience: [audience_assumption from Riley analysis]
Voice Tone: [voice_tone]

SIGNATURE HOOKS:
- [hook 1]: [description + example]
- [hook 2]: [description + example]
- [hook 3]: [description + example]

SIGNATURE MOVES:
- [move 1]
- [move 2]
- [move 3]

CTA PATTERN:
- [CTA type and why it works]

FORBIDDEN:
- [Don't do this]
- [And don't do that]

SAMPLE TOPICS TO WRITE ABOUT:
1. [Topic 1]
2. [Topic 2]
3. [Topic 3]
4. [Topic 4]
5. [Topic 5]

DESIRED OUTPUT:
- 5-10 LinkedIn posts
- 150-400 words each
- In [Creator Name]'s authentic voice
- Posted 3 days apart
- With native LinkedIn formatting (line breaks, emojis, etc.)
```

### Step 3: Invoke Lara's Ghostwriting Workflow

```python
# Call Lara's ghostwriting skill
lara_output = invoke_skill(
    skill_name="lara-acosta-ghostwriter",
    mode="linkedin",
    voice_brief=brief_document,
    num_posts=8,
    topics=sample_topics
)

# lara_output includes:
# - 8 LinkedIn posts in creator's voice
# - Metadata: posting date recommendations, hashtags
```

### Step 4: Add Generated Posts to Content Calendar

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

for post in lara_output['posts']:
    client.pages.create(
        parent={"database_id": calendar_db_id},
        properties={
            "Post Title": {"title": [{"text": {"content": post['headline']}}]},
            "Creator/Source": {"select": {"name": f"{creator_name} (via Lara)"}},
            "Platform": {"select": {"name": "LinkedIn"}},
            "Status": {"select": {"name": "Draft"}},
            "Content": {"rich_text": [{"text": {"content": post['body']}}]},
            "Voice Source": {"select": {"name": "Riley Extracted"}},
            "Ghost Writer": {"select": {"name": "Lara Acosta"}}
        }
    )

print(f"✓ Added {len(lara_output['posts'])} LinkedIn posts to calendar")
```

### Step 5: Schedule Posts (3 days apart)

Use `/riley-content-calendar-orchestrator` to schedule:

```python
import datetime

# Get all Draft posts added by Lara
draft_posts = client.databases.query(
    database_id=calendar_db_id,
    filter={
        "and": [
            {"property": "Ghost Writer", "select": {"equals": "Lara Acosta"}},
            {"property": "Status", "select": {"equals": "Draft"}}
        ]
    },
    page_size=10
)

# Schedule 3 days apart, starting next Tuesday
start_date = get_next_tuesday()
posts = draft_posts['results']

for i, page in enumerate(posts):
    scheduled_date = start_date + datetime.timedelta(days=i*3)
    
    client.pages.update(
        page_id=page['id'],
        properties={
            "Scheduled Date": {"date": {"start": scheduled_date.isoformat()}},
            "Status": {"select": {"name": "Scheduled"}}
        }
    )

print(f"✓ Scheduled {len(posts)} posts")
```

### Step 6: Send Review to Farrice

```python
# Send review email with all posts
review_email_body = f"""
Hi Farrice,

Lara has generated 8 LinkedIn posts in {creator_name}'s voice.

Posts are scheduled starting {start_date}, 3 days apart.

Review & approve in Notion calendar (link below), or reply with feedback.

Calendar: [NOTION_CALENDAR_URL]

Approve all → I'll schedule for publication.
Request changes → I'll iterate with Lara.

---

SAMPLE POST 1:
{posts[0]['body'][:200]}...

SAMPLE POST 2:
{posts[1]['body'][:200]}...

(See full posts in Notion)

Farrice
"""

send_email(
    to="farrice.cain@gmail.com",
    subject=f"Review: LinkedIn Posts ({creator_name} voice via Lara)",
    body=review_email_body
)
```

---

## Output Requirements

**LinkedIn Posts**:
- ✓ 5-10 posts generated
- ✓ 150-400 words each
- ✓ Authentic to creator's voice (not generic)
- ✓ LinkedIn-native formatting (line breaks, emojis, tags)
- ✓ Scheduled 3 days apart on Tuesdays (peak engagement day)

**Quality Gate**:
- ✓ Posts reflect creator's voice signature (spot-check against source)
- ✓ CTAs match creator's pattern (not Lara's default)
- ✓ No LinkedIn slop or generic phrases
- ✓ Posts are actionable (not just inspirational fluff)
- ✓ Audience assumptions match Riley's analysis

**Next Workflows**:
- Publish to LinkedIn
- Monitor engagement (compare to creator's baseline)
- Iterate on Lara's voice calibration

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Posts don't sound like creator (voice extraction failed)
- [ ] Posts are generic LinkedIn motivation (Lara slipped into default mode)
- [ ] CTAs don't match creator's pattern
- [ ] Posts have LinkedIn slop phrases ("Here's what I learned...", "Let me share...")
- [ ] Tone is off (too formal, too casual, etc.)

**Validation Checklist**:
1. Read one generated post; compare to creator's actual LinkedIn posts (do they sound alike?)
2. Verify CTAs match creator's pattern (extracted via Riley)
3. Scan for slop phrases (check against `directives/ai-slop-ban-bank.md`)
4. Check tone (matches voice_tone from Riley analysis?)
5. Ask: "Would this creator actually post this?" (subjective but important)

**Anti-Patterns**:
- Do NOT use LinkedIn's default post format (Lara knows native formatting)
- Do NOT skip voice extraction (Lara needs it to stay authentic)
- Do NOT assume all creators work on LinkedIn (verify audience fit first)
- Do NOT publish without review (even if post looks good)

---

## Troubleshooting

**"Posts sound like Lara, not the creator"**
→ Voice brief was too sparse. Add more specific examples from Riley's analysis.

**"Posts don't generate engagement"**
→ May be audience-topic mismatch. Check Riley's audience analysis: is this creator's audience active on LinkedIn?

**"Lara's default tone leaked through"**
→ Re-brief with stronger voice constraints. Add "FORBIDDEN" section to brief.

**"CTAs are generic"**
→ Specify CTA pattern more explicitly in brief (give 3 examples from creator).

---

## Next Steps After Completion

1. **Validate** posts against creator's authentic voice (blind test)
2. **Publish** per schedule (calendar handles automation)
3. **Monitor** engagement (compare to creator's baseline)
4. **Refine** voice brief based on performance
5. **Re-run** quarterly or when creator's voice evolves

**Downstreams**: LinkedIn publishing, engagement monitoring, voice refinement

