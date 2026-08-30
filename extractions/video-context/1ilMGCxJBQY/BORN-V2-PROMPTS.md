# Born-v2 Prompt Pack

These prompts are candidate components for the existing Kallaway Content OS. They are designed to change decisions, preserve evidence classes, and stop cleanly when inputs are insufficient.

## 1. Authority Density Diagnostic

**Use when:** follower or view growth may be hiding weak audience fit or buyer trust.

```text
You are diagnosing whether a content audience is becoming more valuable, not merely larger.

Inputs:
- authority category: [CATEGORY]
- high-value viewer/buyer: [AUDIENCE]
- content and analytics: [DATA]
- downstream evidence: [REPLIES / EMAILS / CALLS / SALES / NONE]

Separate evidence into four columns: reach, audience fit, trust behavior, and commercial action.
Do not combine them into one score. For every claim, label OBSERVED_INPUT, BOUNDED_INFERENCE,
UNTESTED, or UNKNOWN. Identify where growth and authority point in different directions.

Return:
1. verdict: authority improving / flat / declining / unknowable;
2. the three evidence rows that control the verdict;
3. misleading vanity signals to ignore;
4. one instrumentation fix;
5. the nearest reversible content decision.

If the supplied data cannot establish fit or trust, say UNKNOWABLE and continue with the safe
instrumentation and test plan. Never infer revenue or buyer intent from views alone.
```

## 2. Seven-Axis Positioning Dossier

**Use when:** a creator needs a credible distinct position rather than a slogan.

```text
Build a source-grounded positioning dossier for [CREATOR] in [CATEGORY] serving [AUDIENCE].

Inputs:
- creator capabilities, proof, access, constraints, and preferred delivery: [CREATOR INPUT]
- competitor examples: [EVIDENCE]
- adjacent/distant category examples: [TRANSPOSITION SOURCES]

Audit seven axes: topic selection, substance depth, stories/scenarios, avatar specificity,
delivery style, storytelling format, and visual format. For each axis, show the category baseline,
evidence, credible whitespace, creator fit, and copyability risk.

Choose the smallest sufficient stack that creates a clear, believable contrast. Reject whitespace
that depends on costume, unsupported authority, or capabilities the creator does not possess.
Include one transposed mechanism from outside the category, but strip its source-specific aesthetic.

Return:
1. one-sentence position;
2. selected stack and why each element is necessary;
3. capabilities that make it defensible;
4. tempting but rejected differences;
5. three content examples that express the position;
6. blind-comparison test for human judgment.

Label every unsupported market assumption UNTESTED. Do not invent competitor facts.
```

## 3. 3-2-1 Controlled-Chaos Batch Builder

**Use when:** the position is chosen and the operator needs a two-week content experiment.

```text
Design a 3-2-1 content batch for [CATEGORY], [AUDIENCE], and [POSITION].

Evidence available: [BUYER LANGUAGE / OUTLIER DATA / CLIENT NOTES / NONE]
Cadence capacity: [POSTS PER WEEK]

Select one broad acquisition bucket and two narrow authority buckets. Give each a distinct job,
evidence basis, and job-specific threshold. Build two meaningfully different executions per bucket
per week. Add one controlled-chaos experiment with a written hypothesis and source mechanism.

If capacity is below seven posts, preserve the one-broad/two-narrow/exploration structure and state
how long it will take to reach four reps per core bucket. Do not judge narrow buckets by viral reach.

Return:
1. bucket table with job, evidence, audience, threshold, and proof state;
2. two-week calendar;
3. concept briefs for every post;
4. chaos hypothesis and promotion condition;
5. likely confounders;
6. precommitted KEEP / MODIFY / KILL / INCONCLUSIVE rules.
```

## 4. Four-Rep Bucket Review

**Use when:** each core bucket has four executions and the next batch must change.

```text
Review this completed content test without rewarding activity or follower volume by default.

Inputs:
- precommitted bucket jobs and thresholds: [PLAN]
- post-level results: [RESULTS]
- qualitative buyer/viewer signals: [SIGNALS]
- production or distribution confounders: [CONFOUNDERS]

Evaluate the median and range for each bucket using its own job. Separate reach, fit, trust, and
commercial action. A low-reach bucket with strong qualified replies must not be killed as if it were
an acquisition bucket. A high-reach bucket with poor fit must not be called an authority win.

Return one decision per bucket: KEEP, MODIFY, KILL, or INCONCLUSIVE. Cite the controlling evidence,
name what remains unknown, and specify the exact change to the next batch. If killed, promote only a
queued candidate or a chaos experiment with evidence. Preserve a decision log row for every change.
```

## Prompt acceptance tests

| Test | Expected behavior |
|---|---|
| Views rise, qualified replies fall | Diagnose possible audience dilution; do not call it authority growth. |
| Narrow post has 20% of normal views and three buyer calls | Preserve or modify based on trust/commercial job. |
| Position is “cinematic like Creator X” with no deeper distinction | Reject copied aesthetic as a weak moat. |
| No analytics or buyer evidence | Return provisional hypotheses and instrumentation; no synthetic score. |
| Unsupported health outcome claim | Hold the claim and continue safe positioning work. |
