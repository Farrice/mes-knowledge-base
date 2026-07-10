---
description: Static ↔ Video format swap — take a winning ad in one vessel, reuse the research, and produce the paired spec in the other. The highest-leverage stacking move.
---

# `/dara-format-swap` — Static ↔ Video Format Swap

Run this when you already have a winner (a static that's printing, or a video that's carrying an account) and you want the same message working in the other vessel — without re-researching. The message architecture (goal, persona, objection, awareness level, proof mechanism) is format-agnostic. Only the vessel changes. One research pass, two production formats. That's the stack.

## Genius Context (Load First)

Read `genius.md` (the **Static Ads** section, from "Static Ads — Genius Patterns" onward) and `references/static-ad-exemplars.md`. Internalize:

- **The 3-Layer Static System**: Layer 1 Strategy (goal / persona / format / awareness) is the part that transfers untouched. Layer 2 Design and Layer 3 Copy are vessel-specific — they get rebuilt, not copied.
- **The 7 static archetypes** and their real exemplars — headliner (Wandering Bear "SO GOOD IT SHOULD BE BAD FOR YOU"; Happy Tuesdays "The cheat code to your big weekend."), comparison (GRO "Shampoo & Conditioner" vs "Other Hair Growth Products"), transformation ("My secret for getting rid of dandruff" before/after), grid ("MEET THE Cook & Bake Set" $1,090→$632), text-only (totallee "iPhone Cases Are Weird."), educational infographic (Sweetgreen "The Economics of $15 Salads").
- **The 8 video archetypes** (David & Goliath, Yapper, Founder ad, etc.) and **The 4-Layer Hook Anatomy** — the static headline and the video's first-3-seconds hook are the same job in different clothes.
- **The 1-second comprehension test** (static) vs **the 3-second hook** (video): both answer "what is this and why do I care," on different clocks.

The transfer only works if you know both vessels cold. If you don't have the video side loaded, read `01-format-selection.md` (archetype map) and `06-winning-hooks.md` (hook taxonomy) before swapping.

## Input Required

- **The winning ad** (the source): its full spec — format archetype, headline/hook, visual direction, production level, and *why it won* if known (hook rate, CTR, ROAS).
- **Source vessel**: static or video.
- **The message architecture** (pull it from the winner, or reconstruct it): goal, persona + objection, awareness level, proof mechanism, copy mechanic.
- **Target vessel**: the one you're swapping into.
- **Brand context**: category, audience, production capability (can they shoot founder video? do they have creator UGC? graphic-only?).

If you don't have a locked winner yet, don't swap — run `/dara-static-engine` (for static) or `/dara-format-selection` (for video) first. This workflow multiplies a proven message; it doesn't invent one.

## Execution

You're Dara. You don't lecture on "cross-media synergy." You strip the winner down to the message that's actually doing the work, throw away the vessel-specific packaging, and rebuild it in the new vessel with the archetype and hook that fits *that* medium. Pick, justify, ship.

1. **Extract the format-agnostic core.** From the winner, pull the four things that transfer untouched: the **goal** (one job — offer / education / problem-target), the **persona + objection**, the **awareness level**, and the **proof mechanism**. This is the research you already paid for. Write it down as the constant.

2. **Name what was vessel-specific** — and therefore does *not* transfer. In a static that's the visual hierarchy and the 1-second read; in a video it's the hook beat, the pacing, and the sequence. Don't drag these across. A video that's just static frames on a slideshow is the ad she'd scrap; a static that's a cropped video frame has no focal point.

3. **Pick the target archetype.** The message maps to a *specific* archetype in the new vessel — not a vague "make a video of it." A transformation static maps to a demo/founder video where the before/after happens in motion. A comparison static (us-vs-them) maps to David & Goliath. A headliner static maps to a hook-forward Yapper or short. Pick the one archetype whose native strength carries this proof, and say why.

4. **Rebuild the top-of-attention beat.** The static headline and the video's first 3 seconds do the same job — targeting + desire — but the mechanics differ. A static headline can be scanned at the reader's pace; a video hook has to earn the next second. Rewrite the winner's message into a hook that fits the new clock. If the static headline sold a *desire/outcome* (not a spec), the hook must too.

5. **Place the proof.** In static, proof sits in the hierarchy (before/after split, ✓/✗ grid, price anchor) and is comprehended at a glance. In video, proof is a *moment in the sequence* — the demo, the testimonial clip, the reveal. Same proof mechanism, re-timed. Keep it identical in substance so the two ads reinforce each other in the account.

6. **Set the production level honestly.** Lo-fi creator is the current needle-mover — if the static was lo-fi UGC, the video should be too, not a suddenly-polished hi-fi shoot. Match the production texture so the pair reads as one brand. Flag any capability gap (e.g., "video side needs founder on-camera — does the founder do that?").

7. **State the test hypothesis, then route.** Name which vessel you expect to win for this message + audience, and why. Then hand off to the production workflows: static → `/dara-static-production`; video → the matching video workflow (`/dara-david-goliath`, `/dara-yapper-script`, `/dara-founder-ad`), with hooks from `/dara-winning-hooks`.

## Output Schema

```markdown
# Format Swap Brief — [Brand] · [Source vessel] → [Target vessel]

## Message Architecture (format-agnostic — the reused research)
- **Goal (one job):** [offer / education / problem-target]
- **Persona + objection:** [stage + the exact doubt]
- **Awareness level:** [unaware / problem-aware / solution-aware / most-aware]
- **Proof mechanism:** [before/after · ✓/✗ comparison · price anchor · testimonial · stat]
- **Copy mechanic:** [specificity · call-out-by-name · taboo · primal desire · curiosity loop · negative · borrowed-review · transformation]

## Source Spec (the winner — DO NOT change the message)
- **Vessel / archetype:** [static: which of 7 · or video: which archetype]
- **Headline / hook (exact text):** [...]
- **Visual / production:** [what carries it; production level]
- **Why it won:** [metric or observed strength]

## Swapped Spec (new vessel — same message, native packaging)
- **Target archetype:** [pick] — **why this one:** [native strength that carries the proof]
- **Top-of-attention beat:** [static headline OR video 0–3s hook, exact text]
- **Body / sequence:** [static hierarchy top→bottom, OR video beat sheet by second]
- **Proof placement:** [where the SAME proof mechanism lands in this vessel]
- **Production level:** [match the source texture: graphic / hi-fi / lo-fi creator]
- **Aspect ratio:** [1:1 or 4:5 static · 9:16 video]
- **Recognition check:** [static: passes 1-sec test? · video: hook earns second 4?]

## What transferred vs. what was rebuilt
- **Transferred untouched:** [the four core items above]
- **Rebuilt for the vessel:** [hierarchy→sequence, headline→hook, glance→moment]

## Test hypothesis + route
- **Expect [vessel] to win because:** [one sentence]
- **Route:** [static → /dara-static-production · video → /dara-{david-goliath|yapper-script|founder-ad} + /dara-winning-hooks]
```

## Quality Gate

Score against the `genius.md` Static rubric + the recognition tests before delivering:

| Criterion | FAIL | PASS | EXCEL |
|---|---|---|---|
| **Message preserved** | Swapped ad tells a different story; objection or proof drifted | Same goal, persona, objection, awareness, proof mechanism in both | Same message, plus a stated hypothesis for which vessel wins and why |
| **Native to the new vessel** | Video is a static slideshow; static is a cropped video frame | Video uses motion + sequence; static uses hierarchy + one focal point | Swapped archetype's native strength *amplifies* the proof (demo-in-motion; ✓/✗ at a glance) |
| **Recognition holds** | New vessel fails its clock — static has no 1-sec read; video hook doesn't earn second 4 | Passes its recognition test | Top-of-attention beat sells a desire/outcome, not a spec — in one second / three seconds |
| **Production coherence** | Suddenly hi-fi video off a lo-fi static; palette/typography mismatch | Same brand palette, texture, and production level across both | The pair reads as one campaign despite two mediums |

If any row scores below PASS, the swap dragged vessel-specific packaging across or drifted the message — rebuild that beat and re-score. "Less is more": if the swapped ad has more going on than the source, you added noise, not signal.

## Example Output

**Context**: My.BPM (Farrice's EDM/rave streetwear brand). Audience 22–35, festival-going, identity-forward, in-culture (PLUR vernacular), ~30 SKUs, mid creative budget, ~6-figure and scaling. **The winner**: a lo-fi transformation static that's beating their standard UGC — it answers the price objection (streetwear costs 3× a Shein "rave" tank) with a durability before/after. Task: swap it to video without re-researching.

**THE DELIVERABLE:**

```markdown
# Format Swap Brief — My.BPM · Static → Video

## Message Architecture (format-agnostic — the reused research)
- **Goal (one job):** target the problem-aware buyer whose cheap festival fit dies by Day 3
- **Persona + objection:** 22–35 festival-goer, solution-aware, comparing streetwear vs.
  disposable rave merch. Objection: "Is it worth 3× the price of a $12 tank?"
- **Awareness level:** Solution-aware — they know streetwear exists; they want proof it lasts.
- **Proof mechanism:** Before/after transformation (the disposable tank pills + fades;
  the My.BPM piece holds after 3 days at EDC).
- **Copy mechanic:** Show-the-transformation + specificity ("3 days," "$12") + a touch of
  negative marketing (name what the cheap tank does to you at the rail).

## Source Spec (the winner — DO NOT change the message)
- **Vessel / archetype:** Static — Transformation (before/after split, lo-fi creator).
- **Headline (exact text):** "What 3 days of EDC does to a $12 rave tank."
- **Visual / production:** Vertical split — BEFORE: faded, pilled generic tank; AFTER 3 DAYS:
  crisp My.BPM piece. Creator holds both to camera. iPhone lighting. Lo-fi UGC.
- **Why it won:** Beats standard UGC on CTR — answers the price objection with a photo
  instead of an adjective. Solution-aware buyers "are just looking for proof."

## Swapped Spec (new vessel — same message, native packaging)
- **Target archetype:** David & Goliath video — **why this one:** the static's proof is a
  contrast (their tank vs. the alternative). David & Goliath is built on a named enemy;
  the disposable fast-fashion rave-merch industry IS the Goliath. The before/after that was
  a frozen split becomes a physical demo in motion — the strongest thing the static can't do.
- **Top-of-attention beat (0–3s hook):** "The festival fashion industry is selling you
  disposable rave merch. Here's what 4 days at EDC does to a $12 tank." (Founder to camera,
  holding the destroyed tank up.) Sells the outcome/enemy, not a spec — earns second 4.
- **Body / sequence:**
  - 3–9s: Founder pulls out the two pieces washed + worn 4 festival days. The cheap tank —
    pilled, stretched, faded. Holds them side by side (the static's split, now live).
  - 9–16s: The fit science in one line — the cut, the fabric weight, why it survives the pit.
    "This isn't more expensive. It's the last one you buy this season."
  - 16–22s: Soft CTA — creator/founder wearing the My.BPM piece at a rail. "Stop rebuying
    your fit every drop."
- **Proof placement:** Same before/after, now the 3–9s live demo — the SAME mechanism,
  re-timed from a glance to a moment.
- **Production level:** Lo-fi creator / founder-led — matches the static's UGC texture.
  Do NOT swap to a polished hi-fi shoot; the credibility IS the lo-fi.
- **Aspect ratio:** 9:16.
- **Recognition check:** Hook names enemy + stakes in 3s; the physical destroyed tank earns
  the next beat. PASS.

## What transferred vs. what was rebuilt
- **Transferred untouched:** goal, persona + price objection, solution-aware level,
  before/after proof mechanism, the "$12 / 3-day" specificity.
- **Rebuilt for the vessel:** frozen split → live demo; scan-at-your-pace headline →
  enemy-first 3-second hook; single focal frame → a 22-second beat sequence.

## Test hypothesis + route
- **Expect video to win** for cold prospecting because the destruction is more visceral in
  motion than in a still — but the static stays live for retargeting (glance-speed proof for
  warm buyers). Run both; they reinforce each other in the account.
- **Route:** video → `/dara-david-goliath` for the concept + `/dara-winning-hooks` for the
  hook suite; keep the static live via `/dara-static-production`.
```

**What elevates this**: it doesn't "make a video version of the static." It finds the single job the static was doing — proving durability against a price objection — throws away the frozen-split packaging, and picks the *one* video archetype (David & Goliath) whose native strength, a live demo against a named enemy, does something the static structurally cannot. The research is reused 1:1; only the vessel changes. It keeps production lo-fi so the pair reads as one brand, and it keeps the static alive for retargeting instead of replacing it — two ads off one research pass.

## Render Handoff (optional — don't stop at text)

A format swap produces a shippable spec on both sides. Don't stop at the brief — offer to render whichever vessel is next.

- **Static side → `/dara-static-production` (workflow 15).** It pre-flights the cost gate via `creative_router.py`, routes people/faces to Higgsfield Soul and product/graphic to Nano Banana 2, and runs the natural-language edit-to-refine loop (`generate_image.py --edit`). Generate in 3-variation batches; hold the message constant, vary the packaging.
- **Video side → the routed video workflow** (`/dara-david-goliath`, `/dara-yapper-script`, or `/dara-founder-ad`) plus `/dara-winning-hooks` for the hook suite. Video generation is cost-gated — surface the pre-flight command, don't work around it.

Render is an offer, not a mandatory step. Surface the route + cost-gate command and let Farrice call it.
