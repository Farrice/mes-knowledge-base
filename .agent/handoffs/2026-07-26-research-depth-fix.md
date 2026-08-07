---
thread: research-depth-fix
status: ready
resume_hint: Promote the RECON-GRADE corpus: verify phase + synthesis on .tmp/research/offer-validation-deep/, then gate and finalize with --depth-receipt
unfinished: Corpus unverified (finder-labeled); 3 external deep-research runs not back; Josh testimonial unsent; /cos weekly 14d overdue
branch: main
pin: true
---

# Research Depth Fix — Shallow Work Made Physically Impossible + Offer Re-Derivation

**Date:** 2026-07-26 · **Thread:** research-depth-fix · **Status:** ready

## What this session was

Started as `/cos` daily and turned into the session that fixed the system's most dangerous defect: shallow research shipping as trusted insight. Farrice caught a 12-agent offer-rederivation swarm doing snippet-depth work and said it "almost crushed my hopes and thoughts of my intuition." He demanded the root cause AND a systemic fix, because Claude Code is becoming his home base and the tooling has to be trustworthy enough to move fast on.

## Completed

**1. COS daily + outer loop drained.** Board sat (Greene/Welsh/Orlean, all three independently converged on "ship what already exists"). All 20 outcome check-ins closed — due list 25 → 5. Josh 6Eight settled at $250 collected; lifetime $4,400 → $4,650. Testimonial Capture Kit built (`_active/farrice-brand/proof/`). Father-son training block added to the JJ playbook, gated on his tooth recheck. Health goal recommitted; all 4 life-context sections restamped.

**2. Offer direction re-derived through a grill.** Killed the stale offer backlog with him. Landed: creative strategist lane · POV = "AI is an extension of us, against both the fear camp and the hype camp" (his words, his moat) · teardown-first content engine (his perfectionism fires on self-exposure, never on production — design around it) · funded DTC primary, AI-forward B2B SaaS second · copy is the craft inside the deliverable, never the product on the invoice. CoWork Diandra bundle imported and harmonized (separate skill, zero command collisions, routing disambiguated).

**3. THE FIX — research stack, 8 changes, all verified.** `execution/research_depth.py` (new single depth contract) · `tavily_extract` wired into the floor (was dead code, zero callers) with snippets counting half · DEGRADED at deep/max now exits 2 with `acceptable:false` · verification scaled to ALL load-bearing claims by independent refuters (was top 6-8, self-labeled) · gap rounds standard=1/deep=2/max=3 (standard had zero) · Playwright primary-source lane · `research_quality_gate.py --depth --receipt` binds ANY artifact from any origin · `chain_runner finalize --depth-receipt` caps Factual Grounding at 6 without a passing receipt · docs reconciled.

**4. Proof, then stopped on his instruction.** Measured 296 sources / 155 domains vs round 1's 87/79. Playwright read the live Meta Ad Library (13 brands at 15+ active ads, Omni Creatine ~750) and re-verified CREVARI's $1,000 teardown verbatim. The old shallow artifact now FAILS the new gate at exit 1. Stopped before the 20-agent verify phase to stay proportional.

**5. Self-correction published.** Measuring the incident disproved my own diagnosis: round 1 was not source-poor (87 sources), its real failure was that ZERO of those URLs survived into the decision artifact. Corrected in `DEPTH-FIX-PROOF.md` rather than kept as the tidier story.

## Remaining priority

Promote the 234KB research corpus at `.tmp/research/offer-validation-deep/` to decision-grade: run only the verify phase + synthesis on what already exists, gate the report, finalize with `--depth-receipt`. It is honestly labeled RECON-GRADE right now because the verify phase never ran — do not make the offer call on it as-is.

## Unfinished

- Corpus is RECON-GRADE (finder-labeled claims, no independent verification round)
- Farrice's three external deep-research runs (Gemini/Perplexity/Claude) not yet returned — diff table owed when they land
- Josh testimonial not yet sent (drafts ready, goodwill window open)
- Katie body-fat + measurements owed
- JJ tooth recheck was Monday 2026-07-27 — ask
- `/cos weekly` 14 days overdue

## Core context to load

- `docs/solutions/2026-07-26-shallow-research-passed-as-trusted.md` — the five-failure autopsy + re-solve guard
- `_active/offer-strategy/offer-rederivation-2026-07-25/04-deliverables/DEPTH-FIX-PROOF.md` — measured proof + the correction
- `_active/offer-strategy/offer-rederivation-2026-07-25/04-deliverables/DEEP-RESEARCH-PROMPT.md` — the paste-ready external prompt
- `execution/research_depth.py` — the contract every research floor now reads

## Hot experts this session

Chief of Staff OS · Robert Greene · Justin Welsh · Susan Orlean · Luke Iha (client mastery) · Eugene Teo · Mark Kashef (Wargame OS) · Diandra Escobar (mastery, imported)

## Operator lesson

When you accuse your own system of a failure, measure the accusation first. The real defect sat one layer deeper than the one I was confident about, and confidence would have shipped the wrong fix.
