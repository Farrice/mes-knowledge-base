---
description: "/offer-redteam — three-agent blind adversarial stress test of an offer (prosecutor / defender / evidence). Born from the 2026-07-21 Alignment Audit kill. Converging blind agents = signal; dissent preserved for Farrice's decision. Pairs with the $0 always-on execution/offer_gate.py."
---

# /offer-redteam — Offer Truth Loop (heavy)

**Purpose:** kill or validate an offer with adversarial rigor BEFORE the system builds
dossiers, prospect lists, or funnels on top of it. Anti-echo-chamber by construction:
three agents, blind to each other, structurally incentivized to disagree.

**When to run:** any new offer or revenue-spine proposal; whenever
`execution/offer_gate.py check` flags; whenever Farrice's gut says "is this real?"
**When NOT to run:** an offer that has already sold ≥3 units to non-warm buyers (the
market already voted); pricing tweaks on a validated offer (use /jam or CFO seat).

## Step 0 — Frame the offer under test (main thread, 2 min)
Write one block before dispatching. If you cannot fill a line, that absence is itself
red-team input — pass it to the agents as a stated gap:
- **Offer:** name + price + delivery shape
- **Promised outcome:** what the buyer walks away WITH (one sentence)
- **Buyer:** who pays, at what awareness stage
- **Channel + constraint:** how it's sold (warm/cold/inbound) and the operator's live constraints (time window, cash target)
- **Grounding files:** every doc the system has already built on this offer

## Step 1 — Dispatch three agents in parallel, blind to each other

**PROSECUTOR** (`adversarial-reviewer`): default posture KILL. Must quote the offer's
own artifacts against it (manifold scores, scoreboard actuals, name-morphing across
docs). Contract: verdict KILL / KILL-UNLESS / SURVIVES · 3 strongest kill arguments
with evidence · one honest concession (weakest point in own case) · if KILL-UNLESS,
the ONE modification that flips it.

**DEFENDER** (`general-purpose`): strongest HONEST case. Every claim cites a file,
fact, or named market signal. MUST concede what it cannot beat — a defense that
concedes nothing is a failed defense. May defend only the defensible version of the
offer and concede the rest. Contract: verdict DEFENSIBLE AS-IS / ONLY IF MODIFIED /
INDEFENSIBLE · 3 survival arguments with confidence labels · explicit concessions ·
exact modification if conditional.

**EVIDENCE** (`deep-research`): receipts only, no psychology. Who sells this shape
today, at what price, with what buyer proof (sales pages, testimonials with names,
job-post counts, case studies)? What do buyers say in the wild? Contract: demand
verdict PROVEN / THIN / ABSENT per offer version · best receipts with links · most
damning + most encouraging finding · "could not verify" stated plainly · never
fabricate a link or price.

## Step 2 — Synthesize (main thread; owner voice)
- **Convergence across blind agents = signal.** Name where they converged.
- **Dissent preserved, never blended** (EVAL-045): where they disagree, present both
  positions and hand Farrice the decision — one clear line per side.
- **Verdict:** KILL / MODIFY (state the exact modification) / VALIDATED.
- **The cheapest real-world test:** whatever the debate can't settle, name the $0,
  ≤72-hour market test that settles it (sends, not documents).

## Step 3 — Capture (non-optional)
1. Solution Card in `docs/solutions/` if the verdict changes strategy (Step 6.5 rule).
2. `memory_store.py store --tier semantic --category insight` — the verdict + pointer.
3. `chain_runner.py finalize` with anchors (type: Strategy or Research).
4. If KILLED: purge the offer from active goal threads; mark surviving artifacts
   explicitly ("prospect list survives, dossier becomes content layer") so good work
   isn't orphaned.

## Quality Gate
✓ All three agents ran blind (no shared conclusions in prompts beyond ground files)
✓ Prosecutor conceded something; defender conceded something (if either concedes
  nothing, its output is theater — rerun it)
✓ Evidence agent labeled every receipt VERIFIED/LIKELY and listed unverifiables
✓ Dissent surfaced to Farrice as a decision, not averaged away
✓ Verdict names the cheapest real-world test
✓ Capture complete (card / memory / finalize)

**Precedent run:** `docs/solutions/2026-07-21-alignment-audit-red-team-verdict.md`
(the proof-of-concept — $400 Alignment Audit killed as cold offer in one session).
