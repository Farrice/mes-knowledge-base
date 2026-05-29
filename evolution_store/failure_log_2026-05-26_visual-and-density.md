# Failure Log — 2026-05-26 — Visual aesthetic + Document density (Resonance launch)

**Severity**: HIGH. Two taste-failures on the same client deliverable, same session.
**Project**: andrea-dj (Resonance)
**Cost incurred**: $1.69 wasted Fal spend + ~30,000 token-words of sub-agent output rated unusable.
**Reporter**: Farrice (taste call)
**Calibration trace**: Claude (8/8/7 honest) → cap engine (7.0-7.25, "bimodal marginal") → Farrice (0/10). Three layers of inflation; Farrice is ground truth.

---

## Failure 1 — Visual aesthetic (rated 0/10)

### What was produced
12 launch poster prototypes at `projects/andrea-dj/launch/03-visual-variants/variant-{a,b,c}-hero-shots/` via fantastic-posters + `editorial-fashion` style, palette override per variant. Cost: $1.69 (medium quality, 12 × ~$0.14).

### Direct user critique
> "Visually they look like a group fitness classroom meeting, not a room full of life and energy, representing the resonance of meeting someone and meeting people you can connect with. This isn't hip, modern, or trending at all. It looks like an advertisement for a group fitness class for elderly people."

> "Aesthetically, the images with the DJ equipment, the vinyl, and the accent pieces were probably the best, and even the picture of the room was good. Every image with people in it, including one of the main images, showed a representation of a disconnect versus a resonance with each other."

### Root cause (3 axes)

**Axis 1 — Tool mismatch**: Used `skills/fantastic-posters/` with `editorial-fashion` style. That skill is a POSTER GENERATOR with text overlays + magazine-cover framing. Per `execution/creative_router.py`, "modern DJ party scene with people + energy + environment" should route to **Higgsfield Soul 2.0** (photoreal lifestyle). Wrong branch picked because brief used keyword "editorial" (matched Rule 2 → fal-poster, before Rule 3 → photoreal scene could match).

**Axis 2 — Prompt-language mismatch**: Prompts used "documentary photograph / Magnum reportage / editorial broadsheet / photographed entirely from behind / no posed." These cues pull the model toward reverential museum-quality + observer-distance + static fashion-magazine framing. The "photographed entirely from behind" framing specifically produced the yoga-class-lineup disconnect signal.

**Axis 3 — Aesthetic-reference culture gap**: `aesthetic-references.md` has 28 specific references but they're fashion-photographer-dominant + institution-rooted (Blue Note, NYRB, ECM, Gentlewoman) — museum-coded, not party-coded. Missing entirely: Boiler Room/Cercle daytime archives, Latin American daytime party visual culture, Chicago house lineage, modern digital-native creators, party-energy films. Prompts had no aliveness cues to draw from.

### What's salvageable
- A1-empty-room, A2-gesture-fader, B1-empty-courtyard-room, B3-tile-brick-corner, C1-empty-cream-room, C2-hand-resting-fader (6 of 12)
- All 3 variant DESIGN.md specs (palette/type/geometry remain correct)

### What's discarded
- A3-group-from-behind, A5-single-listening, B2-body-in-room, B4-group-architectural, C3-two-shoulders, C4-side-of-face (6 of 12 — all people shots carry the disconnect signal)

### Prevention rule (logged to memory)
`feedback_visual-tool-routing.md`: NEVER skip `execution/creative_router.py` pre-flight. Brief that mentions PEOPLE doing something → Higgsfield Soul. Brief that mentions STYLE FAMILY → fantastic-posters. Verify before generating.

---

## Failure 2 — Document density (rated implicitly very low — unusable for client)

### What was produced
| Deliverable | Lines | Words (est.) |
|---|---|---|
| Announcement package | 1,109 | ~9,500 |
| Outreach playbook | 1,291 | ~14,600 |
| Gap-action sprint | ~450 | ~4,200 |
| Master README + handoff | ~400 | ~3,500 |
| **Total** | **~3,250** | **~31,800** |

### Direct user critique
> "These documents are so verbose and so filled with fluff that when I do give them to Andrea, there's too much context going on. She needs to know exactly what she needs to do and who she needs to reach out to, and to come with an example so that she can move with speed and confidence."

> "Generic and just filled with words. The density-to-value is very bad. We need to improve that so that every word counts, and if it doesn't matter, it does not need to be put into here to overload her cognitively. Or distract her."

### Root cause
Wrong-agent-for-the-job + completionism over actionability. Sub-agents deployed:
- `master-copywriter` (correct skill, wrong scope — built a strategy doc when needed a tactical content calendar)
- `general-purpose` (defended depth — went 14,600 words against 5-8K budget, ARGUED for keeping it)
- `brand-system-builder` (correct for system docs, wrong for client operational handoff)

All three sub-agent classes optimize for COMPLETENESS. Andrea needs DECISION SPEED + EXAMPLES. The right skill set: `simplify`, `prose-doctor`, `word-rhythm`, plus master-copywriter restrained to "one tactical doc per role, one example, one CTA."

### Prevention rule (logged to memory)
`feedback_density-over-completeness.md`: Client-facing operational docs default ≤2 pages. Multi-page only when the doc is paste-into-AI reference material, not action. Density-to-value > completeness. CTA at top, not buried.

---

## Cross-cutting lesson

Both failures share a root cause: **wrong sub-agent for the job, defaulting to skills that optimize completeness over actionability**. The `/supercomputer` routing table in `directives/supercomputer-mode.md` exists for exactly this reason — and I bypassed it in both visual and document workstreams. From now on:

1. **Visual gen**: always pre-flight through `execution/creative_router.py` (deterministic routing)
2. **Document gen**: brief sub-agents with EXPLICIT page-count + density constraints + worked-example requirement; default to ≤2 pages for client operational

## Calibration trace (lesson for cap_engine)

The cap_engine correctly downgraded my 8/8/7 → 7.0-7.25 (marginal). But Farrice's 0/10 reveals: the cap engine still under-detected this specific failure-class because:
- Cap engine reads the deliverable METADATA (composite scores, structural moves) but cannot see VISUAL OUTPUT or CLIENT-USE-CONTEXT
- Visual taste call requires actually viewing the images (which the cap engine can't)
- Density-vs-completeness requires knowing the user (Andrea) and their reading context (15-min coffee shop)

**Suggested cap-engine enhancement**: when the deliverable involves visual outputs OR client-facing operational docs, the cap should require an additional gate — "has this been bimodal-taste-checked against the actual end-user context?" This catches the failure-class the rubric anchors miss.

---

## Tags
- visual-tool-routing
- prompt-language-mismatch
- aesthetic-reference-gap
- density-vs-completeness
- agent-skill-mismatch
- cap-engine-blindspot
