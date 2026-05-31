---
description: Run Diandra's full LinkedIn production line on a draft in one pass — save-architecture (conditional) → format-validated hook → AI-retrieval-signal confirmation → publish-ready post with receipts.
---

# `/diandra-post-finisher` — Post Finisher (production line in one command)

Composes three workflows so a draft body comes out the other side publish-ready: made save-worthy where it should be, fitted with the strongest format-validated hook, and confirmed to carry AI-retrieval signal. One invocation instead of three.

## When to Use
- You have a drafted post body and want it finished to ship
- You don't want to run workflows 18, 20, and 17 separately and reconcile them by hand
- Any post going out under your name or a client's where the hook actually matters

## Usage
```
/diandra-post-finisher "[paste the draft body]" --bucket [Growth|Authority|Conversion|Personal] --media [none|image|video|carousel|data-viz] --register [formal|informal]
```
Body-first only — if you have just a topic, run `/diandra-hook-architect` Path B or the writing engine (workflow 09) first.

## What It Does (dependency-correct order)
1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` + format library + 40 rules
2. **Reads**: `workflows/22-post-finisher.md`
3. **Phase 0 — Classify**: bucket, save-worthiness, media, register
4. **Phase 1 — Body** (conditional, workflow 18): restructure for saves + visual brief — *only if Authority or teaching/data Growth*
5. **Phase 2 — Hook** (workflow 20, authoritative): 8-10 validated hooks on the FINAL body → winning hook + top 3
6. **Phase 3 — Signal** (workflow 17, confirmation): does the winner carry AI-retrieval signal? Adjust within the limit or defer to sentence two
7. **Phase 4 — Assemble**: finished post + receipts (hook format/chars/gap, save trigger, AI-signal status, why-it-works)

## Why the order is body → hook → signal (not 20→17→18)
Body-first (Pattern 6): you mine the hook from the *final* body, and workflow 18 rewrites the body. So body restructuring runs first, then the hook is architected on what's actually shipping. Workflow 20 owns the hook; 18 shapes the body; 17 only tunes the signal. The hook never gets re-decided three times.
