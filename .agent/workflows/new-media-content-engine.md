---
description: "Master copy engine with oral/written culture awareness — produces platform-native content using cultural physics to match proof types, voice register, and format to each medium"
---

# /new-media-content-engine — Platform-Aware Copy Production

The proof copy engine upgraded with oral/written culture physics. Instead of producing "content" and adapting it, this engine produces culturally native copy for each medium. The same message but expressed through different cultural operating systems.

## Usage

```
/new-media-content-engine --topic "[topic]" --platforms "X, LinkedIn, YouTube, Substack"
/new-media-content-engine --topic "Why most AI tools are solving the wrong problem" --platforms "all"
```

## Steps

### 1. Load Context
Read these files:
1. `skills/luke-iha-proof-copy/SKILL.md`
2. `skills/luke-iha-proof-copy/genius.md`
3. `skills/andreessen-horowitz-new-media/genius.md` → Oral/Written Culture Matrix + Platform-Native Obsession

### 2. Establish the Written-Culture Canonical Piece
**This is the anchor everything else derives from.**

- Write the FULL argument in long-form (Substack essay or YouTube script)
- Full proof ladder deployment (all available proof types)
- This is the written-culture reference — depth, logic, evidence
- Load `skills/luke-iha-proof-copy/workflows/proof-copy-engine.md` for the master copy workflow

### 3. Oral-Culture Extraction (NOT Reformatting)

For each oral platform, create CULTURALLY NATIVE content:

**X / Twitter Thread**
- Strip to the single most provocative claim
- Lead with identity-triggering hook (Luke Iha vicious hook methodology)
- Burst energy: short sentences, emotional stakes, campfire urgency
- Maximum 7 tweets in thread
- Link to canonical long-form for full context (context-length defense)

**YouTube Shorts / TikTok / Reels**
- One "whoa" moment from the full argument
- 30-60 seconds: single point, maximum visual impact
- Script for spoken delivery: conversational, high energy, direct-to-camera
- NO slides or text walls — oral culture means INTERPERSONAL

**Instagram Carousel**
- 8-10 slides, each a self-contained visual argument
- Oral-culture energy: provocative headlines, minimal text per slide
- Last slide = CTA to long-form canonical piece

### 4. Hybrid-Culture Production

**LinkedIn Post**
- Load `skills/lara-acosta/SKILL.md` for LinkedIn-native formatting
- Hybrid mode: personal story opening → professional insight → proof → CTA
- 150-250 words, formatted for scroll-stop
- Proof type: personal experience + customer result (the two that work best in hybrid)

### 5. Written-Culture Depth Pieces

**Substack / Blog**
- The canonical reference (if not already produced in Step 2)
- Full proof ladder, evidence-based, analytical rigor
- 1,000-2,500 words
- This is what people bookmark and send to colleagues

**Email Newsletter Edition**
- Load `skills/cardinal-mason/SKILL.md` for email best practices
- Bridge format: enough depth to build trust, CTA to full piece
- Proof-braid technique: no naked claims

### 6. Voice Consistency Check
Across all platforms:
- Same persona, different register
- Check: would the audience recognize this as the same person across platforms?
- Oral versions feel conversational and energetic
- Written versions feel rigorous and authoritative
- Hybrid versions feel personally professional

### 7. Quality Gate
All must pass:
- [ ] Canonical written piece exists and anchors everything
- [ ] No content is "reformatted" — each is natively designed
- [ ] Proof types match culture mode (demonstration → oral, research → written)
- [ ] Voice is consistent across platforms (same person, different register)
- [ ] Every oral piece links to or references the canonical written piece
- [ ] Hooks are scored using Luke Iha methodology (A-tier or rewrite)

### 8. Output
Save to `.tmp/new-media-content-engine/[topic-slug]-[date]/`
- `canonical-longform.md`
- `x-thread.md`
- `linkedin-post.md`
- `shorts-scripts.md`
- `email-edition.md`
- `carousel-outline.md`

### 9. Finalize
```bash
python3 execution/chain_runner.py finalize "New Media Content Engine" \
    --expert "luke-iha" \
    --skill "luke-iha-proof-copy" \
    --workflow "new-media-content-engine" \
    --type Content \
    --intent 9 --expert-score 9 --adversarial 8 \
    --notes "Proof copy engine with oral/written culture integration"
```
