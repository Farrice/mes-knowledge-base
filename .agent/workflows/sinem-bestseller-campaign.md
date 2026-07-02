---
description: Run a named promotional campaign sprint for paid subscriber conversion
---

# Sinem Bestseller Campaign

Run a full Bestseller Badge campaign sprint using Sinem Günel's "Substack September" model. This is NOT passive growth — it's a product-launch-style event designed to drive step-function jumps in paid subscribers.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Exemplar 3: Substack September)

2. Score intent (Chain Step 1): Score = 5 (deliverable: complete campaign plan with assets and timeline, audience: existing free subscribers + discovery feed, context: paid subscriber conversion sprint, end state: named campaign ready to execute).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Current subscriber count (free and paid)
   - Target milestone: 100 paid (white badge), 1,000 paid (gold badge), or custom
   - Campaign duration preference (7, 14, or 30 days)
   - What exclusive asset(s) can you create for this campaign?
   - Available channels for promotion (Notes, email, LinkedIn, Twitter, etc.)

5. Build the campaign architecture:

   a. **Name the campaign**: Every campaign needs a branded name. Examples:
      - "[Publication Name] September" / "Summer Sprint" / "Founding 100"
      - The name creates urgency, identity, and shareability

   b. **Set the dates**: Fixed start and end. No "open-ended" campaigns.
      - Announce 1 week before launch
      - Run for 7-30 days
      - Clear "doors close" moment

   c. **Design exclusive assets**: What do paid subscribers get ONLY during this campaign?
      - Live workshops or boot camp sessions
      - Member-only calls with the creator
      - Special trainings or masterclasses
      - One-time bonus assets (templates, guides, vault additions)
      - Personal chat welcome from the creator

   d. **Build the promotion calendar**:
      - **Pre-launch (7 days)**: Teaser notes, countdown posts, "why I'm doing this"
      - **Launch day**: Announcement post + 3-5 Notes + email to free list
      - **Mid-campaign**: Daily notes with social proof (new member count), behind-the-scenes, testimonials
      - **Final push (last 3 days)**: Urgency notes, "doors closing" messaging, recap of what's inside
      - **Close day**: Final "thank you" post + results announcement

   e. **Multi-channel deployment**:
      - Notes (primary — 2-3 per day during campaign)
      - Long-form post (launch + close)
      - Email to free subscribers (launch + midpoint + close)
      - Cross-platform (LinkedIn, Twitter if applicable)

6. Track and report:
   - Daily paid subscriber count
   - Conversion rate (free → paid during campaign)
   - Top-performing notes/posts by engagement
   - Revenue impact (monthly + annual split)

7. Cross-expert stacking (optional):
   - Stack with Tyler Denk (`/newsletter-growth-audit`) for referral mechanics
   - Stack with Kallaway (`/hook-forge`) for campaign note hooks

8. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Bestseller campaign — [campaign name]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-bestseller-campaign \
    --type Campaign \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Named campaign sprint with exclusive assets, promotion calendar, multi-channel deploy"
```
