# Skill Architecture — Chase Hughes Context Engineering + The Context Engineering Operating System

## Recommendation: TWO skills, clearly separated

This extraction is too large and too dual-purpose for one skill. Build:

**A. `skills/chase-hughes-context-engineering/`** — the *expert* skill. Hughes's full Behavior-Suite/brainwashing/interrogation/reading layer, faithful to him, atom-or-system depending on workflow. This is the source of truth for the mechanics.

**B. `skills/context-engineering-os/`** — the *operating-layer* skill-system. The owner's standalone "Context Engineering Operating System." It is expert-agnostic in surface (it's a *discipline*, not a persona) but built ON Hughes's PCP spine. It orchestrates persona/workflow files in sequence (the Architect → Force-Mapper → Conditions Builder → Defense/Ethics Auditor → Followability Engineer) and outputs a context-design spec. Runs standalone OR as a front-end to The Chain.

Do NOT expand the existing `chase-hughes-conversational-influence/` skill — it is honestly scoped to one source and 5 patterns. Cross-link it instead. The three skills form a stack: conversational-influence (line-level moves) ⊂ context-engineering (the full Hughes mechanics) → context-engineering-os (the deployable discipline).

> "Sub-agents" below = expert-persona **workflow files** invoked in sequence (Tier 1.5/Tier 3 context isolation), never `.claude/agents/` files. Per the always-on rule, this system never uses Claude Code subagents.

---

## A. `skills/chase-hughes-context-engineering/`

```
skills/chase-hughes-context-engineering/
├── SKILL.md                       # scope, honest-scope note, workflow table, stacking guide
├── genius.md                      # the savant layer (below)
├── references/
│   ├── pcp-and-upstream.md        # PCP + engineer-conditions-not-outcomes, full quotes
│   ├── fear-fractionation.md      # FEAR, fractionation (GABA/theta), division, algorithm bidirectionality
│   ├── followability.md           # 5 trust factors, micro-hesitation, impression test, Truth Plane
│   ├── interrogation.md           # SMRP+AQ, four walls, bait question, punishment question
│   ├── behavior-suite.md          # change-cluster-context, blink/lip/tongue/tense/artery/COPE/blading
│   ├── emotional-substrate.md     # emotional debt, decorator crab, full safe, never-being-seen
│   └── pressure-and-hypnosis.md   # pressure mechanics, experience-prerequisite law, negative-first
└── workflows/                     # see workflow table (Hughes-prefixed)
```

### genius.md outline (Tier 2 load)
- **The one move:** break prediction / restore prediction; engineer conditions, not outcomes.
- **The 13 genius patterns** (from the report) as executable behaviors with success metrics.
- **The dual-use ethic** stated as a hard rule: every mechanic taught with its defense + ethical deployment; intent is the only difference between control and help.
- **The savant rubric** (8 criteria, 4/7/10) + the veto (offense without defense = fail).
- **The voice:** plain, low-grade-level, picture-painting, profanity for emphasis, "as far as we know," names his own susceptibility. Tells stories (chocolate milk, the pub, Manson/Trejo) because the story IS the memory implant.
- **Hot-context note:** PCP and the upstream question are internalizable — don't re-read references for known moves.

---

## B. `skills/context-engineering-os/` (the Operating Layer — a Skill System)

```
skills/context-engineering-os/
├── SKILL.md                       # the OS spine, input→output contract, standalone vs Chain modes
├── genius.md                      # the discipline's philosophy + ethics gate spec
├── references/
│   ├── pcp-spine.md               # the upstream engine (points back to Hughes skill)
│   ├── force-library.md           # FEAR/fractionation/division/algorithm — forces already acting on any audience
│   ├── ethics-defense-gate.md     # the mandatory gate: dual-use check, "would I defend this if surfaced?"
│   └── spec-template.md           # the Context-Design Spec output format
└── workflows/                     # see workflow table (ce-prefixed) — the persona sequence
```

### How it runs
- **Standalone:** `/ce-design "<desired end-state>"` runs the full persona sequence (Architect → Force-Mapper → Conditions Builder → Defense/Ethics Auditor → Followability Engineer) and emits one Context-Design Spec. No Chain finalize needed for a pure spec; finalize fires if it produces deliverable copy/content.
- **Integrated into The Chain:** slots at **Step 3.5 / Step 4** as a context-design front-end. After routing (Step 3) and before/with expert loading (Step 4), `/ce-design` produces the conditions spec; the chosen production expert (Luke Iha copy, Lara Acosta LinkedIn, etc.) then writes INTO that spec. Step 5.5 verification and Step 6 finalize run normally. The Defense/Ethics Auditor persona maps to the existing `directives/quality_assurance.md` + the dual-use veto.

---

## Workflow Table (3 tiers, 13 workflows)

### Tier 1 — Foundation (learn/deploy the core moves)
| Workflow | Slash | Skill | Description |
|---|---|---|---|
| Upstream Engine | `/hughes-upstream` | A | Ask "what's upstream of the thing I want?" + "what context makes it automatic?"; produce the condition chain. The planning verb for everything. |
| PCP Designer | `/hughes-pcp` | A | Design the Perception→Context→Permission drift for a target behavior; name the category word that rewrites permission. |
| Followability Engineer | `/hughes-followability` | A | Build genuine followability: kill micro-hesitations, drop to low grade level, paint pictures, lead with gratitude; win the impression test. |
| CE Design (orchestrator) | `/ce-design` | B | The OS front door — runs the full persona sequence on a desired end-state, outputs a Context-Design Spec. |

### Tier 2 — Practitioner (deploy specific mechanics)
| Workflow | Slash | Skill | Description |
|---|---|---|---|
| Conditions Builder | `/ce-conditions` | B | Turn the upstream condition chain into concrete build steps (funnel touchpoints, content sequence, onboarding, environment design). |
| Force-Mapper | `/ce-force-map` | B | Name the FEAR/fractionation/division/algorithm forces ALREADY acting on the target audience before you design — so you're not fighting an invisible current. |
| Contagious Confidence | `/hughes-resonance` | A | Set your own state first (awareness forward, no hierarchy); install the two-element confidence cause so it transmits. For on-camera/pitch/leadership. |
| Honesty Protocol (SMRP-benevolent) | `/hughes-honesty` | A | Dissolve the four resistance walls (socialize-minimize-rationalize-project) to help someone name a hidden truth/objection. Ethical confession engine. |
| Behavioral Read | `/hughes-read` | A | Change-cluster-context read of a person/transcript/video: baseline, deviations, blink/lip/tongue/tense/need-asymmetry, rewind to trigger. Likelihood only. |

### Tier 3 — Stacking / Defense (composite + inoculation)
| Workflow | Slash | Skill | Description |
|---|---|---|---|
| Defense / Ethics Auditor | `/ce-defense-audit` | B | The mandatory gate. For any context design: detect what's being run, is it dual-use-defensible, would I defend it if surfaced? Also a standalone "is this being run on me?" inoculation pass. |
| Manipulation Detector | `/hughes-detect` | A | Defensive scan of a feed/news/pitch/relationship: FEAR loop, prepackaged enemy, alternative-question trap, fractionation, symptom-confidence. Names it + the resistance move. |
| Source-Code Diagnostic | `/hughes-source-code` | A | The 8-year-old / emotional-debt root-cause pass for self or a coaching client; reframes a stuck adult pattern as an outdated childhood app. |
| Full Context-Engineering Build | `/ce-build` | B | End-to-end composite: upstream → force-map → PCP → conditions → followability → defense/ethics gate → hand to production expert. The supercomputer-grade run. |

---

## Notes for the architecture checkpoint
- **Routing:** add a Mandatory-Routing binding — "engineer conditions / context design / make the behavior automatic / upstream of the outcome" → `/ce-design` (never a single-tactic copy workflow alone). Mirror in `routing_enforcer.py BINDINGS`.
- **Recall grounding:** all these are grounding-relevant domains (persuasion, copy, brand, comms) — Tier 1.5a fires automatically.
- **Stacking with existing Hughes skill:** `/ce-design` produces the macro-context; `/hughes-feel-clever` (existing) is the line-level engineered-self-conclusion move INSIDE that context. Document the seam in both SKILL.md files.