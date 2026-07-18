---
name: voice-os
description: >-
  Always-on voice alignment spine — load before ANY writing task that carries
  Farrice's own name: LinkedIn posts, Substack/Parallax editions, Notes/Threads,
  emails, DMs, replies, memos, comments, docs, drafts, brand copy. Answers "does
  this sound like me" before craft ever runs. Owns a 4-mode fidelity dial
  (MIRROR/BLEND/STRETCH/OFF), the identity + voice-law floor, the banned-moves
  gate, and the felt-verdict calibration loop. Trigger words: voice, tone,
  style, sound like me, in my voice, my voice, does this sound like Farrice,
  voice check, voice pass, calibrate the voice, on-brand, personal voice,
  writing voice, ghostwrite my voice. Do NOT use for: client deliverables where
  Voice OS is explicitly OFF (Jen, Andrea, any client brand — their own voice
  docs govern), or for craft/structure work with no identity stakes (pure
  research synthesis, deterministic scripts).
expert: "Voice OS (spine over VOICE-CARD.md — no craft of its own)"
domain: "Cross-cutting Identity x Voice Fidelity x Calibration"
version: "1.0"
format: "spine"
tier: system
---

# Voice OS

A piece can pass every craft gate — structure sound, hook sharp, no slop — and still not sound like Farrice. Voice OS is the layer that catches that failure before delivery. It owns no craft. It owns identity: who Farrice is, how he actually talks, what he never says, and how far a piece is allowed to drift from his fingerprint before it stops being his. Every writing task that carries his name loads this spine first, then hands craft authority to the expert skill that actually writes.

## What Voice OS Is

Voice OS is the always-on voice alignment layer sitting between intent and craft. It is not a writer, not a persona, not a style guide to quote back at a reader — it is grounding an expert absorbs before drafting. Its one job: keep every piece inside Farrice's identity spine and voice law while craft experts (writers-room, `/parallax`, `/ghostwrite`, How-I-Write OS) do the actual writing.

**Load order** (every session that touches Farrice's own voice):
1. This SKILL.md — orientation, the Dial, the decision table.
2. `_active/farrice-brand/voice/VOICE-CARD.md` — always. The canonical card: §1 Identity Spine, §2 Voice Law, §3 Stylometrics, §4 Channel Registers, §5 Banned Moves, §6 Calibration Bank, §7 The Dial, §8 Loop Protocol.
3. The relevant §4 channel register only — LinkedIn, Substack edition, Notes/Threads, email/DM, or client-facing docs. Don't load registers you're not writing for.
4. `genius.md` (Tier 2, craft/complex work) — the texture layer: signature-move mechanics traced to source, the two-stage rhythm behind the stylometrics, the recognition test, and the sourced anti-pattern bank. Load this whenever the deliverable is more than a mechanical mode-check — i.e. any time craft judgment is needed, not just gate enforcement.

If `VOICE-CARD.md` doesn't exist yet, say so and stop — do not improvise a voice from memory. Run `python3 execution/voice_ratchet.py status` to confirm state before assuming the card is missing; the ratchet script reports "not found" cleanly if it truly isn't compiled.

## The Dial (voice fidelity modes)

Four modes, one hard floor that never lifts. The dial answers "how much of this piece is Farrice's literal fingerprint vs. an elevated/explored version of it."

| Mode | Fidelity | When | What's fixed | What's free |
|------|----------|------|---------------|-------------|
| **MIRROR** | 95% | Personal comms, DMs, replies, anything conversational under his name | Everything — full fingerprint, including imperfect texture (run-ons, real speech rhythm) | Almost nothing — this is closest to raw him |
| **BLEND** *(default)* | ~70% | Default for all content — the "better version of me" | Identity anchors (§1) + Voice Law (§2) + Banned Moves (§5) — HARD | Craft structures, expert frameworks, fresh metaphors/perspectives from other creative lenses — WELCOME |
| **STRETCH** | 40% | Explicit creative exploration — "surprise me," "take liberties," "through [X]'s lens," 3-variant divergence phases | Only the hard floor | Expert/foreign voice may lead; style experiments; drafts through another writer's voice |
| **OFF** | n/a | Client deliverables — Jen, Andrea, any client brand | Nothing from this card — client voice docs govern entirely | Only the universal slop ban + no-fabrication floor still applies |

**HARD FLOOR — never lifts in any mode**: privacy law (family autobiography never public without clearance — the pattern can be dramatized, the specifics cannot), no fabrication about a real person, the AI-slop ban bank (§5 + `directives/ai-slop-detector.md`), the wince test, no cheap question closes.

**Mode selection cues**: "sound like me" / "in my voice" → MIRROR. Default content with no mode named → BLEND. "Surprise me" / "take liberties" / "through [X]'s lens" / a 3-variant divergence ask → STRETCH. Any client deliverable → OFF. **Explicit mode naming always wins** — if Farrice says a mode, use it, full stop.

### Decision table: artifact type → default mode

| Artifact | Default mode |
|----------|---------------|
| DM / text reply / personal email | MIRROR |
| LinkedIn post, Substack edition, Notes/Thread | BLEND |
| Brand manifesto, positioning copy, offer copy (his own) | BLEND |
| Divergent 3-variant exploration, "through X's lens" drafts | STRETCH |
| Jen / Andrea / any client deliverable | OFF |
| Internal strategy doc, memo to self | MIRROR-adjacent (extrapolate from raw register — no polished exemplar exists yet, per §4 corpus-gap note) |

## Balance Philosophy

The card is a floor and a compass, not a ceiling. Expert skills — writers-room, `/parallax`, `/ghostwrite`, How-I-Write OS — keep full craft authority in BLEND and STRETCH; Voice OS never re-teaches hook structure, scene craft, or rhetoric. It constrains identity and bans slop. It never constrains imagination. Per the repo's no-forced-wiring rule, Voice OS composes WITH existing content workflows as a grounding layer they load — it never becomes a pipeline step every workflow must route through, and it never replaces the writer.

## Verification Before Delivery

Two checks, always, before a MIRROR or BLEND draft ships:

1. `python3 execution/prose_classifier.py check <file>` — the existing deterministic slop detector. 5+ signals flags and caps Expert Standard at 6 per the root Quality Gate.
2. **§6 Calibration Bank pattern match** — read the draft's strongest lines against the PASS and FAIL banks in VOICE-CARD.md §6. A line that pattern-matches the FAIL column (forced jargon, tells-instead-of-shows, generic question close) gets rewritten before showing, even if `prose_classifier.py` passed it — the bank catches voice-specific tells the generic classifier doesn't know about.

A draft that fails either check is not ready. Rewrite the flagged lines, re-check, then deliver.

## The Loop

Voice OS improves by feeding on felt verdicts, not periodic rewrites.

1. **Capture.** The instant Farrice reacts to a line — praise or wince — run `/voice-ratchet` (or the underlying `python3 execution/voice_ratchet.py add ...`) to log the verbatim line, verdict, why, and source. Same standing rule as thought-bank capture: this should happen silently, in-session, the moment the reaction happens — never deferred to "I'll remember to log this later."
2. **Accumulate.** `calibration-log.md` is the raw append log; VOICE-CARD.md §6 is the curated, deduplicated distillation. `python3 execution/voice_ratchet.py status` reports pending-since-last-compile and flags RECOMPILE RECOMMENDED at 5+ pending entries.
3. **Recompile.** Run `/voice-compile` when the ratchet reports ≥5 new entries, or quarterly, or when a §3 stylometric claim gets contradicted by 3+ new corpus pieces. Recompile folds new verdicts into §6, checks stylometric deltas, bumps the version, and regenerates `PORTABLE-VOICE-CARD.md`.
4. **Re-export.** After every compile, the portable card should get re-synced to wherever external AIs or tools consume it (Drive, other agents) — the compile workflow flags this as a recommendation, doesn't automate the export.

## Relationship to Existing Assets

- **`/voice-audit` (Sean Mabry voice-mastery skill)** — deep line-by-line QA on ghostwritten content. Point it at `VOICE-CARD.md` as the voice reference instead of building a fresh voice document from scratch when Farrice is the subject; keep using it as-is for third-party/client voice work.
- **`_active/farrice-brand/CLAUDE.md` voice rules** — remain binding. VOICE-CARD.md absorbs and supersedes their content in more granular form (stylometrics, channel registers, calibration bank); the CLAUDE.md rules are the compressed pointer, the card is the depth.
- **`FARRICE-MASTER-CONTEXT.md`** — identity depth behind the card. VOICE-CARD.md §1 Identity Spine is the compiled distillation for writing purposes; the master context doc is the fuller self-work synthesis for identity/positioning/offer work generally.
- **Content-quality pipeline** (`feedback_content-quality-pipeline-recipe.md`) — Voice OS is one input into that pipeline's voice-rules stage, not a replacement for it.

## Workflows

Operator-facing step-by-step entries (When to Use / Input Required / Steps / Output contract /
Quality Gate) for each of the four Loop/Dial procedures below. Each points to its deeper
structure-pure-v2 prompt in `references/prompts-v2/` for the full field-by-field protocol.

- **Pre-Draft Grounding Brief** — `workflows/grounding-brief.md` (maps to `/voice-os mode <name>`)
- **Post-Draft Verification Pass** — `workflows/verification-pass.md` (maps to `/voice-os apply <file>`)
- **Felt Verdict Capture** — `workflows/felt-verdict-capture.md` (maps to `/voice-ratchet`)
- **Voice Card Recompile** — `workflows/card-recompile.md` (maps to `/voice-compile`)

## Front Doors

- `/voice-os [status|mode <name>|apply <file>]` — status check, mode set, or apply a voice pass to an existing draft.
- `/voice-ratchet` — capture one felt verdict.
- `/voice-compile` — recompile the card from accumulated verdicts + sources.
- `/voice-audit` — deep line-by-line QA (Sean Mabry, unchanged, point it at the card).

## Anti-Patterns

- Writing a Farrice-voiced piece without loading VOICE-CARD.md first — this is the exact "expert-domain output without loading the expert" failure the root Chain bans.
- Treating BLEND as a license to homogenize — the identity anchors and banned moves are HARD in BLEND; only craft technique is free.
- Quoting the card back at a reader, or narrating "per my voice guidelines" — the card is grounding to absorb, never a script to cite.
- Deferring calibration capture — a felt verdict not logged in-session is a felt verdict the loop never learns from.
- Running Voice OS against client deliverables — OFF means OFF; the client's own voice doc governs, full stop.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Voice OS — Felt Verdict Capture** — `skills/voice-os/references/prompts-v2/felt-verdict-capture.md`
- **Voice OS — Post-Draft Voice Verification Pass** — `skills/voice-os/references/prompts-v2/post-draft-voice-verification-pass.md`
- **Voice OS — Pre-Draft Voice Grounding Brief** — `skills/voice-os/references/prompts-v2/pre-draft-voice-grounding-brief.md`
- **Voice OS — Voice Card Recompile** — `skills/voice-os/references/prompts-v2/voice-card-recompile.md`

<!-- END:execution-prompts -->
