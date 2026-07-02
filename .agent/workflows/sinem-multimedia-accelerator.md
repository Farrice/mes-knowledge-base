---
description: Deploy audio/video trust acceleration strategy (50% growth premium)
---

# Sinem Multimedia Accelerator

Deploy Sinem's multimedia trust acceleration strategy. Creators using audio/video grew 50% faster. Substack's Recording Studio eliminates tooling barriers — pre-recorded conversations with auto-generated clips and thumbnails.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Hidden Knowledge #7)

2. Score intent: Score = 4.

3. Route: Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Current content format (text-only, audio, video, or mixed)
   - Comfort level with audio/video (beginner, intermediate, advanced)
   - Available tools (Substack Recording Studio, external podcast, video setup)
   - Weekly time budget for content creation

5. Design the multimedia integration:

   **Tier 1 — Audio layer** (lowest friction):
   - Add audio readings to existing text posts via Recording Studio
   - Record 5-10 min companion audio with behind-the-scenes context
   - Auto-generate clips for Notes promotion

   **Tier 2 — Video layer** (medium friction):
   - Pre-recorded conversations with collaborators
   - Short video notes (1-2 min) for discovery feed
   - Use Substack's auto-generated thumbnails

   **Tier 3 — Live layer** (highest engagement):
   - Weekly or monthly live sessions for paid subscribers
   - Live Q&A events during Bestseller campaigns
   - Recorded and archived as paid-tier assets

6. Deployment plan:
   - Week 1-2: Add audio to next 3 posts (Tier 1)
   - Week 3-4: Record first video note or conversation (Tier 2)
   - Month 2+: Launch first live session for paid members (Tier 3)

7. Finalize:
```bash
python3 execution/chain_runner.py finalize "Multimedia strategy — [publication]" \
    --expert sinem-gunel --skill substack-business-architecture \
    --workflow sinem-multimedia-accelerator --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "3-tier multimedia: audio → video → live with 50% growth premium"
```
