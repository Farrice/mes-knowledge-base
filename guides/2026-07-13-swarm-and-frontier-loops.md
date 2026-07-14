---
date: 2026-07-13
session: swarm-apex S1 (2026-07-07) + harness-frontier-loops (2026-07-06)
tier: operator-guide
status: enriched
---

# Swarm Conductor + Frontier Loops — What We Built 2026-07-06/07 and How to Use It

> Two adjacent sessions, one operating shape. **Harness Frontier Loops** (2026-07-06) closed the router's feedback loop — it LEARNS now — and shipped `/go` as the anti-bottleneck front door. **Swarm Apex Session 1** (2026-07-07) turned `/swarm` from sequential persona simulation into a real conductor on the native Workflow engine: deterministic plan, ONE gate, unattended parallel execution, honest receipt. Plan + verified platform research: `_active/swarm-apex-2026-07-07/PLAN.md` and `research/` (don't redo the research — the briefs are on disk). This guide's job: know when to reach for `/swarm` vs `/go` vs a plain Agent dispatch.

## ⚡ If you only read 10 lines

- `/swarm <objective>` = multi-trajectory fan-out with a plan gate; `--pattern heavy|research`, `--effort low|medium|high`.
- Two patterns LIVE: `heavy` (4/8/12 expert trajectories, dissent-preserving aggregation, adversarial verify) and `research` (6/6/10 subtopics, VERIFIED/LIKELY/UNCONFIRMED claim labels). `mission` and `browser` are NOT built yet (Sessions 3–4).
- Plan step: `python3 execution/swarm_conductor.py plan --brief "<outcome>" --pattern heavy|research --effort low|medium|high --slug <kebab-slug>` → writes `.tmp/swarm/<slug>/mission.md` + prints the exact Workflow invocation.
- Plan gate = compass, not cage: "go without gate" skips the wait, never the mission file.
- After the run: `swarm_conductor.py receipt --slug <slug> --status pass|partial|fail --agents N --tokens N --deliverable <path>` — REAL measured numbers, never estimates. `status` lists all missions.
- Binding constraints: 12-worker cap · workers word-ceilinged (≤500 tokens) · never pin Opus · 🟢/🟡/🔴 grounding tags on every factual claim · no `.claude/agents/` roster.
- Live-fired 2026-07-07: research 15/15 agents, 0 errors, 9.3 min, $0, 2 claims REFUTED pre-delivery; heavy 16/16 agents, 7.9 min, verify pass refuted the mission's own premise. Receipts in `.agent/run-receipts/`.
- The router learns: nightly weight nudges in `.agent/skill-weights.json`, weekly `.agent/router-report-card.md`, synonym queue human-reviewed. **Don't rebuild the router.**
- Hybrid embedding retrieval exists behind `SKILL_ROUTER_EMBED=1` (default OFF); build the cache with `python3 execution/find_skill.py --build-embeddings`.
- Routing frame: one clear deliverable → `/go`. One background worker → plain Agent dispatch. Many independent trajectories on ONE problem → `/swarm`.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/swarm <objective>` | Plan gate → unattended fan-out → deliverable + dissent/claims + receipt | Multi-trajectory work: hard decisions (`heavy`) or factual questions (`research`) |
| `/swarm --pattern heavy --effort high <objective>` | 12 expert trajectories, forks preserved, claim ledger | Strategy/positioning calls where a single-leader blend would hide disagreement |
| `/swarm --pattern research <question>` | Cited narrative + task trace + labeled claim inventory | Any real-world factual question — never answer research from training memory |
| `swarm_conductor.py plan/receipt/status` | Mission file + gate line / honest receipt / mission list | The deterministic ends of every swarm run (the workflow calls these for you) |
| `/go "<messy thought>"` | Mission Card (goal, pattern, tier, gates) → routed single-conductor execution | Anything with one intended deliverable — the default front door |
| Plain `Agent` dispatch | One background worker's result | A single self-contained task (a search, a draft, a review) — no conductor overhead |
| `python3 execution/find_skill.py --build-embeddings` | `.agent/skill-embeddings.json` cache (~$0.007/70s, untracked by design) | Before enabling `SKILL_ROUTER_EMBED=1` |

## The mental model

1. **Every platform is fan-out + synthesis + trace.** The Swarm Apex research verified Manus, Grok Heavy, Kimi, and Perplexity all reduce to this — they win on packaging and one-button UX, and cannot match our 221-persona expert depth or deterministic verification (Perplexity's ~37% citation misattribution IS the wedge). `/swarm` is that shape, natively, with receipts.
2. **The conductor composes; it never absorbs.** `/swarm` is thin: `swarm_conductor.py` scaffolds deterministically, native `.workflow.js` scripts execute, existing hubs stay peers. Council work stays on `/convene` — `/swarm` does not re-wrap it.
3. **Plan-gate then unattended.** One 30-second approval, then hands-off with a receipt at the end. No babysitting, no manual polling.
4. **The router is a closed loop now.** Suggest→load→outcome reconciles in-hook; nightly learning nudges per-skill weights (clamped [0.5, 2.0], decaying to 1.0, stored separately from the index so rebuilds can't clobber them). Fixing routing = feeding the loop, not patching the classifier.

## `/swarm` — the conductor (heavy + research)

**What it is.** Five steps: DICE-score the intent → `swarm_conductor.py plan` writes `.tmp/swarm/<slug>/mission.md` (the Manus-style recitation surface every worker re-reads) and prints the exact `scriptPath` + JSON args → on "go," fire the native Workflow in the background (`heavy` → `swarm-heavy.workflow.js`; `research` → `swarm-research.workflow.js`) → surface deliverable + forks/gaps + claim counts, then write the receipt with measured agents/tokens → full Chain Step 6 finalize (a swarm run gets no lighter finalize than a single-expert one). Rosters are cast at plan time, never re-cast at execution. Strategy-shaped briefs auto-get the PATH DECISION Incumbency Rule written into the mission's constraints.

**When to reach for it.** The tell is *plural independent takes on one problem*: a decision where dissent must survive synthesis (`heavy`), or a factual landscape question needing decomposed parallel search with labeled claims (`research`).

**When NOT to.** Cross-domain deliberation → `/convene` (presets `/council` `/roundtable` `/strike` `/campaign` `/deploy`). Extractions and single-artifact requests → not `/swarm` jobs. Multi-day autonomous missions and browser tasks → **not built yet**; browser work goes through `directives/browser-automation-safety.md` directly. Note: `/swarm-research` as a slash command is a superseded alias to `/deep-research` — the research pattern is `/swarm --pattern research`.

**Worked example (first live fire, 2026-07-07).** Research pattern on the claim-safe content landscape: 15/15 agents, 0 errors, 9.3 min, $0 incremental, 987,945 tokens measured, verify pass REFUTED 2 claims which were corrected pre-delivery; deliverable `research_outputs/2026-07-07-claim-safe-content-landscape.md`, receipt `.agent/run-receipts/2026-07-07T175051Z0000-swarm-research.md`. Same day, heavy pattern on Path-A proof-of-work: 8 named expert lenses, 16/16 agents, 7.9 min, 6/8 lens convergence + 5 preserved forks with falsifiable resolvers — and the verify pass refuted the mission's own load-bearing premise from that morning's research, correcting the answer in place.

**Honest edges.** Sessions 2–4 unshipped: `claim_audit.py`/`gates.py` not yet wired into synthesis, no `mission` pattern (no multi-day resume), no `browser` pattern, no `package_deliverable.py`. On surfaces without the native Workflow tool (Codex), execution degrades to sequential swarm-commander simulation — degraded and *reported*, never hidden. Acceptance bar per platform: same brief run natively vs the subscription, Farrice judges blind; done = subscription cancelled — no blind judgment has been run yet.

## The learning router (frontier loops)

**What it is.** `skill_router_hook` always ranks (the allowlist demoted to a soft floor of 2.5/3.0, with visible "generalist mode" abstention below it); outcomes reconcile deterministically into the routing-intelligence feedback log; nightly `run_routing_learning()` in the evolution orchestrator nudges `.agent/skill-weights.json`; synonym candidates queue in `.agent/synonym-candidates.md` for human review only; a weekly report card lands at `.agent/router-report-card.md` (match rate, weight movers, gaps, loop-alive check).

**When to reach for it.** Routing feels off → read the report card and weight deltas before touching anything. Recall gets fuzzy → consider `SKILL_ROUTER_EMBED=1` (benchmarked top-3 0.67→0.73 at +600ms p95) *after* the report card looks healthy on live weight data.

**When NOT to / landmines.** Never rebuild the router — it learns. Never hand-edit skill-weights.json. If touching the hybrid path: the blend **must stay rescaled to raw BM25 magnitude** — naive [0,1] normalization collapses below the hook's floor and produces silent total abstention. Router-misfire fixes extend the golden set (`verify_control_intent.py`) before patching the classifier.

## /swarm vs /go vs plain Agent — the routing frame

| Situation | Route | Why |
|---|---|---|
| Messy thought, one intended deliverable | `/go` | Compiles a Mission Card against goals + doctrine, picks the pattern (which may itself be swarm) |
| One self-contained task | Plain Agent dispatch | A conductor adds nothing to a single worker |
| Hard decision needing preserved dissent | `/swarm --pattern heavy` | Independent trajectories + adversarial verify |
| Real-world factual question | `/swarm --pattern research` | Decomposed sweep + labeled claims + receipt |
| Cross-domain expert deliberation | `/convene` | Already native; `/swarm` won't re-wrap it |
| High-stakes route needing a failure-map first | `/wargame-mission` pre-flight | Optional layer above the swarm, never forced |
