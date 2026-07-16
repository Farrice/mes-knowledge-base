---
description: "The compounding test — score any existing or prospective 'second brain' on four retrieval axes (connection / contradiction / freshness / provenance) to expose storage-only builds. Kieran Flanagan's 'Storage Is Easy. Retrieval Is the Hard Part.' packaged as a sell-side diagnostic distinct from /library-health-check."
---

# Library Retrieval Audit

Run the two-column compounding test against a system someone ALREADY has (or is about to build). It separates storage+search ("a filing cabinet with a chatbot") from retrieval+evolution ("a brain that compounds"), scores four axes 0-2, and converts the gap into scope.

> Distinct from `/library-health-check`: that audits YOUR own KB for maintenance (run monthly). This is a **sell-side diagnostic** you run on someone ELSE's system or a prospective one — the gap it exposes IS the pitch.

> The one-liner it earns (closing thesis slide, verbatim): "The gap widens every week. The people building these systems now create an asset that compounds daily. Everyone else starts from zero every time they open a new chat window."

## Pre-Flight Gate
- Load `genius.md` §Retrieval-vs-Storage Diagnostic + §Rubric.
- Kieran's frame (verbatim): "A lot of people think of it as just storage and search... dumping everything into a folder, you can search notes with the AI, you call it a second brain, and the knowledge really decays over time... The hard part really is the retrieval and evolution."
- You need read access to (or a description of) the target system: how it stores, how it's queried, whether ingest is ongoing.

## Skill Acquisition
Read `genius.md` (four axes + how each maps to Simon machinery). This diagnostic doubles as a coverage map: each failing axis names the exact Simon workflow that installs the fix.

## Execution
1. **Classify the build** against the two columns:
   - **Storage + Search** (most people): dump everything in a folder · search notes with AI · call it a second brain · knowledge decays silently.
   - **Retrieval + Evolution** (compounds): AI connects ideas you'd never link · contradiction detection across notes · freshness tracking on every source · provenance on every idea.
2. **Score the four axes, 0-2 each** (0 = absent / storage-only, 1 = partial, 2 = live):
   - **Connection** — does it surface links across notes you'd never make yourself? (Storage returns only what you searched.) → maps to health-check stage 7 (undrawn connections).
   - **Contradiction** — does it flag conflicts across entries? (Storage keeps both, notices nothing.) → maps to stage 1.
   - **Freshness** — is every source freshness-tracked and up to date daily? Kieran: "It's always up to date... it enriches every single day." → maps to stage 5 + `/library-ingest-triage` freshness pass.
   - **Provenance** — can it tell you where every idea/decision originated? Kieran: "a great system for telling you where ideas and decisions... originated from." → maps to the 6-property Source field + stage 3.
3. **Retrieval-output test** — ask the system to produce the compounding tell: a knowledge-graph-ranked priority view. The savant target (demo, verbatim "Cortex"): "Cortex ranked 5 priorities from your knowledge graph · 3 projects tracked," session strip "ctx: 3 projects · 12 goals · 63 lessons," and one-click query buttons **Brief me** / **Pre-mortem**. Each priority card must carry: title + urgency tag + project tag + one-line status ("Blocked 19 days on VP Sales review. Launch window closes Dec 12.") + three columns **WHY NOW / DEPENDS ON** (named people, e.g. "Priya Menon · Legal") **/ SUGGESTED ACTION** ("Book 30-min audit slot this week or ship gate. Decision dec-1"). A storage-only system cannot produce this — it has no graph to rank from. Score: can it / can't it.
4. **Compute the verdict**: /8 on the four axes + graph-retrieval pass/fail. ≤3 or graph-fail = "storage, not a brain" (a filing cabinet with a chatbot). 4-6 = partial. 7-8 + graph-pass = compounding.
5. **Convert gap → scope**: each failing axis routes to its fix — Connection/Contradiction/Freshness/Provenance gaps → `/library-health-check` install + schema upgrade (`/library-kb-design`); no ongoing enrichment → `/library-ingest-triage`; no compounding loop → `/library-second-brain` or `/library-compound-loop`; flat/one-tier → `/library-brain-ladder`.
6. **Deliver the one-liner** (step-intro thesis) as the emotional close — the gap widens every week.

## Content Type Adaptations
| Target system | Adaptation |
|---|---|
| Obsidian / Notion dump (DIY) | Almost always scores ≤2 (pretty, linked, abandoned) — the canonical floor; lead with the graph-retrieval fail |
| Cloud project / "point at docs" | Search is good, evolution is zero; Freshness + Compounding are the exposed gaps |
| A prospect's existing "AI brain" | Sell-side: score live on a call, show the four-axis gap, scope the install |
| Your own KB (self-check) | Use `/library-health-check` instead — this diagnostic is for external/prospective systems |

## Output Requirements
The two-column classification + four-axis score card (0-2 each, with the specific observed evidence per axis) + graph-retrieval pass/fail with the priority-card contract used as the test + verdict (storage / partial / compounding) + gap→scope routing table (each failing axis → the Simon workflow that fixes it) + the closing one-liner. Deliver as a diagnostic sheet a buyer can see themselves in.

Execution prompt: references/prompts-v2/retrieval-compounding-audit.md — honor its Output Contract.

## Quality Gate
- Are all four axes scored with OBSERVED evidence (not assumed), and is the graph-retrieval test actually run against the priority-card contract?
- Does the verdict name the matching state (storage / partial / compounding) rather than a bare number?
- Does every failing axis route to a specific fix workflow (gap = scope), not a generic "improve it"?
- Is this framed sell-side (someone else's/prospective system), not confused with the self-maintenance `/library-health-check`?
- §Rubric Retrieval>Storage ≥8 requires all four axes live AND graph-retrieval pass.

## Stacking
Upstream diagnostic that scopes the rest of the Simon suite: failing axes route to `/library-health-check`, `/library-kb-design`, `/library-ingest-triage`, `/library-second-brain`, `/library-compound-loop`, `/library-brain-ladder`. Pairs with `liam-mley` discovery when the audited system is a business (the retrieval gap becomes an AIOS Context-Layer scope).
