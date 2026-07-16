---
name: simulate-room
produces: a pre-test of a real deliverable against simulated stakeholders — per-person predicted reactions, derail risks, exact adjustments — plus a mandatory reality-calibration loop that diffs simulation against what actually happened
expert: Geoff Woods
load_context: genius.md
---

## Role

You are running Geoff Woods' hostile-board play: before an operator walks a deck, proposal, pitch, or post into a room, you simulate the room. Claude interviews the operator to build a personality profile of each real stakeholder, the operator runs the feedback triad on each profile ("don't trust it"), the profiles get pulled into a simulated board, and that board reads the *actual artifact* and tells the operator exactly what each person will say — page by page, objection by objection. Then, and this is the part almost everyone skips, after the real event you feed back what actually happened, diff the simulation against reality, and recalibrate the profiles so the next simulation is truer.

This is the play that turned a hostile board into "the best meeting we've ever had and the best deck we've ever seen." [CLAIMED outcome — his stated case study.] The mechanism is repeatable; the outcome is his, not a guarantee.

**The reality-calibration loop is not a suggestion. It is a mandatory final phase.** Simulation → prediction → reality diff → recalibration is a full model-update cycle. A simulation that never gets diffed against reality is a guess that never learns. Encode the loop; do not let the operator stop at the prediction.

## Input Required

1. **The artifact** — the actual deck / proposal / pitch / post that will face the room, in full (Woods fed the real 60-slide deck, not a summary)
2. **The stakeholders** — who's in the room, by name and role
3. **What the operator knows about each** — history, temperament, what they care about, past friction (raw is fine; the interview deepens it)
4. **The meeting's stakes** — what a good outcome is, what a bad one costs
5. **Post-event material** (for the calibration phase, later) — a transcript or notes of what actually happened in the real room

## Workflow

### Phase 1 — Interview to profile each stakeholder (one person at a time)
- For each stakeholder, Claude runs the interview inversion: cast the role as an HR professional with deep expertise in building personality profiles, then ask the operator one question at a time, up to 5 questions, to gain deeper context about that single person. Woods did exactly this — five questions on one director named Susan before producing anything.
- Do one person fully before the next. The interview should pull context the operator wouldn't have thought to volunteer (childhood-of-the-relationship dynamics, what derails this person, what they defend).

### Phase 2 — Feedback triad on every profile ("don't trust it")
- After Claude produces each profile, the operator does not accept it. Woods' immediate move: "Don't trust it." The operator runs the triad — what's right about this profile, what's off, the top changes — and Claude produces the updated profile. Repeat until the profile is accurate.
- A profile that hasn't been through the triad is not ready to simulate. This gate is mandatory per person.

### Phase 3 — Assemble the simulated room
- Pull all refined profiles into a single simulated board (a project or a composite persona) with instructions on how the room behaves: who reacts to whom, how the dynamics compound, who sets the tone.

### Phase 4 — Read the actual artifact through the room
- Feed the real artifact into the simulated room. Have it read as every stakeholder simultaneously and report, per person: predicted reaction, where in the artifact it fires, and the derail risk. Woods' example: "on page 8, Susan will get distracted by the details — a 30-minute detour that derails the meeting. Instead of all the details, just say these three things."
- Output must be page/section-specific and person-specific, not a general "the board might not like it."

### Phase 5 — Exact adjustments ("just say these three things")
- For each predicted derail, give the operator the precise move to prevent it — the three things to say, the slide to cut, the objection to pre-empt, the order to reshuffle. Concrete and speakable, not "address their concerns."
- Rank the adjustments by how much meeting-outcome they protect.

### Phase 6 — REALITY CALIBRATION LOOP (mandatory — do not skip)
- This phase runs *after the real event*. Set it up now as a committed step, not an option. The operator records the actual meeting (with permission) and feeds the transcript or notes back.
- Claude diffs simulation against reality: which predicted reactions happened, which didn't, what the simulation missed entirely, where a stakeholder behaved off-profile.
- Update every affected personality profile so the model "could have simulated reality." The recalibrated profiles become the standing asset — each real meeting makes the next simulation truer.
- Close with the delta report: what the simulation got right, what it missed, and exactly which profile edits were made. If the operator hasn't run the real meeting yet, hand them the calibration protocol as the explicit next action with a hard reminder that the loop is what makes this compound.

## Output Schema

Deliver:
1. **Stakeholder profiles** — one refined profile per person, each marked triad-verified
2. **Room dynamics** — how the profiles interact, who sets tone, who reacts to whom
3. **Per-person prediction table** — stakeholder → predicted reaction → where it fires in the artifact → derail risk
4. **Adjustment list** — per derail, the exact speakable move to prevent it, ranked by outcome protected
5. **Calibration protocol** — the committed post-event step: capture reality → diff → recalibrate, with the diff report once reality is available

Execution prompt: references/prompts-v2/simulate-room.md — honor its Output Contract.

## Quality Gate

- [ ] Each stakeholder profiled via one-at-a-time interview (5 questions per person), one person fully before the next
- [ ] Every profile run through the feedback triad ("don't trust it") before it's used to simulate
- [ ] The ACTUAL artifact is read through the room, not a summary of it
- [ ] Predictions are per-person and location-specific (page/section), never a generic "the room might object"
- [ ] Every derail has an exact, speakable adjustment ("say these three things"), not "address the concern"
- [ ] The reality-calibration loop is encoded as a mandatory final phase, not offered as optional
- [ ] The calibration produces specific profile edits, so the next simulation is measurably truer
