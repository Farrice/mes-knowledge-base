# Failure Log — v2 Visual Regression (2026-05-26)

**Project**: Andrea / Resonance launch package
**Severity**: Taste-call failure (2/10 — same severity class as v1's 0/10)
**Pipeline**: Higgsfield MCP → Nano Banana 2 (substituted from requested Nano Banana Pro)
**Cost incurred**: ~$1.50 Higgsfield credits on 6 hero shots

---

## What happened

After v1 (Fal / fantastic-posters / editorial-fashion) scored 0/10 ("group fitness classroom meeting"), the revamp plan called for routing through Higgsfield Soul for photoreal lifestyle. The MCP routing layer substituted **Nano Banana 2** (substitution by tier availability, not explicit request) instead of the **Nano Banana Pro** that the user expected. Output regressed:

- Same-sex pairings appeared in hero shots when the brief is heterosexual-pair-focused
- Age drift to 25-32 when the brief is 30-38
- Multicultural cast read as "ambiguously brown" rather than the named specifics from the ICP
- AI-slop anatomy visible (multiple ligaments, fused fingers, glassy eyes)
- Aesthetically WEAKER than v1 at the detail/texture level despite better body-language register

## Root cause — 3 axes

### Axis 1 — Tier substitution silently degraded model quality
Higgsfield's MCP layer routes "nano-banana" requests through whatever tier is available without surfacing the substitution. Pro → 2 is a real quality drop, but the tool returned a normal response. **No surfacing of the substitution at call time.** I should have caught it by checking the response metadata before processing. Lesson: when a paid pipeline substitutes models without explicit confirmation, the next-call mitigation is to ABORT and route to a different provider, not proceed with degraded output and hope.

### Axis 2 — Brief internalization gap on partnership orientation
The brand brief states "adults seeking committed partners" and the ICP names heterosexual M/F archetypes (Maya / LCSW women, Marcus / Daniel men). I read "diverse cast" and "multicultural" as inclusive-by-default and let same-sex framing into prompts. **The brief is heterosexual-pair-focused** — that's not exclusionary, it's the founder's specific brand thesis. Generic "diversity" framing in prompts produced generic-diversity output. Fix: name M/F partnership explicitly in every prompt + name specific ethnicities per ICP archetypes, not "diverse."

### Axis 3 — Age and detail anchoring drifted with model capability
With v1 (fantastic-posters) the model held tighter to age cues because the editorial-fashion style biases toward mature framing. With Nano Banana 2 (photoreal lifestyle), age cues like "30-40" got read as 24-32 because the model's training distribution skews younger for "party" semantics. Fix: tighten the age band ("30 to 38, mature faces, eye crinkles when smiling, not in their 20s") and add explicit "no Gen Z styling."

## What's salvageable from v2

- The v2 hero shots are NOT salvageable for delivery — they go to `_archive/` not into the launch package.
- The body-language register IS partially salvageable as direction notes (the lean-in, the recognition beat) — keep that in the prompts.
- The Higgsfield workflow gave us a fast-iteration pipeline that we'll re-enter ONLY when Nano Banana Pro is explicitly available via API, not substituted.

## The pivot (user-directed)

Per user direct quote: *"Maybe we need to take a different approach and have you create detailed prompts that I can deploy within ChatGPT for your image and model, and/or through Gemini, so I can work on their specific platforms for design."*

**Pivot**: image generation moves OUT of MCP pipelines entirely for v3. Claude produces high-density deployment-ready prompts. User deploys manually in ChatGPT (GPT Image 2) or Gemini (Nano Banana Pro web tier). User holds the iteration loop. Claude holds the prompt grammar.

**New deliverable**: `projects/andrea-dj/launch/03-visual-variants/prompt-set-for-manual-deployment.md` — 6 hero prompts (2 per variant) calibrated to:
- Heterosexual M/F partnership focus
- Age 30-38
- Named ICP multicultural specifics (Costa Rican / Mexican / Colombian / Black mixed-Caribbean / Polish-Italian / Filipino / Korean)
- Anti-AI-slop language paragraph (verbatim, paste at end of every prompt)
- v2 cultural anchors (Boiler Room Tenaglia Loft, Cercle Adana Twins, Wong Kar-wai, Cuarón/Lubezki, Sofia Coppola, Hou Hsiao-hsien)
- Per-variant palette enforcement

## Calibration update — what gets banned from future generation

Add to `directives/recall-grounding-protocol.md` or equivalent:

| Banned in prompt language | Reason |
|---|---|
| "diverse cast" / "multicultural cast" without naming specifics | Produces generic-diversity output |
| "30-40" age band | Too wide, model picks the young end |
| "young adults" | Drifts to 20s |
| "vibrant party" | Drifts to EDM festival framing |
| "documentary photography" | Pulls observer-distance solemnity (v1 failure carried forward) |
| Any "diverse couples" framing for partnership-recognition shots | Use M/F explicitly |
| Same-sex pairings in hero shots for partnership-recognition events | Off-brief for this brand |
| Implicit assumption that MCP-substituted tier matches requested tier | Verify response metadata or abort |

## Calibration update — what gets required

| Required in every prompt for v3+ | Why |
|---|---|
| "Heterosexual M/F partnership focus" stated explicitly | Brief-correct |
| Age "30 to 38, mature faces" | Tightens model |
| Specific named ethnicities per ICP | Avoids generic-diversity drift |
| Anti-AI-slop paragraph (verbatim) | Catches anatomy fails |
| Connection cues from photography-rules.md §6.5 | Body language register |
| Daylight / sober / no bar | Brand-correct |
| Reference register naming (e.g., "Boiler Room Tenaglia Loft NYC 2013 style") | Anchors model to specific visual culture |

## Cost trace

| Run | Cost | Outcome |
|---|---|---|
| v1 Fal/fantastic-posters/editorial-fashion (8 calls + 4 retries) | ~$3.20 | 0/10 |
| v2 Higgsfield Nano Banana 2 (6 calls) | ~$1.50 | 2/10 |
| v3 manual deployment (user-driven on ChatGPT/Gemini Pro tier) | $0 (subscription, not per-call) | TBD |

Total: ~$4.70 spent before reaching a working pipeline. The pivot to manual deployment cuts per-call cost to $0 and puts the iteration loop in the hands of the person with the taste authority (Farrice → Andrea).

## What this teaches the system

1. **Substituted tiers are a silent failure class.** Add a pre-call assertion: if the response metadata names a different model than requested, abort.
2. **"Diverse" in prompts is too soft to land.** Name specifics from ICP every time.
3. **Manual deployment is a valid route, not a regression.** When the user has direct platform access and taste authority, prompt-engineering for their hands is higher-leverage than MCP autocall.
4. **Brief internalization needs ICP-anchored re-reads.** Heterosexual M/F partnership focus is not "exclusionary" — it's the brand thesis. Reading inclusively-by-default produced off-brief output.

## Tags

`visual-tool-routing` `tier-substitution-failure` `brief-internalization-gap` `manual-deployment-pivot` `mf-partnership-orientation` `age-band-tightening` `anti-ai-slop-protocol`
