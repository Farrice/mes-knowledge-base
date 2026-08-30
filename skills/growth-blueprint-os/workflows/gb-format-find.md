---
name: "gb-format-find"
description: "Structure×visual format matrix with per-format mechanism cards (retention psychology + failure mode + transfer conditions), cross-niche craft sourcing with receipts, and production recipes at the operator's real constraint level."
expert: "Growth Blueprint OS"
produces: "growth-lab/<niche-slug>/format-playbook.md + exports/format-matrix.html"
---

# Growth Blueprint OS — Format Find (Playbook + Matrix)

## Pre-Flight Gate

- **Read state:** `top-50.md` (the data core — its format columns are Stage 1's input; build on `topic-buckets.md`'s descriptive format buckets, don't redo them), `whitespace-map.md` (format whitespace = attributes 6–7 + belief positioning), `bullseye.md` (the three buckets the picks must carry), `positioning-dossier.md` (delivery-style evidence + real constraints).
- **Pool check:** analyzed pool thin (<15 usable rows)? Say so; offer `gb-topic-scan` first (better) or proceed with the coarser map, labeled.
- **Pack state:** FRESH / STALE / ABSENT — governs specimen citation below.
- **Definition to carry (deflationary, adopted):** a format is just two things layered — the **storytelling structure** (how the spoken words are organized) and the **visual layout** (how it's shot and edited). Separating them is the unlock: structures and visuals recombine. Format hunting is a finite phase — pick 2–3 to test, converge on 1–2 hero formats, then reps.

## Skill Acquisition

Load `genius.md` (§2.3 two-zone sourcing, §2.6 teaching panels; carried: four-part naming, honest ceiling). Load `references/artifact-design-language.md` for the matrix treatment. Wave-2 substance stack available after this workflow: `kallaway-hook-mastery`, `kallaway-addictive-storytelling`, `kallaway-word-mastery` (offer, don't force).

## Execution

### Stage 1 — Build the two databases (data step — degradation tiers apply)

**Storytelling structures** — cluster the ✓ pool by script skeleton, not topic (from `format_hint`, `hook_text`, and transcripts where `transcript_path` exists on flagged outliers; extend from the data, never force-fit a taxonomy). Per structure: beat-by-beat skeleton (2–4 beats), which topic buckets it carries in this niche, count + median outlier + trend, 2–3 linked specimens. Principle to carry into scoring: viewers consume information most easily as lists, comparisons, and rankings — which is why those skeletons dominate most niches.

**Visual layouts** — cluster by production style. Per layout: what defines it, **difficulty/effort for this operator's real constraints** (from the dossier: gear, minutes per video, filming-between-calls reality — a cinematic layout is a bad pick for someone filming between client calls; be honest about production cost), stats, specimens.

**Four-part naming rule (adopted — always shown together):** every structure and layout gets (1) a plain-English name, (2) a one-sentence what-it-is, (3) a 12-second example written as if describing a video's opening, (4) one real linked specimen from the pool. No naked jargon anywhere in the artifact.

**Degradation:** FRESH → every structure/layout row cites ≥2 specimens w/ URL+outlier+date (VERIFIED). STALE → date-stamped, LIKELY, refresh command in the header. ABSENT → the databases build from the operator's pasted favorites + our classification, every performance stat is struck from the tables (not zeroed — absent), the artifact banner reads INTERVIEW-ONLY, and mechanism cards (Stage 2) carry the full weight, labeled as craft knowledge rather than niche measurement.

### Stage 2 — Mechanism cards (ours — the anti-confounding layer)

His matrix says "proven in-niche" with stats that bundle topic, channel, and hook quality — a structure's median outlier cannot isolate the structure's contribution, and copying winners without the mechanism is cargo cult. Every structure (and every recommended combo) gets a **mechanism card**:

| Field | Content |
|---|---|
| Retention mechanism | The named psychological reason the skeleton holds attention (open-loop discharge, ranked-list completion pull, contrarian snap, transformation witness…) — grounded in the retention canon (stack: `kallaway-addictive-storytelling`) and, where transcripts exist, shown operating in ≥1 cited specimen |
| Failure mode | How this structure dies in unskilled hands — the specific way it goes wrong (list with no payoff ramp, myth-kill that blames the viewer, case study with no stakes) |
| Transfer conditions | What must be true for the mechanism to survive the jump to THIS operator's topics and constraints — and what breaks it. This is the answer to "will it work for *my* topic?", which stats alone cannot give |
| Confound note | What the in-niche stats bundle (channel effect, topic effect, celebrity effect) — printed so the number is read as pool evidence, not causal proof |

### Stage 3 — Combination matrix + whitespace pairs

Structures × layouts: which pairs actually appear in the niche's winners (cell = median outlier + count + specimen), which are empty. Read against the whitespace map: an unclaimed pair that suits the operator is format whitespace. **Invented rows (adopted move):** promote the operator's chosen buckets or signature assets into candidate *structural* rows whose cells read "open" — the matrix is a survey PLUS a proposal, visually distinguished. Cross-niche craft layer (two-zone rule, receipted — his own doctrine, under-used by him): for the top mechanism cards, pull 1–2 cross-niche specimens demonstrating the craft at its best, cited, labeled craft-inspiration-only.

### Stage 4 — Pick the test set (2–3 combos)

Score each candidate combo, showing reasoning: (1) **best vehicle for their information** — which structure lets them communicate what they actually know most clearly; (2) **proven in-niche or a deliberate whitespace bet** — at most ONE whitespace bet in the picks; (3) **fits delivery style + real constraints** (dossier evidence); (4) **carries all 3 buckets** — a format that only works for one bucket is a narrow tool. Per pick: why, the beat-by-beat skeleton, the visual recipe, **a production recipe at the operator's constraint level** (gear list, setup, minutes per rep, what to model from the specimens before filming), 2–3 model videos to study, and which sample-batch slots it should carry. State the hero-format rule plainly: after 2–3 batches the data crowns 1–2 heroes — testing ends, reps begin. **Honest ceiling (adopted):** recording and editing are un-automatable — the recipe is model-and-mimic (angles, distance, pacing, where the text hook sits), and the operator's last mile is the quality.

### Stage 5 — The matrix artifact + save

Render `exports/format-matrix.html` per `references/artifact-design-language.md`: rows = structures, columns = layouts, plain-English names + four-part explainers behind an info affordance; cells show specimen thumbnail/link + outlier badge + count — recognition over numbers; empty cells dim ("nobody's doing this"), whitespace pairs glow; "Try these 3 first" strip up top with mechanism cards attached; legend carries its own caveats inline (e.g. flagging a celebrity-inflated scale band — name the trap inside the chart). Premium Minimal semantics; export row. Save `format-playbook.md`, update `manifest.json` (deps: [top-50, whitespace-map]), snapshot priors. One-line state + next: `gb-blueprint`.

## Output Contract

Execution prompt: `references/prompts-v2/format-playbook-matrix.md` — honor its Output Contract.

1. **State markdown** — `format-playbook.md`: structure database → layout database (every entry four-part named, constraint-scored) → **mechanism cards** → combination matrix table (whitespace pairs + invented rows flagged) → cross-niche craft specimens (receipted, craft-only) → the 2–3 test picks w/ production recipes + model links → hero-format rule → blind-spot section (confound note; pack coverage) → data-tier declaration.
2. **Client HTML** — `render_brief.py --client` → `exports/format-matrix.html` + `format-playbook-client.html`.
3. **Export** — PDF; export row on both.

## Content-Type Adaptations

| Mode | Adaptation |
|---|---|
| **Self-run (Farrice)** | Constraint level = his actual production reality; mechanism cards cross-wired to the existing kallaway-* retention canon rather than restated |
| **Client engagement** | Production recipes written for the client's team hands (or their editor) — implementation-grade; matrix is a named deliverable a client can circulate |
| **Lead-magnet step-down** | The matrix image + one full mechanism card as proof-of-method; remaining cards, picks, and recipes are the paid depth; one CTA row |

## Quality Gate

Score against `genius.md` §3; any single 1 fails. Load-bearing here:
- **Q5 (hard):** every structure and every pick carries a mechanism card — retention mechanism, failure mode, transfer conditions. "Proven in-niche" alone fails.
- **Q2:** every database row ≥2 specimens or explicitly absent-tier; cross-niche specimens receipted.
- **Q6:** production recipes executable at the operator's stated constraint level without a follow-up question.
- **Q7:** confound note printed; at most one whitespace bet in the picks and it is labeled a bet.
- **Q9:** matrix in exports/, manifest updated, next step named.
