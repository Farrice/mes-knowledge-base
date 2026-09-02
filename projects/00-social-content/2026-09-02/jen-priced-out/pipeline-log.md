# pipeline-log — jen-priced-out (2026-09-02)

Run of the Scrapes `00-social-content` procedure for a CLIENT brand (Jen Santulan), first time. Orchestrator: Claude (Fable 5.1). Brand context: `_active/clients/jen-listings/brand_context/` (sibling; Farrice's `brand_context/` untouched).

| Phase | What happened | Reasoning |
|---|---|---|
| 1 CONFIG | Jen sibling brand_context created: voice-profile.md (from ENGINE-V2, her memos, client CLAUDE.md), icp.md (from ENGINE-V2 / CONTENT-MIX / strategy brief). No tokens.json for Jen. | The skill is single-brand per project root and its sys-config pins Farrice's brand_context. Running it on Jen with Farrice's context would stamp his voice and palette on her post. A sibling context is the separation. |
| 1 VISUAL guard | Six refs staged at `brand_context/visual_refs/travel-moments/1-6.png` (Canva "Yellow and Black Modern Travel Moments"). Classified INSPIRATION ONLY, not brand. | Jen's verdict 2026-09-02: she hates templatized packaging and yellow/orange. `valley-editions/CANVA-GRAMMAR.md` Design 2 already maps this exact template family to her palette (yellow slot → ivory-steel gradient; `moment` archetype). The Scrapes template factory (6 ssc-template-builder agents + Template Studio approval) was NOT run: it would rebuild the yellow Salford look as her templates. |
| 2 SCENARIO | C: topic → research → post + images. Topic: SFV renters with the down payment saved who feel priced out. | |
| 3 GATHER | Facts from `valley-editions/edition-01/RESEARCH-PACK.md` (Redfin Tarzana, checked 2026-09-02) + one Perplexity search for LA rent / county medians (Aug 2026 sources). `str-trending-research` not used (KEEP OURS per precedence map; needs keys we don't hold). | Claims ledger in post.yaml with VERIFIED / LIKELY labels. |
| 5.0 CONTENT | District: Position (a market read). Hook opens on the reader's situation ("you saved the down payment. still renting."), house is beat two. One job per frame. Register: calm-warm @_jiing lowercase. | Hook checked against `carousel-first-slide-copywriting.md`: ≤8 words, declarative, concrete, earns the swipe (Formula 3, common-sense betrayal: "not priced out"). |
| 5.0.5 / 5.3 VISUAL PLANNING | Done inline by the orchestrator, not via `ssc-designer`. Arc: cover → asking → closed → rent → statement → close. Visual floor: 6/6 frames carry a real photo (anchor). Diversity: 4 archetypes, no two consecutive identical. Plates from the cleared Valley pool + her own listing + her porch portrait; no AI imagery, no stock-looking frames. | `ssc-designer` requires `brand_context/templates/<pool>/manifest.json` and fails loudly without it; Jen has no pool. Inline planning on her approved renderer is the honest path today. Recorded as a known deviation. |
| 5.4 CAPTION | Drafted around the slide arc: walk-in → ✔️ facts → door → her verbatim close → name · Equity Union · DRE → hashtags incl. adjacent cities. | Her caption shape per `jen-listing-send-package-shape`. |
| 5.5 HUMANIZE | `execution/prose_classifier.py check caption.md` → 3.5/10 (low is good). Two signals: ✔️ anaphora and one emoji, both her sanctioned caption shape. `tool-humanizer` not run (ban bank is the gate per precedence map). | |
| 7 IMAGES | `render.py` → `editions.py` archetypes (cover_gem, moment ×3, statement, close), 1080×1350, chrome-headless-shell. Plates swapped after first look: cover archival B&W → `vannuys-valerio-2024.jpg`; "Closed" red-brick bungalow (reads Australian) → her `listing-01-exterior.jpg`. | Her surface, her photos. Cover footer reads "01 / 05" (hardcoded in her renderer; 6 frames) — fix in editions.py next pass. |
| 7.5 STUDIO | Not launched. | Content Studio serves Scrapes-template runs; these frames came from her renderer. Review = the PNGs in this folder. |
| 8 SAVE | post.yaml, caption.md, 01–06 PNGs, this log. Publishing: skip. Sends stay human; Jen thumbs-up first. | |

## Known deviations from the Scrapes procedure (deliberate)
1. No template factory / Studio for Jen (her verdict against templatized packaging; her renderer already exists).
2. Visual planning inline instead of `ssc-designer` (no template pool for Jen).
3. Research via our own receipts instead of `str-trending-research`.

## Before post day
- Re-verify LA median rent ($3,800, single source) or soften to "around $3,800".
- Fix cover footer count in `editions.py` (01 / 06).
- Jen thumbs-up on frames 1–6 and caption.
