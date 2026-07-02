# E1 — Factory Audit: The Embodiment Delta
*2026-07-02 · Elevation Track (plan: "Wake Up Raphael") · 3 Opus lenses + Fable synthesis + main-thread spot-verification*

## Verdict

The factory produces heartbeat **by accident, not by design**. Every quality mechanism in the extraction pipeline is structural or self-referential — nothing ever compares a skill's output to the expert's real published work. Skills come out embodied when the builder happened to mine deep (Stanton, Hawley) and hollow when they didn't (the 2026-01 bulk stratum). The good news: the delta between heartbeat and hollow is now catalogued, most of it is mechanically detectable, and the fix points are exact.

## Finding 1 — Where the factory stops short (all claims file:line-verified)

- **QC is structural only.** `/extract` S3 validation is optional ("Recommended", skippable); the only human gate eyeballs ONE sample workflow (extract.md:97-98). `/extract-forge` P7 = "files exist" + read 2-3 workflows (extract-forge.md:143-148). `mes-3.0-validate.md` never executes a prompt — it checks grammar, file completeness, and taste-vibes, and is opt-in (:6).
- **Self-referential calibration.** Exemplars are mined *from the source transcript* (mes-3.0-extract.md:132-149) and graded against MES's own canonical extraction (extract-mastery/genius.md:72-74) — never against the expert's corpus. The factory grades its own homework.
- **The system's one true embodiment test never fires at build time.** "Could the named expert distinguish this from their own work?" lives at content_creation_gate.md:40-42 (Step 5b, MANDATORY) — but only when *using* a skill, never when *building* one. ✅ spot-verified.
- **Extraction ships pre-scored.** extract.md:100-106 templates `--intent 8 --expert-score 8 --adversarial 7` into the finalize command (forge: 9s). ✅ spot-verified. This is the upstream origin of the flattened-7.25 score pathology: authors assert grades, nothing measures them.

## Finding 2 — Heartbeat anatomy (Hawley · Stanton · writers-room · Lamott-Allen)

Ranked by load-bearingness; all four share the top five:

1. **Taste-as-refusal**: explicit anti-pattern / would-never-do lists (Hawley 8 items, Stanton 10, writers-room Anti-Slop, Lamott Failure Modes). Heartbeat lives in the negative space.
2. **Verbatim-anchored decision heuristics** — "when X, do Y because Z" with the expert's quote attached; never topic summaries.
3. **Recognition test stated inside the skill**: "would [expert] recognize this as X — or someone using X-vocabulary?"
4. **Machinery kept invisible**: execute the move, never label it on the page.
5. **Diagnose-before-treat gate**: writers-room Phase 2.5 (the literal 2/10→10/10 fix) — find the load-bearing issue, concentrate treatment; uniform application = flat output.
6. Anchored good/bad exemplar pairs + 4/7/10 rubric with *named* anchors.
7. Concrete-metaphor library carrying every abstraction (Stanton's cable-car clamp, beach ball, dinosaur).
8. Provenance discipline: source-ledger with timestamp→signal→translation rows; expansion via gap-diff only (Lamott).

**The Stanton natural experiment (single most important E1 result):** thinnest source of the four (one ~11k-word interview, TED talk deliberately excluded) yet the deepest genius.md (26KB ✅ spot-verified). **Richness of extraction, not richness of source, produces heartbeat.** Source-count gates are the wrong lever; mining-depth standards are the right one.

## Finding 3 — Hollowness signature (+ a disconfirmed prior)

**3 of 4 suspected-hollow skills were actually embodied** (alan-aragon, michael-israetel, sean-dollwet — all 2026-07-01 claude.ai harvest, all pass the generalist test with real study citations, dollar thresholds, named tools). Hollowness tracks **vintage, not batch-ness**: the hollow stratum is the **2026-01 bulk import (~2,800 files)**, e.g. adam-enfroy genius.md patterns 1-14 (adjective-soup, zero specifics) fossilized beneath a rich 2026-07 enrichment bolt-on (patterns 15-33).

Signature, ranked by predictive reliability:
1. **Zero named entities per pattern** (no study, number, tool, dollar figure, verbatim quote) — the strongest single tell.
2. **Referenced-but-never-instantiated criteria** ("passes all 5 validation criteria" — the 5 never listed).
3. **Dangling cross-references** — workflows cite `genius.md § Decision Framework / § Voice DNA` that don't exist (✅ spot-verified on Enfroy: 8 workflows reference them, genius.md has 0 such headers). Grep-detectable.
4. Identical workflow skeletons within a skill (moderate — bodies can still be specific).
5. Generic slop-bans as the only voice layer (weak alone).
- **File count is an anti-signal**: 3-workflow Dollwet is dense; 8-workflow Enfroy hides a hollow core. Never use size as a quality proxy.

## THE EMBODIMENT DELTA CHECKLIST (the E4 payload)

**Build standard — every extraction must ship with:**
- [ ] Anti-pattern list: ≥5 things this expert would NEVER do, each traceable to source
- [ ] Decision heuristics in "when X → do Y because Z" form, each with verbatim anchor
- [ ] Recognition test written into SKILL.md: "would [expert] recognize this as theirs?"
- [ ] "Machinery invisible" injunction (execute moves, never name them in output)
- [ ] Diagnose-before-treat step in every production workflow (load-bearing issue first)
- [ ] ≥3 exemplars + ≥1 anti-exemplar; rubric anchored at 4/7/10 with named anchors
- [ ] Every abstraction pinned to a concrete image/metaphor from the source
- [ ] Source-ledger (timestamp→signal→translation) + expansion-by-gap-diff rule
- [ ] **Blind-pass eval before ship**: run one Tier-1 workflow, compare against 2-3 real published pieces by the expert; verdict feeds the finalize scores (kills the hardcoded 8/9s)
- [ ] Named-entity floor: every genius pattern carries ≥1 proper noun/number/verbatim quote

**Detection heuristics for E2 census (mechanically checkable):**
1. Named-entity density per genius pattern (0 = hollow flag)
2. Dangling §-reference grep (workflow cites nonexistent genius.md section)
3. Uninstantiated-criteria scan ("N criteria/rules" with no list following)
4. Workflow-skeleton similarity hash within each skill
5. Presence checks: anti-patterns section · recognition test · anchored rubric · source-ledger
6. **Vintage stratum** (git add-date): 2026-01 bulk import = highest-risk; 2026-07 harvest = low-risk
7. Ignore file/workflow count entirely

## E4 insertion points (exact)
- `extract-forge.md` Phase 7 → new step **7.4 Blind-Pass Test** (primary slot)
- `mes-3.0-validate.md` between Check-3 and Check-4 → **Check 3.5 Blind-Pass** (both routes inherit); make validation non-optional for A-tier promotion
- `extract.md` CHECKPOINT-2 (:97-98) → require blind-pass verdict instead of one-workflow eyeball; replace hardcoded finalize scores (:100-106) with verdict-derived scores
- Wire content_creation_gate.md Step 5b's question into build time via the checklist above

## Revised E2 design (evidence-driven changes to the plan)
- **Stratify the census by vintage**, not by my original sample frame: (a) 2026-01 bulk import, (b) mid-period forges, (c) 2026-07 harvest. Expected hollow concentration: (a) >> (b) > (c).
- Automate detection heuristics 1-6 above as a census script; reserve human/bake-off attention for flagged skills + A-tier candidates.
- E3 bake-off sample should include: one 2026-01 bulk skill (expected fail), one enrichment-hybrid (Enfroy-type), one harvest skill (expected pass), one heartbeat control (expected pass), one high-usage daily driver.

## Provenance
Three Opus 4.8 read-only lenses (factory map · heartbeat anatomy · hollowness signature), synthesized on Fable; four load-bearing claims independently re-verified on the main thread (hardcoded scores, Step 5b location, Enfroy dangling refs, Stanton 26KB). Factual grounding: all file:line citations retained above.
