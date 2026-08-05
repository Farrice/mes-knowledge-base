---
date: 2026-08-05
session: benoit-vatere
tier: operator-guide
status: enriched
---

# Benoit Vatere Forge — Full-Funnel Media Systems Extraction (Liquid Death) — What We Built 2026-08-05 and How to Use It

> One 34-minute interview with Liquid Death's Chief Media & Digital Commerce Officer became the roster's missing **media-systems seat**: how to buy media, how to know whether it worked, and which channels deserve a dollar at all. Ten workflows, twelve genius patterns, eight execution prompts, all gates green, verdict "like". Companion files: `skills/benoit-vatere/genius.md` (load first, always) · `skills/benoit-vatere/SKILL.md` (workflow table) · `extractions/benoit-vatere/extraction-report.md` (full dossier) · `extractions/benoit-vatere/reference-corpus/` (19,818 words of unseen Benoit, already fetched, waiting to enrich the skill).

## ⚡ If you only read 10 lines

1. `/benoit-vatere` is the front door — persona + full arsenal. Everything else is a narrow lane off it.
2. The one doctrine line: **platform ROAS is contaminated; incrementality is the truth layer** — "those $3… would have happened without the ad as well."
3. The failure metric he named: **CAC:LTV chased from day one**. Every brand's golden core is finite; past it CAC inverts and people blame the algorithm.
4. Channels are lever sets, not audiences. No frequency control = no awareness dollar. **Social is not an awareness channel, period.**
5. Test threshold: **≥20% potential effect or don't run it**; inconclusive by **day 4** = kill and move on.
6. Creative rule: **one job per unit** — REMEMBER-NAME / LINK-BENEFIT / RE-ANGLE / WIN-BACK. Never two.
7. Fastest incrementality without infrastructure: **ROAS × new-to-brand %**. High ROAS + low NTB = fake winner.
8. First thing to run on any account, ever: the Spend Map (via `/benoit-vatere` — it is the front-door flagship, no standalone command).
9. Skill is **B+ tier**: `skill_auditor.py check --skill benoit-vatere` = 7/7, blind pass PASS (EVAL-059). A-tier needs a Farrice-judged side-by-side.
10. Next move is already loaded: `/extract` Extension Mode on the two corpus transcripts to close the one named gap (tool-name density).

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `/benoit-vatere` | Persona + full arsenal; flagship = Spend Map (tagged spend, imbalance read, ONE rebalance move) | Any media question; first touch on an account; **the only way to fire Spend Map** |
| `/incrementality-triage` | ROAS×NTB quadrant with fake-winner flags, a geo holdout design, iROAS ladder with confidence classes | Budget allocation; a channel that "prints"; dashboards and bank account disagree |
| `/channel-lever-audit` | Channel × job × lever matrix, ADMIT/REFUSE verdict with mechanism cited | Channel planning; a media rep is pitching; "should we be on X?" |
| `/funnel-creative-map` | One-job brief headers + buyer-state message ladder (never-seen → lapsed) | Creative planning; two-job ads in the account; retargeting repeats the first message |
| `/golden-core-diagnostic` | CAC-inversion diagnosis (four-beat verdict, ≤150 words) + up-funnel shift memo with an investor paragraph | "Meta stopped working"; rising CAC; **the lead-magnet teardown** |
| `/home-run-test-charter` | ≥20%-effect test roadmap, kill conditions pre-written, kill log scaffold | Test queue full of inconclusive 5% hunts |
| `/pdp-chain-audit` | CTR→CPM→CPC→cost-per-PDP-view decomposition, weakest lever named, one fix chartered | Good CTR, bad results; social→retailer journeys |
| `/retail-media-plan` | Retail allocation move + control-comfort corrective (CPG only, `fidelity: low`) | CPG over-indexed on D2C; TikTok Shop questions |
| `/bv-x-dara-stage-briefs` | Per-stage briefs: Benoit headers, Dara bodies, dissent ledger | Creative production against the system map |
| `/bv-x-vince-measurement-stack` | Three-layer measurement stack (platform / blended / incrementality) with jurisdiction rules | DTC+retail attribution disputes |

## The mental model

**Three ideas make the rest obvious.**

**1. The system is the asset; the campaign is a rounding error.** Everyone studies Liquid Death's creative. Benoit built the machine underneath it — categorize every dollar by funnel stage, then judge, then place, then speak. The host called it "the collision point of data and taste," and Benoit's own framing is that the glamorous shoot is a small part of what sells anything. When a request smells like "let's run a campaign," the Benoit move is to ask what system it feeds.

**2. Speed of signal beats precision of measurement.** His line is "I don't need perfect, I need signals" — because chasing the right confidence level means "by the time you get it, it's over." A two-year MMM is a share-defender's tool. Every workflow here is built to return a decision in **days-to-weeks**, with the confidence class stated honestly (TESTED > TRIAGED > PLATFORM-CLAIMED) rather than hidden.

**3. Control is a portfolio you allocate, not a thing you maximize.** Release control where scale lives (retail — "where you get the most scale is mostly where you get the least amount of control"); hold control over how you buy (frequency, creative-to-audience assignment). Marketers default to the opposite because their own website feels safe. This single inversion explains the retail-media doctrine AND the refusal to let a platform pick creatives.

## Capability 1 — The measurement trio (Spend Map · Incrementality Triage · PDP Chain)

**What it is.** Three audits that compose into a full media diagnosis. Spend Map tags every dollar by funnel stage and reads the imbalance against two known failure shapes (consumer brands all top-funnel, B2B all bottom). Incrementality Triage crosses platform ROAS with new-to-brand % to find revenue that would have happened anyway, then designs one matched-market geo holdout (spend in New York, dark in LA, read the retail delta). PDP Chain decomposes mid-funnel efficiency into CTR → CPM → CPC → click-to-landing drop-off → cost per product page view, because a great CTR on an expensive CPM is still an expensive PDP view.

**When to reach for it.** Inheriting any account. A client audit opener. A channel that suddenly looks incredible. Any time someone quotes a ROAS number in a decision meeting.

**When NOT to.** Don't run these on a brand with no spend history — there's nothing to tag. For pre-launch allocation design, use the Spend Map's from-scratch path or go straight to `/channel-lever-audit`. Don't reach for Incrementality Triage when the real question is creative quality; that's `dara-denney-meta-ads`.

**How to invoke.** `/benoit-vatere` then the Spend Map flagship → `/incrementality-triage` → `/pdp-chain-audit`. Each has a wired execution prompt under `skills/benoit-vatere/references/prompts-v2/` with an Output Contract, Skeleton, and Quality Gate — honor them rather than improvising the shape.

**Worked example.** The blind-pass sample runs the golden-core read on a $2.1M DTC supplement brand with CAC up 74% and 91% conversion-stage spend, and lands the verdict in his four-beat shape: cause → curve → the operator's own words → reframe. See `extractions/benoit-vatere/blind-pass-sample.md`.

**Honest edges.** `/retail-media-plan` carries `fidelity: low` by design — the source gives doctrine and destination, not platform tactics; any tactic beyond the transcript needs live research. Cost-per-PDP-view assumes click-to-landing is instrumented; when it isn't, the gap IS the finding, and the prompt forces a NOT-INSTRUMENTED flag rather than a guessed number.

## Capability 2 — The doctrine tools (Channel Lever Audit · Funnel Creative Map · Home-Run Test Charter)

**What it is.** Three enforcement surfaces for the parts of his method that are opinions with teeth. The lever audit admits or refuses channels by the levers they surrender — and keeps the refusals on file as receipts for when the pitch comes back. The creative map assigns exactly one job per unit and builds a message ladder keyed to buyer state, so no state ever sees a repeated default. The test charter screens candidates for ≥20% plausible effect and writes every kill condition *before* launch.

**When to reach for it.** A rep is pitching a platform. An account is full of ads doing three jobs at once. A test queue that never concludes anything.

**When NOT to.** These don't produce creative — they constrain it. Actual ad production routes to `/bv-x-dara-stage-briefs` or the Dara skill directly. And the home-run doctrine is explicitly for hypergrowth; a multibillion-dollar incumbent defending share legitimately hunts single digits, and the workflow says so instead of forcing the rule.

**How to invoke.** `/channel-lever-audit` · `/funnel-creative-map` · `/home-run-test-charter`.

**Honest edges.** Platform capabilities drift fast. Everything version-dependent lives quarantined in `skills/benoit-vatere/references/era-bound-2026.md` — Meta frequency behavior, Advantage+-style automation, TikTok Shop's state — and must be re-verified before any external claim. The durable principles (no frequency lever = no awareness dollar) survive the drift; the mechanics don't.

## Capability 3 — Verified embodiment (the corpus + blind pass)

**What it is.** The gate that separates this from a vocabulary skin. Two *unseen* verbatim Benoit pieces were collected — a 2025 keynote (5,611 words) and a 2026 podcast episode (12,492 words) — and generated outputs were judged against them. The keynote independently confirmed the extracted doctrine, including the frequency-capping complaint and the answer that rising acquisition cost means nothing is coming from the top.

**When to reach for it.** Any time you doubt whether a skill actually carries an expert or just their nouns. The corpus-first move generalizes: hunt an expert's conference talks *before* declaring an extraction finished.

**How to invoke.** `python3 execution/blind_pass.py prepare --expert benoit-vatere` (corpus gate) → judge side-by-side → `python3 execution/blind_pass.py record --expert benoit-vatere --verdict PASS --notes "..."`. Gate check: `python3 execution/skill_auditor.py check --skill benoit-vatere` (currently 7/7).

**Honest edges.** The verdict is **model-judged**, recorded as EVAL-059; A-tier promotion requires a Farrice-judged pass, still open. The one named gap: real Benoit name-drops infrastructure mid-answer far denser than a single interview supports. The corpus already contains those names — enrichment is a loaded gun, not a research project.

## Composition (options, not pipeline)

| Stacks with | Earns its cost when |
|---|---|
| `dara-denney-meta-ads` | Creative must actually get made against the stage/job map — headers from Benoit, bodies from Dara, disagreements surfaced not averaged |
| `vince-nijhof-dtc-operator-system` | Brand sells both DTC and retail; blended MER and incrementality need jurisdictions (rule: causality beats correlation) |
| `sarah-levinger-ad-psychology` | RE-ANGLE and WIN-BACK briefs need real objection psychology, not just a new angle slot |
| Proof-to-Market ($2,500 sprint) | Selling supplement/performance CPG — Spend Map + Golden Core + Retail Media speak that buyer's exact vocabulary (retail media, NTB, PDP, velocity) |
| `/ghostwrite` · `/parallax` | Turning the Golden Core teardown into Farrice-voice distribution — load VOICE-CARD + dial first |

## Session receipts

- Commits: `dec2f5654` (forge) · `c40754e9b` (felt verdict "like") · `d5db94d31` (closeout gate).
- Gates: renaissance audit 0 fail · heartbeat 7/7 · blind pass EVAL-059 PASS · `chain_runner.py finalize` logged · `forge_gate.py record` stamped.
- Co-tenancy note: a sibling session shipped `kallaway-hook-mastery` against this tree the same day and committed it independently (`8753da92e`) — no collision, but the closeout stub's "assets changed" list spans both sessions. Confirm `session_lock.py` before the next multi-file build.
- Known cosmetic gap: `/spend-map` has no standalone command (reachable only as the `/benoit-vatere` flagship). Mint it if it gets used often.
