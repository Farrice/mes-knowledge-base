---
description: Build or reposition a Substack publication with the Three Questions positioning lock
---

# Sinem Publication Setup

Build or reposition a Substack publication from scratch using Sinem Günel's Three Questions positioning methodology. Treats the publication as business infrastructure — not a newsletter.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md`
   - Read `agents/sinem-gunel/AGENT.md`

2. Score intent (Chain Step 1): Score = 5 (deliverable: publication architecture, audience: creator/business owner, context: Substack launch or reposition, end state: fully positioned publication ready for growth).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - What is your publication about? (current name, topic, niche)
   - Who is it for? (target reader — be specific)
   - What do you want a reader to eventually DO beyond reading? (buy a product, book a call, join a community)
   - Current subscriber count (if existing publication)
   - Any existing paid tier? If yes, what's behind it?

5. Execute the Three Questions Positioning Lock:
   a. **Question 1 — What?** Lock the publication's core promise into a single sentence. Test: could someone repeat this to a friend in 5 seconds?
   b. **Question 2 — Who?** Define the specific human this is for. Not demographics. Identity: what do they believe, fear, want to become?
   c. **Question 3 — What-Next?** Define the downstream action. This is NOT "subscribe." This is: buy my course, book my coaching, join my program.

6. Build publication components:
   - **Name audit**: Does the name pass the "say it out loud" test? Is it searchable? Does it convey the promise?
   - **About page**: Deploy the Silent Salesman pattern (who you are + what they get + do they belong — 200 words)
   - **Hero post**: Write the "start here" post that demonstrates the publication's value and creates the first trust deposit
   - **Navigation design**: Map the guided pathway (free → paid → products → high-ticket)
   - **Welcome email**: First message new subscribers receive — set expectations and deliver immediate value

7. Cross-expert stacking (optional):
   - Stack with Dai Media (`/consumer-posture-profile`) for identity-based positioning
   - Stack with Kallaway (`/content-cluster`) for topic mapping

8. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Publication setup — [publication name]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-publication-setup \
    --type Strategy \
    --intent 9 --expert-score 8 --adversarial 8 \
    --notes "Three Questions lock + about page + hero post + navigation + welcome email"
```
