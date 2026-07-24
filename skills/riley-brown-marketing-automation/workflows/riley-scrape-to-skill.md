---
description: "Riley Brown's flagship — turn any creator into a named, callable voice-writing skill in three prompts (scrape non-sponsored winners → freeze as a skill → deploy in-voice on a fresh topic)"
---

# /riley-scrape-to-skill — Creator → Voice Skill (front door)

Riley's whole doctrine in one run (Exemplar 1): scrape a creator's verified top-performers, exclude sponsored posts with an audit trail, freeze them as a *named* skill, then generate in that voice on a brand-new topic. His words: "turn all of the his top performing videos into a skill. Call it Callaway top performing... so that I can write content in his style at any time." The output must survive being read aloud — "actually so good... exactly in his tone."

## Pre-Flight Gate

Load `genius.md` decision framework first. Proceed only if:
- The creator is **public** and has a scrapeable corpus (IG/TikTok/YouTube). Private/gated → stop.
- You can **judge** this creator's domain (taste is the non-delegable input — Hidden Knowledge #3). If you can't tell their good from their bad, flag it; the extraction will be blind.
- The goal is a *reusable* voice, not a one-off — otherwise a single scrape + inline prompt is enough.

## Skill Acquisition

- `genius.md` — Patterns 1 (examples-over-instructions), 4 (creator-to-skill), 5 (authenticity filter), 2 (turn-it-into-a-skill)
- `references/source-quotes.md` — Exemplar 1 verbatim prompts
- Live infra: `.agent/workflows/scrape-creator.md`, the `/extract` family

## Execution (Riley's three prompts, on our infra)

1. **Scrape (the exemplar layer).** Run `/scrape-creator`:
   ```bash
   python3 execution/social_intel.py scrape "<handle_or_url>" --platform <auto|instagram|tiktok|youtube> --limit 10 --batch "riley-<creator>-$(date +%Y-%m-%d)"
   ```
   Riley's model note applies to the *analysis*, not the scrape: "5.6 soul... medium... this is a straightforward task." Confirm the read-back honestly (how many transcripts actually succeeded), the way his agent did.
2. **Filter + why-effective.** In the analysis pass, **exclude sponsored/boosted posts and state each exclusion** ("not sponsored... those can be boosted. So it's like fake") — this is Riley's authenticity filter with a retained audit trail. Then answer his second ask: *why is this creator effective?* Ground verdicts in a hook lens (`skills/kallaway-*`, `diandra-hook-architect`) per `/scrape-creator` step 2.
3. **Freeze it as a named skill.** The corpus is already banked in the Notion page bodies, so graduate straight to `/extract` (ungated, standing decision 2026-06-09). The extraction *is* Riley's "turn it into a skill" — a named, inspectable asset, not a black box. Mark the winning posts' `Extract Candidate` checkbox first.
4. **Deploy in-voice on a fresh topic.** Invoke the new skill on a topic the creator never covered, Riley-style: "…does a great job explaining things simply while also making it seem urgent and cool. Please create a script for this. Write three options in his voice." Read the output aloud — does it pass the "exactly in his tone" bar?
5. **Correct into the file.** If a take drifts, don't fix it in chat — write the rule into the skill ("never say X"), so it compounds (Pattern 3).

## Content Type Adaptations

| Source | Adaptation |
|---|---|
| YouTube long-form | yt-dlp captions are free; transcript is the exemplar substance |
| TikTok / Reels | Apify transcript actor (~$0.25/run cap); hook + pacing carry more than script |
| Instagram | no transcript actor in contract — caption stands in for Hook/Analysis |
| LinkedIn creator | scrape captions; pair with `/riley-lara-amplifier` for the ghostwrite |

## Output Requirements

- A **named** skill/extraction (the API into the voice), born from a successful run — not a prompt written from scratch.
- Sponsored exclusions stated with evidence; non-sponsored winners only in the exemplar set.
- At least one deploy-ready in-voice output on a *new* topic, read aloud and judged.
- Notion batch verifiable (`Batch` tag); `Extract Candidate` marked on graduated posts.

Execution prompt: references/prompts-v2/creator-voice-skill-deploy.md — honor its Output Contract.

## Quality Gate

Output survives being read aloud ("exactly in his tone")? · Sponsored posts excluded *with* audit trail? · The asset is a named, inspectable file, not a re-explained prompt? · Corrections written into the file, not left in chat? · Did you actually judge the voice, or delegate blind (taste gate)?
