# Prompt Renaissance — Runbook (structure-pure v2)

*Goal: refactor ALL ~1,860 canonical crown-jewel prompts to the Farrice-approved structure-pure v2 standard. Wave 1 (150, commit `f5ea83a18`) proved the pattern: 150/150, zero errors, 1 honest fidelity-low flag.*

## The v2 Standard (Farrice-approved 2026-07-10)

The originals produced outstanding outputs BECAUSE of their deterministic practitioner structure. The exemplars' FUNCTION (deterministic output expectation) must survive; their CONTENT (long fabricated samples, invented stats) must go.

**KEEP (verbatim where good):** Role/activation frame (real credentials only) · Input Required `[BRACKET]` architecture · Execution protocol (steps, decision rules, frameworks — never thin the methodology) · Deploy When triggers.

**TRANSFORM** — replace example outputs / "Key Elements Demonstrated" with:
1. `## Output Contract` — exact deliverable components, format, length bounds
2. `## Output Skeleton` — section-by-section SHAPE specimen, placeholders/one-line descriptors ONLY; zero fabricated content, names, or results
3. `## Quality Gate` — 3-6 checkable criteria distilled from what the exemplar was demonstrating

**STRIP (always):** fabricated statistics ("73% conversion", "$127K", "17-second rule" precision without source) · invented clients/case studies/logos presented as real · MES/"virtuoso" meta-framing · unverifiable credibility padding.

**FIDELITY RULE:** never invent methodology to fill gaps. If a prompt is thin once fabrication is stripped, mark frontmatter `fidelity: low` and report it.

**FILE FORMAT:** `skills/<skill>/references/prompts-v2/<same-filename>` (extraction-era: `extractions/<name>/prompts-v2/`). Frontmatter: name, source_prompt (repo-relative), skill, standard: structure-pure-v2, refactored: <date>. NEVER edit originals, SKILL.md, genius.md, registries, or workflows.

## Wave Cycle (repeat until queue empty)

```bash
python3 execution/renaissance_queue.py --status                 # remaining count
python3 execution/renaissance_queue.py --wave-size 150          # → wave-input.json (resumable: skips existing v2s)
```

Then launch the fleet: one **Sonnet (effort high)** agent per skill group in `wave-input.json` (parallel; disjoint dirs so no write conflicts; per-agent structured report {skill, refactored, skipped, fidelity_low, summary}). Fleet prompt template = the wave-1 pattern: read group's originals fully → skim the skill's genius.md once for real credentials → write v2s per the standard above → report.

After each wave:
1. Spot-check 1-2 v2s from the most fabrication-heavy group: 3 required sections present, zero invented names/stats, frontmatter correct.
2. `python3 execution/prompt_library.py build` (indexes kind=prompt-v2)
3. Commit: `git add skills/*/references/prompts-v2 extractions/*/prompts-v2 .agent/prompt-index.json && git commit -m "feat(renaissance): wave N — <count> prompts to structure-pure v2 (<fidelity-low count> flags)" ` + Co-Authored-By trailer
4. Log fidelity-low files in the commit body for Farrice's review.
5. Next wave. Session limit mid-wave = fine: re-running the queue builder auto-skips completed v2s.

Final wave: add `--include-extractions` to sweep the 42 raw-era originals.
