---
description: Build the Silent Salesman about page (who/what/belong in 200 words)
---

# Sinem About Page

Build a Substack about page using Sinem Günel's "Silent Salesman" methodology.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Move 3)

2. Score intent: Score = 4.

3. Route: Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Your name and relevant background (2-3 sentences max)
   - What the publication delivers (topics, format, cadence)
   - Who the ideal reader is (identity, not demographics)
   - What the reader should eventually do (downstream action)

5. Build the Silent Salesman (under 200 words total):
   - **Section 1 — Trust** (40-60 words): Who you are + why this matters to you. Not a bio. Not credentials.
   - **Section 2 — Value** (60-80 words): What lands in their inbox, how often, what changes after 30 days.
   - **Section 3 — Belonging** (40-60 words): Describe ideal reader so they think "this is me."

6. Quality gate: Under 200 words. Reader recognition in first sentence. No jargon.

7. Finalize:
```bash
python3 execution/chain_runner.py finalize "About page — [name]" \
    --expert sinem-gunel --skill substack-business-architecture \
    --workflow sinem-about-page --type Copy \
    --intent 8 --expert-score 8 --adversarial 7 \
    --notes "Silent Salesman: who/what/belong in 200 words"
```
