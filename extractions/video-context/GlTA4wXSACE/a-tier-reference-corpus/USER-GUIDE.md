# Storytelling System User Guide

## What This Gives You

You now have a decision-first storytelling system that can create stronger communication without forcing every task into a dramatic story.

The hardened corpus and repairs currently live in the isolated `codex/david-perell-storytelling-system` worktree. They are locally usable and verified there, but they are not yet committed, merged, or activated as a global mirror.

Its first question is not “How do we make this more cinematic?” It is:

> How much story can this objective and this evidence honestly support?

The system chooses one of three modes:

| Mode | What it means | Best fit |
|---|---|---|
| `FULL STORY` | Transformation is the spine because the material contains a real want, obstacle, turn, and change | Founder stories, origin stories, customer transformations, keynote material |
| `STORY FRAGMENT` | Evidence or explanation stays primary; one real moment, analogy, or before-and-after improves recognition or recall | Sales pages, educational pieces, health communication, research-led content |
| `NO STORY` | The audience needs a decision, procedure, status, specification, or safeguard instead of narrative theater | Technical memos, operating handoffs, incident updates, direct instructions |

That restraint is a capability. It prevents invented emotion, false stakes, unsupported causality, and “storytelling” that makes serious work less clear.

## What the Six-Domain Corpus Added

The Shaan system already had storytelling workflows. This corpus added real-world calibration and regression proof.

1. **Founder:** proved the system can recognize when a complete transformation story is justified and write it without inventing scenes or market proof.
2. **Sales:** exposed that a real before-and-after does not automatically justify turning the whole offer into a full story. This remains the one pending dosage boundary.
3. **Health:** proved that evidence can stay primary while one sourced personal moment improves recognition without becoming medical proof.
4. **Technical:** proved that refusing story can be the expert move when the job is an engineering decision.
5. **Educational:** proved that a framework can remain the spine while a bounded real example makes it easier to understand and remember.
6. **Operational:** proved that readiness, sending, selling, and collecting must remain separate states. Turning readiness into a success story would be false.

The result is not merely six samples. It is a behavioral test suite for whether future storytelling changes preserve dosage, truth, ownership, and restraint.

## The Simplest Way to Use It

Ask Codex:

```text
Use /shaan-story-deploy on this material.

Objective: [what the audience should understand, feel, decide, remember, or do]
Raw material: [facts, notes, evidence, draft, or source paths]
Audience: [stranger, reader, buyer, customer, or internal stakeholder]
Truth risk: [personal, ordinary real-world, or evidence-sensitive]
Destination: [post, article, email, sales page, video, memo, or provisional]
Voice owner: [Farrice, brand, client, or none]

Choose FULL STORY, STORY FRAGMENT, or NO STORY before writing. Use one body owner, preserve uncertainty, and return the finished asset plus a Story Deployment Receipt.
```

Only three fields are decision-critical: objective, raw material, and truth risk. If the channel or audience is not settled, the system can produce a clearly labeled, platform-neutral provisional asset instead of inventing context.

## What You Can Use It For

### Founder and personal storytelling

Use it to turn real life material into:

- a founder manifesto;
- an origin story;
- an About page narrative;
- a podcast introduction;
- a keynote spine;
- a bank of reusable signature stories.

Useful prompt:

```text
Use /shaan-story-deploy to determine whether these notes contain a full founder story. Do not invent scenes, dialogue, motives, or chronology. If the story qualifies, produce a platform-neutral manifesto and show me the exact want, obstacle, turn, and change you used.
```

### Content creation

Use it to:

- turn voice notes into polished drafts;
- diagnose and rebuild flat articles or scripts;
- create social posts from expertise;
- strengthen hooks and frames without clickbait;
- convert one idea into a story-led newsletter or video;
- decide when a direct explanation is stronger than a personal anecdote.

Useful prompt:

```text
Run /shaan-story-deploy on this content idea. Choose the smallest truthful narrative dosage, then create the asset for [platform] and explain what the story mechanic contributes that direct explanation alone would not.
```

### Sales and offer communication

Use it to:

- build or revise landing-page cores;
- create sales-page and email-sequence architecture;
- turn supplied customer proof into bounded before-and-after evidence;
- separate real process facts from attractive but invented service language;
- keep one CTA and one body-writing owner.

Useful prompt:

```text
Use /shaan-story-deploy on this offer brief and proof set. Treat the offer and proof spine as primary. Use a story fragment unless the supplied facts support a complete transformation. Do not invent what happens inside the service, customer reactions, conversion results, or urgency.
```

### Health, research, and educational communication

Use it to:

- make evidence easier to understand without turning anecdotes into proof;
- build educational frameworks around verified sources;
- use a real moment or labeled analogy as a recall aid;
- preserve `VERIFIED`, `LIKELY`, and `UNCONFIRMED` distinctions;
- block unsupported benefit or dose claims, causal inference, and category-wide conclusions.

Useful prompt:

```text
Use /shaan-story-deploy for this evidence-sensitive brief. Keep evidence as the spine. Allow at most one sourced story fragment for recognition or recall. Do not let the fragment strengthen the scientific claim, imply causality, or become advice.
```

### Technical and operational communication

Use it to:

- write decision memos;
- clarify incidents and safeguards;
- build send/no-send handoffs;
- separate current state, proposed repair, and acceptance criteria;
- preserve `prepared`, `sent`, `held`, `sold`, and `collected` as different states.

Useful prompt:

```text
Run /shaan-story-deploy on this internal brief. If the real job is a decision, procedure, status, specification, or risk statement, choose NO STORY. Improve hierarchy and clarity without adding a protagonist, dramatic stakes, or implied success.
```

### Voice systems and team handoff

Use the broader Shaan system to:

- build a voice-transfer playbook from authorized samples;
- create a signature story bank;
- build an audience-feeling and brand-voice blueprint;
- teach a ghostwriter, teammate, or AI how to reproduce the underlying mechanics without copying surface style.

Useful prompt:

```text
Use the Shaan voice-transfer workflow on these authorized samples. Extract the format and the logic behind it. Build an example bank and editing filters. Preserve the source voice without treating every piece as a story.
```

## What You Receive Each Time

A complete run returns:

1. the finished communication asset;
2. the selected narrative dosage;
3. why the other two modes were rejected;
4. the one production owner used;
5. the facts and sources relied on;
6. uncertainty and prohibited inventions;
7. remaining deployment risk.

This receipt makes the writing inspectable. You can disagree with the taste decision without having to reconstruct how the system got there.

## How the Regression System Protects Future Work

Before promoting a meaningful change to the storytelling system:

1. keep the original judged V1 references unchanged;
2. write improvements as a new version;
3. run the six briefs without showing workers the references or expected routes;
4. judge dosage, truth, ownership, usefulness, and restraint;
5. turn each miss into a named fixture before making a repair;
6. allow one bounded repair replay;
7. leave unresolved behavior pending instead of widening the router or grading generously.

Run the local guard with:

```bash
python3 extractions/video-context/GlTA4wXSACE/a-tier-reference-corpus/verify_corpus.py --final
```

## What Is Still Unproven

- The references are local A-tier candidates, not yet human-recognized A-tier.
- The sales case is still pending because the repaired replay selected `FULL STORY` where the held-out target requires `STORY FRAGMENT`.
- The corpus proves local behavior, not audience response, conversion, reach, sales, or revenue.
- The hardened version is not active on `main` or in a global mirror until a separate Git/deployment decision is approved.
- No asset is automatically cleared for publication, client use, medical guidance, or external deployment.

## Recommended Default

For almost any storytelling or content request, start with `/shaan-story-deploy` rather than naming a deeper workflow. Let the system decide story dosage first. Name a specialized workflow directly only when you already know the job. Examples include signature-story banking, voice transfer, narrative-script repair, and a full sales journey.
