---
name: "Hilary Gridley — Judgment Encoding & Anti-Slop Management OS"
description: "Stop the slop upstream: turn tacit expert judgment into narrow deployable evaluator tools (edit pairs → patterns → plain-English rubric → system prompt), articulate what-good-looks-like at every altitude, redesign workflows AI-native (nothing-is-a-surprise, one-step-further), and build the Taste Profile — the canonical context asset that raises the floor of all AI and human work. From the ex-Whoop team lead behind 'How to Be a Super Manager with AI.'"
version: "1.0"
workflows: 13
source: "Marketing Against the Grain deep-dive (8,716 words + slide capture, 2026-07-28 forge)"
---

# Hilary Gridley — Judgment Encoding & Anti-Slop Management OS

Everyone else detects slop after it's produced. Gridley prevents it upstream: slop is an unarticulated quality bar, and the cure is a manager's tacit standard made explicit, encoded into narrow tools, and installed as operating culture. Crown jewel: the complete pipeline for turning taste into tooling — **edit pairs → pattern mining → criteria → plain-English pass/fail rubric → deployable evaluator**. "Anyone has access to your brain."

Load `genius.md` before any workflow. Deep extraction: `extractions/hilary-gridley/extraction.md`. Slide capture: `extractions/hilary-gridley/visual-context.md`.

## Available Workflows

### Tier 1 — Foundation

| Workflow | Produces | Use When |
|---|---|---|
| [hg-judgment-encode](workflows/hg-judgment-encode.md) | A deployable evaluator tool minted from real edit pairs (pattern table + criteria + plain-English rubric + system prompt + validation) | An expert's edits exist and their judgment should scale beyond them — the flagship |
| [hg-quality-bar](workflows/hg-quality-bar.md) | Quality Bar doc + accountability contract at all three altitudes (time / portfolio / artifact) | A team/role/operator is producing slop and nobody has ever stated what good looks like |
| [hg-ai-native-redesign](workflows/hg-ai-native-redesign.md) | Two-panel spec: today's friction-mapped workflow vs the proactive AI-native rebuild, time-badged, with build order | Any recurring reactive situation deserves the months-to-minutes treatment |
| [hg-slop-diagnostic](workflows/hg-slop-diagnostic.md) | Root diagnosis (three roots + flywheel direction + leaking layer) + ordered intervention prescription | Slop is visible but the cause isn't — run before prescribing any tool |

### Tier 2 — Practitioner

| Workflow | Produces | Use When |
|---|---|---|
| [hg-evaluator-fleet](workflows/hg-evaluator-fleet.md) | Scored tool inventory + wave-1 tool cards (max 3), each artifact × audience × outcome | Planning which evaluators to build, in what order — the anti-second-brain gate |
| [hg-edit-pair-harvest](workflows/hg-edit-pair-harvest.md) | Structured Column A/B corpus with provenance grade (or a collection brief) | Encoding is wanted but the evidence base isn't assembled yet |
| [hg-feedback-script](workflows/hg-feedback-script.md) | Speakable graduated-feedback script + escalation move | Slop just landed on your desk and the response must build iteration, not defensiveness |
| [hg-kick-the-crutch](workflows/hg-kick-the-crutch.md) | Crutch/assistant/coach verdict + redesign spec + flywheel check | Any existing AI tool might be making its users worse |
| [hg-exec-editor](workflows/hg-exec-editor.md) | The get-to-yes editor for high-stakes messages (rubric + system prompt + validation) | Upward/outward comms carry asymmetric downside — her canonical tool, instantiated |

### Taste Profile Cluster (the moat asset)

| Workflow | Produces | Use When |
|---|---|---|
| [hg-taste-profile](workflows/hg-taste-profile.md) | The canonical three-layer Taste Profile (emotional customer understanding + brand narrative canon + quality bar), provenance-grounded | A brand/operator needs the one context asset that upgrades all AI and human output — spec: `references/taste-profile-spec.md` |
| [hg-taste-profile-offer](workflows/hg-taste-profile-offer.md) | Productized engagement package: positioning, deliverable stack, proof arc, 10-day delivery, send artifacts | Selling the Taste Profile build as a client engagement (send-before-build binds) |

### Tier 3 — Stacking

| Workflow | Produces | Use When |
|---|---|---|
| [hg-verdict-to-evaluator](workflows/hg-verdict-to-evaluator.md) | Harness-native evaluators mined from Farrice's own verdict/edit logs + "new since last codification" pattern report | The sitting Column A/B data in this system should become fireable quality gates |
| [hg-surprise-audit](workflows/hg-surprise-audit.md) | Surprise inventory + proactive signal design table + wire-this-week build notes | Any operation still runs on humans noticing things |

## Stacking Guide

| Pair with | For |
|---|---|
| `voice-os` / voice-ratchet / felt-verdict-capture | `hg-verdict-to-evaluator` consumes their logs; minted evaluators cite VOICE-CARD as canon |
| `context-profile-architect` | Taste Profile (content layer) → 01-architect (machine-native JSON twin); 02-excavate feeds Layer 1 depth |
| `avatar-machine` / `icp-deep-canvasser` | Phase-0 GROUND discipline for Taste Profile Layer 1; the profile is the anti-ICP complement, not a replacement |
| `geoff-woods-ai-thought-partner` | Bar-setting ritual and taste interviews run as co-creation (`/gw-*`) |
| `wargame-os` | Two halves of judgment transfer: failure-maps for executors + rubrics for evaluators |
| `nate-b-jones` (harness design) | `hg-surprise-audit` + `hg-ai-native-redesign` feed harness audits; sniff-check ↔ evaluator criteria |
| `oren-anti-slop-classifier` / `anti-slop-audit` / prose_classifier | Output-side detectors as the LAST line; this skill builds the upstream bar they backstop |
| `godin-remarkability-engine` | The remarkability premium (slop world rewards OMG work) as offer/positioning fuel |
| `/offer-redteam` + offer_gate | Mandatory pre-launch pass for `hg-taste-profile-offer` |

## Quick Reference

- **Genius Context**: [genius.md](genius.md) — load first, always
- **References**: [taste-profile-spec.md](references/taste-profile-spec.md) · [loop-frameworks.md](references/loop-frameworks.md) (Bodnar/Flanagan material, attributed) · [source-quotes.md](references/source-quotes.md)
- **Default entries**: slop somewhere → `hg-slop-diagnostic`. Scale someone's judgment → `hg-judgment-encode`. One asset to raise a brand's floor → `hg-taste-profile`.
- **The three-question spine of the whole system**: What does good look like? Where's the evidence of your taste? What if the AI went one step further?

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

10 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Hilary Gridley — AI-Native Two-Panel Redesign** — `skills/hilary-gridley/references/prompts-v2/ai-native-redesign.md`
- **Hilary Gridley — Edit-Pair Corpus Assembly** — `skills/hilary-gridley/references/prompts-v2/edit-pair-harvest.md`
- **Hilary Gridley — Evaluator Fleet Plan** — `skills/hilary-gridley/references/prompts-v2/evaluator-fleet.md`
- **Hilary Gridley — Executive Editor (Get-to-Yes)** — `skills/hilary-gridley/references/prompts-v2/exec-editor.md`
- **Hilary Gridley — Graduated Feedback Script** — `skills/hilary-gridley/references/prompts-v2/feedback-script.md`
- **Hilary Gridley — Evaluator Tool from Edit Pairs** — `skills/hilary-gridley/references/prompts-v2/judgment-encode.md`
- **Hilary Gridley — Quality Bar & Accountability Contract** — `skills/hilary-gridley/references/prompts-v2/quality-bar.md`
- **Hilary Gridley — Slop Root Diagnosis** — `skills/hilary-gridley/references/prompts-v2/slop-diagnostic.md`
- **Hilary Gridley — Taste Profile Productized Offer Package** — `skills/hilary-gridley/references/prompts-v2/taste-profile-offer.md`
- **Hilary Gridley — Taste Profile (Three-Layer Context Asset)** — `skills/hilary-gridley/references/prompts-v2/taste-profile.md`

<!-- END:execution-prompts -->
