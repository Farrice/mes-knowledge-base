# Workflow: /riley-luke-copy-auditor

**Tier**: Stacking (Riley + Luke Iha)  
**Complexity**: Medium  
**Time**: 10-20 minutes  
**Cost**: $15-35 (Riley $10 + Luke $5-25)  
**APIs**: Foreplay, Claude, Luke Iha skill  
**Output**: Competitor ad copy audit + persuasion gaps identified

---

## Pre-Flight Gate

**When to Use**:
- You want to audit competitor ad copy through a copywriting lens
- You need to identify persuasion gaps in competitor messaging
- You're refining your own ad copy using proven competitor patterns

**Prerequisites**:
- Notion database from `/riley-competitor-scraper` (10+ ads minimum)
- Luke Iha copywriting skill loaded (`/luke-iha-vicious-hooks` or similar)
- Foreplay API (for competitor ad data)

**Don't Use When**:
- You only have 3-5 competitor ads (too few for comparison)
- Ads are from different industries (patterns won't transfer)
- You're not ready to action copy improvements

---

## Skill Acquisition

**Read First**:
1. `SKILL.md` — Section: "Tier 2 (Practitioner) Extensions" → "Riley + Luke Iha"
2. `/riley-ad-performance-auditor` workflow (output format)
3. Luke Iha skill documentation (load via `/luke-iha-vicious-hooks`)

**Key Concepts**:
- Riley provides ad data + performance context (duration as ROI proxy)
- Luke audits copy through copywriting lens (persuasion, hooks, proof, urgency)
- Handoff: Riley's winning ads → Luke's persuasion checklist
- Output: Actionable copy improvements for your own ads

---

## Execution

### Step 1: Extract Top Performing Ads from Notion

Query longest-running ads (90+ days):

```python
import notion_client

client = notion_client.Client(auth="YOUR_NOTION_TOKEN")

# Get longest-running ads
results = client.databases.query(
    database_id="AD_DB_ID",
    filter={"property": "Duration (days)", "number": {"greater_than_or_equal_to": 90}},
    sorts=[{"property": "Duration (days)", "direction": "descending"}],
    page_size=5
)

ads = []
for page in results['results']:
    props = page['properties']
    ads.append({
        "ad_id": props['Ad ID']['rich_text'][0]['text']['content'],
        "copy": props['Copy']['rich_text'][0]['text']['content'],
        "hook": props['Hook']['rich_text'][0]['text']['content'],
        "cta": props['CTA Text']['rich_text'][0]['text']['content'],
        "duration_days": props['Duration (days)']['number'],
        "competitor": props['Competitor']['select']['name']
    })

return ads
```

### Step 2: Create Luke Audit Brief

Prepare structured input for Luke:

```
COPY AUDIT BRIEF FOR LUKE IHA

Research: Competitor Ad Analysis
Competitive Set: [Competitor 1, Competitor 2, Competitor 3]

TOP PERFORMING ADS (90+ days running):

AD 1: [Competitor A]
Duration: [days] (assumed strong performer)
Hook: [hook text]
Copy: [full ad copy]
CTA: [CTA text]

AD 2: [Competitor B]
Duration: [days]
Hook: [hook text]
Copy: [full ad copy]
CTA: [CTA text]

AD 3: [Competitor C]
Duration: [days]
Hook: [hook text]
Copy: [full ad copy]
CTA: [CTA text]

---

AUDIT FOCUS:
1. Hook effectiveness (what makes them work?)
2. Problem-agitation (how is pain amplified?)
3. Solution credibility (proof mechanism)
4. Call-to-action (urgency + clarity)
5. Persuasion gaps (what's missing?)

AUDIENCE CONTEXT:
[From Riley analysis: audience demographics + pain points]

INDUSTRY CONTEXT:
[What makes this category different?]

DESIRED OUTPUT:
- Persuasion checklist (✓ what they do right)
- Gap analysis (✗ what's missing)
- Recommendations for our ads (what to test)
- Risk signals (what to avoid)
```

### Step 3: Invoke Luke's Copywriting Skill

```python
# Call Luke's skill to audit copy
luke_output = invoke_skill(
    skill_name="luke-iha-copywriting-auditor",
    mode="ad_copy_audit",
    brief=audit_brief,
    focus_areas=["hooks", "problem_agitation", "credibility", "urgency", "gaps"]
)

# luke_output includes:
# - Persuasion checklist (what each ad does right)
# - Gap analysis (missing elements)
# - Recommendations (specific moves to test)
# - Risk signals (patterns to avoid)
```

### Step 4: Create Audit Report in Notion

Add Luke's analysis:

```python
audit_page = client.pages.create(
    parent={"database_id": "AUDITS_DB_ID"},
    properties={
        "Title": {"title": [{"text": {"content": f"Copy Audit: {', '.join(competitors)}"}}]},
        "Analysis Date": {"date": {"start": datetime.now().isoformat()}},
        "Competitors Audited": {"rich_text": [{"text": {"content": ', '.join(competitors)}}]},
        "Hook Patterns": {"rich_text": [{"text": {"content": str(luke_output['hook_analysis'])}}]},
        "Problem Agitation": {"rich_text": [{"text": {"content": str(luke_output['problem_agitation'])}}]},
        "Credibility Strategy": {"rich_text": [{"text": {"content": str(luke_output['credibility_strategy'])}}]},
        "Urgency Tactics": {"rich_text": [{"text": {"content": str(luke_output['urgency_tactics'])}}]},
        "Persuasion Gaps": {"rich_text": [{"text": {"content": str(luke_output['gaps'])}}]},
        "Recommendations": {"rich_text": [{"text": {"content": str(luke_output['recommendations'])}}]},
        "Risk Signals": {"rich_text": [{"text": {"content": str(luke_output['risk_signals'])}}]},
        "Status": {"select": {"name": "Audited"}}
    }
)

return audit_page['id']
```

### Step 5: Generate Copy Brief for Your Ads

Use Luke's recommendations to brief your copy team:

```
COPY BRIEF: Your Ads (Based on Competitor Analysis)

WINNING PATTERNS TO ADOPT:
1. [Pattern 1]: [How competitors use it]
   → Your approach: [How you could adapt it]

2. [Pattern 2]: [How competitors use it]
   → Your approach: [How you could adapt it]

3. [Pattern 3]: [How competitors use it]
   → Your approach: [How you could adapt it]

GAPS TO FILL (Opportunities):
1. [Gap 1]: [Why competitors avoid it]
   → Your test: [How you could own it]

2. [Gap 2]: [Why competitors avoid it]
   → Your test: [How you could own it]

RISKS TO AVOID:
- [Don't do this]: [Why competitors avoid it]
- [Don't do that]: [Why it backfires]

PERSUASION CHECKLIST FOR YOUR COPY:
□ Hook stops scroll (first 5 words matter)
□ Problem resonates with audience (they nod, not cringe)
□ Solution is clear (not vague)
□ Credibility is established (proof, social proof, authority)
□ Urgency is created (scarcity, time-bound, status)
□ CTA is crystal clear (one action, benefit-driven)

---

CREATIVE DIRECTION:
- Tone: [tone based on competitor analysis]
- Format: [video|static|carousel based on what's winning]
- Length: [based on performance data]
- Platform: [where it will run]
```

### Step 6: Send Copy Brief to Creative Team

```python
brief_email = f"""
Hi [Creative Team],

Luke (copywriting expert) has audited competitor ads + identified winning patterns.

Attached: Copy Brief for our next ad creative.

Key wins to adopt:
- {luke_output['recommendations'][0]}
- {luke_output['recommendations'][1]}
- {luke_output['recommendations'][2]}

Gaps to explore:
- {luke_output['gaps'][0]}
- {luke_output['gaps'][1]}

Persuasion checklist: Use template above to validate your copy.

Create 3 variations that test the recommendations above.

Timeline: [deadline]
Budget: [budget]

Questions → Ask Luke (copy expert) via /luke-iha-copy-review

---

Audit Report: [NOTION_LINK]
"""

send_email(
    to="creative_team@company.com",
    subject="Copy Brief: Competitor Analysis + Recommendations",
    body=brief_email
)
```

---

## Output Requirements

**Copy Audit Report**:
- ✓ Hook analysis for each ad (specific breakdown, not generic)
- ✓ Problem agitation strategy (how is pain amplified?)
- ✓ Credibility mechanisms (what builds trust?)
- ✓ Urgency tactics (what creates urgency?)
- ✓ Persuasion gaps (what's missing across all ads?)
- ✓ Recommendations (specific moves, not vague)
- ✓ Risk signals (patterns to avoid)

**Quality Gate**:
- ✓ All ads analyzed per persuasion checklist
- ✓ Gaps are non-obvious (not "bad copy")
- ✓ Recommendations are testable (not vague)
- ✓ Risk signals are grounded in competitor data
- ✓ Copy brief is actionable by creative team

**Next Workflows**:
- Creative team creates 3 ad variations using brief
- A/B test variations
- Iterate based on performance

---

## Quality Gate

**Red Flags** (fail if any):
- [ ] Hook analysis is generic ("has a hook")
- [ ] Gaps are obvious (e.g., "needs a CTA")
- [ ] Recommendations are vague ("write better copy")
- [ ] Risk signals don't apply to your industry
- [ ] Copy brief doesn't include persuasion checklist

**Validation Checklist**:
1. Pick one ad; read Luke's hook analysis; does it match your reading?
2. Check gaps; are they surprising? (If obvious, they're not useful)
3. Review recommendations; ask: "Could a junior copywriter execute this?" (if not, it's vague)
4. Scan risk signals; do they apply to your target audience?
5. Review copy brief; verify persuasion checklist is included

**Anti-Patterns**:
- Do NOT assume all competitors are doing it right (audit may reveal flaws)
- Do NOT skip the gap analysis (opportunities are often ignored by competitors)
- Do NOT recommend copying verbatim (adapt, don't clone)
- Do NOT ignore persuasion fundamentals (even long-running ads can miss basics)
- Do NOT publish without a copy review (even if your creative is great, Luke can improve it)

---

## Troubleshooting

**"Luke's analysis doesn't match my intuition"**
→ Luke is grounded in persuasion science; intuition can be biased. Test his recommendations.

**"Gaps feel like false opportunities"**
→ Competitors may have tested these gaps and abandoned them. Consider: why might this gap exist?

**"Recommendations are too risky"**
→ Balance innovation with caution. Recommend A/B testing (test Luke's move vs. safe control).

**"Copy brief feels disconnected from ads"**
→ Luke's insight may need translation. Work with creative team to map recommendations to concrete copy changes.

---

## Next Steps After Completion

1. **Validate** audit against source ads (spot-check 2 ads)
2. **Share** copy brief with creative team
3. **Creative team** creates 3 variations using brief
4. **A/B test** variations (run ads, measure performance)
5. **Iterate** based on results
6. **Re-run** audit quarterly as competitive landscape shifts

**Downstreams**: Creative execution, A/B testing, ad performance tracking

