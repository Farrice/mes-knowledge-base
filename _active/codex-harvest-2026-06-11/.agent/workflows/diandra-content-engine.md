---
description: Daily content production engine
---

# `/diandra-content-engine` — The Daily Content Production Line

Takes any topic and bucket assignment → enriches with live research → writes body-first → produces a publish-ready LinkedIn post with hook candidates, format variations, and cross-platform adaptations.

**The daily workhorse. Run this every time you sit down to write.**

## When to Use
- You have a topic and need a finished post
- You want the body-first method executed properly (not starting with hook)
- You need multiple format variations from one topic
- You want cross-platform output (LinkedIn + X + Substack)

## Usage

```
/diandra-content-engine [topic] --bucket [growth|authority|conversion|personal]
/diandra-content-engine "Why most coaches overcomplicate their tech stack" --bucket authority
/diandra-content-engine --today   (auto-suggests based on calendar gaps)
```

---

## Phase 1: Intent Lock & Calendar Check

**Actor**: Orchestrator

### Bucket Declaration

Lock the bucket BEFORE writing — this determines hook style, structure, and CTA:

| Bucket | Job | Optimize For | CTA Style |
|--------|-----|-------------|-----------|
| **Growth** (35%) | Reach new people | Shares, comments, profile clicks | Discussion invite |
| **Authority** (35%) | Prove expertise | Saves, bookmarks, "I learned" comments | Save/bookmark ask |
| **Conversion** (20%) | Move toward buying | DMs, link clicks, inbound | Keyword DM trigger |
| **Personal** (10%) | Deepen connection | Emotional comments, connection requests | Shared experience ask |

### If `--today` mode:

1. Check if a content calendar exists at `_active/content/calendar.md` or `.tmp/diandra-content-engine/calendar.md`
2. Analyze bucket distribution of recent posts
3. Recommend which bucket is underrepresented
4. Suggest 3 topic ideas for that bucket using user's content north stars

```markdown
## Today's Recommendation
**Bucket gap**: You haven't posted [authority] content in [X] days.
**Suggested topics**:
1. [topic idea — source: recent client call / news / internal doc]
2. [topic idea]
3. [topic idea]

**Pick one, or give me your own topic.**
```

**WAIT FOR USER SELECTION.**

---

## Phase 2: Topic Enrichment (RESEARCH)

**Actor**: Orchestrator + research tools

> Body-first writing works best when you have SPECIFIC material to work with.

### Execute 2-3 targeted queries:

| Query | Purpose |
|-------|---------|
| `"[topic] data statistics 2026"` | Fresh numbers to ground claims |
| `"[topic] reddit linkedin complaints"` | Real verbatim pain points |
| `"[topic] expert quote thought leader"` | Authoritative quotes to cite |

Use `search_web` + `read_url_content` on top results.

### Produce Enrichment Brief:

Save to `.tmp/diandra-content-engine/enrichment-[slug].md`:

```markdown
## Enrichment Brief: [Topic]
**Bucket**: [type]

### Data Points
- [Specific stat with source]
- [Specific number with context]

### Real Quotes
- "[Verbatim from Reddit/LinkedIn]" — source
- "[Expert quote]" — source

### Counter-Arguments
- What the skeptic would say: [argument]
- Your response: [rebuttal with evidence]
```

---

## Phase 3: Body-First Production

**Actor**: Orchestrator (single-agent — this is the core writing step)

### Load Diandra's writing system:
// turbo
Read:
1. `skills/diandra-escobar-linkedin-growth/genius.md` — Pattern 6 (Body-First Writing), Pattern 12 (North Star Alignment)
2. `skills/diandra-escobar-linkedin-growth/workflows/09-linkedin-writing-engine.md`

### Step 1: Write the Body

Write 150-300 words of substance, bucket-appropriate:
- **Growth**: Analyze an entity. Position + evidence + implication.
- **Authority**: Teach something. Framework, list, step-by-step, insight + example.
- **Conversion**: Show a result. Before → method → after. Include specific numbers.
- **Personal**: Tell a story. Scene → conflict → resolution → lesson.

**Rules**:
- Use specific numbers, names, examples from the enrichment brief
- Every paragraph earns its place — delete anything that doesn't add new information
- Include at least one concrete example from real experience or research
- Write in the creator's natural voice (check genius.md Voice DNA)

### Step 2: Mine for 5 Hook Candidates

Read the body and extract the 5 strongest lines:

| # | Hook | Type | Strength |
|---|------|------|----------|
| 1 | [most surprising line] | Data/Claim | ⭐⭐⭐⭐⭐ |
| 2 | [most provocative line] | Contrarian | ⭐⭐⭐⭐ |
| 3 | [most specific line] | Detail | ⭐⭐⭐⭐ |
| 4 | [most emotional line] | Scene | ⭐⭐⭐ |
| 5 | [most relatable line] | Recognition | ⭐⭐⭐ |

### Step 3: Assemble the Post

- Hook (selected #1 candidate) + body + CTA (matched to bucket)
- Recommend the best hook with reasoning

### Step 4: Visual Recommendation

| Bucket | Visual Type |
|--------|-------------|
| Growth | Screenshot / one-pager / framework diagram |
| Authority | Step-by-step diagram / data visualization |
| Conversion | Before/after / result screenshot |
| Personal | Photo / candid moment |

1-sentence visual brief for designer or Pencil.

---

## Phase 4: Multi-Variant Assembly (3 Formats)

**Actor**: 3 parallel sub-agents via Task tool

Take the approved body content and reformat into 3 LinkedIn-native formats:

### Sub-Agent 1: Text Post (Default)
```
Using the body content and selected hook, produce a clean text post:
- 150-250 words
- Short paragraphs (1-2 lines per paragraph)
- Heavy white space for mobile readability
- Hook in first 2 lines (must survive "See more" truncation)
- CTA matched to bucket

Write to: .tmp/diandra-content-engine/format-text.md
```

### Sub-Agent 2: Carousel Outline
```
Using the body content, produce an 8-12 slide carousel:
- Slide 1: Hook (scroll-stop)
- Slides 2-10: One idea per slide, ≤40 words each
- Final slide: CTA + handle
- Visual direction notes per slide
- Swipe-forward motivation between slides

Write to: .tmp/diandra-content-engine/format-carousel.md
```

### Sub-Agent 3: Image + Text Combo
```
Using the body content, produce an image-based post:
- Short text (75-150 words)
- Detailed image/infographic brief (what should the visual contain?)
- The image carries the value; the text contextualizes
- CTA in text, value in image

Write to: .tmp/diandra-content-engine/format-image.md
```

---

## Phase 5: Cross-Platform Adaptation

**Actor**: Orchestrator

From the approved LinkedIn post, produce platform-native adaptations:

### X/Twitter Thread
- Compress to 5-7 tweets
- Tweet 1 = hook (must work standalone)
- Each tweet = one atomic idea
- Thread structure: setup → value → CTA

### Substack/Newsletter Section
- Expand to 400-600 words
- Add personal narrative framing
- Include the "deeper dive" that wouldn't fit LinkedIn
- CTA: subscribe or reply

### Universal Text (platform-agnostic)
- Clean, unformatted version
- No platform-specific CTAs
- Usable in email, Slack, community posts

---

## Phase 6: Quality Gate + Deliver

### Quality Checks (per genius.md):

| Criterion | Check |
|-----------|-------|
| Body-First | Hook genuinely mined from body? |
| Bucket-CTA Match | CTA serves declared bucket? |
| Specificity | ≥2 specific numbers/names/examples? |
| Voice Check | Sounds like creator, not "AI LinkedIn post"? |
| North Star Alignment | Reinforces ≥1 content north star? |
| Visual Included | Visual recommendation attached? |
| Banned Word Scan | Clean against Voice DNA banned phrases? |
| Anti-Pattern | Not a summary, not preachy, not generic? |

### Deliver

```markdown
# ✍️ CONTENT ENGINE: [Topic]

**Bucket**: [type] | **Research**: 🟢 GROUNDED
**Date**: [date]

---

## THE POST (Recommended Format: [text/carousel/image])

[Full post — hook + body + CTA]

---

## HOOK CANDIDATES (5)
| # | Hook | Type | Recommended |
|---|------|------|-------------|
| 1 | [hook] | [type] | ⭐ Primary |
| 2-5 | ... |

---

## FORMAT VARIATIONS

### Text Post
[complete post]

### Carousel (8-12 slides)
[slide-by-slide copy]

### Image + Text
[text + image brief]

---

## CROSS-PLATFORM

### X Thread (5-7 tweets)
[thread]

### Substack Section
[expanded version]

### Universal Text
[platform-agnostic version]

---

## VISUAL BRIEF
[1-sentence image recommendation]

## NORTH STAR ALIGNMENT
[Which north stars this reinforces]

## PROVENANCE
Research: [query count] queries | 🟢 GROUNDED
Skills: Diandra Escobar genius.md + workflow 09
```

Save to `.tmp/diandra-content-engine/post-[slug]-[date].md`.

### Next Steps

```
> **Ready to post?** Copy the variation you like best.
>
> **Want more?**
> - Run `/diandra-content-engine` with a different topic/bucket
> - Run `/diandra-growth-sprint` for a growth post using a specific entity
> - Run `/diandra-steal-and-remix` to find new content inspiration
```

---

## Output Files

```
.tmp/diandra-content-engine/
  enrichment-[slug].md
  format-text.md
  format-carousel.md
  format-image.md
  post-[slug]-[date].md   (assembled final package)
```
