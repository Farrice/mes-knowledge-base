---
description: Craft recipient-first outreach for larger creator partnerships
---

# Sinem Collaboration Outreach

Deploy Sinem Günel's collaboration physics for reaching out to larger creators. Every message leads with value for THEM, proposes a specific format, and makes it easy to say yes.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md` (Move 5: Collaboration Outreach Formula)

2. Score intent (Chain Step 1): Score = 4 (deliverable: outreach messages for creator partnerships, audience: larger creators, context: Substack growth via collaboration, end state: 3-5 ready-to-send outreach messages).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Target creators (names, publications, subscriber counts if known)
   - Your publication's unique angle — what makes YOU a fit for THEM?
   - What format do you want to propose? (cross-promotion, guest post, live stream, interview, collaborative note)
   - Any existing relationship with these creators? (cold, warm, or hot lead)

5. Execute the 3-element outreach formula:

   For each target creator, build a message containing:

   a. **Element 1 — Specific format proposed**: Not "let's collaborate" but "I'd love to do a 30-minute live conversation on [specific topic] that both our audiences would benefit from."
   
   b. **Element 2 — Why YOU specifically**: Not your resume. One sentence on what makes your perspective uniquely valuable to their audience. What gap do you fill that they don't cover?
   
   c. **Element 3 — What's in it for THEM**: Not "exposure to your audience." Specific value: "Your readers would get [concrete benefit]. I'll handle all promotion on my end. You just show up."

6. Quality gates:
   - The message must be scannable in 5 seconds
   - Value for recipient appears in the first 2 sentences
   - No credential dumps
   - No "I'm a huge fan" openers (everyone says this)
   - The ask is clear and requires minimal effort from them
   - Total message length: under 150 words

7. Apply the Complementary Competitor Paradox:
   - Prioritize creators in the SAME space (overlapping audience = pre-qualified readers)
   - "Competitors" are your best collaboration partners — audiences overlap but are not identical

8. Cross-expert stacking (optional):
   - Stack with Lara Acosta (`/profile-conversion`) for LinkedIn-first outreach pipeline
   - Stack with trust-building workflows for warming cold leads before outreach

9. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Collaboration outreach — [target creators]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-collaboration-outreach \
    --type Outreach \
    --intent 8 --expert-score 8 --adversarial 7 \
    --notes "3-element formula: specific format + unique fit + recipient value"
```
