---
name: kieran-content-intelligence-system
description: >-
  Build and run a compounding content ideation system - 7 practitioner capabilities that PRODUCE finished deliverables so you never run out of content ideas. Use for: content ideas and what to post next; audience profiles built for reaction rather than qualification (explicitly not an ICP); extracting winning patterns from your own performance data; trend research with saturation scoring; building and pruning a content queue or calendar; deep-dive research and craft-ready outlines; monthly refresh that re-ranks patterns and updates context files. Also use when AI content keeps coming out generic and they want to know why. Trigger on content ideas, ideation, what should I post, out of ideas, never run out of ideas, audience profile, not an ICP, winning patterns, performance data, content queue, content backlog, trend research, market signals, saturation, research dossier, content outline, monthly refresh, compounding content system, or why does my AI content sound generic.
license: Extracted from public source material and architected as practitioner prompts. Deploy freely.
routing: long-tail
---

> **Provenance:** Imported from Cowork 2026-09-01 (Fresh's exported skills package).
> **Routing (added on import).** Component skill — its 7 Crown Jewels are merged into
> the flagship `kieran-flanagan-content-intelligence`. Load the flagship unless you
> need this file's tighter 7-capability surface.

# KIERAN FLANAGAN — CONTENT INTELLIGENCE SYSTEM
### The compounding ideation engine · 7 Crown Jewel capabilities
*MES 3.0 + Skill Download OS*

**Every capability PRODUCES a finished deliverable.** None teach. You provide context, the capability executes, you receive an artifact.

---

## ⚠️ THE FIREWALL — read before running anything

This system works because of **where the boundary between AI and human sits.**

**Upstream** — recoverable from the world, therefore delegable: audience research, pattern extraction, market signal, ideation, research, outlining.
**Downstream** — unrecoverable, therefore owned: every published sentence, which analogy gets used, what is funny, what the user will stake their reputation on.

**The seam is outline-to-draft.** You hand over a fully-loaded outline. The user writes the prose.

> *"I do not use my system to create finished pieces of content. I do not copy and paste from AI."*

**When CJ-6 says the deliverable is an outline, do not draft prose** — not a polished version, not a rough pass "to get them started," not the first two paragraphs as a favour. If AI-assisted output starts reading as generated, the firewall has drifted. Hold it.

---

## ROUTING

| Request sounds like | Load |
|---|---|
| "who is my audience" · "build an audience profile" · "my content feels generic" | `prompts/cj-1-audience-profile-forge.md` |
| "what works for me" · "analyze my best posts" · "find my patterns" | `prompts/cj-2-winning-patterns-extractor.md` |
| "what's trending" · "market signals" · "is this topic saturated" | `prompts/cj-3-trend-upside-scanner.md` |
| **"give me content ideas"** · "what should I post" · "I'm out of ideas" | `prompts/cj-4-triangulated-idea-engine.md` ⭐ |
| "organize my ideas" · "content calendar" · "my queue is a mess" | `prompts/cj-5-content-queue-operating-system.md` |
| "research this idea" · "outline this" · "build me a dossier" | `prompts/cj-6-deep-dive-research-outline-builder.md` |
| "how did last month go" · "update my system" · "monthly review" | `prompts/cj-7-refinement-compounding-loop.md` |

**Load the file and follow it exactly.** Each runs cold — none requires another to have been run first. When context is missing, each builds a labelled working version inline rather than degrading.

`reference/extraction-report.md` holds the full methodology — 18 decoded patterns and the four-level progression. Read it when extending the system or when the user asks *why* something works.

---

## COMMANDS

`/ideas [topic]` → CJ-4 · `/profile [audience]` → CJ-1 · `/patterns [platform]` → CJ-2 · `/signals [domain]` → CJ-3 · `/queue` → CJ-5 · `/dossier [idea]` → CJ-6 · `/refresh` → CJ-7

**`/week [operator]`** — CJ-3 → CJ-4 → CJ-5 → CJ-6 on the top idea. One command: a week planned, one piece research-ready.
**`/foundation [operator]`** — CJ-1 → CJ-2. The two assets everything else reads from.

---

## OPERATING PRINCIPLES

**1 · Patterns, not topics.** Map ideas to structural shapes that have worked, never to subject matter. Topics decay in weeks; patterns compound for years.

**2 · Triangulate before spending craft.** Write only where three signals converge — **proven** (a format that works for this operator), **trending** (live demand with a real analog), **owned** (a genuine defensible position). Score all three, show the components, never just the total.

**3 · Audience profile ≠ ICP.** An ICP optimizes for qualification. An audience profile optimizes for *reaction*. Feeding an ICP into a content system is the most common root cause of generic output.

**4 · Label every inference. Never invent a number.** Missing context → build a working version inline, mark it `INFERRED`, cap its confidence. Never present a recalled figure as observed, an unverifiable source as verified, or a target as a research finding. A statistic you cannot source discredits everything around it.

**5 · Grade confidence, including downgrades.** Refresh cycles record what got *less* certain, not only what improved.

**6 · Overstock, then prune hard.** Ideas are cheap. Selection under surplus beats generation under scarcity. Kill without deliberation.

**7 · Track the first derivative.** A #1 pattern declining two months running is a worse bet than a #4 climbing.

**8 · The corpus is the moat; the prompt is commodity.** Everyone has the same models. Almost nobody has a structured year of their own performance data.

---

## THE 30-DAY PATH

**Day 1 (90 min)** — `/profile` → `/patterns` on the last 30 posts → `/signals` → `/ideas`. Three context assets and ten grounded ideas.
**Week 1** — `/queue`, then `/dossier` on the two strongest. **The user writes them.** Publish.
**Weeks 2–3** — Publish from the queue, never from a blank page.
**Day 30** — `/refresh`. **This is where compounding starts.**

**Say this honestly if the user asks about payoff**: week one is *worse* than ad-hoc prompting — setup costs time, assets are thin. Break-even around week three. Materially better by month three. Not comparable by month twelve.

---

## AUTOMATION

Schedule `/signals` weekly — a fresh saturation-scored report every Monday means never starting a week from nothing. Highest-value automation here.
Schedule `/refresh` monthly — least gratifying, highest compounding return, therefore the one that gets skipped. Put it on a clock.

**Automate up to the firewall. Never across it.**

---

## STACKING

Pairs directly with **`kieran-content-domain-arsenal`** — this system decides *what* to make; that arsenal executes copy, positioning, storytelling, virality, and creative direction. Hand a CJ-6 dossier straight to the arsenal's copy engine.

Also stacks with any platform-native execution skill (this supplies ideation and research; that supplies distribution), and with a comedy system — which closes the one gap the source expert names explicitly and cannot fill: *"it never really does a good job of finding the funny ideas."*

---

*MES 3.0 + Skill Download OS — Extract. Download. Deploy. Surpass. Transcend.*
