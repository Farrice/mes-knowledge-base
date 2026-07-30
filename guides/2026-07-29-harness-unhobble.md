---
date: 2026-07-29
session: harness-unhobble
tier: operator-guide
status: enriched
---

# Antigravity Harness — Amnesty + Apex Unhobble v1 — What We Built 2026-07-29 and How to Use It

> The biggest single-day rebuild since the system existed: the Rule Amnesty stripped ~70% of per-message machinery and resolved 16 rule contradictions; Harness Apex closed the two organs that were missing (metabolism — telemetry that gets READ; focus — work that gets FINISHED); the constitutions became generated artifacts; Farrice got a driver's card, a morning notification, and a fresh-pen run packet for the profile copy after 4 renditions hit the brake. Companions: `OPERATOR-ROUTINE.md` (the driver's card) · `.agent/missions/profile-copy-fresh-0730/portable.md` (the queued mission) · `_active/linkedin-launch/04-deliverables/lane-briefs-2026-07-29.md` (the three-lane business map) · memories `project_rule-amnesty-2026-07-29` + `project_harness-apex-2026-07-29`.

## ⚡ If you only read 10 lines

- Start any day: `/cos` (2 min). Work: talk raw, or `/go "<rant>"` for anything you'll judge. Close: `/end-session`.
- **`route?`** — one word, any time: the session must name what's loaded or stop producing. Your kill switch for un-routed drafting.
- **`/park <name> "reason"`** — set anything aside, resumable forever; parking is a good outcome now.
- **"fresh pen"** — taste-bearing copy from a heavy session tastes like cardboard; say this and the mission moves to a clean session via a run packet. Tonight's lesson, made vocabulary.
- Sessions open with OPEN MISSIONS count (finisher nudge at 3+); campaign work outranks system work at /go compile. Neither ever blocks.
- Your felt verdicts are now READ by a machine: `python3 execution/voice_evaluator.py check <file>` (live bar re-reads calibration-log every run).
- Constitutions are GENERATED: edit `directives/constitution/shared-blocks.md`, run `python3 execution/constitution_compiler.py sync` — never edit CLAUDE.md/AGENTS.md shared sections directly.
- Weekly closeout is now CORE ~10 min (Sunday) / DEEP monthly. It actually completes now.
- 7:15am macOS notification delivers the day's ONE next action (launchd `com.antigravity.cos-notify`).
- NEXT ACTION: fresh session → `/go run the packet at .agent/missions/profile-copy-fresh-0730/portable.md`

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/go "<rant>"` | routed, expert-loaded mission card before any work | any deliverable with your name or money on it |
| `route?` | the loaded-asset list, or a full stop | copy smells like raw AI floor |
| `/park <slug> "<why>"` | stopped line + resumable handoff + parked card | anything you're not finishing now |
| `/resume` | pinned triage board (parked first) | session start on existing work |
| `python3 execution/pulse_dashboard.py --open` | open-mission list w/ ages | "what's actually open?" |
| `python3 execution/voice_evaluator.py check <f>` / `bar` | tell-class hits + your live FAIL bar | before/after any voice-bearing draft |
| `python3 execution/constitution_compiler.py sync` | both constitutions re-rendered | after editing shared-blocks.md |
| `python3 execution/brief_branch_harvester.py --prune` | strands landed + branches cleaned | divergence alarm mentions brief/* |
| `/weekly-closeout` | 10-min CORE drain (money Qs, queue, calibration) | Sundays |

## The mental model (4 ideas)

1. **The product is a multiplication**: Claude's intelligence × your arsenal × your loaded context. Skip any factor and you get the raw floor — which reads like everyone else's AI. `route?` exists to police the middle factor.
2. **Rules are evidence, not verdicts** (Partner Posture, in both constitutions). Only the cost gate and factual veto block work; two tree interlocks protect the repo. Everything else nudges.
3. **Loops must end in a human or a dollar, or they're decoration.** The apex audit found the system had closed every loop that needed neither. Now: felt verdicts feed an evaluator, revenue check-ins are real (4, not 190), missions get finished or parked (40 open → 1).
4. **A session is a pen.** Heavy system sessions write bad copy — 4 renditions proved it; the 9/10 About came from a clean session running the five-move recipe. Fresh-pen packets move taste work to clean contexts on demand.

## Per-capability sections

### The finisher mechanics (/park, open-mission alarm, revenue-first)
**What:** `pulse_dashboard.py --open --alarm` at SessionStart (silent under 3 open, nothing >7d); `/park` writes a stopped line + blocked handoff + parked card the AFK runner can resume; `/go` Stage 0 consults the campaign beacon and asks one confirm line when system work jumps the money queue. **When:** always-on. **When NOT:** never blocks — "open it anyway" always works. **Worked example:** the 40-mission backlog triaged to 1 in one batch decision. **Honest edge:** the finisher nudge fires from mission-log data; work done outside /go (raw sessions that never compile) stays invisible to it.

### The felt-verdict loop (voice_evaluator)
**What:** two layers — deterministic tell-classes with scar citations (room-abstraction, grand-noun labeling, em-dash, setup phrases…) + a LIVE BAR parsing calibration-log.md at run time, so every `/voice-ratchet` verdict strengthens the check instantly, zero re-minting. **When:** any draft in Farrice's voice; the pen reads `bar` BEFORE writing. **When NOT:** expert-embodiment content (extractions keep the expert's voice — purity guard). **Worked example:** rejected v3 lights up on grand-noun hits; locked Take A passes clean. **Honest edge:** layer 1 catches the letter, never the spirit — reader-turn presence and what-do-they-get remain judgment checks it can only remind about.

### Constitution generation
**What:** `directives/constitution/shared-blocks.md` renders golden rule / compass / Partner Posture into both CLAUDE.md and AGENTS.md via marker-injection; `check` mode wired into the parity verifier — drift now fails the fleet same-day. **When:** any edit to shared doctrine. **When NOT:** per-harness sections outside markers stay hand-edited on purpose. **Honest edge:** only 3 blocks are generated so far; other shared-ish sections (Chain steps) can still drift.

### Fresh-pen run packets
**What:** a curated portable mission (`.agent/missions/<slug>/portable.md`) carrying verdict walls, route orders, proof inventory, and ship steps — pasted into a clean session via `/go run the packet at <path>`. **When:** rendition ≥2 rejected, or session context is heavy and the artifact is taste-bearing. **When NOT:** mechanical work — bloat doesn't hurt it. **Worked example:** `profile-copy-fresh-0730` (queued). **Honest edge:** packet quality is everything; a thin packet reproduces the failure in a cleaner room.

### Metabolism repairs (background, no action needed)
Brief harvester lands cloud-routine branches daily (1,827 lines recovered, 13 branches pruned); ground-truth gate derives from calibrated evals (2→32 skills; 3 queue rows now evolution-eligible); revenue registration excludes extractions (outcome = usage); outcome-chase unstuck; dead stores got readers or archives; observe-log reader restored after the orphan-sweep sequencing bug (solution card: verdict lists are perishable).

## Composition
| Stack | When it earns its cost |
|---|---|
| fresh-pen packet + `/go` | any rejected-twice taste artifact |
| voice_evaluator + writers-room Layer 3 | outbound copy in his voice |
| `/park` + AFK runner (`.agent/mission-queue/parked/`) | big missions paused mid-flight |
| lane-briefs + campaign beacon | choosing what opens after mission 2b |

## Honest edges, session-wide
4 copy renditions were rejected before the process corrected — the arsenal-routing reflex is now vocabulary (`route?`) but not yet mechanical; his wave verdicts (amnesty/W0–W3) and 4 real outcome check-ins are still uncollected; W4 (arsenal usage truth) is parked; Equinox tier + employment dates remain his fill-ins.
