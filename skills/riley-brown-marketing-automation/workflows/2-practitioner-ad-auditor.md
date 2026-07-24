# Workflow: /riley-ad-performance-auditor

**Tier**: Practitioner  
**Complexity**: Medium  
**Time**: 5-20 minutes  
**Cost**: $10-30 (Claude extra-high reasoning + Foreplay monthly)  
**APIs**: Foreplay, Claude, Notion  
**Output**: Structured ad analysis (success patterns, hooks, CTAs, actionable recommendations)

---

## Pre-Flight Gate

**When to Use**:
- You have a Notion database from `/riley-competitor-scraper` (10+ ads minimum)
- You want to understand WHY competitor ads are working
- You're building an ad creative strategy or testing plan

**Prerequisites**:
- Notion database with competitor ads (sorted by duration)
- Claude API key (for extra-high reasoning)
- 10+ longest-running ads (90+ days minimum)

**Don't Use When**:
- Ads have <30 days runtime (too new to assess performance)
- You need actual ROI data (Foreplay gives proxy only: runtime)
- Competitor ads are too diverse (no coherent strategy to extract)

---

## Skill Acquisition

**Read First**:
1. `genius.md` — Section: "Longest-Running Ads as ROI Proxy Heuristic"
2. `genius.md` — Section: "Comparative Analysis: The Audit Frame"
3. `SKILL.md` — Quick Reference: `/riley-ad-performance-auditor`
4. `references/api-integration-guide.md` — Section: "7. Claude/GPT-5.6 API" (Extra-High Reasoning)

**Key Concepts**:
- Duration is a proxy for performance (not ground truth)
- Winning ads share common patterns (hooks, proof, urgency, CTAs)
- Your job: reverse-engineer the formula by analyzing 3-5 longest-running ads
- Output: actionable recommendations for your own ads

---

## Execution

### Step 1: Extract Longest-Running Ads from Notion

Query the database (filter by duration 90+ days):

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Query database, sorted by Duration DESC, filter >90 days
results = client.databases.query(
    database_id="DB_ID",
    filter={
        "property": "Duration (days)",
        "number": {"greater_than_or_equal_to": 90}
    },
    sorts=[{"property": "Duration (days)", "direction": "descending"}],
    page_size=5  # Top 5 longest-running
)

ads = []
for page in results['results']:
    props = page['properties']
    ads.append({
        "ad_id": props['Ad ID']['rich_text'][0]['text']['content'],
        "competitor": props['Competitor']['select']['name'],
        "platform": props['Platform']['select']['name'],
        "ad_type": props['Ad Type']['select']['name'],
        "copy": props['Copy']['rich_text'][0]['text']['content'],
        "hook": props['Hook']['rich_text'][0]['text']['content'] if props['Hook']['rich_text'] else "",
        "cta_text": props['CTA Text']['rich_text'][0]['text']['content'] if props['CTA Text']['rich_text'] else "",
        "duration_days": props['Duration (days)']['number'],
        "last_seen": props['Last Seen']['date']['start']
    })

return ads
```

### Step 2: Build Claude Prompt (Extra-High Reasoning)

```
You are analyzing 5 competitor ads that have been running 90+ days. These are PROVEN winners (longest runtime = assumed best ROI).

Your task: reverse-engineer the success formula.

ADS:
[For each ad, numbered 1-5:]
Ad {N}: {competitor} on {platform} ({duration_days} days running)
Hook: {hook}
Copy: {copy}
CTA: {cta_text}

---

Analyze and return a JSON object with:

1. success_patterns:
   - [Pattern 1]: [What all 5 ads share that makes them work?]
   - [Pattern 2]: [Another common element?]
   - (etc., 3-5 patterns max)

2. hook_analysis:
   - types_present: [List hook types observed: Story, Question, Statistic, Emotion, Curiosity Gap, etc.]
   - most_effective_hook: [Which hook type appears most in the 5 ads?]
   - why_it_works: [Why is that hook type effective for this audience?]

3. copy_strategy:
   - problem_framing: [How is the problem presented?]
   - solution_positioning: [How is the solution presented?]
   - proof_mechanism: [How is proof/credibility established?]
   - urgency_tactics: [Is urgency used? How? (Scarcity, time-based, social proof, etc.)]

4. cta_mechanism:
   - cta_types_present: [List CTA types: Sign Up, Download, View More, Buy, Comment, etc.]
   - most_common_cta: [Which CTA appears most?]
   - why_effective: [Why does that CTA work for this audience/product?]

5. platform_fit:
   - facebook_instagram_specific: [Visual design, 3-second hook, etc.]
   - tiktok_specific: [Trend usage, music, pacing, etc.]
   - linkedin_specific: [Credibility focus, professional tone, etc.]

6. differentiation_gaps:
   - what_competitors_avoid: [What topics/approaches are NOT used?]
   - opportunity_angles: [What angles could you test that competitors aren't?]

7. predicted_roi_ranking:
   - [Ad 1]: Why it's winning (score 1-10)
   - [Ad 2]: Why it's winning (score 1-10)
   - (etc.)

8. actionable_recommendations:
   - for_your_own_ads: [Specific moves to copy from these winners]
   - risky_experiments: [What could you test that's different?]
   - avoid_list: [What NOT to do based on competitor absence?]

Return ONLY valid JSON, no explanation.
```

### Step 3: Call Claude API (Extra-High Reasoning)

```python
import anthropic
import json

client = anthropic.Anthropic(api_key="YOUR_CLAUDE_KEY")

response = client.messages.create(
    model="claude-opus-4-1",
    max_tokens=3000,
    thinking={
        "type": "enabled",
        "budget_tokens": 15000  # Extra-high reasoning budget
    },
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# Extract JSON from response
analysis_text = response.content[-1].text
analysis = json.loads(analysis_text)
```

### Step 4: Validate Analysis

```python
required_fields = [
    "success_patterns", "hook_analysis", "copy_strategy",
    "cta_mechanism", "platform_fit", "differentiation_gaps",
    "predicted_roi_ranking", "actionable_recommendations"
]

for field in required_fields:
    assert field in analysis, f"Missing: {field}"
    assert analysis[field] not in [None, "", {}], f"Empty: {field}"
```

### Step 5: Create Ad Audit Report in Notion

Add analysis results as a linked page or export:

```python
# Create new page in Ad Audits DB
audit_page = client.pages.create(
    parent={"database_id": "AUDITS_DB_ID"},
    properties={
        "Title": {"title": [{"text": {"content": f"Ad Audit: {analysis['predicted_roi_ranking']}"}}]},
        "Date": {"date": {"start": datetime.now().isoformat()}},
        "Success Patterns": {"rich_text": [{"text": {"content": str(analysis['success_patterns'])}}]},
        "Hook Types": {"rich_text": [{"text": {"content": analysis['hook_analysis']['most_effective_hook']}}]},
        "Copy Strategy": {"rich_text": [{"text": {"content": str(analysis['copy_strategy'])}}]},
        "CTA Type": {"select": {"name": analysis['cta_mechanism']['most_common_cta']}},
        "Differentiation Gaps": {"rich_text": [{"text": {"content": str(analysis['differentiation_gaps'])}}]},
        "Recommendations": {"rich_text": [{"text": {"content": str(analysis['actionable_recommendations'])}}]},
        "Status": {"select": {"name": "Analyzed"}}
    }
)

return audit_page['id']
```

### Step 6: Generate Audit Report (Markdown Export)

```
# Ad Performance Audit: [Date]

## Executive Summary
These 5 ads have been running 90+ days. Analysis reveals the winning formula.

## Success Patterns
[For each pattern:]
Pattern: [Pattern Name]
Evidence: [Which ads show this pattern?]
Why it works: [Analysis]

## Hook Analysis
Most Effective Hook Type: [hook type]
Why: [explanation]

Hooks observed:
  - [Ad 1]: [hook]
  - [Ad 2]: [hook]
  - [Ad 3]: [hook]
  - [Ad 4]: [hook]
  - [Ad 5]: [hook]

## Copy Strategy
Problem Framing: [how it's presented]
Solution Positioning: [how it's positioned]
Proof Mechanism: [how credibility is shown]
Urgency: [if any]

## CTA Mechanism
Most Common CTA: [CTA type]
Why it works: [why this CTA resonates]

CTAs observed:
  - [Ad 1]: [CTA]
  - [Ad 2]: [CTA]
  - [Ad 3]: [CTA]
  - [Ad 4]: [CTA]
  - [Ad 5]: [CTA]

## Platform Fit
Facebook/Instagram: [specific tactics]
TikTok: [specific tactics]
LinkedIn: [specific tactics]

## Differentiation Gaps
What competitors AVOID:
  - [topic/approach 1]
  - [topic/approach 2]

Opportunity angles (unexplored):
  - [angle 1]
  - [angle 2]

## Predicted ROI Ranking
1. [Ad 1 title] — Score: [1-10]
   Why: [reason]

2. [Ad 2 title] — Score: [1-10]
   Why: [reason]

(etc.)

## Actionable Recommendations

### For Your Own Ads
- [Specific move 1]
- [Specific move 2]
- [Specific move 3]

### Risky Experiments (Test These)
- [Experiment 1]
- [Experiment 2]

### Avoid List
- [Don't do this]
- [Don't do that]
```

---

## Content Type Adaptations

### Video Ads (Facebook, Instagram, TikTok)
- Hook: First 1-3 seconds MUST stop scroll
- Pacing: Fast cuts, pattern interrupts
- CTA: Swipe up, tap link, or comment
- Proof: Show results, testimonials, or demo

### Static Image Ads
- Hook: Headline + image combo
- Copy: Benefit-driven headline + supporting body (50-150 words)
- CTA: Button (Learn More, Sign Up, Buy)
- Proof: Subtext with credibility (5,000+ customers, etc.)

### Carousel Ads
- Hook: First card hooks (visual + text combo)
- Flow: Card 2 builds on card 1, etc.
- CTA: Usually on last card
- Proof: Spread across multiple cards

---

## Output Requirements

**Ad Audit Report**:
- ✓ 3-5 success patterns identified (not generic)
- ✓ Hook types analyzed with reasoning
- ✓ Copy strategy broken down (problem → solution → proof → CTA)
- ✓ CTA mechanism explained with rationale
- ✓ Differentiation gaps reveal opportunities
- ✓ Actionable recommendations are specific (not "write better copy")

**Quality Gate**:
- ✓ Patterns repeat across ≥3 of the 5 ads (signal, not noise)
- ✓ Hook analysis matches source ad copy (sanity check)
- ✓ CTA recommendation explains WHY it works
- ✓ Differentiation gaps are non-obvious
- ✓ Risky experiments are testable (not vague)

**Next Workflows**:
- Feed to `/riley-luke-copy-auditor` (copywriting lens)
- Feed to your own ad creation workflow
- Use recommendations to brief creative team

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Success patterns are generic (e.g., "has a call-to-action")
- [ ] Hook analysis doesn't reference actual hooks from ads
- [ ] CTA recommendation lacks reasoning
- [ ] Differentiation gaps are surface-level (e.g., "different colors")
- [ ] Risky experiments are too vague or risky
- [ ] Predicted ROI ranking doesn't align with duration data

**Validation Checklist**:
1. Pick one success pattern; verify it appears in ≥3 of the 5 ads (scan copy)
2. Read the hook analysis; does most-effective-hook match the ads' opening lines?
3. Review CTA recommendation; ask: "Would an average marketer understand WHY this CTA works?"
4. Scan differentiation gaps; are they surprising? (If obvious, they're not opportunities)
5. Pick one risky experiment; ask: "Is this testable and specific?" (If vague, re-prompt)

**Anti-Patterns**:
- Do NOT assume longest-running = best (could be inertia)
- Do NOT over-index on one ad (analyze pattern across all 5)
- Do NOT recommend copying verbatim (adapt, don't clone)
- Do NOT ignore platform differences (TikTok ≠ LinkedIn)
- Do NOT skip the CTA mechanism (it's often the difference between success/fail)

---

## Troubleshooting

**"Claude API returns surface-level patterns"**
→ Prompt may need more ad copy samples. Include full copy, not just hooks.

**"Predicted ROI ranking doesn't match duration data"**
→ Claude may be inferring quality beyond duration. That's OK; ask Claude to weight duration more heavily in scoring.

**"Differentiation gaps feel obvious"**
→ Competitors may be running a unified strategy. Consider: are the gaps actually opportunities, or evidence of a saturated market?

**"Risky experiments are too risky"**
→ Balance innovation with caution. Re-prompt: "List experiments that are 60% likely to succeed, not 20%."

---

## Next Steps After Completion

1. **Validate** audit report against source ads (spot-check 3 patterns)
2. **Share** with creative team or use for your own ad briefs
3. **Feed to** `/riley-luke-copy-auditor` (copywriting lens)
4. **Test** top recommendations on 3 new ad variations
5. **Iterate** based on performance data

**Downstreams**: `/riley-luke-copy-auditor`, your ad creation process, `/parallax` (if converting to content)

