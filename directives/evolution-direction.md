# Evolution Direction

> **Analog**: Karpathy's `program.md` — the natural language instruction set that guides the self-improvement loop.
> **Purpose**: Single source of truth for what to evolve, why, and when to stop.
> **Updated**: After every evolution cycle. Read before every `/skill-evolution` run.
> **Created**: 2026-04-06

---

## Current Evolution Priorities

### Priority 1: Activate Phase 2 (First Evolution Cycle)

**Target**: Pick the lowest-performing skill from Performance Log (76+ entries available).

**Why**: Phase 2 infrastructure has been built since 2026-03-10 but has never been activated. The threshold (20 entries) was met months ago. Running the first cycle proves the loop works end-to-end.

**Approach**:
1. Run `python execution/skill_benchmark.py benchmark <skill-name>` on 3-5 candidate skills
2. Select the one with the clearest improvement target (lowest dimension score)
3. Write hypothesis, generate variant, test, keep/discard
4. Log result + git commit if KEPT

**Success criteria**: One full evolution cycle completed, result logged, variant either KEPT or DISCARDED with a documented lesson.

### Priority 2: Ground Truth Calibration

**Target**: Validate that our quality scores actually reflect expert-level quality.

**Why**: Without calibrating against real expert output, we could be "evolving" toward AI-pleasing patterns that don't match real expertise. The ground truth system exists but hasn't been used systematically.

**Approach**:
1. Run `python execution/ground_truth.py gap-report` to see current coverage
2. Add 2-3 expert samples to the most-used domains (if missing)
3. Run blind comparisons on skills that just went through evolution
4. If scores diverge >2 points from expert baseline, recalibrate

### Priority 3: Cross-Pollination Activation

**Target**: After first KEPT variant, check if improvement transfers to related skills.

**Why**: Phase 3 has 0 activations. One successful transfer would prove the pattern family mapping works.

**Blocked by**: Priority 1 (needs at least one KEPT evolution result).

---

## Constraints (Do Not Cross)

1. **Never modify genius.md content** — expert frameworks are the bedrock. Only workflow files and Evolution Log sections change.
2. **Never test more than one hypothesis per cycle** — isolated variables prevent false positives.
3. **Keep the human in the loop** — present comparisons, wait for approval before replacing workflows.
4. **Time-box all benchmark runs** — 10 minutes max per task. If it's not producing in 10 minutes, the approach is wrong.
5. **Binary decisions during evolution** — composite >= 7 = KEEP, < 7 = DISCARD. No "marginal" retries.
6. **Git-commit every KEPT variant** — auditable evolution history, always.

---

## Stopping Criteria

**Pause evolution and reassess when**:
- 3 consecutive DISCARD results on the same skill (hypothesis space may be exhausted for now)
- A KEPT variant causes downstream regression in a different skill
- Quality scores diverge >2 points from Ground Truth blind comparison results
- Revenue Tracker shows KEPT variants producing lower business outcomes than originals

---

## Evolution History

> Updated after every cycle. Shows the full trail of what was tried and what happened.

| Date | Skill | Hypothesis | Result | Score Delta | Notes |
|------|-------|-----------|--------|-------------|-------|
| 2026-04-09 | lara-acosta-linkedin-mastery | Add Phase 4b Proof Layer Audit + adversarial quality gate checks | KEPT | 7.8 → 8.3 (+0.5) | First evolution cycle. Targets adversarial resilience. |
| 2026-04-09 | kallaway-word-mastery | Add Emotional Stakes Architecture to Grip & Tension Engine | KEPT | 8.3 (tie, qualitative win) | 5 stakes mechanics (Personal Mirror, Cost Made Concrete, Belief Collision, Near-Miss Story, Identity Bridge). Reader becomes protagonist. |
| 2026-04-09 | nicolas-cole-sentence-craft | Add Sentence Demand Architecture to Terminal Power & Rhythm Engineering | KEPT | 8.3 (tie, 43% vs 32% compression) | 5 demand mechanics (Incomplete Transfer, Expectation Violation, Specificity Spike, Reversal Bridge, Compression Cliffhanger) + Energy Crescendo Mapping. |
| 2026-04-09 | harry-dry-copywriting | Add Moment-of-Encounter Simulation to Landing Page Blueprint | KEPT | 8.2→8.5 (qualitative) | Reader-state reconstruction produces headlines that name private frustrations, not category benefits. Conflict Architecture 7→9. |
| 2026-04-09 | luke-iha-vicious-hooks | Add Identity Infiltration Architecture to Vicious Hook Writer | KEPT | 6.67→8.0 (+1.33) | 5 IM mechanics for naming private behaviors, unsaid thoughts, public/private gaps. Biggest adversarial jump (+2). |
| 2026-04-09 | lara-acosta-content-system | Add Signal-to-Pivot Feedback Loop to Authority Strategy Blueprint | KEPT | 31→39/50 (+25.8%) | Signal Classification, Adaptation Moves, One-Variable Rule. Turns static plans into living systems. |
| 2026-04-09 | oren-taste-development | Add Decision Pressure Architecture to Taste-Led Brand Authority | KEPT | 6.3→8.3 (+2.0) | Tradeoff matrix, calibration protocol, pressure inoculation scripts, taste-to-revenue bridge. Largest delta. |
| 2026-04-09 | chris-cimorelli-copywriting | Add Consumer Posture Translation Layer to Front-End Promotion | KEPT | 7.0→8.3 (+1.3) | Phase 0 builds linguistic palette from Dai Media consumer posture. Identity Resonance 5→9. Cross-pollination with dai-media skill. |
| 2026-04-09 | nicolas-cole-newsletter-flywheel | Add Serial Investment Architecture to Newsletter Flywheel | KEPT | 7.0→8.3 (+1.3) | 5 mechanics (Conceptual Deposit, Belief Escalation, Identity Ratchet, Callback Yield, Incomplete Transfer). Each edition compounds reader investment. Powers Parallax. |
| 2026-04-09 | bond-halbert-copywriting | Add Scroll Momentum Architecture to Velocity-Optimized Sales Copy | KEPT | 7.0→8.3 (+1.3) | Fold-level velocity-locks (Incomplete Transfer, Micro-Action, Pattern Break, Anxiety Anchor, Section-Entry Independence). DR power preserved, digital survival added. Adversarial +2. |
| 2026-04-09 | steven-pressfield-narrative-mastery | Add Narrative Debt Architecture to Sales Narrative Engine | KEPT | 7.3→9.0 (+1.7) | Phase 0 debt chain: Tension Deposits, Inheritance Chain, Partial Resolution Hooks, Accumulation Marker, Compound Payoff. Transforms sequential phases into compounding narrative. Each sentence makes ending more inevitable. |
| 2026-04-09 | donald-miller-storybrand | Add Specificity Excavation Layer to BrandScript Generator | KEPT | 6.6→9.0 (+2.4) | Step 0 reconstructs customer's private world (vocabulary, friction scenes, identity gap, competitor jealousy) before SB7 slot-filling. Villain specificity +4. Largest delta yet. |
| 2026-04-09 | rory-sutherland-marketing | Add Reframe Stress Test to Psychological Brand Strategy Blueprint | KEPT | 6.3→8.3 (+2.0) | 3 behavioral prediction filters (Identity Congruence, Comparison Frame Prediction, Implementation Clarity Gate). Bridges gap between clever reframe and deployable positioning. Adversarial +3. |
| 2026-04-09 | david-mcraney-belief-change | Add Keystone Belief Triangulation to Belief Dissolution Copywriting | KEPT | 7.0→8.7 (+1.7) | Maps belief dependency graph, identifies structural keystone, designs cascade sequence. 1 reframe dissolves 5 beliefs. Inverts HK7 (load-bearing beliefs) from defensive to offensive. |
| 2026-04-09 | erica-mallet-brand-magnetism | Add Magnetism Pulse Diagnostics to Brand Magnetism Bible | KEPT | 7.0→8.3 (+1.3) | Phase 6: Leading indicators (language matching, unsolicited forwarding, identity declaration), 5 decay signals, monthly pulse check, corrective actions. Closes "how do you know it's working?" gap. Adversarial +2. |
| 2026-04-09 | monk-ai-offer-architecture | Add Decision Architecture Layer to Offer Ecosystem Design | KEPT | 7.0→8.3 (+1.3) | 3 DA mechanics (Asymmetric Dominance Positioning, Pre-Regret Inoculation, Rational Self-Evidence Engineering). Buyers construct their own logical argument for the target tier. Adversarial +2. |
| 2026-04-09 | dan-koe-multipassionate-mastery | Add Convergence Inevitability Architecture to Personal Monopoly Foundation | KEPT | 6.0→8.3 (+2.3) | Phase 2.5: Dependency Mapping, Removal Test, Origin Story Convergence, Audience Translation Formula. Transforms "I have many interests" from declaration to structural proof. Adversarial +3. |
| 2026-04-09 | jason-fladlien-marketing | Add Cost-of-Keeping Calculus to Identity-Based Offer & Funnel Design | KEPT | 6.0→8.0 (+2.0) | Phase 0: 4-dimension cost ledger (Time, Status, Opportunity, Identity Tax) + Self-Evidence Test + Identity Layer Reveal. Makes subtraction self-evident instead of marketer-asserted. Adversarial +3. |
| 2026-04-09 | luke-iha-million-dollar-mechanisms | Add Process Autopsy Protocol to Mechanism Discovery Engine | KEPT | 6.0→8.3 (+2.3) | Phase 1.5: Method Decomposition, 4 Proprietary Edge lenses (Counterintuitive Step, Invisible Step, Sequence Dependency, Client Inflection Point), competitor-claim gate. Mechanisms grounded in actual process, not category abstraction. Adversarial +3. |
| 2026-04-09 | kallaway-content-psychology | Add Resonance Prediction & Signal Feedback to Strategic Market Architecture | KEPT | 7.3→8.7 (+1.4) | 5 resonance indicators, falsifiable predictions, signal reading protocol, adaptation triggers. Largest genius file (868 lines). Turns static strategy into self-correcting system. Adversarial +2. |
| 2026-04-09 | nicolas-cole-niche-positioning | Add Compounding Signal Analysis to Specificity Drill | KEPT | 6.3→8.3 (+2.0) | 5 compounding signals (Referral Density, Problem Recurrence, Expertise Accumulation, Authority Snowball, Adjacent Expansion). Scores niche /15. Transforms "is this specific enough?" into "will this compound?" Adversarial +3. |
| 2026-04-09 | lulu-cheng-meservey-communications | Add Behavioral Commitment Architecture to Founder Narrative workflow | KEPT | 7.0→8.0 (+1.0) | 5 commitment mechanics (Self-Test, Micro-Declaration, Sunk Cost Seed, Private Litmus, Identity Threshold). Bridges gap between naming what people feel and changing what people do. Adversarial +2. |
| 2026-04-09 | luke-iha-creative-strategy | Add Category Pattern Disruption layer to Creative Strategy Brief | KEPT | 7.0→8.3 (+1.3) | Phase 2.5: Category Creative Inventory, Pattern Convergence Map, Disruption Candidates, uncopiability test. Maps how category LOOKS/FEELS/MOVES, not just what it says. Adversarial +2. |
| 2026-04-09 | dai-media-consumer-posture | Add Decision Trigger Mapping to Consumer Identity Discovery Blueprint | KEPT | 7.0→8.7 (+1.7) | 5 trigger mechanics (Identity Confirmation Threshold, Permission Structure, Environmental Catalyst, Cost-of-Inaction Crystallization, Social Proof Alignment Check). Bridges posture-to-purchase gap. Copy-actionable synthesis paragraph. Adversarial +2. |
| 2026-04-09 | mitch-albom-writing-mastery | Add Emotional Frequency Selection to High-Density Manuscript Polish | KEPT | 7.3→8.3 (+1.0) | Phase 0: 3 frequencies (Recognition, Revelation, Catharsis) + Mirror/Window test + Manipulation Check. Tunes emotional register before writing begins. Recognition = naming what reader already feels. Baseline told reader about tragedy; variant made reader recognize their own. |
| 2026-04-09 | ward-farnsworth-rhetorical-mastery | Add Emotional State Matching (Phase 0) to Visceral Persuasion Bridge | KEPT | 6.0→8.3 (+2.3) | Reader State Diagnosis, Device-to-State Map (5 states to 5 devices), Intensity Calibration (one device per section, 60/40 rule, Pub Test). Rhetoric becomes invisible -- devices serve emotional moments instead of showcasing technique. Adversarial +3. |
| 2026-04-09 | tommy-clark-linkedin-growth | Add Social Currency Architecture to High-Visibility Growth Engine | KEPT | 6.3→8.3 (+2.0) | 5 forwarding mechanics (Named Recipient Effect, Gift Frame, Protective Impulse Trigger, Status Transfer Check, Conversation Starter Close). Engineers the moment a reader becomes a distributor. Posts become vehicles, not destinations. Adversarial +2. |
| 2026-04-09 | david-deutsch-copywriting | Add Earned Trust Architecture (Phase 0) to Cold Traffic Conversion | KEPT | 7.0→8.3 (+1.3) | 3 mechanics (Name Skepticism Aloud, Concede Real Limitation, Proof-as-Invitation). Modern audiences pattern-recognize DR techniques; this layer builds trust through transparency before persuasion fires. Adversarial +2. |
| 2026-04-09 | caleb-ralston-personal-brand | Add Signature Paradox Engine (Pattern 25) — irresolvable identity contradiction as compounding engine | KEPT | 7.0→8.7 (+1.7) | Deepens Pattern 18 from packaging to compounding mechanism. Paradox = Pole A (expertise) + Pole B (contradictory identity). Brands with paradox get MORE interesting over time. Expert Standard +2, Adversarial +2. |
| 2026-04-09 | sam-parr-taste-acquisition | Add Taste Transfer Architecture to Taste Acquisition Roadmap | KEPT | 6.0→8.3 (+2.3) | Phase 0.5: 5 perceptual primitives (Contrast Sensitivity, Proportion Awareness, Rhythm Detection, Coherence Intuition, Tension-Resolution Sense). Maps existing taste from other domains, compresses Copy phase 40-60%, adds cross-domain synthesis gate. Eliminates "domain-naive" assumption. Adversarial +3. |
| 2026-04-09 | diandra-escobar-linkedin-growth | Add Growth Lever Diagnosis + Compound Sequencing to Content-Market Fit Sprint | KEPT | 6.3→8.3 (+2.0) | 10-Post Signal Read identifies dominant growth lever by post 10 (not 40). 3-Post Compound Sequences engineer post-to-post demand. Bi-weekly Velocity Checkpoints with 4-step Stall Response Protocol. Adversarial +3 (biggest gain). |
| 2026-04-09 | seth-godin-philosophy | Add Temporal Cost Accounting to Strategic Clarity Engine | KEPT | 6.3→8.0 (+1.7) | Phase 3.5: Trust Ungained, Identity Unearned, Compounding Unlocked + Honest Deadline. Bridges "this is true" to "here's what I do Monday." Uses Godin's own Pattern 13 + Tacit 5 as temporal mirror. Adversarial +3. |
| 2026-04-09 | eric-roth-screenwriting-mastery | Add Subconscious Accumulation Architecture to Screenplay Architect | KEPT | 7.3→8.7 (+1.4) | 5 accumulation mechanics (Echo Planting, Absence Architecture, Behavioral Drift Mapping, Thematic Pressure Points, Convergence Tightening). Engineers invisible emotional pressure — endings feel inevitable. Expert Standard +2, Adversarial +1. First SCREENWRITING skill evolved (not content adaptation). |
| 2026-04-09 | brock-johnson-shareworthy-content | Add Sharer Identity Casting (Phase 1.5) to Shareworthy Content Factory | KEPT | 7.0→8.3 (+1.3) | Separates SHARER from READER psychology. 5 steps: identify actual sharers, name performed identity role, draft forwarding sentence, map second-order audience, design identity payoff into content. Sharing becomes self-presentation, not favor-to-creator. Adversarial +2, Expert Standard +1. |
| 2026-04-09 | authority-hacker-ai-social-media | Add Momentum Sequencing — post-to-post compounding via signal classification, 3-post sequences, callback yield | KEPT | 6.7→8.3 (+1.6) | Fills gap between Pattern 6 (weekly audit) and creative compounding. Posts become nodes in serialized narrative, not isolated events. Adversarial +2. |
| 2026-04-09 | alex-copper-creative-strategy | Add Creative Collision Architecture to Performance Creative Production | KEPT | 7.0→8.3 (+1.3) | Phase 0: Category Creative Inventory, Audience Expectation Set, Collision Design (one-violation rule), Uncopiability Test. Engineers genuine surprise by violating one category expectation while preserving strategic alignment. "Right but boring" eliminated. Adversarial +2. |
| 2026-04-09 | jasmin-alic-linkedin-growth | Add Comment Compounding Architecture to Distributed Growth Engine | KEPT | 6.0→8.3 (+2.3) | Phase 2.5: 5 compounding mechanics (Thread Mining, Reciprocity Stacking, Vocabulary Harvesting, Response-to-Post Synthesis, Engagement Debt Ledger). Turns one-way commenting-to-post pipeline into three-output engine (content seeds + relationship capital + audience intelligence). Daily routine restructured: 40min blitz + 10min mining + 10min reciprocity. Adversarial +3. |
| 2026-04-09 | ghostwriting-voice-engine | Add Reasoning Architecture Extraction (WF01 Phase 3.5) + Reasoning Pattern Deployment (WF02 Phase 3.5) | KEPT | 6.7→8.3 (+1.6) | Captures HOW someone thinks through problems — cognitive sequence, proof construction pattern, characteristic reasoning move. Baseline matched vocabulary/rhythm but thinking was interchangeable. Variant produced diagnostic trace-back reasoning that only a practitioner-thinker would use. Expert Standard +2, Adversarial +2. Core ghostwriting system, first evolution. |
| 2026-04-09 | cardinal-mason-ai-copywriting | Add Cognitive Fingerprint Injection to Multi-Channel Conversion Suite | KEPT | 6.3→8.3 (+2.0) | 5 additive mechanics (Rhythm Sabotage, Mid-Thought Pivot, Lived-Detail Anchoring, Imperfect Architecture, Voice Temperature Shifts). Flips AI-humanization from subtractive (remove tells) to additive (inject cognitive fingerprints). Adversarial +3. |

---

## Research Directions (What to Explore Next)

These are ideas for future evolution cycles, not current commitments:

- **Hook quality across content skills**: Many content skills score well on structure but plateau on hook power. Test whether borrowing Kallaway's curiosity gap patterns improves hook scores.
- **Voice authenticity**: Prose classifier catches AI tells, but can we actively inject more human variance? Test whether adding "voice disruption" steps (vary sentence length, add specific details) improves Expert Standard.
- **Cross-domain proof patterns**: Luke Iha's proof mechanisms might strengthen brand strategy skills. Test whether weaving proof architecture into positioning workflows improves Adversarial Resilience.

---

## System Status

| Component | Status | Last Activated | Entries |
|-----------|--------|---------------|---------|
| Feedback Ratchet (Phase 1) | ACTIVE | 2026-04-05 | 76 |
| Skill Evolution (Phase 2) | **ACTIVE** | 2026-04-09 | 31 |
| Cross-Pollination (Phase 3) | **READY** | 2026-04-09 (scanned) | 7 improvements mapped, 0 transferred |
| Ground Truth | READY | Manual only | — |
| Intelligence Gap Detector | READY | On-demand | — |
| Revenue Tracker | READY | Manual only | — |

---

*This document is the evolution compass. Update it after every cycle. Read it before every evolution run.*
