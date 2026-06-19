---
name: writing-depth-layer
description: >-
  Deepen any work — add depth, resonance, soul, truth, and voice across social,
  marketing, copywriting, and books. A cross-cutting craft-depth orchestration
  layer that does NOT re-teach craft: it diagnoses what depth is missing, then
  composes existing craft experts (Hawley, Roth, Connelly, Cole, Pressfield,
  Lamott-Allen, Fareed, platform experts) in the right order and dose, and
  returns a deepened draft plus a change-map ("Depth Receipt"). Trigger words:
  deepen, depth, resonance, "make this land", more human, more soul, more voice,
  less generic, less AI. Do NOT use for: pure speed copy (use /copy-engine),
  formatting/structure-only tasks, or research synthesis (use execution/research.py).
expert: "Writing Depth Layer (conductor over the craft roster)"
domain: "Cross-cutting Writing Depth x Composition x Reader Impact"
version: "1.0"
format: "completion-engine"
workflows: 12
tier: system
---

# Writing Depth Layer

A draft can be finished and still be dead. It has all its limbs — a hook, a structure, a CTA — and none of its blood. The Depth Layer is not another writer; it is the conductor who walks in after the draft exists, finds the one or two places where the work is hollow, defended, or generic, and brings in exactly the right craft experts — in the right order, at the right dose — to make it land. It returns the deepened draft and a short receipt of what it changed and why. It never re-teaches craft. It composes the people who already own it.

## Role

The Depth Layer is a cross-cutting orchestrator that DEEPENS any existing draft — social post, ad, marketing page, book chapter, client memo — by diagnosing which kinds of depth are missing and composing the craft roster to supply them. It owns no craft of its own. Its intelligence is composition: *what is hollow here, who fixes that, in what order, and how much.* The output reads more honest, clearer, warmer, more specific, and less defended — and it never reads like a stack of techniques.

## Core Thesis

A real writer "cares more about the sentence than the content" (Lamott + Allen). Good writing earns the reader twice: plain, vivid, economical craft earns the *next sentence*; compassion plus hard truth plus heart earns the reader's *trust*. The Depth Layer exists because most drafts fail the second earning — they are competent and hollow. Deepening is therefore not lengthening. Deepening often means cutting. The test is never "is this comprehensive?" — comprehensive is failure. The test is: does it land?

### The 8 Depth Deficits (the diagnostic taxonomy — every audit scores these)

| # | Deficit | Owner(s) |
|---|---------|----------|
| 1 | **No architecture** — events but no spine/theme/reason-this-exists | Hawley (theme / ending-first) |
| 2 | **Hollow / generic** — abstract, could-be-anyone, no concrete stakes | Connelly telling-detail + Lamott-Allen specificity |
| 3 | **Emotionally unearned** — sentiment asserted not earned (melodrama OR flatness) | Lamott-Allen really-real + Roth erosion |
| 4 | **No signature voice** — sounds like AI/anyone; no rhythmic fingerprint | voice-as-music + ghostwriting-voice-engine + Cole |
| 5 | **Over-explained / bloated** — proves what's already trusted; 25–30% cuttable | Lamott-Allen economize + Cole compression + Roth erosion |
| 6 | **Weak rhythm** — monotone length, no cadence, fails read-aloud | Cole sentence craft + Lamott-Allen read-aloud |
| 7 | **Missing telling detail** — tells instead of shows; no concrete image | Connelly + Roth visual prose |
| 8 | **No reader trust** — confusing, unfair, throat-clearing, fake closure | Lamott-Allen reader-trust |

### The Ordering Law (non-negotiable)

Architecture FIRST → structure/scene → line/rhythm → truth/voice LAST.

> Hawley (spine) → Roth/Connelly (scene + detail) → Cole + Lamott-Allen technical-craft (line/rhythm) → Lamott-Allen really-real (truth) + voice-as-music (voice).

Inverting the order — line-craft before architecture — yields well-crafted sentences with no spine. **Architecture first, always.**

### The Deepen Loop (how every rewrite workflow runs)

1. **DIAGNOSE** — score the draft on the 8 deficits; name the 1–3 weakest links. Diagnose before treating. Never refine slop on a misdiagnosed draft.
2. **SELECT + ORDER** — pick only the owners for *confirmed* deficits; sequence by the Ordering Law; set the dose by vertical.
3. **APPLY** — load each owner's `genius.md` (+ the specific workflow) and apply the move *into* the prose. Preserve the user's core meaning and voice.
4. **RECEIPT** — end with a Depth Receipt.

### Depth Receipt Format (always end rewrite/inject workflows with this)

- **Weakest link found:** `<deficit>`
- **Moves applied:** for each — `<deficit fixed>` → `<move in plain craft terms>` → `<expected reader effect>` → `<source principle>`
- **Dose / vertical fit:** `<why this dose for this vertical>`
- **Remaining risk:** `<what still could fail>`

Do NOT name-drop experts inside the deepened prose itself; integrate moves invisibly. Experts are named only in the Receipt.

## Use When / Do Not Use

**Use when** — a draft already exists and the ask is to make it land: "deepen this," "add depth/resonance/soul/truth/voice," "make this more human," "more soul," "more voice," "less generic," "less AI," "this feels flat," "it's competent but hollow." Works across social, copy, marketing/brand, book/long-form, and client/personal-brand verticals.

**Do not use for:**
- **Pure speed copy** — first-draft converting copy from cold start → `/copy-engine`.
- **Formatting / structure-only** — layout, headers, scannability with no depth deficit.
- **Research synthesis** — gathering or verifying facts → `execution/research.py`.

Also do not full-rewrite when the user asked for diagnosis only (`/depth-audit`), and do not full-rewrite when a surgical single-move inject (`/depth-inject`) would do.

## Workflow Table

### Tier 1 — Foundation (entry points)

| Command | Workflow | Produces |
|---------|----------|----------|
| `/deepen` | `deepen.md` | Deepen (Flagship Orchestrator) — runs the full Deepen Loop on any draft: auto-detect vertical, diagnose, select + order owners, deepened draft + Depth Receipt. |
| `/depth-audit` | `depth-audit.md` | Depth Audit (Diagnosis Only) — scores the 8 deficits, names the 1–3 weakest links, recommends owners + order. No rewrite. |
| `/depth-stack` | `depth-stack.md` | Depth Stack (Maximum-Depth Pipeline) — full ordered pass through every applicable owner for highest-stakes work; layered deepening + full Receipt. |

### Tier 2 — Practitioner (per-vertical orchestrators)

| Command | Workflow | Produces |
|---------|----------|----------|
| `/depth-social` | `depth-social.md` | Depth — Social — light, fast deepening that preserves hook/brevity/scannability; calls `/really-real-social` as the truth slot. |
| `/depth-copy` | `depth-copy.md` | Depth — Converting Copy — depth without losing conversion; offer/CTA/proof/clarity intact; calls `/really-real-marketing` as the truth slot. |
| `/depth-marketing` | `depth-marketing.md` | Depth — Marketing / Brand Media — humanity + specificity + belief (Sutherland reframe + Roth); calls `/really-real-marketing` as the truth slot. |
| `/depth-book` | `depth-book.md` | Depth — Book / Long-Form — full layered stack, architecture-led (Hawley); calls `/really-real-book` as the truth slot. |
| `/depth-client` | `depth-client.md` | Depth — Client / Personal Brand — trusted advisory prose, argument architecture (Fareed) + restraint; calls `/really-real-client` as the truth slot. |
| `/depth-inject` | `depth-inject.md` | Depth Inject (Surgical Single-Move) — fixes exactly one named deficit with one owner; minimal-touch rewrite + Receipt. |

### Tier 3 — Craft / Stacking (specialist layers)

| Command | Workflow | Produces |
|---------|----------|----------|
| `/depth-line` | `depth-line.md` | Depth — Line-Level Craft — sentence rhythm, compression, cadence, read-aloud pass (Cole + Lamott-Allen technical-craft). |
| `/depth-voice` | `depth-voice.md` | Depth — Voice (Voice-as-Music) — installs a rhythmic fingerprint so prose stops sounding like AI/anyone (voice-as-music + ghostwriting-voice-engine). |
| `/depth-gate` | `depth-gate.md` | Depth Gate (Composition Decision-Tree) — given a draft + intent, returns *which* depth workflow to run and *which* owners to compose, in order. |

## Stacking Guide — how it composes the craft roster

The Depth Layer never reimplements craft. Each deficit has an OWNER; the layer loads that owner's `genius.md` and the named workflow, then applies the move into the prose. The truth slot is ALWAYS delegated to the matching `/really-real-*` pass — the layer calls it, never reimplements it.

| Owner | Skill path (verified) | Composed for | Representative commands |
|-------|----------------------|--------------|-------------------------|
| **Noah Hawley** | `skills/noah-hawley-storytelling-mastery` (`genius.md`) | Deficit 1 — architecture / spine / theme. Runs FIRST. | `/hawley-theme-engine`, `/hawley-ending-first`, `/hawley-voice-bible`, `/hawley-velocity-draft`, `/hawley-content-season` |
| **Eric Roth** | `skills/eric-roth-writing-mastery` (`genius.md`) | Deficits 3, 5, 7 — erosion (cut), visual prose, earned emotion. | `/visual-prose-for-copy`, `/content-erosion-protocol`, `/memorable-hooks-forge`, `/social-subtext-engine`, `/theme-driven-content-strategy` |
| **Michael Connelly** | `skills/michael-connelly-vivid-writing` (`genius.md`) | Deficits 2, 7 — telling detail, show-don't-tell, momentum. | `/telling-detail-engine`, `/slingshot-opener`, `/subtext-dialogue-builder`, `/momentum-audit`, `/connelly-rewrite-protocol` |
| **Nicolas Cole** | `skills/nicolas-cole-sentence-craft` (`genius.md`) | Deficits 5, 6 — compression, density, terminal rhythm. | `/atomic-compression-density-audit`, `/audience-calibration-vocabulary-control`, `/terminal-power-rhythm-engineering` |
| **Steven Pressfield** | `skills/steven-pressfield-narrative-mastery` (`genius.md`) | Deficit 1 (narrative spine) + resistance / manifesto force. | `/narrative-architecture-blueprint` (01), `/hook-mystery-architecture` (04), `/resistance-warfare` (08), `/manifesto-engine` (13), `/narrative-diagnostic` (14) |
| **Lamott + Allen (really-real)** | `skills/lamott-allen-really-real-writing` (`genius.md`) | Deficits 2, 3, 5, 6, 8 + **the truth slot** (`/really-real-*`). Technical-craft KNOWLEDGE lives here only. | `/really-real-audit`, `/really-real-rewrite`, `/really-real-reader-trust`, `/really-real-social`, `/really-real-marketing`, `/really-real-client`, `/really-real-book` |
| **lamott-craft (Lamott solo)** | `skills/lamott-craft` (`genius.md`) | Deficits 2, 3 — ABDCE structure, anti-literary filter, observation. | `/abdce-structure`, `/three-draft-system`, `/anti-literary-filter`, `/dialogue-craft`, `/observation-pipeline` |
| **Fareed Zakaria** | `skills/fareed-zakaria-writing-mastery` (`genius.md`) | Client/advisory argument architecture + authority voice. | `/high-stakes-argument-architecture`, `/public-intellectual-voice-narrative`, `/strategic-authority-positioning`, `/multi-medium-content-multiplication` |
| **Lara Acosta** | `skills/lara-acosta-linkedin-mastery` (`genius.md`) | Social platform-native shape, voice scaling. | `/high-performance-content-engine`, `/personal-brand-blueprint`, `/ghostwriting-voice-scaling-system`, `/revenue-authority-accelerator` |
| **Kallaway** | `skills/kallaway-word-mastery` (`genius.md`) | Deficits 4, 6 — grip/tension, charisma, vulnerability architecture. | `/opening-sentence-forge`, `/grip-and-tension-engine`, `/rhythm-rewrite`, `/charisma-engineering`, `/vulnerability-architecture` |
| **Diandra Escobar** | `skills/diandra-escobar-linkedin-growth` (`genius.md`) | Social hook / save-worthiness / format. | `/linkedin-writing-engine` (09), `/first-50-hook-rewriter` (17), `/save-worthy-content-architect` (18), `/five-format-hook-architect` (20), `/ai-optimized-headline-engineer` (16) |
| **ghostwriting-voice-engine** | `skills/ghostwriting-voice-engine` (`genius.md`) | Deficit 4 — capturing and reproducing a real human voice. | `/voice-capture` (01), `/content-production` (02), `/unsolicited-demo` (03) |
| **Rory Sutherland** | `skills/rory-sutherland-marketing` (`genius.md`) | Marketing/brand — belief, conspiratorial reframe, perception. | `/behavioral-copy-audit`, `/conspiratorial-reframe-engine`, `/consumer-perception-alchemy`, `/reverse-benchmarking-audit`, `/perception-metric-reframe` |

**Per-vertical dosing** (the layer sets dose before applying):

- **SOCIAL** (LinkedIn/X/IG/newsletter short) — LIGHT + FAST. Fix 1–2 deficits max. Preserve hook, brevity, scannability, platform-native shape. Truth slot = `/really-real-social`. Never over-deepen a 150-word post into an essay.
- **COPY** (ads/VSL/landing/email/offers) — depth WITHOUT losing conversion. Offer logic, CTA, proof, clarity-to-action stay intact; add conviction, specificity, voice. Truth slot = `/really-real-marketing`. Literary flourish never beats clarity-to-action.
- **MARKETING / BRAND** — humanity + specificity + belief. Sutherland reframe + Roth. Truth slot = `/really-real-marketing`.
- **BOOK / LONG-FORM / NOVEL** — full stack, deep, layered. Architecture (Hawley) matters most here. Scene = Connelly/Roth. Truth slot = `/really-real-book`.
- **CLIENT / PERSONAL-BRAND** — trusted advisory prose. Argument architecture (Fareed) + restraint + credibility. Truth slot = `/really-real-client`.

## Composition Rule + Anti-Duplication

**Composition Rule.** The Depth Layer always COMPOSES an owner; it never duplicates one. For any confirmed deficit, find the owner in the Stacking Guide, load that owner's `genius.md` + the named workflow, apply the move, and credit it only in the Receipt. If no owner exists for a "deficit," it is not a depth deficit the layer handles — surface it, do not invent craft.

**Anti-Duplication Contract (critical):**
- The per-vertical `/depth-*` workflows are FULL-STACK orchestrators (architecture + craft + truth, dosed per vertical) that CALL the single-layer `/really-real-*` passes as their truth slot. They MUST NOT re-implement `/really-real-*`.
- Technical sentence-craft KNOWLEDGE lives ONLY in `skills/lamott-allen-really-real-writing` (the expanded technical-craft module). The Depth Layer ORCHESTRATES it; it does not copy it.
- `genius.md` of `writing-depth-layer` is composition/routing intelligence ONLY — zero craft re-teaching.

**Anti-Patterns (the layer would never):**
- Produce "comprehensive" output. Comprehensive = failure. Deepen is not lengthen — deepening often means CUTTING.
- Crowd the prose with named experts or visible technique labels.
- Manufacture trauma, false vulnerability, or sentiment the draft has not earned.
- Sacrifice function (conversion, clarity, platform fit) for "literary" feel.
- Rewrite when the user asked for diagnosis only, or full-rewrite when a surgical inject would do.
- Re-implement craft an owner already does — always COMPOSE the owner, never duplicate it.

## Quick Reference

- **Composition / routing intelligence:** `skills/writing-depth-layer/genius.md` (the 8-deficit diagnostic, the Ordering Law, the dosing model, the routing map — no craft re-teaching).
- **References:**
  - `skills/writing-depth-layer/references/depth-deficit-taxonomy.md` — the 8 depth deficits with detection signals, severity rubric (0/1/2), and owner map.
  - `skills/writing-depth-layer/references/routing-map.md` — deficit → owner → verified-path → real-command mapping, plus the Ordering Law (architecture → scene/detail → line/rhythm → truth/voice) and why inverting it fails.
  - `skills/writing-depth-layer/references/vertical-dosing.md` — per-vertical dose tables (social/copy/marketing/book/client), deficits-that-matter-most-per-vertical priors, truth-slot bindings, and function to preserve.
  - `skills/writing-depth-layer/references/composition-guide.md` — 3 worked end-to-end examples (flat LinkedIn post → diagnosis → chain → deepened + Receipt; flat copy → same; flat memoir paragraph → same).
