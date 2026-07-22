---
date: 2026-07-21
session: paolo-lead-magnet-engine
tier: operator-guide
status: enriched
---

# Paolo Trivellato LinkedIn Lead Magnet Engine — What We Built 2026-07-21 and How to Use It

> A full /extract-forge of Paolo Trivellato (Starborn AI, starbornai.com) from two frame-watched videos: the Kyle Hunt "$0→$89k/mo boring offer" whiteboard breakdown and his Lara Acosta interview. Shipped: `skills/paolo-trivellato-lead-magnet-engine/` (11 workflows, 9 born-v2 prompts), agent `agents/paolo-trivellato/AGENT.md`, front door `/paolo-trivellato`. Companions: `extractions/paolo-trivellato/extraction-report.md` (MES 3.0), `references/source-quotes.md` (verbatim on-screen templates), `docs/solutions/2026-07-21-x-corpus-via-playwright-public-snapshot.md`.

## ⚡ If you only read 10 lines

- This skill owns the LinkedIn **conversion backend** — everything AFTER the post: DM scripts, opt-in, email, ascension. Content craft still routes to Acosta et al.
- Front door: `/paolo-trivellato` · flagship: `/pt-lead-engine` (full engine + 30-day plan).
- Hook law: authority line ≤8 words, full stop, first — "I am an eight-figure agency COO."
- One resource = ONE pain, in the ICP's first-person words, copy-paste usable in 24h.
- Keyword comment gate, never a link in a fresh post; link only after taper.
- DM carries the **opt-in page**, never the resource; refusal → send it anyway.
- Close = assume the yes with a concrete slot; 3–5 messages max.
- Daily posts **including Sundays**; 20/40/30/10 mix by awareness stage, never topic pillars.
- Ascension: ~$100 workshop with a One-Narrow-Promise ("...so you never feel blind about your agency performance again"); most upgrades land in the follow-up emails.
- ALL Paolo/Kyle numbers are self-reported — quarantined; never cite as verified. A-tier awaits a Farrice blind pass (corpus is ready).

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/pt-lead-engine` | Full engine doc + 30-day plan | New offer/client needs the whole system |
| `/pt-lead-magnet-post` | Comment-gated giveaway post | Any single magnet post |
| `/pt-lead-magnet-resource` | The blueprint/prompt/guide behind the gate | Resource build or upgrade |
| `/pt-comment-capture` | DM scripts + opt-in spec + ops runbook | Comments must become emails + calls |
| `/pt-content-rotation` | Awareness-stage weekly calendar | Daily-post layer planning |
| `/pt-profile-funnel` | 4-element profile rewrite | Profile burns the traffic posts drive |
| `/pt-email-engine` | Welcome E1–E5 + weekly rhythm + follow-ups | Capture flow going live |
| `/pt-workshop-ascension` | $100-workshop → consulting design | Warm list ready to monetize |
| `/pt-boring-offer-audit` | LENS gap audit w/ quoted evidence | Existing presence underperforming; prospect diagnostic |
| `/pt-trend-jack` | Trend-jacked magnet (prompt-from-SOP recipe) | Live LLM/tool wave intersects the service |
| `/pt-x-acosta-reach` | Two takes: conversion spine × Acosta craft | Magnet needs viral-format reach pass |

## The mental model

1. **The offer doesn't change; the system does.** A boring B2B offer can't use flashy hooks — so credibility comes from a rare authority line + ICP-verbatim pain, and revenue comes from the funnel steps after the post. "Take someone from *I like your posts* to *I paid you and I trust you with my business*."
2. **Comment gates are network physics, not engagement bait.** Each comment exposes the post to that commenter's connections (spider-web); commenters must connect to receive the DM; connections auto-follow. Links throttle the climb — gate with a keyword, add the link after taper.
3. **Rented → owned.** LinkedIn is rented reach; email is owned delivery. The DM's only job is moving the commenter onto the list (opt-in interposition) — then eleven emails over two weeks make the sale before the pitch lands.
4. **Trust is bought in $100 increments.** The workshop filters non-buyers, pre-pays trust, and demonstrates the methodology live; the consulting upgrade is a diagnosis conversation in the follow-up window, not a pitch.

## Capability: the forge itself (what shipped)

- **What it is**: MES 3.0 Deep extraction — 14 genius patterns, 9 hidden-knowledge items, 5 verbatim exemplars (post skeleton, DM scripts, One-Narrow-Promise wording, welcome subjects, the Starborn playbook post), quality rubric, recognition test, source-anchored anti-patterns.
- **How it was sourced**: both videos watched with `/watch` (100 + 87 frames read) — the on-screen whiteboard carried the verbatim templates the transcript alone would have paraphrased into genericness (the 2026-07-07 transcript-only failure, directly mitigated).
- **Verification state**: renaissance audit 0 fail · `skill_auditor` heartbeat 6/6 · blind pass EVAL-050 **PASS model-judged** vs two real published pieces (his long-form X post + starbornai.com copy) · finalize composite 8.33 · commit `149d26736` on main.
- **Honest edges**: (a) A-tier requires a **Farrice-judged** blind pass — 5 minutes: read `extractions/paolo-trivellato-lead-magnet-engine/blind-pass-generated-01.md` beside the corpus, then `python3 execution/blind_pass.py record --expert paolo-trivellato-lead-magnet-engine --verdict PASS|FAIL --notes "..."`. (b) Source is two videos from one creator — the DM-conversion and workshop layers rest on his self-reported client results; the site corroborates Kyle exists but lists "$36K MRR added," not $89k/mo. (c) Site bio says "the last decade"; interview says he's 18 — quarantine everything biographical.

## Capability: running the engine (when/when not)

- **When**: any boring/unsexy B2B service (ops, finance, systems, accounting) selling to agencies/SaaS/e-com/consultants on LinkedIn; qualified-inbound-starved operators with real expertise; Proof-to-Market's LinkedIn launch (direct fit — B2B service, no income claims possible, wellness-brand ICP).
- **When NOT**: B2C/e-commerce plays (his own site excludes them); operators who won't post daily (the plan scales down but say the tradeoff); niches where 2–3 magnets/week reads spammy → 1–2/month per his own guidance; DM-averse operators → Lara's email-first variant is built into the workflows as legitimate dissent.
- **Cheaper alternatives**: single post → `/pt-lead-magnet-post` alone; content-only need → Acosta/Diandra skills; strategy-level view → `daniel-priestley-sll-engine`.

## Worked example (from the live session)

Blind-pass test artifact: a fractional-CFO-for-agencies magnet post generated via the lead-magnet-post prompt — authority line ("I've been the CFO inside 40 agencies."), present-tense pain descent, 4 spec'd deliverables, honest 48h takedown, "Comment CASH" gate. Judged against his real X post (which states the same mechanics natively: hook formula "[outcome] + [timeframe] + [mechanism]", FOMO goal, 500–1,000 comments per magnet). File: `extractions/paolo-trivellato-lead-magnet-engine/blind-pass-generated-01.md`.

## Composition (options, never pipeline steps)

| Stack | When it earns its cost |
|---|---|
| `/pt-x-acosta-reach` (Acosta craft pass) | Magnet spine is right but reach formats are stale |
| `/jh-offer-stack` upstream | Workshop promise needs narrative-traced composition |
| `matthew-lakajev` DM swap | Enterprise/spam-sensitive ICP where assume-the-yes is too hot |
| `/pt-trend-jack` + kallaway/lulu taste gate | Live LLM/tool wave; prompt library = raw giveaway material |
| VOICE-CARD layer | ALWAYS when shipped under Farrice's name (binding) |

## Session snapshot

- **Completed**: forge end-to-end (watch ×2 → MES → vision → build → prompts → registration → verification → finalize → commit/push `149d26736`); solution card for X-corpus-via-Playwright; memory entry.
- **Decisions**: 11 workflows at forge lower band (fidelity-honest); claims quarantine binding; corpus from X status page + own site.
- **Remaining**: Proof-to-Market `/pt-lead-engine` build (pinned, thread `paolo-lead-magnet-engine`); Farrice blind pass for A-tier.
- **Where things live**: skill `skills/paolo-trivellato-lead-magnet-engine/` · extraction `extractions/paolo-trivellato/` · corpus `extractions/paolo-trivellato-lead-magnet-engine/reference-corpus/` · handoff `.agent/handoffs/2026-07-21-paolo-lead-magnet-engine.md`.
