# The Avatar Machine — Deployment Guide

How to actually use `luke-iha-avatar-machine` for highest leverage. Written for Farrice; generalizes to any operator.

## 1. The one mental model

The Manifold is a **market X-ray, not a market sketch.** A normal ICP describes the patient ("42, male, busy, values competence"). The Manifold plots the internals ("Urgency 8, Stigma 6, Locus internal-3, Core Wound = replacement-by-the-louder-and-less-qualified, Identity-clash landmine = the word 'personal brand'"). You don't read it — you *operate off the numbers.* Every score has a consequence; the consequences are the copy instructions.

**The keystone position:** this is the front door of the whole Luke stack. Market understanding flows *down* from here into hooks, proof, VSLs, mechanisms. If you ever find yourself writing copy for a market you haven't plotted, you skipped the front door.

## 2. What it is NOT

- Not a replacement for your qualitative ICP work. Your McRaney/Cimorelli profiles are *feedstock* — the Manifold adds the dimensional/mechanical layer on top.
- Not a one-click button. The flagship `/avatar-manifold` is a 14-stage build; treat it like a research project, not a prompt.
- Not for offer/sales docs. Those are selling-side. The Manifold is understanding-side. Build the Manifold first, *then* write the offer off it.

## 3. The three deployment modes

| Mode | When | What you run |
|---|---|---|
| **Full build** | New market, or a market you'll sell to repeatedly | `/avatar-manifold` (import existing ICP as VOC so you don't redo strong parts) |
| **Single-tool** | You need one specific thing fast (a hook set, a constraint dissolved, a backstory) | the relevant Tier-2 workflow (`/epiphany-threshold`, `/dissolution-forge`, etc.) |
| **Audit** | You have an existing ICP/avatar/brief and want to know if it's good | `/manifold-audit` → gap report → fix with named workflows |

## 4. Decision tree

```
New market you'll sell to repeatedly?       → /avatar-manifold (the asset)
Existing ICP, unsure if it's deep enough?   → /manifold-audit (then fix gaps)
Need hooks right now?                        → /market-pickup-lines (+ /epiphany-threshold)
A specific objection keeps killing sales?    → /dissolution-forge
Writing a VSL/sales-page backstory?          → /anti-hero-journey
About to write copy off a finished Manifold? → /manifold-to-copy (routes to the stack)
Don't understand the buyer at all yet?       → /buyer-sourcer first (pull real VOC)
```

## 5. The highest-leverage sequences (recipes)

**A. The Keystone Run (new market → finished copy)**
`/buyer-sourcer` → `/avatar-manifold` → `/manifold-to-copy` → [Luke copy stack]. This is the full value chain. Do it once per real market; reuse the Manifold forever.

**B. The Upgrade (you already have a strong ICP)**
`/manifold-audit` on the existing doc → it tells you which 3-4 layers are missing → run *only* those single-tool workflows → staple results onto the existing ICP. Don't rebuild what already scores 8+.

**C. The Sales-Unblock (a specific objection is killing conversion)**
`/dissolution-forge` on that one constraint → drop the AWE dissolution into your call script / sales page objection section. 20-minute fix, immediate revenue impact.

**D. The Hook Sprint (content/ads)**
`/epiphany-threshold` (generate the Goldilocks belief set) → `/market-pickup-lines` (turn them into hooks) → hand to `luke-iha-vicious-hooks` for the viciousness pass.

## 6. The single rule that creates the leverage

**Import, don't regenerate.** When you run `/avatar-manifold` on a market where you already have ICP material, feed the existing doc in as VOC + identity feedstock. The workflow then spends its effort on the *missing dimensional layers* (Pain Matrix scores, Core Wound resource matrix, Epiphany Threshold, Dissolution arsenal, Anti-Hero arc) instead of redoing the qualitative work you've already nailed. This is the difference between a 30-minute upgrade and a 3-hour rebuild.

## 7. Anti-patterns (how NOT to use it)

- ❌ Running the full Manifold on a market you'll touch once. Use single-tools instead.
- ❌ Auditing an offer/sales doc on the ICP rubric and panicking at the low score — wrong artifact type. Audit ICPs; build offers *from* them.
- ❌ Treating modeled language as real VOC. If you didn't pull it from reviews/comments/calls, flag it and replace it. The structure is AI-modelable; the *words* must be market-pulled.
- ❌ Leading copy with an Identity-clashing hook. The Resonance Hierarchy exists to tell you what NOT to say first.
- ❌ Stopping at the Manifold. The Manifold is intelligence; revenue happens when you `/manifold-to-copy` it into assets.

## 8. How this fits Farrice's portfolio specifically

- **The Invisible Expert / Authority Flywheel** is the single best market in the portfolio to run the full Manifold on, because it is *identity-driven* — and the Manifold's core machinery (Resonance Hierarchy, Core Wound, Dissolution Frameworks) is identity-native. The existing deep ICP already supplies 9/10 identity + language feedstock; the Manifold only needs to add the dimensional half.
- **AI Brain Build** has no Manifold under it — it's built on offer intuition. Running `/avatar-manifold` on the "course-graveyard coach" gives it the buyer-understanding spine it's currently missing.
- **The meta unlock:** Farrice sells ICP Intelligence as a *product*. The Manifold IS a superior version of that deliverable. Productize `/avatar-manifold` output as the premium tier of the ICP Intelligence offer — it's a higher-grade artifact than anything competitors ship.
