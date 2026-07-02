---
description: Daily Notes discovery engine — story-driven notes with batching system
---

# Sinem Notes Discovery Engine

Deploy Sinem Günel's Notes-as-primary-growth-lever methodology. Story-driven notes get subscribers; educational notes get likes. This workflow produces a week's worth of discovery-optimized notes.

## Steps

1. Load expert context:
   - Read `.agents/skills/source-command-sinem-substack/genius.md`

2. Score intent (Chain Step 1): Score = 4 (deliverable: batch of story-driven notes, audience: Substack discovery feed, context: daily growth engine, end state: 7-14 publish-ready notes).

3. Route (Chain Step 3): Sinem Günel → `substack-business-architecture` skill.

4. Gather input:
   - Recent long-form post URL or topic (source material for extraction)
   - 2-3 personal stories or experiences from the past week
   - Any trending topics in your niche right now
   - Current daily Notes posting cadence (how many per day?)

5. Execute the Story > Education principle:
   a. **Story extraction**: From each input, extract the specific MOMENT — not the lesson. What happened? Where were you? What did you feel?
   b. **Arc construction**: For each note, build the 5-part arc:
      - Open with a specific moment (not a framework)
      - Share the insight that emerged
      - Show the action taken
      - Give the result
      - Turn to the reader ("Have you experienced this?")
   c. **Batch production**: Generate 7-14 notes across these categories:
      - 3-4 story-driven notes (personal moments → insights)
      - 2-3 observation notes (what you noticed → what it means)
      - 1-2 contrarian takes (common advice you disagree with → why)
      - 1-2 reader engagement notes (questions, polls, "what would you do?")

6. Quality gate — Each note must:
   - Stand alone (no "as I said in my last post" dependencies)
   - Open with a specific moment, NOT a tip or framework
   - Be readable in under 60 seconds
   - End with a reader turn that invites response

7. Cross-expert stacking (optional):
   - Stack with Kallaway (`/five-input-content-gate`) for obsession-level calibration
   - Stack with Eric Roth (`/roth-social`) for cinematic depth in story notes

8. Finalize (Chain Step 6):
```bash
python3 execution/chain_runner.py finalize "Notes batch — [topic/week]" \
    --expert sinem-gunel \
    --skill substack-business-architecture \
    --workflow sinem-notes-discovery \
    --type Content \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Story-first notes batch with 5-part arc construction"
```
