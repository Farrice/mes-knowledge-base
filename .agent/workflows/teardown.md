---
description: The Teardown Engine — point it at a named brand, reverse-engineer their customer's avatar (better than they know it), write copy that out-converts their live assets, package the before/after, and brand-jack it constructively on LinkedIn. The flagship demonstration of the Avatar + Copy Engine OS.
tier: system
wired: true
---

# /teardown — The Teardown Engine (the demonstration IS the marketing)

Point this at any brand. It reverse-engineers their customer's avatar from **real social listening**, writes copy that beats their live assets, packages the before/after, and produces a constructive LinkedIn brand-jack post. It is to a **named brand** what `/avatar-machine` is to a **cold market** — the same Ground-Once spine, with a reconnaissance front-end (capture THEIR copy) and a public-demonstration back-end.

> **The fusion:** this is not a separate product. It is the *proof* of the core product — best-in-market avatar research + end-to-end converting copy. You don't claim it; you show it, on a brand everyone recognizes. The fused artifact is the marketing, the lead engine, and the product demo at once.

> **80% composition.** Every phase calls an existing piece. The only teardown-specific code is `execution/teardown_ethics_gate.py` (the constructive/legal floor). The quality moat stays in Python: `verify_proof_ledger` (G5) + `chain_runner.finalize` (Gate C) + the ethics gate.

## Usage
```
/teardown <brand or url> [--angle their-own-customer|competitor-of-target] [--asset auto|vsl|ad|email|landing]
```
Slug: `teardown-<brand-kebab>`. Scratch: `.tmp/teardown/<slug>/`. State: `projects/<slug>/state.yaml`.

## Cost
~$0.61 one-time grounding (Gemini + VOC, self-gated, fails closed to $0). Recon is free-tools-first (~$0–$0.10). Copy + artifact + post are **$0** (WARM cache reuse). Re-running on the same brand = $0.

---

## PHASE 0 — INTAKE + ETHICS FRAME (Gate T0)
Parse: **brand · url · category · angle** (`their-own-customer` = rewrite for the target's own audience · `competitor-of-target` = reverse-engineer Brand X to help a different client beat them — the paid-audit path). Slugify.
```bash
// turbo
python3 execution/anchor_memory.py init <slug> --audience "<target's customer market>" 2>/dev/null || python3 execution/anchor_memory.py load <slug>
python3 execution/teardown_ethics_gate.py intake --brand "<brand>" --angle <angle> --request "<the user's framing>" --workflow teardown
```
**Gate T0 (halt):** four fields named AND ethics `intake` verdict ∈ {PASS, REVIEW}. A **BLOCK** means the framing is hit-piece-shaped — reframe to constructive ("what they got right / what I'd improve") and re-run. *Tear down the COPY, never the PEOPLE.*

## PHASE 1 — RECONNAISSANCE (capture THEIR live copy)
Reuse `/competitor-intel` + `/spy-market`, plus live capture. Free tools first.
- `mcp__perplexity-ask__perplexity_ask` — positioning, category, public claims.
- **WebFetch** their hero/pricing/landing (SSR). **Playwright** (`browser_navigate` → `browser_snapshot`/`browser_take_screenshot`) for the live site AND `facebook.com/ads/library/?q=<brand>` to capture **running ad copy + hooks** (this is the asset-type list Phase 3 must beat).
- Write `.tmp/teardown/<slug>/recon.md`: their headline · subhead · CTA · mechanism claims · proof claims · **asset-type inventory** (VSL/FB ad/landing/email) · screenshot paths.
```bash
// turbo
python3 execution/anchor_memory.py anchor <slug> --type competitor_recon --path .tmp/teardown/<slug>/recon.md --desc "target live copy + asset inventory" --ref-for "ground,beating-copy,teardown-artifact"
```
**Gate T1 (light):** recon.md has ≥1 verbatim live asset + the inventory, OR proceed flagged "copy not publicly capturable" (then Phase 4 before/after compares positioning, not copy).

## PHASE 2 — GROUND THEIR CUSTOMER'S AVATAR (the chokepoint — the differentiator)
The **one grounding chokepoint** — identical call the OS already routes through. This is the avatar research the demo foregrounds: *we know their customer's core wound; they guessed.*
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<target's customer>" --product "<target's offer>" --tier deep 2>&1 | tail -6
cat .tmp/copy-engine/<slug>/ground-status.json
```
Then build the full **Avatar Manifold** by delegating to `/avatar-machine` Phases 2–3 (do NOT re-implement the 6 dependency batches — call the workflow). **Gate T2 = the existing G2:** dossier exists AND `voc_source_urls ≥ 15` OR `[MODELED]` accepted explicitly.

## PHASE 3 — BEATING COPY ($0 — WARM reuse)
For each asset type captured in `recon.md`, invoke `/copy-engine` (slug already grounded → WARM → $0):
```
/copy-engine write a converting <asset> for <target's offer> / market: <target's customer> / objective: out-convert <brand>'s live <asset>
```
Each produces a draft + `proof-claims.md` and passes **Gate G5** (`verify_proof_ledger`) — every stat/price the rewrite asserts is labeled before it reaches the public teardown. *This is the structural reason the rewrite is safer than a hand-written hot take.*

## PHASE 4 — THE TEARDOWN ARTIFACT (before/after + the avatar insight)
Assemble `.tmp/teardown/<slug>/teardown.md`:
1. **Avatar Intelligence** (lead with this) — the core wound / identity-safe angle / Pain-Matrix leverage dim the brand's copy misses. *This is the "better avatar research than anyone" proof.*
2. **Before / After** — their live copy (**excerpt ≤25% + transformed**, never reproduced) vs the grounded rewrite, side by side.
3. **What they're leaving on the table** — the specific dimension their copy doesn't touch.
4. **Why the rewrite converts** — mapped to belief-state sequencing, not opinion.
```bash
// turbo
python3 execution/teardown_ethics_gate.py check --brand "<brand>" --file .tmp/teardown/<slug>/teardown.md --recon .tmp/teardown/<slug>/recon.md --workflow teardown
python3 execution/verify_proof_ledger.py --draft .tmp/teardown/<slug>/teardown.md --ledger .tmp/copy-engine/<slug>/proof-claims.md 2>/dev/null || echo "label/cut brand-claims before delivery"
```
**Gate T4:** ethics `check` exits 0 (not BLOCK) AND every factual claim *about the brand* is labeled. Then `/package-deliverable` (Tier 1 Gamma for the public version; Tier 3 HTML→PDF for a paid audit).

## PHASE 5 — PUBLIC DEMONSTRATION (the distribution engine)
Invoke `/jackpost` with **brandjack** pre-selected, handing it `recon.md` + `teardown.md` (so it skips re-research). Its native 3-angle triad — **What They Did Right / What They Missed / What This Means For You** — IS the constructive frame. Lead with "What They Did Right."
```
/jackpost "<brand> — what their copy misses about their own customer" --platform linkedin
```
```bash
// turbo
python3 execution/teardown_ethics_gate.py public --brand "<brand>" --file .tmp/teardown/<slug>/linkedin-post.md --recon .tmp/teardown/<slug>/recon.md --workflow teardown
```
**Gate T5 (strictest):** ethics `public` exits 0 on the FINAL post. *The post is delivered ready — the user posts it.* Auto-posting is out of scope.

## FINALIZE (Gate C — per artifact, never batch) + tracking
```bash
// turbo
python3 execution/chain_runner.py finalize "Teardown — <brand> (<angle>)" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow teardown --type Content \
  --intent N --expert-score N --adversarial N --factual <score-from-ledger> \
  --sub-agents N --critical-path 5 --anchor-named \
  --project <slug> --anchor-type teardown_artifact --anchor-path .tmp/teardown/<slug>/teardown.md \
  --notes "GROUND=<status>. Recon assets=K. Ethics=PASS. Angle=<angle>." \
  --source-request "<original request>"
python3 execution/revenue_tracker.py log "Teardown — <brand>" --skill teardown --expert luke-iha --type lead --outcome "public demo drafted" --revenue 0 2>/dev/null || true
```
**Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match** (finalize exits 0 even when it blocks). Re-`revenue_tracker log --revenue N` when a teardown converts to a paid audit.

---

## Phase → existing-piece map
| Phase | Calls (existing) | New? | Gate | Anchor out |
|---|---|---|---|---|
| 0 Intake | `anchor_memory init` + `teardown_ethics_gate intake` | gate only | **T0** | — |
| 1 Recon | `/competitor-intel`, `/spy-market`, Playwright FB Ad Library | no | T1 | `competitor_recon` |
| 2 Ground | `avatar_manifold_runner ground` → `/avatar-machine` P2–3 | no | **G2** | `avatar_manifold` |
| 3 Beating copy | `/copy-engine` ×N (WARM, $0) | no | **G5** | `copy` |
| 4 Artifact | assembler → `teardown_ethics_gate check` → `/package-deliverable` | gate only | **T4** | `teardown_artifact` |
| 5 Public | `/jackpost` brandjack → `teardown_ethics_gate public` | gate only | **T5** | — |
| Finalize | `chain_runner finalize` ×per-artifact + `revenue_tracker` | no | **C** | — |

## Ethics (the constructive/legal floor — `execution/teardown_ethics_gate.py`)
Three deterministic fires: `intake` (P0, catch hit-piece framing before spend), `check` (P4, load-bearing — constructive marker required, verbatim-reproduction guard ≥40 words, brand-claims defer to `verify_proof_ledger`), `public` (P5, strictest on the shipped post). BLOCK → exit 2 → the `// turbo` line halts. Logged to `.agent/teardown-ethics-log.jsonl`. **Tear down the copy, not the people; excerpt + transform, never reproduce; assert nothing about the brand you can't source.**

## Productization
Free public teardown series = the lead engine (Rung 0.5). The CTA converts to the **$1,500 Competitor Teardown Audit** (Rung 1.5) → Authority Foundation → FCAO anchor. See `_active/farrice-brand/offers/avatar-copy-engine-offer.md`.
