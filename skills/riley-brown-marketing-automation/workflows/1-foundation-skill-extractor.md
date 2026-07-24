# Workflow: /riley-skill-extractor

**Tier**: Foundation  
**Complexity**: Low-Medium  
**Time**: 3-10 minutes  
**Cost**: $5-20 (Claude standard reasoning)  
**APIs**: Claude/GPT-5.6, Notion  
**Output**: Callable skill template in `/skills/[creator-name]-voice/`

---

## Pre-Flight Gate

**When to Use**:
- You have a Notion database from `/riley-social-scraper` (5+ videos minimum)
- You want to turn creator patterns into a portable, reusable skill
- You're building a multi-creator skill library

**Prerequisites**:
- Notion database with video transcripts + engagement metrics
- Claude API key (or GPT-5.6)
- Top 5 videos ranked by engagement (from database)

**Don't Use When**:
- You have <3 videos (pattern extraction too noisy)
- Transcripts are <200 words each (insufficient signal)
- Creator's videos span wildly different topics (no coherent voice)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "Creator Voice as Extractable Bytecode"
2. `genius.md` — Section: "Signature Moves: Extract & Extend"
3. `SKILL.md` — Quick Reference: `/riley-skill-extractor`
4. `references/api-integration-guide.md` — Section: "7. Claude/GPT-5.6 API"

**Key Concepts**:
- Voice = constellation of hook style, pacing, CTA pattern, audience assumption
- Extract by analyzing top 5 videos (highest engagement = best representative)
- Output: skill template that downstream workflows can spawn
- Notion as the source of truth (don't re-read transcripts; pull from DB)

---

## Execution

### Step 1: Export Top 5 Videos from Notion

Query the Notion database:

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Query database, sorted by Engagement Score DESC, limit 5
results = client.databases.query(
    database_id="DB_ID",
    filter={
        "property": "Is Sponsored",
        "checkbox": {"equals": False}
    },
    sorts=[{"property": "Engagement Score", "direction": "descending"}],
    page_size=5
)

videos = []
for page in results['results']:
    videos.append({
        "title": page['properties']['Video Title']['rich_text'][0]['text']['content'],
        "transcript": page['properties']['Transcript']['rich_text'][0]['text']['content'],
        "engagement_score": page['properties']['Engagement Score']['formula']['number'],
        "hook_style": page['properties']['Hook Style']['select']['name'] if page['properties']['Hook Style']['select'] else "Unknown"
    })

return videos
```

### Step 2: Build Claude Prompt (Standard Reasoning)

```
You are analyzing the top 5 videos from creator [CREATOR_NAME]. Your task: extract their voice signature.

VIDEOS:
[For each video:]
Title: {title}
Engagement Score: {engagement_score}
Hook Style: {hook_style}

Transcript:
{transcript}

---

Extract and return a JSON object with:
1. hook_formula: The opening move (first 30 seconds, distilled)
2. pacing_pattern: How they build tension/interest (fast/medium/slow, examples)
3. cta_mechanism: How they end (explicit ask? soft? story-based?)
4. audience_assumption: Who is the assumed listener? (age, expertise, pain point)
5. signature_moves: 3-5 unique stylistic tics (e.g., "pauses for effect", "asks rhetorical questions")
6. topic_cluster: Main topics across the 5 videos
7. voice_tone: Tone (authoritative, friendly, urgent, exploratory, comedic)
8. replicability_score: 1-10 how easily can a non-expert replicate this voice?

Return ONLY valid JSON, no explanation.
```

### Step 3: Call Claude API

```python
import anthropic

client = anthropic.Anthropic(api_key="YOUR_CLAUDE_KEY")

response = client.messages.create(
    model="claude-opus-4-1",  # Standard reasoning, not extra-high
    max_tokens=1500,
    messages=[
        {
            "role": "user",
            "content": prompt  # From Step 2
        }
    ]
)

# Parse JSON
import json
voice_signature = json.loads(response.content[0].text)
```

### Step 4: Validate Voice Signature

Check each field:

```python
required_fields = [
    "hook_formula", "pacing_pattern", "cta_mechanism", 
    "audience_assumption", "signature_moves", "topic_cluster", 
    "voice_tone", "replicability_score"
]

for field in required_fields:
    assert field in voice_signature, f"Missing: {field}"
    assert voice_signature[field] not in [None, "", []], f"Empty: {field}"
```

### Step 5: Create Skill Folder Structure

```bash
mkdir -p skills/[creator-name]-voice/
touch skills/[creator-name]-voice/SKILL.md
touch skills/[creator-name]-voice/genius.md
mkdir -p skills/[creator-name]-voice/workflows/
```

### Step 6: Write SKILL.md Template

```markdown
# SKILL: [Creator Name] Voice Generator

**Tier**: Extracted (Foundation → Practitioner)
**Domain**: Content generation, voice replication, messaging
**Extracted From**: /riley-social-scraper (N videos, engagement score 8.5+)
**Last Updated**: [DATE]
**Status**: Production-Ready

---

## Voice Signature

**Hook Formula**: [hook_formula]

**Pacing**: [pacing_pattern]

**CTA Mechanism**: [cta_mechanism]

**Audience Assumption**: [audience_assumption]

**Signature Moves**: 
[signature_moves list]

**Topic Cluster**: [topic_cluster]

**Voice Tone**: [voice_tone]

**Replicability Score**: [replicability_score]/10

---

## How to Use This Skill

When you want to write content in [Creator Name]'s voice:

1. Specify the topic
2. Choose a platform (YouTube, LinkedIn, Instagram)
3. Invoke the workflow: `/[creator-name]-voice-generator`
4. Provide your key message
5. System generates 3 takes in that creator's voice

---

## Example Prompt

"Write a 60-second LinkedIn post about [topic] in [Creator Name]'s voice."

Expected output: Post with their hook formula, pacing, and CTA type.

---

## Anti-Patterns

- Don't force their voice onto unrelated topics (e.g., Fitness creator on tax law)
- Don't skip the CTA; it's core to their formula
- Don't mix hook styles (stay consistent with their signature)

---

## Downstream Uses

- `/[creator-name]-voice-generator` → Generate content
- `/ghostwrite` (Lara) → LinkedIn posts
- `/parallax` → Substack essays

**Master**: genius.md
```

### Step 7: Write genius.md Template

```markdown
# GENIUS: [Creator Name] Voice

**Extraction Date**: [DATE]
**Source**: 5 videos, avg engagement 8.5/10
**Replicability**: [score]/10

---

## The Signature

[Copy from voice_signature JSON, narrative form]

---

## Exemplars

### Video 1: [Title]
**Timestamp**: [HH:MM-HH:MM]
**Hook**: [Quote or description]
**Why it works**: [Brief analysis]

### Video 2: [Title]
**Timestamp**: [HH:MM-HH:MM]
**Hook**: [Quote]
**Why it works**: [Brief analysis]

### Video 3: [Title]
**Timestamp**: [HH:MM-HH:MM]
**Hook**: [Quote]
**Why it works**: [Brief analysis]

---

## Signature Moves

1. [Move 1]: [Description + example]
2. [Move 2]: [Description + example]
3. [Move 3]: [Description + example]
4. [Move 4]: [Description + example]
5. [Move 5]: [Description + example]

---

## Quality Rubric

| Dimension | Score | Notes |
|-----------|-------|-------|
| Fidelity to Source | [1-10] | How accurately does voice match videos? |
| Scalability | [1-10] | Can users generate 10+ posts in this voice? |
| Distinctiveness | [1-10] | Is voice recognizable vs. generic? |
| CTA Clarity | [1-10] | Is call-to-action formula explicit? |
| Topic Flexibility | [1-10] | Can voice adapt to new topics? |
| Ease of Replication | [1-10] | Can non-expert follow the formula? |

**Composite**: [avg]/10

---

## Anti-Patterns

- Don't assume this creator works for [unrelated topic]
- Don't mix this voice with other creators (dilutes signature)
- Don't skip CTAs
- Don't remove pauses/breathing room (part of pacing)
- Don't make audience assumptions different from source videos

---

## What's Next

- Run `/[creator-name]-voice-generator` to create 10 sample posts
- A/B test 3 of them on LinkedIn or YouTube
- Refine based on engagement (feed back into Notion DB)
- Update rubric scores after testing
```

### Step 8: Link to Notion

Add a new page in the Notion database:

```
Title: "Skill Generated: [Creator Name] Voice"
Type: "Meta" (new property)
Linked Skill: /skills/[creator-name]-voice/SKILL.md
```

---

## Content Type Adaptations

### YouTube Videos
- Hook: Usually story, statistic, or question (first 15 sec)
- Pacing: Slower build (allow time for retention)
- CTA: "Subscribe" + soft call to action

### LinkedIn Posts
- Hook: Relatable statement or provocative claim
- Pacing: Fast (scroll-stopping in first 2 lines)
- CTA: Engagement (ask question, invite discussion)

### Instagram Reels / TikTok
- Hook: Visual + audio combo (must work without sound)
- Pacing: Very fast (0.5 sec hook window)
- CTA: Subtle (swipe up, follow, share)

---

## Output Requirements

**Skill Folder**:
- ✓ SKILL.md (500+ words, voice signature explicit)
- ✓ genius.md (1000+ words, exemplars + rubric)
- ✓ workflows/ directory (ready for downstream skills)

**Quality Gate**:
- ✓ Hook formula is specific (not generic)
- ✓ CTA mechanism is replicable
- ✓ Signature moves are testable (can another person execute them?)
- ✓ Replicability score ≥5/10 (too low = voice is too idiosyncratic)

**Next Workflows**:
- `/[creator-name]-voice-generator` (generate content using this voice)
- `/ghostwrite` (Lara uses this voice for LinkedIn)
- `/parallax` (Farrice uses this voice for Substack)

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Hook formula is vague or generic (e.g., "starts with a question")
- [ ] CTA mechanism is missing or unclear
- [ ] Signature moves are descriptive but not actionable
- [ ] Replicability score <5/10 (too hard to replicate)
- [ ] Fewer than 3 signature moves extracted
- [ ] Voice signature doesn't match source videos (sanity check against transcripts)

**Validation Checklist**:
1. Read one source video transcript; highlight the hook (first 30 sec)
2. Compare to extracted hook_formula; does it match?
3. Pick one signature move; re-read a video and spot it in action
4. Take the CTA mechanism; does it appear in ≥3 of the 5 videos?
5. Ask: Could a stranger replicate this voice from the description? (subjective)

**Anti-Patterns**:
- Do NOT over-generalize (e.g., "uses words" is useless)
- Do NOT confuse topic with voice (fitness topic ≠ fitness voice)
- Do NOT extract from only 1-2 videos (patterns too noisy)
- Do NOT skip the source video links (needed for verification)
- Do NOT assume all creators' voices are portable (some are too niche)

---

## Troubleshooting

**"Claude API returns empty response"**
→ Prompt may be too long. Truncate transcripts to 1000 chars each.

**"Replicability score comes back <3/10"**
→ This creator's voice is too idiosyncratic. Consider whether to archive this skill or accept the limitation.

**"Hook formula matches only 1 of 5 videos"**
→ Creator may have inconsistent hooks. Re-run analysis on different set of 5 videos.

**"CTA Mechanism is missing from JSON"**
→ Prompt may need manual follow-up. Add manual step: "Read the CTAs in the 5 videos and list them."

---

## Next Steps After Completion

1. **Test** the voice on 3 sample topics (manual writes)
2. **Register** the skill in `/skills/[creator-name]-voice/` and run sync_registries.py
3. **Create** the downstream `/[creator-name]-voice-generator` workflow
4. **Deploy** to /skills and offer to Farrice for blind pass
5. **Iterate** on rubric scores after live testing

**Downstreams**: `/[creator-name]-voice-generator`, `/ghostwrite` (Lara), `/parallax` (Farrice)

