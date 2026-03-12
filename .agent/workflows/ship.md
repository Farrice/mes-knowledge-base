# Ship — Quick Content Sprint

> **Invocation**: `/ship` | `@ship` | "run ship" | "let's ship"
> **Purpose**: Produce and publish content fast. 1 expert, no perfectionism, auto-logged.
> **When**: You want to get something out into the world without the full chain.

---

## How It Works

This is a streamlined content workflow. It skips the multi-expert ensemble, writers' room, and full quality gate. It gets you from idea to published in 20-30 minutes.

**The full system is still available.** This is a fast lane, not a restriction. Use `/deep-work` for strategic pieces, `/content-sprint` for the full chain, or any other workflow anytime.

---

## Step 1: What Are We Shipping?

Ask Farrice:
- **What's the topic or idea?** (Can be a sentence, a question, a half-formed thought)
- **What platform?** (LinkedIn default, unless specified)
- **Is there an existing draft?** (Check `_active/linkedin-launch/` for ready-to-publish drafts)

If there's already a draft ready to publish → skip to Step 4.

---

## Step 2: Load 1 Expert

Match the content type to the right expert:

| Content Type | Load This Expert |
|-------------|-----------------|
| LinkedIn post | Lara Acosta (`skills/lara-acosta-linkedin-content/SKILL.md`) |
| Hooks/attention | Kallaway (`skills/kallaway-content-psychology/SKILL.md`) |
| Storytelling | Shaan Puri (`skills/shaan-puri-storytelling/SKILL.md`) |
| Sales/copy | Cardinal Mason (`skills/cardinal-mason-ai-copywriting/SKILL.md`) |
| Framework/education | Nicolas Cole (`skills/nicolas-cole-digital-writing/SKILL.md`) |

Load SKILL.md only (Tier 1). Not genius.md. Not the full workflow suite. Just enough to write well.

Also load: `FARRICE.md` (voice reference — always).

---

## Step 3: Write the Draft

- Write ONE version. Not 3 variants. One.
- Target: 150-400 words for LinkedIn.
- Apply the loaded expert's core pattern (e.g., Lara's Pattern 20 for headlines).
- Read FARRICE.md voice rules: Show don't tell. No forced jargon. Real open loops.

---

## Step 4: Quick Self-Check

Read the draft once. Answer these 3 questions:

1. **Does it sound like Farrice?** (Would he say this to a friend?)
2. **Would a stranger stop scrolling?** (First 2 lines matter most)
3. **Is there a reason to keep reading to the end?** (Tension, curiosity, open loop)

All 3 yes → **Publish now.**
Any no → **One revision pass**, then publish regardless.

---

## Step 5: Auto-Log

After publishing (or delivering the final draft), log the session automatically:

```bash
python execution/log_performance.py log "[Post title or topic]" \
    --skill [loaded-skill-name] \
    --type Content \
    --quality [1-10 honest score] \
    --intent [1-10] \
    --expert [1-10] \
    --adversarial [1-10] \
    --status Keep \
    --notes "[What worked, what felt off, Farrice feedback]"
```

**The AI proposes the scores. Farrice confirms or adjusts.** No cognitive load on the user.

---

## What This Workflow Does NOT Do

- No multi-expert loading (use `/deep-work` for that)
- No writers' room treatment (use `/deep-work` or `/content-sprint`)
- No 3-variant approach (use `/content-sprint --serial`)
- No ecosystem check (use `/deep-work` for strategic positioning pieces)

**This is for volume. Ship Day energy. Get it out, learn from the data, improve next time.**
