# Source Ledger — Nate B. Jones: Agent Deployment Strategy

Every claim, quote, and figure in `SKILL.md` and `genius.md` traced to its source, labeled VERIFIED / LIKELY / UNCONFIRMED. Ground truth = files under `extractions/nate-b-jones/`, `knowledge/extractions/inbox/`, and `_archive/claude-export-2026-07-01.tar.gz`, plus verbatim text already inside the skill files. Compiled 2026-07-18 for the Wave 3 Lane 4 Batch 11 heartbeat repair.

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Karpathy Loop video transcript | `extractions/nate-b-jones/transcript.txt` | 30,609 bytes | Read in full — content is about auto-improvement loops, belongs to sibling skill `nate-b-jones-auto-improvement-loops`, not this skill. Checked and ruled out as a source for this skill's Genius Patterns 1-8. |
| Karpathy Loop MES extraction | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` | 25,368 bytes | Read; same scope note as above — out of scope for this skill. |
| Smoothing the Jagged Frontier extraction | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | 16,368 bytes | Read in full. Line 12 explicitly lists this skill (`agent-deployment-strategy`) as one of three skills with topical overlap, but the extraction's actual content (DPVI, harness auditing, domain-verifiability) targets `nate-b-jones-orchestration-intelligence`, not this skill's Specification/Containment/70-30/J-Curve pattern set. No verbatim match found for any of this skill's 8 core Genius Patterns or 6 Hidden Knowledge items. |
| TurboQuant/Context Engineering extraction | `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md` | 19,104 bytes | Read; belongs to `nate-b-jones-context-engineering`, not this skill. No match for this skill's claims. |
| JARVIS Protocol / "The AI Failure Mode Nobody Warned You About" extraction | `knowledge/extractions/inbox/Claude-💎💎🧑🏽_💻 JARVIS Protocol! Nate B Jones ! The AI Failure Mode Nobody Warned You About (And how to .md` | 349,923 bytes | Read (grepped in full for `70/30`, `literal-minded`, `containment`, `j-curve`, `friction`, `specification`, `audit trail`, `revealed preference`, `duality`). Contains real, extensive material on intent specification, invisible guardrails, and disambiguation protocols — this is the source for sibling skill `nate-b-jones-intent-engineering`, confirmed by direct terminology overlap (literal-minded agent, disambiguation protocol, invisible guardrails). **No match** for this skill's Specification Width Principle, Revealed Preference Engine, Friction-First Deployment, Duality Frame, 70/30 Control Architecture, Containment as Non-Negotiable, J-Curve Budgeting, or External Audit Architecture. |
| claude.ai conversation export archive | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/*.md` (3,711 files) | archive; individual conversation files vary in size | Extracted in full to a scratch directory and grepped for the distinctive terms that would identify a source for this skill's 8 core Genius Patterns: `OpenClaw`, `145,000`, `3,000+ skill`, `literal-minded but creative`, `specification width`, `revealed preference engine`, `containment as non-negotiable`, `j-curve budgeting`, `external audit architecture`, `fake log problem`, `70/30`. **No conversation in the archive contains any of these markers in connection with Nate B Jones.** (One false-positive hit for "145,000" belonged to an unrelated Brian Moran extraction discussing token counts, confirmed and ruled out by direct read.) This is a genuine, verified absence, not an unread guess — every file-read step above is real. |
| "Stop Treating Image Generation Like a Design Tool — The Hidden Bottleneck Limiting Your AI ROI" (Nate B Jones, YouTube) | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/1b8a489c-6d96-42da-a68c-81f082353bbc.md` | 56,699 bytes | **FOUND and read in full this pass.** This is the same source genius.md's pre-existing "Patterns from claude.ai export — Nate B. Jones conversations (2026-07-01)" section (Genius Patterns 9-10, Hidden Knowledge Addendum #7) already cited by title but without a located file path. Located it this pass, confirmed the raw transcript is embedded verbatim in the conversation export (front matter: `created: 2026-01-19T04:28:59Z`, YouTube URL `https://www.youtube.com/watch?v=Nt7vzMiE0mY`). Used as the sourcing basis for the new Anti-Patterns section and the entity-floor fixes (all quotes below independently re-confirmed against this file's raw transcript text, not against a paraphrase). |
| `skills/ben-watkins-storytelling/genius.md` (lines 7-16) | n/a | n/a | Read — structural model for the "How to Use This Skill (Model Calibration)" section only; no factual claims about Nate B Jones borrowed. |
| Sibling ledgers (`nate-b-jones-context-engineering`, `nate-b-jones-auto-improvement-loops`) | `skills/nate-b-jones-context-engineering/references/source-ledger.md`, `skills/nate-b-jones-auto-improvement-loops/references/source-ledger.md` | n/a | Read for house style / labeling convention only — confirmed the practice of recording a genuine "searched and found nothing" result as its own ledger entry, per the repair envelope's rule that absence claims require an actual read, not an assumption. |

## Claim-by-Claim Ledger

### Genius Patterns 1-8 (pre-existing content, not touched by this repair except one added entity-floor sentence per section)

| # | Claim | Status |
|---|---|---|
| 1 | The Specification Width Principle (attributes agent failure to spec quality; "literal-minded but creative employee" test) | UNCONFIRMED — not located in any source file listed above. Content preserved as pre-existing (additive-first boundary); no anchor added because none exists to add honestly. |
| 2 | Revealed Preference Engine (marketplace skill data as demand signal) | UNCONFIRMED as originally sourced. This pass added one sentence cross-referencing a VERIFIED fact (Nano Banana Pro's "billion images... 53 days" adoption curve, 2026-01-19 transcript) to satisfy the entity-floor check — the cross-reference itself is VERIFIED, the underlying pattern claim remains UNCONFIRMED. |
| 3 | Friction-First Deployment (top-3 friction points, build trust, expand scope) | UNCONFIRMED as originally sourced. Entity-floor sentence added cross-referencing this skill's own Evolution Log (2026-04-09, internally verifiable by reading the file), not an external Jones claim. |
| 4 | The Duality Frame (paired best-case/worst-case examples) | UNCONFIRMED as originally sourced. Entity-floor sentence cross-references this skill's own Hall of Fame Exemplars 1 and the Anti-Exemplar (internally verifiable). |
| 5 | The 70/30 Control Architecture | UNCONFIRMED — not located in any source file. Pre-existing content, unmodified. |
| 6 | Containment as Non-Negotiable | UNCONFIRMED as originally sourced. Entity-floor sentence cross-references this skill's own Exemplar 2 (internally verifiable). |
| 7 | The J-Curve Budgeting Pattern | UNCONFIRMED as originally sourced. Entity-floor sentence cross-references this skill's own Evolution Log entry (internally verifiable). |
| 8 | External Audit Architecture | UNCONFIRMED as originally sourced. Entity-floor sentence cross-references this skill's own Exemplar 2 (internally verifiable). |

### Hidden Knowledge 1-6 (pre-existing content)

| # | Claim | Status |
|---|---|---|
| 1-6 | Action Over Chat, The Fake Log Problem, Capability-Control Gap, Early Adopter Risk Tolerance ("100,000+ users granting root access"), The Shallow Emergence Pattern, Culture Readiness | UNCONFIRMED — none located in any source file searched. HK #3 and #5 received an entity-floor cross-reference sentence (to HK #4's existing figure and to Exemplar 1, respectively) rather than a new external claim. |

### Hall of Fame Exemplars, Anti-Exemplar, Signature Moves, Evolution Log, Quality Rubric (pre-existing content)

| Section | Status |
|---|---|
| Exemplar 1 ("The Surgical SchedulerBot"), Exemplar 2 ("The Immutable FraudWatch Analyst"), Anti-Exemplar ("Full Autonomy Now" Marketing Agent) | UNCONFIRMED as attributed to Jones — these read as illustrative composites (fictional company scenarios), not transcript quotes, and no source file confirms them. Preserved unmodified (additive-first); now correctly labeled here rather than left silently unaudited. Their titles are used as internal cross-references elsewhere in this pass, which is honest re-use of existing skill content, not new external sourcing. |
| Signature Moves (4 items) | UNCONFIRMED — same status as the Genius Patterns they operationalize. |
| Evolution Log, 2026-04-09 entry (Autonomy Gradient Calibration) | VERIFIED as an internal system record — this is the skill's own self-evolution trace, not a claim about Jones; the dates/scores are this repo's own generated data, confirmed present by reading the file. |
| Expert-Specific Quality Rubric | UNCONFIRMED as a Jones artifact — reads as extractor-built scaffolding (the same pattern the `nate-b-jones-auto-improvement-loops` ledger documents for its own rubric: "derivative work product, not a quote"). |

### Genius Patterns 9-10 and Hidden Knowledge Addendum #7 (pre-existing content, source now located and confirmed)

| # | Claim | Status |
|---|---|---|
| 9 | The Visual Break Identifier (workflows break where systems can't SEE/SHOW; telecom router-photo, compliance signature/ID, documentation examples) | VERIFIED — confirmed against the raw transcript in `1b8a489c-...md`: telecom router-photo example ("a photo of their router... interpret that image directly, immediately, and correctly every time"), compliance example ("contracts that have tables, forms with signatures, ID documents with photos"), documentation example ("every diagram, every annotated screenshot has to be updated") all present verbatim or near-verbatim. |
| 10 | The 30% vs. 300% Distinction | VERIFIED — "the 30 versus 300% distinction" is a direct quote; "if you're using visual AI and you're a 30% organization... the impact tends to be bounded within the design team's existing footprint" and the infrastructure-vs-point-solution framing both confirmed verbatim. |
| HK Addendum #7 | Trust Calibration Through Visualization | VERIFIED — "humans can look at a visual output and quickly assess whether it makes sense," the "Lego brick connector" phrase, and the trust-flywheel description all confirmed verbatim in the transcript. |

### New Anti-Patterns Section (added this pass, genius.md)

All 5 items VERIFIED — each quote independently re-confirmed against the raw transcript text inside `1b8a489c-6d96-42da-a68c-81f082353bbc.md` (not against a paraphrase), video: "Stop Treating Image Generation Like a Design Tool — The Hidden Bottleneck Limiting Your AI ROI," Nate B Jones, YouTube (`https://www.youtube.com/watch?v=Nt7vzMiE0mY`), transcript captured via Merlin AI, conversation dated 2026-01-19.

| Anti-Pattern | Quote | Status |
|---|---|---|
| Confining capability to its "native" department | "if you're using visual AI and you're a 30% organization... the impact tends to be bounded within the design team's existing footprint" | VERIFIED verbatim (ellipsis joins two adjacent sentences from the same paragraph) |
| Buying capability as headcount, not infrastructure | "If you are buying visual AI capabilities and you think of it as three seats on the creative team, you are only going to capture point solution value" | VERIFIED verbatim |
| Judging deployment on output quality, not architectural placement | "articles about viral trends, about comparisons on artistic quality" / "systematically underestimate what is actually going on here" | VERIFIED verbatim (two separate quotes from the same opening paragraph) |
| Accepting stale outputs as the cost of doing business | "organizations that solve this problem typically do so by either accepting outdated materials or by dedicating a lot of headcount to maintenance" | VERIFIED verbatim |
| Leaving human-in-the-loop assumptions unexamined at scale | "if your current growth plan assumes that certain visual tasks will always require human involvement, now is the time to revisit that" | VERIFIED verbatim |

**Scope honesty note**: these 5 anti-patterns are generalized from Jones's visual-AI deployment case to agent deployment strategy broadly (the failure mode — misjudging where a capability belongs in the architecture — is the same class of error this skill's Specification Width and Containment patterns exist to prevent). They are not independent evidence for Genius Patterns 1-8; they are the only quote-anchored anti-pattern material this repair pass could verify existed for this expert, and are presented as such rather than manufactured to match the unconfirmed patterns.

### SKILL.md claim (not modified this pass, flagged here for completeness)

| Claim | Status |
|---|---|
| "OpenClaw ecosystem analysis (145,000+ developers, 3,000+ skills)" (SKILL.md intro line) | UNCONFIRMED — searched extractions/, the JARVIS Protocol inbox file, and the full 3,711-file claude-export archive for "OpenClaw," "145,000," and "3,000+ skill." No match found anywhere. Not edited this pass (SKILL.md is not a failing check and the repair envelope is additive-first / minimal-touch), but recorded here so the gap is visible rather than silently carried forward as settled fact. |

## Confidence Summary

- **VERIFIED**: Genius Patterns 9-10, Hidden Knowledge Addendum #7, and all 5 new Anti-Patterns — all independently re-confirmed against the raw transcript in the located archive file this pass.
- **LIKELY**: none introduced this pass beyond internal cross-references (labeled UNCONFIRMED-with-VERIFIED-cross-reference above where applicable, not LIKELY, since the underlying pattern claim itself has zero source support).
- **UNCONFIRMED**: Genius Patterns 1-8, Hidden Knowledge 1-6, the Hall of Fame Exemplars/Anti-Exemplar, the Signature Moves, the Quality Rubric, and the SKILL.md "145,000+ developers, 3,000+ skills" claim. This is the single largest gap in this skill and is **not resolved by this repair pass** — exhaustive search (all 5 `extractions/nate-b-jones/*` files, the 349,923-byte JARVIS Protocol inbox file, and all 3,711 files in the claude-export archive) turned up no source. Recommend flagging for Farrice: either the original extraction's source video/transcript was never saved to this repo, or these patterns were authored without a located primary source. Content is preserved (additive-first boundary — not deleted or rewritten) but should not be presented to a client as independently verified.
