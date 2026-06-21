---
description: Daily content production engine
---

# `/diandra-content-engine` — The Daily Content Production Line

Takes a **finished body** (written separately, in one coherent voice) → mines hooks + locks bucket/format/CTA → produces hook candidates, format variations, and cross-platform adaptations. **It does not write body copy** (that lives in a separate, single-author engine).

**The daily workhorse. Run this every time you sit down to write.**

> **Scope note (2026-06-20 lesson):** Diandra is a **hooks + format** engine, separate and unwired from body copy. Don't use her to write the body, and don't stitch her with narrative experts into one auto-flow (the "Sandwich" produced disjointed copy that scored *worse* than the original single-author draft). Hooks in isolation → `/diandra-hook-architect`. Body copy → a separate single-author narrative engine.

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

Route research through the unified engine — `python3 execution/research.py "<query>" --depth quick` (Gemini-first → Perplexity → Tavily bedrock floor, honest Research Receipt, $0 on failure). Use `--depth standard` for higher-stakes posts; for `deep`/`max` the swarm is `.agent/workflows/deep-research-swarm.workflow.js`.

**GROUNDED gate**: The 🟢 GROUNDED label below is earned, not assumed. Mark 🟢 GROUNDED only if `research.py` returns a Research Receipt with ≥2 real source URLs. If research returned $0/empty or you wrote from priors, mark 🟡 UNGROUNDED (modeled) instead — never claim grounding the receipt doesn't support.

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

## Phase 3: Hook + Format Engine (Diandra's actual genius — NOT body copy)

> **⚠️ Scope (2026-06-20 lesson):** This engine does **NOT** write body copy. Diandra's genius is hooks + format. Using her to write the body produces flat, informational prose; auto-composing her with narrative experts in one flow ("the Sandwich") stitched together disjointed, unflowing copy that scored *worse* than the original single-author draft. Bring a FINISHED body (written separately, by one coherent author) and Diandra tops it with a hook + format. Keep the body engine and hook engine **separate and unwired**.

**Actor**: Orchestrator (Diandra hook/format layer only)

### Step 0 — Bring the body (written separately, by ONE coherent author)

The body already exists before this runs, written in a single voice: your own draft, the `/quality-content` single-author body, or one narrative engine (`writers-room`, `@mitch-albom`, `@shaan-puri`, `@wright-thompson`, or `/depth-social`). **Do not generate or rewrite the body here, and never stitch multiple experts' fragments into one body** — that synthesis is what destroyed voice coherence (the disjointed 4/10). One mind writes the body.

### Step 1 — Load Diandra's hook system

// turbo
Read `skills/diandra-escobar-linkedin-growth/genius.md` — Pattern 6 (body-first hook mining), Pattern 20 (the gap is the engine), Pattern 21 (the 5-format hook system), the no-questions-in-hooks rule, the mobile-width model. (For hooks in pure isolation, the standalone tool is `/diandra-hook-architect`.)

### Step 2 — Mine 5 hooks from the provided body

The best hooks already exist inside the finished body. Pull the 5 strongest lines; no question hooks (reframe any question as reported dialogue); apply the 5-format system + width ceilings. Recommend the top hook with reasoning.

| # | Hook | Format | Type | Strength |
|---|------|--------|------|----------|
| 1 | [most surprising / highest-stakes line] | Punchy+Context / Dense / Bomb / Stacked | Data/Claim | ⭐⭐⭐⭐⭐ |
| 2 | [most provocative line] | ... | Contrarian | ⭐⭐⭐⭐ |
| 3-5 | ... | ... | Detail / Scene / Recognition | |

### Step 3 — Assemble + Visual

- Chosen hook placed above the **UNCHANGED** body + bucket-matched CTA (no cheap question signoff)
- 🛡️ **Hard rule: Diandra tops the body, never rewrites it.** She may adjust only the single seam line where hook meets body.
- 1-sentence visual brief for designer or Pencil:

| Bucket | Visual Type |
|--------|-------------|
| Growth | Screenshot / one-pager / framework diagram |
| Authority | Step-by-step diagram / data visualization |
| Conversion | Before/after / result screenshot |
| Personal | Photo / candid moment |

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

**Bucket**: [type] | **Research**: [🟢 GROUNDED if Research Receipt has ≥2 source URLs · else 🟡 UNGROUNDED (modeled)]
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
Research: [query count] queries via execution/research.py | [🟢 GROUNDED — N source URLs from Research Receipt · else 🟡 UNGROUNDED (modeled)]
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
