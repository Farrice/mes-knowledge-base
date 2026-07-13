---
description: Two-axis deliverable review — Voice ∥ Brief — run as parallel subagents and reported side by side, never merged. Use before delivery on any taste-bearing or client-facing deliverable.
tier: system
---

# /two-axis-verify — Voice ∥ Brief

Adapted from Matt Pocock's two-axis `/code-review` (Standards ∥ Spec). The structural insight: a piece can nail the voice and miss the brief, or deliver the brief in a voice that isn't yours — **merging the axes lets one mask the other**, so they run as parallel subagents and report separately.

## Axes

- **Voice** — does the piece conform to the *documented* voice and craft standards? Sources: `_active/farrice-brand/voice/VOICE-CARD.md` + active dial mode (or the client's CLAUDE.md/voice card for client work), `directives/ai-slop-ban-bank.md`, plus the content-smell baseline below.
- **Brief** — does the piece faithfully deliver the originating intent? Sources: the brief/spec/sharpened intent, the felt-standard quotes if a Translation Card exists.

## Process

1. **Pin the inputs**: deliverable path + brief source. If the brief is missing, ask for it; if none exists, the Brief subagent reports "no brief available" — it never reconstructs one.
2. **Deterministic layer first**: `python3 execution/prose_classifier.py check <file>` — paste its hits into the Voice subagent prompt so the model layer starts where the deterministic layer stopped.
3. **Spawn both subagents in parallel** (one message, two Agent calls; Sonnet-tier is right — this is executor work).
   - *Voice prompt*: the piece + voice sources + smell baseline pasted in full (the subagent has no other access to it) + brief: "Report every violation: cite the rule (file + line where possible). Distinguish hard violations (documented bans) from judgment calls (baseline smells — a documented standard overrides the baseline). Under 400 words."
   - *Brief prompt*: the piece + the brief + brief: "Report: (a) asks that are missing or partial; (b) content nobody asked for (scope creep); (c) asks that look delivered but miss the intent. Quote the brief line for each finding. Under 400 words."
4. **Aggregate** under `## Voice` and `## Brief`, verbatim. Never merge or rerank across axes; close with one line — findings per axis, worst issue *within* each axis.
5. **Feed Chain Step 6**: Voice findings inform the Expert Standard score; Brief findings inform Intent Alignment. Hard Voice violations = fix before delivery, same as a Factual Grounding veto.

## Content-smell baseline

Judgment calls, named as leading words — the documented ban bank overrides. Each smell: what it is → the fix.

- **Template slop** — a structure a thousand posts share, filled in. → rebuild from the piece's one specific insight.
- **Twin-sentence ending** — the paired short-sentence closer stamping "profundity." → end on an image, declaration, or bookend.
- **Triple anaphora** — three lines opening with the same phrase. → keep one, vary or cut the rest.
- **"It's not X. It's Y."** — the contrast-reveal tic. → state Y plainly with its evidence.
- **Phantom research** — a claim with no source behind it. → verify (VERIFIED/LIKELY/UNCONFIRMED) or cut.
- **Comprehensive-itis** — coverage where a single truth was asked for. → cut to the one thing and its proof.
- **Generic question signoff** — "What do you think?" engagement bait. → image, declaration, or bookend close.
- **Hedge stack** — qualifiers stacked until the claim dissolves. → commit or cut the claim.
- **Terminology echo** — parroting the brief's own words back instead of the *thinking* behind them. → their thinking, not their terminology.
- **Prose blob** — a client asset delivered as paragraphs where a production sheet was the format. → per-asset labeled cards (DOC-FORMAT-SPEC).

## When

Client-facing deliverables (binding: implementation-grade always), taste-bearing brand pieces before publish, and any deliverable where Step 6 scored <7 once already. Skip for internal scratch and system artifacts.
