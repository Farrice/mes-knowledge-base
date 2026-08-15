# Keyword Sprint Portfolio Extension: Architecture Checkpoint

## Status

- Vision: `APPROVED` by Farrice on 2026-08-12.
- Architecture: `PENDING APPROVAL`.
- Implementation: `NOT STARTED`.
- Public or commercial activation: `NO PERMISSION`.
- Market-effect state: `UNTESTED`.

## Verdict

Extend the existing `/search-content-mastery` system with one typed
`SearchOpportunityPortfolio` record and a portfolio-linked `SearchBrief` V2
handoff. Preserve the existing Nathan Gotch skill, the frozen eleven-source
base corpus, every SearchBrief V1 fixture, and the current command front door.

No new expert, standalone keyword-research command, opaque scoring engine, or
universalized copy of Nathan Gotch's paid spreadsheet belongs in this build.

## Skill System Contract

| Field | Architecture decision |
|---|---|
| Source evidence | Existing canonical package for `vVJB2FjOF2k`; new native-caption and frame-backed package for `9CajZ7SJQ_w`; explicit uncertainty and source hashes |
| Objective | Turn a mixed keyword backlog into a provenance-preserving, human-approved, capacity-bounded sprint that can hand one selected opportunity to production |
| Components | Existing `/search-content-mastery`, Nathan workflow 16, Search Content Mastery audit/plan workflow, local runtime, two new schemas, source ledgers, and verifier fixtures |
| Step order | Validate project -> create portfolio -> inspect relationships and components -> approve sprint -> create linked brief -> use existing create/score/measure/service flow |
| Inputs | Valid project pack, one category, dated imports/observations, current URLs/positions when known, business relevance, capacity, and operator judgment |
| Outputs | `SearchOpportunityPortfolio`, selected/parked/rejected ledger, portfolio-linked `SearchBrief` V2, execution receipt, and behavior proof |
| Handoff summary | Pass portfolio ID/path, selected opportunity ID, source receipts, page-action rationale, proof gap, and next validation command |
| Human checkpoint | Required before portfolio approval, page-action commitment, production handoff, and any external or commercial action |
| Validation | Strict schemas, runtime positive and negative controls, V1 regression, corpus verification, skill/prompt/routing checks, and a realistic behavior-changing fixture |
| Behavior-changing proof | An unbounded overlapping list becomes one finite sprint; position does not auto-create pages; only one approved selected row reaches a brief |
| Result surface | Local JSON records plus a readable decision receipt inside the existing project pack |
| Context policy | Current portfolio and selected row hot; project truth and exact source receipts on demand; full transcripts and unrelated experts cold |
| Reuse hook | Reuse before SearchBrief planning for local, ecommerce, service, editorial, and search-everywhere projects |
| Goal packet | Not required; this build does not change self-improvement, cleanup, or evolution behavior |
| Agentic engineering packet | Not required; this build extends a domain runtime without new dependencies or control-plane behavior |

## Source Boundary

### Preserved primary

`vVJB2FjOF2k` remains governed by its existing canonical evidence package and
the frozen eleven-source corpus. It is not re-extracted or blended into a new
primary.

### Accepted source delta

`9CajZ7SJQ_w`, *The Complete SEO Keyword Research Masterclass for 2026*, is the
new source candidate. Its native captions and balanced visual capture establish
what Nathan said or showed. They cannot independently prove the effectiveness
of his formulas, Rankability, rankings, traffic, conversions, or revenue.

### Formula boundary

The source presents a creator-specific weighted spreadsheet and explicitly says
the weights are not exact science. The extension transfers the visible decision
components and human-review logic. It does not reconstruct or imply access to
the proprietary formula.

## Capability Delta

The current workflow 16 already owns provenance, current position, multiple
search surfaces, visible scoring dimensions, explicit opportunity classes, one
bounded cluster, and zero-volume hypothesis labeling. The new episode changes
behavior in four narrower places:

1. **Awareness-aware priority:** preserve awareness stage separately from
   search intent so commercial proximity can inform, but never automatically
   determine, priority.
2. **Page relationship diagnosis:** distinguish one primary topic, same-page
   variants, secondary candidates, and unmapped opportunities before choosing
   improve, consolidate, create, support, distribute, observe, or reject.
3. **Competition and effort visibility:** inspect domain, page, brand/AI,
   result-surface crowding, and content-production effort as separate evidence
   components.
4. **Finite sprint closure:** select a capacity-bounded 30-90-day portfolio and
   state what completion means instead of leaving an unlimited keyword backlog.

Source counts such as 10-20 and 25-50 are retained as creator heuristics, not
schema limits. Project capacity determines the selected count.

## Workflow Architecture

This is Extension Mode. The table preserves the existing five-workflow Nathan
portfolio and four-workflow companion OS rather than padding the build with new
slash commands.

| Tier | Workflow or component | State | Responsibility after the extension | Source contribution | Stacking partner |
|---|---|---|---|---|---|
| Tier 1: Foundation | Nathan 15: Search Intelligence Foundation | Preserved | Establish entity, brand, SME, import, competitor, and execution truth before research | First video remains the primary | SearchProjectManifest |
| Tier 1: Foundation | Nathan 16: Source-Labeled Search Opportunity Portfolio | **Expanded** | Create the awareness-aware, page-relationship-aware, finite sprint decision portfolio | Second video supplies the behavior delta | Search Content Mastery `portfolio` mode |
| Tier 1: Foundation | Search Content Mastery 02: Audit And Plan | **Expanded** | Validate the project, form the portfolio, require approval, and create a linked brief | System handoff inference | Nathan 16 plus SearchBrief V2 |
| Tier 2: Practitioner | Search Audit And Opportunity Map execution prompt | **Expanded** | Produce source/date rows, relationship diagnoses, visible components, and selected/parked/rejected sets | Second video plus existing corpus | Nathan 16; Ethan only for an actual AEO/GEO experiment |
| Tier 2: Practitioner | SearchOpportunityPortfolio runtime contract | **New component, not a new command front door** | Reject incomplete provenance, opaque scores, automatic position actions, invalid capacity, and invalid state sets | System implementation of source mechanics | Existing local project-pack runtime |
| Tier 2: Practitioner | Nathan 17: Search Content Production And Readiness | Preserved with typed input | Accept only the approved selected opportunity passed through SearchBrief V2 | No new production doctrine | `/create` and channel-native craft owner |
| Tier 3: Stacking | Nathan 18: Search-Everywhere Vertical Plan | Preserved | Consume approved portfolio rows when the chosen object belongs on local, ecommerce, video, third-party, commerce, or AI surfaces | Existing corpus remains sufficient | Relevant vertical route only |
| Tier 3: Stacking | Nathan 19: Search Measurement Integrity Review | Preserved | Keep predicted priority and later ranking, citation, traffic, conversion, and collection events separate | Existing measurement source remains primary | SearchEvent and human-reviewed learning |

Only Nathan 16, companion workflow 02, its prompt, schemas, and runtime receive
material behavior changes. Workflows 15 and 17-19 are preservation and handoff
surfaces, not new extractions.

## Connected System Flow

```text
SearchProjectManifest
        |
        v
audit + source/import evidence
        |
        v
SearchOpportunityPortfolio (DRAFT)
        |
        +-- provenance and unknown-field validation
        +-- human page-relationship and action judgment
        +-- explicit selected / parked / rejected sets
        |
        v
human approval
        |
        v
SearchOpportunityPortfolio (APPROVED)
        |
        v
plan --portfolio ... --opportunity-id ...
        |
        v
SearchBrief V2 with typed opportunity_ref
        |
        v
existing create -> score -> measure -> service flow
```

The runtime validates records and handoffs. It does not generate keyword ideas,
choose page actions, approve portfolios, forecast outcomes, or mutate workflows
from performance data.

## Record Contract: SearchOpportunityPortfolio V1

### Top-level fields

| Field | Requirement |
|---|---|
| `schema_version` | Constant `search-opportunity-portfolio/v1` |
| `record_type` | Constant `SearchOpportunityPortfolio` |
| `portfolio_id` | Runtime-generated stable record ID |
| `project_id` | Must match the validated project manifest |
| `created_at` | UTC ISO-8601 timestamp |
| `status` | `DRAFT`, `APPROVED`, or `REJECTED` |
| `category_cluster` | One named commercial category, service/location, or coherent topic family |
| `sprint` | Window, capacity basis, selected IDs, and completion definition |
| `source_receipts` | Non-empty dated evidence references used by the portfolio |
| `opportunities` | Non-empty strict opportunity records |
| `parked_opportunity_ids` | IDs explicitly deferred |
| `rejected_opportunity_ids` | IDs explicitly rejected |
| `proof_state` | `UNTESTED` or `RUNTIME_OBSERVED`; never a market-effect claim |
| `notes` | Optional operator context |

### Sprint object

| Field | Rule |
|---|---|
| `window_days` | Integer from 30 through 90 |
| `capacity_limit` | Positive project-specific integer; no creator count is hard-coded |
| `capacity_basis` | Required explanation of team, time, asset, or approval capacity |
| `selected_opportunity_ids` | Unique IDs, count no greater than capacity, empty only while `DRAFT` |
| `completion_definition` | Observable done condition for the sprint |

An `APPROVED` portfolio requires at least one selected opportunity. Selected,
parked, and rejected sets must be disjoint and must resolve to existing rows.

### Opportunity object

| Group | Required fields and behavior |
|---|---|
| Identity | `opportunity_id`, `query`, and exact `cluster` |
| Evidence | One or more dated `source_receipts`; unknown or fabricated mappings are rejected |
| Buyer state | `awareness_stage` and `intent` remain separate |
| Current state | `current_url`, `current_position`, and `position_bucket`; unknown is explicit |
| Topic relationship | `primary`, `same_page_variant`, `secondary_candidate`, `new_unmapped`, or `unknown` |
| Search surfaces | Traditional, local, video, third-party, commerce, and AI observations as relevant |
| Demand proxies | Named metric, value, source, observation date, and limitation |
| Priority components | Commercial value, business relevance, position upside, click opportunity, feasibility, content effort, brand/AI competition, and measurement readiness; each keeps rating, rationale, and evidence visible |
| Decision | One page/action class plus rationale and remaining proof gap |
| Measurement | A falsifiable hypothesis only for promoted opportunities |

### Awareness stages

`unaware`, `problem_aware`, `solution_aware`, `product_aware`, `most_aware`, or
`unknown`.

### Position buckets

`top_1`, `low_hanging_2_15`, `diagnostic_16_49`, `weak_50_plus`, `unranked`, or
`unknown`.

Buckets are diagnostic queues. They may not automatically create, refresh,
split, consolidate, or delete a page.

### Action classes

`improve`, `consolidate`, `create`, `support`, `distribute`, `observe`, or
`reject`.

An action requires an operator rationale. A `secondary_candidate` may suggest a
dedicated page, but poor rank alone never establishes permission to create it.

### Scoring law

- Component ratings are visible and separately evidenced.
- A final operator priority may be `HIGH`, `MEDIUM`, `LOW`, or `PARKED`.
- No required composite number exists.
- Inputs containing `composite_score`, `weighted_score`, hidden weights, or an
  automatic action derived only from position are rejected as unknown schema.
- CPC, volume, difficulty, result features, backlink metrics, and AI mentions
  remain proxies rather than outcomes.

## SearchBrief V2 Handoff

The existing SearchBrief V1 remains valid and unchanged.

Portfolio-linked planning creates `search-brief/v2`, which retains the V1
production contract and adds a required `opportunity_ref`:

- `portfolio_id`
- `portfolio_path`
- `opportunity_id`

The runtime must verify that:

1. the portfolio belongs to the same project;
2. the portfolio status is `APPROVED`;
3. the opportunity is in `selected_opportunity_ids`;
4. its action is not `observe` or `reject`;
5. the brief's `target_query` exactly matches the selected opportunity;
6. the portfolio path remains inside the portable project pack.

Legacy `plan --project ... --input ...` continues to create SearchBrief V1.
`plan --portfolio ... --opportunity-id ...` creates V2. Existing callers and
fixtures therefore require no migration.

## Runtime Surface

### New mode

```bash
python3 execution/search_content_mastery.py portfolio \
  --project <project-pack> \
  --input <strict-portfolio-input.json>
```

The command validates the project and input, writes
`portfolios/<portfolio-id>.json`, appends one execution event, and reports the
record path and status.

### Extended plan mode

```bash
python3 execution/search_content_mastery.py plan \
  --project <project-pack> \
  --portfolio <portfolio.json> \
  --opportunity-id <selected-id> \
  --input <strict-brief-input.json>
```

No external API, crawler, spreadsheet import, publishing, scheduler, connector,
or autonomous promotion is added.

## Corpus Versioning

The current `corpus-manifest.json` remains byte-preserved as the frozen
eleven-source base. The new episode is added as an append-only delta manifest:

`corpus-deltas/2026-08-12-9CajZ7SJQ_w.json`

The verifier will check:

- the exact frozen base IDs and hashes;
- the accepted delta manifest and evidence package;
- the active system contract's declaration of base plus delta;
- no duplicate source ID or canonical transcript;
- no creator/tool assertion promoted beyond its evidence label.

This avoids rewriting the earlier approval receipt while making the active
system aware of the new evidence.

## File Change Plan

### New evidence and contract files

- `extractions/video-context/9CajZ7SJQ_w/*`: canonical evidence package.
- `extractions/nathan-gotch-search-content-mastery/corpus-deltas/2026-08-12-9CajZ7SJQ_w.json`.
- `schemas/search-content-mastery/search-opportunity-portfolio.schema.json`.
- `schemas/search-content-mastery/search-brief-v2.schema.json`.
- Portfolio fixtures under `execution/fixtures/search-content-mastery/portfolios/`.

### Existing files extended in place

- `skills/nathan-gotch-ai-seo/workflows/16-source-labeled-opportunity-portfolio.md`.
- `skills/nathan-gotch-ai-seo/references/prompts-v2/36-source-labeled-opportunity-portfolio.md`.
- `skills/nathan-gotch-ai-seo/references/search-content-mastery-source-ledger.md`.
- `skills/search-content-mastery-os/SKILL.md`.
- `skills/search-content-mastery-os/workflows/02-audit-plan.md`.
- `skills/search-content-mastery-os/references/prompts-v2/search-audit-opportunity-map.md`.
- `skills/search-content-mastery-os/references/data-contract.md`.
- `.agent/workflows/search-content-mastery.md` and its existing parity wrappers.
- `execution/search_content_mastery.py`.
- `execution/verify_search_content_mastery.py`.
- `extractions/nathan-gotch-search-content-mastery/skill-system-contract.md`.
- `skills/search-content-mastery-os/references/source-ledger.md`.

No broad index regeneration is planned. Only an exact command description or
retrieval chunk is touched if a verifier proves it necessary.

## Validation Matrix

### Source integrity

1. Metadata, provenance, transcript, timed segments, analysis, uncertainty,
   visual ledger, and hashes exist and are non-empty.
2. Every extracted mechanic has a timestamp or visual receipt.
3. Self-reported performance and product claims remain `UNCONFIRMED`.
4. The frozen eleven-source manifest remains unchanged.

### Positive runtime controls

1. Valid local-service portfolio writes successfully.
2. Valid portfolio with mixed first-party and live observations preserves every
   source/date limitation.
3. An approved selected opportunity creates a linked SearchBrief V2.
4. Existing SearchBrief V1 planning still passes byte-compatible behavior.
5. Batch mode accepts `portfolio` before `plan` without permitting recursion.

### Known-bad controls

1. Missing source/date is rejected.
2. Unknown spreadsheet fields or hidden composite scores are rejected.
3. Position-only automatic page creation is rejected.
4. Selected, parked, and rejected ID overlap is rejected.
5. Selected count above declared capacity is rejected.
6. An approved portfolio with no selected opportunities is rejected.
7. A zero-volume idea stated as proven demand is rejected or held as a
   hypothesis.
8. A portfolio from another project is rejected.
9. An unapproved, observed, rejected, or unselected opportunity cannot create a
   SearchBrief V2.
10. A brief query that differs from the selected row is rejected.

### Behavior proof

Input: an unbounded mixed list containing overlapping terms, an existing
position 2-15 page, a weakly ranked secondary topic, a zero-volume first-party
question, and an AI-recommended competitor.

Expected delta:

- synonyms are not automatically assigned separate pages;
- the existing page becomes an improvement review, not an automatic rewrite;
- the secondary topic receives a page-split diagnosis with a proof gap;
- the zero-volume item remains a dated hypothesis;
- brand/AI competition and content effort remain visible;
- one capacity-bounded sprint is selected;
- only a human-approved selected row can become a SearchBrief.

### Regression and proof boundaries

- Existing corpus, V1 brief, import, score, measurement, service, routing,
  skill, command parity, and three cold-start checks remain green.
- Runtime proof may reach `RUNTIME_OBSERVED`.
- Human recognition, ranking impact, citation impact, traffic, conversions,
  collected revenue, and product performance remain `UNTESTED`.

## Preservation Locks

1. `corpus-manifest.json` and the first-video evidence package stay unchanged.
2. SearchBrief V1 remains valid and keeps its current meaning.
3. New experts, command front doors, dependencies, external APIs, and paid tools
   are outside scope.
4. Position buckets remain diagnostic; they never trigger page actions.
5. Proprietary weights and claims of formula equivalence are excluded.
6. Portfolio learning cannot auto-promote into skills or routing.
7. Health Performance, offer canon, and unrelated project packs are excluded.
8. Publishing, deployment, push, merge, and external writes remain unauthorized.

## Implementation Sequence After Approval

1. Build and verify the source evidence package and append-only corpus delta.
2. Define schemas and strict runtime validators.
3. Implement `portfolio` and portfolio-linked V2 planning without changing V1.
4. Extend the Nathan workflow and the conductor prompt by reference.
5. Create positive and known-bad fixtures.
6. Run targeted tests, then the full Search Content Mastery verifier, skill
   audits, prompt gates, routing regression, and export-format guard.
7. Produce a behavior-changing proof and stop for Verified Runtime Review.

## Architecture Approval Gate

Implementation may begin only after Farrice explicitly approves this
architecture. Approval authorizes local reversible changes in the isolated
Codex worktree only. It does not authorize external activation, push, merge,
publication, paid tools, or claims of market effect.
