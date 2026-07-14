---
description: The end-to-end Novelty Content Engine — the conductor that takes ANY need (topic, asset, platform, audience) and orchestrates all 13 /novelty-* workflows plus the cross-skill Kallaway stacks (audience-obsession, word-mastery, addictive-storytelling) into a single gated pipeline that ships finished, coherence-checked, scorecard-passed content. Use this as the front door whenever you want real content built, not a single component diagnosed. Modes: SINGLE, CAMPAIGN, BATCH.
---

# /novelty-engine — The Novelty Content Engine (end-to-end conductor)

The front door for building actual content on the Illusion-of-Novelty principle. Where `/novelty-forge` runs the five components on one asset, the **engine orchestrates the whole skill** — angle mining, the five-component build, a coherence/retention pass, a delivery pass, the Illusion-Integrity scrub, a closed-loop Gut-Check QA gate, optional multi-platform scaling, and optional data calibration — composing the 13 `/novelty-*` workflows and the adjacent Kallaway skills in the order that produces ship-ready work.

> **Why the engine exists (the lesson from the AI-boom × wellness benchmark):** `/novelty-forge` alone hits the novelty ceiling but is *lane-blind to body coherence* — it can score a piece 10/10 on novelty while a narrative loop dangles open and the prose reads flat. The engine fixes that by routing the draft through `/novelty-to-addictive` (loop integrity) and word-mastery (delivery) BEFORE the Gut-Check gate. Novelty earns the look; coherence + delivery keep it.

## Pre-Flight Gate
Load `../genius.md` if not hot. Answer before running (this is the engine's intake — Phase 0):
1. **The need** — what is the content about (topic), what ASSET/platform, and what is the GOAL (reach / saves / DMs / conversion / authority)?
2. **Mode** — SINGLE (one finished asset) · CAMPAIGN (one reveal → many assets/platforms) · BATCH (N variations of one asset for testing).
3. **Avatar** — who is the reader, what do they already BELIEVE about this topic (held belief, for Contrast), and what OUTCOME do they want (for Outcome Mapping + the proof bullseye)? If you cannot name the held belief and the wanted outcome, you are not ready — load the avatar first (see Skill Acquisition).
4. **Path** — is the topic genuinely new (Path A: reveal it exists) or old/saturated (Path B: mine a new angle — the default)?
5. **Honesty inventory** — what facts/proof/urgency are REAL and available? (The engine never fabricates to fill a component. Only the *novelty* is manufactured.)
6. **Data** — is there past performance data for this account/niche (for Phase 8 calibration)? If not, the engine runs un-calibrated and outputs the data to collect.

## Skill Acquisition
- **Always:** `../genius.md` (IP anchor), `../references/illusion-of-novelty-doc.md` (canonical source), `../references/gut-check-scorecard.md` (the QA instrument), `../references/orchestration-blueprint.md` (the full routing diagram + decision gates for this engine).
- **Avatar (Phase 0):** `kallaway-audience-obsession` (the payload — wanted outcome + what to implant) and/or `mcraney-deep-canvass` / project ICP file (the held belief for Contrast). No avatar specificity → no bullseye proof and no true-opposite contrast.
- **Retention (Phase 3):** `kallaway-addictive-storytelling/genius.md` + `/addiction-loop-architect` (the Four-Step Addiction Loop). Reached via `./novelty-to-addictive.md`.
- **Delivery (Phase 4):** `kallaway-word-mastery` → `/tone-calibration-engine` (gossip-whisperer register), `/rhythm-rewrite` (spoken rhythm), `/believability-audit` (AI-tell scrub).
- **Scale (Phase 7):** `/platform-adapt`, `/atomize`, `/content-series` via `./novelty-campaign.md`.
- **Live research & signal (Phase 0.5 + Phase 8) — the Sandcastles-equivalent:** `../references/research-grounding-stack.md` (the full tool map). Real external grounding: `mcp__perplexity-ask__perplexity_research` / `perplexity_search` (live web + recency filters), `WebSearch` / `WebFetch`, the Tavily skills (`tavily-search` / `tavily-research` / `tavily-extract`), `execution/research.py` (Gemini-first unified engine, Honest Receipt), Apify (social-post + metrics scraping, `directives/apify-usage-policy.md`), `mcp__recall__search` (3,000+ cards), and `/hunt-trends` for zeitgeist. This is what replaces "working from internal context only."
- The engine **calls** the granular `./novelty-*.md` workflows; it does not reimplement them. Treat each as a subroutine.

## Execution — the pipeline

The engine runs phases in order, gating where marked. It **routes by mode** (not every phase fires every time) and **never blindly runs all 13** — it composes the right subset and repairs the weakest component in a closed loop.

### Phase 0 — Intake & Ground
Answer the Pre-Flight. Run the avatar load if the held belief / wanted outcome are thin. Lock: topic, asset, platform, goal, mode, Path A/B, the honesty inventory. This phase sets every downstream input; a vague avatar here caps the whole run.

### Phase 0.5 — Research & Ground (LIVE SIGNAL — the Sandcastles-equivalent) — DO NOT SKIP for real content
Kallaway does not write from memory; Sandcastles feeds him live signal. The engine replicates that. Before building, pull REAL external grounding (tools + protocol in `../references/research-grounding-stack.md`):
1. **Trend / recency scan** — what is genuinely NEW or moving in this topic right now? (`/hunt-trends`, `mcp__perplexity-ask__perplexity_search` with a recency filter, `WebSearch`.) This feeds the **New Reveal** (a real new angle/update) and the **honest Urgency** window. A reveal grounded in a real recent shift beats an invented one.
2. **Fact / proof harvest** — pull the REAL studies, stats, dosing, numbers, named sources that can carry the Bullseye Proof. (`execution/research.py` Gemini-first with its Honest Receipt; `perplexity_research`; `tavily-extract` on primary sources; `mcp__recall__search` for prior verified cards.) Label everything VERIFIED / LIKELY / UNCONFIRMED at harvest time. **The honesty spine starts here:** proof must be real and sourced, or it does not get used.
3. **What's-working scan (competitor / winner signal)** — what angles, hooks, and formats are actually performing in this niche right now? (Apify social scraping per `directives/apify-usage-policy.md`; `perplexity_search`; manual/Playwright pulls of high-performing posts.) This sharpens angle selection in Phase 1 and seeds the Phase 8 pattern loop with real outside-in data, not just the account's own history.
Output of this phase: a grounded brief — real trend, real verified facts/sources, real competitor signal — that every downstream phase builds on. Skip Phase 0.5 only for a throwaway internal draft; for any real asset it is mandatory, and it is the single biggest lever separating this engine from "AI writing from its own context."

### Phase 1 — Angle (divergent → convergent)
Run `./novelty-angles.md` → 12–20 fresh angles scored freshness × outcome-pull. Select the strongest outcome-connected angle (or honor a forced angle the user supplied). In BATCH mode, carry the top N angles forward as separate builds.
*Skip only if the user hands you a locked angle.*

### Phase 2 — Build the Illusion (the five components)
Compose, in order:
1. `./novelty-reveal.md` → New Reveal + Outcome Mapping for the chosen angle.
2. `./novelty-contrast.md` → anchor the reveal against the held belief as a true opposite (the gap = intrigue).
3. `./novelty-urgency.md` → honest-window audit → real urgency line, or an explicit, correct SKIP.
4. `./novelty-proof.md` → climb the Trust Ladder to the highest HONEST rung (viewer-mimic > warm crowd > third-party).
5. `./novelty-hook.md` → compile a dense 1–2 line hook carrying reveal + outcome + contrast (+ real urgency).
6. **Assemble** per `./novelty-forge.md` using the **canonical ordering** (whisper opener → reveal + outcome → contrast → urgency-if-real → bullseye proof) and the **8-step writing workflow** (`../references/illusion-of-novelty-doc.md` §9) — reveal + contrast land EARLY, in the hook zone. Output: a complete first draft of the asset.

### Phase 3 — Make It Stick (coherence + retention) — DO NOT SKIP
Run `./novelty-to-addictive.md`: map the draft onto the Four-Step Addiction Loop (Stakes → Big Question → Head Fake → Rehook). **Close every loop you opened** (an opened narrative thread that never resolves is the #1 flatness defect — the benchmark caught exactly this in a novelty-ceiling piece). Kill dead-air stretches. This is the phase `/novelty-forge` alone does not perform; it is mandatory in the engine.

### Phase 4 — Voice & Delivery
Stack `kallaway-word-mastery`: run `/tone-calibration-engine` to set the **gossip-whisperer** register (never town-crier), `/rhythm-rewrite` for spoken rhythm (read-aloud test), and `/believability-audit` to strip AI-tells. For ghostwriting, route voice through the client's voice rules / DESIGN.md instead of a generic register.

### Phase 5 — Protect the Illusion
Run `./novelty-protect.md`: scan and cut every mascot-reveal (hedge, false modesty, "this is really just…", "everyone knows this") and convert any town-crier line to a whisper. This is the Illusion Integrity scrub.

### Phase 6 — QA GATE (closed-loop) — the engine's quality lock
Run `./novelty-audit.md` (Gut-Check Scorecard): score the 5 components 0–2 for a /10, run the Illusion Integrity pass/fail override and the 3-question sanity test.
**Decision rule:**
- **Score ≥ 9 AND Integrity PASS** → the asset ships. (9 is the honest ceiling when no real urgency window exists; 10 only with a real window.)
- **Any component at 0 or 1, OR Integrity FAIL** → route the single weakest component back to its repair workflow (`./novelty-reveal.md` / `-contrast` / `-urgency` / `-proof` / `-protect`), apply ONE targeted fix, then re-audit. **Cap at 2 repair cycles** to avoid thrash; if still failing after 2, surface the blocker to the user rather than forcing a fabricated component.
**Honesty / verification gate (always):** confirm facts, urgency windows, and proof are REAL. Flag any unpermissioned anecdote, unverified stat, or real-person claim for Chain Step 5.5 — never let a repair pass "improve" proof by inventing a sharper-sounding mimic. The illusion is of novelty only.

### Phase 7 — Scale (CAMPAIGN mode only)
Run `./novelty-campaign.md`: lock the validated reveal as the campaign spine, atomize across the requested platforms/assets so **each asset leads with a different component** (the one reveal never reads copy-pasted), and sequence seed → amplify → convert. Each atomized asset re-runs at minimum Phase 5 (protect) + Phase 6 (QA gate); high-stakes assets re-run Phases 3–6.

### Phase 8 — Calibrate (with real data — close the Sandcastles loop)
Run `./novelty-pattern.md` against REAL data, not vibes: (a) the account's own winners-vs-losers (transcripts + metrics, via Apify or an export), and (b) the competitor/winner signal harvested in Phase 0.5. Fold the specific words/structures/proof-rungs that actually win this niche into the build as bespoke rules. If the account has no history yet, the Phase 0.5 competitor scan still gives an outside-in pattern to start from, and you output the exact data to collect (the social-scrape + metrics set) so the next run compounds. "One-size framework, bespoke execution" — and the execution rules come from real pulled data, the way Sandcastles does it.

## Content-Type Adaptations
| Asset | How the engine adapts the pipeline |
|---|---|
| **Short-form video script** | Phase 2 weights the hook zone hardest (reveal in ~3 sec) + adds a visual-hook note; Phase 3 retention pass is heavy (loop density); delivery = spoken rhythm. |
| **LinkedIn post** | Long-form allows an anecdote-then-reveal build (reveal by line ~5 is fine); Phase 3 closes the opening loop; first-comment asset for saves. |
| **X/Twitter thread** | Phase 1 angle becomes the thread spine; each tweet = one loop; hook tweet carries reveal+contrast; Phase 7 natural if threading a campaign. |
| **Email** | Subject line = the New Reveal compressed; P.S. is a common mascot-leak (Phase 5 checks it); whisper register throughout. |
| **Ad / VSL** | Urgency (Phase 2.3) only if a real window; proof climbs to bullseye; Phase 6 gate is strict (conversion stakes); NO meta/fourth-wall. |
| **Sales / landing page** | Reveal in the headline; contrast in the subhead; proof stacked toward bullseye; protect scans the guarantee/close for hedges. |
| **Long-form article / newsletter** | Phase 3 retention across sections (rehooks between sections); Phase 8 calibration most valuable here. |
| **Ghostwritten thought-leadership** | Phase 4 routes voice through the client's voice rules, not a generic whisper; Phase 6 honesty gate is strict on the client's real claims/anecdotes. |

## Output Requirements
Return, per asset:
1. **The finished content** — ready to ship in the requested format.
2. **The component map** — which line does which job (reveal / outcome / contrast / urgency / proof / loop-open / loop-close / whisper).
3. **The Gut-Check scorecard** — the 0–2 table, /10, Integrity PASS/FAIL, and the repair history if any cycle ran.
4. **The honesty/verification flags** — every fact/stat/anecdote that needs grounding or permission before publish (with VERIFIED/LIKELY/UNCONFIRMED labels where it touches real-world claims).
5. **CAMPAIGN mode:** the asset matrix (asset × leading component × sequence position).
6. **BATCH mode:** the N variants + the single dimension varied across them (for clean testing).
7. **Calibration note** — the winning patterns applied (Phase 8) or the data to collect.

## Quality Gate
The engine's own output is held to `../references/gut-check-scorecard.md` (≥9 + Integrity PASS per asset) PLUS the coherence check from Phase 3 (no dangling loops, no dead air — the defect the novelty scorecard alone cannot see) PLUS the genius.md anti-patterns. **Honesty spine (non-negotiable):** facts, urgency windows, and proof are REAL; only the novelty is manufactured. Any fabricated fact, bolted-on urgency, or invented proof is an automatic fail regardless of the novelty score. If a run cannot reach ≥9 honestly in 2 repair cycles, ship the blocker to the user, not a forced component.

## Relationship to other front doors
- `/novelty-forge` = single-pass 5-component builder (the engine calls it in Phase 2). Use forge when you want a fast novelty draft without the full coherence/delivery/QA stack.
- `/novelty-engine` = the full conductor (this file). Use it when you want ship-ready content.
- `/supercomputer` / `/autopilot` = general multi-domain mission orchestrators. Use those when the job spans brand + design + ops, not just novelty content. The engine is novelty-first and can be a stage inside them.
