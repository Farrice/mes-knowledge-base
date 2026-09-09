# Skill System Contract — Jun Yuh Story Engine

## Contract

| Field | Decision |
|---|---|
| Source evidence | `https://www.youtube.com/watch?v=XS-E6rnCr5U`; canonical local package in this directory; transcript-only evidence; 4,083 timestamped spoken rows and 28,477 clean words. |
| Objective | Turn supplied lived moments into truth-safe story material, then route that material into social formats or the correct universal story owner. |
| Components | Existing `jun-yuh` agent; `jun-yuh-creator-vision`; new Story Material Miner, Story Format Router, and Jun Story Engine workflows; `/jun-story-engine` command bridge; existing `/shaan-story-deploy`; dedicated verifier and fixtures. |
| Step order | source/fact intake → story-existence sniff → LIFE retrieval → Safe/Real/Raw interview → 3P viability → privacy/truth gate → mission → social format or Shaan handoff → output/receipt. |
| Inputs | Objective, supplied lived facts or source path, share boundary, audience relationship, domain/truth risk, destination when known, and voice owner when applicable. |
| Outputs | Story Material Packet; either a Social Story Plan/final social asset or a compact Shaan Story Material Handoff; Story Engine Receipt. |
| Handoff summary | Pass facts, LIFE domain, Safe/Real/Raw answers, 3P candidates, missing beats, privacy exclusions, mission, destination, and one open risk—not the full transcript. |
| Composition rule | Jun owns material mining and social format placement. Shaan owns cross-domain narrative dosage. A downstream domain/format expert owns the body when Jun social content is not selected. Kallaway is optional post-draft audit only. |
| Human checkpoint | Already satisfied for local reversible build. Required before publication, global mirror/plugin promotion, external write, use of private third-party material, or a claim that the system is market-proven. |
| Validation | Source-package verifier; dedicated Jun Story Engine verifier with positive/negative fixtures; skill validation; prompt audit/build/wiring; command/workflow discoverability; cold-start proof; anti-slop and export guards for written artifacts. |
| Behavior-changing proof | One constructed health-performance founder case must move from generic teaching to a supported story asset; one incident-status negative control must remain `NO STORY`; one sensitive-event case must preserve privacy and avoid invented details. |
| Result surface | `/jun-story-engine` plus persistent source, contract, proof, and guide artifacts. |
| Context policy | Hot: command wrapper, compact Jun engine, Shaan dosage map. On demand: one Jun component, one format prompt, or one downstream owner. Cold: full transcript, unused Jun workflows, Kallaway, and all non-selected experts. |
| Reuse hook | Use `/jun-story-engine` when the operator has raw lived material or “nothing interesting to say”; use `/shaan-story-deploy` directly when story material and objective already exist. |
| Goal packet | Required and completed below because existing skills, prompts, routing, and command surfaces change. |
| Agentic engineering packet | Required and completed below because context policy, source-truth handoffs, and use-now routing change. |

## Dependency Rules

1. Jun may ask for meaning but may not supply a real person's memory, feeling, motive, dialogue, chronology, or transformation.
2. If `RAW` is unknown, declined, or unsafe, continue with `SAFE` or `REAL`; never pressure toward trauma.
3. A `FULL STORY` handoff needs supported Problem, Pursuit, and Payoff plus Shaan's want/obstacle/change/turn test.
4. A missing Pursuit downgrades the material; it does not authorize a fabricated method.
5. Social formats are adapters. They may not override the mission, truth boundary, or dosage.
6. Emotion-matched footage is labeled illustrative and may not imply it depicts the historical event.
7. Non-social deployment goes to Shaan before a body-writing owner is selected.
8. One body owner per run.

## Goal Packet

| Field | Decision |
|---|---|
| `target` | `jun-yuh-creator-vision`, Jun agent/command surface, and the bounded upstream handoff in Shaan's deployment map. |
| `scope` | Add three workflows, three v2 prompts, one source ledger, one command bridge, fixtures, verifier, and documentation. Exclude broad router rewrites, global mirrors, plugins, publishing, and unrelated storytelling skills. |
| `per_item_criteria` | Every new item must cite the source package, preserve one-owner composition, permit `NO STORY`, and pass the dedicated verifier. |
| `permitted_side_effect` | Local reversible edits inside `codex/jun-yuh-story-system`. |
| `proof_artifact` | `behavior-proof.md`, `fixtures/story-engine-cases.json`, and `execution/verify_jun_story_engine.py` output. |
| `measurable_stop` | All positive and negative fixtures pass; source, skill, prompt, bridge, and router checks pass; no unexplained tracked changes remain. |
| `turn_cap` | Two repair passes after the first verifier run. |
| `evaluator` | Dedicated stdlib verifier plus existing skill/prompt/router checks and a manual source-boundary review. |
| `wake_up_check` | `python3 execution/verify_jun_story_engine.py` from the lane root. |
| `human_checkpoint` | Satisfied for this local build by Farrice's explicit request; external/global/publishing changes remain gated. |
| `rollback_or_archive_rule` | Keep changes isolated on `codex/jun-yuh-story-system`; if proof fails after two repairs, leave the branch parked and report PARTIAL. Never delete existing Jun/Shaan behavior. |

## Agentic Engineering Packet

| Field | Decision |
|---|---|
| Objective | Make story mining usable from a cold start without loading the full masterclass or every storytelling expert. |
| Source truth | This video-context package; current Jun skills and agent; Shaan Story Deployment Map; Skill System, Behavior-Changing Extraction, Goal-Loop, and How I Write contracts. |
| Context plan | Hot command and compact router; load one component at a time; full transcript and adjacent experts remain cold. |
| Work chunks | source package → extraction/contract → Jun components → Shaan handoff → prompts/bridges → fixtures/verifier → behavior proof. |
| Review loop | Dedicated verifier; two repair passes; failure parks the branch rather than widening scope. |
| Dependency gate | No new package, plugin, API, or external automation. Watch/yt-dlp were existing trusted tools and native captions were used. |
| Structure pass | Search for duplicated ownership, stale counts, broken prompt pointers, and hidden transcript dependence. |
| Use-now artifact | `/jun-story-engine` with a cold-start prompt and Story Material Packet. |
| Hardening proof | Positive transform, privacy case, `NO STORY` negative control, router discovery, skill validation, and prompt audit. |

## Evolution Council Verdict

- **Target:** existing Jun storytelling capability and its upstream connection to Shaan.
- **Goal packet complete:** yes.
- **Recommended path:** bounded skill evolution in an isolated lane.
- **Permitted side effect:** additive local workflows, prompts, command bridge, source references, and verifier; one bounded Shaan handoff edit.
- **Proof artifact:** dedicated fixtures, verifier, and behavior proof.
- **Stop condition:** stated Goal Packet stop passes or the branch parks after two repair attempts.
- **No-regression check:** existing Jun skill validation and Shaan story deployment truth/dosage language remain present.
- **Human checkpoint:** satisfied for local work; global/external promotion remains blocked.
- **Open risk:** transcript-only evidence cannot certify exact visual execution; source-reported performance remains unverified.
