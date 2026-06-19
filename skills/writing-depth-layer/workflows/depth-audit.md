---
description: "/depth-audit — score a draft on all 8 depth deficits (0/1/2), name the weakest links with evidence quotes pulled from the draft, and recommend the composition chain (owners, order, dose) for the stated vertical. Diagnosis only — never touches the prose."
---

# Depth Audit (Diagnosis Only)

A surgeon does not cut before reading the chart. The single most expensive error in this whole layer is refining slop on a misdiagnosed draft — fixing a deficit the piece doesn't have crowds clean prose with technique, while the real weakest link stays untouched. This workflow exists to make that error impossible. It is the diagnostic instrument that runs *before* any deepen pass: it scores, it cites the evidence, it prescribes the chain — and it stops. No sentence is rewritten, no owner is loaded to apply a move.

This mirrors the writers'-room diagnose-before-treat gate one altitude up: you do not get to "improve" a draft until you can name, with quotes, exactly what is wrong with it and in what order it must be fixed. The output is a scorecard plus a recommended composition chain — a treatment plan a `/depth-*` orchestrator (or a human) can execute, with the prose left exactly as the writer left it.

## Pre-Flight
Read these files before executing:
1. `skills/writing-depth-layer/genius.md` (the composition brain — § 3 The 8 Depth Deficits, § 5 The Ordering Law, § 8 Per-Vertical Dosing, § 11 Decision Framework)
2. `skills/writing-depth-layer/references/depth-deficit-taxonomy.md` (the per-deficit detection signals, before-snippets, and the 0/1/2 severity rubric for each deficit — this is the scoring instrument)
3. `skills/writing-depth-layer/references/vertical-dosing.md` (which deficits matter most per vertical, the dose, and the function to PRESERVE — sets where DIAGNOSE looks first and what the chain must not break)
4. *(For the chain recommendation only)* `skills/writing-depth-layer/references/routing-map.md` (deficit → owner → real path → real command, and the Ordering Law sequence) — consult to *name* owners/commands; do NOT load any owner skill on a diagnosis-only run.

> **🔒 Pre-Flight Gate**: Before scoring, run the **Decision Framework** in `genius.md § 11 Decision Framework`, item 2 — confirm the user asked for *diagnosis only*. STOP condition: this workflow NEVER rewrites prose and NEVER loads an owner skill to apply a move. If the user wants the draft deepened, this audit is the first half — finish the diagnosis, then hand off to the matching `/depth-*` orchestrator. Naming an owner is allowed; loading one to treat is not.

## Input Required
- **The draft** — the full text to audit, pasted inline. Partial drafts get a partial diagnosis; say so if only an excerpt is supplied.
- **The vertical** — social / copy / marketing / book-long-form / client-personal. This sets which deficits to suspect first and which dose the recommended chain prescribes. If ambiguous, ask; the chain is wrong if the vertical is wrong.
- **The function to protect** — the one thing this piece must keep doing (convert, stop the scroll, hold authority, carry the arc). This becomes the PRESERVE constraint the recommended chain is forbidden to break.
- *(Optional)* **Stakes / goal / channel** — where it publishes, who reads it, what it's for. Narrows the PRESERVE list and the dose (X vs. LinkedIn vs. newsletter short; VSL vs. landing vs. cold email).
- *(Optional)* **Known constraints** — words it can't use, claims it can't make, length ceiling. Flagged in the chain so a downstream deepen pass honors them.

---

## Workflow

### Step 1: Frame the diagnosis (vertical, function, where to look first)
Before reading for problems, set the lens. The same sentence is a 0 in a novel and a 2 in a 150-word post — severity is read against the vertical, not in the abstract.

| Frame | The question to answer | What good looks like |
|---|---|---|
| **Vertical** | Which of the five rooms is this playing in? | Named, not assumed. Social / copy / marketing / book / client — each carries a different dose and a different "deficits that matter most" list (`vertical-dosing.md`). |
| **Function to protect** | What is the one thing this draft must not stop doing? | Concrete for *this* piece: "the CTA must stay unmissable," "the hook must keep stopping the scroll," "the spine must carry 4,000 words." The PRESERVE constraint. |
| **Where to look first** | Which deficits does this vertical make most likely? | From `vertical-dosing.md`: social → #2/#6/#5; copy → #2/#4/#3; marketing → #2/#3/#4; book → #1/#7/#3/#8; client → #1/#8/#5. A prior, not a verdict — still score all eight. |

Do not let the prior become the diagnosis. The dosing table tells you where to look first; it does not score the draft for you.

### Step 2: Score all 8 deficits, 0/1/2, with an evidence quote
Score every deficit, in Ordering-Law order (1→8), using the per-deficit detection signals and severity rubric in `depth-deficit-taxonomy.md`. The scale is shared across all eight:

| Score | Label | Meaning |
|---|---|---|
| **0** | Absent | The draft already does this well enough to leave alone. Do NOT route an owner here — touching it risks over-deepening. |
| **1** | Present | At least one detection signal fires, but the draft still functions. A light dose / surgical inject would fix it. |
| **2** | Severe | Multiple signals fire, or one fires so hard the draft fails its job. Full dose, in Ordering-Law sequence. |

For each deficit, run its detection signals from the taxonomy and record three things — **the score, the evidence, and a one-line why**:

| Deficit (Ordering-Law order) | Score it by (taxonomy signal, abbreviated) | Evidence required |
|---|---|---|
| 1 — No architecture | Can you name the spine in one sentence? Are paragraphs freely reorderable? Does the ending pay off the opening? | The reorderable section, or "no spine recoverable" — quote the floating beat. |
| 2 — Hollow / generic | Proper-noun-swap test; abstract stakes; zero anchors. | The could-be-anyone sentence, quoted. |
| 3 — Emotionally unearned | Labeled feeling vs. rendered feeling; melodrama OR flatness. | The asserted-sentiment line ("it was devastating…") or the drained-flat beat, quoted. |
| 4 — No signature voice | Default explainer cadence; banned AI-tells; byline-strip test. | The AI-tell, quoted verbatim ("Here's the thing…", "It's not X. It's Y."). |
| 5 — Over-explained / bloated | The "in other words" restatement; defensive caveats; estimate the % cuttable. | The restated idea, quoted, plus a cuttable-% estimate. |
| 6 — Weak rhythm | Sentence lengths cluster; read-aloud stumbles; soft endings. | The monotone run or the soft terminal, quoted. |
| 7 — Missing telling detail | Adjective/conclusion instead of image; no quotable concrete object. | The told-not-shown line ("she was nervous"), quoted. |
| 8 — No reader trust | Throat-clearing open; confusing leap; fake closure. | The throat-clearing or fake-closure line, quoted. |

**Evidence is mandatory for every score of 1 or 2.** A severity call without a quote from the draft is a hunch, not a diagnosis — and a hunch sends the wrong owner. A 0 needs no quote (nothing is wrong) but may note *why* the draft already clears it. Distinguish #2 (hollow at the level of stake/subject) from #7 (the missing rendered image) — they route to overlapping owners but are different diagnoses.

### Step 3: Name the weakest link(s) — the treatment target
A draft is healthy when no deficit scores 2 and at most one or two score 1. The treatment target is the **1–3 highest-scoring deficits** — the weakest links — never "all eight."

- All 2s are weakest links. If there are more than three 2s, the draft likely has a Deficit 1 (no architecture) problem masquerading as many — re-read for the spine first; downstream deficits often resolve once the center exists.
- If nothing scores above 1, say so plainly: this draft is healthy; recommend a light single-deficit inject at most, or no deepen pass at all. Do not manufacture a target to look thorough — a clean draft that gets "deepened" gets worse.
- Honor the vertical's dose ceiling when naming the target: **social caps at 1–2 deficits**, no matter how many scored above 0. The audit recommends within the dose, never past it.

### Step 4: Recommend the composition chain (owners, order, dose)
Translate the weakest links into a treatment plan — *naming* owners and commands from `routing-map.md`, without loading any of them. This is a prescription, not a procedure.

| Chain element | What to specify | Source |
|---|---|---|
| **Owners** | One owner (real skill path) per confirmed deficit only — never for a 0. | `routing-map.md` Deficit → Owner table |
| **Order** | Sequence the owners by the Ordering Law, NOT by deficit number: architecture → scene/detail → line/rhythm → truth/voice. | `genius.md § 5` / `routing-map.md § Ordering Law` |
| **Commands** | The real `/command` to run for each owner (verified roster only). | `routing-map.md` REAL command column |
| **Dose** | Light/medium/heavy per the vertical, with the PRESERVE constraint stated. | `vertical-dosing.md` Dosing Table |
| **Truth slot** | Name the vertical's `/really-real-*` pass the deepen pass will CALL (social→`/really-real-social`, copy & marketing→`/really-real-marketing`, book→`/really-real-book`, client→`/really-real-client`). Name it; the orchestrator calls it — this audit does not. | `vertical-dosing.md` Truth slot column |
| **Handoff** | Which `/depth-*` orchestrator should execute this chain, and whether a surgical inject or full rewrite is warranted by the scores. | scope match (`genius.md § 11`, item 2) |

The chain is the diagnosis made actionable. It ends here — the audit recommends; the orchestrator (or the writer) executes. No move is applied on this run.

## Content-Type Adaptations
| Vertical | How this workflow adapts (dose / order / truth slot) |
|---|---|
| **Social** | Suspect #2 hollow, #6 rhythm, #5 bloat first; do NOT score #1 harshly — a 150-word post's spine is usually implicit in the hook. Cap the recommended chain at **1–2 deficits, LIGHT dose**; flag that the deepest move is often a CUT. Truth slot: `/really-real-social`. PRESERVE: hook, brevity, scannability, platform shape. |
| **Copy** | Suspect #2 hollow (vague benefit), #4 no voice (sounds like every ad), #3 unearned (sentiment without proof). Recommend MEDIUM dose inside the conversion skeleton. Truth slot: `/really-real-marketing`. PRESERVE: offer logic, CTA, proof, clarity-to-action — flag any deficit whose fix risks blurring the next step. |
| **Marketing** | Suspect #2 could-be-any-brand, #3 manufactured warmth, #4 no voice. Recommend MEDIUM-HEAVY humanity + belief; note Rory Sutherland reframe (`/conspiratorial-reframe-engine`) as the optional belief layer. Truth slot: `/really-real-marketing`. PRESERVE: the belief / positioning / strategic frame. |
| **Book/long-form** | Score #1 architecture FIRST and weight it heaviest — a 2 here outranks every other call. Then #7 detail, #3 unearned, #8 trust. Recommend FULL STACK in strict Ordering-Law sequence. Truth slot: `/really-real-book`. PRESERVE: spine/theme, continuity, earned trust across the arc. |
| **Client/personal** | Suspect #1 argument has no spine, #8 throat-clearing / fake closure, #5 proving the already-trusted. Recommend MEASURED dose with restraint; note Fareed argument architecture (`/high-stakes-argument-architecture`). Truth slot: `/really-real-client`. PRESERVE: argument logic, credibility, the restraint that signals a trusted advisor — flag any manufactured-vulnerability risk. |

## Output Format
This workflow produces a scorecard + recommended chain. **No rewritten prose, and therefore no Depth Receipt** (the Receipt belongs to rewrite/inject workflows only).

```
# Depth Audit: [draft name / first line]
Vertical: [social / copy / marketing / book / client] · Function to protect: [the one thing it must keep doing]

## SCORECARD (0 = absent · 1 = present · 2 = severe)
1. No architecture ......... [0/1/2] — [why, one line] · Evidence: "[quote from draft]"
2. Hollow / generic ........ [0/1/2] — [why] · Evidence: "[quote]"
3. Emotionally unearned .... [0/1/2] — [why] · Evidence: "[quote]"
4. No signature voice ...... [0/1/2] — [why] · Evidence: "[quote]"
5. Over-explained / bloated  [0/1/2] — [why; ~X% cuttable] · Evidence: "[quote]"
6. Weak rhythm ............. [0/1/2] — [why] · Evidence: "[quote]"
7. Missing telling detail .. [0/1/2] — [why] · Evidence: "[quote]"
8. No reader trust ......... [0/1/2] — [why] · Evidence: "[quote]"
(Evidence mandatory for every 1 and 2; a 0 may note why the draft already clears it.)

## WEAKEST LINK(S) — treatment target
[The 1–3 highest-scoring deficits, in Ordering-Law order. Or: "Draft is healthy — no deficit above [N]; no deepen pass recommended" / "light single inject at most."]

## RECOMMENDED COMPOSITION CHAIN
Order (Ordering Law, not deficit number):
  1. [Deficit #] → [Owner] (`skills/...`) → run [/command] — [dose note]
  2. [Deficit #] → [Owner] (`skills/...`) → run [/command] — [dose note]
  ...
Truth slot (CALLED by the deepen pass, not by this audit): [/really-real-<vertical>]
Dose: [LIGHT / MEDIUM / HEAVY] — [why this dose for this vertical]
PRESERVE (the chain must not break): [function to protect]
Handoff: [/depth-<vertical> orchestrator] · Scope: [surgical inject / full rewrite — and why]
Constraints to honor downstream: [any known word/claim/length limits, or "none stated"]

## NOTE
Diagnosis only — prose unchanged. No owner was loaded; no move was applied. Hand this chain to the named /depth-* orchestrator to execute.
```

## Quality Gate
> **🛡️ Anti-Pattern Check**: review output against `genius.md § 9 Anti-Patterns` and `genius.md § 10 Anti-Duplication Contract`. Flag and fix any violation before delivering — no lengthening-as-deepening, no expert name-drops in prose (N/A here — there is no prose), no function sacrificed, no manufactured sentiment, no craft re-taught.
- **Zero prose changed.** Not one sentence of the draft is rewritten, injected, or "lightly polished." If any output line is altered draft text, this stopped being an audit — delete it. Diagnosis only.
- **No owner loaded, no move applied.** Owners and commands are *named* from `routing-map.md`; none were loaded to treat. A loaded owner on a diagnosis run is scope creep — rebuild as a pure prescription.
- **Every 1 and 2 carries a quote from the draft.** A severity call without evidence is a hunch and sends the wrong owner. Return and quote it, or lower the score to 0.
- **Ordering Law respected in the chain.** The recommended sequence runs architecture → scene/detail → line/rhythm → truth/voice — by the law, not by deficit number. A chain that puts rhythm before a recovered spine is wrong; re-sequence.
- **Only confirmed deficits routed.** No owner is recommended for a deficit scored 0. The target is the 1–3 weakest links, capped by the vertical's dose (social: 1–2). A "comprehensive" eight-owner chain is a failure, not thoroughness — return and cut to the weakest links.
- **No Depth Receipt.** This workflow produces a scorecard + chain, not deepened prose; the Receipt block belongs only to rewrite/inject workflows. If a Receipt appears here, remove it.

## Common Pitfalls
- **Diagnosis drifts into treatment.** You scored, then "couldn't help" rewriting the worst sentence. Recovery: stop at the prescription; the whole value of this gate is that it does not touch the prose. Hand the chain to the `/depth-*` orchestrator and let it treat.
- **Scores with no evidence.** You marked Deficit 4 a "2" but quoted nothing — the writer can't see it and a downstream pass can't trust it. Recovery: for every 1 and 2, paste the exact offending line from the draft; if you can't find one, the score is wrong.
- **The prior became the verdict.** You let `vertical-dosing.md`'s "deficits that matter most" decide the scores instead of reading the actual draft. Recovery: the dosing table sets where to *look first*, never the score — re-run all eight against the real text.
- **Over-diagnosis to look thorough.** You named five weakest links on a healthy draft, prescribing an eight-owner chain that would bury a clean piece in technique. Recovery: cap at the 1–3 highest scores; if nothing tops a 1, say "healthy — no deepen pass" and stop. A clean draft deepened gets worse.
- **Chain ordered by deficit number.** You listed owners 1→8 instead of by the Ordering Law, so voice (4) landed before a recovered spine (1). Recovery: re-sequence by architecture → scene → line/rhythm → truth/voice; the deficit numbers are an index, not an apply order.
- **Wrong vertical, wrong dose.** You audited converting copy as if it were a Substack essay and recommended a heavy full-stack chain that would bury the CTA. Recovery: re-confirm the vertical and the function to protect before scoring; the dose and the "look first" list are both set by the vertical.
