# Research Spine — the canonical execution layer for the Avatar Machine

Every wired workflow points here instead of re-stating the chain. This is the single source of truth for **how the Avatar Machine executes real research** so it cold-starts (zero pre-provided material) and grounds every plot in market data — never contextual guessing.

> **Rule zero:** the model *reasons*; tools *ground*. The structure (Pain Matrix, Core Wound, Anti-Hero prose, Epiphany calibration) is the model's job. The raw inputs (market landscape, verbatim VOC, live hooks) MUST come from real tools. Collapsing those layers — letting the model invent "specific language" — is the failure this spine exists to prevent (genius.md rubric criterion 6).

---

## Canonical artifacts (fixed paths)

| File | Holds | Produced by |
|---|---|---|
| `.tmp/copy-engine/deep-research.md` | Market-landscape foundation (demographics, problem/symptoms, failed solutions, objections, beliefs, pricing, zeitgeist) | Gemini Deep Research (PRIMARY) |
| `.tmp/copy-engine/voc-pack.md` | ≥30 verbatim VOC soundbites + 30–40 live hooks, each with a source URL/handle | `/buyer-sourcer` (MCP-rich mining) or the runner's Apify pull |
| `.tmp/copy-engine/<slug>/ground-dossier.md` | The two above, concatenated + GROUND STATUS, for orchestrated multi-market runs | `execution/avatar_manifold_runner.py` |
| `.tmp/copy-engine/ground-status.json` | `{status: PASS|PARTIAL|DEGRADED, sources, modeled_flags}` | the runner / floor-check |

Workflows **load** these. If they exist, ground off them. If absent and the workflow runs standalone (not `--no-ground`), fire the targeted pull below.

---

## The canonical chain (priority order)

1. **Gemini Deep Research — PRIMARY.** Self-gates at the $10 prepaid ceiling (`.agent/gemini-api-usage.json`, `MIN_BALANCE_USD 0.50`, 5-query/task cap). Raises `BudgetExhaustedError` → fall to step 2.
   ```bash
   // turbo
   mkdir -p .tmp/copy-engine
   python3 execution/deep_research_client.py "<query>" --mode standard|max --task-context "avatar-<slug>" \
     > .tmp/copy-engine/deep-research.md 2>/dev/null \
     || echo "DEGRADE: Gemini unavailable → Perplexity, else recall-only + [MODELED]"
   ```
2. **Perplexity — FALLBACK.** MCP `mcp__perplexity-ask__perplexity_research` (or `execution/perplexity_client.py`, `model="sonar-deep-research"`). $30/mo, `.agent/perplexity-usage.json`.
3. **Apify — VOC SCRAPING** (raw voices, not synthesis). Never raises; returns `{"fallback":true}` on budget exhaustion.
   ```bash
   // turbo
   python3 execution/apify_client.py reddit "<niche pain>" --limit 50 --comments    # primary: raw private-monologue language
   python3 execution/apify_client.py amazon "<adjacent product>" --limit 30          # failed-solution + post-purchase soundbites
   python3 execution/apify_client.py youtube "<niche>" --limit 10 --transcript       # beliefs, objections, market addictions
   ```
4. **Playwright MCP — LIVE HOOKS / GATED** (`mcp__playwright__browser_navigate` → `browser_snapshot`/`browser_evaluate`). FB Ad Library (`facebook.com/ads/library`), login-gated funnels, JS-rendered review pages. Tier-1 read-only auto-fires per `directives/browser-automation-safety.md`. The Python runner cannot call MCP — this is model-side (run inside `/buyer-sourcer` or a dispatched `deep-research` sub-agent).
5. **Recall — EXPERT GROUNDING** (`mcp__recall__search`, focused, 2 queries). Tier-1.5 precedent/framework grounding. Free, auto-fires.

**The division of labor:** Apify/Playwright/Perplexity *gather raw voices*; Gemini/Perplexity *synthesize themes*; the model *produces the deliverable*. Never collapse (the `icp-research.md` architectural rule). Collapsing = "structurally sound but flat" output.

---

## The cold-start sequence (zero pre-provided material)

Fired by `execution/avatar_manifold_runner.py ground` OR `/avatar-manifold` PHASE 0:
1. Gemini foundation query (`--mode max` for the full manifold; `standard` for a single framework) → `deep-research.md`.
2. Apify VOC (reddit primary + amazon + youtube) → assembled into `voc-pack.md`, each soundbite source-tagged.
3. Playwright FB Ad Library + Recall (model-side, additive) → live hooks + expert grounding appended to `voc-pack.md`.
4. Floor-check + `research_quality_gate.py validate <file> --strict` → set GROUND STATUS.

---

## Graceful-degradation ladder (one place, all workflows obey)

| Tool exhausted | Reroute to |
|---|---|
| Gemini `BudgetExhaustedError` | Perplexity `sonar-deep-research` |
| Perplexity < $1 | free `search_web` + `read_url_content` (WebFetch) |
| Apify `{"fallback":true}` | Perplexity verbatim-quote query ("find 30 verbatim quotes from real <ICP>…") → `search_web` |
| Playwright unavailable | skip FB Ad Library; note the gap; hooks rely on Gemini-found angles |
| **Everything exhausted** | GROUND STATUS `DEGRADED`; every soundbite forced `[MODELED — replace with VOC]`; the manifold still builds (model reasons over framework structure) but is loudly flagged not-market-pulled |

---

## The real-VOC rule (the deterministic backstop)

Any soundbite **without a traceable source URL/handle** is mechanically tagged `[MODELED — replace with VOC]`. Real-VOC is the default *by construction*; the model cannot launder invented phrases into `[VOC]` because the tag is bound to the presence of a URL, not the model's judgment. Enforced by the floor-check every wired workflow runs:

```bash
// turbo
python3 - <<'PY' || echo "GROUND GATE: thin/unsourced — re-mine before proceeding"
import re,sys,glob
f=glob.glob(".tmp/copy-engine/voc-pack.md")+glob.glob(".tmp/copy-engine/*/voc-pack.md")
if not f: sys.exit(1)
t=open(f[0]).read()
urls=len(re.findall(r'https?://',t)); modeled=t.upper().count("[MODELED]")
print(f"VOC pack: {urls} source links, {modeled} [MODELED] flags")
sys.exit(0 if urls>=15 and modeled==0 else 1)
PY
```

`research_quality_gate.py validate <dossier> --strict` independently audits: ≥15 sources, provenance ≥80%, recency 2024+, no echo chamber.

---

## Cost discipline — tiers, reuse, and the iteration contract

**Research is a COLD-START cost, not a per-pass cost.** This is the rule that keeps the arsenal cheap to run.

**Three tiers** (`avatar_manifold_runner.py ground --tier …`; see `estimate` for live numbers):
| Tier | Cost | Fires | Use when |
|---|---|---|---|
| `free` | **$0** | HN Algolia VOC + model-side Recall/WebFetch/Playwright/search_web (real live social listening) | budget-conscious cold start |
| `lean` | **~$0.10** | free VOC + Apify amazon/youtube accelerator | cheap-but-real default |
| `deep` | **~$0.60 (std) / ~$1.60 (max)** | Gemini Deep Research synthesis + free VOC + Apify | want the deep synthesized foundation |

**The reuse gate (budget-saver):** a fresh dossier (`< --max-age-days`, default 30) is **reused at $0** — the runner prints `♻️ Reusing cached GROUND`. So:
- **Cold start** → research fires once (tier-selected, cost shown up front, `--dry-run` to preview).
- **Every iteration after** — writers-room passes, variants, refinement, re-runs of `/manifold-to-copy` — **reuses the cached dossier, $0.** Never re-fires.
- Re-fire only with `--refresh`, or when the dossier is stale (warns, doesn't force).

**Real VOC source reality (verified live 2026-05-31):** Gemini Deep Research is the reliable Python-side path (deep web-grounded synthesis). Reddit 403s server-side, so verbatim VOC at scale comes **model-side** (WebFetch/Playwright/Recall — proper browser infra) plus the free HN API. The runner never reports a false PASS: empty Gemini → Perplexity fallback; thin VOC → routes to model-side mining + flags `[MODELED]`.

## Cost & gates

| Tool | Per-run cost | Gate |
|---|---|---|
| Gemini Deep Research | $0.50 (standard) – $1.50 (max) | self-gates, $10 prepaid ceiling |
| Apify VOC | ~$0.10 (reddit 50 + amazon 30 + youtube 10) | self-gates, $29/mo, hard-stop 90% |
| Perplexity | $0 unless fallback (~$0.25) | $30/mo |
| Playwright / Recall | free | — |
| **Session gate (G2)** | — | `python3 execution/cost_gate.py status` — `SESSION_SOFT_CAP_USD 5.00` |

Typical full cold-start manifold run ≈ **$1–2**. Check `cost_gate.py status` first when a session has already spent on paid APIs.

---

## How a workflow references this spine

Each wired workflow opens its GROUND section with:
> *"Load `references/research-spine.md`. If the cold-start dossier (`.tmp/copy-engine/deep-research.md` + `voc-pack.md`) exists, ground off it. Else, if standalone and not `--no-ground`, fire the targeted pull for the dimensions this workflow needs (below)."*

It then names only its *specific* queries/sources — never re-states the chain, the fallbacks, or the gates. Those live here.
