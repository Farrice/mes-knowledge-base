# Evolution Log: Donald Miller StoryBrand — Specificity Excavation

**Date**: 2026-04-09
**Skill**: donald-miller-storybrand
**Workflow**: 01-brandscript-generator
**Aspect**: Slot-filling genericness → Private-world specificity
**Status**: KEEP

## Hypothesis

Adding a "Specificity Excavation Layer" (Step 0) before any SB7 slot-filling forces the writer to reconstruct the target customer's private vocabulary, daily friction scenes, identity stakes, and competitor jealousy moments BEFORE populating Character/Problem/Guide/Plan/CTA/Failure/Success. This prevents the most common BrandScript failure mode: structurally valid output that is emotionally interchangeable across audiences.

The cognitive mechanism: instead of asking "What's the internal problem?" (which invites categorical answers like "feeling overwhelmed"), the excavation asks "What does this person mutter at 11pm?" — forcing simulation of a specific human's private experience.

## Benchmark

**Prompt**: "Create a BrandScript for an Authority Flywheel service targeting S&C coaches"

### Control (Current workflow — no Step 0)

**Key outputs**:
- Character desire: "Be recognized as the expert they actually are"
- Villain: "The algorithm / content marketing grind"
- Internal problem: "Feel invisible despite deep expertise"
- Failure: "Stay invisible, keep discounting, watch less-qualified coaches win online"
- Success: "Wake up to inbound inquiries, charge premium rates, be known as THE expert"

**Diagnosis**: Every element is structurally correct per SB7. But swap "S&C coach" for "therapist" or "consultant" and nothing breaks. The BrandScript works as a template — it doesn't work as recognition.

- Composite score: 6.6

### Variant (+ Specificity Excavation Layer)

**Step 0 outputs** (excavation):
- Private vocabulary: "I just watched a coach with a weekend cert get 50K followers explaining deadlifts wrong"
- Daily friction: Staring at blank Instagram caption for 20 minutes, closing app, coaching a session, opening app again, still blank
- Identity gap: Can program a periodization block in their sleep but freeze when someone says "tell me about yourself"
- Competitor jealousy: Weekend-cert coach with Canva templates and 50K followers getting the D1 consulting gig

**Key outputs**:
- Character desire: "S&C coaches who can transform an athlete's career in a session but can't explain what they do in a caption"
- Villain: "The 'post 5x a week or die' content machine that rewards performance over substance"
- Internal problem: "I just watched a coach with a weekend cert get 50K followers explaining deadlifts wrong — and I can't get a single client from posting"
- Failure: "The coach who copied your periodization model gets the D1 consulting gig because they had the content to prove credibility"
- Success: "A college S&C director DMs you saying 'I've been reading your stuff — can we talk about a consulting arrangement?'"

- Composite score: 9.0

## Delta

| Dimension | Control | Variant | Delta |
|---|---|---|---|
| Hero Recognition ("that's ME") | 6 | 9 | +3 |
| Villain Specificity | 5 | 9 | +4 |
| Internal Problem Authenticity | 6 | 9 | +3 |
| Failure Concreteness | 6 | 9 | +3 |
| Success Emotional Resonance | 6 | 9 | +3 |
| Structural Compliance (SB7) | 9 | 9 | 0 |
| Clarity (Caveman Test) | 8 | 9 | +1 |
| **Composite** | **6.6** | **9.0** | **+2.4** |

## What Changed

Added **Step 0: Specificity Excavation** to `workflows/01-brandscript-generator.md`. The step has 4 sub-components:
- 0a: Private Vocabulary Discovery (internal monologue, not category labels)
- 0b: Daily Friction Inventory (scenes, not abstractions)
- 0c: Identity Stakes Map (craft-self vs. public-self gap)
- 0d: Competitor Jealousy Moment (specific unfairness that fuels urgency)

Gate added: if Step 0 outputs could apply to any adjacent profession, they are too generic — redo.

Quality Gate updated with 2 new checks:
- Specificity Excavation was performed
- Recognition Test passed (every element contains audience-specific detail)

## Key Insight

The SB7 framework's greatest strength (universal applicability) is also its greatest weakness: it makes generic output structurally indistinguishable from specific output. Both pass all quality checks. The Specificity Excavation Layer doesn't change the framework — it changes what you FEED the framework. By reconstructing a customer's private world first, every slot gets filled with material that only that audience would recognize.

The biggest single improvement was the villain (+4). Generic villains ("the algorithm," "the status quo") create no urgency. Specific villains ("the weekend-cert coach with 50K followers who explains deadlifts wrong") create rage. Rage is survival-brain fuel — which is exactly what Miller's neurological exploit needs to fire.

Cross-pollination note: This Specificity Excavation pattern could transfer to any framework-heavy skill that risks slot-filling (email sequences, funnel architects, website wireframes). The mechanism is domain-agnostic: simulate private experience before filling structural slots.
