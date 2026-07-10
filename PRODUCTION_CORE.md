# Production Core — The ~25 Things That Do The Work

> Machine contract: `.agent/production-core.json` (router boost, auditor protection).
> Rule: **routing defaults to core; long-tail requires explicit `/name` invocation or a decisively stronger match.**
> Evidence basis: post-bugfix skill audit 2026-06-09 (forge self-certification excluded) + finalize logs + client deliverables.
> Provisional roster — the monthly CORE DRIFT report in `skill_auditor.py audit` is the correction mechanism.

## The Money Path (client/brand production)

| Entry | Use for | Evidence |
|---|---|---|
| `/copy-engine` | Cold-start converting copy (VSL/ad/email/landing) | binding `cold_start_converting_copy` |
| `/ghostwrite` + Lara Acosta (mastery, growth) | LinkedIn from scratch | A-tier, 4 log mentions |
| `/parallax` | Parallax Substack editions | binding `parallax_editions` |
| `/writers-room` | Refining an EXISTING draft (never production-from-scratch) | binding `writers_room_refinement` |
| `voice-os` (`/voice-os`, card at `_active/farrice-brand/voice/VOICE-CARD.md`) | Always-on voice layer for anything in Farrice's own voice — dial MIRROR/BLEND/STRETCH/OFF + calibration loop | binding `farrice_voice_alignment`, built 2026-07-07 |
| Luke Iha suite (avatar-machine, copy-blocks, vicious-hooks, vsl-leads) | Buyer intelligence → copy blocks | 16 log mentions, A-tier traces |
| Stefan Georgi (dopamine-copy) · Jason Fladlien (marketing) | DR copy emotion/offer architecture | 95% of copy-usage logs |
| `jen-santulan-listing-content` | Jen client work (cd `_active/jen-listings/`) | active client |
| `brand-operating-system` (`/build-bos`) | 6-layer brand builds | Resonance BOS shipped |
| `/strength-conditioning` (+ galpin/israetel/teo/aragon lanes) | ALL fitness/S&C coaching work (active coaching business) | claude.ai export harvest 2026-07-01; conductor + 4 lanes |
| `/extract-mastery` (MES 3.0) | Expertise extraction methodology layer (feeds /extract-forge) | Farrice's own IP, flagship of 8-variant family |

## Thinking, Strategy & Content Psychology

| Entry | Use for |
|---|---|
| `/convene` (presets: /council /roundtable /strike /campaign /deploy) | Multi-expert deliberation |
| `/deep-research` → `execution/research.py` | All generic research (Receipt-carrying) |
| Diandra Escobar · Kallaway | LinkedIn algorithm / content psychology |
| Nicolas Cole (newsletter-flywheel, digital-products) | Newsletter engine, productization |
| Dai Media · Donald Miller (StoryBrand) · Rory Sutherland | Consumer posture / messaging clarity / behavioral lens |
| Nate B. Jones (context-engineering, auto-improvement-loops) | AI orchestration design |
| David Placek | Naming (highest single-use score: 9.3) |

## Visual & Design

| Entry | Use for |
|---|---|
| `creative-direction` | Art direction, mood boards, storyboards |
| `design-md` | DESIGN.md specs, brand tokens, UI codegen |

## Orchestration & System

| Entry | Use for |
|---|---|
| `/supercomputer` | Multi-deliverable missions (anchor memory + cost gate) |
| `/autopilot` | Gate-suppressed end-to-end runs |
| `/weekly-pulse` · `/weekly-closeout` | Weekly planning · outer-loop closure |
| `chain_runner.py finalize` | Quality gate (enforced by Stop-hook ledger) |
| `knowledge_compiler.py` | Wiki ingest/query/lint |
| `extract-forge` | New expert extraction — ungated (forge_gate.py = usage telemetry only) |

## Everything Else

The other ~220 skills and ~990 workflows are **long-tail option value** — real, kept, searchable via `/recommend` or `find_skill.py`, but they do not compete with core in default routing. If a long-tail skill earns 3+ production traces, promote it here (and into `production-core.json`).
