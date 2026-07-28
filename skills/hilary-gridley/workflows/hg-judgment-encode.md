---
description: The crown-jewel pipeline — turn an expert's tacit taste into a deployable evaluator tool via edit-pair mining (Column A/B → patterns → criteria → plain-English pass/fail rubric → system prompt)
---

# hg-judgment-encode — Mint an Evaluator From Edit Pairs

Encode one expert's judgment on one artifact class into a tool anyone (human or agent) can run work against. The standard comes from EVIDENCE — real before/after edits — never from introspection or generic principles.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` — decision frameworks + anti-patterns bind.
- **Evidence gate**: ≥5 real before/after pairs of ONE artifact class exist or can be assembled (run `/hg-edit-pair-harvest` first if not). Fewer than 5 → tell the operator what to collect; do NOT proceed on invented standards. 3-4 pairs → proceed with `provenance: thin` flagged in the output.
- **Scope gate**: one artifact × one audience × one outcome, stated up front. "General writing feedback tool" = refused; narrow it first.

## Skill Acquisition

- `genius.md` §Crown Jewel + §Anti-Patterns
- `references/source-quotes.md` §The pipeline (register calibration)

## Execution

1. **Assemble the corpus.** Table: Column A = original drafts, Column B = the expert's revised/approved versions. Note who edited and when. Exclude pairs where the edit was factual correction only — you're mining taste, not accuracy.
2. **Mine the delta.** For each pair, name what changed and why it's better. Then across ALL pairs: which edits recur? Surface 8-12 candidate patterns with a frequency count and one verbatim example each. (AI's role here is pattern legibility — the standard lives in the edits.)
3. **Distill to criteria.** Collapse to 5±2 criteria — recurring, consequential, expressible as a check. Drop one-off preferences. Each criterion gets a name in the expert's own vocabulary where the edits reveal it.
4. **Write plain-English pass/fail.** Per criterion: what passing looks like, what failing looks like — concrete enough that a new hire self-grades accurately on day one. Include one real example of each from the corpus.
5. **Compose the evaluator system prompt**: role line naming whose judgment this encodes + the scoped artifact/audience/outcome → evaluation steps (score each criterion pass/fail with a quoted line of evidence from the submitted work) → feedback (what to improve, in priority order) → **suggested rewrites in the expert's register** for every failed criterion → closing instruction: never rewrite the whole piece; return it to the author for their pass (kick-the-crutch).
6. **Validate against the corpus.** Run 2 held-out Column A drafts through the evaluator. It must flag what the expert actually changed. Misses → tighten criteria, rerun once.
7. **Ship + install.** Deliver the evaluator prompt + a 3-line usage note (when to run it, what to do with a fail, when to escalate to the human expert). Name it artifact × audience × outcome (e.g. "Executive Email Editor — get to yes").

## Content Type Adaptations

| Artifact class | Corpus source | Watch for |
|---|---|---|
| Exec/client emails | Sent-folder before/after, manager revisions | Lead-with-message, ask clarity, tone thresholds |
| LinkedIn/social posts | Draft vs published, verdict logs | Hook standards, voice thresholds, slop tells |
| Sales/landing copy | Draft vs shipped + performance notes | Claims discipline, proof placement, CTA logic |
| Briefs/PRDs/strategy docs | v1 vs approved | Decision clarity, altitude, what's-cut |
| Agent/AI outputs | Generation vs human-corrected | Recurring correction classes → becomes a harness gate |

## Output Requirements

- Deliverable: pattern table (with frequencies + examples) + criteria set + plain-English rubric + paste-ready evaluator system prompt + validation report (which held-out edits it caught/missed).
- The expert must recognize the patterns as theirs ("that IS what I do") — run the recognition line past them when possible.
- Execution prompt: `references/prompts-v2/judgment-encode.md`

## Quality Gate

Score against genius.md rubric: standard provenance (evidence-mined?), pass/fail legibility (day-one self-grade?), feedback actionability (rewrites in register?), purpose specificity (narrow-named?), teaching residue (returns work to author, shows criteria?). Any anti-pattern present — generic principles, whole-piece rewriting, second-brain scope — is a fail; fix before delivery.
