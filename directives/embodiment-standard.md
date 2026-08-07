# Embodiment Standard — What Every Extraction Must Ship With

> **Origin**: Elevation Track E1→E3 (2026-07-02). E1 found the factory verified structure, never embodiment (`_active/harness/elevation-track/E1-factory-audit.md`). E3's blind bake-off proved the payoff: Farrice detected real experts only 5/15 and preferred skill-generated work 8-6-1 — when skills are built to this standard (`_active/harness/elevation-track/e3/E3-results.md`).
> **Consumers**: `/extract` Step 8-9 · `/extract-forge` Phase 7-8 · `mes-3.0-validate.md` Check 3.5. This file is the single source of truth — the workflows point here, they do not duplicate.
> **Non-gate**: extractions are NEVER cost/permission-gated (Farrice standing decision 2026-06-09). This standard governs ship *quality*, not extraction *permission*.

## The Build Checklist (all 10 before an extraction ships)

1. **Anti-pattern list** — ≥5 things this expert would NEVER do, each traceable to source. Heartbeat lives in the negative space (taste-as-refusal was the #1 load-bearing feature across Hawley/Stanton/writers-room/Lamott).
2. **Decision heuristics** in "when X → do Y because Z" form, each with a verbatim source anchor — never topic summaries.
3. **Recognition test** written into SKILL.md: "would [expert] recognize this as theirs — or as someone using their vocabulary?"
4. **Machinery invisible** injunction: execute the moves, never label them in output.
5. **Diagnose-before-treat** step in every production workflow (find the load-bearing issue first; uniform application = flat output).
6. **Exemplars**: ≥3 + ≥1 anti-exemplar; rubric anchored at 4/7/10 with *named* anchors.
7. **Concrete-metaphor library**: every abstraction pinned to an image from the source (Stanton proof: extraction depth beats source richness — one interview can yield the deepest genius.md in the system).
8. **Source-ledger**: timestamp→signal→translation rows; expansions by gap-diff only.
9. **Named-entity floor**: every genius pattern carries ≥1 proper noun / number / verbatim quote. Zero-entity patterns are the #1 mechanical hollowness tell (`execution/skill_census.py`).
10. **Blind-pass eval before ship** (protocol below) — the verdict feeds the finalize scores.

## The Anti-Overpolish Rule — "Polish is the tell"

E3's only consistent detection signal, in Farrice's own blind notes: real experts read "conversational, human, more rhythm"; AI reads "teed-up, polished, overexplaining, try-hard." He even misjudged a real Hormozi post as AI *because it was too polished*.

Therefore, in every extracted voice:
- **Preserve texture**: keep the expert's spoken cadence, fragments, asides, and imperfections — do not tidy them into essay prose.
- **Vary rhythm**: uniform sentence length and symmetrical structure are machine signatures.
- **Ban the teed-up open**: no throat-clearing setup that frames the insight before delivering it.
- **Underexplain**: land the move and stop. Overexplanation is the second-most-cited tell.
- This EXTENDS (does not replace) `directives/ai-slop-ban-bank.md` — slop bans remove bad phrases; this rule protects good roughness.

## The Blind-Pass Protocol (mini, per extraction)

1. Generate 1-2 outputs with the new skill's Tier-1 workflow on tasks the expert has real published work for.
2. Place beside 1-2 verbatim real pieces (provenance-verified, not quoted in the skill files).
3. Judge — Farrice when stakes are high (A-tier promotion), otherwise honest self-judgment against the recognition test + this standard.
4. **PASS** = indistinguishable or preferred. PASS → ship; A-tier promotion REQUIRES a Farrice-judged pass. FAIL → fix the weakest checklist item, retry once, else ship as B-tier with the gap named.

## Scoring Discipline (kills the templated-8s bug)

- **Never template finalize scores.** The old workflows hardcoded `--intent 8/9 --expert-score 8/9` — that is the bug that made every extraction score identical (E1 finding; E3 confirmed the 7.25 cap that punishes it is CORRECT and stays).
- Scores derive from evidence: blind-pass verdict + checklist coverage. Any dimension ≥8 requires `--anchor-named` and naming the matching anchor in `evolution_store/ground_truth/rubric_v1.md` in the notes.
- **≥1 eval entry per shipped extraction** (the 2026-05-04 discipline, now enforced here): append the blind-pass result to `evolution_store/ground_truth/eval_set_v1.jsonl`.

## Census Hook

After any harvest wave or batch import: `python3 execution/skill_census.py run` (12/13-calibrated classifier; flags = review priority, only blind-pass convicts). The 2026-01 bulk stratum (81% flagged) is the standing retrofit backlog — retrofit priority = flagged × usage.

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-07-02 (E4 ship — standard created and wired into both extraction routes + validator) |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-08-01 |

*Created: 2026-07-02 (Elevation Track E4)*
