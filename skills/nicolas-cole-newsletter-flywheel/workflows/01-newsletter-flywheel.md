---
description: End-to-end newsletter flywheel — raw idea to research to 3-variant post to publish-ready output
---

# Newsletter Flywheel — Full Pipeline

The complete flywheel from raw concept to publish-ready newsletter post with 3 variants.

## Prerequisites
- Load `nicolas-cole-newsletter-flywheel` skill (SKILL.md + genius.md)
- If first run, validate concept with `/book-never-ends` first

## Pipeline

### Stage 1: Concept Lock (skip if already validated)
1. Run the Two Rules Gate on the newsletter concept:
   - Rule 1: Is this a book that never ends? (Y/N + why)
   - Rule 2: What is the tangible, repeatable asset? (Name the noun)
2. If either fails → stop and run `/tangible-faucet` first
3. Confirm the tangible asset passes the Wine Club Test: "It's like a _____ club but for _____"

### Stage 2: Research & Ideation
1. Take the user's raw idea/topic for this edition
2. Research via Perplexity (if budget allows) or web search:
   - What's trending in this topic space right now?
   - What pain points are underserved in the audience's world?
   - What tangible assets exist that could be adapted/improved?
3. Cross-pattern: trending topic × audience pain × tangible asset format
4. Output: **3 distinct angles** on the same topic, each producing the tangible asset differently

### Stage 3: Produce 3 Variants
For each of the 3 angles, produce a complete newsletter post:
1. **Subject line** — hook using the tangible asset as the draw
2. **Opening** — The "book that never ends" frame: why this edition matters, what the reader GETS
3. **Body** — The tangible asset itself (prompt, template, framework, walkthrough, etc.)
4. **Commentary layer** — Expert perspective on the asset: why it works, what to watch for, what most people get wrong
5. **Close** — Tease next edition's tangible asset (keep the faucet running)

### Stage 4: Editor Pick
Present all 3 variants to the user with:
- Variant labels (e.g., "The Tactical," "The Story-Led," "The Contrarian")
- 1-sentence pitch for each
- Recommendation on which is strongest and why

### Stage 5: Polish & Publish-Ready
After user selects a variant:
1. Apply `nicolas-cole-sentence-craft` for sentence-level optimization
2. Format for SubStack (headers, pull quotes, tangible asset highlighted)
3. Draft social teaser for LinkedIn (1-liner + link preview)
4. Output final post ready for copy-paste to SubStack

## Chain Finalization
```bash
python3 execution/chain_runner.py finalize "[Newsletter post title]" \
    --expert nicolas-cole --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-flywheel --type Content \
    --intent 9 --expert-score 8 --adversarial 7 \
    --notes "Full flywheel execution"
```
