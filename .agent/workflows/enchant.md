---
description: "The Enchantment OS — Mark Forsyth's method deployed pure and single-author. compose = raw intent to finished piece; elevate = an existing draft's line, sound and voice-texture layer. Stages two takes (full-ornament vs gate-clean) and banks the felt verdict to the taste ledger."
---

# /enchant — The Enchantment OS

> **Invocation**: `/enchant` · `/enchant compose` · `/enchant elevate` · "run enchant"
> **Owner**: `skills/mark-forsyth-rhetoric` — Mark Forsyth, single author, no other expert loads
> **Posture**: this front door owns no craft of its own. It classifies, sequences, and gates. Every move is
> owned by a workflow inside the skill.

Grammar and glamour are the same word. A *grammar* was something written down; a *glamour* was a spell you
cast on somebody to enchant them and carry them off. This front door exists because Forsyth's answer to
*why write well* is not "to be understood" — it is:

> **"Don't write just to be efficient and get the meaning across. Write to enchant."**

## Why this exists alongside `/how-i-write`

Both compose finished pieces. That is deliberate, and it is a measurement Farrice commissioned on
2026-08-06: `/how-i-write` is an **orchestra** (3–6 experts at named altitudes, one body-voice owner);
`/enchant` is a **single author** running one method end to end. The Phase-7 bake-off runs the same brief
through both and banks the felt verdict.

**Hard rule: never run both on the same passage in the same pass.** That is a double-picked lane, and the
2026-06-22 bake-off already measured what it costs. Full boundaries:
`skills/mark-forsyth-rhetoric/references/lane-contract.md`.

## Pre-Flight

1. **Load the method**: read `skills/mark-forsyth-rhetoric/genius.md` (the catalog, the thesis, the
   announcer rule) and `references/figure-catalog.md` (the working cheat sheet).
2. **Load the lane contract**: `references/lane-contract.md` — specifically which harness gates suspend
   inside this skill and which never do.
3. **If the piece is in Farrice's or a client's voice**, load the voice card as a layer first
   (`_active/farrice-brand/voice/VOICE-CARD.md` or the client equivalent). Forsyth supplies the shapes; the
   voice card supplies the person.
4. **Read the prior taste-ledger pattern**: `.agent/jam/taste-ledger.jsonl`, filtered to
   `domain: "enchantment"`. State it in one line ("last 3 enchant runs you took the fuller cut — starting
   there"). If the ledger is empty, say so.

## Step 0 — Classify the job (always, and it can end the run)

Run `workflows/05-classify-the-job.md`.

**INSTRUCTION** → say so plainly and stop. Enchanting a dishwasher manual, a compliance line, a pricing
table or fair-housing language is a failure, not a flourish. Offer the plain rewrite instead.
**MEMORY** → proceed.
**MIXED** → name the boundary by section and run only on the memory sections.

## Mode A — `compose` (raw intent or raw material → finished piece)

Run `workflows/04-write-to-enchant.md` end to end:

```
diagnose the occasion → prepare completely, aloud → set the establishing shot
  → draft fast in one run → map the announcer → run-up edit
  → pull-through architecture (if sectioned) → gates
```

Single-author law: Forsyth holds the pen for the whole piece. If the brief actually needs multi-expert
composition, say so in one line and route to `/how-i-write` rather than importing a second voice.

## Mode B — `elevate` (existing draft → line, sound, voice-texture)

```
06-enchantment-audit  → name the ONE highest-leverage finding
   ↓
13-announcer-map      → where the voice rises; produce the cut list
   ↓
07-figure-diagnostic  → the ONE figure each stakes moment wants
   ↓
08 / 09 / 10 / 11 / 12 → the owning forge builds candidates
   ↓
14-run-up-rewrite     → any rhythm-dead run deleted and rewritten whole
   ↓
16-pull-through       → if the piece has sections
```

**Scope discipline**: `/enchant elevate` treats line, sound and voice-texture. It does **not** rebuild
structure, thesis or argument. If the audit finds the spine is what is broken, say so and route to
`/depth-audit` → `/depth-inject` or `/how-i-write`. Refining slop on a misdiagnosed draft wastes the pass.

## The Two-Take Contract (taste-bearing work only)

Decided 2026-08-06. The sources disagree about whether ornament can be overdone — 2024: *"I've never seen
somebody overusing the figures of rhetoric"*; 2026: *"there's always going to be a limit where that was too
many chilies."* Rather than guess Farrice's ceiling, `/enchant` measures it.

Return **both**:

- **TAKE A — full ornament.** Forsyth's calibration, governed by the announcer rule only.
- **TAKE B — gate-clean.** The same piece with anything `prose_classifier.py` or the slop ban bank flags
  removed or rebuilt.

Then:
1. Name, in one line, **which take you believe in and why.** A partner with no stake is a vendor.
2. Show the diff in one line: what B lost, what A risks.
3. Take Farrice's verdict and append to `.agent/jam/taste-ledger.jsonl`:
   `{ts, artifact, domain: "enchantment", take_a, take_b, verdict, dials, note}`
4. When a verdict pattern repeats 3+ times, **propose** a default in one line — never set one silently.

**Skip the two-take contract** for mechanical runs (a single line fix, a diagnostic, an audit) and for
INSTRUCTION verdicts. Two takes is for taste-bearing work: the whole piece, the hook, the close, the name.

## Gates

| Gate | Behaviour inside `/enchant` |
|---|---|
| `prose_classifier.py check` | **Runs and prints. Never blocks.** Its flags produce TAKE B and appear in the receipt |
| Density-over-completeness | Suspended when the verdict is MEMORY |
| Low-cognitive-load message gate | Suspended for sound and mystery |
| **Factual veto** | **Never suspends.** Enchantment licenses shaping words, never inventing facts |
| **Cost gate** | **Never suspends** |
| **Compliance / fair-housing language** | **Never suspends** — classed INSTRUCTION by Step 0 |
| `fact-verifier` | Required whenever the piece carries real-world claims |

## Output Contract

- The piece (or the treated draft) — clean, with **no Greek terminology anywhere in the prose**
- For taste-bearing work: TAKE A and TAKE B, plus your stated preference and the one-line diff
- **The receipt**: job verdict · occasion · voice choices · the 2–4 announcer moments with the figure at each
  (own-name, Greek in parentheses) · the cut list · what the classifier flagged and whether it was overridden
  · any UNCONFIRMED claims
- One line naming what you would cut first if the piece had to lose 20%

## Quality Gate

- [ ] The job was classified before any craft ran; INSTRUCTION verdicts stopped the run
- [ ] Ornament sits at 2–4 stakes moments, with plain prose between
- [ ] No line stacks two figures unless both are provably load-bearing
- [ ] No Greek name in delivered prose
- [ ] Read aloud end to end without a stumble
- [ ] Two takes staged for taste-bearing work, with a stated preference
- [ ] The verdict was banked to the taste ledger
- [ ] Real-world claims verified or labeled; no figure applied to a fact that must survive verification
- [ ] `/how-i-write` was not also run on the same passage

## Pairs With

- `/how-i-write` — the composed alternative. Choose one per passage, never both
- `/writers-room` — multi-lens treatment; Forsyth fires there as a lens card
- `/ward-rhetorical-engine` — when the line needs a *punch* rather than a *shape*
- `/depth-audit` → `/depth-inject` — when the structure, not the line, is the problem
- `/voice-os` — when the voice problem spans a body of work rather than one opening
