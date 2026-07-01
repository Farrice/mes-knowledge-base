# Operating the Harvest — User Guide

*Your full claude.ai account (3,711 conversations, 142 Projects) is now inside this harness: searchable memory + 39 new skills + 16 enriched skills. This is how you drive it. (2026-07-01, commit `338bea73`+)*

---

## 1 · The front doors (what to type, when)

| You want… | Type | What happens |
|---|---|---|
| **Any fitness/coaching work** (programs, nutrition, client questions) | `/strength-conditioning` | Conductor diagnoses the need → routes Galpin (physiology/limiters), Israetel (hypertrophy), Teo (technique/minimalist), Aragon (nutrition) → composes integrated programs. **This is Production Core now — it fires by default for fitness work.** |
| A specific fitness lane directly | `/michael-israetel` · `/eugene-teo` · `/alan-aragon` · `/andy-galpin` | That expert's full methodology (each has 3-4 workflows + genius patterns) |
| **Extract expertise from any source** (your MES 3.0 IP) | `/extract-mastery` | 4-Layer Cognitive Archaeology → Crown Jewel prompts → 30-day surpass path. Sits UNDER `/extract-forge` (forge = full pipeline, this = the methodology layer) |
| Turn expertise into a deployable agent | `/knowledge-architecture` | Your KACE + Intelligence Architecture IP: extract → mastery pathway → domain agent |
| Structure chaos into reusable AI context | `/context-profile` | Your ARCHITECT framework: ICP/brand dumps → machine-native JSON profiles |
| Offers, pricing, scaling | `/alex-hormozi` (money models) · `/chris-do` (value-based pricing) · `/ash-maurya` (lean validation) | New Domain-12/4 swim lanes |
| Viral content science | `/brendan-kane` (formats/Hook Points — built from his full book) · `/jenny-hoyos` (shorts) · `/cognitive-engagement` (dopamine loops) | New Domain-2 lanes |
| Funnels & DR | `/russell-brunson` · `/craig-clemens` (education-first) · enriched `/jason-fladlien` (now 30 workflows incl. webinars) | |
| Solopreneur / audience / niche | `/justin-welsh` · `/matthew-lakajev` (LinkedIn→revenue) · `/pat-flynn` · `/david-perell` · `/sunny-lenarduzzi` (YouTube) | |
| **Search your entire chat history** | `python3 execution/memory_store.py search "<topic>"` or `memory_facade.py "<topic>" --sources sovereign` | All 3,624 imported conversations, keyword now, semantic as embeddings finish |
| Read a full original conversation | Open the `md_path` from search results (`.tmp/claude-export/normalized/conversations/`) | Redacted full transcripts, local only |

**Enriched veterans** — these got major new layers; just use them as before: Priestley (+parasocial/24-asset/partnerships), Godin (+strategy discipline), Fladlien (27→30), Kallaway (+bingeability/creator ladder), Cole (+real pricing menus), Iha (+live-review method), Oren John (+2026 hooks), **Alex Cooper** (+AI creative department; the "Copper" typo is fixed and memorized).

## 2 · What we achieved / what we didn't (honest ledger)

**Achieved:** full import (privacy held — raw stays git-ignored, PII redacted, nothing to Notion) · 112 projects → 65 unique → routed vs your 273 existing skills → **zero duplicated capability** (8 skips, MES meta-fabrications excluded by name) · 281-expert census of 2,010 conversations · fitness package + 34 more skills + 16 enrichments · routing wired (Domain 16, 6 swim-lane adds, 2 Production Core entries).

**Not done / by design:**
- **Embeddings ~75% incomplete** — free-tier caps at 1,000/day. Keyword search works NOW; vector recall grows daily. Fix instantly with a paid `GEMINI_API_KEY` (~$0.08 total) then `python3 execution/memory_embed.py backfill`.
- **Distill → semantic rules not yet run** — the generate quota (500/day) was spent on triage; first batch runs on the next quota window: `ANTIGRAVITY_DISTILL_INCLUDE_EXPORT=1 python3 execution/memory_distill.py run --days 3 --max-clusters 15`. Then **you** approve via `python3 execution/memory_review.py list` → `approve <id>` / `reject <id>`. Nothing auto-promotes.
- **Deep veins unmined** — we took each big expert's top ~10-12 conversations. Remaining: Priestley 84, Godin 68, Fladlien 68, Kallaway 39. Rerun anytime: the census (`_active/claude-export/harvest/census-full.json`) has every conversation ID.
- **137 marginal experts** — searchable in memory, deliberately not skill-ified (anti-bloat).
- **Not battle-tested** — structure is verified; heartbeat isn't. First real client program through `/strength-conditioning` is the true gate. Your rule: felt verdict > gate scores.
- **Coach Cooz excluded** (your call — client work).

## 3 · Operating cadence

- **Embeddings + distill: AUTOMATED — nothing to remember.** launchd job `com.antigravity.harvest-memory-daily` (daily 07:40 + on login) embeds up to each day's quota, then runs one capped distill batch when new embeddings land. Coverage completes in ~3-4 days, then it becomes a free no-op. Watch: `tail .memory/backups/harvest-memory-daily.log`. **Instant-finish lever:** enable billing on your Google AI Studio project (aistudio.google.com → Settings → Plan) — removes the 1,000/day cap; the next job run finishes everything for ~$0.09.
- **Weekly (~10 min, the only human job):** `python3 execution/memory_review.py list` → `approve <id>` / `reject <id>` on distilled rules. Nothing auto-promotes without you.
- **When a new skill feels flat:** don't rebuild — `/extract-amplify <skill>` with more of that expert's conversations from the census, or tell me and I'll run an enrich pass.
- **Adding future exports:** drop new batch zips in `.tmp/claude-export/raw/`, then `parser parse → triage heuristic → ingest run` (all idempotent — only new conversations process). Runbook: `docs/claude-export-import.md`.

## 4 · Where everything lives

`execution/claude_export_*.py` (pipeline) · `docs/claude-export-import.md` (pipeline runbook) · `_active/claude-export/reports/` (harvest-roadmap, consolidation-plan — git-ignored, local) · `_active/claude-export/harvest/census-full.json` (281 experts → conversation IDs) · `.tmp/claude-export/normalized/` (full redacted transcripts) · **Downloads zips = irreplaceable backup** (export URLs were single-use — don't delete) · Memory pin: `project_claude-export-harvest` in auto-memory.
