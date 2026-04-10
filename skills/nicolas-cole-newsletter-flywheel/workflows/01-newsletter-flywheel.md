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

### Stage 2b: Serial Investment Architecture (run for Edition 2+)

Before producing variants, map the inter-edition investment mechanics. Skip for Edition 1.

**For each edition, answer these 5 questions:**

1. **Conceptual Deposit**: What term, framework, or lens from the PREVIOUS edition can be reused WITHOUT re-explaining? (Returning readers get insider recognition; new readers feel late to the story.)
2. **Belief Escalation**: What belief did the previous edition install? What is the NEXT belief step that only makes sense if the reader took the first one? (Each edition moves the reader one rung further from their entry worldview.)
3. **Identity Ratchet**: What ACTION did the previous edition invite (reply, forward, use a prompt, try a framework)? How does THIS edition acknowledge that action to deepen the reader's self-identification with the newsletter tribe? (Unsubscribing should feel like identity abandonment, not inbox cleanup.)
4. **Callback Yield**: What specific metaphor, example, or moment from a previous edition can be REFERENCED (not repeated) in a way that rewards returning readers? ("Last week I showed you X. This week, the other side of that coin.")
5. **Incomplete Transfer**: What did the previous edition's tangible asset produce that is USEFUL alone but COMPOUNDS with this edition's asset? (The prompt pack from #5 generates a map; the prompt pack from #6 shows how to read that map. #5 becomes retroactively more valuable.)

**The Serial Investment Test**: Would a subscriber who read the previous edition find THIS edition meaningfully more valuable than someone reading cold? If no, the investment mechanics are decorative, not structural. Redesign.

### Stage 3: Produce 3 Variants
For each of the 3 angles, produce a complete newsletter post:
1. **Subject line** — hook using the tangible asset as the draw; for Edition 2+, reference the conceptual deposit from the previous edition
2. **Opening** — The "book that never ends" frame: why this edition matters, what the reader GETS. For Edition 2+, include at least one callback yield and one identity ratchet acknowledgment.
3. **Body** — The tangible asset itself (prompt, template, framework, walkthrough, etc.). Design the asset to compound with the previous edition's asset (Incomplete Transfer).
4. **Commentary layer** — Expert perspective on the asset: why it works, what to watch for, what most people get wrong. Weave in the belief escalation — move the reader one step further.
5. **Close** — Don't just tease the next asset. Plant the Incomplete Transfer: name what THIS edition's asset produces, then hint that the NEXT edition reveals what to DO with that output. The reader should feel they're holding half a key.

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
