---
date: 2026-07-28
session: about-rebuild-ship
tier: operator-guide
status: enriched
---

# Co-Creation Layer + Pen Protocol — What We Built 2026-07-28 and How to Use It

> One session, two layers: the **content layer** (About rebuilt reader-first into three classifier-CLEAN takes awaiting your gut-pick) and the **harness layer** (the machinery that makes your feedback loop physical — spiral brake, feedback-turn protocol, work-mode front door, plus the writers-room Pen Protocol). Companions: `docs/solutions/2026-07-28-co-creation-enforcement-layer.md`, `docs/solutions/2026-07-28-writers-room-pen-protocol.md`, `.agent/handoffs/2026-07-28-about-rebuild-ship.md` (the ship checklist).

## ⚡ If you only read 10 lines

- Raw dumps now route themselves: every substantive prompt gets a `MODE:` line (BUILD-NEW / REFINE-EXISTING / IDEATE / DECIDE / CAPTURE) + its operating card. Override with two words: `mode ideate`.
- Give feedback naturally — the hook forces: verdicts restated → ONE question on ambiguity → ratchet → ONE take. No more educated guesses.
- 2 rejected takes or 3 renditions of one artifact = 🛑 SPIRAL BRAKE. Variants stop; the options become fresh-crack / gut-check / pick. By design.
- Doctrine line: **a doctrine without a counter is a vibe** — rules fire only when their state is measured, injected, and miss-observed.
- Writers-room now runs the **Pen Protocol**: one lead voice writes with full latitude; the room critiques pass/fail, never layer-edits.
- PASS bank (VOICE-CARD §6) is a **floor, never a freeze list** — old passes aren't immune to today's diagnosis.
- Kill switch if the layer annoys: `touch .agent/co-creation.off` (or `CO_CREATION_OFF=1`). Nothing ever blocks you.
- First thing to run next session: `/resume about-rebuild-ship` → `/voice-compile` (12 verdicts pending) → pick a take.
- Three About takes live at `_active/linkedin-launch/03-launch/2026-07-28-about-rebuild-three-takes.md` — pick, don't regenerate.
- Teardowns #1-3 still UNSENT. Send-before-build is the open verb blocking inbound.

## Command table

| Invocation | Produces | Reach for it when |
|---|---|---|
| *(automatic — every prompt)* co-creation layer in `steering_loop_hook.py` | MODE line + operating card + spiral brake when state warrants | Always on; nothing to invoke |
| `mode <BUILD-NEW\|REFINE-EXISTING\|IDEATE\|DECIDE\|CAPTURE>` in any prompt | Forces that mode's operating card | The auto-classified mode is wrong |
| `touch .agent/co-creation.off` | Layer fully silent | It misfires or you want a raw session |
| `python3 execution/hooks/steering_loop_hook.py status` | One-line hook health (enabled, sessions, misses) | Wondering if the loop is alive |
| `/writers-room` (Phase 3 = Pen Protocol) | Diagnosis → writer's brief → ONE full-latitude take → room critiques pass/fail | Any existing draft needs real improvement |
| `python3 execution/voice_ratchet.py add --verdict pass\|fail --line "..." --why "..." --source "..."` | Felt verdict banked to calibration log | Any gut reaction to a line, mid-session |
| `/voice-compile` | Folds pending verdicts into VOICE-CARD (12 pending → 1.3) | 5+ pending, and before judging new copy |
| `python3 execution/prose_classifier.py check <file>` | CLEAN/WARNING + AI-tell signals | Before any copy ships anywhere |
| `/resume about-rebuild-ship` | The pinned ship thread with checklist | Next session, first command |

## The mental model

**1. Counters, not reminders.** Step 0, the iteration brake, and the steering reminder were all live through two spiral sessions (2026-07-27 headline ×8, 2026-07-28 About v10→v14) and fired zero times — because nothing measured renditions, rejections, or ask-before-produce. The layer stores that state (`.agent/co-creation-state.json`, renditions derived from the session ledger's `produced_paths`) and injects it where behavior happens. When a standing rule keeps being violated, don't rewrite the rule — find the counter it lacks.

**2. An ensemble edits; an author writes.** A fully-loaded 15-expert room still produced "bland, flat, generic" because every lens applied its move to the same body and nobody held the pen. The Pen Protocol inverts it: diagnostics compress into a one-screen brief, ONE lead voice writes whole, the room re-enters as critics. Matches the standing one-author-per-body memory.

**3. Reader front and center or don't bother.** The About lineage failed as architecture, not sentences: I-spine memoir with the reader visiting. The ruling (now in VOICE-CARD §6 and the handoff): every beat answers "why should the inbound lead care." The three takes are three different architectures honoring that same ruling.

## Capability: Co-Creation Enforcement Layer

**What it is** — Three stateful mechanisms inside the already-wired `execution/hooks/steering_loop_hook.py` (UserPromptSubmit + Stop; zero new settings.json entries). Spiral brake reads rendition counts from the session ledger and rejection counts from critique-shaped prompts; feedback-turn protocol classifies critiques and injects the verify→align→act contract; work-mode front door classifies raw prompts into five modes with operating cards. Stop-mode observer logs `feedback-turn-blind-produce` and `spiral` events to `.agent/sessions/steering-observe.jsonl`, and repeat misses escalate the next injection.

**When to reach for it** — You don't; it reaches for you. The tell that it's working: you dump raw thoughts and the reply opens by naming a mode or restating your verdicts instead of guessing.

**When NOT to** — A deliberately freeform exploration session where classification noise outweighs structure: `touch .agent/co-creation.off` (delete the file to re-enable). Cheaper alternative for one prompt: the `mode X` override.

**How to invoke** — Automatic. Overrides and switches per the command table above.

**Worked example (live)** — First real firing was this session's own `/end-session`: brake correctly read rendition 4 of `about` from the live ledger — and exposed over-firing on slash commands, gated the same hour (slash/`@` prompts now skip the layer). Bench: 8 cases including corrupted-state → silent exit 0, and both Stop-observer branches.

**Honest edges** — Classifier floors are heuristic: critiques under 180 chars won't classify as feedback; CAPTURE detection is conservative and will under-fire; stem normalization can split odd naming schemes (`take_a`/`take_b` count as separate stems). Rejection attribution needs the artifact named in the prompt (or exactly one active multi-rendition stem). The Stop observer is observe-only by design — it logs misses, it does not block turns.

## Capability: Writers-Room Pen Protocol

**What it is** — Binding rewrite of `.agent/workflows/writers-room.md` Phase 3. Order: diagnostics → one-screen WRITER'S BRIEF (top-3 issues, source material first, temperature, cap, must-keeps with verdict dates) → ONE lead voice writes the whole body with full latitude (lenses as absorbed instincts, override allowed) → room critiques pass/fail → findings return to the same pen. Conditional lenses (Dan Wang's "long-form only" gate) are invitations, never format gates. Rides the 2026-07-27 loading protocol: lens cards via Read, genius.md on fire, never grep.

**When to reach for it** — Any content draft ≥500 chars needing real improvement (it's the project default). The tell for pen-choice: what does the draft lack — texture → Wang, theme → Albom, sentence craft → Cole, persuasion → Wiebe; Farrice-voice pieces default to Fresh Voice/GVE embodiment.

**When NOT to** — From-scratch Parallax editions (`/parallax` owns those); < 500-char tweaks (just edit); a piece already at 3+ renditions (the brake will tell you — pick or fresh-crack instead).

**How to invoke** — `/writers-room` with the draft. The Layer-1 compression checkpoint still applies (state the ratio before injecting new material) as the pen's own measurement.

**Worked example** — Takes A/B/C in the three-takes file: same diagnosis and brief, three different pens/architectures (Mirror / Aisle scene / Operator thesis), each written whole, all CLEAN 0/10 at ≤2,600.

**Honest edges** — The room-as-critics pass ran informally this session (pen + classifier, no full per-lens critique round); the 17 other multi-expert rooms in `.agent/sessions/room-audit-2026-07-27.md` still have committee-editing structures — patch on contact, not preemptively.

## Composition (options, not pipeline)

| Stack | When it earns its cost |
|---|---|
| Layer + `/voice-ratchet` → `/voice-compile` | Always during content feedback — the protocol names the ratchet command so verdicts bank themselves |
| Brake + `/jam` | When the brake fires on taste-bearing work, a jam (two takes → gut verdict) is often the cleanest "fresh crack" move |
| Mode `DECIDE` + `/offer-redteam` | Offer/positioning forks — decision-before-artifact plus adversarial pressure |
| Solution-card candidates named in the card | `send-before-build`, memoir ratio, offer specificity — same counter pattern, wire when they next bite |

*Note: the `hg-*` workflow set in this cycle's changed-files list is sibling-session work (Hilary Gridley extraction) — not covered here; it will get its own guide from that session's closeout.*
