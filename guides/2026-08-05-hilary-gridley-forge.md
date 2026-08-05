---
date: 2026-08-05
session: hilary-gridley-forge
tier: operator-guide
status: enriched
---

# Hilary Gridley — Anti-Slop Judgment Encoding OS — What We Built 2026-08-05 and How to Use It

> A full `/extract-forge` on Hilary Gridley's anti-slop masterclass (Marketing Against the Grain, 8,716-word transcript + a slide captured via `/watch`). Shipped: `skills/hilary-gridley/` — 13 workflows in 3 tiers, 14 genius patterns, 10 born-v2 execution prompts, `agents/hilary-gridley/AGENT.md`, and the Taste Profile cluster (canonical spec + productized offer) that Farrice directed as a first-class deliverable. Companion files: `skills/hilary-gridley/SKILL.md` (manifest) · `genius.md` (load before any workflow) · `references/taste-profile-spec.md` (the moat asset's spec) · `extractions/hilary-gridley/extraction.md` (full MES 3.0) · `extractions/hilary-gridley/visual-context.md` (verbatim slide) · handoff `.agent/handoffs/2026-08-05-hilary-gridley-forge.md`.
>
> Scope note: the closeout spine's auto-filed asset list swept `caleb-*`, `bv-*`, and `oren-*` workflows sitting uncommitted in the tree from other threads. Those are **not** this session's output. This session's assets are the `hilary-gridley` skill, agent, extraction, one solution card, and the `/hg-*` command family.

## ⚡ If you only read 10 lines

1. **The crown jewel is one pipeline**: edit pairs → pattern mining → 5±2 criteria → plain-English pass/fail → deployable evaluator. `/hg-judgment-encode`.
2. **Evidence beats introspection.** Gridley never lists her standards — she assembles Column A (drafts sent to her) / Column B (her revisions) and asks AI for the delta. ≥5 clean pairs or the honest output is a collection brief.
3. **The highest-leverage first run is `/hg-verdict-to-evaluator LinkedIn posts`** — your felt-verdict, voice-ratchet, and taste-calibration logs are already Column A/B data nobody has mined.
4. **Narrow or nothing**: one artifact × one audience × one outcome per tool ("Executive Email Editor — get to yes"). A "second brain" is the refused shape.
5. **The Taste Profile is three layers**: emotional customer understanding (anti-ICP) + brand narrative canon + the quality bar. Spec: `references/taste-profile-spec.md`.
6. **Grounding gate on the profile is absolute** — an invented Taste Profile is itself slop; ungrounded fields get marked, never filled plausibly.
7. **AI-native redesign has a grammar**: two panels, both time-badged, step 1 in past tense ("flagged this three days ago — you already knew"), named data windows, one unrequested second-order insight.
8. **Slop is diagnosed at three roots** — no coordination, no canon, no articulated bar — and the flywheel spins either virtuous or doom-loop. `/hg-slop-diagnostic` before prescribing any tool.
9. **Verified**: `skill_auditor.py check --skill hilary-gridley` → 7/7 PASS · blind pass model-PASS as EVAL-057 vs two verbatim Substack pieces. **A-tier awaits a Farrice-judged pass.**
10. **The expert's name is Gridley, not Gidley** — auto-captions garbled it; caught against her own Substack byline mid-forge and renamed everything before it calcified.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/hilary-gridley` | Front door: persona + full arsenal | You want the expert seated before choosing a tool |
| `/hg-judgment-encode` | Evaluator tool from real edit pairs (patterns + criteria + rubric + system prompt + validation) | An expert's edits exist and their judgment should scale beyond them |
| `/hg-quality-bar` | Quality Bar doc + accountability contract, three altitudes | Slop is landing and nobody ever stated what good looks like |
| `/hg-ai-native-redesign` | Two-panel spec (today vs AI-native, time-badged) + build order | A recurring reactive situation deserves the months-to-minutes treatment |
| `/hg-slop-diagnostic` | Root diagnosis + ordered intervention prescription | Slop is visible but the cause isn't — run before prescribing tools |
| `/hg-evaluator-fleet` | Scored inventory + wave-1 tool cards (max 3) | Deciding which evaluators to build, in what order |
| `/hg-edit-pair-harvest` | Structured Column A/B corpus + provenance grade | Encoding is wanted but the evidence base isn't assembled |
| `/hg-feedback-script` | Speakable graduated-feedback script + escalation move | Slop just landed and the reply must build iteration, not defensiveness |
| `/hg-kick-the-crutch` | Crutch/assistant/coach verdict + redesign spec | An existing AI tool might be making its users worse |
| `/hg-exec-editor` | Get-to-yes editor for high-stakes messages | Upward/outward comms carry asymmetric downside |
| `/hg-taste-profile` | The three-layer Taste Profile, provenance-grounded | A brand needs the one asset that raises the floor of all its AI work |
| `/hg-taste-profile-offer` | Productized engagement package + send artifacts | Selling the profile build (send-before-build binds) |
| `/hg-verdict-to-evaluator` | Harness-native evaluator from Farrice's own logs | Turning this system's accumulated judgment into fireable gates |
| `/hg-surprise-audit` | Surprise inventory + proactive signal design table | An operation still runs on humans noticing things |

## The mental model

**Three ideas make the rest obvious.**

**1. Slop is an unarticulated quality bar, not a tooling failure.** Every existing anti-slop asset in this repo — `prose_classifier.py`, `/anti-slop-audit`, `/oren-anti-slop-classifier`, `/satori-anti-ai-slop` — scores work *after* it exists. Gridley's system sits upstream: the bar is stated, encoded, and deployed before anyone writes. Her line: "If you are not setting that quality bar as a leader, you can't be surprised when that quality starts slipping." The detectors become the last line, not the only one.

**2. Taste is compiled from evidence, not recalled from memory.** Asked what five things she checks in an exec email, she says she couldn't tell you cold. So she doesn't try — she puts drafts in one column, her revisions in the other, and asks what changed. AI's job there is pattern *legibility*, not quality knowledge. This is why generic "make this better" prompts produce generic feedback: no evidence base.

**3. The tool is a byproduct; the clarity is the product.** "Even if you don't make any tools out of this, even if you just have conversations where you say that to people — you're going to be a better manager." Corollary: every tool must pass the kick-the-crutch test — remove it tomorrow and the team should be *better* than before it existed, not helpless.

## Capabilities shipped

### The judgment-encoding pipeline (`/hg-judgment-encode`)

**What it is.** A five-step compiler from tacit taste to a running evaluator: assemble ≥5 verbatim before/after pairs → mine recurring edit patterns with frequency counts → distill to 5±2 criteria named in the expert's own vocabulary → write plain-English passing/failing prose per criterion → compose a system prompt that scores pass/fail with quoted evidence, suggests rewrites for failed spans, and *returns the work to the author*. Validation runs against held-out pairs; misses tighten the criteria once.

**When to reach for it.** Someone's judgment is the bottleneck and their edits exist somewhere retrievable.

**When NOT to.** Fewer than 3 clean pairs — run `/hg-edit-pair-harvest` and take the collection brief instead. Also not for accuracy checking; this mines taste, and factual-only corrections get filtered out of the corpus.

**How to invoke.** `/hg-judgment-encode` (loads `skills/hilary-gridley/workflows/hg-judgment-encode.md` → `references/prompts-v2/judgment-encode.md` for the Output Contract).

**Worked example.** Her Executive Editor: criteria mined were *leads with the message in the first sentence · actionable · tone right · every single word adds clarity rather than ambiguity*. `/hg-exec-editor` instantiates it for any operator, carrying those four as the cold-start floor plus a get-to-yes layer (change framed as impact + mitigation + recommendation, never an open "is it cool if…?" ask).

**Honest edges.** Untested against a real corpus in this repo — the first true run is the handoff's next action. The provenance grade (`strong`/`thin`/`insufficient`) is the honesty mechanism; watch that it doesn't get waved through.

### The Taste Profile cluster (`/hg-taste-profile`, `/hg-taste-profile-offer`)

**What it is.** The concept is Bodnar/Flanagan's from *Loop* (kept attributed in `references/loop-frameworks.md`, never blended into Gridley's body); the depth architecture and quality-bar layer are hers. Three layers: **L1** emotional customer understanding — beliefs, feeling-states with triggers, thresholds ("what pushes them too far") each with a concrete violating example, identity stakes, verbatim language map; **L2** brand narrative canon — product mechanism-story, the single named feeling, origin, enemy and stakes, ranked proof spine; **L3** the quality bar — plain-English pass/fail per artifact class, hall of fame, the brand's personal anti-pattern list, voice threshold dials.

**When to reach for it.** A brand's AI output is off-brand and inconsistent across people and tools, and the fix everyone proposes is another tool.

**When NOT to.** As an ICP refresh — that's `avatar-machine` / `icp-deep-canvasser`, and the profile is explicitly the anti-ICP complement. Also not when L1 evidence doesn't exist: the workflow's first output becomes a grounding plan, by design.

**How to invoke.** `/hg-taste-profile` (spec: `skills/hilary-gridley/references/taste-profile-spec.md`). For the JSON twin when agents consume it programmatically, hand off to `context-profile-architect` workflow 01 — the prose profile stays canonical.

**Honest edges.** The offer package (`/hg-taste-profile-offer`) is an unvalidated shelf asset: no prospect send yet, price anchor deliberately left as Farrice's call, and `/offer-redteam` is mandatory before any public launch. Send-before-build binds — the three send artifacts ship before delivery collateral.

### AI-native redesign + proactivity (`/hg-ai-native-redesign`, `/hg-surprise-audit`)

**What it is.** Her teaching slide, captured verbatim via `/watch` focused passes at 1024px (`extractions/hilary-gridley/visual-context.md`). Two panels with time badges (**~half a day** → **~15 min**), TODAY written with felt-friction language ("piecing together," "squint at the overlap," "wait two days"), and the WITH-AI panel starting in past tense: "Your system flagged this three days ago… **You already knew.**" Then the ladder — three options each with a previewable artifact, evidence from a *named* data window ("your last 90 days"), one unrequested second-order insight, human picks by taste, system cascades downstream.

**When to reach for it.** Change management (the concrete picture is a credibility instrument — vagueness reads as cluelessness), harness build specs, or client sales artifacts.

**When NOT to.** As a general "how should we use AI" answer — it needs one concrete trigger situation. Extract the situation first.

**Honest edges.** `/hg-surprise-audit` on this harness must audit what already exists (hooks, launchd, health reports) before proposing watchers; duplicate monitors are the obvious failure mode.

## Composition (options, never pipeline steps)

| Stacks with | When it earns its cost |
|---|---|
| `voice-os` / voice-ratchet / felt-verdict-capture | You have verdict history and want it compiled — `/hg-verdict-to-evaluator` is the bridge |
| `context-profile-architect` | Agents will consume the Taste Profile programmatically and need the JSON twin |
| `avatar-machine` / `icp-deep-canvasser` | Taste Profile L1 needs real voice-of-customer grounding first |
| `wargame-os` | You want both halves of judgment transfer: failure-maps for executors, rubrics for evaluators |
| output-side anti-slop stack | Always — as the last line behind the upstream bar, not instead of it |
| `/offer-redteam` + offer_gate | Mandatory before the Taste Profile offer goes anywhere public |

## Receipts and known gaps

- **Heartbeat gate**: `python3 execution/skill_auditor.py check --skill hilary-gridley` → 7/7 PASS (two initial fails — unsourced anti-patterns and a missing recognition test — fixed in `genius.md`).
- **Prompt audit**: `renaissance_audit.py` 3,733 files, 0 fail; library built; pointers wired into SKILL.md.
- **Blind pass**: model-judged PASS, EVAL-057, against two verbatim published pieces in `extractions/hilary-gridley/reference-corpus/`. The corpus independently corroborated the extraction ("an evaluator that holds your team's work to your standard… nothing goes out the door below your bar"). **A-tier promotion still requires a Farrice-judged side-by-side** — the sample is at `extractions/hilary-gridley/blind-pass-sample.md`.
- **Factual flag**: the host's "Inside the Box by David Epstein" citation is marked UNCONFIRMED in `loop-frameworks.md` (attribution appears garbled). Use the constraints principle; never cite the book from this source.
- **System bug found**: the generated expert front door cites a skill's first workflow path as its example row, which `arsenal_index` reads as "reachable" — so the wrapper minter silently skips that workflow on every fresh forge, while reporting clean. Card: `docs/solutions/2026-07-28-front-door-masks-first-workflow-from-minter.md`. **Check after any forge**: `ls .agent/workflows/<prefix>-*.md | wc -l` must equal the workflow count. Permanent fix (ignore front-door files in reachability) is proposed, unbuilt.
