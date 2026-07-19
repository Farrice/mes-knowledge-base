---
name: market-pulse
description: 2x/week ear-to-ground loop — signal scan, angle mining, content bank filing
status: active
trigger: RemoteTrigger (Mon+Thu 09:00 AM ET)
time_estimate: 60-90 minutes
---

# Market-Pulse Workflow — Proof-to-Market Sprint Loop

**Cadence:** Monday + Thursday 09:00 AM ET  
**Duration:** 60–90 minutes  
**Outputs:** `research_outputs/market-pulse/[YYYY-MM-DD]-pulse.md` + 5–8 atomic angle files filed to `_active/farrice-brand/content/bank/angles/`  
**Review Gate:** Farrice 5-min review before publishing angles to social  

---

## Phase 1: Signal Scan (25 minutes)

**Sources (in order; stop when you find 3–5 signals):**

1. **NutraIngredients** (daily, free) — Launch announcements, funding rounds, regulatory news
2. **PRNewswire** (searchable, free) — Brand press releases (supplement, performance, wellness)
3. **FTC Health/Supplement Guidance** (weekly check) — New enforcement actions, warning letters
4. **McKinsey Health Reports** (monthly) — Category trends, consumer shifts
5. **Vitamin Shoppe Trends Dashboard** (if available) — Top-selling categories, emerging gaps

**What counts as a signal?**

- Brand launching a new product line or repositioning
- Funding round (Series A/B/C, acqui-hire, acquisition)
- Retail expansion (Costco, CVS, Amazon fresh, direct)
- Regulatory action (FTC warning, FDA letter)
- Category trend (GLP-1 adjacencies, longevity move, gen-Z entry)
- AI/tech integration (personalization, ChatGPT, smart packaging)

**For each signal, log:**
- Brand name
- Signal type (launch / raise / retail / regulatory / trend / AI)
- Date discovered
- Source URL
- 1-line description
- Verification: VERIFIED / LIKELY / UNCONFIRMED

**Output location:** Keep a running list in the pulse.md file (see Phase 4).

---

## Phase 2: Angle Mining (30 minutes)

**For each signal, generate 1–2 angles per pillar** (5 pillars × 3–5 signals = 15–25 angles, reduce to 5–8 by quality/relevance).

**The 5 Pillars (from founding brief):**

1. **Message Before Money** — positioning clarity upstream of spend
2. **Claim-Safe Growth Lever** — stacking claims by evidence strength
3. **Sea of Same** — category differentiation through uncontested language
4. **Body Doesn't Read Deck** — translating positioning into lived experience
5. **Machine Reading Label** — AI-search visibility & label language

**Angle Template (per pillar per signal):**

```
**Pillar:** [Pillar Name]
**Signal:** [Brand + occasion]
**Angle Title:** [Catchy hook, 5–10 words]
**Thesis:** [1–2 sentence positioning insight]
**Hook:** [Opening line for social content]
**Authority Source:** [Why this matters — link/expert/data point]
**Emoji/Tone:** [Mood — observed/urgent/contrarian/analytical]
**Content Form:** [Post / DM / comment / case study]
**Example Snippet:** [5–15 word example for how to surface this]
```

**Angle Mining Checklist:**

- [ ] Signal ties to a real occasion (not hypothetical)
- [ ] Angle doesn't duplicate a recent post/DM
- [ ] Thesis connects signal to Farrice's 5-pillar frame
- [ ] Hook is observation-first, not prescriptive
- [ ] Authority source is primary (link/quote/data), not inference
- [ ] Tone matches BLEND voice (I-narrative, no jargon, friend-on-shoulder)

**Quality Bar:**
- 5–8 angles per pulse run (not 20+)
- Each angle *deployable* in 1–2 DMs or 1 social post
- No cheap questions, no generic category insights
- Every angle ties to a specific brand occasion (cold DM hook)

---

## Phase 3: Content Bank Filing (15 minutes)

**Directory Structure:**

```
_active/farrice-brand/content/bank/
├── angles/
│   ├── message-before-money/
│   │   ├── 2026-07-18-create-wellness-rebranding-angle.md
│   │   └── 2026-07-20-nativepath-claim-safety-angle.md
│   ├── claim-safe-growth-lever/
│   ├── sea-of-same/
│   ├── body-doesnt-read-deck/
│   └── machine-reading-label/
├── hooks/
│   ├── cold-dm-hooks.md
│   ├── category-insights.md
│   └── regulatory-hooks.md
└── drafts/
    ├── social-post-drafts.md
    └── case-study-seeds.md
```

**File Naming Convention (angles/):**

`[YYYY-MM-DD]-[brand-slug]-[signal-type]-[pillar-slug].md`

Example: `2026-07-18-create-wellness-rebrand-message-before-money.md`

**Angle File Format:**

```markdown
---
date: YYYY-MM-DD
pillar: [Pillar Name]
signal: [Brand + Occasion]
status: ready | draft | deployed
---

# [Angle Title]

**Thesis:**  
[1–2 sentences]

**Hook:**  
[Opening line]

**Authority:**  
[Link/quote/data]

**Example Snippet:**  
[5–15 words]

**DM Version (if ready to send):**  
[Customized DM to [Brand Contact]; 3–5 sentences]

**Deployment Notes:**  
[Who to send to, timing, if this is a comment or DM]
```

**Filing Checklist:**

- [ ] File in correct pillar folder
- [ ] Filename matches convention
- [ ] Status field set (ready/draft/deployed)
- [ ] DM version is customized (no placeholders left)
- [ ] Authority source is linked or quoted
- [ ] No health claims without FTC/FDA safe language

---

## Phase 4: Watchpoint Update (10 minutes)

**Create/update:** `research_outputs/market-pulse/[YYYY-MM-DD]-pulse.md`

**File Format:**

```markdown
---
date: YYYY-MM-DD
run_id: pulse-[date]
status: ready-for-review
---

# Market Pulse — [YYYY-MM-DD]

## Signals Discovered (This Run)

| Brand | Occasion | Type | Date | Source | Verification |
|-------|----------|------|------|--------|--------------|
| [Brand] | [Signal] | [launch/raise/retail] | [Date] | [URL] | VERIFIED |

## Category Tensions Identified

- [Tension 1 + why it matters to Farrice's offer]
- [Tension 2 + why it matters]

## Regulatory Watch

- [FTC action / FDA letter / warning letter relevant to beachhead]
- [Implication for claim-safe language]

## AI-Search Signals

- [ChatGPT trend in the space]
- [Perplexity recommendation pattern observed]
- [Implication for Machine Reading Label pillar]

## Angles Filed This Run

| Pillar | Title | Brand | Status |
|--------|-------|-------|--------|
| [Pillar] | [Angle Title] | [Brand] | ready |

**Angles ready to deploy:** [Count]  
**Angles in draft:** [Count]  
**Total angles in bank:** [Count]

## Next Loop Watchpoints

- [Watch for X brand announcement by date]
- [Monitor FTC enforcement actions]
- [Track category saturation in Y segment]

## Notes

[Any observations about market movement, category language shifts, regulatory trends that inform future angle mining]
```

**Watchpoint Update Checklist:**

- [ ] All signals from Phase 1 logged in table
- [ ] Category tensions tied to Farrice's 5-pillar frame
- [ ] Regulatory/AI-search sections include implications (not just facts)
- [ ] Angles filed section matches Phase 3 output
- [ ] Next loop watchpoints are specific (not generic)

---

## Alarm Conditions (Escalate if any occur)

| Condition | Action |
|-----------|--------|
| **7 days, no brand occasions found** | Expand source list or adjust beachhead filter; log to Farrice |
| **FTC news + zero angles filed** | Angle mining skipped or failed; review Phase 2 and retry |
| **Pulse run completed but <3 angles filed** | Reduce signal count (Phase 1) or widen pillar filter; review quality bar |
| **Same brand signal twice in 14 days** | Deduplicate; update watchpoint to skip near-term re-mines |
| **Angle written but no DM customization attempted** | File stays in `draft` status; retry with one specific contact in mind |

---

## Gates (Never Skip)

✓ **No phantom research.** Every signal has a source URL.  
✓ **Receipts labeled.** VERIFIED (date-stamped press release), LIKELY (news article), UNCONFIRMED (rumor/indirect).  
✓ **Claim-safe pass.** No health claims in angles without FTC/FDA safe language (structure-function, not disease cure).  
✓ **No cheap questions.** Angles end with a statement, observation, or offer—never "Thoughts?" or generic category question.  
✓ **Pillar-tied.** Every angle connects to one of the 5 pillars explicitly (in "Pillar" field of frontmatter).  

---

## Deployment Path (After Farrice Review)

1. **Farrice review** (5 min) — reads pulse.md, approves angles, flags rewrites
2. **Rewrites** (if needed) — update angle files in content bank
3. **Social post drafting** (optional, Farrice decides) — convert 1–2 angles to LinkedIn posts or threads
4. **DM deployment** (cold outreach) — send angles to Tier 1 Dream 100 contacts (1–2 per run)
5. **Log results** — impressions, DMs received, calls booked (tied to source angle)

---

## Content Bank Maintenance (Monthly)

- Deduplicate angles (if 2 angles too similar, merge)
- Archive deployed angles (move to `_active/farrice-brand/content/bank/archive/[YYYY-MM]/`)
- Refresh watchpoints (update next-loop predictors)
- Review quality bar (any angles that didn't land? Why?)

---

**Created:** 2026-07-18  
**Last Updated:** 2026-07-18  
**Next Scheduled Run:** Monday 2026-07-22, 09:00 AM ET
