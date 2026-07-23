---
date: 2026-07-23
session: fladlien-build
tier: operator-guide
status: enriched
---

# Jason Fladlien OS — What We Built 2026-07-19→23 and How to Use It

> Three passes turned the Fladlien skill from 31 workflows into a complete persuasion operating system: a watched-source forge expansion (5 new Tier-8 workflows + genius tranche 3), a standard-verification gap-close (+6 recovered secrets), and the full harvest of his own 55-pattern document (56 patterns / 10 categories / 39.6k words + 494 table rows) — deployed three ways: repo reference bank, born-v2 prompts, and a rebuilt database in Farrice's Notion. Companions: `skills/jason-fladlien-marketing/SKILL.md` (the 36-workflow map), `references/pattern-bank/INDEX.md` (the 56-pattern table), `extractions/jason-fladlien/amplification-2026-07-19.md` (coverage map).

## ⚡ If you only read 10 lines

- `/fladlien-best-90` — the opening diagnostic for ANY business: "your best 90 minutes — where does it exist?" 99% answer "it doesn't"; that gap is the pitch.
- `/fladlien-pattern-bank` — line-level persuasion injection from all 56 patterns; it must Read `references/pattern-bank/<category>.md` at fire time (Quality Gate enforces).
- `/fladlien-point-engine` — teaching spine: ≤4 principles × ≤4 evidence, Setup 50% / Payoff 45% / Tie-down 5%, emotional state named per point BEFORE content.
- `/fladlien-tie-down` — audit pass on any finished script: gap-bisection until no tie-down gap dwarfs the median; ≥2 major commitments.
- `/fladlien-set-setting` — sell the smaller outcome sooner ("$100 a month from now, not $1M a year"); ideal-vs-realistic dual frame is the native compliant structure.
- Full stack order: game-selection → research → set-setting → offer/offer-anatomy → best-90 → point-engine → fear-engine/keys → tie-down → pattern-bank.
- Doctrine line: "We don't optimize for the yes. We remove the reasons to say no, and yes becomes inevitable."
- A-tier verdict is PENDING Farrice: read `extractions/jason-fladlien-marketing/blind-pass-specimen-2026-07-19.md` beside `reference-corpus/`, then `blind_pass.py record`.
- Notion copy: Knowledge Vault → "Persuasive Patterns | Jason Fladlien — Full 56-Pattern Library" (child DB `3a649875-a897-81e7-a1d1-f5ebe5675c2f`).
- Scrape lesson (solution card): Notion api/v3 paginates via cursor — 200 + big JSON ≠ complete; run the missing-ref invariant.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/fladlien-best-90` | 90-min asset blueprint + Two Agendas opener + time-or-money fork | A business has no single asset showing its best 90 minutes (almost all) |
| `/fladlien-pattern-bank` | Pattern-injected rewrite + Pattern Map (replaced-line discipline) | Any conversation/copy/DM/script that's all claims and direct asks |
| `/fladlien-point-engine` | 4×4 grid + per-point SPT scripts w/ named emotional states | Building any teaching block that precedes an ask |
| `/fladlien-tie-down` | Gap map + inserted tie-downs + ≥2 major commitments | A finished script that "taught well" but closes soft |
| `/fladlien-set-setting` | Solve-for reframe + dual outcome frame + least-change ladder | Big-promise offer with soft conversion; regulated niches |
| `/fladlien-game-selection` | Play/pass verdict (now opens with the 3-element test) | Before entering any market/project/client |
| `python3 execution/blind_pass.py record --expert jason-fladlien-marketing --verdict PASS\|FAIL --notes "..."` | A-tier promotion or held B | After Farrice's side-by-side read |

## The mental model

1. **Subtraction → focus → leverage** is the whole system. Every layer (offer, webinar, pattern) removes reasons to say no before adding reasons to say yes; fear-work converts because it's the underserved register, the same scarcity logic as radical candor.
2. **Points are three-beat units.** Nothing ships as a bare payoff — setup earns the emotional state, the tie-down banks the agreement. This scales from a 2-hour webinar down to one DM line.
3. **The patterns are primitives, not scripts.** The 10 categories each pull one lever (attention inward, fact-fusion, identity, staircase, the unspoken, constraints, contrast, reframe, future-pacing, building blocks). Deploy 2-4 per piece by diagnosis, never all ten; the injection replaces a weaker normal line or it doesn't go in.

## Capability: Tier-8 workflows (forge expansion, 2026-07-19)

**What it is**: 5 workflows + born-v2 prompts extracted from two watched sources (his 8:26 patterns video — 40 frames read, verified no on-screen schema — and the 2h21m Charlie Morgan interview, 28.6k words). Genius tranche 3 added patterns §36-44 (Two Agendas, local-transformation-global-promise, 4×4 grid, 50/45/5 SPT, tie-down density, set & setting, identity-by-collapse, best-90, whale-door) plus 12 hidden-knowledge items and 3 verbatim exemplars (Marshmallow Save, Confidence Paradox, Hundredth Webinar Confession).
**When to reach for it**: any teach-then-sell asset, high-ticket presentation, or offer repositioning.
**When NOT to**: pure brand/editorial voice work — route `/voice-os` + writers-room; Fladlien is a conversion layer, not Farrice's voice.
**Honest edges**: blind pass is model-judged only (EVAL-049 PASS); A-tier awaits Farrice. The Tier-8 workflows have zero live deployments yet — first real run should be Proof-to-Market.

## Capability: the full 56-pattern bank (2026-07-23)

**What it is**: Fladlien's own "Persuasive Patterns" document, scraped complete from his public Notion (after DM), 39,608 body words + 494 table rows. Repo home: `references/pattern-bank/` (INDEX + 10 category files, each pattern = structure template + examples + multi-section Why-It-Works). Notion home: Knowledge Vault child DB, all 56 rows verified block-for-block (v1 incomplete rows archived in trash — expected).
**How to invoke**: via `/fladlien-pattern-bank` (which mandates fire-time category reads), or open INDEX.md directly for the quick table.
**Worked example**: Embedded Commands page — repetition familiarity ("decide, decide, decide"), negation processing ("the mind must represent the idea before it can process the negation"), autonomy preservation — now with its full 115-block body.
**Honest edges**: the bank is Fladlien's claims about his own patterns, not independently verified conversion data; deployment in regulated niches still passes through compliant-grip rules (specificity moves, never strips) and the Reader Contract.

## Capability: the scrape method (reusable beyond Fladlien)

**What it is**: public notion.site harvesting via api/v3 — `queryCollection` for rows, `loadCachedPageChunk` WITH cursor-follow per page, missing-ref invariant + block-type coverage audit before compiling, then rebuild into Farrice's Notion via `execution/notion_api.py` (pinned 2022-06-28; child DB under a Knowledge Vault entry — integration can't create top-level pages).
**When to reach for it**: any shared Notion doc whose Duplicate button drops subpage bodies (they all do when the share is view-only).
**When NOT to**: JS-only single pages — plain Playwright snapshot is cheaper.
**Honest edges**: `syncRecordValues` is 403 on public sites (pagination is the only recovery); rate-limit sleeps (~0.35s) make 56-page migrations ~2 min.
**Solution card**: `docs/solutions/2026-07-23-notion-cached-chunk-cursor-pagination.md`.

## Composition options (never forced)

| Stack | When it earns its cost |
|---|---|
| best-90 → point-engine → tie-down → pattern-bank | Building a real selling asset end-to-end (Proof-to-Market first candidate) |
| pattern-bank × `/ml-opinion-ladder` | Auditing Lakajev's DM sequence for which Fladlien primitives it already uses |
| set-setting × `/avatar-machine` | The solve-for reframe needs the market's realistic-outcome threshold |
| point-engine × Kallaway content OS | Short-form teaching blocks with setup-stakes retention |

## Open items

- Farrice blind-pass verdict (A-tier gate) — specimen + corpus staged.
- Git divergence recovery pass: `origin/brief/2026-07-21` (+1), `origin/session/2026-07-20` (+1) — recover files first, never `merge -s ours`.
- Notion DB "Deployed In" relation column (usage tracker) — idea, unbuilt.
