---
description: Atomize ONE strong New Reveal into a coordinated multi-asset, multi-platform campaign — many contrast frames, proofs, and urgency variants that never feel copy-pasted, around a single true claim.
---

# /novelty-campaign — One Reveal, Many Doors (Campaign Atomizer)

Takes a single validated New Reveal + wanted Outcome and scales it into a sequenced campaign across formats and platforms, where each asset *leads with a different component* so the audience meets the same truth from a fresh angle every time. Fire this when one angle has proven strong enough to own for a week-plus and you need coverage, not a one-off post.

## Pre-Flight Gate

Answer these (from `../genius.md` Decision Framework) before atomizing — if `../genius.md` is not already hot, read it now:

1. **Is the spine ONE reveal or several?** A campaign scales *one* New Reveal expressed many ways. If you have three different reveals, you have three campaigns — split them, do not braid false claims to manufacture volume.
2. **What single Outcome does the avatar want** that this reveal maps to? (Constant across every asset.)
3. **What is the avatar's actual held belief** this reveal overturns? (You'll rotate *which* facet of that belief each asset contrasts against — so name the belief richly.)
4. **Which platforms have a REAL urgency window**, and which don't? (Urgency rotates in only where it's honest per medium — see Step 4.)
5. **What's the highest honest Trust-Ladder rung available, per asset?** (Different assets can carry different proofs — a bullseye case fits video, a stat fits the long-form. Map proof to asset.)
6. **Where is each medium tempted to hedge or go town-crier?** Pre-commit the storyline and the whisper register before drafting.

## Skill Acquisition

- **Always:** `../genius.md` (the five components, two apex moves, rubric, honesty spine).
- **Stack — scaling mechanics:** `/platform-adapt` (native re-expression per platform — this workflow specifies *which component leads*; platform-adapt handles *how the medium wants it said*) and `/atomize` (parent/child decomposition — this workflow is the novelty-aware specialization of it). Both are workspace workflows (`.agent/workflows/`).
- **Stack — keep-them-watching:** `/addiction-loop-architect` (`skills/kallaway-addictive-storytelling/workflows/addiction-loop-architect.md`) for any asset where the reveal needs a retention engine after the hook lands.
- **Optional avatar payload:** if held-belief or bullseye-proof specificity is thin, pull `kallaway-audience-obsession` before drafting briefs.
- **Optional sequencing depth:** `kallaway-social-commerce` if the campaign terminates in an offer/funnel.

## Execution

### 1 — Lock the campaign spine (the one thing every asset must obey)

Write a one-line spine and freeze it. Everything downstream inherits it; nothing downstream contradicts it.

```
SPINE (vary, never verbatim):
  Reveal:  <the new aspect/angle of the old thing — ONE>
  Outcome: <the wanted result it maps to — ONE>
  Old belief: <the avatar's actual held belief this overturns>
  Honest urgency window (if any): <real time-fact, or "none">
  Honest top proof available: <bullseye case / warm crowd / third-party>
```

If you cannot fill `Reveal` and `Outcome` as singletons, stop — you are not ready to atomize. Run `/novelty-forge` to lock the spine first.

### 2 — Build the LEAD-ROTATION matrix (the anti-repetition engine)

The failure mode of atomization is one message pasted seven times. The fix: each asset *leads* with a different one of the five components, so the audience experiences the same truth through a different door each time. Rows = assets/platforms; the lead column is the lever.

| Asset / Platform | Leads with (rotate) | Why this lead fits the medium |
|---|---|---|
| Short-form video | **New Reveal + Outcome** (densest open) | Scroll-stop economy; you have ~1.5s, lead with the unfamiliar fact + the want |
| LinkedIn post | **Contrast Framing** (the held-belief gap) | Pro audience rewards "you've been told X, turns out Y" reflection over spectacle |
| X/Twitter thread | **Urgency** (if real) or **Contrast** | Recency-native feed; "just changed" earns the open, then unspool the gap line by line |
| Email | **Bullseye Proof** (the viewer-mimic story) | Inbox is intimate; lead with the person who looks like the reader, reveal the mechanism second |
| Ad / VSL | **Contrast + Outcome** | Cold traffic needs the gap *and* the want immediately; proof carries the body |
| Landing page | **Outcome + Proof stack** | Decision context; the reader already arrived curious — convert with result + ladder of proof |
| Long-form article | **New Reveal as a named frame** | Depth medium rewards the named mechanism (naming = cheapest novelty lever) + full proof |
| Ghostwritten thought-leadership | **The held-belief reframe** | Authority register: contrast a *category* belief, deliver as a quiet insider observation |

Rule: no two adjacent assets in the sequence lead with the same component. The reveal is constant; the *entry angle* is what stays fresh.

### 3 — Write a per-asset brief (one short brief each, not a finished draft)

Each brief specifies five things so a drafter or sub-agent can execute it solo:

```
ASSET BRIEF (vary, never verbatim):
  Lead component:     <from the matrix>
  Angle expression:   <how the constant reveal is phrased for THIS lead — fresh words>
  Platform-native contrast: <which facet of the held belief to oppose here; must be a TRUE opposite>
  Trust-ladder rung:  <bullseye / warm crowd / third-party — the highest HONEST one this asset can carry>
  Urgency:            <real window phrasing — or "skip: no honest window here">
  Whisper delivery:   <the gossip-whisperer move for this medium — see ../genius.md 5b>
  Mascot-guard:       <the specific hedge to NOT write for this asset>
```

Diagnostic per brief: *does this asset re-earn all three questions (Relevant / Novel / Interesting) on its own, or does it lean on another asset to carry one?* Each asset must stand alone — an audience that sees only this one piece should still feel the novelty.

### 4 — Rotate urgency honestly (per-platform, never bolted on)

Urgency is the one skippable component, and in a campaign it's also the one that *decays unevenly across platforms*. Apply per asset, never globally:

- A **real window** ("the study dropped this week," "this only became available last month") is fresh on X/short-form today and stale on an evergreen article next quarter. Use it where timing is live; skip it where the asset will outlast the window.
- Different assets may honestly carry **different urgency facets of the same window** (a thread leads on "just dropped"; the landing page omits urgency and leans on proof). This is variation, not contradiction.
- Never invent a second deadline to give an asset its own urgency. A campaign with three real components on each asset beats a campaign where one asset wears fake scarcity. The audience smells it once and distrusts the whole campaign.

### 5 — Sequence: seed → amplify → convert

Assign each asset a role and an order. Hand platform-mechanics to `/platform-adapt`; this workflow owns the *narrative* sequence.

- **Seed** (open the loop wide): the densest, most native scroll-stop — usually short-form video or the X thread. Plants the reveal in the broadest pool.
- **Amplify** (deepen the gap): LinkedIn post + long-form article re-enter the same reveal through Contrast and the named frame, for the audience that wants to *think* about it. Cross-reference the seed, never repeat its words.
- **Convert** (collapse the gap into action): email + landing page (+ ad/VSL for cold traffic) carry the heaviest honest proof and the Outcome, and ask for the next step. Urgency appears here *only* if the window is still real at this point in the sequence.

A loose timing default: seed day 1–2, amplify day 2–4, convert day 4–7. Compress or stretch to the real urgency window, never to a fabricated one.

### Worked mini-example — gutter cleaning (one reveal → 5-asset campaign)

A boring topic for a roofing/home-services operator. **Spine (locked once):**

```
Reveal:  it's not the clogged gutters that rot your fascia — it's the 20-minute
         overflow during a single hard rain, which the gutter looks "fine" between.
Outcome: avoid a $4–9k fascia-and-soffit replacement.
Old belief: "I'll clean the gutters when I can see them sagging / overflowing."
Honest urgency window: regional storm season starting in ~3 weeks (real, dated).
Honest top proof: a recent customer, same neighborhood, who had clean-looking
         gutters and a $7k rot bill — photos on file.
```

**Asset 1 — Short-form video (SEED, leads New Reveal + Outcome).**
Open: "Your gutters look totally clear — and that's exactly why your roofline is rotting." (reveal + outcome, ~1.5s). Body: the 20-minute-overflow mechanism, delivered low-key. Whisper: "most homeowners never hear about this until the contractor's already on the roof." Mascot-guard: do not say "obviously water damage is nothing new."

**Asset 2 — X/Twitter thread (SEED→AMPLIFY, leads Urgency, real window).**
Hook: "Storm season hits this region in 3 weeks. If your gutters look clean right now, that's the trap." Unspool the held-belief gap line by line; close on the mechanism. Urgency honest (dated season). Proof: warm-crowd rung in-thread ("we see this every spring on a dozen homes").

**Asset 3 — LinkedIn post (AMPLIFY, leads Contrast).**
Open on the belief: "Every homeowner thinks gutter damage announces itself. The expensive ones never do." Reframe the "sagging means clogged" belief against the silent-overflow reality. Quiet, insider register. No urgency (this post may outlive the storm window). Proof: third-party-plus-warm-crowd.

**Asset 4 — Email (AMPLIFY→CONVERT, leads Bullseye Proof).**
Subject leans on the mimic: "A house two streets over had 'clean' gutters and a $7,000 bill." Lead with the neighbor case (viewer-mimic rung), reveal the mechanism second, map to the outcome (avoid the bill). CTA: book a pre-season check. Urgency: window still real here, so keep it.

**Asset 5 — Landing page (CONVERT, leads Outcome + Proof stack).**
Headline on the outcome: "Stop a $9,000 roofline repair before the first hard rain." Proof ladder stacked top-to-bottom: neighbor photos (bullseye) → multiple-home pattern (warm crowd) → the overflow mechanism explained (third-party-style). One honest urgency line tied to the dated season. Whisper register throughout; book button, not a billboard.

One true reveal — the silent-overflow mechanism — met five times through five different doors. No facet was inflated into a second claim.

## Content-Type Adaptations

How this workflow's output (the per-asset brief + lead choice) changes by asset:

| Asset | Lead component | Contrast expression | Trust-ladder fit | Urgency rule | Whisper / delivery shape |
|---|---|---|---|---|---|
| **Short-form video script** | New Reveal + Outcome in line 1 | One spoken "you'd think X — nope" beat, fast | Bullseye if you ARE the demo or have a mimic clip; else warm crowd | Use only if live this week; decays fastest here | Lowercase, conspiratorial VO; "barely anyone knows this yet" |
| **LinkedIn post** | Contrast (held-belief gap) | Belief stated as a line, overturned next line; reflective | Warm crowd or a single named case; pro audience tolerates third-party | Usually skip — posts outlive windows | Quiet insider observation; no hype, no exclamation |
| **X/Twitter thread** | Urgency (if real) or Contrast | Gap unspooled across tweets 2–5, one facet each | Warm crowd in-thread; link bullseye case if owned | Lead here if the window is live; recency-native feed | "okay so here's the part nobody mentions" register |
| **Email** | Bullseye Proof | Reframe inside the story (the mimic *believed X, hit Y*) | Highest rung the campaign owns — email is intimate | Keep if window real at send time | Letter-to-one-person; secret-sharing, never blast |
| **Ad / VSL** | Contrast + Outcome | Gap + want in the first 3 seconds for cold traffic | Proof stacked in body, bullseye first | Use only with a genuine window; cold traffic punishes fake | Confident-calm, not announcer; under-claim magnitude |
| **Sales / Landing page** | Outcome + Proof stack | Belief-vs-reality as a section, not a one-liner | Full ladder top-to-bottom, bullseye leading | One honest line, tied to a real date | Whisper headline; proof does the persuading, not adjectives |
| **Long-form article** | New Reveal as a **named frame** | Belief dismantled with depth + evidence | All three rungs in sequence (story → pattern → mechanism) | Skip if evergreen; rotate window out as it ages | Essayistic-confident; the name is the novelty lever |
| **Ghostwritten thought-leadership** | Held-belief reframe (category-level) | Contrast a *category* assumption, not a tactic | Author's own result (bullseye) or named warm crowd | Almost always skip; authority outlasts windows | Restrained, declarative; the insight delivered as overheard, never sold |

The constant down every row: same Reveal, same Outcome, true-opposite contrast, honest proof, gossip-whisperer tone. The variable: which door opens the asset.

## Output Requirements

Return, in this order:

1. **Spine block** — the locked Reveal / Outcome / Old belief / Urgency window / Top proof (one block, frozen).
2. **Lead-rotation matrix** — the asset table with the chosen lead component per asset and a one-line "why this lead" each.
3. **Per-asset briefs** — one brief per asset in the campaign (the 7-field block from Step 3), drafter-ready. Not finished copy; briefs.
4. **Sequence map** — seed / amplify / convert roles with order and the honest urgency-window timing.
5. **One fully worked asset** — promote a single brief to a finished draft as a quality reference for the rest.

## Quality Gate

Score against `../genius.md` Quality Rubric. Campaign-critical criteria:

- **#3 Contrast Integrity** — every asset's contrast is a *true opposite* of the avatar's actual held belief, not a strawman or an adjacent belief. Mis-paired contrast across a campaign multiplies confusion.
- **#4 Urgency Honesty** — urgency appears *only* where a real window exists for that asset at that point in the sequence. Any bolted-on deadline = automatic ≤4 and it contaminates audience trust in the whole campaign.
- **#5 Trust-Ladder Height** — each asset reaches the highest *honest* rung it can carry; no proof is fabricated to give an asset its own bullseye.
- **#6 Illusion Intact** + **#7 Whisper Test** — zero mascot reveals across all assets; gossip-whisperer register everywhere, town-crier nowhere.
- **#9 Domain Fit** — each asset is shaped to its medium (lead rotated, native), not one message reformatted seven times. Repetition across assets caps the campaign at 6.

**Honesty spine (non-negotiable):** the illusion is of NOVELTY only — one true reveal expressed many ways. Never inflate a single reveal into multiple false claims to fill the matrix, and never fabricate a fact, an urgency window, or a proof to give an asset its own hook. If an asset has no honest lead, it does not belong in the campaign.

**Self-check (one line):** *One true reveal, every asset a different door, every contrast a real opposite, every urgency a real window, every proof real and as close to the viewer as honesty allows — and not one mascot head on the ground anywhere in the sequence.*
