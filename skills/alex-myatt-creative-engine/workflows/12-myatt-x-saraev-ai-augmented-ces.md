---
description: Full CES (Creative Engine System) with AI as amplifier (not generator) — automated IVOC mining, brief generation, batch concept production, all loaded with proprietary inputs first
---

# Workflow 12 — AI-Augmented CES (Myatt × Nick Saraev)

> **Tier 3 — Stacking.** Combines Alex Myatt's CES with Nick Saraev's AI agentic workflows. The non-negotiable principle: AI is amplifier, not generator. Proprietary inputs (your SOPs, your IVOC, your past creative archive) load FIRST; AI runs ON TOP. Get this order wrong and the system collapses to AI-slop with Alex's logo on it.

---

## Pre-Flight Gate

- [ ] You have an existing CES output from `/myatt-ces` OR a documented creative archive (your past ads, briefs, SOPs)
- [ ] You have IVOC done OR will mine it via this workflow
- [ ] You have access to AI tools (Claude / Gemini / GPT) AND ideally agentic platforms (n8n / Make / Zapier)
- [ ] You commit to Alex's principle: AI doesn't generate research, you do

**If you have no CES history**: do NOT start with this workflow. Run `/myatt-ces` manually first to build proprietary inputs. Then return.

---

## Skill Acquisition

1. **`genius.md`** (Alex) — full mental model + the explicit "AI is amplifier" hidden insight
2. **Nick Saraev**: `agents/nick-saraev/AGENT.md` — agentic workflow architecture
3. **`references/andromeda-mechanics.md`** — diversity layers + budget pathology
4. **`references/cross-domain-patterns.md`** — where CES principles transfer

---

## Execution

You are running CES with AI augmenting at every operational layer. Critical: proprietary inputs ALWAYS load first. AI never originates — it amplifies, varies, drafts FROM your inputs.

### Step 1 — The "AI Loading Order" Principle (set the standard upfront)

```
LOADING ORDER (CRITICAL — DO NOT REORDER)

1. PROPRIETARY INPUTS LOAD FIRST:
   - Your IVOC bank (verbatim, mined by you)
   - Your past creative archive (your best 20-50 ads, tagged by Idea/Style/Hook performance)
   - Your existing SOPs (brief templates, asset library protocol, turnaround SLAs)
   - Your Avatar definitions for this account
   - Your strategic brief (Luke's work if stacked)

2. AI LOADS PROPRIETARY INPUTS INTO CONTEXT:
   - System prompt: "You are operating ON TOP OF the following proprietary inputs. You amplify, vary, draft FROM these. You do not invent new inputs."
   - All proprietary docs in context window or via RAG

3. AI ASSISTS AT EACH CES STEP — but never originates the foundation
```

**Anti-pattern reminder**: a copywriter shows Alex their "research" — it's a Claude chat. Alex says "that's not your research, that's Claude's research." Don't be that copywriter. Don't ship that workflow.

### Step 2 — AI-Augmented IVOC Mining

```
IVOC AUGMENTATION (Saraev pattern: agentic mining)

WHAT YOU DO MANUALLY:
- Pick the 3+ unmoderated venues
- Define the search queries / threads to mine
- Verify quote authenticity by sampling

WHAT THE AGENT DOES:
- Scrapes Reddit threads / YouTube comments / Amazon reviews via API or browser automation
- Returns RAW verbatim quotes (no summarization, no paraphrasing)
- Sorts by recurrence and emotional charge

WHAT YOU DO AT THE END:
- Verify a 10% sample of the agent's pulls are authentic verbatim
- Cluster manually OR direct AI to cluster with explicit "do not invent quotes" guard
- Approve the Language Map

OUTPUT: same as /myatt-ivoc but 5-10x faster
GUARDRAIL: every quote in the bank is traceable to a real URL/post
```

**Suggested architecture**:
- n8n / Make workflow with browser automation node
- Claude or Gemini in a downstream node for clustering ONLY (not generation)
- Output to a tagged spreadsheet with venue / URL / verbatim quote columns

### Step 3 — AI-Augmented Brief Generation

```
BRIEF AUGMENTATION

WHAT YOU DO MANUALLY:
- Define the Avatar (your judgment)
- Pick the Idea axis from IVOC clusters (your taste)
- Pick the Style axis (your craft)

WHAT THE AGENT DOES:
- Generates DRAFT briefs at every Idea×Style intersection using your brief template
- Applies your tagged past-creative archive to suggest "ads similar to this concept performed X% / Y%"
- Pre-fills Andromeda Entity ID intent based on similarity to existing entities

WHAT YOU DO AT THE END:
- Edit every draft brief — your judgment on what to keep, what to rewrite
- Override AI suggestions on Avatar fit (AI doesn't truly understand the Avatar)
- Approve final briefs

OUTPUT: 30-72 briefs in the time it used to take to write 5
GUARDRAIL: human edit on every brief before production
```

### Step 4 — AI-Augmented Hook Generation

```
HOOK AUGMENTATION

WHAT YOU DO MANUALLY:
- Define the 5 hook types and your IVOC-derived language
- Pick which Vicious Hook principles are non-negotiable for this batch (4+)

WHAT THE AGENT DOES:
- Generates 5 hook variants per concept (one per type) using your IVOC language verbatim
- Self-scores each hook against the Vicious 8 principles
- Surfaces hooks below 4/8 for rewrite or rejection

WHAT YOU DO AT THE END:
- Read every hook (Alex's "Show Me Your Research" standard applies — your judgment, not AI's)
- Cut hooks that are technically vicious but feel hollow
- Approve final hook bank

OUTPUT: same as /myatt-vicious-diversity but at 3-5x throughput
GUARDRAIL: human read on every hook
```

### Step 5 — AI-Augmented Production Operations

```
PRODUCTION OPS AUGMENTATION (where Saraev's agentic patterns shine)

WHAT YOU AUTOMATE:
- Asset tagging: AI tags new footage by Style category, mood, lighting, talent
- Brief-to-script: AI converts approved briefs into first-draft scripts (you edit)
- Designer hand-off: AI generates the visual brief PDF from the concept brief
- QA gate: AI auto-checks each finished asset against the brief (length, hook timing, on-brand elements)
- Performance tagging: AI ingests Meta data and tags wins/losses back to Idea/Style/Hook per concept
- Weekly client report: AI generates the dashboard + summary; you add 2-3 sentences of strategic context

WHAT STAYS HUMAN:
- Brief approval (your judgment on Avatar fit)
- Final creative QA before launch (Alex's Vacation Test)
- Strategic decisions (kill threshold, winner-stacking direction, next test cycle scope)
- Client conversations
```

### Step 6 — AI-Augmented Care Square

```
CARE SQUARE AUGMENTATION (from Pattern 8)

WHAT YOU AUTOMATE:
- Results dimension: auto-pulled KPI dashboard (weekly)
- Perception dimension: AI drafts the "showable artifact" each month (the report the client shows their CEO)
- Relationship dimension: AI surfaces birthdays, podcast appearances, big company news (Crunchbase / LinkedIn / news APIs)
- Efficiency dimension: AI handles weekly summary emails, response acknowledgements, status updates

WHAT STAYS HUMAN:
- The actual relationship moments (you send the hamper, you make the call, you remember the kid's name)
- The strategic conversations
- The intervention plan when a dimension goes weak
```

### Step 7 — The Compound Output

```
AI-AUGMENTED CES — DELIVERABLE

INPUTS LOADED (proprietary, pre-AI):
- IVOC bank: [N quotes from M venues]
- Creative archive: [N tagged past ads]
- SOPs: [linked]
- Avatar: [defined]
- Strategic brief: [if Luke-stacked]

CES OUTPUT (AI-augmented throughput):
- Content Grid: [N Ideas × M Styles = X concepts]
- Hook bank: [Y hooks across 5 types]
- Vacation Test pass rate: [Z%]
- Production cycle target: [N concepts shipped per week]
- Weekly throughput vs manual baseline: [Xx faster]

OPERATIONS RUNNING:
- Asset tagging: automated
- Brief→script: AI-drafted, human-edited
- QA gate: AI-pre-check, human-final
- Performance tagging: automated
- Care Square ops: AI-augmented Results/Perception/Efficiency; Relationship stays human

QUALITY METRICS:
- Andromeda compliance rate: [%]
- IVOC traceability: [% of hooks/copy traceable to verbatim quote]
- Human edit rate: [% of AI-drafted briefs/hooks substantively edited]
  → If <40%, you're under-editing; reload "amplifier not generator" standard
  → If >80%, your AI prompts need refinement; AI not adding leverage

LEVERAGE METRIC:
- Hours saved per cycle vs manual CES: [X hrs]
- Hours reinvested into Strategy/Selling/System: [Y hrs]
```

---

## Content Type Adaptations

| Use case | Adaptation |
|---|---|
| **Single account, scaling production** | Full pipeline; AI does the "more of the same quality" lift |
| **Agency with multiple accounts** | Build agent stack ONCE, deploy across accounts; quarterly retune for account-specific IVOC |
| **Solo operator going from 5 to 50 ads/week** | Highest leverage — this workflow is what makes that jump possible |
| **Substack / newsletter operations (Farrice direct)** | Adapt: IVOC mining for newsletter audience; brief generation = edition-pitch generation; production = AI-drafted first drafts you edit; Care Square applies to subscriber relationships |
| **Authority work** | Adapt: AI handles content scheduling, post-tagging, engagement triage; YOU stay in voice + strategy + relationships |

---

## Output Requirements

- [ ] Loading order documented (proprietary inputs first, AI second)
- [ ] AI-augmented IVOC bank (with sample-verified verbatim quotes)
- [ ] AI-augmented brief generation output (with human-edit log)
- [ ] AI-augmented hook bank (with human-read sign-off)
- [ ] Production ops automation map (what's automated, what stays human)
- [ ] Care Square automation map
- [ ] Quality metrics table (Andromeda compliance, IVOC traceability, human-edit rate, leverage)

Deliverable: 6-12 pages PLUS the actual deployed workflow (n8n / Make / Zapier scenarios linked).

---

## Quality Gate

Apply Alex's bar PLUS the AI-loading-order principle:

- [ ] AI deployment ≥7 (proprietary inputs loaded BEFORE AI generation)
- [ ] All standard CES gates pass: Andromeda, IVOC, hook layering, system decomposability
- [ ] Human-edit rate is in the 40-80% sweet spot (under = under-editing AI slop; over = AI not adding value)
- [ ] Every shipped asset is traceable to proprietary inputs (not "AI made it up")

**Anti-pattern check** (Alex would reject):
- [ ] AI as research source (Claude chat = automatic rejection)
- [ ] AI-generated IVOC quotes (must be scraped verbatim, not synthesized)
- [ ] Hook bank with hooks AI invented from nothing — every hook traces to IVOC
- [ ] Care Square Relationship dimension automated (Relationship is human; only the surfacing of triggers is automated)
- [ ] System without human in the loop on creative QA (Vacation Test must be human-confirmed)

---

## Stacking

- **Prerequisite**: existing `/myatt-ces` output OR documented archive
- **Pairs with**: `/myatt-three-s` — quantify the time freed by AI augmentation; reinvest into Strategy/Selling
- **Cross-expert**: `agents/nick-saraev/` for the agentic build patterns (n8n / Make / browser automation)
- **Quality QA**: `/myatt-vacation-test` on every batch — AI doesn't replace this gate, it just makes the input bigger
- **Care Square**: the augmentation makes Care Square Efficiency dimension easy to score 9-10 across all accounts
