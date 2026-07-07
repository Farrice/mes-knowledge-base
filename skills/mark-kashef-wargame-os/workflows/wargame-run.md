---
description: A wargame order file exists in tasks/ and needs to be fought on paper — produce the moves, expected observations, failures, forks, recon, aborts, and verification runs a cheap executor will follow blind
---

# /wargame-run — Fight The Mission On Paper

Takes one wargame order (`tasks/NN-<name>.md`) and produces the fought-on-paper wargame (`wargames/NN-<name>.md`) per genius.md's Document Schema. This is the judgment-banking step — "you pay for the genius once, you keep it forever" — so it runs at the highest tier available, not at whatever tier happens to be running the conversation.

## Pre-Flight Gate

1. **Does a wargame order actually exist for this mission?** If not, stop and run `/wargame-order` first — this workflow fights a mission that's already been written, it doesn't invent one.
2. **Has this mission already been drafted?** Check `wargames/NN-<name>.md` and `LEDGER.md` — if a draft exists, this is a redraft, not a first pass; note that in the ledger entry rather than silently overwriting history.
3. **Is the current session's model tier the highest one available for this cap?** Per genius.md heuristic 10, the drafting pass protects the top tier; only the refinement loop (`/wargame-grade`) is allowed to degrade first.
4. **Is recon strictly read-only for this mission?** Confirm no step of the recon plan writes, deletes, or mutates anything before running it.

## Skill Acquisition

Load before executing:
- `skills/mark-kashef-wargame-os/genius.md` — full file: Core Mechanism (supervision transfer), Decision Heuristics 1–10, the Document Schema, the Quality Rubric, Anti-Patterns 1/5/7
- `skills/mark-kashef-wargame-os/references/goal-and-loop-contracts.md` — the `/goal` contract points 2–5 and the effort-economics box
- The wargame order file itself: `.agent/missions/<mission-slug>/tasks/NN-<name>.md`

## Execution

1. **Read the order** — `Read` the full `tasks/NN-<name>.md`, separating the WARGAME ORDER preamble from `=== THE MISSION BRIEF ===`.
2. **Set the consequence horizon** — this is the operator's dial (heuristic 7), not a default the tool silently picks. If Farrice hasn't specified 2nd/3rd/4th order, apply the effort-tag default from `goal-and-loop-contracts.md` (XHIGH missions — website, tax, offer, bugs — get 3rd-order; HIGH missions — copy, local AI, chatbot, model, competitors, automation — get 2nd-order) and state the applied default explicitly in the wargame's header rather than asking and stalling.
3. **Recon, read-only** — `Bash`/`Read`/`Grep` against the exact target named in the order's recon-first line. Only non-mutating commands (`ls`, `find`, `grep`, `cat`, `Read`) — never `rm`, `mv`, `git commit`, or any write.
4. **Route the drafting pass to the top tier** — dispatch via `Agent` with `model: "opus"` (or the highest tier the cap allows), feeding it: the order file, genius.md's Document Schema and heuristics, and the recon findings from step 3. If Opus is capped, degrade exactly one tier per the Opus-Fallback Policy and note the degrade in the ledger — never stall the wargame, and never let the refinement loop's later degrade happen before this one.
5. **Assemble the Document Schema** from the sub-agent's output into `wargames/NN-<name>.md`:
   - Mission spec — problem, audience, CTA/definition of done, all choices pre-frozen
   - RECON NEEDED block — numbered, each with the exact settling command and both branch routes
   - Moves 1–N — each stating Move / Expect (observable) / Fail (+ the cause it signals) / Counter-move / Trigger
   - Abort conditions — observable states where the executor stops and flags
   - Verification runs — each naming the check, the timing, and what pass looks like
6. **Write the file** — `Write` `.agent/missions/<mission-slug>/wargames/NN-<name>.md`.
7. **Append the self-grade** — `Edit` `LEDGER.md`: mission, draft location, an honest point-by-point self-grade against `references/eight-point-standard.md`'s eight points, flagged explicitly as a self-grade pending the adversarial pass in `/wargame-grade`.

## Worked Example (one move, Kashef-grade)

From the `01-website.md` exemplar (`extractions/wargame-source/mes-extraction.md`) — this is the density bar every move in Step 5 must hit, not just the shape:

```
Move 6 — Social proof strip.
Expect: three stat blocks render in a single row at desktop width, wrap to a
  stacked column below 480px.
Fail: fixed-width stat items overflow at 375px — signals missing flex-wrap.
Counter-move: add flex-wrap: wrap to the container.
Trigger: if overflow is observed at any tested breakpoint, apply the counter-move
  before moving to Move 7.
```

Note what makes this Kashef-grade and not merely plan-shaped: the Fail line names a *physical* symptom (overflow at 375px) and the *cause it signals* (missing flex-wrap) — not just "might look bad on mobile." A move that only says "test on mobile" has not cleared rubric criterion 2.

## Content Type Adaptations

| Mission type | Recon shape | Move density | RECON NEEDED focus |
|---|---|---|---|
| **Code build** | trace core flows, grep for existing assets | 8–12 moves, one per functional section | file/asset existence, framework version, whether the executor's own pattern-matching will misfire (e.g. inheriting an ARIA attribute from an earlier move) |
| **Copy-content** | read current page + voice samples | 5–8 moves, one per section/CTA variant | tone match against the sample, which claims need a proof source |
| **Research-analysis** | open each competitor property directly | moves = one per competitor + one gap-map move | source availability, conflict-resolution rule when sources disagree |
| **Ops-automation** | read the process description + tool list | one move per pipeline phase | which step breaks first, whether a human checkpoint is load-bearing |

Every content type still owes all five Document Schema sections — the table above governs emphasis, not which sections are optional. A research-analysis wargame with no abort conditions ("stop and flag if two sources conflict and neither can be resolved") is just as incomplete as a code-build wargame missing one.

## RECON NEEDED — Format Reminder

Each item names the exact command AND both branch routes, not a description of what to check:

```
R2 — brand assets. Command: find . -iname "*.png" -o -iname "*.svg" under assets/.
  If found: copy into site/assets/, reference by relative path in Move 4.
  If not found: inline SVG placeholders, zero <img> tags, tagged <!-- DEMO CONTENT -->.
```

An item that reads "check if brand assets exist" without the command and both routes fails rubric criterion 4 even if the intent is right.

## Output Requirements

`.agent/missions/<mission-slug>/wargames/NN-<name>.md` containing all five Document Schema sections in order, plus a header line stating the consequence horizon applied and the model tier the drafting pass ran at. A matching `LEDGER.md` append with the self-grade.

## Quality Gate

- [ ] Every move has all five parts: Move, Expect, Fail+cause, Counter-move, Trigger (rubric criteria 1–2)
- [ ] Every fork is if-observe-X-then-route — zero "use your judgment" language survives (rubric criterion 3, Anti-Pattern 4)
- [ ] Every RECON NEEDED item carries the exact runnable command and both branch outcomes (rubric criterion 4)
- [ ] Recon ran nothing that mutated state (Anti-Pattern 7)
- [ ] The drafting pass ran at the top available tier — a degrade, if any, is logged and justified, not silent (heuristic 10)
- [ ] The file does not read as a linear happy-path plan (Anti-Pattern 1) — if you can't point to a move that names a specific failure and its cause, it isn't wargamed yet
- [ ] The consequence horizon applied is stated in the header — never left implicit
- [ ] At least one move anticipates the executor's own likely mistake (pattern-matching an earlier move), not just a world-caused failure — rubric criterion 8
- [ ] No move requests the drafting sub-agent's exposed reasoning — only artifacts, moves, and quotes came back (genius.md Anti-Pattern 5, the reasoning-extraction landmine)
