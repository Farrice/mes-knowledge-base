---
description: Subscriber acquisition strategy for newsletters
---

# Newsletter Growth Audit

Design how subscribers find your newsletter using multi-expert stacking.

## Steps

1. Load context (Chain Step 4):
   - Read `skills/nicolas-cole-newsletter-flywheel/genius.md`
   - Read `skills/nicolas-cole-newsletter-flywheel/workflows/17-newsletter-growth-audit.md`
   - If LinkedIn-focused: Read `skills/lara-acosta-linkedin-mastery/SKILL.md`
   - If hook engineering needed: Read `skills/luke-iha-proof-ladder/SKILL.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: growth strategy + 90-day roadmap, audience: self, context: subscriber acquisition, end state: channel-specific tactics with milestones).

3. Route (Chain Step 3): Nicolas Cole (tangible asset positioning) + Lara Acosta (LinkedIn funnel) + Luke Iha (hook architecture) + Kallaway (content psychology) + Kieran Flanagan (cross-platform atomization).

4. Gather input: Newsletter name, tangible asset, current subscriber count, active social platforms, existing content assets, budget for paid acquisition.

5. Execute — Acquisition audit, tangible-asset-as-hook positioning, channel-specific strategies (LinkedIn, X, YouTube, SubStack organic, referrals), hook engineering for signup CTAs, 90-day growth roadmap.

6. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Newsletter growth audit — [newsletter name]" \
    --expert nicolas-cole \
    --skill nicolas-cole-newsletter-flywheel \
    --workflow newsletter-growth-audit \
    --type Strategy \
    --intent [1-10] --expert-score [1-10] --adversarial [1-10] \
    --notes "Multi-expert stack: Cole + Lara + Luke + Kallaway + Kieran"
```
