# Extraction Vision — Riley Brown (Agentic Marketing Operations)

**Source**: "Codex Is Basically Running My Company Now" (2026-07-21, 36.7 min) + 2 sibling videos (corpus RICH, 13,063 words) + 100 frames visual context
**Mode**: Forge, autonomous checkpoints (Farrice decision 2026-07-24). **EXPANSION**: completes + corrects the unregistered `skills/riley-brown-marketing-automation/` draft committed this morning (b492479ad, Codex-side, built without transcript ground truth).
**Creative latitude**: 3 (Autonomous) · **Depth**: Mastery

## Who this expert actually is

Riley Brown, AI-native founder (Chorus). Not a marketing tactician — an **agentic-operations architect**. His genius is not any single workflow; it's the operating doctrine for running a company's entire marketing function through a coding agent + a portfolio of small composable skills wrapped around commodity APIs.

## Core Thesis (the one truth)

> "AI hasn't gotten any better at writing content. AI is really good at replicating... really good examples. The only thing you need to do in order to create really good content is provide really good examples."

Everything he builds is **example-supply-chain engineering**: scrape the best → structure it (Notion) → convert to callable skills → generate in learned voice → distribute → never leave the agent.

## Uniqueness Audit (vs. 222-expert roster)

- **No roster expert covers agent-native marketing OPS.** We have content geniuses (Kallaway, Lara, Cole), ad experts (Dara, Luke), and system builders (Saraev, Kashef) — but nobody whose domain is "the agent IS the marketing department."
- Signature uniqueness: (1) **creator→skill conversion** as a repeatable move; (2) **longest-running-ad proxy** for winning creative; (3) **"API key → 'create a skill that fully controls X'"** — self-authoring integrations in one minute; (4) **draft-links-never-send** human gate for outbound at scale; (5) skills that call other skills mid-task (scrape-creators feeding buffer-publisher captions).

## Business Leverage Map

- **Direct revenue line**: ad-spy + creative pipeline serves the $2,500 supplement/performance-brand sprint. Creator→skill serves every ghostwriting/client-content lane.
- **Harness leverage**: his 9 workflows map ~80% onto infrastructure we already own (Apify sc-* actors, notion_api.py, Tavily, Gmail/Drive MCP, Fantastic Studio/Dara). Extraction doubles as the blueprint for Phase 3 capability builds.
- **Meta-leverage (highest)**: his self-authoring-integration pattern and self-updating-skill pattern ("update the email draft skill so you never say X again") upgrade how we build ALL future connectors.

## Cross-Expert Stacking Map

- Riley × **Kallaway** (he literally scrapes Kallaway on camera): scraped corpus → our existing kallaway skill validates/deepens voice replication.
- Riley × **Dara Denney**: longest-running-ad intel feeds `/dara-static-engine` production.
- Riley × **Diandra/Lara**: scraped LinkedIn corpora → hook/voice engines.
- Riley × **Meg Heckman / buyer-trigger**: scraped competitor ads → trigger audits.
- Riley × **extraction pipeline itself**: any scraped creator becomes an /extract candidate (scrape → corpus → skill is literally our own loop, industrialized).

## Gap Fill

Adds the **operations tier** the roster lacks: distribution, scheduling, inbox, file hygiene — the unglamorous layer that makes the content tier compound.

## Direction for Architecture (Phase 4)

Keep the existing draft's 3-tier shape (it's sound), but: correct unverified claims against transcript ground truth; workflows must reference OUR infrastructure (apify_client.py sc-* actors, notion_api.py, Tavily, MCP) not raw third-party APIs we don't hold keys for; add prompts-v2; register fully; blind-pass against real Riley scripts.
