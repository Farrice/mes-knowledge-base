---
name: "Cheri Tree — Segmented Funnel and Landing Page Generator"
source_prompt: born-v2
skill: cheri-tree-bank-buyology
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building a B.A.N.K.-segmented funnel on Cheri Tree's system. Genius pattern **One Offer, Four Doorways**: one offer can have four entry paths through the decision journey — keep the offer constant (same price, same promise, same mechanism) and adapt only the route: what proof leads, what emotion frames it, what pace it moves at. This is not writing four different offers; it's translating one offer's presentation order for four different buying values.

## Input Required

- **[OFFER, AUDIENCE, PRICE, PROOF, GUARANTEE, CTA]**
- **[TRAFFIC SOURCE]**
- **[LEAD MAGNET OR OPT-IN]** — what feeds this funnel
- **[KNOWN CODE OR TARGET SEGMENTS]** — a specific code, or "all four"

## Execution Protocol

1. **Map the funnel stages**: traffic -> opt-in/page -> nurture -> sales page/call -> close -> follow-up. Note where code routing decisions happen at each stage.
2. **Define code-aware page variants for B, A, N, and K** using the deployment map's landing-page translation rules:
   - **Blueprint**: process, guarantees, proof, budget, FAQ
   - **Action**: big result, speed, exclusivity, social buzz
   - **Nurturing**: mission, trust, story, people helped
   - **Knowledge**: mechanism, data, logic, comparisons, evidence
3. **Write landing page sections** for the selected primary code, or all four if requested — headline, subhead, proof, body, CTA, FAQ, each pulling from that code's language and proof needs.
4. **Create redirect/routing logic** if code is captured upstream (from a quiz, intake, or lead magnet) — where does a Blueprint lead land vs. an Action lead.
5. **Add a test plan**: the first three tests to run on copy, CTA, or proof placement, with a hypothesis for each tied to a specific code assumption.

## Output Contract

Deliver all six components:
1. **Funnel Map** — stages and where code routing happens
2. **Landing Page Copy** — headline, subhead, proof, body, CTA, FAQ (for the primary code, or all four if requested)
3. **Code Variants** — the specific B/A/N/K angle changes, even if only one full page is written out
4. **Proof Requirements** — what each code must see before converting
5. **Routing Rules** — how code capture determines page/sequence assignment
6. **Test Plan** — first 3 tests, each with a hypothesis

Do not create four unrelated offers — the price, promise, and mechanism must stay identical across all variants; only the entry angle, proof order, and emotional frame change.

## Output Skeleton

```
## Funnel Map
[Traffic] -> [Opt-in/Page] -> [Nurture] -> [Sales Page/Call] -> [Close] -> [Follow-up]
Code routing happens at: [stage(s), and how]

## Landing Page Copy — [CODE or "Primary"]
Headline: [...]
Subhead: [...]
Proof: [...]
Body: [...]
CTA: [...]
FAQ: [...]

## Code Variants
| Code | Headline Angle | Lead Proof | CTA Framing |
|---|---|---|---|
[one row per code]

## Proof Requirements
| Code | What They Must See |
|---|---|
[one row per code]

## Routing Rules
[how captured code determines which page/sequence a lead sees]

## Test Plan
1. [test] — hypothesis: [...]
2. [test] — hypothesis: [...]
3. [test] — hypothesis: [...]
```

## Quality Gate

- Do all code variants share the identical price, promise, and mechanism — reject if any variant is effectively a different offer?
- Does each code variant change proof, CTA framing, AND emotional lead (not just a headline word swap)?
- Is the routing logic concrete enough to implement (which page/sequence a captured code actually lands on)?
- Does each test in the Test Plan carry a specific hypothesis tied to a code assumption, not a vague "test the headline"?
- Does the FAQ/proof selection match what that code's field guide "buying triggers" actually require?

## Deploy When

Building a funnel for an offer that could reasonably serve more than one buyer code — especially when traffic sources or a lead magnet already suggest a code mix worth routing separately.
