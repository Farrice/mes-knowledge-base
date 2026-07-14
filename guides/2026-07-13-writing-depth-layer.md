---
date: 2026-07-13
session: writing-depth-layer
tier: operator-guide
status: enriched
---

# Writing Depth Layer — What We Built 2026-06-14 and How to Use It

> `/deepen` plus eleven `/depth-*` workflows (`skills/writing-depth-layer/`) — a cross-cutting **conductor** that deepens any existing draft by diagnosing which of 8 depth deficits it has, then composing the craft roster (Hawley → Roth/Connelly → Cole/Lamott-Allen → voice) in Ordering-Law sequence at a per-vertical dose. It owns zero craft of its own and returns the deepened draft + a Depth Receipt change-map. Deeper spec: `skills/writing-depth-layer/genius.md` + `references/depth-deficit-taxonomy.md` + `references/routing-map.md` + `references/vertical-dosing.md`.

## ⚡ If you only read 10 lines

- **EXPLICIT-ONLY invocation — the standing doctrine.** No routing binding, no auto-fire (Farrice's call). The layer runs only when you type `/deepen` or a `/depth-*` command; nothing routes here silently.
- The tell for reaching for it: a draft EXISTS and the ask is "make it land / more soul / more voice / less generic / less AI / competent but hollow."
- The Deepen Loop: DIAGNOSE (score the 8 deficits, name the 1–3 weakest) → SELECT + ORDER → APPLY → RECEIPT. Diagnose before treating, always.
- The Ordering Law (non-negotiable): architecture FIRST → scene/detail → line/rhythm → truth/voice LAST. Line-craft before architecture = well-crafted sentences with no spine.
- Deepening is not lengthening — it often means CUTTING. "Comprehensive" output = failure.
- The truth slot is ALWAYS delegated to the matching `/really-real-*` pass; the layer calls it, never reimplements it.
- Dose by vertical: social = LIGHT, fix 1–2 deficits max, never over-deepen a 150-word post into an essay; copy = depth without losing conversion (offer/CTA/proof intact).
- Diagnosis only → `/depth-audit` (no rewrite). One named deficit → `/depth-inject` (surgical). Unsure which workflow → `/depth-gate` (routing slip only).
- Never name-drop experts inside the deepened prose — moves integrate invisibly; experts appear only in the Depth Receipt.
- Wrong tool checks: cold-start converting copy → `/copy-engine`; LinkedIn/social refinement specifically → `/writers-room`; premium piece from raw material → `/how-i-write`.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/deepen` | Full Deepen Loop on any draft: auto-detect vertical, diagnose, compose owners, deepened draft + Depth Receipt | Flagship — any existing draft that needs to land |
| `/depth-audit` | Scores on the 8 deficits + 1–3 weakest links + recommended owners/order. **No rewrite** | You want diagnosis before deciding on treatment |
| `/depth-stack` | Maximum-depth staged pipeline through every applicable owner, per-stage deltas, consolidated Receipt | Highest-stakes pieces only |
| `/depth-social` | Light, fast deepening preserving hook/brevity/scannability | LinkedIn/X/IG/newsletter-short drafts |
| `/depth-copy` | Depth with offer/CTA/proof/clarity intact | Ads, VSLs, landing pages, emails, offers |
| `/depth-marketing` | Humanity + specificity + belief (Sutherland reframe + Roth) | Marketing/brand media |
| `/depth-book` | Full layered stack, architecture-led (Hawley) | Book/long-form chapters |
| `/depth-client` | Trusted advisory prose, argument architecture (Fareed) + restraint | Client/personal-brand deliverables |
| `/depth-inject` | Fixes exactly ONE named deficit with one owner; minimal-touch rewrite + Receipt | You already know the single weak spot |
| `/depth-line` | Sentence rhythm, compression, cadence, read-aloud pass | Line-level craft only |
| `/depth-voice` | Rhythmic fingerprint install (voice-as-music + ghostwriting-voice-engine) | Prose sounds like AI/anyone |
| `/depth-gate` | One-screen routing slip: which workflow, which owners, what order/dose. Routing only, never rewrites | Draft + intent in hand, unsure which door |

## The mental model

Three ideas make the rest obvious:

1. **A draft can be finished and still be dead.** All limbs — hook, structure, CTA — none of its blood. Most drafts fail the second earning: craft earns the next sentence, but truth + heart earn the reader's trust. The layer exists for competent-and-hollow.
2. **It's a conductor, not another writer.** Its entire intelligence is composition: what is hollow here, who fixes that, in what order, at what dose. Each of the 8 deficits has a named OWNER in the roster (no architecture → Hawley; hollow/generic → Connelly + Lamott-Allen; no voice → voice-as-music + Cole; flat thesis line → Ward Farnsworth; and so on, with sub-lane specialists like Browder for flat stakes, Orlean for undecided structure, Shukman for unearned awe, Harding for flat sensory detail). The layer loads the owner's `genius.md` + workflow and applies the move into the prose. If no owner exists for a "deficit," it is not a depth deficit — surface it, do not invent craft.
3. **Explicit-only is the design, not an oversight.** Depth passes are taste-bearing and expensive; auto-firing them on every draft would either dilute voice work or burn cost on drafts that only needed formatting. You opt in, deliberately, per piece. The corollary: the layer never fires on your behalf, so remembering it exists is your job — the tell is any "this feels flat" reaction to a finished draft.

## Using it well

**What it is, mechanically.** The `.agent/workflows/` shims (`deepen.md`, `depth-gate.md`, `depth-stack.md`, etc.) each load `skills/writing-depth-layer/SKILL.md` + `genius.md` + the matching `skills/writing-depth-layer/workflows/*.md`, then run the documented loop and end with the Depth Receipt: weakest link found, moves applied (deficit → move → expected reader effect → source principle), dose/vertical fit, remaining risk. Seven structure-pure v2 prompts live at `skills/writing-depth-layer/references/prompts-v2/` — honor their Output Contracts when a deliverable matches.

**When to reach for it.** Draft exists + "make it land" in any register, across social, copy, marketing/brand, book/long-form, and client verticals. It sits alongside the Hawley extraction as its architecture layer: Hawley sets the spine first on new work; the Depth Layer conducts the deepening pass on a drafted piece.

**When NOT to** (each with the cheaper door):
- Pure speed copy from cold start → `/copy-engine`.
- Formatting/structure-only with no depth deficit → just edit.
- Research synthesis → `execution/research.py`.
- LinkedIn/social refinement as its own discipline → `/writers-room`.
- Building a premium piece from raw material across all altitudes → `/how-i-write` (which routes back here via `/depth-audit` → `/depth-inject` on its existing-draft branch).
- Full rewrite when the user asked for diagnosis only, or when a single `/depth-inject` would do.

**Anti-duplication contract (binding on anyone extending this).** Technical sentence-craft knowledge lives ONLY in `skills/lamott-allen-really-real-writing` (the expanded `references/technical-craft-36-rules.md` module — the source video was already forged there; never re-extract it). The per-vertical `/depth-*` orchestrators CALL `/really-real-*` as their truth slot and must never re-implement it. `writing-depth-layer/genius.md` is composition/routing intelligence only — zero craft re-teaching.

**Honest edges.** Composite logged 7.25 — the auto-calibrator ran conservative; it passed independent review plus live verification on social and copy drafts, but book/client verticals have less live mileage. The worked end-to-end examples live in `references/composition-guide.md` (flat LinkedIn post, flat copy, flat memoir paragraph — each diagnosed → chained → deepened + Receipt) rather than a live session artifact. And explicit-only cuts both ways: the layer will never rescue a hollow draft you didn't think to send it.

## Composition table (options, not pipeline steps)

| Pair with | How | It earns its cost when |
|---|---|---|
| Noah Hawley extraction | Hawley spine first, then `/deepen` on the draft | New long-form where architecture was never set |
| `/really-real-*` passes | Called automatically as the truth slot | Always — this wiring is built in, never manual |
| `/how-i-write` OS | It routes to `/depth-audit` → `/depth-inject` on existing drafts | Premium multi-altitude builds |
| Voice OS (`VOICE-CARD.md` + dial) | Depth pass first, voice layer per standing binding | Anything shipping as Farrice |
| Chain Step 6 | Receipt's "remaining risk" feeds adversarial scoring | Scoring a deepened piece honestly |
