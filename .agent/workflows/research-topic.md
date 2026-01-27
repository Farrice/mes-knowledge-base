---
description: Deep research on any topic with organized, actionable deliverable
---

# /research-topic

Use this workflow for comprehensive research on any topic, combining live internet data with organized synthesis.

## Usage

```
/research-topic [topic] --depth [quick|standard|deep] --output [summary|report|brief]
```

**Examples:**
- `/research-topic "TikTok Shop seller requirements 2024" --depth quick --output summary`
- `/research-topic "AI automation agencies market size and competitors" --depth deep --output report`
- `/research-topic "Augusta Rule tax strategy requirements" --depth standard --output brief`

**Defaults:** `--depth standard --output summary`

---

## Bounded Browser Controls

> [!IMPORTANT]
> **Hard Tab Limits by Depth Level** (NEVER exceed):
> - Quick: **3 tabs max**
> - Standard: **5 tabs max**  
> - Deep: **8 tabs max**

**Rules:**
- Each tab must have a **stated purpose** before opening
- No speculative browsing—only targeted source retrieval
- Prioritize sources BEFORE opening any tabs

---

## Quality Rubric (RARA)

Evaluate every source against this 4-point rubric:

| Criterion | Question | Threshold |
|-----------|----------|-----------|
| **R**elevance | Does source directly address the research question? | Must be >70% on-topic |
| **A**ccuracy | Can claims be cross-verified? | 2+ sources agree |
| **R**ecency | Is information current? | <1 year for fast-moving topics |
| **A**uthority | Is source credible? | Official docs, industry leaders, .gov/.edu preferred |

---

## Stopping Criteria

> [!CAUTION]
> **Research MUST STOP when ANY of these conditions are met:**

1. **Tab limit reached** for the depth level
2. **Saturation detected**: 3+ sources saying the same thing with no new information
3. **Diminishing returns**: Last source added <10% new information
4. **Time limit hit**: Quick=3min, Standard=8min, Deep=20min
5. **Core questions answered**: All key questions from scoping have answers

---

## Workflow Steps

### 1. Clarify Research Scope
- Confirm the topic and any specific angles the user wants covered
- **Define 3-5 specific questions** that constitute "complete" research
- Set the depth level and tab budget

### 2. Initial Web Search
// turbo
- Run 3-5 targeted searches to map the information landscape
- Identify: authoritative sources, recent updates, key players, data sources
- **Create prioritized source list** before opening any browser tabs
- Note gaps that need deeper investigation

### 3. Deep Source Mining (Bounded)
// turbo
- Read sources in priority order, respecting tab limits:
  - `--depth quick`: 3 tabs max
  - `--depth standard`: 5 tabs max
  - `--depth deep`: 8 tabs max
- **Track saturation**: Stop if 3+ sources repeat the same information
- Extract: facts, data points, quotes, frameworks, dates

### 4. Cross-Reference & Validate
- Compare information across sources for accuracy
- Apply **RARA rubric** to each source
- Flag any contradictions or outdated information
- Prioritize recent/authoritative sources over older/weaker ones

### 5. Pre-Synthesis Saturation Check
Before writing any output, explicitly verify:
- [ ] All scoped questions have answers
- [ ] No new information emerging from recent sources
- [ ] Gaps identified for follow-up (if any)

**If gaps remain**: Request permission for targeted follow-up (max 2 additional tabs)

### 6. Synthesize Findings
Based on `--output` format:

**Summary (default):**
- 300-500 word executive summary
- Key facts in bullet points
- Top 3-5 actionable insights
- Source links for verification
- **RARA assessment** (overall quality score)

**Report:**
- Full structured report (1000-2000 words)
- Sections: Overview, Key Findings, Data/Evidence, Implications, Recommendations
- Embedded source citations
- **Methodology note**: tabs used, stopping criterion triggered
- Save as artifact in brain directory

**Brief:**
- One-page decision brief
- Situation → Findings → Recommendation format
- Designed for quick decision-making

### 7. Identify Knowledge Gaps
- Note what COULDN'T be found or verified
- Suggest follow-up research if needed
- Offer to go deeper on any specific area

---

## Research Depth Guide

| Depth | Time Limit | Tab Limit | Sources | Best For |
|-------|------------|-----------|---------|----------|
| Quick | 3 min | 3 | 3-5 | Simple facts, quick answers |
| Standard | 8 min | 5 | 5-8 | Business decisions, market overviews |
| Deep | 20 min | 8 | 10-15+ | Strategy, competitive analysis, complex topics |

---

## Output Locations

- **Summaries**: Delivered directly in conversation
- **Reports**: Saved to `/Users/farricecain/.gemini/antigravity/brain/[conversation-id]/`
- **Briefs**: Delivered in conversation, optionally saved

---

## Pro Tips

- Add specific angles: `/research-topic "X" focusing on pricing and market size`
- Request comparisons: `/research-topic "X vs Y for [use case]"`
- Time-bound: `/research-topic "X" focusing on 2024 changes`
- Combine with skills: After research, use `/deploy-skill` to act on findings
