# Gelb Architecture Design — Checkpoint 2

## Skill Domain

```
Domain: cinematic-documentary
Slash Prefix: gelb-
Agent Directory: agents/david-gelb/
Skill Directory: skills/cinematic-documentary/
Workflow Count: 13
Tier: Deep (Mastery)
```

---

## Workflow Architecture

### Tier 1 — Foundation (Character + Hook + Arc)

| # | Workflow | Slash | Input | Output | Patterns Used |
|---|---------|-------|-------|--------|---------------|
| 1 | **Character-First Inversion** | `/gelb-character` | Topic or subject | Character-centered narrative brief: who, origin, want vs. need, emotional stakes | 1, 2, 6 |
| 2 | **Origin Story Excavation** | `/gelb-origin` | Subject name + raw background info | Formative moment identification, motivation map, Spider-Man-grade origin architecture | 2, 6 |
| 3 | **Bond Cold Open Design** | `/gelb-hook` | Draft or topic | 3 cold open options (action, mystery, contradiction) with post-hook transition blueprint | 3 |
| 4 | **Want vs. Need Mapper** | `/gelb-arc` | Character brief or draft | Want/need separation matrix, arc roadmap showing surface pursuit → deep revelation | 5, 6, 8 |

### Tier 2 — Structure (Narrative Engineering)

| # | Workflow | Slash | Input | Output | Patterns Used |
|---|---------|-------|-------|--------|---------------|
| 5 | **False Victory Architect** | `/gelb-false-victory` | Draft or outline | Midpoint false victory placement, complication design, post-turn pacing plan | 5, 6 |
| 6 | **Scene Audit Protocol** | `/gelb-scene-audit` | Any draft with sections | Section-by-section change analysis: what enters, what exits, cut/rebuild prescriptions | 8, 9, 10 |
| 7 | **Cinematic Pacing Engine** | `/gelb-pacing` | Complete draft | Momentum map, transition audit (cut-to vs. cut-away), cold-start diagnosis, overcorrection calibration | 10, 12, 15 |

### Tier 3 — Craft (Editing + Coherence)

| # | Workflow | Slash | Input | Output | Patterns Used |
|---|---------|-------|-------|--------|---------------|
| 8 | **Emotion Over Information Pass** | `/gelb-emotion` | Any content draft | Information → emotion audit: flagged explanatory passages, prescribed emotional replacements, "egg sushi" conversions | 4, 9 |
| 9 | **Fewest Words Rewrite** | `/gelb-compress` | Any draft | Compression pass: every sentence tested for earned place, redundancy flagged, economy score | 9 |
| 10 | **Gesamtkunstwerk Audit** | `/gelb-coherence` | Finished piece or brand touchpoints | Element-by-element coherence check: does every element (tone, imagery, structure, details) echo the same DNA? | 14 |

### Tier 4 — Process (Creative Lifecycle)

| # | Workflow | Slash | Input | Output | Patterns Used |
|---|---------|-------|-------|--------|---------------|
| 11 | **Assembly Despair Navigator** | `/gelb-despair` | Current creative state + draft | Phase diagnosis (dailies → despair → overcorrection → balance), next-action prescription, emotional calibration | 12, 15 |
| 12 | **Doctor-Patient Feedback Processor** | `/gelb-feedback` | Raw feedback (client notes, peer review, metrics) | Symptom extraction report: symptoms isolated, prescriptions discarded, taste-processed revision plan | 13 |
| 13 | **Playlist Prelude** | `/gelb-tone` | Project brief or concept | Emotional reference palette: 3-5 reference works (across media), tone vocabulary, collaborator alignment brief | 11 |

---

## Cross-Expert Stacking Chains

| Chain | Workflow(s) | What It Produces |
|-------|------------|-----------------|
| **Gelb → Roth** | `/gelb-character` → `/roth-copy` | Character-first narrative architecture → cinematic prose deployment |
| **Gelb → Wright** | `/gelb-origin` → `/wright-detail` | Origin story excavation → surgical detail-as-revelation writing |
| **Gelb → Connelly** | `/gelb-scene-audit` → `/connelly-momentum` | Scene-level change audit → momentum engineering at sentence level |
| **Gelb → Kallaway** | `/gelb-hook` → `/vicious-hook` | Bond cold open design → platform-native hook engineering |
| **Gelb → Pressfield** | `/gelb-despair` → `/resistance` | Assembly despair navigation → Turning Pro resistance protocol |
| **Gelb → Lamott** | `/gelb-despair` → craft coaching | Creative despair processing through tender pedagogy |
| **Gelb → Oren** | `/gelb-coherence` → `/taste-cev` | Gesamtkunstwerk coherence audit → CEV taste evaluation |
| **Gelb → Junyuh** | `/gelb-character` → `/junyuh-origins` | Character-first inversion → Problem/Pursuit/Payoff origin mining |
| **Gelb → Dai Media** | `/gelb-arc` → consumer posture | Want vs. need separation → radical individual consumer modeling |
| **Gelb → Sutherland** | `/gelb-emotion` → perception engineering | Emotion-over-information → perception reframing for behavioral impact |

---

## Workflow Detail Specifications

### `/gelb-character` — Character-First Inversion
**Purpose**: Transform any topic-centered content idea into a character-driven narrative.
**Trigger**: User has a topic but no protagonist; content reads like a report, not a story.
**Input**: Topic, subject name (optional), raw material / interview notes.
**Process**:
1. Identify the human being whose journey through this topic creates emotional stakes
2. Map their relationship to the topic: Why this person? Why now? What's at risk?
3. Apply Origin Story as Master Key (Pattern 2): find the formative moment
4. Apply Want vs. Need Separation (Pattern 6): map surface desire vs. deep truth
5. Output character brief with emotional architecture

**Output**: Character narrative brief — protagonist profile, origin moment, want/need matrix, emotional stakes, 3 opening angles.

### `/gelb-origin` — Origin Story Excavation
**Purpose**: Find and structure the "Spider-Man moment" — the formative event that explains everything.
**Trigger**: User needs to tell someone's story but has only chronological biography.
**Input**: Subject's background info (interview, bio, conversation notes).
**Process**:
1. Scan for formative moments (wound, revelation, pivotal choice)
2. Apply the Spider-Man Test: Does this moment explain every subsequent decision?
3. If no single moment passes the test, identify the *pattern* across 2-3 moments
4. Structure the origin as a deployable narrative unit (not backstory dump)
5. Map how the origin echoes in present-day behavior

**Output**: Origin story architecture — the moment, the lesson installed, the behavioral pattern it predicts, deployment recommendations (where to reveal it in the narrative).

### `/gelb-hook` — Bond Cold Open Design
**Purpose**: Engineer the pre-credits action sequence for any content piece.
**Trigger**: Content opens with context/setup instead of grabbing the audience.
**Input**: Draft or topic + target audience.
**Process**:
1. Scan for the most vivid, high-stakes, or intriguing moment anywhere in the material
2. Design 3 cold open options: Action (in medias res), Mystery (unanswered question), Contradiction (expectation violation)
3. For each, design the "post-credits" transition — how to pull back to context after the hook
4. Score each against the Bond Test: Would you stay if this were the opening scene?

**Output**: 3 cold open scripts with transition bridges. Ranked by grabbing power + thematic relevance.

### `/gelb-false-victory` — False Victory Architect
**Purpose**: Plant the midpoint comfort and design the complication that shatters it.
**Trigger**: Content feels flat in the middle; no narrative turn; predictable trajectory.
**Input**: Draft or outline with identified midpoint.
**Process**:
1. Identify where the surface-level goal appears achieved
2. Design the audience comfort moment — "everything is going to be fine"
3. Identify the deeper goal the character doesn't yet know about
4. Design the complication that reveals the gap between surface and deep
5. Map post-turn pacing: how quickly does the new reality set in?

**Output**: False victory architecture — comfort moment, complication trigger, post-turn emotional arc, revised outline.

### `/gelb-scene-audit` — Scene Audit Protocol
**Purpose**: Enforce scene-level change in every section of content.
**Trigger**: Draft feels bloated or flat; sections feel like they exist because they "should."
**Input**: Any segmented draft.
**Process**:
1. For each section: What does the reader/character believe *entering*?
2. What do they believe *leaving*?
3. If same → FAIL. Prescribe: cut or rebuild with a change
4. Check transitions: does each section cut *to* the next (momentum) or cut *away* (cold start)?
5. Generate section map with PASS/FAIL/REBUILD verdicts

**Output**: Section audit report — change matrix, cut recommendations, rebuild prescriptions, momentum map.

### `/gelb-emotion` — Emotion Over Information Pass
**Purpose**: Convert explanatory passages into emotional demonstrations.
**Trigger**: Content reads like a lecture or explainer; audience learns but doesn't *feel*.
**Input**: Any draft.
**Process**:
1. Flag every passage that delivers information without emotional context
2. For each: identify the "egg sushi" conversion — what's the human moment that makes this information unforgettable?
3. Apply the Cinema Test: "Would this scene work as a movie moment?"
4. Rewrite flagged passages with emotional wrappers
5. Score final draft: Information-Emotion Ratio (target: 30/70 or lower)

**Output**: Emotion audit with rewritten passages. Information-Emotion ratio score. Before/after comparisons.

### `/gelb-despair` — Assembly Despair Navigator
**Purpose**: Diagnose where a creator is in the creative lifecycle and prescribe the correct next action.
**Trigger**: Creator feels "this is terrible" about a work-in-progress; wants to abandon or restart.
**Input**: Current emotional state + draft/project status.
**Process**:
1. Diagnose phase: Dailies Excitement → Assembly Despair → Overcorrection → Balance
2. If Despair: normalize, prescribe "don't quit, don't over-polish"
3. If Overcorrection: prescribe restoration of cut material
4. If Balance: prescribe feedback round (Assembly Watch technique)
5. Provide the Pressfield cross-chain option if resistance is the root cause

**Output**: Phase diagnosis, emotional calibration, specific next action, timeline expectation.

### `/gelb-feedback` — Doctor-Patient Feedback Processor
**Purpose**: Process raw feedback by extracting symptoms and discarding prescriptions.
**Trigger**: User has received client/peer/audience feedback and doesn't know what to do with it.
**Input**: Raw feedback (copy-pasted notes, email, comment threads, metrics).
**Process**:
1. Separate every piece of feedback into Symptom (what isn't working) vs. Prescription (what they think you should do)
2. Discard all prescriptions
3. Cluster symptoms by type: confusion, boredom, disbelief, emotional disconnect
4. For each symptom cluster, generate taste-processed solutions (not the audience's solutions)
5. Prioritize by impact: which symptoms affect the most critical narrative moments?

**Output**: Symptom extraction report — clustered symptoms, discarded prescriptions, taste-processed revision plan, priority ranking.

---

## Build Checklist

### Phase 5: Genius File
- [ ] `skills/cinematic-documentary/genius.md` — All 14 genius patterns + 8 hidden knowledge + rubric
- [ ] Organized by methodology level (Foundation → Structure → Craft → Process)
- [ ] Each pattern: behavior + deployment context + anti-pattern lock

### Phase 6: SKILL.md
- [ ] `skills/cinematic-documentary/SKILL.md` — Expert identity, tier card, workflow index
- [ ] Cross-expert stacking chains documented
- [ ] Quality rubric embedded

### Phase 7: Workflows
- [ ] 13 workflow files in `skills/cinematic-documentary/workflows/`
- [ ] Each workflow: trigger, input, process, output, patterns used, anti-patterns
- [ ] Slash commands registered in `.agent/workflows/`

### Phase 8: Integration
- [ ] Agent directory: `agents/david-gelb/AGENT.md`
- [ ] Expert router registration
- [ ] Workflow router registration
- [ ] Verification test (Checkpoint 3)

---

## Approval Request

> **Checkpoint 2 — Architecture Review**
>
> 13 workflows across 4 tiers. 10 cross-expert stacking chains.
> Approve to proceed to Phase 5-8 (Build)?
