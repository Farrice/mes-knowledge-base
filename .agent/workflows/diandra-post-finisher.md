---
description: Run Diandra's full LinkedIn production line in one pass — writes the body (if given a topic) → save-architecture (conditional) → format-validated hook → AI-retrieval-signal confirmation → publish-ready post with receipts.
---

# `/diandra-post-finisher` — Post Finisher (the whole production line in one command)

Runs the canonical line — `09 → [18 if save-worthy] → 20 → 17` — so a topic or a draft body comes out the other side publish-ready: body written (if needed), made save-worthy where it should be, fitted with the strongest format-validated hook, and confirmed to carry AI-retrieval signal. One invocation instead of four.

## When to Use
- You have a topic OR a drafted body and want a finished, ship-ready post
- You don't want to fire workflows 09, 18, 20, 17 separately and reconcile them by hand
- Any post going out under your name or a client's where the hook actually matters

## Usage
```
/diandra-post-finisher "[topic OR full draft body]" --bucket [Growth|Authority|Conversion|Personal] --media [none|image|video|carousel|data-viz] --register [formal|informal]
```
Give it a body for the richest hooks; give it a topic and it writes the body first (Phase 0.5, Workflow 09). Want to run a single stage instead? Fire it directly: `/diandra-content-engine` (write) · `/diandra-save-architect` (saves) · `/diandra-hook-architect` (hook) · `/diandra-first-50` (AI signal).

## What It Does (dependency-correct order)
1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` + format library + 40 rules
2. **Reads**: `workflows/22-post-finisher.md`
3. **Phase 0 — Classify**: input type (topic/body), bucket, save-worthiness, media, register
4. **Phase 0.5 — Draft** (conditional, workflow 09): write the body — *only if you gave a topic, not a body*
5. **Phase 1 — Body** (conditional, workflow 18): restructure for saves + visual brief — *only if Authority or teaching/data Growth*
6. **Phase 2 — Hook** (workflow 20, authoritative): 8-10 validated hooks on the FINAL body → winning hook + top 3
7. **Phase 3 — Signal** (workflow 17, confirmation): does the winner carry AI-retrieval signal? Adjust within the limit or defer to sentence two
8. **Phase 4 — Assemble**: finished post + receipts (hook format/chars/gap, save trigger, AI-signal status, why-it-works)

## Why the order is 09 → 18 → 20 → 17 (not 09→20→17→18, not 17→18→20)
Body-first (Pattern 6): you mine the hook from the *final* body, and workflow 18 rewrites the body. So writing and restructuring run first, then the hook is architected on what's actually shipping, then the signal is confirmed last. Workflow 20 owns the hook; 09/18 shape the body; 17 only tunes the signal. The hook never gets re-decided.
