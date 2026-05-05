---
description: Pull 50+ verbatim customer quotes from 3+ unmoderated venues (Reddit, YouTube comments, Amazon reviews) and cluster into 8-12 distinct Idea axes for any product/audience
---

# Workflow 04 — IVOC Mining Sprint

> **Tier 2 — Practitioner.** Indirect Voice of Customer. The research foundation that makes everything else work. Most ads / posts / emails fail because they use brand language; this workflow forces customer language.

---

## Pre-Flight Gate

- [ ] You have a defined product domain (not just "fitness" — "high-protein meal replacement for busy parents")
- [ ] You have access to the open web (Reddit / YouTube / Amazon)
- [ ] You have 60-120 minutes for the sprint

---

## Skill Acquisition

1. **`genius.md`** — IVOC Mining pattern + Research Provenance quality criterion
2. **`references/cross-domain-patterns.md`** — IVOC transfers beyond ads

---

## Execution

You are Alex Myatt running an IVOC sprint. The deliverable is verbatim customer language, NOT your interpretation. AI-summarized quotes don't count. Your judgment is in the clustering, not the source.

### Step 1 — Venue Selection (5 min)

Pick 3+ unmoderated venues for the product/audience. Unmoderated = customers complain freely without brand intervention.

**Default venue stack**:
1. **Reddit** — subreddit search. Find the 1-2 subs where the audience actually lives. Search past 6 months. Sort by top + new.
2. **YouTube comments** — comment threads on competitor product reviews / unboxings / "is X worth it?" videos. Comments are where buyers self-disclose.
3. **Amazon reviews (negative)** — 1-3 star reviews on competitor products. Negative reviews surface unmet needs and exact pain language.
4. **Niche forums / Discords / Facebook groups** — where audience-specific.
5. **Trustpilot / G2 / Capterra (negative)** — for SaaS / service businesses.
6. **TikTok comments** — under "X review" / "is X worth it" videos.

**Rule**: 3+ venues minimum. Single-venue research = single-source bias.

### Step 2 — Quote Pull (45-60 min)

Pull 50+ verbatim quotes. Copy-paste, don't paraphrase.

```
QUOTE BANK

VENUE 1: r/[subreddit_name]
- "[verbatim quote]" — [thread title or context]
- "[verbatim quote]" — [thread title or context]
... (15-20 quotes)

VENUE 2: YouTube comments on [video title / channel]
- "[verbatim quote]"
- "[verbatim quote]"
... (15-20 quotes)

VENUE 3: Amazon reviews on [competitor product]
- "[verbatim quote]" — [N stars]
- "[verbatim quote]" — [N stars]
... (15-20 quotes)
```

**Quality bar**: every quote is a real string a real person typed. No paraphrasing. No "general sentiment" summaries. No AI-generated quotes.

**Anti-pattern check**: if you find yourself "summarizing what customers usually say," STOP. Go pull more verbatim. The source IS the deliverable; cleverness in clustering is downstream.

### Step 3 — Cluster Into Ideas (20 min)

Group quotes by recurring word, recurring fear, recurring objection, recurring metaphor. Each cluster = one Idea axis for the Content Grid.

```
IDEA CLUSTERS

CLUSTER 1: [Cluster name — captures the shared meaning]
- "[quote]" (Venue 1)
- "[quote]" (Venue 2)
- "[quote]" (Venue 3)
- "[quote]" (Venue 1)
[3+ quotes minimum per cluster]

CLUSTER 2: [Cluster name]
- ...

(Aim for 8-12 clusters)
```

**Cluster quality bar**:
- Minimum 3 verbatim quotes per cluster
- Quotes from at least 2 different venues per cluster (cross-venue recurrence = real pattern)
- Cluster name is in CUSTOMER language, not brand language

### Step 4 — Cluster Ranking

For each cluster, score:

| Cluster | Recurrence (how often) | Emotional charge (how angry/desperate) | Buying-intent proximity |
|---|---|---|---|
| Cluster 1 | High / Med / Low | High / Med / Low | High / Med / Low |
| ... | | | |

**Highest-leverage clusters**: high recurrence + high emotional charge + close to buying-intent moment. These become your top Idea axes.

### Step 5 — Language Map (the gold)

Pull the 10-15 most-repeated VERBATIM PHRASES across all clusters. These are the exact words to use in copy/ads.

```
LANGUAGE MAP — TOP 15 PHRASES TO USE VERBATIM IN COPY

1. "[exact phrase]"
2. "[exact phrase]"
...
15. "[exact phrase]"

LANGUAGE MAP — PHRASES TO AVOID (brand language nobody uses)
1. "[phrase]" — not in any IVOC; brand assumption
2. ...
```

### Step 6 — Hand-Off Brief

Output for downstream use:

```
IVOC SPRINT OUTPUT — [Product / Audience]
- Venues mined: 3+ (named)
- Total verbatim quotes: 50+
- Idea clusters identified: 8-12
- Top 3 highest-leverage clusters: [named with reasoning]
- Language Map: 15 use phrases + N avoid phrases

READY FOR: /myatt-grid (build content grid from clusters), /myatt-ces (full creative engine), or any copywriting workflow needing audience language
```

---

## Content Type Adaptations

| Surface | Adaptation |
|---|---|
| **Meta ads (default)** | Use as written |
| **B2B SaaS** | Add G2 / Capterra / Trustpilot to venue list. Reddit + LinkedIn comments |
| **Service businesses** | Trustpilot + Google Reviews + niche-specific forums |
| **Newsletter / Substack** | Comments on competitor newsletters, niche subreddits, Twitter replies to competitors |
| **Local services** | Google Reviews + Yelp (negative) + Nextdoor + local Facebook groups |
| **Coaching / Info products** | Skool community feeds + Discord servers + YouTube comments on free content in space |

---

## Output Requirements

- [ ] 50+ verbatim quotes (no paraphrasing)
- [ ] From 3+ unmoderated venues
- [ ] Clustered into 8-12 distinct Idea axes
- [ ] Each cluster has ≥3 quotes from ≥2 venues
- [ ] Cluster ranking by recurrence × charge × buying-intent
- [ ] Language Map (15 use phrases + avoid list)

Deliverable: 4-8 pages depending on quote density.

---

## Quality Gate

- [ ] Research provenance ≥7 (50+ verbatim quotes, multi-venue)
- [ ] Cluster names in customer language (not brand language)
- [ ] Top clusters cross-venue (real pattern, not single-thread artifact)

**Anti-pattern check** (Alex would reject):
- [ ] No AI-generated "typical customer quotes"
- [ ] No paraphrased quotes ("customers often say things like...")
- [ ] No single-venue clusters (likely artifact of one influencer/thread)
- [ ] No clusters in marketing language ("desire for transformation")

---

## Stacking

- **Downstream**: feed clusters directly into `/myatt-grid` (X-axis) or `/myatt-ces` (full deployment)
- **Universal**: this output also fits any copywriting / hook generation workflow that needs verbatim audience language
- **AI-augmented variant**: run `/myatt-ai-augmented-ces` if you want AI to assist with venue surfacing (but still verbatim pulls)
