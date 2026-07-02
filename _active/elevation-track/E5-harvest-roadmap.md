# E5 — Breadth-Harvest Roadmap
*2026-07-02 · Elevation Track · capability contract for the next extraction wave*

> **Contract**: every target below ships to `directives/embodiment-standard.md` (10-item checklist + P7.4 blind-pass). This is **capability planning, not repositioning** — targets serve Path A and existing engines only. **INCUMBENCY RULE honored**: no target introduces a new position or offer (`project_path-decision-2026-07-01`). Breadth without dedup rebuilt the 2026-01 hollow stratum once; the per-target DEDUP VERDICT (grep-verified against `skills/` + `DOMAIN_REGISTRY.md`) is mandatory.

## 1. Demand Signals (evidence only)

- **Gap log is THIN and not yet actionable.** `.agent/gap-log.md` holds exactly one entry — an out-of-domain fluke (`cavitation-diagnose-excavator`, hydraulic excavator noise, score 1.2). The log was created today and auto-populates from `skill_router_hook` from now on; it feeds this roadmap **continuously going forward**, but at n=1 it carries no signal. This wave is therefore driven by **registry-vs-census coverage analysis**, not miss-frequency.
- **Census says the debt is retrofit, not breadth.** 137/324 skills carry any usage; the flagged mass (81% of bulk-01) is the *retrofit* backlog (flagged × usage — Lara-mastery, luke-iha-copy-blocks, futurepedia, oren-operational, creative-direction). Those are **not** harvest targets — retrofit proceeds independently (§3). The harvest signal is **negative space**: domains absent from the 96-agent / 16-domain registry.
- **The acute gap is Path A's own name.** Path A = *claim-safe content for funded health brands*; the LinkedIn beachhead (`farrice-engine`) = wellness/fitness/performance **BRANDS**. Yet across all 96 agents / 16 domains there is **zero regulatory / claim-safe / substantiation expertise** (grep `complian|regulat|ftc|fda|dshea|legal|claim-safe` → none). Domain 16 covers fitness **coaching** subject matter (Galpin/Israetel/Teo/Aragon); Domain 1 covers DR persuasion (`jw-engine`, `copy-engine`) — **neither carries a claim-substantiation gate.** Every health-brand claim `farrice-engine` produces is currently improvised against no expert.
- **"Coaching" ≠ "funded brand."** The roster serves the *coaching business* buyer (`yuri-elkaim-health-coaching-business`, `strength-conditioning`) and generic CPG (`ross-mckay-premium-at-scale`). No expert owns marketing strategy for a **funded wellness/supplement brand** — the actual Path A client.

**Single strongest signal:** the entire expert roster contains no regulatory/claim-safe capability while the flagship engine ships health-brand claims daily. This is a live liability, not a nice-to-have.

## 2. Target List (ranked; DEDUP VERDICT grep-verified)

| # | Domain gap | Serves | DEDUP VERDICT | Source type | Shape | Route |
|---|---|---|---|---|---|---|
| **1** | **Claim-safe / regulatory health marketing** (FTC Health Products Compliance Guidance 2022, FDA structure-function vs. disease claims, DSHEA, NAD) | Path A core + backstops `farrice-engine`/`jw-engine`/`copy-engine` — the missing substantiation gate | **NEW** — grep `complian\|regulat\|ftc\|fda\|dshea\|claim-safe` → 0 hits across 338 skill dirs | FTC guidance doc + supplement regulatory-affairs course/attorney interview (public: CRN, FTC .gov) | Single skill w/ a deterministic claim-classifier workflow (structure-function / disease / unqualified) | `/extract-forge` (rich, multi-source; needs enrichment) |
| **2** | **Funded health/wellness/supplement BRAND marketing strategy** (brand-side, not coaching) | Path A client = the funded-brand marketing lead the beachhead sells to | **NEW** — nearest are `ross-mckay-premium-at-scale` (generic CPG) + `yuri-elkaim` (coaching biz); distinct client & altitude | Health-brand founder/CMO interview (AG1/Ritual/Seed-tier operators) | Single skill | `/extract-forge` |
| **3** | **Science / evidence-to-content translation** (turn a study into accurate + compelling copy) | Feeds Target 1's substantiation + `jw-engine`/`copy-engine` accuracy | **NEW** — `alex-content-science` is viral-mechanics reverse-engineering, not evidence handling; Aragon's claim-autopsy is coaching-facing | Science-communication book or a health-science communicator interview | Single skill | `/extract-forge` |
| **4** | **DTC lifecycle / retention email** (Klaviyo flows, post-purchase, LTV) | Health brands live on retention; extends the money path beyond acquisition | **EXTEND** — `matt-mcgarry-newsletters` (newsletter-only) + `vince-nijhof-dtc-operator-system` (paid-first, no retention lane); add a lifecycle workflow set, don't rebuild | Retention/email operator course or interview | Extend `vince-nijhof` **or** `matt-mcgarry` w/ a lifecycle workflow module | `/extract` (single-source; add workflows) |
| **5** | **Creator / influencer partnership + whitelisting/seeding** (brand-side) | DTC health brands run on creator seeding + spark ads; no brand-side owner | **NEW** — `adam-enfroy` (SEO affiliate blogs), `darrel-wilson` (AI affiliate) are creator-*side* SEO, not brand-side seeding/whitelisting | Brand influencer-ops interview/course | Single skill | `/extract` |
| 6 | Performance/UGC ad creative for DTC | acquisition | **ALREADY-COVERED — drop** — `dara-denney-meta-ads`, `sarah-levinger-ad-psychology`, `sabri-suby`, `alex-copper`, `omar-eddaoudi-premium-ads`, `vince-nijhof` | — | — | — |
| 7 | B2B content ops / audience intelligence for brands | brand content | **ALREADY-COVERED — drop** — `kieran-flanagan-{content-engine,content-ops,audience-intelligence}` | — | — | — |
| 8 | CRO / voice-of-customer / landing-page testing | conversion | **ALREADY-COVERED — drop** — `joanna-wiebe-persuasion-mastery` + Domain 1 evaluation lane | — | — | — |

Targets 6–8 are listed to **show the dedup gate firing**, not to build. The wave = Targets 1–5 (three NEW, one EXTEND, one NEW), Path-A-ranked.

## 3. Standing Rules

- **Embodiment standard is non-optional.** Every target runs the full `directives/embodiment-standard.md` checklist and a **P7.4 blind-pass before ship**; finalize scores are evidence-derived, and any dimension ≥8 must `--anchor-named` a `rubric_v1.md` anchor. ≥1 eval entry per shipped extraction appended to `eval_set_v1.jsonl`.
- **Census re-run after the wave.** `python3 execution/skill_census.py run` once all targets ship; the harvest stratum's ~6% flag rate is the bar to hold.
- **Retrofit backlog (bulk-01) runs independently.** Priority = flagged × usage (Lara-mastery, luke-iha-copy-blocks, futurepedia, oren-operational, creative-direction). It is **NOT part of this wave** — do not fold retrofit and harvest into one pass.
- **Gap log feeds this roadmap continuously.** Re-derive Target ranking whenever a domain hits 3+ misses (`gap_analysis.py recommendations`).

## 4. Explicitly NOT in This Wave

- **Anything requiring new positioning or a new offer.** INCUMBENCY RULE: no repositioning/offer docs until $5K/mo collected. These targets add *capability under the existing Path A*; if any extraction starts implying a new service line, stop and re-scope.
- **No rebuild of `how-i-write`, `jw-engine`, `copy-engine`, or `writers-room`.** These engines are good — **extend, never rebuild** (`feedback_multi-engine-rebuild-degrades-elevated-content`: rebuilding elevated work degraded it to 3/10). Target 3 *feeds* copy/jw engines; it does not replace them. Target 4 *extends* an existing DTC/newsletter skill.
- **No duplicate ad-creative, B2B-content, or CRO extractions** (Targets 6–8 dropped — roster already deep).
- **No new writing-craft experts** — the How-I-Write OS and story-stack already saturate that lane.
