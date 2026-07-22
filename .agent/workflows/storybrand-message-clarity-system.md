---
description: Clarify any business message with a StoryBrand soundbite strategy and Message Clarity Pack from business context, copy, website text, or offer language so customers instantly understand and buy
---

# /storybrand-message-clarity-system

Orchestrate Donald Miller's StoryBrand and cognitive-load systems into one replayable message-clarity workflow. This is a skill system, not a duplicate expert skill.

## Objective

Produce a Message Clarity Pack that makes the business easy to understand, easy to repeat, and ready to deploy across customer-facing channels.

## Source Grounding

Read first:

1. `extractions/donald-miller/storybrand-message-clarity-system/source-map.md`
2. `extractions/donald-miller/storybrand-message-clarity-system/skill-system-contract.md`
3. `semantic_libraries/antigravity/primitives/low-cognitive-load-message-gate.md`
4. `skills/donald-miller-cognitive-load/SKILL.md`
5. `skills/donald-miller-storybrand/SKILL.md`

Use the source map for grounding, but do not load full transcripts unless the user asks for evidence details or the output needs timestamp-level support. Treat `SzugliCQ3XY` as the BELAY message-scale case study from local metadata, not the earlier Guru Conference planning assumption.

## Runtime Inputs

Required:

- Business name
- What it sells
- Target customer
- One primary customer problem

Optional:

- Existing copy, website text, offer text, sales script, social bio, or URL
- Active channels and responsible roles
- Existing BrandScript, one-liner, or sound bites

If the required inputs are missing and cannot be inferred, ask only for the missing business, customer, offer, or one primary problem.

## Component Order

### Phase 0: Low-Cognitive-Load Message Gate

Load:

1. `.agent/workflows/low-cognitive-load-message-gate.md`

Run this gate when existing copy, offer language, homepage text, social bio, pitch language, or a draft message is supplied. If no copy is supplied, use the gate on the candidate problem, answer, and repeatability-lock language after Phase 1.

The gate owns only the stop condition:

- phrase-level cognitive-load scores
- one-problem enforcement
- hero/guide correction
- repeatability lock
- PASS / REVISE / REWORK verdict

If the gate returns `REWORK`, fix the locked problem before continuing. If it returns `REVISE`, carry the required fixes into the cognitive-load autopsy and PEACE phases. Do not let the gate replace the full Message Clarity Pack.

### Phase 1: Input Gate And One-Hole Lock

Use the cognitive-load One-Hole rule:

- Name one specific customer problem.
- Reject bundled problems with commas or multiple pains.
- Choose the problem that is most felt, most urgent, and easiest for the customer to recognize.

Output:

- Business
- Target customer
- One-hole problem
- Skip/ask rationale if context is insufficient

### Phase 2: Cognitive-Load Autopsy

Load:

1. `skills/donald-miller-cognitive-load/genius.md`
2. `skills/donald-miller-cognitive-load/workflows/01-cognitive-load-autopsy.md`

If copy is supplied, score the existing language. If no copy is supplied, score the proposed problem, offer, and one-liner candidates.

Output:

- High-load phrases
- Why they are heavy
- Zero-load rewrite direction
- Phrases to avoid

### Phase 3: PEACE Sound Bites

Load:

1. `skills/donald-miller-cognitive-load/workflows/02-peace-soundbite-generator.md`

Generate locked sound bites:

- Problem
- Empathy
- Answer
- Change
- End Result

Output:

- 3 to 5 problem candidates with scoring
- selected PEACE system
- standalone, chain, and decade repetition checks

### Phase 4: StoryBrand One-Liner And Alignment

Load:

1. `skills/donald-miller-storybrand/genius.md`
2. `skills/donald-miller-storybrand/workflows/04-one-liner-generator.md`
3. `skills/donald-miller-storybrand/workflows/01-brandscript-generator.md` only for alignment rules, unless the user explicitly asks for a full BrandScript.

Build the one-liner from the locked problem, answer, and result. Then add short BrandScript alignment notes:

- Character/customer
- External, internal, and philosophical problem
- Guide empathy and authority
- Simple plan
- CTA decision resolution
- Failure stakes
- Success transformation

Output:

- Core one-liner
- conversation, social bio, email signature, and pitch variants
- BrandScript alignment notes

### Phase 5: Deployment Matrix

Load:

1. `skills/donald-miller-cognitive-load/workflows/05-soundbite-deployment-matrix.md`

If active channels are not supplied, use:

- website hero
- social bio or profile headline
- pinned post
- email signature
- sales-call opener
- proposal cover
- newsletter subject line

Output:

- channel-by-channel placement
- exact copy to use
- lock status
- monthly consistency audit

## Output Schema

```markdown
# Message Clarity Pack: [Business]

## One-Hole Lock
- Customer:
- Problem:
- Why this problem wins:

## Cognitive-Load Autopsy
| Current or Candidate Phrase | Load | Why It Is Heavy | Zero-Load Rewrite |

## Locked PEACE Sound Bites
| Role | Sound Bite | Use |

## StoryBrand One-Liner
- Core:
- Conversation:
- Social Bio:
- Email Signature:
- Pitch:

## BrandScript Alignment Notes
| Element | Message |

## Deployment Matrix
| Channel | Exact Copy | Owner/Role | Lock |

## Monthly Consistency Audit
- [ ] Website hero still uses the locked problem or end-result language.
- [ ] Social bio/profile headline still carries the answer and change.
- [ ] Last 10 posts include at least one locked sound bite.
- [ ] Last 5 emails use the problem or end result.
- [ ] Sales opener uses the problem and empathy.
- [ ] No channel has "refreshed" the locked phrases without rerunning this workflow.

## Quality Gate
- Verdict:
- Revision made:
- Remaining risk:
```

## Quality Gate

Before final output, verify:

- The low-cognitive-load gate was run or explicitly skipped with a reason.
- One customer problem is locked.
- The customer is hero and the business is guide.
- Product language appears after the problem is clear.
- Every sound bite is plain enough to repeat.
- Problem and End Result bookend each other.
- The one-liner follows Problem -> Solution -> Result.
- The deployment matrix uses exact locked wording, not creative variations.
- Any source-video claim stays transcript-only unless full visual evidence exists.

**Execution prompts**: before producing the deliverable, check `skills/donald-miller-cognitive-load/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
