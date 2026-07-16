---
description: On-demand social listening — query creator/hashtag/niche, scrape Apify, synthesize brief with receipts
---

# /social-listen — Social Listening Head (On-Demand)

Deploy the social listening pipeline: **Apify scraping (actor-selected) → data → synthesis → strategic brief with receipts.** This workflow answers "What's happening in [niche/creator/hashtag]?" with raw data grounded in Apify, then synthesizes it into a strategic listening brief.

**Apify is for raw extraction. Synthesis is for signal.** This workflow is the pipeline: Apify → Perplexity/synthesis → deliverable with receipts showing every actor invoked and what was found.

## Usage

```
/social-listen "DWA on Threads" --lane farrice-brand
/social-listen --creator "thatgirl" --lane myBPM --depth deep
/social-listen "#fitnessmotivation" --transcripts
/social-listen "FTHB first-time home buyer advice" --lane jen
/social-listen --hashtag "streetwear drops" --lane myBPM
```

## When to Use

**Routes HERE** (`/social-listen`):
- Niche research: "What are people saying about X?"
- Creator/personality analysis: Profile data, content themes, audience sentiment
- Hashtag trend scanning: Emerging topics, conversation sentiment, content patterns
- On-demand listening: Quick snapshots of specific topics before deciding on posting/response strategy
- Transcript enrichment: Creator/YouTube content depth via transcript analysis (NEW — Scrape Creators actors)

**Routes elsewhere instead:**
- Recurring pulse (scheduled): `/social-pulse` (weekly per lane, background)
- Generic web research: `/deep-research` (when Apify doesn't apply)
- Real-time monitoring setup: Use the recurring pulse infrastructure

---

## Input Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `query` | string (positional or `--query`) | YES | The topic, hashtag, creator name, or research question | `"DWA on Threads"` or `"@thatgirl"` |
| `--lane` | string | NO | Which lane this query belongs to (farrice-brand, myBPM, jen, client-[name]). Affects actor selection and ledger. | `--lane farrice-brand` |
| `--creator` | string | NO | Shorthand for creator/profile research | `--creator thatgirl` |
| `--hashtag` | string | NO | Shorthand for hashtag scanning | `--hashtag fitnessmotivation` |
| `--transcripts` | flag | NO | Prioritize transcript actors for YouTube/TikTok content | `--transcripts` |
| `--depth` | string | NO | Research depth: `quick` (1 actor) \| `standard` (2-3 actors) \| `deep` (full set) | `--depth deep` |
| `--max-cost` | float | NO | Override per-run cost ceiling (default $0.25) — must respect $29/mo global cap | `--max-cost 0.50` |

---

## Steps

### Step 1 — Query Parsing & Intent Classification

Parse the input to determine **research intent**:

| Signal | Intent | Primary Actors |
|--------|--------|----------------|
| `@creator` or `--creator` | Creator/profile analysis | `sc-tiktok-profile` (TikTok) or `sc-youtube-channels` (YouTube) |
| `#hashtag` or `--hashtag` | Hashtag trend scanning | `sc-tiktok-hashtag`, `sc-tiktok` (trending under hashtag) |
| Free-text niche | Niche research + sentiment | `sc-tiktok` (search), `reddit` (subreddit depth) |
| Transcript flag OR YouTube link | Transcript-heavy research | `sc-youtube-transcripts`, `sc-tiktok-transcripts` |
| Reddit subreddit reference | Reddit deep dive | `reddit` (posts + comments) |

**Actor Selection Rules**:

1. **If `--transcripts` flag**: Route to transcript actors first (`sc-youtube-transcripts`, `sc-tiktok-transcripts`). These are the enrichment layer Farrice is missing today — direct voice, not interpreted.
2. **If creator research** (`--creator` or `@mention`): TikTok → `sc-tiktok-profile`, YouTube → `sc-youtube-channels` (full channel metadata).
3. **If hashtag research**: `sc-tiktok-hashtag` for focused hashtag data. Add `sc-tiktok` for broader trending under hashtag.
4. **If niche/question research**: Decompose into social + Reddit. Start with `sc-tiktok` (search) + `reddit` (comments/discussions).
5. **Fallback chain** (if primary actor unavailable): Use generic actors (`tiktok`, `youtube`, `instagram` from original 7) or Perplexity synthesis-only.

**Depth scaling** (if `--depth` not specified, default to `standard`):

| Depth | Actors Invoked | Cost Estimate | Use Case |
|-------|----------------|---------------|----------|
| `quick` | 1 primary actor | ~$0.10-0.15 | Quick snapshot |
| `standard` | 2-3 actors (default) | ~$0.20-0.50 | Balanced research |
| `deep` | Full decomposition (4-5 actors) | ~$0.75-1.25 | Comprehensive listening |

---

### Step 2 — Budget Gate & Pre-Run Check

**Mandatory for any pay_per_event actor call:**

```bash
python3 execution/apify_client.py budget-status
```

Output shows:
- Global budget state (green / yellow / red)
- Pulse sub-budget status
- Projected cost for this run

**Proceed if:**
- Global state is green OR yellow (yellow = warn, proceed)
- Pulse sub-budget has headroom (if pulse_mode would apply; only for recurring pulse, not `/social-listen`)
- Actual cost ≤ `--max-cost` ceiling (default $0.25)

**Fallback if budget blocked:**
- Return the fallback response (`{"fallback": true, "status": "budget_exhausted"}`)
- Offer Perplexity synthesis instead: `"Budget is tight. I can synthesize what I know from memory + web search instead. Would that help?"`
- Do NOT retry automatically.

---

### Step 3 — Execute Apify Actor(s)

Run the selected actors via `execution/apify_client.py` with cost control:

```bash
# Example: TikTok profile + transcript
python3 execution/apify_client.py sc-tiktok-profile --profile "thatgirl" --max-cost 0.25
python3 execution/apify_client.py sc-tiktok-transcripts --search "thatgirl" --limit 5 --max-cost 0.25
```

**Logging**: Every actor invocation is logged to `.agent/apify-usage.json` with:
- Timestamp
- Actor key
- Results count
- Actual cost (usageTotalUsd from Apify response)
- Lane (if provided)

**Error handling**:
- If single actor fails: Proceed with other actors, note the gap in receipts
- If all actors fail: Return fallback response + offer Perplexity alternative
- If cost ceiling exceeded: Stop, return cost_ceiling_exceeded status, offer Perplexity alternative

---

### Step 4 — Data Synthesis & Brief Generation

**Input**: Raw Apify results (JSON arrays of posts/profiles/videos/transcripts)

**Process**:

1. **Data Cleaning**: Remove duplicates, filter spam/low-quality content
2. **Pattern Extraction**: 
   - Top recurring themes / conversations
   - Sentiment signals (positive, critical, question-asking, content patterns)
   - Creator/influencer mentions (who's influential in this niche)
   - Emerging trends / new content types
3. **Language Harvesting**: Extract verbatim phrases, hooks, objections (this is the signal layer Farrice needs)
4. **Gaps Identification**: What's missing? Unanswered questions, under-served angles

**Synthesis call** (if raw data is substantial — 50+ items):

Use Perplexity MCP `perplexity_ask` to synthesize:

```
Synthesize this social listening data into a brief covering:
1. **What's the conversation?** (top 3-5 recurring themes)
2. **Who's driving it?** (key creators/voices)
3. **What's the sentiment?** (opportunities, risks, questions)
4. **What's the language?** (verbatim phrases, hooks, objections)
5. **What's emerging?** (new trends, under-served angles)

Ground every claim in the data. Exact quotes matter.
```

This synthesis is the output layer — Farrice reads it, not the raw JSON.

---

### Step 5 — Listening Brief + Receipts

**Format** (Markdown, saved to `.agent/social-listening-briefs/[date]-[lane]-[topic].md`):

```markdown
# Social Listening Brief: [Topic]

**Date**: [date]
**Lane**: [lane]
**Query**: [original query]
**Data Age**: [most recent post date]

---

## Sources & Cost

| Actor | Type | Items | Cost | Status |
|-------|------|-------|------|--------|
| `sc-tiktok-profile` | Creator profile | 1 | $0.12 | ✓ |
| `sc-tiktok-transcripts` | Transcripts | 5 | $0.18 | ✓ |
| **Total** | — | **6** | **$0.30** | **✓** |

**Budget state**: Green (used $0.30 of ~$28.70 remaining)

---

## The Conversation

### Top Themes
1. **[Theme A]** (N posts) — Key quote: "[verbatim]" — What it signals: [implication]
2. **[Theme B]** (N posts) — Key quote: "[verbatim]"
3. **[Theme C]** (N posts)

### Emerging Trends
- [Trend 1] — first appeared [date], [N] posts in last 7 days
- [Trend 2]

---

## Key Voices & Creators

| Creator | Followers | Vibe | Key Content |
|---------|-----------|------|-------------|
| [@handle] | [count] | [positive/critical/educational] | [1-line summary] |

---

## The Language (Hooks, Objections, Desires)

### What People Want
- "[verbatim desire 1]" — [N] instances
- "[verbatim desire 2]"

### What People Fear
- "[verbatim objection 1]"
- "[verbatim objection 2]"

### How People Describe Themselves
- "[identity phrase]"
- "[community marker]"

---

## Sentiment Snapshot

| Sentiment | % | Count |
|-----------|---|-------|
| Positive / Enthusiastic | [%] | [count] |
| Critical / Questioning | [%] | [count] |
| Neutral / Informational | [%] | [count] |

---

## Gaps & Opportunities

- **Under-served angle**: [description] — No one's talking about [specific thing]
- **Unanswered question**: [question] — Appears [N] times but no expert weighs in
- **Positioning gap**: [description]

---

## Recommendations for [Lane]

1. **Content angle**: [specific idea based on language/gap]
2. **Timing**: [if trend is accelerating]
3. **Collaboration**: [if specific creators are moving the conversation]

---

## Raw Data Export

[Optional: link to `.tmp/social-listening/[slug]/` for full JSON if needed]
```

**Save location**: `.agent/social-listening-briefs/[YYYY-MM-DD]-[lane]-[slug].md`

**Receipts matter**: Every claim ties back to an actor + a quote/data point. No synthesis without receipts.

---

### Step 6 — Delivery & Lane Logging

1. **Present the brief** to Farrice (visual form or copy-paste, depending on context)
2. **Log to lane config** if lane specified: Update `.agent/social-listening-lanes.json` with run timestamp, cost, key findings
3. **Surface to COS** if this is strategic: Flag in `.agent/cos/` for morning brief if trends detected
4. **Archive the JSON**: Save raw Apify results to `.tmp/social-listening/[slug]/` for future reference

---

## Error Handling

| Scenario | Response |
|----------|----------|
| **Single actor fails** | Skip that actor, proceed with others. Note gap in receipts. |
| **All actors fail** | Return fallback status. Offer: "I can synthesize from web search + memory instead — want me to try?" |
| **Cost ceiling exceeded** | Stop run, return `cost_ceiling_exceeded` status. Offer Perplexity synthesis-only. |
| **Budget is yellow/red** | Proceed with warning. Prefer cheap actors (reddit, instagram, web) over expensive (maps). If pulse sub-budget is constrained, skip pulse-mode runs. |
| **Insufficient data** (< 10 items returned) | Note in brief. May be legitimate (niche query, new hashtag) or actor limitation. Offer follow-up with different actor. |
| **Transcript actor returns no transcripts** | Note "transcripts unavailable" and fall back to profile/comments data. |

---

## Estimated Cost & Time

| Scenario | Actors | Cost | Time |
|----------|--------|------|------|
| Quick creator profile | 1 actor (profile) | ~$0.12-0.18 | 1-2 min |
| Standard hashtag scan | 2-3 actors (hashtag + search) | ~$0.25-0.50 | 2-4 min |
| Deep niche research | 4-5 actors (multi-platform) | ~$0.75-1.25 | 5-8 min |
| Transcript-heavy | 2-3 transcript actors | ~$0.25-0.75 | 2-5 min |

**Monthly capacity at $29/mo**: ~30-50 `/social-listen` calls at standard depth (assuming pulse takes ~$5/mo).

---

## Fallback Contract (CRITICAL)

This workflow NEVER breaks on budget or Apify errors.

If Apify returns `{"fallback": true}`:

1. **First fallback**: Perplexity synthesis from what's already known (internal context)
2. **Second fallback**: Web search + Tavily for quick context
3. **Third fallback**: Honest message: "Budget exhausted for this type of research. Can I help with a different angle?"

Workflow degrades, never fails. User always gets a response.

---

## Next Steps After Listening Brief

- **COS integration**: Brief feeds into morning COS brief if strategic
- **Content planning**: Use findings to inform what Farrice posts
- **Creator follow-up**: Use language + trends to shape engagement
- **Recurring pulse**: If this topic should be monitored regularly, graduate to `/social-pulse` (weekly scans)
- **Deep research**: If findings raise strategic questions, route to `/deep-research` for deeper competitive/psychological mining

