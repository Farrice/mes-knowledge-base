---
description: Extract 50 standalone notes from a single long-form post
---

# Sinem 50-Notes Extraction

Take any published long-form post and extract 50 potential notes from it. Every strong sentence, reframe, insight, or example becomes its own standalone note. This is the content multiplier that makes daily Notes posting sustainable without daily creation labor.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Move 1: The 50-Notes Extraction)

2. Score intent (Chain Step 1): Score = 4 (deliverable: 50 note drafts from 1 post, audience: Substack discovery feed, context: content atomization, end state: 50 standalone notes ready for scheduling).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - The full text of the long-form post to extract from
   - Target reader profile (who should these notes attract?)
   - Any notes from this post that have already been published

5. Execute the 50-Notes Extraction:
   a. **Pass 1 — Sentence Mining**: Read every sentence. Flag any that could stand alone as a reframe, contrarian take, or insight. Target: 20+ candidates.
   b. **Pass 2 — Story Seed Mining**: Identify every specific moment, example, anecdote, or case study. Each one is a note seed. Target: 10+ candidates.
   c. **Pass 3 — Question Mining**: Find every implicit question the post raises. Turn each into a reader-engagement note. Target: 5+ candidates.
   d. **Pass 4 — Contrarian Mining**: Identify every point where the post challenges conventional wisdom. Sharpen each into a standalone provocation. Target: 5+ candidates.
   e. **Pass 5 — Framework Mining**: Extract any step-by-step processes and convert to single-image or list notes. Target: 5+ candidates.
   f. **Pass 6 — Expansion Mining**: Find compressed ideas (1 sentence in the post that deserves 1 paragraph as a note). Expand into full notes. Target: 5+ candidates.

6. For each extracted note, apply the 5-part arc:
   - Specific moment opener (not a tip)
   - Insight layer
   - Action or implication
   - Result or proof
   - Reader turn

7. Tier the 50 notes:
   - **Tier 1 (10 notes)**: Highest standalone impact — schedule for peak engagement times
   - **Tier 2 (20 notes)**: Strong but needs context — schedule for regular cadence
   - **Tier 3 (20 notes)**: Good but derivative — use as engagement responses or remix later

8. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "50-notes extraction — [post title]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-50-notes-extract \
    --type Content \
    --intent 8 --expert-score 9 --adversarial 7 \
    --notes "6-pass extraction system: sentences, stories, questions, contrarians, frameworks, expansions"
```
