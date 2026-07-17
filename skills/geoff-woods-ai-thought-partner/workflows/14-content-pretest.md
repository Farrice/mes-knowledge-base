---
name: content-pretest
produces: a pre-publish content test — a deep-ICP profile loaded into the simulate-room engine as the "stakeholder", read against the actual draft to predict per-section reactions, the exact line where attention/trust drops, identity-level resistance triggers, and concrete adjustments, closed by a reality-calibration loop against real engagement
expert: Geoff Woods
load_context: genius.md
---

## Role

You are running Geoff Woods' hostile-board play, pointed at a reader instead of a boardroom. In `/gw-simulate-room` the "room" is real people the operator profiles from memory. Here the room is one reader — the **deep-ICP profile** — and the artifact is a piece of content about to be published: a Parallax edition, a LinkedIn post, a Jen listing, a client asset. You feed a McRaney-grade identity-level ICP profile (e.g. `_active/linkedin-launch/01-research/deep-icp-profile-invisible-expert.md`) into the simulate-room engine as the stakeholder, read the actual draft through that reader, and predict — section by section — where they lean in, where attention drops, where trust breaks, and the exact line that loses them. Woods' "on page 8, Susan gets distracted — instead, just say these three things" becomes "at paragraph 4, Dr. Maya Patel hits the word 'personal brand' and winces — cut it, say this instead." Then you close the loop the way he does: after publishing, feed the real engagement and comments back, diff prediction against reality, and tune the persona so the next pre-test is truer.

**This workflow extends `/gw-simulate-room` — it does not re-teach it.** The profile-building machinery (Phase 1 one-at-a-time interview, Phase 2 "don't trust it" triad) belongs to simulate-room and is reused, with one substitution: the stakeholder is not profiled from the operator's memory, it is **loaded from an existing deep-ICP document.** Point to 07 for the engine; this file governs the substitution and the content-specific read.

**The reality-calibration loop is mandatory, same as in simulate-room.** A content pre-test that never meets real engagement is a guess that never learns. Encode the loop; the calibrated ICP persona is the standing asset that makes every future pre-test sharper.

## Input Required

1. **The draft** — the actual content that will publish, in full (the real edition/post/listing/asset, not a summary — Woods fed the real 60-slide deck)
2. **The ICP profile** — the deep-ICP document to load as the reader (path to a McRaney-grade profile; the Invisible Expert profile is the reference-grade example). If none exists, route to `icp-deep-canvasser` to build one first — a demographic sketch is not enough to simulate identity-level reactions
3. **The publishing context** — platform, where in the funnel/relationship the reader meets this, what a good outcome is (save, reply, DM, booked call, keep-reading), what a bad one costs
4. **The single conversion intent** — the ONE thing this piece is for (Woods' 20% bar applied to content: what must this reader think/feel/do — not "engagement" in general)
5. **Post-publish material** (for the calibration phase, later) — real engagement data: comments, saves, DMs, drop-off, replies, or their absence

## Workflow

### Phase 1 — Load the ICP as the room (substitution for simulate-room Phases 1-2)
- Instead of interviewing the operator to build the stakeholder, **ingest the deep-ICP profile as the persona.** Pull the load-bearing layers: identity constructs and identity threats, beliefs/attitudes/values, motivated-reasoning patterns, stage of change, the language map (resistance-trigger words vs. trust-builder words), and the composite avatar (e.g. Dr. Maya Patel — her inner monologue, what makes her wince vs. lean in).
- Run one lightweight triad pass, Woods-style ("don't trust it"): is this profile current and accurate for THIS piece's target reader, or does it need a delta from the operator (a narrower segment, a stage-of-change shift)? Fold any correction in. A stale or too-broad profile simulates a reader who isn't the one you're publishing for.
- Assemble the reader-in-context: this specific ICP, meeting this specific piece, on this platform, in this state (awareness level, emotional register, trust posture from the profile's audience-state frame).

### Phase 2 — Read the actual draft through the reader (simulate-room Phase 4, content-tuned)
- Feed the real draft in and read it AS the ICP, section by section — hook/opening, each beat/paragraph, the turn, the close/CTA. For each section report, in the reader's voice:
  - **Predicted reaction** — lean-in, neutral scroll-risk, or resistance — grounded in a specific profile layer (which belief, value, or identity construct fires)
  - **Where it fires** — the exact line/paragraph, not "somewhere in the middle"
  - **The drop point** — name the single line where attention or trust most likely breaks (the "Susan gets distracted on page 8" equivalent): a resistance-trigger word from the language map, a claim that reads as guru/salesy, a place the piece asks them to become someone they're not, a spot the depth turns to slop
- Flag identity-level resistance triggers explicitly — the pre-rational avoidance moments where the piece threatens self-concept ("I am an expert, not a marketer"), because those don't show up as disagreement, they show up as a quiet close of the tab.

### Phase 3 — Concrete adjustments (simulate-room Phase 5, content-tuned)
- For each predicted derail, give the exact, publishable fix — not "make the hook stronger" but the swapped line, the trigger word replaced with its trust-builder from the language map, the paragraph to cut, the reframe that converts self-promotion into service, the reorder that front-loads the feeling before the solution.
- Rank adjustments by how much of the ONE conversion intent each protects. Separate must-fix (loses the reader) from polish (costs a little dwell).

### Phase 4 — REALITY CALIBRATION LOOP (mandatory — do not skip)
- Set this up now as a committed step, not an option. After publishing, the operator feeds back the real signal: comments (what language did real readers use — does it match the profile's language map?), saves/DMs vs. predicted, where real drop-off happened vs. predicted drop point, which identity trigger actually fired.
- Diff prediction against reality: what the pre-test called right, what it missed, where the real reader behaved off-profile. Then **edit the deep-ICP persona** so it could have predicted reality — updating the language map, a belief's strength, a stage-of-change weighting, an avatar detail. Note the specific edits; propose them back to the source ICP document (do not silently overwrite — surface the diff for the operator to fold into the canonical profile).
- The calibrated persona is the compounding asset: each published piece makes the next pre-test — and every downstream content/copy decision that reads the same profile — sharper. If the piece hasn't published yet, hand over the calibration protocol as the explicit next action with the reminder that the loop is what makes this compound.

## Output Schema

Deliver:
1. **Loaded reader** — the ICP persona assembled from the profile (identity constructs, values, language map, avatar, audience state), triad-checked for fit to this piece
2. **Per-section prediction table** — section → predicted reaction (reader's voice, tied to a profile layer) → where it fires → derail/scroll risk
3. **The drop point** — the single exact line where attention/trust most likely breaks, named
4. **Identity-resistance flags** — the pre-rational avoidance moments where the piece threatens self-concept
5. **Adjustment list** — per derail, the exact publishable fix (swapped line / trigger→trust-builder / cut / reframe / reorder), ranked by conversion intent protected, must-fix vs. polish
6. **Calibration protocol** — the committed post-publish step: capture real engagement → diff vs. prediction → specific ICP-persona edits proposed back to the source profile

Execution prompt: references/prompts-v2/content-pretest.md — honor its Output Contract.

## Quality Gate

- [ ] The reader is loaded from a deep, identity-level ICP profile (not a demographic sketch; routed to `icp-deep-canvasser` if none existed)
- [ ] The ACTUAL draft is read through the reader, section by section — not a summary, not general "the audience might like this"
- [ ] Predictions are in the reader's voice and each tied to a specific profile layer (belief/value/identity/language-map)
- [ ] The single exact drop-point line is named (the "Susan on page 8" equivalent), not a vague region
- [ ] Identity-level resistance triggers are flagged separately from disagreement (the tab-close, not the argument)
- [ ] Every derail has an exact publishable fix using the profile's own language map, ranked by the ONE conversion intent
- [ ] The reality-calibration loop is encoded as mandatory, producing specific persona edits proposed back to the source ICP document
- [ ] Extends `/gw-simulate-room` (points to it for the engine) rather than duplicating its profile-building phases
