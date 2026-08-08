---
date: 2026-08-07
session: expert-practice-os
tier: session-brief
status: enriched
---

# Extraction: Expert Practice OS - Runtime Proof Blocked — What We Built 2026-08-07 and How to Use It

> This session turned Authority.io video `4HqO0h13MX4` into a cold, reusable practice-routing system for coaching and consulting. It preserves Farrice's first public lane (life coaching, solopreneurship, and AI consulting) without forcing that positioning or proof onto a client. Start with the exact handoff in `.agent/handoffs/2026-08-07-expert-practice-os.md`; the skill contract lives in `skills/expert-practice-os/SKILL.md`.

## ⚡ If you only read 10 lines

- The build is preserved on `main`; do not re-extract the video or rebuild the system.
- Expert Practice OS is a thin conductor: it validates the practitioner packet and chooses one lane owner.
- It does not perform coaching, consulting, offer creation, acquisition, delivery, or economics work.
- Closed cold lanes are AI consulting, life coaching/life design, and solopreneurship.
- Farrice's first public configuration is specific to Farrice; fresh client runs cannot borrow it or its proof.
- Behavior proof is green: two positive fixtures, 21 adversarial mutations, and four unit tests pass.
- Current structural proof is red at 29/31 because a later index regeneration broke the cold authority boundary.
- Repair only registration and prompt-catalog state; do not broaden the architecture.
- Detached runtime embodiment is still untested, so registration and revenue modeling remain locked.
- Resume with `/resume expert-practice-os`; after repair, rerun both verifier commands below.

## Command table

| Invocation | What it produces | Reach for it when |
|---|---|---|
| `/resume expert-practice-os` | Loads the exact blocked-state handoff | Starting the repair in a fresh task |
| `python3 skills/expert-practice-os/tests/verify_skill_system.py` | Structural cold-state and wiring verdict | After changing any registry, index, prompt, or skill-system file |
| `python3 skills/expert-practice-os/tests/test_verify_behavior_run.py` | Four unit tests covering both positive fixtures and all adversarial mutations | After structural repair or behavior edits |
| Open `skills/expert-practice-os/SKILL.md` by exact path | Loads the cold conductor contract without public routing | Inspecting or testing the system before promotion |

## Session snapshot

### Completed

- Built the Expert Practice OS conductor, packet schema, proof-state schema, route ownership map, claims boundary, three niche adapters, and cold execution prompt.
- Added the Sunny Lenarduzzi Profitable Offer Prototype companion workflow without blending it into the conductor.
- Created a Final 10% AI-consulting fixture and a life-design-coach fixture, plus adversarial cases that catch proof borrowing, multi-owner routing, premature economics, unregistered niches, and external action.
- Sealed the isolated build in `1009846c1` and merged it to `main` in `fe9bed03a`.

### Locked decisions

- **One conductor, one lane owner.** The conductor classifies and hands off; lane experts do the work later.
- **Universal packet, non-universal offer.** Packet, risk, proof, capacity, stage, and handoff are reusable. Positioning, protocol, promise, delivery, and evidence stay practitioner-specific.
- **Proof states stay separate.** Local behavior, detached runtime, client outcomes, market demand, and revenue are not interchangeable.
- **Economics activates last.** Annual and monthly six-figure models require detached runtime proof, stage-appropriate operating inputs, and explicit approval.

### Current blocker

Commit `4cf6b851d` regenerated indexes after the merge. It placed the cold skill and Sunny companion workflow into authoritative skill/arsenal surfaces and removed their two non-authoritative prompt-catalog entries. The skill's own behavior still passes; integration authority does not. The repair target is therefore narrow: restore the intended cold registration state and prompt discovery, then return the structural verifier to 31/31.

### Honest edges

- No detached read-only runtime proof exists yet.
- No offer has been sold or delivered through this system.
- No six-figure annual or monthly result is claimed or forecast.
- No registration, publishing, outreach, payment setup, or external action is authorized.
- The closeout lane is parked because another live session wrote to `main`; merge it only through the lane tool after the fresh writer clears.

## Where things live

| Need | Path |
|---|---|
| Cold conductor contract | `skills/expert-practice-os/SKILL.md` |
| Architecture and proof boundary | `extractions/video-context/4HqO0h13MX4/skill-system-contract.md` |
| Structural verifier | `skills/expert-practice-os/tests/verify_skill_system.py` |
| Economics activation gates | `skills/expert-practice-os/references/economics-activation-contract.md` |
| Exact resume state | `.agent/handoffs/2026-08-07-expert-practice-os.md` |
