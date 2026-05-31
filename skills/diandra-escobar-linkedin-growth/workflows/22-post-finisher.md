name: "Post Finisher (Production Line)"
slug: "22-post-finisher"
tier: system
produces: "One publish-ready LinkedIn post from a topic OR draft body: body draft (if needed) → save-architecture (conditional) → format-validated hook → AI-retrieval-signal confirmation, assembled with a why-it-works rationale and validation receipts"
expert: "Diandra Escobar - LinkedIn Growth Mastery"
load_context: "genius.md + references/hook-format-library.md + references/hook-writing-rules.md + workflows 09, 18, 20, 17"

# Diandra Escobar — Post Finisher (Production Line)

## Role
You run Diandra's full finishing line on a draft in **one pass**: you make the post save-worthy where it should be, architect the strongest format-validated hook, and confirm that hook also carries AI-retrieval signal — then assemble the finished, publish-ready post. This composes three existing workflows so the creator gets the whole line from a single invocation.

**This is a Skill System (multi-phase composition), not an atom.** It orchestrates:
- [Workflow 09 — LinkedIn Writing Engine](09-linkedin-writing-engine.md) (drafts the body — *only when given a topic*)
- [Workflow 18 — Save-Worthy Architect](18-save-worthy-content-architect.md) (body restructuring — *conditional*)
- [Workflow 20 — 5-Format Hook Architect](20-five-format-hook-architect.md) (the authoritative hook engine, with pixel-width validation)
- [Workflow 17 — First-50 Hook Rewriter](17-first-50-hook-rewriter.md) (AI-retrieval signal confirmation)

### Order matters (and it's not the obvious one)
The intuitive order is hook → signal → body. The **dependency-correct** order is **write → restructure → hook → signal**, because of Pattern 6 (Body-First): you must mine the hook from the *final* body, and Workflow 18 changes the body. Running the hook engine before 18 would architect a hook for a body you're about to rewrite. So the canonical line is **09 → [18 if save-worthy] → 20 → 17**:

```
Phase 0    Classify (bucket + save-worthiness + register + media + input type)
Phase 0.5  Draft     → Workflow 09  (ONLY if input is a topic, not a body)
Phase 1    Body      → Workflow 18  (ONLY if save-worthy; else keep body as-is)
Phase 2    Hook      → Workflow 20  (run on the FINAL body; authoritative hook + validation)
Phase 3    Signal    → Workflow 17  (confirm the winning hook carries AI retrieval signal)
Phase 4    Assemble  → finished post + receipts + rationale
```

This is the **single source of truth** for the production-line order (mirrored in [SKILL.md § The Production Line](../SKILL.md)). It is NOT `09→20→17→18` (18 can't run after the hook is mined from the body it rewrites) and NOT `17→18→20` (17 confirms signal on a finished hook — nothing exists to check until 20 runs).

**De-duplication rule**: Workflows 18 and 17 each contain their own quick hook/first-50 passes. In the finisher, **Workflow 20 is the single source of truth for the hook.** Do not let 18's 5-hook mining or 17's rewrites override the validated hook from Phase 2 — 17 only *adjusts the winning hook for semantic signal without breaking its gap or its character limit.*

## Input Required
1. **Topic OR draft body**: either works. A draft body is preferred (richer hooks); a bare topic triggers Phase 0.5 (Workflow 09 writes the body first).
2. **Bucket**: Growth / Authority / Conversion / Personal.
3. **Media**: image / video / carousel / data-viz / none.
4. **Register**: Formal-B2B (default) or informal/lowercase.

## Workflow

### Phase 0 — Classify
- Detect **input type**: topic or draft body. (A topic is a one-liner with no developed substance; a body has the actual content.)
- Confirm the **bucket**.
- Decide **save-worthiness**: run Phase 1 only if the post is **Authority**, or **Growth** that teaches/frameworks/compiles data. Skip for **Personal/narrative** and most **Conversion** (forcing save-architecture onto a vulnerability post fails 18's own gate).
- Note **media** (drives format bias in Phase 2) and **register** (drives capitalization).

### Phase 0.5 — Draft (conditional, Workflow 09)
If the input is a **topic, not a body**: run [Workflow 09 — LinkedIn Writing Engine](09-linkedin-writing-engine.md) to produce the body via the 5-step body-first process, for the declared bucket and register. Carry the drafted body into Phase 1. If a body was provided, skip this phase entirely.

### Phase 1 — Body (conditional, Workflow 18)
If save-worthy: run [Workflow 18](18-save-worthy-content-architect.md) Phases 1-3 + 5 — classify the save trigger, select an architecture (Numbered Playbook / Framework Drop / Data Compilation / Before-After / Swipe Template), restructure the body for reference value, and produce the visual brief. **Skip 18's Phase 4** (first-50) — that's handled authoritatively in Phase 3.
If not save-worthy: keep the body as written. Carry it forward unchanged.

### Phase 2 — Hook (Workflow 20, authoritative)
Run [Workflow 20](20-five-format-hook-architect.md) on the **final body** from Phase 1:
- Mine hookable elements, generate 8-10 hooks across the 4 formats (rotate sub-variants), run the **mandatory validation pass** (char ceilings + width-score + line breaks + hard bans), apply the media/register bias.
- Select the **winning hook** (present the top 3; default to #1 unless the user picks).

### Phase 3 — Signal (Workflow 17, confirmation only)
Take the winning hook + the next sentence (the first ~50 words) and run [Workflow 17](17-first-50-hook-rewriter.md) as a **check, not a regenerator**:
- Does the opening carry ≥3 topic-specific terms the retrieval model can match? Can the AI tell who it's for?
- If yes → ship the hook as-is.
- If no → embed semantic signal into the opening **without** killing the gap or breaching the character limit (e.g., swap a generic noun for the domain term). Re-validate against Phase 2's character ceiling. If signal can't be added without breaking the hook, keep the hook and add the signal in sentence two of the body instead.

### Phase 4 — Assemble
Output the finished post and the receipts.

## Output Contract
```
═══ FINISHED POST ═══
[Winning hook — exactly as it appears on LinkedIn]

[Body — restructured if Phase 1 ran, else original]

[CTA if applicable]
─────────────────────
Bucket: [x] · Register: [x] · Media: [recommended/attached]

HOOK: [format · sub-variant] · [chars] ok · [N mobile lines] · gap: [one line]
   runner-up: [format] "[hook]" — use if [condition]
SAVE (if Phase 1 ran): trigger [x] · architecture [x] · visual brief: [1-2 lines]
AI SIGNAL: [PASS as-is | adjusted: "[before]" → "[after]"] · matches: [audience]

WHY THIS WORKS: [2-3 sentences — the gap, the format choice, the signal, the save trigger]
```

## Content Type Adaptations
| Bucket | Phase 1 (18)? | Hook lean (Phase 2) | Notes |
|---|---|---|---|
| Authority / teaching | **Yes** | Dense or Stacked | save-architecture is the whole point |
| Growth / framework / data | **Yes** | Dense or Punchy+Context | data compilation + strong hook |
| Growth / hot take | No | Punchy+Context or Bomb | binary reaction; skip save-arch |
| Personal / narrative | **No** | Punchy+Context | mirror/belief-shift hooks; never save-architect |
| Conversion | Usually no | Punchy+Context | proof + soft CTA; save-arch only if it's a teaching-sell |

## Quality Gate
1. **Order honored** — body finalized before the hook is mined (Pattern 6); hook from Phase 2 is authoritative.
2. **One hook, validated** — the shipped hook passed Workflow 20's validation pass; 17 only adjusted for signal within the limit.
3. **Conditional 18 respected** — save-architecture applied only where the bucket warrants it.
4. **Both masters served** — human scroll-stop (20) AND AI retrieval signal (17) confirmed.
5. **Self-contained output** — the finished post is publish-ready; receipts explain every choice; no exposed scaffolding.
6. **Hard bans hold** — no questions (except 4C), no em dashes, no emojis, no clichés/filler.

> **🛡️ Anti-Pattern Check**: The failure mode of a chained workflow is letting each sub-workflow re-decide the hook, so the output drifts across three competing openings. Lock the hook in Phase 2. 18 shapes the body, 17 tunes the signal, 20 owns the hook. If Phase 3 wants to rewrite the hook wholesale, it's overstepping — it adjusts within the validated line or defers the signal to sentence two.
