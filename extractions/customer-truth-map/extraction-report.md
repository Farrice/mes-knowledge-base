# Extraction Report — Customer Truth Map (Blazing Zebra)

**Method:** MES 3.0 Deep (extract-forge). **Date:** 2026-06-21.
**Sources:** PDF "The Customer Truth Map" (13pp) + video `GAVILEkfsvE` ("Master TARGETED Market
Research… with NotebookLM", Blazing Zebra; transcript: `transcript.txt`, 2,924 words).
**Expert:** Blazing Zebra (former marketing-agency owner; ran enterprise VoC survey programs).
**Domain:** Voice-of-Customer language mining → empathy-map truth map → JTBD → gap analysis → apply
→ refresh. **Disposition:** NEW skill (`skills/customer-truth-map/`), standalone-that-composes.

## Uniqueness audit (vs. existing stack)
Genuinely net-new: the empathy-map (Say/Think/Feel/Do) + pains/gains structure, the verbatim
real-language discipline, the Do-category workaround mining, the gap-table ranking, and the
living-document/freshness loop with a change-log-as-asset. Existing skills it composes rather than
duplicates: `/buyer-sourcer` (luke-iha) for heavy VoC mining, `/mcraney-deep-canvass` for belief
excavation, consumer-posture for identity. No existing skill owns the empathy-map→JTBD→gap→refresh
loop. Confirmed distinct from `belief-first-audience-intelligence` (belief-centric, not language-
mining-centric).

## Genius patterns (12) — see `skills/customer-truth-map/genius.md`
Words-as-gold/AI-as-sorter · Unprompted>prompted · Keep-the-typos · The verbatim rule · Do-category
goldmine · Pain→Job reframe · Widest-gap-first · Quote-to-slot · Grounded-idea generation ·
Triangulation · Freshness-as-edge · Honest-about-tools.

## Hidden knowledge (8) — see genius.md
Own past conversations are often the best source · narrowest target wins · stop when it stops
surprising · work in chunks · bracket for sense never paraphrase · NotebookLM-gathers/chat-builds ·
what AI reliably does vs. doesn't · change-log becomes its own asset.

## Signature moves (7) — see genius.md
Name problems in their voice first · the verbatim re-issue · circle the workarounds · rank by gap
width · one quote per idea · confidence-label cross-source · date the top of the map.

## Hall of Fame exemplars (3 + anti) — see genius.md
The follow-up reframe (JTBD) · the Do-category catch (Monday spreadsheet) · quote-to-slot · anti:
the tidy paraphrase that reads like marketing.

## Quality rubric (9 criteria) — see `references/quality-rubric.md`
Verbatim Integrity (veto) · Unprompted Sourcing · Narrowness · Map Completeness · Do-Category Mining
· Job Depth · Gap Ranking · Put-to-Work Fidelity · Freshness Discipline.

## Architecture built
1 orchestrator + 12 workflows (`/ctm-*`); SKILL.md + genius.md + 9 references + agent persona.
**Surpass layer:** wired gather (Apify reddit / NotebookLM / Playwright), grounding (Recall +
memory_facade), no-fabrication gate (verbatim-integrity + fact-verifier + prose_classifier),
depth composition (`/ctm-deepen`), deterministic refresh (`/ctm-refresh` + `/schedule`).
Worked exemplar: Jen Santulan first-time-homebuyer audience (live smoke test).
