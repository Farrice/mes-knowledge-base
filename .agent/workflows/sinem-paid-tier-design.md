---
description: Build asset-based paid tier that feels like a product, not a tip jar
---

# Sinem Paid Tier Design

Design a paid subscription tier using Sinem Günel's Asset-Based Paywall methodology. The paid tier should feel like purchasing a product — not donating to a creator. Every subscriber should feel the price is justified by a single asset alone.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Move 4: Asset-Based Paywall)

2. Score intent (Chain Step 1): Score = 4 (deliverable: paid tier architecture with assets, audience: publication owner, context: Substack paid tier, end state: complete paid tier spec with pricing and asset vault).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - What expertise/knowledge do you have that could be packaged as assets?
   - Do you have any existing templates, frameworks, checklists, or courses?
   - What does your ideal reader struggle with most? (3 specific problems)
   - Current pricing (if existing paid tier) or proposed price point
   - Monthly vs. annual pricing structure preferences

5. Design the asset vault:
   a. **Core Assets** (what makes someone subscribe):
      - Template library (at least 3 templates solving specific problems)
      - Strategy framework or playbook (a "system" they can follow)
      - Printable reference guide (something they'll use weekly)
   b. **Ongoing Assets** (what keeps someone subscribed):
      - Monthly deep-dives (not "bonus posts" — actionable guides with worksheets)
      - Live Q&A or workshop access (if capacity allows)
      - Community access or private chat (if using Substack Chat)
   c. **Exclusive Assets** (what drives annual plan conversion):
      - Annual-only bonus pack
      - Early access to new products
      - Founding member perks (if early stage)

6. Apply the "Covers the Cost" test:
   - Pick ANY single asset from the vault
   - Would a reasonable person pay the subscription price for that one asset alone?
   - If NO: the vault is too thin. Add higher-value assets.
   - If YES: the tier passes. Each additional asset becomes bonus value.

7. Pricing architecture:
   - Monthly price: Based on asset value (typically $5-$15 for individual creators)
   - Annual price: 15-20% discount to make annual the obvious choice
   - Position annual as default (per Sinem's Move 6)
   - Welcome sequence: immediate value delivery + guided tour of the vault

8. Cross-expert stacking (optional):
   - Stack with Tom Noske (`/promise-payoff`) for trust-transaction framing
   - Stack with Nicolas Cole (`/offer-stack`) for irresistible offer engineering

9. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Paid tier design — [publication name]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-paid-tier-design \
    --type Strategy \
    --intent 8 --expert-score 8 --adversarial 8 \
    --notes "Asset-based paywall with Covers the Cost test and annual-first pricing"
```
