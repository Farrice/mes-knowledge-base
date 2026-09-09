---
name: riley-brown-marketing-automation
description: Riley Brown's (Agent Native / Chorus) agentic marketing-operations doctrine — running a company's entire marketing through a coding agent + a portfolio of small, named, composable skills wrapped around scraper APIs. Examples-over-instructions (retrieve verified exemplars, don't prompt harder), creator→skill voice compilation, longest-running-ad competitor intel, template-steal ad factories, email drafts at scale, constraint-encoded booking links, "turn it into a skill" freezing, and per-task model/cost routing — all terminating in a human-editable draft behind approval. Use for scraping creators/competitors, building marketing skill libraries, ad-spy, on-brand creative from winners, inbox/scheduling ops, and agent-native distribution.
---

# Riley Brown — Agentic Marketing Operations

**The gap this fills**: the roster has content geniuses (Kallaway, Lara, Cole), ad experts (Dara, Luke), and system builders (Saraev, Kashef) — but nobody whose domain is "**the agent IS the marketing department**." Riley owns the operations tier: scraping, distribution, scheduling, inbox, file hygiene — the unglamorous layer that makes the content tier compound. Core truth: **AI can't verify content quality the way it verifies code, so the job is feeding the agent verified examples on demand, judging with real taste, and freezing every capability into a named skill that compounds.**

**Expert**: Riley Brown (@rileybrownai), AI-native founder of Chorus (open agent platform) and Vibecode. Runs his startup's marketing entirely inside Codex + custom skills. **Source: 3 verified Riley Brown videos + a 100-frame visual analysis of the primary demo** (`extractions/riley-brown/`). Extraction: `extractions/riley-brown/mes-extraction.md`.

**Load order**: Tier 1 = this file + the workflow. Tier 2 (+`genius.md`) for any composition, creative, or client-facing work. Verbatim prompts + claims ledger: `references/source-quotes.md`.

## Costs — Our Routes vs. Riley's Stack

Riley demos a **paid third-party stack** (ScrapeCreators, Foreplay, Firecrawl, Buffer, Paper). **We hold none of those keys and don't need them.** Every workflow below routes through infrastructure we already own — mostly **$0**, with a small metered Apify budget for social scraping. Riley's original tools are noted only as *what he uses*, never as a dependency.

| Capability | Riley's tool (paid) | **Our route ($0 unless noted)** |
|---|---|---|
| Scrape a creator | ScrapeCreators | `/scrape-creator` → `social_intel.py` (Apify sc-* actors ~$0.005–0.25/run; yt-dlp captions free) |
| Bank one already-watched public YouTube video | `/watch` evidence packet | `/social-to-notion --watch-packet ...` → same Social Intelligence DB; no second scrape |
| Competitor ad-spy | Foreplay ($59–149/mo) | `/ad-spy` → Meta Ad Library via read-only Playwright, **$0** |
| Winning-ad → creative | Paper.design | `/creative-from-winners` → Dara / Fantastic Studio / Canva / Higgsfield |
| Brand-asset scrape | Firecrawl | `/brand-asset-scrape` → Tavily + Playwright, **$0** |
| Email drafts at scale | Gmail | `/inbox-drafts` → Gmail MCP (drafts only), **$0** |
| Social scheduling | Buffer/Typefully | `/post-scheduler` → Typefully (key pending) |
| Booking links | Cal.com | `/scheduling-links` → Cal.com API (key pending) |
| Data warehouse | Notion | Social Intelligence DB (`3a749875-a897-8104-a867-fc9aeb53f52c`) via `notion_api.py` |

Full mapping: `references/api-integration-guide.md`.

## Workflow Table (12 workflows, 3 tiers)

### Tier 1 — Foundation (the core moves)

| Workflow | Produces | Use when |
|---|---|---|
| `workflows/riley-scrape-to-skill.md` (**front door**) | Creator → named voice-writing skill, deploy-in-voice on a fresh topic | Turning any creator into a callable style |
| `workflows/riley-ad-spy.md` | Longest-running competitor ads, ranked, inference-labeled analysis | Competitive creative intel |
| `workflows/riley-turn-it-into-a-skill.md` | Any successful run frozen as a named, inspectable skill/workflow | A task will recur; a correction should stick |
| `workflows/riley-inbox-drafts.md` | N voice-matched email drafts, never sent | Inbox backlog; decline-and-pitch at scale (his highest-leverage move) |

### Tier 2 — Practitioner (the ops + creative layer)

| Workflow | Produces | Use when |
|---|---|---|
| `workflows/riley-creator-analyzer.md` | Per-post "why it works" verdicts grounded in a hook lens | A scraped corpus needs the surpass-Riley analysis pass |
| `workflows/riley-template-steal-ads.md` | On-brand variant batch off a winning ad's structure | Volume ad testing from a proven skeleton |
| `workflows/riley-brand-scrape.md` | Structured brand-asset sheet (colors/type/logos/voice) | Grounding creative in a real brand |
| `workflows/riley-distribution-ops.md` | Staged social posts + constraint-encoded booking links + file hygiene | The unglamorous distribution/scheduling/booking tier |

### Tier 3 — Stacking (cross-expert pipelines)

| Workflow | Pairs with | Use when |
|---|---|---|
| `workflows/riley-parallax-pipeline.md` | Farrice voice + Satori + Parallax | Research → scrape → essay → design → distribute under Farrice's brand |
| `workflows/riley-lara-amplifier.md` | lara-acosta-*, diandra-escobar-* | Scraped LinkedIn corpus → ghostwritten posts |
| `workflows/riley-dara-adfactory.md` | dara-static-engine (Meg/Luke as copy lens) | Ad-spy intel → original static-ad production |
| `workflows/riley-automations.md` | any workflow above | Promoting a useful one-off to a recurring/scheduled automation ("act in the future") |

## Quick Reference (the spine)

**DIAGNOSE (verification gap) → OWN THE TASTE → SCRAPE VERIFIED EXEMPLARS → TURN IT INTO A SKILL → CHAIN → DRAFT-LINK TERMINUS → DIAL MODEL/COST → CORRECT INTO THE FILE / AUTOMATE**

- Content is subjective and unverifiable — supply *examples*, don't prompt harder.
- Only delegate what you can judge; taste is the load-bearing human input.
- Exclude sponsored/boosted posts *with retained exclusion evidence*.
- Longest-running ad = the winner, but labeled *inference from durability, not ROAS proof.*
- The durable asset is a **named skill**, born from a successful run — read what it wrote.
- Skills chain live; pick MCP / REST / computer-use per tool.
- **Never auto-send.** Every action ends in an editable draft/link behind approval.
- Per-task model + effort dial; open-source for mechanical work.
- Write corrections into the skill file so they compound; promote useful one-offs to automations.

## Stacking Guide (consistent with `extractions/riley-brown/vision.md`)

- **Riley × Kallaway** — he literally scrapes Kallaway on camera. `/scrape-creator` → `/extract` deepens voice replication; `skills/kallaway-*` grounds the "why it works" verdicts.
- **Riley × Dara Denney** — longest-running-ad intel from `/ad-spy` feeds `/dara-static-engine` production (`riley-dara-adfactory`).
- **Riley × Lara / Diandra** — scraped LinkedIn corpora → hook/voice engines (`riley-lara-amplifier`).
- **Riley × Meg Heckman / buyer-trigger** — scraped competitor ads → trigger audits.
- **Riley × the extraction pipeline itself** — any scraped creator becomes an `/extract` candidate (scrape → corpus → skill is our own loop, industrialized; `/scrape-creator` marks Extract Candidate).
- **Farrice deployments** — VOICE-CARD + dial is a mandatory layer on anything shipped under his name (binding `farrice_voice_alignment`).

## Anti-Patterns (reject on sight)

Prompt-engineering a voice from scratch · scraping raw engagement without excluding sponsored · presenting ad duration as ROAS *proof* · auto-sending/auto-posting with no editable-draft terminus · cloning a competitor ad word-for-word or carrying its real byline (the "Dr. Fahim Hussain" failure) · fresh prompt instead of a saved named skill · corrections left in chat · delegating in a domain you can't judge · inventing performance numbers the source doesn't expose · treating a skill as a black box instead of reading the file it wrote.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

9 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Batch Email Drafts — [INTENT]** — `skills/riley-brown-marketing-automation/references/prompts-v2/batch-email-drafts.md`
- **Brand Assets — [BRAND DOMAIN]** — `skills/riley-brown-marketing-automation/references/prompts-v2/brand-asset-sheet.md`
- **Competitor Ad Intel — [COMPETITOR SET]** — `skills/riley-brown-marketing-automation/references/prompts-v2/competitor-ad-intel-report.md`
- **Voice-Skill: [SKILL NAME] — [CREATOR]** — `skills/riley-brown-marketing-automation/references/prompts-v2/creator-voice-skill-deploy.md`
- **Why-It-Works Analysis — [BATCH TAG]** — `skills/riley-brown-marketing-automation/references/prompts-v2/creator-why-it-works-analysis.md`
- **Distribution Staging — [DATE]** — `skills/riley-brown-marketing-automation/references/prompts-v2/distribution-staging-package.md`
- **Durable Asset — [SKILL NAME]** — `skills/riley-brown-marketing-automation/references/prompts-v2/durable-asset-forge.md`
- **Exemplar-Grounded Voice Pipeline — [PIPELINE TARGET]** — `skills/riley-brown-marketing-automation/references/prompts-v2/exemplar-grounded-voice-pipeline.md`
- **On-Brand Ad Variant Batch — Source: [SOURCE AD]** — `skills/riley-brown-marketing-automation/references/prompts-v2/on-brand-ad-variant-batch.md`

<!-- END:execution-prompts -->
