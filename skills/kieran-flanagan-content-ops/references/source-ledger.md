# Source Ledger — kieran-flanagan-content-ops

Claim-by-claim provenance for SKILL.md + genius.md. Labels: **VERIFIED** (quote/fact
located verbatim or near-verbatim in a source file), **LIKELY** (paraphrase or
extraction-author synthesis of a real Kieran statement, not word-for-word), **UNCONFIRMED**
(no source located after an actual file read — treat as a plausible operating default,
not a sourced Kieran claim).

## Source inventory (sizes verified via `wc -c`, repo-relative paths)

| File | Bytes | Role |
|---|---:|---|
| `extractions/kieran-flanagan/transcript.txt` | 27,523 | PRIMARY — full transcript, "I Built an AI Team That Creates All My Content," Marketing Against the Grain (the transcript's closing outro plays a HubSpot ad bumper branded "Marketing Against the Grain"; `extraction-report.md` labels the source "Greg Isenberg Show" — see discrepancy note below). This is the direct source for the content-ops skill (orchestrator, feedback loop, 11-skill architecture). |
| `extractions/kieran-flanagan/extraction-report.md` | 14,945 | PRIMARY — MES extraction report synthesized from the transcript above. Genius Patterns 1-8, Hidden Knowledge, Methodology sections. |
| `extractions/kieran-flanagan-second-brain/extraction-notes.md` | 19,570 | NOT USED for this skill's content — this is a separate, later extraction ("second brain" video) whose net-new material was explicitly routed to `simon-intellectual-library-os` and `liam-mley-ai-brain-builder` per its own "Where it landed" section. Not cited here to avoid manufacturing cross-skill provenance. |
| `extractions/kieran-flanagan-second-brain/visual-context.md` | 62,307 | Same as above — out of scope for content-ops. |
| `extractions/kieran-flanagan-second-brain/download/video.en.vtt` | 198,837 | Same as above — out of scope for content-ops. |

**Discrepancy note (honest, not swept under)**: `extraction-report.md` line 4 labels the
source "YouTube Interview... (Transcript, Greg Isenberg Show)." The transcript itself
never names its show, and its outro ad bumper is HubSpot-branded, consistent with
Kieran's own podcast, Marketing Against the Grain (which the second-brain extraction's
metadata independently confirms as his show, `nTiMbqFwv4c`, "Marketing Against the
Grain"). The show-name attribution in `extraction-report.md` is therefore flagged
UNCONFIRMED/likely mislabeled — it does not affect any content claim used in this skill,
since all quotes below are anchored to `transcript.txt` directly, not to the show name.

## Genius Patterns 1-3 (genius.md)

| Claim | Label | Source |
|---|---|---|
| Orchestrator Pattern (meta-skill, chains other skills, human checkpoints) | VERIFIED | `transcript.txt`: "the orchestrator skill is going to actually use all the other skills, which makes it really easy to use the system"; `extraction-report.md` Pattern 7 |
| Feedback Loop Self-Improvement (engagement data feeds back into system) | VERIFIED | `transcript.txt`: "I can just go and run a skill. And the skill does a review analysis of all of the performance... it actually updates all of my skills. So it's a skill that improves my skills." |
| Separation of Execution and Optimization (orchestrator never creates content) | LIKELY | Consistent with the demonstrated 5-layer architecture in `extraction-report.md` Methodology, but the explicit "never let optimization tools create content" framing is the extraction author's structural inference, not a direct Kieran quote. |

## Hidden Knowledge 1-4 (genius.md)

| # | Claim | Label | Note |
|---|---|---|---|
| 1 | "2-3 feedback cycles (2-6 weeks)" for noticeable improvement | UNCONFIRMED | Not located in `transcript.txt` or `extraction-report.md` after full read. |
| 2 | "I just talk with the orchestrator and ask it to do things..." | LIKELY | Near-identical line in `transcript.txt` ("You can kind of just th with the orchestrator skill and ask it to do things and it goes and uses all of the other skills for you") — the verb is almost certainly a transcription artifact for "talk with." Cleaned-up paraphrase, not letter-for-letter. |
| 3 | "10-20 posts" / "10 published posts or 1 month" minimum batch for feedback | UNCONFIRMED | Not located in either source file. |
| 4a | Monthly review cadence ("Kieran runs monthly review cycles") | VERIFIED | `transcript.txt`: "every month I run a review and it actually makes the skills better" |
| 4b | "Style whiplash" framing / explicit weekly-vs-monthly tradeoff reasoning | UNCONFIRMED | Phrase and reasoning not located; extrapolated from the verified monthly-cadence fact (4a). |

## Hall of Fame Exemplars (genius.md)

| Item | Label | Note |
|---|---|---|
| Exemplar 1 — "Anti-Vocabulary Advantage" bundled series (LinkedIn/X/Newsletter copy) | ILLUSTRATIVE, not attributed to Kieran | Skill-authored demonstration copy showing the anti-vocabulary pattern in action. Not a real Kieran post, not a transcript quote. Flagged explicitly in genius.md as a provenance note to prevent misreading as a Kieran quote. |
| Exemplar 2 — Growth-Stage SaaS audience profile | ILLUSTRATIVE, not attributed to Kieran | Synthetic profile demonstrating "content-reactive profiling" (`extraction-report.md` Pattern 1). Not a real published Kieran profile. |
| Anti-Exemplar — generic AI LinkedIn post | ILLUSTRATIVE (negative example) | Authored to demonstrate AI slop, not a claim about Kieran. |

## Signature Moves 1-5 (genius.md)

| # | Claim | Label | Source |
|---|---|---|---|
| 1 | System Architect's Blueprint (maps full pipeline before starting) | VERIFIED | `transcript.txt`: "11 skills across five different layers of content"; `extraction-report.md` Methodology, 5-Layer Architecture |
| 2 | Voice Dissection First, Creation Second (content-reactive profile + USE/NEVER-USE lists before creation) | VERIFIED | `extraction-report.md` Patterns 1-2; `transcript.txt` audience-profile walkthrough ("vocabulary library... what they do and don't say") |
| 3 | Negative Constraint Principle (anti-vocabulary does more work than USE list) | VERIFIED | `extraction-report.md` Pattern 3 + Hidden Knowledge: "A 50-word 'never use' list eliminates more AI slop than a 200-word 'always use' list." |
| 4 | Evidence Staging Protocol (draft first, enrich second) | VERIFIED | `transcript.txt`: "trying to enrich just a idea is kind of hard" (demonstrates the sequencing requirement directly); `extraction-report.md` Pattern 5 |
| 5 | Monthly System Refinement (resists weekly tweaks) | LIKELY | Core monthly cadence VERIFIED (see Hidden Knowledge 4a); the "resists weekly tweaks / style whiplash" framing is UNCONFIRMED per above — Signature Move 5 blends a verified fact with an unconfirmed elaboration. |

## Anti-Patterns (new section, genius.md)

| # | Claim | Label | Source |
|---|---|---|---|
| 1 | Cut-and-paste shipping rejected | VERIFIED | `transcript.txt`: "too many people will use these cut and paste. That's not how you do that, right?" |
| 2 | Enriching a raw idea (vs. a drafted argument) fails | VERIFIED | `transcript.txt`: "trying to enrich just a idea is kind of hard" |
| 3 | Shipping first hook draft rejected | VERIFIED | `transcript.txt`: "obviously I would never ship this" (re: his own "zero employees" LinkedIn draft) |
| 4 | Drag-and-drop "vibe marketing" workflow tools rejected | VERIFIED | `transcript.txt`: "I was never a big fan of the kind of vibe marketing where it was workflow tools because it's not vibing... This is not software." |
| 5 | Stopping before the feedback loop = non-systems-thinker | VERIFIED | `transcript.txt`: "If you're a system thinker, most people stop here." |
| 6 | Demographic/survey-built personas rejected as "fiction" | LIKELY | `extraction-report.md` Hidden Knowledge — extraction-author synthesis of Kieran's content-reactive-profiling position; not a verbatim on-camera quote. |
| 7 | One AI pass drafting + citing simultaneously produces hallucinated data | LIKELY | `extraction-report.md` Hidden Knowledge — same synthesis caveat; the underlying "draft then enrich" sequencing is independently VERIFIED via item 2 above. |

**Anti-patterns sourced-item count**: 7 of 7 carry an explicit file anchor; 5 are VERIFIED
verbatim quotes, 2 are LIKELY (extraction-author synthesis of a real position, labeled
honestly rather than upgraded to VERIFIED).

## Expert-Specific Quality Rubric (genius.md)

Authored evaluation framework (criteria + score anchors), not a factual claim about
Kieran — out of scope for VERIFIED/LIKELY/UNCONFIRMED labeling. Criteria names map
directly to VERIFIED patterns above (Content-Reactive, Platform Voice Fidelity,
Anti-Vocabulary Compliance, etc.), so no new provenance risk.

## Workflows after the 2026-07-30 expansion

The historical 2026-07-18 repair covered three workflows. The skill now has four:

- `01-content-orchestrate.md` adds an Ideate route and explicit human selection gate.
- `02-content-feedback.md` proposes formula-level Winning Content Profile deltas without mutation.
- `03-content-review-cycle.md` owns monthly approval, version changes, and queue-health decisions.
- `04-content-queue.md` owns selected queue state and visible lifecycle operations.

## 2026-07-30 Expansion: Human-Curated Queue State

| Claim | Source | Label |
|---|---|---|
| Kieran keeps a persistent content queue | `extractions/transcripts/cSz_6SNEirU.txt` | VERIFIED |
| He shows the queue, kills unwanted ideas, and adds three selected candidates | Same transcript | VERIFIED |
| He says the queue requires continual cleanup because it has too many items | Same transcript | VERIFIED |
| Queue categories such as spicy take, data nugget, and educational are personal to how he works | Same transcript | VERIFIED |
| Queue context is available across Claude and ChatGPT | Same transcript | VERIFIED |
| Explicit lifecycle states, mutation deltas, persistent tombstones, and a single-operation contract | `extractions/kieran-flanagan-content-signal-loop/architecture-checkpoint.md` | INFERRED implementation |
| Feedback proposes profile deltas and monthly review approves them | Same architecture checkpoint, grounded in Kieran's verified monthly update behavior | INFERRED control split |

The implementation does not claim Kieran used Markdown, these exact field names, or tombstones. Those controls make the demonstrated shared-state behavior auditable and resistant to duplicate resurfacing.
