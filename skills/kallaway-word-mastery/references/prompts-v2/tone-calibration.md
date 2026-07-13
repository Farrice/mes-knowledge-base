---
name: "Kallaway — Tone Calibration"
source_prompt: born-v2
skill: kallaway-word-mastery
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working the Tone Calibration layer of Kallaway's Word Mastery system — precision-targeted register shifting with word-level accountability for every choice. This sits third in the Articulation Stack (after Anxiety Resolution and Rhythm Architecture), and it's not a vibe pass — it's a diagnostic of the current register against a defined linguistic toolkit for the target register, with annotated reasoning for why each significant word was chosen over its alternatives.

## Input Required

1. **[SOURCE_CONTENT]** — the text to rewrite
2. **[TARGET_TONE]** — one of: casual, professional, entertaining, comedic, authoritative (or a stated blend, e.g. "casual-authoritative")
3. **[CONTEXT]** — where this will be published and who the audience is

## Execution Protocol

### Step 1 — Tone Diagnosis
Analyze the source content's current register. Report the register, 3-5 specific word choices or sentence structures that signal it, a formality level (1-10), an authority signal (1-10), a likability signal (1-10), and the specific gap to the target register.

### Step 2 — Register Shift Map
Apply the linguistic toolkit for the target register:

| Register | Word Choices | Sentence Structure | Rhetorical Devices |
|---|---|---|---|
| **Casual** | Contractions (can't, gonna), slang, colloquial | Short, simple, direct, active voice, fragments allowed | Exclamations, ellipses, bullet points |
| **Professional** | Formal vocabulary, no personal pronouns | Complex with subordinate clauses, passive voice permitted | Semicolons, third-person, measured pacing |
| **Entertaining** | Everyday words, first-person, contractions | Varied lengths, active voice, story-driven | Italics/bold for emphasis, rhetorical questions |
| **Comedic** | Exaggerated slang, playful substitutions, idioms | Short, punchy, fragments for rhythm | Hyperbole, unexpected juxtapositions, rule-of-three |
| **Authoritative** | Precise jargon, objective terms, power words | Declarative, third-person, downward inflection | Colons for lists, confident assertions, data anchors |

### Step 3 — Word-Level Rewrite
Rewrite the full content in the target register. For every significant word choice, annotate inline (or in the annotation layer) why that specific word was chosen over the plausible alternatives.

### Step 4 — Code-Switch Injection (optional)
If the target tone benefits from texture, inject 1-2 register switches within the piece — e.g., open casual → teach authoritative → close casual, or narrate entertaining → prove authoritative → resolve casual. The switch itself creates energy; a monotone register is forgettable after ~200 words.

### Step 5 — Formality-Trust Calibration
Apply the Likable Expert principle regardless of the primary target register: informal sentence structure (short, direct) carrying formal-level proof (specific data, precise terminology). Formal registers build trust in professional contexts but risk alienating casual audiences; informal registers boost likability but risk perceived authority. The Kallaway solution stacks both — sound like a friend who happens to be the world's leading expert.

## Output Contract

- **Rewritten content**: full piece in the target register
- **Tone scorecard**: before/after formality, authority signal, likability signal
- **Annotation layer**: 5-10 key word-level choices explained (what was chosen, what alternative was rejected, why)
- **Code-switch map**: where register shifts occur, if applied (state "none applied" if not used)

## Output Skeleton

```
CURRENT TONE ANALYSIS
Register: [detected register]
Evidence: [3-5 word choices/structures signaling it]
Formality Level: [1-10] | Authority Signal: [1-10] | Likability Signal: [1-10]
Gap to Target: [what specifically needs to change]

REWRITTEN CONTENT
[full piece in target register]

TONE SCORECARD
Formality: [before] → [after]
Authority Signal: [before] → [after]
Likability Signal: [before] → [after]

ANNOTATION LAYER (5-10 choices)
- "[chosen word/phrase]" over "[rejected alternative]" — [why]

CODE-SWITCH MAP
[where switches occur and what type, or "none applied"]
```

## Quality Gate
- [ ] Every sentence in the rewrite is actually consistent with the target register's toolkit (not just the opening lines)?
- [ ] A reader would identify the tone without being told?
- [ ] Original meaning and content value preserved through the register shift?
- [ ] If code-switching was applied, transitions are smooth rather than jarring?
- [ ] Annotations explain genuine word-choice reasoning, not generic justification?

## Creative Latitude

The register toolkit is a floor vocabulary, not a script — within "authoritative," for instance, there is enormous range between clinical and commanding, and the model should find the specific register-within-the-register that fits this writer and this content rather than defaulting to the blandest version of the target tone. The formality-trust blend (informal structure + formal proof) is the single highest-leverage move available and should be pushed hard even when not explicitly requested, because it's what separates competent tone-matching from writing that actually sounds like someone worth listening to.

## Deploy When

Repurposing content across platforms that require different registers (LinkedIn professional → Twitter casual); client work where the brief specifies a tone not naturally being written in; AI-generated content that came out in the wrong register; content that "doesn't sound right" but the reason can't be articulated.
