---
name: customer-truth-map
description: Replace guesswork with the customer's own words. The Customer Truth Map is a voice-of-customer system that gathers real, unedited customer language from where people already talk, cleans it to signal (verbatim, never paraphrased), organizes it into an empathy-map-derived map (Say / Think / Feel / Do + Pains / Gains), reframes pains into Jobs-to-be-Done, ranks the widest gaps, then runs copy, content, positioning, and offers through that map — and keeps it fresh as a living document. Use when copy "lands with a thud," when you're entering a new market or audience, when content keeps missing problems people actually have, when positioning feels assumed rather than evidenced, or when you need a reusable customer-reality document multiple deliverables can execute against. Wired to real tools (Apify Reddit, NotebookLM, Playwright, Recall, research) and composes /buyer-sourcer + /mcraney-deep-canvass; feeds /copy-engine + /novelty-forge.
expert: Blazing Zebra
domain: Voice-of-Customer — real-language mining, empathy mapping, Jobs-to-be-Done, gap analysis (the audience-truth layer)
version: "1.0"
workflows: 13
extracted_from: "PDF 'The Customer Truth Map' (13pp) + video GAVILEkfsvE (Blazing Zebra), 2026"
orchestrator: "/customer-truth-map"
tier: system
---

# Customer Truth Map — Voice-of-Customer, Organized

> **The customer's words are the gold; AI sorts the gold from the pebbles — organizing, never
> inventing.** Stop paying the guessing tax: gather exactly how customers describe their problems in
> their own words, organize those real words into one living map, and run everything you write
> through it. Load [genius.md](genius.md) before any workflow.

## Domain
The **audience-truth layer** that sits upstream of all copy/content/offer work: turn scattered,
unprompted customer language (the midnight one-star review, the frustrated forum thread, the
support email you forgot) into one organized, refreshable map of what your customer says, thinks,
feels, and does — and the pains and gains underneath. Every downstream skill assumes you know the
customer; this one *produces that knowledge from their real words.*

## Core Thesis
The hardest problem in business is the **canyon** between the person selling and the person who
needs it. Expertise makes it worse (the **curse of expertise** — you drift from the beginner's
words), so you pay the **guessing tax**: you invent the customer's problem in your language. The fix
is to listen instead of guess — unprompted talk beats surveys (a survey question pre-decides the
categories), and AI's one reliable job is organizing large messy piles of real language. The
**honesty spine**: organize real words, never manufacture them. Fabrication throws away the whole
advantage.

## Canonical Source
The expert's own guide is rendered faithfully at
[references/customer-truth-map-guide.md](references/customer-truth-map-guide.md) — the **primary
source of truth**; where any workflow or genius.md diverges, the guide wins. Verbatim prompts:
[references/prompt-library.md](references/prompt-library.md). Verbatim quotes:
[references/source-quotes.md](references/source-quotes.md). Lineage credited by the expert:
**Empathy Map** (Dave Gray/XPLANE), **Jobs-to-be-Done** (Christensen), **The Mom Test**
(Fitzpatrick).

## The Method (six phases)
1. **Gather** raw customer language (typos and all) from where they already talk.
2. **Clean** noise into signal — verbatim, word-for-word, no paraphrase.
3. **Build the map** — Say / Think / Feel / Do + Pains / Gains; name the patterns; circle the
   workarounds.
4. **Find the deeper job + the gaps** — pains → Jobs-to-be-Done; rank the widest gaps.
5. **Put the map to work** — copy, content, positioning, offers — all map-grounded.
6. **Triangulate + keep fresh** — merge sources by confidence; refresh quarterly; change-log as asset.

## Workflows (13)

### ★ Front Door — the conductor
| Workflow | Slash | What it does |
|---|---|---|
| `customer-truth-map` | `/customer-truth-map` (alias `/ctm`) | **End-to-end.** Cold start → finished, refreshable map → first map-grounded outputs. Orchestrates all 12 workflows below, grounded by Recall + memory, gated by the verbatim-integrity + quality rubric. Modes: BUILD · APPLY · REFRESH. |

### Tier 1 — Build the Map (the six phases)
| Workflow | Slash | What it does |
|---|---|---|
| `ctm-scope` | `/ctm-scope` | Phase 1.1–1.2: name 15–20 problems in the customer's voice, pick 2–3, find the exact communities + own-data sources. Grounds via Recall + `memory_facade.py`. |
| `ctm-gather` | `/ctm-gather` | Phase 1.3: **WIRED** raw-language collection — Apify Reddit → NotebookLM → Playwright (login-gated) → manual, + own-data ingest. Budget-gated with fallback chain. |
| `ctm-clean` | `/ctm-clean` | Phase 2: verbatim signal extraction (word-for-word, no paraphrase) + the verbatim-integrity gate. |
| `ctm-map` | `/ctm-map` | Phase 3: sort into Say/Think/Feel/Do + Pains/Gains, name 2–3 patterns each, flag vivid/repeated, circle the Do-category workarounds. |
| `ctm-jobs` | `/ctm-jobs` | Phase 4.1: reframe pains → JTBD ("When… I want… so I can…") + unconsidered angles. |
| `ctm-gaps` | `/ctm-gaps` | Phase 4.2: Pain/Job → Current Fix → The Gap (+ gap-width score); the widest-gap shortlist. |

### Tier 2 — Put the Map to Work (Phase 5)
| Workflow | Slash | What it does |
|---|---|---|
| `ctm-to-copy` | `/ctm-to-copy` | 10 quotes → slots (headline/subhead/objection/proof) + 8 headlines in the customer's register. Hands off to `/copy-engine`. |
| `ctm-to-content` | `/ctm-to-content` | 15 grounded content ideas (each with its source quote) + a long-form outline from the widest gap. Hands off to `/novelty-forge`, `/parallax`, `/diandra-*`. |
| `ctm-to-offer` | `/ctm-to-offer` | 3–5 positioning angles + 3 offer extensions tied to specific gaps (simple vs. major flagged). Hands off to positioning/BOS. |

### Tier 3 — Living + Surpass
| Workflow | Slash | What it does |
|---|---|---|
| `ctm-triangulate` | `/ctm-triangulate` | Phase 6 merge: multiple maps → Consistent Truths vs Source-Specific (confidence-labeled). |
| `ctm-refresh` | `/ctm-refresh` | Phase 6 freshness: quarterly pass / annual rebuild + dated change-log; schedulable via `/schedule`. |
| `ctm-deepen` | `/ctm-deepen` | **Surpass layer:** hand the map to `/mcraney-deep-canvass` (belief/resistance) + `/consumer-posture-profile` (identity) + the Step 5.5 Verification protocol — surface map → identity-level depth. |

## The Three Operating Modes (from the orchestrator)
| Mode | What it does | Entry |
|---|---|---|
| **BUILD** | Cold start → finished map (Phases 1–4) | `/customer-truth-map` BUILD |
| **APPLY** | Existing map → copy/content/offers (Phase 5) | `/customer-truth-map` APPLY |
| **REFRESH** | Existing map → updated + change-logged (Phase 6) | `/customer-truth-map` REFRESH |

## Stacking Guide (compose, don't reimplement)
This skill is the **audience-truth layer**. It calls research and feeds production:

| Stack with | When | Chain |
|---|---|---|
| `/buyer-sourcer` (luke-iha-avatar-machine) | scaled, source-traced VoC mining | `/ctm-gather` delegates the mine |
| `/mcraney-deep-canvass` | surface map → belief/resistance | `/ctm-deepen` |
| `/consumer-posture-profile` (consumer-posture-research skill) / dai-media | add identity/occupation/activity layer | `/ctm-deepen` |
| Verification protocol (Step 5.5) | any real-world claim riding with the language | gate before fact-bearing output |
| `/copy-engine`, `/ghostwrite`, master-copywriter | map → finished copy | `/ctm-to-copy` |
| `/novelty-forge`, `/parallax`, `/diandra-*` | map → finished content | `/ctm-to-content` (supplies held belief + real language) |
| `/build-bos`, positioning skills | gaps → positioning/offer | `/ctm-to-offer` |
| `/schedule` | make the quarterly refresh a real recurring job | `/ctm-refresh` |

**Common sequences:**
- `/customer-truth-map` (full arc)
- `/ctm-scope → /ctm-gather → /ctm-clean → /ctm-map → /ctm-jobs → /ctm-gaps` (build)
- `/ctm-map → /ctm-deepen` (surface → identity-level depth)
- `/ctm-gaps → /ctm-to-offer` (widest gap → offer)
- run the build across 2+ communities → `/ctm-triangulate` → `/ctm-refresh` quarterly

## Quality Rubric (full version in [genius.md](genius.md) / [references/quality-rubric.md](references/quality-rubric.md))
**Verbatim Integrity is the veto** — any fabricated or paraphrased customer quote is an automatic
fail, regardless of the rest. Then: Unprompted Sourcing · Narrowness · Map Completeness ·
Do-Category Mining · Job Depth · Gap Ranking · Put-to-Work Fidelity · Freshness Discipline. Score
1–10; name the anchor for any score ≥8.

## File Map
```
skills/customer-truth-map/
├── SKILL.md                          ← You are here
├── genius.md                         ← IP anchor (12 patterns, 8 hidden, 7 moves, 3 exemplars, 9-criterion rubric)
├── references/
│   ├── customer-truth-map-guide.md   ← CANONICAL SOURCE (the expert's guide; primary truth)
│   ├── prompt-library.md             ← expert's 6-phase prompts (verbatim) + enhanced/wired versions
│   ├── source-quotes.md              ← verbatim expert anchors
│   ├── genius-patterns.md            ← 12 executable patterns (expanded)
│   ├── hidden-knowledge.md           ← 8 tacit insights (expanded)
│   ├── tool-wiring.md                ← exact gather invocations + budget gates + fallback chains
│   ├── cross-domain-adaptations.md   ← the map → 8 verticals/asset types (domain-agnostic key)
│   ├── quality-rubric.md             ← 9-criterion scoring instrument (anchors at 3/6/9)
│   └── worked-exemplar-jen-fthb.md   ← a REAL worked map (first-time-homebuyer audience)
└── workflows/
    ├── customer-truth-map.md         ← ★ FRONT DOOR — end-to-end conductor (BUILD · APPLY · REFRESH)
    ├── ctm-scope.md                  ← Tier 1
    ├── ctm-gather.md                 ← Tier 1 (wired)
    ├── ctm-clean.md                  ← Tier 1
    ├── ctm-map.md                    ← Tier 1
    ├── ctm-jobs.md                   ← Tier 1
    ├── ctm-gaps.md                   ← Tier 1
    ├── ctm-to-copy.md                ← Tier 2
    ├── ctm-to-content.md             ← Tier 2
    ├── ctm-to-offer.md               ← Tier 2
    ├── ctm-triangulate.md            ← Tier 3
    ├── ctm-refresh.md                ← Tier 3
    └── ctm-deepen.md                 ← Tier 3 (surpass layer)
```

**Source:** Blazing Zebra, "The Customer Truth Map" (PDF) + "Master TARGETED Market Research… with
NotebookLM" (`youtube.com/watch?v=GAVILEkfsvE`) — transcript at
`extractions/customer-truth-map/transcript.txt`. Standalone skill that composes the existing
VoC/belief/posture stack.
