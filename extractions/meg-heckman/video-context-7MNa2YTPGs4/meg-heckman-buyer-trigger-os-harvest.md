# Meg Heckman Buyer-Trigger Apparel OS Harvest

## Summary

This harvest turns Meg Heckman's buyer psychology video into a cold, reusable Antigravity skill system for apparel, POD products, product design, offers, landing pages, and client creative.

The implementation keeps two layers:

- `skills/meg-heckman-buyer-trigger-os/` for the Meg-specific apparel/POD/product-design operating system.
- `semantic_libraries/antigravity/primitives/buyer-trigger-design-psychology.md` for cross-vertical reuse.

## Source Evidence

| Source | Status |
|---|---|
| URL | `https://www.youtube.com/watch?v=7MNa2YTPGs4` |
| Local package | `extractions/video-context/7MNa2YTPGs4/` |
| Canonical expert spelling | Meg Heckman |
| Alias preserved | Meg Hackman |
| Spoken evidence | 276 non-overlapping timestamped transcript segments |
| Frame evidence | 20 sampled frames; content not automatically described |
| OCR evidence | Unavailable |
| Claim boundary | Revenue and margin figures are source claims, not independently verified proof |

## Build Shape Decision

| Candidate Shape | Decision | Reason |
|---|---|---|
| Summary only | Rejected | User asked for deployable capability and cross-domain harness reuse. |
| Hot command | Rejected | The plan required a cold/on-demand skill, not a new front door. |
| New broad marketing expert | Rejected | Too broad; risks duplicate buyer-psychology sprawl. |
| Cold skill system | Accepted | Gives Meg a separate operating lane while staying source-grounded. |
| Cross-vertical primitive | Accepted | Lets other workflows reuse the mechanics without loading the whole skill. |

## Skill System Contract

| Field | Implementation |
|---|---|
| Source evidence | `extractions/video-context/7MNa2YTPGs4/video-context-ledger.md`, `metadata.json`, `uncertainty-report.md` |
| Objective | Turn Meg Heckman's POD buyer triggers into a reusable cold OS for identity-led product purchase intent. |
| Components | `meg-heckman-buyer-trigger-os`, `buyer-trigger-design-psychology.md`, Meg route card, Josh trigger pass, behavior proof examples. |
| Step order | source package -> route fit -> primitive -> cold skill -> workflows -> proof artifacts -> router/validator checks. |
| Inputs | Source URL/package, product or offer concept, target buyer, use context, constraints. |
| Outputs | Trigger Fit Table, concept revisions, scorecards, cross-vertical transfer maps, behavior proof. |
| Handoff summary | Pass source path, target buyer, candidate concept, and weakest trigger; do not pass full transcript dumps. |
| Composition rule | `/source-to-skill-system` owns; Meg supplies mechanics; creative-direction and Kallaway are optional lenses; proof gate decides readiness. |
| Human checkpoint | Required before hot command promotion, global mirror, publishing, paid generation, external writes, or real subagents. |
| Validation | Contract verifiers, skill validation, router/index checks, artifact guards, behavior proof. |
| Behavior-changing proof | Josh V1 trigger pass, MyBPM prompt upgrade, and non-apparel offer transfer below. |
| Result surface | Rendered conversation document plus local Markdown source and metadata sidecars. |
| Context policy | Keep skill cold; load source ledger/reference first; load only the workflow needed. |
| Reuse hook | Josh apparel, MyBPM, client creative, landing pages, offers, and product concepts needing fast purchase intent. |

## Trigger Fit Table: Proof Set

| Candidate | Target Buyer | Identity Signal | Recognition Speed | Specificity | Social Currency Moment | Familiar/Twist Pair | Emotion-First Reason | Risk | Revision |
|---|---|---|---|---|---|---|---|---|---|
| Commit On Eight | Swing dancer with software/developer overlap | "I commit to the count instead of floating." | Fast for 8-count dancers and developers. | Good, but still a little clean. | Friend says it is painfully you after watching them hesitate on the floor. | Git commit + 8-count phrase. | Confidence, timing, private competence. | Too subtle for non-developer dancers. | Add listing angle: "For the dancer who stops overthinking and sends the count." |
| No Drops In Prod | Social dancer/product/software person who values floor safety | "I am funny, responsible, and insider enough to know prod is sacred." | Fast for software people; medium for non-technical dancers. | Strong scene: social floor is production. | Someone laughs because it says the safety rule without scolding. | Dance drops + production environment. | Relief, superiority without cruelty, responsible insider humor. | `prod` may be opaque. | Make the product page carry the bridge: "Social floor is production. Test the chaos in rehearsal." |
| Push / Pull Request | Partner dancer with code-review fluency | "I understand connection as a protocol." | Medium; needs layout clarity. | Strong niche overlap, weaker outside it. | A dancer/developer sends it to the one friend who gets both layers. | Partner push-pull + pull request. | Delight at a precise overlap. | Can become too diagrammatic. | Use less tech diagram, more human line: "Connection is a protocol." |
| MyBPM Pulse Grid Tee | EDM streetwear buyer who treats nightlife as identity | "My body runs on the set, the crowd, and the pulse." | Medium; visual prompt is strong but emotionally broad. | Broad EDM/rave identity needs a more specific person. | Someone at a show recognizes the pulse-grid as post-set identity, not generic neon. | BPM data grid + after-hours body memory. | Belonging, body memory, modern rave nostalgia. | Current prompt leans aesthetic over buyer trigger. | Add a specific buyer scene and product text: "STILL SYNCED" / "MY.BPM 03:17 AM". |
| AI offer landing page | Founder/operator whose AI content gets attention but no buyer movement | "I am done mistaking AI output for buyer signal." | Fast if the headline names the private failure. | Specific scene: content shipped, no one bought. | Buyer shares because it names the hidden cost of AI slop. | AI productivity promise + buyer-signal correction. | Relief and urgency before proof. | Can drift into generic AI consulting. | Lead with "Your AI is producing. Your buyers are not moving." |

## Behavior Proof

### Josh V1

- **Input tested:** Existing Josh swing-nerd shirt candidates.
- **Weakness diagnosed:** Scorecard had insider clarity and wearability, but did not explicitly score future reaction, emotion-first purchase reason, or recognition speed.
- **Source mechanics used:** identity signal, instant recognition, specificity, social currency, familiar/twist, emotion-first justification.
- **Output produced:** `_active/josh-swing-nerd-shirts-v1/MEG_HECKMAN_TRIGGER_PASS.md`.
- **Behavior delta:** The launch package now judges whether each shirt creates a buyer-recognition moment, not only whether it is clever and wearable.
- **Validation run:** artifact guards and router checks.
- **Remaining risk:** Josh and real dancers still need to test live purchase/comment signals.

### MyBPM

- **Input tested:** `deliverables/designs/20260414_181005_mybpm_edm_streetwear_tee_with_prompt.json`.
- **Weakness diagnosed:** Strong visual aesthetic, but the buyer identity is broad EDM/rave culture rather than a specific person with a recognition moment.
- **Source mechanics used:** topic-to-person specificity, familiar/twist pairing, emotion-first reason.
- **Output produced:** upgraded prompt direction below.
- **Behavior delta:** Moves from "neon geometric EDM shirt" to "post-set body-memory streetwear signal."
- **Validation run:** included in this proof doc; no paid image generation run requested.
- **Remaining risk:** Needs a visual mockup and real EDM/streetwear buyer read.

#### MyBPM Prompt Upgrade

```text
Create a premium black streetwear T-shirt for MyBPM called "Still Synced". The buyer is the person leaving a 3:17 AM warehouse set whose body still feels locked to the kick pattern after the lights come up. Center the design around a precise pulse-grid graphic: thin electric-blue BPM lines, magenta phase-shift markers, and a subtle green heartbeat trace that feels like music data becoming body memory. Integrate small text: "MY.BPM" and "STILL SYNCED / 03:17 AM". The visual should feel like modern rave identity, not generic EDM decoration: restrained, wearable, high-contrast, and collectible. Use one main graphic system with enough negative space to look premium on a real shirt. Avoid DJ decks, crowd silhouettes, festival clichés, random neon chaos, and overcomplicated fractals.
```

### Cross-Vertical Offer Transfer

- **Input tested:** A generic AI service offer that says "we help businesses use AI."
- **Weakness diagnosed:** Broad category promise, no specific buyer scene, weak identity signal.
- **Source mechanics used:** specific person, instant recognition, emotion-first reason.
- **Output produced:** "Your AI is producing. Your buyers are not moving."
- **Behavior delta:** The offer now targets the founder who has output but no purchase intent, creating recognition before explanation.
- **Validation run:** included in cross-vertical primitive; no public copy gate run because this is internal proof.
- **Remaining risk:** Needs source-backed proof if used in public revenue copy.

## Composition Ledger

| Slot | Asset | Contribution Accepted | Evidence Of Change | Skipped/Rejected |
|---|---|---|---|---|
| Spine | `/source-to-skill-system` | Built a cold skill system and primitive, not a summary. | Skill system contract above. | Hot command rejected. |
| Differentiator | Meg Heckman source mechanics | Six buyer triggers became workflows and trigger table. | `skills/meg-heckman-buyer-trigger-os/` | Broad marketing persona rejected. |
| Mechanism | `/extraction-governor-agent` | Preserved source grounding and route-fit decision. | Source package + build shape table. | No unsupported visual claims. |
| Craft | `creative-direction` as optional lens | Apparel/POD outputs include print, wearability, and visual constraints. | Workflows and Josh pass. | No paid image generation. |
| Risk Gate | Behavior-changing extraction contract | Required Josh, MyBPM, and non-apparel proof. | Behavior proof section. | No claim of market validation. |

## Next Use

Use `skills/meg-heckman-buyer-trigger-os/workflows/buyer-trigger-audit.md` when a concept already exists, and `apparel-concept-generator.md` when starting from a niche.
