# NotebookLM Practitioner Prompt Suite

This pack turns any NotebookLM notebook into a source-grounded production workspace for research, decisions, slides, infographics, reports, audio/video overviews, data tables, and output QA.

Use it in three passes:

1. Run a Source Control prompt before you create anything important.
2. Run an Evidence Extraction or Synthesis prompt to build the working material.
3. Run a Quality Control prompt before you trust, share, export, or publish the result.

The core rule: selected sources first, evidence before synthesis, claim-level citations where NotebookLM can provide them, and clear fallback language when a feature is account-tier, device, age, language, source-limit, or quota constrained.

## Start Here

Use this prompt pack as an operating system, not a list of one-off prompts. Pick one route, run the source boundary first, then move through extraction, synthesis, production, and QA.

| Job | Minimum prompt chain | Best NotebookLM surface |
|---|---|---|
| Raw context, unclear output | NLM-AUTO-01 -> NLM-AUTO-03 -> chosen lane prompt | Chat, saved note |
| Uploaded brand, ICP, offer, or creative assets | NLM-AUTO-02 -> NLM-AUTO-08 -> chosen Studio prompt | Chat, saved note, Studio |
| Best-asset recommendation | NLM-AUTO-04 -> NLM-AUTO-05 -> NLM-QC-08 | Chat, Studio |
| Serious research answer | NLM-SOURCE-02 -> NLM-EXTRACT-01 -> NLM-SYNTH-05 -> NLM-QC-01 | Chat, saved note |
| Strategy recommendation | NLM-SOURCE-01 -> NLM-EXTRACT-04 -> NLM-SYNTH-04 -> NLM-QC-04 | Chat, saved note |
| Slide deck | NLM-SOURCE-02 -> NLM-VISUAL-01 -> NLM-VISUAL-02 -> NLM-VISUAL-03 -> NLM-QC-08 | Chat, Studio Slide Deck |
| Infographic | NLM-EXTRACT-06 -> NLM-VISUAL-04 -> NLM-VISUAL-05 -> NLM-QC-03 | Chat, Studio Infographic |
| Data table or chart | NLM-EXTRACT-06 -> NLM-VISUAL-06 -> NLM-QC-01 -> NLM-QC-02 | Chat, Ultra chat if available |
| Audio or video overview | NLM-SOURCE-03 -> NLM-VISUAL-07 or NLM-VISUAL-08 -> NLM-QC-03 | Studio Audio or Video Overview |

## Prompt Index

This pack contains 50 reusable prompts: 8 Autopilot Intake launchers plus 42 prompt cards across six production lanes.

| Lane | Prompt cards | Use this lane when |
|---|---:|---|
| Autopilot Intake | 8 | You have raw intent, uploaded brand/ICP/offer context, or a rough creative direction and need NotebookLM to infer the brief. |
| Source Control | 6 | You need scope, gaps, selected-source boundaries, source quality, or research expansion rules. |
| Evidence Extraction | 6 | You need claims, quotes, frameworks, contradictions, examples, numbers, or source rows. |
| Synthesis | 6 | You need a brief, insight map, point of view, decision matrix, memo, or audience translation. |
| Transformation | 6 | You need to turn source evidence into reports, outlines, client briefs, learning guides, workflows, or new prompts. |
| Visual Production | 10 | You need slides, infographics, charts, audio, video, style direction, or Ultra downloadable artifacts. |
| Quality Control | 8 | You need citation checks, unsupported-claim removal, visual QA, contradiction preservation, risk review, or final export checks. |

## Production Standard

The pack is built to force four practitioner habits:

1. Source boundary before output.
2. Evidence ledger before recommendation.
3. Storyboard before visual generation.
4. QA pass before sharing, exporting, or publishing.

Any output that skips those habits should be treated as a draft, not a finished result.

## Raw Intent Mode

Use Raw Intent Mode when you do not know the perfect fields yet. Paste rough thoughts, uploaded-context notes, or a loose request. NotebookLM should infer the missing fields from selected sources, mark assumptions, and only ask one question if the missing answer would change the output.

### Minimal Raw Intent Interface

Use this instead of the full interface when you want room to think:

| Field | Meaning |
|---|---|
| `{raw_intent}` | What you are trying to do, even if it is messy. |
| `{selected_sources}` | The source titles, labels, or source group currently checked. |
| `{known_output_or_asset}` | Optional: slide deck, infographic, audio, video, report, table, quiz, content, strategy, or "not sure". |
| `{context_assets}` | Optional: ICP, offer, brand guide, creative book, content library, strategy docs, testimonials, notes, transcripts, or examples already uploaded. |
| `{what_good_feels_like}` | Optional: examples, taste notes, vibe, quality bar, or outcome you would be happy with. |
| `{hard_constraints}` | Optional: things that must be included, avoided, protected, or made easy. |

### Blank Field Rule

Add this when you leave fields blank:

```text
If I leave a field blank, infer it from the selected sources and raw intent. Mark each inferred field as "inferred". Mark each source-backed field as "source-backed". Ask at most one clarifying question only if the missing field would materially change the output. Otherwise proceed with stated assumptions.
```

## Default Prompt Interface

Use these fields in every prompt. Replace anything in braces before pasting into NotebookLM.

| Field | Meaning |
|---|---|
| `{notebook_goal}` | The job this notebook supports. |
| `{selected_sources}` | Source titles or source group checked in the Sources panel. |
| `{artifact_type}` | The target output, such as report, slide deck, infographic, audio, video, table, quiz, or decision brief. |
| `{audience}` | Who will use the output. |
| `{decision_or_use_case}` | The decision, task, or content job this output must support. |
| `{depth}` | Concise, standard, detailed, or expert. |
| `{output_language}` | Desired output language. |
| `{format}` | Table, memo, checklist, outline, deck storyboard, Studio prompt, etc. |
| `{tone}` | Direct, executive, instructional, creative, critical, friendly, technical, etc. |
| `{constraints}` | Time, length, brand, source, risk, chart, export, or publishing constraints. |
| `{tier_or_device_limits}` | Free, Plus, Pro, Ultra, Workspace, mobile-only, desktop-only, under-18, English-only, etc. |
| `{unknowns_policy}` | Default: If the selected sources do not support an answer, say `Not found in the selected sources`. |

### Universal Anti-Slop Clause

Add this to any prompt that matters:

```text
Use only the selected sources: {selected_sources}. Cite source-backed factual claims where NotebookLM can provide citations. Separate direct source evidence from interpretation. If a claim is not established in the selected sources, label it as not established or remove it. Preserve contradictions instead of smoothing them into a false consensus. Avoid generic advice unless a selected source explicitly supports it.
```

## Autopilot Intake Layer

These prompts are for the way you actually work: rough intent first, uploaded context doing the heavy lifting, then a clean prompt or Studio asset brief.

### NLM-AUTO-01 Raw Intent Router

Best surface: Chat

Use when: You have a rough idea but do not know the exact output fields yet.

Prompt:

```text
I am giving you raw intent, not a polished brief.

<raw_intent>
{raw_intent}
</raw_intent>

Selected sources: {selected_sources}
Known output or asset, if any: {known_output_or_asset}
Context assets uploaded: {context_assets}
What good feels like: {what_good_feels_like}
Hard constraints: {hard_constraints}

Use only the selected sources unless I explicitly ask for source discovery.

Infer the working brief:
- notebook_goal
- likely audience
- artifact_type
- decision_or_use_case
- depth
- tone
- format
- constraints
- unknowns_policy

For each field, label it as source-backed, inferred, or missing.

Then recommend the best next prompt from this suite and explain why in one short paragraph.

Ask at most one clarifying question only if the answer would change the artifact type or audience. Otherwise proceed with stated assumptions.
```

Expected output: Filled working brief plus the next prompt to run.

Failure modes: Over-asks questions, treats inferred fields as facts, or ignores uploaded context.

QA check: Every field is labeled source-backed, inferred, or missing.

### NLM-AUTO-02 Notebook Profile Extractor

Best surface: Chat, saved note

Use when: You uploaded ICPs, brand notes, offer docs, creative books, content, or business context.

Prompt:

```text
Build a reusable Notebook Profile from the selected sources.

Selected sources: {selected_sources}
Context assets uploaded: {context_assets}
Raw intent: {raw_intent}

Extract only what the selected sources support.

Return:
- Brand or business summary
- Offer or product summary
- ICP and buyer segments
- Audience pains, desires, objections, beliefs, and triggers
- Voice, tone, phrases, and banned language if present
- Creative patterns already used
- Proof assets and credibility markers
- Gaps that are not established
- Suggested source labels for easier future use

End with a compact "Notebook Profile Note" I can save as a note and reselect as context later.
```

Expected output: Source-grounded profile and saveable note.

Failure modes: Invents brand strategy or fills business gaps from general knowledge.

QA check: The output separates "source-backed" from "not established".

### NLM-AUTO-03 Missing Field Autocomplete

Best surface: Chat

Use when: A prompt asks for audience, tone, format, or constraints and you do not want to manually fill them.

Prompt:

```text
Autocomplete the prompt fields for this job.

Raw intent: {raw_intent}
Selected sources: {selected_sources}
Known output or asset: {known_output_or_asset}
Context assets uploaded: {context_assets}

Fill these fields using the selected sources first and inference second:
- notebook_goal
- selected_sources
- artifact_type
- audience
- decision_or_use_case
- depth
- output_language
- format
- tone
- constraints
- tier_or_device_limits
- unknowns_policy

Use a table with columns:
Field | Filled value | Basis: source-backed, inferred, user-provided, or missing | Confidence 1-5 | Risk if wrong

Then produce a copy-paste version of the completed prompt interface.
```

Expected output: Field table and completed prompt interface.

Failure modes: Treats every field as equally certain.

QA check: The "Risk if wrong" column makes weak assumptions visible.

### NLM-AUTO-04 Studio Asset Recommender

Best surface: Chat

Use when: You want NotebookLM to choose whether the source context should become slides, an infographic, audio, video, report, data table, mind map, flashcards, or quiz.

Prompt:

```text
Recommend the best Studio assets to create from this notebook.

Raw intent: {raw_intent}
Selected sources: {selected_sources}
Context assets uploaded: {context_assets}
Known output or asset: {known_output_or_asset}
Use case: {decision_or_use_case}

Rank these asset options:
- Slide Deck
- Infographic
- Audio Overview
- Video Overview
- Report
- Data Table
- Mind Map
- Flashcards
- Quiz

For each option, return:
- Fit score from 1 to 5
- Best use
- What source evidence it needs
- What it would probably get wrong
- Whether it should be generated now, later, or skipped

Then recommend one primary asset and two support assets.
```

Expected output: Ranked Studio asset plan.

Failure modes: Recommends every asset instead of making tradeoffs.

QA check: At least one asset is marked "skip" or "later".

### NLM-AUTO-05 Studio Custom Prompt Generator

Best surface: Chat before Studio

Use when: You need a clean custom prompt to paste into a NotebookLM Studio asset.

Prompt:

```text
Create a custom Studio prompt from my raw intent.

Raw intent: {raw_intent}
Selected sources: {selected_sources}
Context assets uploaded: {context_assets}
Target Studio asset: {known_output_or_asset}
What good feels like: {what_good_feels_like}
Hard constraints: {hard_constraints}

If the target asset is "not sure", choose the best Studio asset first and explain the choice.

Then produce:
1. The filled working brief.
2. A copy-paste custom prompt for the selected Studio asset.
3. A shorter fallback prompt for mobile or limited controls.
4. A QA prompt to run after the asset is generated.

The Studio prompt must include:
- selected-source scope
- inferred audience and use case
- output mode or format
- visual or narrative direction if relevant
- citation or source-grounding expectations where available
- what to exclude
- what to do if evidence is missing
```

Expected output: Ready-to-paste Studio custom prompt plus QA prompt.

Failure modes: Produces a generic prompt that ignores the notebook profile.

QA check: The custom prompt names the selected sources and excludes unsupported claims.

### NLM-AUTO-06 Existing Content Reframer

Best surface: Chat, Studio

Use when: You upload your own content and want it turned into better assets without losing your thinking.

Prompt:

```text
Reframe my existing content into a stronger {artifact_type}.

Selected sources: {selected_sources}
Raw intent: {raw_intent}
Context assets uploaded: {context_assets}
Target asset: {known_output_or_asset}
What good feels like: {what_good_feels_like}

Treat the uploaded content as the primary source of voice, positioning, examples, and intent.

Return:
- Core thesis from my content
- Best supporting ideas
- Best examples or proof
- Phrases worth preserving
- Ideas that are unclear or unsupported
- Recommended asset format
- Copy-paste Studio prompt for the chosen asset

Do not make the content more generic. Preserve the strongest original distinctions and remove only repetition, confusion, or unsupported claims.
```

Expected output: Reframing brief and Studio prompt.

Failure modes: Polishes away the user's point of view.

QA check: The output includes phrases worth preserving.

### NLM-AUTO-07 Multi-Asset Studio Bundle

Best surface: Chat before Studio

Use when: You want one notebook to become a package of Studio assets.

Prompt:

```text
Turn this notebook into a coordinated Studio asset bundle.

Raw intent: {raw_intent}
Selected sources: {selected_sources}
Context assets uploaded: {context_assets}
Primary use case: {decision_or_use_case}
What good feels like: {what_good_feels_like}
Hard constraints: {hard_constraints}

Create a bundle plan with:
- Primary asset
- Support asset 1
- Support asset 2
- Optional learning asset
- Optional data asset
- Asset order
- Reused evidence spine
- What each asset should NOT repeat

Then write custom Studio prompts for:
- Slide Deck
- Infographic
- Audio Overview
- Video Overview
- Report
- Data Table
- Flashcards or Quiz

If an asset is a poor fit, say why and provide a skip note instead of forcing it.
```

Expected output: Multi-asset plan plus custom prompts.

Failure modes: Makes every asset say the same thing.

QA check: Each asset has a different job and a shared evidence spine.

### NLM-AUTO-08 Notebook Profile Note Builder

Best surface: Chat, saved note

Use when: You want the notebook to remember your brand, ICP, offer, and taste for later prompts.

Prompt:

```text
Create a compact Notebook Profile Note I can save and reuse.

Selected sources: {selected_sources}
Context assets uploaded: {context_assets}
Raw intent: {raw_intent}

Only include details supported by selected sources. Use short sections:
- Brand/business
- Offer
- ICP
- Audience beliefs and objections
- Voice and taste
- Creative patterns
- Proof and credibility
- Constraints
- Open questions

Then add:
- "How to use this note" with 3 instructions
- "What this note does not prove"
- "Best Studio assets for this notebook"

Keep it concise enough to save as a note and select later as context.
```

Expected output: Saveable profile note.

Failure modes: Turns the profile into strategy advice instead of reusable context.

QA check: Includes "What this note does not prove".

## Lane 1: Source Control

### NLM-SOURCE-01 Coverage Audit

Best surface: Chat

Use when: You need to know whether the notebook is ready for a serious output.

Prompt:

```text
Audit the selected sources for {notebook_goal}.

Selected sources: {selected_sources}
Target artifact: {artifact_type}
Audience: {audience}
Use case: {decision_or_use_case}
Unknowns policy: {unknowns_policy}

Return a table with:
- Source name
- What this source contributes
- Key topics covered
- Gaps or missing context
- Duplicated material
- Contradictions or tension with other sources
- Readiness score from 1 to 5 for creating {artifact_type}

Then give a short verdict: ready, usable with caveats, or not ready.
```

Expected output: Source readiness table plus a go/no-go verdict.

Failure modes: Treats all sources as equal, ignores missing context, or gives a generic "looks good" answer.

QA check: The output names at least one concrete gap, caveat, or reason the notebook is ready.

### NLM-SOURCE-02 Selected-Source Boundary

Best surface: Chat

Use when: You need to make sure only checked sources influence the answer.

Prompt:

```text
Before answering, confirm the working source boundary.

Use only these selected sources: {selected_sources}
Do not use unselected sources, general knowledge, or assumptions.

For {notebook_goal}, list:
1. The selected sources you will rely on.
2. The topics these sources can answer well.
3. The topics these sources cannot answer well.
4. Any source you suspect is missing.

End with this sentence exactly:
"I will treat anything outside the selected sources as not established."
```

Expected output: Source boundary statement.

Failure modes: Adds external claims or skips the not-established commitment.

QA check: The last sentence appears exactly.

### NLM-SOURCE-03 Missing Evidence Finder

Best surface: Chat

Use when: You have an intended deliverable but suspect the sources are thin.

Prompt:

```text
Find what is missing before I create {artifact_type}.

Notebook goal: {notebook_goal}
Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Constraints: {constraints}

Return:
- What the sources prove strongly
- What they suggest weakly
- What they do not establish
- What must be verified before sharing or publishing
- 5 specific source additions that would improve the notebook

Use citations for factual claims where available. Do not invent missing facts.
```

Expected output: Gap report.

Failure modes: Treats weak evidence as proven.

QA check: Has a "do not establish" section with real limits.

### NLM-SOURCE-04 Source Quality Triage

Best surface: Chat or Data Table

Use when: Your notebook includes mixed source types such as PDFs, transcripts, web pages, images, and notes.

Prompt:

```text
Score the selected sources for production use.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Target output: {artifact_type}

Create a table with:
- Source name
- Source type
- Recency or date if visible
- Directness to the goal
- Evidence strength from 1 to 5
- Likely bias or limitation
- Best use in the final output
- Avoid using it for

After the table, recommend the 3-7 sources to rely on most for {artifact_type}.
```

Expected output: Source quality table.

Failure modes: Recency or source type is guessed without support.

QA check: Each source has an "avoid using it for" field.

### NLM-SOURCE-05 Research Expansion Query Builder

Best surface: Chat, Fast Research, Deep Research where available

Use when: You need better sources before generating a high-stakes output.

Prompt:

```text
Design a source expansion plan for this notebook.

Notebook goal: {notebook_goal}
Current selected sources: {selected_sources}
Target artifact: {artifact_type}
Audience: {audience}
Use case: {decision_or_use_case}
Tier/device limits: {tier_or_device_limits}

Return:
- The current source weakness in one paragraph
- 8 high-density search queries for NotebookLM Fast Research or Deep Research
- What each query is meant to find
- Accept/reject criteria for sources
- Which searches are optional if quotas are limited

Do not run research in this answer. Give me the search plan.
```

Expected output: Search plan with query intent.

Failure modes: Broad search phrases that produce generic sources.

QA check: Every query includes a reason and source filter.

### NLM-SOURCE-06 Notebook Configuration Brief

Best surface: Chat, Configure Chat

Use when: You want a custom notebook behavior that stays consistent across future prompts.

Prompt:

```text
Create a NotebookLM Configure Chat instruction set for this notebook.

Notebook purpose: {notebook_goal}
Primary user: {audience}
Common tasks: {decision_or_use_case}
Selected sources: {selected_sources}
Tone: {tone}
Constraints: {constraints}

The configuration must tell NotebookLM to:
- Use selected sources first
- Separate source-backed claims from interpretation
- Surface contradictions
- Say when something is not found in sources
- Keep outputs practical and non-generic

Return:
1. Recommended chat style: Default, Learning Guide, or Custom
2. Copy-paste custom instructions
3. 5 testing queries to verify the behavior
4. Signs the configuration is failing
```

Expected output: Custom instruction block.

Failure modes: Creates a persona that overreaches beyond sources.

QA check: Includes testing queries.

## Lane 2: Evidence Extraction

### NLM-EXTRACT-01 Claim Ledger

Best surface: Chat or Data Table

Use when: You need the notebook's important claims in a verifiable form.

Prompt:

```text
Extract the 20 most important claims for {notebook_goal}.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Depth: {depth}

Return a table with:
- Claim
- Source citation where available
- Source name
- What the claim proves
- Confidence from 1 to 5
- Caveat or limitation
- Agreement status: supported by multiple sources, single-source only, contradicted, or unclear

Do not include claims that are not present in selected sources.
```

Expected output: Evidence table.

Failure modes: Claims appear without source support.

QA check: Every row has a caveat or agreement status.

### NLM-EXTRACT-02 Quote and Proof Bank

Best surface: Chat, Notes

Use when: You need quotable support for a report, content piece, deck, or brief.

Prompt:

```text
Build a proof bank for {artifact_type}.

Selected sources: {selected_sources}
Notebook goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}

Return:
- 12-20 strong source-backed points
- The citation or source location where available
- A short explanation of what each point proves
- Best use: slide, report, infographic, audio, video, or decision memo
- Risk if used out of context

Prefer precise source evidence over broad summaries.
```

Expected output: Reusable proof bank.

Failure modes: Pulls broad paraphrases with no proof value.

QA check: Every item states what it proves.

### NLM-EXTRACT-03 Framework Reconstruction

Best surface: Chat

Use when: The sources contain a system, method, playbook, or operating logic.

Prompt:

```text
Reconstruct the operating system inside the selected sources. Do not summarize.

Selected sources: {selected_sources}
Notebook goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}

Return:
1. The named or implied framework
2. Step-by-step mechanics
3. Inputs required
4. Decisions the user must make
5. Outputs produced
6. Quality criteria
7. Failure modes
8. What the sources do not explain

Use citations where available. If a step is inferred rather than directly stated, label it "inference."
```

Expected output: Operational reconstruction.

Failure modes: Summarizes themes instead of mechanics.

QA check: Includes inputs, decisions, outputs, and failure modes.

### NLM-EXTRACT-04 Contradiction Map

Best surface: Chat, Data Table

Use when: You have multiple sources with tension or different recommendations.

Prompt:

```text
Find contradictions, tension, and unresolved disagreements across the selected sources.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Use case: {decision_or_use_case}

Return a table with:
- Issue
- Source A position
- Source B position
- Evidence or citation for each side
- Why the disagreement matters
- Whether source recency, authority, data quality, or directness helps resolve it
- Recommended handling: preserve tension, resolve with caveat, or research further

Do not force consensus.
```

Expected output: Contradiction table.

Failure modes: Blends disagreement into a bland middle.

QA check: At least one row preserves tension if real tension exists.

### NLM-EXTRACT-05 Example Miner

Best surface: Chat

Use when: You need concrete examples for slides, teaching, or content.

Prompt:

```text
Mine the selected sources for examples that make {notebook_goal} concrete.

Selected sources: {selected_sources}
Audience: {audience}
Artifact: {artifact_type}

Return:
- Example
- Source citation where available
- What concept it illustrates
- Why this example will matter to {audience}
- Best output fit: slide, report, infographic, audio, video, quiz, or memo
- Rewrite risk: what must not be changed if I adapt it

Prefer vivid, specific examples over broad categories.
```

Expected output: Example bank.

Failure modes: Examples become generic categories.

QA check: Each example has a "rewrite risk."

### NLM-EXTRACT-06 Data and Number Ledger

Best surface: Data Table, Chat

Use when: Numbers, charts, comparisons, or performance claims are involved.

Prompt:

```text
Extract every number, metric, date, percentage, count, benchmark, or comparison relevant to {notebook_goal}.

Selected sources: {selected_sources}
Target artifact: {artifact_type}
Use case: {decision_or_use_case}

Return a table with:
- Number or metric
- Exact wording around it if available
- Source and citation
- Unit
- Time period
- Denominator or sample if present
- What it supports
- What it does not prove
- Whether it is safe for a chart

Do not calculate new values unless the source provides enough data. If calculating, show the formula.
```

Expected output: Numeric evidence table.

Failure modes: Numbers are copied without units or denominator.

QA check: Every numeric row has a "what it does not prove" field.

## Lane 3: Synthesis

### NLM-SYNTH-01 Executive Brief

Best surface: Chat, Report

Use when: You need a source-grounded brief for a decision maker.

Prompt:

```text
Create an executive brief for {decision_or_use_case}.

Selected sources: {selected_sources}
Audience: {audience}
Depth: {depth}
Tone: {tone}
Constraints: {constraints}
Unknowns policy: {unknowns_policy}

Structure:
1. Bottom line
2. What the sources establish
3. What is uncertain or contested
4. Options or paths
5. Recommendation, if supported by sources
6. Risks and caveats
7. Follow-up questions

Cite material claims where available. Label interpretation separately from source evidence.
```

Expected output: Decision-ready brief.

Failure modes: Recommendation outruns the evidence.

QA check: Includes uncertainty or contested points.

### NLM-SYNTH-02 Insight Map

Best surface: Chat, Mind Map

Use when: You want the big structure of the notebook before turning it into an output.

Prompt:

```text
Create an insight map for {notebook_goal}.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}

Return:
- 5-9 major themes
- Subpoints under each theme
- Source support for each theme
- Links between themes
- Contradictions or weak points
- Best next artifact to generate from this map

Use short labels suitable for a Mind Map if I choose to generate one next.
```

Expected output: Theme map.

Failure modes: Too many themes, no hierarchy.

QA check: Each theme has source support.

### NLM-SYNTH-03 Point-of-View Builder

Best surface: Chat, Report

Use when: You need a strategic stance, editorial angle, or research point of view.

Prompt:

```text
Build a source-grounded point of view for {notebook_goal}.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Tone: {tone}

Return:
1. Core thesis
2. Evidence that supports it
3. Evidence that complicates it
4. Alternative interpretations
5. What I should say carefully
6. What I should not claim
7. A concise final position

Every material claim must be grounded in selected sources or labeled as interpretation.
```

Expected output: Defensible point of view.

Failure modes: Overconfident thesis with weak support.

QA check: Includes "what I should not claim."

### NLM-SYNTH-04 Decision Matrix

Best surface: Data Table, Chat

Use when: You need to compare options grounded in notebook sources.

Prompt:

```text
Create a decision matrix for {decision_or_use_case}.

Selected sources: {selected_sources}
Audience: {audience}
Constraints: {constraints}

Rows: viable options from the sources.
Columns:
- Option
- Source support
- Upside
- Downside
- Evidence strength from 1 to 5
- Cost or effort if available
- Risk
- Best fit condition
- Recommendation

If the sources do not contain enough evidence for a recommendation, say so.
```

Expected output: Decision table.

Failure modes: Invents options not present in sources.

QA check: Every option has source support.

### NLM-SYNTH-05 Research Memo

Best surface: Report, Chat

Use when: You need a clean research artifact for future reuse.

Prompt:

```text
Write a research memo for {notebook_goal}.

Selected sources: {selected_sources}
Audience: {audience}
Depth: {depth}
Format: {format}

Sections:
- Research question
- Source set
- Key findings
- Evidence table
- Contradictions
- Practical implications
- Open questions
- Source-backed next steps

Keep claims tied to citations where available. Do not add external facts.
```

Expected output: Reusable memo.

Failure modes: Reads like a generic report instead of a source memo.

QA check: Contains an evidence table and open questions.

### NLM-SYNTH-06 Audience Translation

Best surface: Chat

Use when: You need the same notebook content converted for a different reader.

Prompt:

```text
Translate the selected source material for {audience}.

Selected sources: {selected_sources}
Notebook goal: {notebook_goal}
Use case: {decision_or_use_case}
Tone: {tone}
Constraints: {constraints}

Return:
- What this audience needs to understand
- What they already likely know
- What they may misunderstand
- A source-grounded explanation
- 5 terms that need definition
- 5 examples or analogies grounded in the sources
- What not to simplify

Do not change the meaning of the sources for accessibility.
```

Expected output: Audience-specific explanation.

Failure modes: Dumbs down technical meaning.

QA check: Includes "what not to simplify."

## Lane 4: Transformation

### NLM-TRANSFORM-01 Report Builder

Best surface: Studio Reports, Chat

Use when: You need a formal report from selected sources.

Prompt:

```text
Create a {format} report for {audience}.

Goal: {notebook_goal}
Selected sources: {selected_sources}
Use case: {decision_or_use_case}
Depth: {depth}
Tone: {tone}
Constraints: {constraints}

The report must include:
- Clear title
- Executive summary
- Source-grounded findings
- Evidence table
- Contradictions or caveats
- Practical implications
- What to verify before publishing

If a section is not supported by the selected sources, mark it "Not found in the selected sources."
```

Expected output: Report draft or custom report prompt.

Failure modes: Polished but unsupported sections.

QA check: Has "what to verify before publishing."

### NLM-TRANSFORM-02 Content Outline

Best surface: Chat, Notes

Use when: You want content from a notebook without adding false authority.

Prompt:

```text
Turn the selected sources into a content outline for {artifact_type}.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Tone: {tone}
Constraints: {constraints}

Return:
- Working title
- Angle
- Reader promise
- Outline
- Source-backed proof points for each section
- Examples to include
- Claims to avoid
- Final fact-check checklist

Do not draft the full piece yet. Build the outline and proof spine only.
```

Expected output: Outline with proof points.

Failure modes: Writes the full piece before proof is stable.

QA check: Each section has proof points.

### NLM-TRANSFORM-03 Client Brief

Best surface: Report, Chat

Use when: You need a clean handoff for a client, team, or collaborator.

Prompt:

```text
Create a client-ready brief from the selected sources.

Selected sources: {selected_sources}
Client/audience: {audience}
Goal: {notebook_goal}
Use case: {decision_or_use_case}
Tone: {tone}
Constraints: {constraints}

The brief should include:
- Context
- Key findings
- Evidence-backed implications
- Recommended action if supported
- Risks
- Open questions
- Next meeting agenda

Avoid internal process language. Keep it useful to the client.
```

Expected output: Client-facing brief.

Failure modes: Leaks internal thinking or unverified claims.

QA check: Open questions and risks are visible.

### NLM-TRANSFORM-04 Learning Guide

Best surface: Learning Guide, Chat, Flashcards, Quizzes

Use when: You want a study or training system from the notebook.

Prompt:

```text
Create a learning path for {audience} using the selected sources.

Selected sources: {selected_sources}
Learning goal: {notebook_goal}
Knowledge level: {depth}
Use case: {decision_or_use_case}
Constraints: {constraints}

Return:
- Learning outcomes
- Concept sequence
- Common misunderstandings
- Practice questions
- Flashcard topics
- Quiz structure with easy, medium, and hard questions
- Application exercise
- What the sources do not cover
```

Expected output: Learning system.

Failure modes: Only summarizes instead of building practice.

QA check: Has application exercise and difficulty levels.

### NLM-TRANSFORM-05 Workflow Playbook

Best surface: Chat, Report

Use when: You need the source material turned into a repeatable operating process.

Prompt:

```text
Convert the selected sources into a workflow playbook.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}

Return:
- When to use this workflow
- Inputs required
- Step-by-step process
- Decision points
- Output produced at each step
- Quality checks
- Common mistakes
- Completion criteria

Label any inferred process steps as inference.
```

Expected output: Repeatable playbook.

Failure modes: Gives advice instead of process.

QA check: Has completion criteria.

### NLM-TRANSFORM-06 Prompt Synthesizer

Best surface: Chat

Use when: You want NotebookLM to create a prompt to use in another clean session.

Prompt:

```text
Synthesize a master execution prompt from the selected sources. Do not execute the task.

Selected sources: {selected_sources}
Notebook goal: {notebook_goal}
Target artifact: {artifact_type}
Audience: {audience}
Use case: {decision_or_use_case}
Constraints: {constraints}

Create a copy-paste prompt with:
<role>
<intent>
<context_from_sources>
<evidence_rules>
<execution_steps>
<constraints>
<output_format>
<quality_check>

The prompt must require source-grounded claims, contradiction handling, and an unsupported-claim audit.
```

Expected output: Master prompt for a fresh AI session.

Failure modes: Executes instead of synthesizing.

QA check: Uses the XML-style blocks.

## Lane 5: Visual Production

### NLM-VISUAL-01 Slide Deck Strategy

Best surface: Chat before Slide Deck

Use when: You need the deck logic before generating slides.

Prompt:

```text
Design the slide strategy before generating a Slide Deck.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}
Deck mode: choose either Presenter Slides or Detailed Deck
Length: {depth}
Tone/style: {tone}
Constraints: {constraints}

Return:
- Recommended deck mode and why
- Slide-by-slide storyboard
- One message per slide
- Source-backed proof needed for each slide
- Suggested visual type per slide
- Claims to avoid
- Revision notes to use after generation

Do not generate the final deck text yet. Build the storyboard.
```

Expected output: Deck blueprint.

Failure modes: Skips deck mode or makes too many points per slide.

QA check: Each slide has one message and a proof need.

### NLM-VISUAL-02 Slide Deck Generation Prompt

Best surface: Slide Deck customization

Use when: You are ready to generate the deck.

Prompt:

```text
Create a {format} slide deck for {audience} using only selected sources: {selected_sources}.

Goal: {notebook_goal}
Use case: {decision_or_use_case}
Language: {output_language}
Length: {depth}
Tone: {tone}
Constraints: {constraints}

Use this structure:
- Open with the practical stakes for {audience}
- Build a clear evidence path from selected sources
- Preserve contradictions or caveats where material
- Use one main idea per slide
- For Presenter Slides: minimal text, strong titles, visual support for the speaker
- For Detailed Deck: self-contained explanations, source-backed details, clear section flow

Avoid decorative filler, vague claims, crowded slides, and unsupported facts. If a point is not found in selected sources, omit it or label it as not established.
```

Expected output: Generated slide deck.

Failure modes: Visual polish with weak source grounding.

QA check: Deck mode is visible in the generated result.

### NLM-VISUAL-03 Slide Revision QA

Best surface: Slide Deck revise flow, Chat for audit

Use when: You have a generated deck and need to improve it.

Prompt:

```text
Audit this generated slide deck against the selected sources and audience needs.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}
Deck mode: {format}

Return:
- Slide-by-slide issue list
- Unsupported or weak claims
- Visual hierarchy problems
- Slides with too much text
- Missing caveats
- Revision instructions for each slide
- Claims that must be rechecked after revision

Remember: if using NotebookLM slide revision, source grounding may not be considered during revisions, so flag any changed claim that needs a fresh source check.
```

Expected output: Revision list.

Failure modes: Only comments on style, not source support.

QA check: Includes source recheck warning.

### NLM-VISUAL-04 Infographic Strategy

Best surface: Chat before Infographic

Use when: You need a strong infographic, not a decorative summary.

Prompt:

```text
Design the infographic before generation.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}
Orientation: square, portrait, or horizontal
Detail level: concise, standard, or detailed
Tone/style: {tone}

Return:
- Recommended orientation and detail level
- The reading path from top to bottom or left to right
- 3-5 key source-backed points
- 0-3 numbers or stats to include
- Labels that must appear exactly
- Visual metaphor
- Source caveat to include
- What to avoid
```

Expected output: Infographic plan.

Failure modes: Too many stats, unclear reading path.

QA check: Has a stat cap and source caveat.

### NLM-VISUAL-05 Infographic Generation Prompt

Best surface: Infographic customization

Use when: You are ready to generate the infographic.

Prompt:

```text
Create an infographic for {audience} using only selected sources: {selected_sources}.

Goal: {notebook_goal}
Use case: {decision_or_use_case}
Language: {output_language}
Orientation: {format}
Detail level: {depth}
Style: {tone}
Constraints: {constraints}

Use a clear reading path. Include no more than 3 key stats unless the sources require more. Label every number with unit and context. Do not create decorative charts. Include a short caveat when the sources are partial, contested, or dated.

The final image should be understandable in 30 seconds.
```

Expected output: Generated infographic.

Failure modes: Pretty but unreadable, or numbers without context.

QA check: Every number has a label.

### NLM-VISUAL-06 Data Table and Chart Prompt

Best surface: Data Table, Ultra artifact creation where available

Use when: You need tables, charts, or exportable structured data.

Prompt:

```text
Create a data table for {notebook_goal} using only selected sources: {selected_sources}.

Audience: {audience}
Use case: {decision_or_use_case}
Output language: {output_language}
Constraints: {constraints}

Table columns:
- Item or observation
- Source
- Citation where available
- Metric or fact
- Unit
- Time period
- Denominator or sample
- Formula if calculated
- Chart-safe? yes/no
- What this does not prove

After the table, recommend the best chart type only if the source data supports it. Include axis labels, units, and one caveat for the chart.
```

Expected output: Table plus chart recommendation.

Failure modes: Chart recommendation without clean source data.

QA check: Contains "what this does not prove."

### NLM-VISUAL-07 Audio Overview Steering Prompt

Best surface: Audio Overview customization

Use when: You want a useful audio output rather than a generic podcast.

Prompt:

```text
Create an Audio Overview for {audience}.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Use case: {decision_or_use_case}
Format: choose Deep Dive, Brief, Critique, or Debate
Language: {output_language}
Tone: {tone}
Constraints: {constraints}

Focus the discussion on the practical questions {audience} needs answered. Preserve source disagreements. Explain source-backed ideas clearly, but do not add unsupported claims. If using Debate, make each side defend a real tension from the sources. If using Critique, evaluate the material against the stated goal and cite what the sources support.

Avoid flattening cultural context, changing terms from the sources, or making the hosts sound more certain than the sources allow.
```

Expected output: Guided audio generation.

Failure modes: Smooth audio with weak source fidelity.

QA check: Format is chosen for a clear reason.

### NLM-VISUAL-08 Video Overview Steering Prompt

Best surface: Video Overview customization

Use when: You want the video to be visual and useful, not just narrated slides.

Prompt:

```text
Create a Video Overview for {audience}.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Use case: {decision_or_use_case}
Format: Brief, Explainer, or Cinematic if available and appropriate
Language: {output_language}
Visual style: {tone}
Constraints: {constraints}

Make the video visual-first. Use source-backed diagrams, timelines, comparisons, process visuals, charts, or concrete examples where the sources support them. Focus on the 3-5 ideas {audience} most needs to understand. Preserve caveats and disagreements.

Avoid generic stock-like imagery, decorative visuals, unsupported claims, and overstuffed scenes. If Cinematic is unavailable due to tier, age, or language limits, use Explainer as the fallback.
```

Expected output: Guided video generation.

Failure modes: Narrated summary with weak visuals.

QA check: Includes explicit visual forms such as timeline, chart, or process.

### NLM-VISUAL-09 Visual Style Direction

Best surface: Infographic, Slide Deck, Video Overview customization

Use when: You need non-generic visual identity.

Prompt:

```text
Apply this visual direction to {artifact_type}.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Tone: {tone}
Constraints: {constraints}

Visual direction:
- Palette: specify 2-4 colors with names and hex codes if known
- Typography character: specify clear style, not exact font dependency
- Layout: specify density, spacing, hierarchy, and reading path
- Imagery: specify concrete motifs grounded in the topic
- Avoid: generic AI imagery, decorative charts, unreadable text, clutter, and unsupported visuals

Make the design serve the source-backed message first. Visual style must not distort the meaning of the sources.
```

Expected output: Style-guided visual artifact.

Failure modes: Style overtakes evidence.

QA check: Includes "avoid" list.

### NLM-VISUAL-10 Ultra Downloadable Artifact Prompt

Best surface: Advanced NotebookLM chat for eligible accounts

Use when: Ultra or eligible Workspace features can create files, charts, spreadsheets, or PowerPoint.

Prompt:

```text
If my account supports advanced NotebookLM artifact creation, create {artifact_type} from the selected sources.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}
Output format: {format}
Constraints: {constraints}

Requirements:
- Use only selected source content unless I explicitly ask for web research.
- Include a source-backed evidence section or notes area.
- For charts, include the source table, formula, units, axis labels, and caveat.
- For documents or PowerPoint, include a final "Unsupported or needs verification" section.
- If this feature is unavailable on my tier or device, provide the closest copy-paste Studio prompt instead.
```

Expected output: Advanced artifact or fallback prompt.

Failure modes: Acts as if advanced features are always available.

QA check: Has fallback behavior.

## Lane 6: Quality Control

### NLM-QC-01 Citation Fit Audit

Best surface: Chat

Use when: You need to check whether citations support the claims.

Prompt:

```text
Audit the previous answer for citation fit.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Use case: {decision_or_use_case}

Return a table with:
- Claim from the answer
- Citation or source used
- Does the citation actually support the claim? yes/no/partial
- Problem if partial or no
- Fix: keep, weaken, cite differently, remove, or mark not established

Be strict. Polished language is not proof.
```

Expected output: Claim-by-claim audit.

Failure modes: Rubber-stamps weak citations.

QA check: At least one row can be marked partial/no if the answer overreached.

### NLM-QC-02 Unsupported Claim Removal

Best surface: Chat

Use when: You want the cleanest safe version of an answer.

Prompt:

```text
Revise the previous answer by removing or weakening unsupported claims.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Audience: {audience}
Use case: {decision_or_use_case}

Rules:
- Keep source-backed claims.
- Weaken claims with partial support.
- Remove claims not found in selected sources.
- Preserve caveats and contradictions.
- Do not add new claims during revision.

Return:
1. Revised answer
2. Removed claims
3. Weakened claims
4. Remaining verification needs
```

Expected output: Safer revised answer.

Failure modes: Adds new claims while revising.

QA check: Includes removed and weakened claims.

### NLM-QC-03 Visual Output Audit

Best surface: Chat after generating slides/infographic/video

Use when: You need to red-team a visual artifact.

Prompt:

```text
Audit this {artifact_type} for production readiness.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Constraints: {constraints}

Score 1-5:
- Source grounding
- Message clarity
- Audience fit
- Visual hierarchy
- Readability
- Data integrity
- Caveat handling
- Actionability

Then list:
- Must-fix issues
- Nice-to-fix issues
- Unsupported visual or text claims
- Specific revision instructions
- Final publish/share verdict
```

Expected output: Visual QA scorecard.

Failure modes: Only praises the artifact.

QA check: Includes must-fix issues or an explicit no-must-fix verdict.

### NLM-QC-04 Contradiction Preservation Audit

Best surface: Chat

Use when: You worry the output created false consensus.

Prompt:

```text
Audit the previous answer for false consensus.

Selected sources: {selected_sources}
Goal: {notebook_goal}
Use case: {decision_or_use_case}

Find any place where the answer:
- Blended disagreements
- Ignored a minority view
- Treated weak evidence as settled
- Failed to mention source age, context, or limitation

Return:
- Original wording
- Source tension
- Why it matters
- Corrected wording
```

Expected output: Tension audit.

Failure modes: Says "no contradictions" without checking.

QA check: References actual source tension or clearly says none found.

### NLM-QC-05 Publication Risk Gate

Best surface: Chat

Use when: An output will be public, client-facing, or relied on for a decision.

Prompt:

```text
Run a publication risk gate on the previous output.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Constraints: {constraints}

Check for:
- Unsupported factual claims
- Medical, legal, financial, or professional advice risk
- Privacy or confidential information
- Copyright-sensitive reuse
- Numbers without source context
- Overconfident recommendations
- Missing caveats
- Audience mismatch

Return verdict: safe to share, share with edits, or do not share yet.
Include exact edits required.
```

Expected output: Share verdict.

Failure modes: Gives vague caution without exact edits.

QA check: Verdict is one of the three allowed options.

### NLM-QC-06 Prompt Portability Audit

Best surface: Chat

Use when: You want to know whether a prompt will work across many notebooks.

Prompt:

```text
Audit this prompt for portability across NotebookLM notebooks.

Prompt to audit:
{format}

Target notebook goal: {notebook_goal}
Audience: {audience}
Artifact type: {artifact_type}
Tier/device limits: {tier_or_device_limits}

Return:
- Missing variables
- Hidden assumptions
- Source-grounding weakness
- Feature or tier dependency
- Failure mode in a sparse notebook
- Failure mode in a conflicting-source notebook
- Revised portable version
```

Expected output: Better reusable prompt.

Failure modes: Only edits wording, not behavior.

QA check: Names sparse and conflicting-source failure modes.

### NLM-QC-07 Notebook Output Scorecard

Best surface: Chat, Notes

Use when: You want a simple trust score before acting.

Prompt:

```text
Score the previous output from 1 to 5 on each criterion:

- Groundedness
- Citation fit
- Coverage
- Contradiction handling
- Uncertainty handling
- Audience fit
- Artifact fit
- Actionability
- Risk control

Selected sources: {selected_sources}
Goal: {notebook_goal}
Use case: {decision_or_use_case}

After scoring, give:
- Overall trust verdict
- Lowest-scoring criterion
- Exact repair prompt I should run next

Do not give a high score unless the selected sources clearly support the output.
```

Expected output: Trust score.

Failure modes: Grade inflation.

QA check: Names the lowest-scoring criterion.

### NLM-QC-08 Final Studio Export Checklist

Best surface: Chat or Notes

Use when: You are about to download, present, export, or share.

Prompt:

```text
Create a final export checklist for this {artifact_type}.

Selected sources: {selected_sources}
Audience: {audience}
Use case: {decision_or_use_case}
Tier/device limits: {tier_or_device_limits}
Constraints: {constraints}

Checklist must cover:
- Source support
- Citations or source notes
- Claims to verify
- Visual readability
- Chart or number integrity
- Tone and audience fit
- Feature limits or fallback used
- Export format
- Sharing permissions
- Final go/no-go

Return a compact checklist plus the final go/no-go verdict.
```

Expected output: Final checklist.

Failure modes: Skips sharing permissions or feature limits.

QA check: Has final go/no-go.

## Specialized Studio Recipes

### Slide Deck Recipe

1. Run `NLM-SOURCE-01 Coverage Audit`.
2. Run `NLM-VISUAL-01 Slide Deck Strategy`.
3. Generate with `NLM-VISUAL-02 Slide Deck Generation Prompt`.
4. Audit with `NLM-VISUAL-03 Slide Revision QA`.
5. Final check with `NLM-QC-08 Final Studio Export Checklist`.

Key rule: choose Presenter Slides for live talks, Detailed Deck for a leave-behind.

### Infographic Recipe

1. Run `NLM-EXTRACT-06 Data and Number Ledger`.
2. Run `NLM-VISUAL-04 Infographic Strategy`.
3. Generate with `NLM-VISUAL-05 Infographic Generation Prompt`.
4. Audit with `NLM-QC-03 Visual Output Audit`.
5. If numbers appear, run `NLM-QC-01 Citation Fit Audit`.

Key rule: no more than 3 key stats unless the source material demands more.

### Data Table and Chart Recipe

1. Run `NLM-SOURCE-04 Source Quality Triage`.
2. Run `NLM-EXTRACT-06 Data and Number Ledger`.
3. Run `NLM-VISUAL-06 Data Table and Chart Prompt`.
4. Audit with `NLM-QC-01 Citation Fit Audit`.
5. If sharing, run `NLM-QC-05 Publication Risk Gate`.

Key rule: every number needs unit, time period, denominator if available, and what it does not prove.

### Audio Overview Recipe

1. Run `NLM-SYNTH-02 Insight Map`.
2. Choose Deep Dive, Brief, Critique, or Debate.
3. Generate with `NLM-VISUAL-07 Audio Overview Steering Prompt`.
4. If the audio will be shared, run `NLM-QC-05 Publication Risk Gate` on a transcript or summary.

Key rule: use Debate only for real source tension.

### Video Overview Recipe

1. Run `NLM-EXTRACT-05 Example Miner`.
2. Run `NLM-VISUAL-08 Video Overview Steering Prompt`.
3. Use Brief for fast takeaways, Explainer for teaching, Cinematic only when available and appropriate.
4. Audit with `NLM-QC-03 Visual Output Audit`.

Key rule: ask for diagrams, timelines, processes, comparisons, or charts when the sources support them.

### Reports Recipe

1. Run `NLM-SOURCE-01 Coverage Audit`.
2. Run `NLM-EXTRACT-01 Claim Ledger`.
3. Generate with `NLM-TRANSFORM-01 Report Builder`.
4. Audit with `NLM-QC-01 Citation Fit Audit`.
5. Clean with `NLM-QC-02 Unsupported Claim Removal`.

Key rule: no polished report before the claim ledger exists.

### Mind Map Recipe

1. Run `NLM-SYNTH-02 Insight Map`.
2. Generate the Mind Map.
3. Click major branches and ask follow-up questions using `NLM-EXTRACT-04 Contradiction Map` or `NLM-SOURCE-03 Missing Evidence Finder`.

Key rule: use the Mind Map to find structure, not to certify truth.

### Flashcard and Quiz Recipe

1. Run `NLM-TRANSFORM-04 Learning Guide`.
2. Generate flashcards around core terms, examples, and distinctions.
3. Generate quizzes at easy, medium, and hard levels.
4. Audit with `NLM-QC-07 Notebook Output Scorecard`.

Key rule: quiz for application, not only recall.

## Studio Custom Prompt Starters

Use these when you are inside a NotebookLM Studio customization box and want to paste one strong instruction without running the full prompt chain first. If you are not sure which asset to create, run `NLM-AUTO-04 Studio Asset Recommender` first.

### Slide Deck Custom Prompt

```text
Create a Slide Deck from the selected sources for the audience and use case implied by the notebook. If the best mode is a live presentation, use Presenter Slides with clean visual support and brief talking points. If the best mode is a leave-behind, use a Detailed Deck with enough context to stand alone.

Use the uploaded brand, ICP, offer, creative, and content context when present. Preserve the strongest source-backed point of view. Do not add generic advice.

Structure:
1. Opening problem or opportunity
2. Source-backed insight
3. Evidence path
4. Implications for the audience
5. Recommended action or takeaway
6. Caveats and what the sources do not prove

Keep every factual claim grounded in selected sources. If evidence is missing, name the gap instead of filling it.
```

### Infographic Custom Prompt

```text
Create an infographic from the selected sources for the audience and use case implied by the notebook.

Infer the best orientation from the job:
- Square for social or compact summary
- Portrait for step-by-step or one-page teaching
- Horizontal for comparison, timeline, or presentation support

Use no more than 3 key stats unless the sources clearly require more. Include short labels, a clear reading path, one visual hierarchy, and one caveat box titled "What this does not prove."

Use uploaded brand, ICP, offer, creative, and content context when present. Do not invent numbers, audience claims, or outcomes.
```

### Audio Overview Custom Prompt

```text
Create an Audio Overview using the selected sources and the notebook's uploaded context.

Choose the best format from the source material:
- Deep Dive for teaching and synthesis
- Brief for fast executive understanding
- Critique for reviewing my own draft, offer, strategy, or creative
- Debate only when the selected sources contain real tension or opposing views

Focus on the audience, offer, ICP, brand, or content goals implied by the selected sources. Keep the hosts grounded in the material. Do not let them turn source evidence into unsupported advice.

End the overview with:
1. The strongest source-backed takeaway
2. The most important uncertainty
3. One practical next step
```

### Video Overview Custom Prompt

```text
Create a Video Overview from the selected sources and uploaded context.

Infer the best format:
- Brief for fast orientation
- Explainer for teaching a process, strategy, or framework
- Cinematic only if available, appropriate, and supported by the source material

Use visuals that match the material: diagrams for systems, timelines for sequences, comparisons for tradeoffs, charts only when numbers and units are present, and concrete examples when uploaded content supports them.

Preserve the notebook's brand, ICP, offer, and creative context when present. Avoid unsupported claims, stock-feeling visuals, and generic motivational narration.

Include one caveat or limitation from the selected sources.
```

### Report Custom Prompt

```text
Create a report from the selected sources for the audience and use case implied by the notebook.

Choose the best report type:
- Briefing document for executive understanding
- Study guide for learning
- FAQ for buyer, team, or student questions
- Custom report for strategy, content, offer, or research decisions

Use this structure:
1. Purpose
2. Source boundary
3. Key findings
4. Evidence table
5. Interpretation
6. Recommendation or next move if supported
7. What the sources do not prove
8. Open questions

Keep evidence and recommendation separate. Use citations where available.
```

### Data Table Custom Prompt

```text
Create a Data Table from the selected sources.

Infer the best rows and columns from the raw intent and source material. Include only fields supported by selected sources.

Required columns when relevant:
- Source
- Claim or data point
- Unit
- Time period
- Denominator or sample if available
- Formula if calculated
- Confidence
- Limitation
- What this does not prove

If a requested number, formula, row, or comparison is not present in the selected sources, write "Not found in selected sources" in that cell.
```

### Flashcards Custom Prompt

```text
Create flashcards from the selected sources for the audience and learning goal implied by the notebook.

Prioritize:
- Core terms
- Distinctions people confuse
- Source-backed examples
- Process steps
- Buyer, brand, offer, or strategy concepts if those sources are selected

Make cards application-based when possible, not only definition-based. Include explanations that point back to the selected source material. Do not add facts outside the selected sources.
```

### Quiz Custom Prompt

```text
Create a quiz from the selected sources for the audience and learning goal implied by the notebook.

Use a mix of:
- Easy recall
- Medium concept application
- Hard scenario judgment

Test whether the learner can use the material, not only repeat it. Include answer explanations grounded in the selected sources. If the sources do not establish the answer, do not ask the question.
```

### Mind Map Steering Prompt

NotebookLM's current Help page documents Mind Maps as generated from chat or Studio, but does not document the same custom prompt box pattern as Slide Decks, Infographics, Audio, Video, Reports, Data Tables, Flashcards, and Quizzes. Use this in chat before generating or when asking follow-up questions from Mind Map nodes.

```text
Prepare this notebook for a useful Mind Map.

Selected sources: {selected_sources}
Raw intent: {raw_intent}
Context assets uploaded: {context_assets}

Identify the best central node, 5-8 major branches, and the most useful sub-branches for my goal. Separate source-backed branches from inferred branches. Mark any branch that is weakly supported.

After I generate the Mind Map, give me 5 node-click questions that will help me inspect gaps, contradictions, and asset ideas.
```

### Saved Note Prompt

```text
Create a saved note I can use as reusable context for this notebook.

Use selected sources only. Summarize the notebook's brand, ICP, offer, content themes, voice, proof, constraints, and open questions. Keep it compact. End with instructions for how future prompts should use this note.
```

## Account, Device, and Feature Fallbacks

Use this fallback clause whenever feature access is uncertain:

```text
If the requested NotebookLM feature is unavailable because of account tier, device, age, language, quota, source limit, or workspace policy, do not stop. Provide the closest supported fallback:
- For unavailable Slide Deck: provide a slide-by-slide storyboard and copy-paste Slide Deck prompt.
- For unavailable Infographic: provide an infographic brief with reading path, labels, stat cap, and style direction.
- For unavailable Cinematic Video: use Explainer or Brief.
- For unavailable Deep Research: provide Fast Research queries and source filters.
- For unavailable downloadable artifact: provide a Markdown, table, or prompt that I can paste into the available Studio surface.
```

## Validation Harness

Run these tests before trusting the suite as a reusable system.

| Scenario | Prompt to run | Pass condition |
|---|---|---|
| Single clean PDF | `NLM-EXTRACT-01 Claim Ledger` | Claims are accurate and cited. |
| Multi-source disagreement | `NLM-EXTRACT-04 Contradiction Map` | Disagreement is preserved. |
| Missing answer | `NLM-SOURCE-03 Missing Evidence Finder` | Says not found in selected sources. |
| YouTube transcript | `NLM-EXTRACT-05 Example Miner` | Messy speech becomes usable examples without invented polish. |
| Strategy notebook | `NLM-SYNTH-01 Executive Brief` | Evidence and recommendation are separated. |
| Slide deck | `NLM-VISUAL-01 Slide Deck Strategy` | Chooses Presenter Slides or Detailed Deck before generation. |
| Infographic | `NLM-VISUAL-04 Infographic Strategy` | Specifies orientation, reading path, stat cap, labels, and caveat. |
| Data table/chart | `NLM-VISUAL-06 Data Table and Chart Prompt` | Includes units, formulas if used, source rows, and limits. |
| Excluded source | `NLM-SOURCE-02 Selected-Source Boundary` | Unchecked source is not used. |

## Quality Bar

Trust an output only if it scores 4 or 5 on:

- Groundedness
- Citation fit
- Contradiction handling
- Uncertainty handling
- Artifact fit
- Audience fit
- Risk control

If Groundedness or Citation Fit is below 4, run `NLM-QC-02 Unsupported Claim Removal` before using the output.

## Source Notes

This pack was built around current NotebookLM behavior verified on June 22, 2026:

- NotebookLM chat supports source-grounded answers with inline citations and selected-source control.
- Sources can include common files, web URLs, YouTube transcripts, images, audio, Google Drive files, Sheets, Slides, and more, subject to limits.
- Studio supports outputs such as Audio Overviews, Video Overviews, Mind Maps, Reports, Data Tables, Flashcards, Quizzes, Slide Decks, and Infographics, with feature and account differences.
- Studio reports can be created from preset or custom report types, and Data Tables support a prompt box for rows, columns, language, and focus.
- Flashcards and Quizzes support difficulty and a prompt box for audience, style, focus, or outline.
- Mind Maps are documented as source-generated visual summaries, but the current Help page does not document the same custom prompt box pattern as the other Studio assets.
- Slide Decks distinguish Detailed Decks from Presenter Slides and revisions may not account for sources, so source checks after revision matter.
- Infographics support language, detail level, orientation, visual style, and custom focus instructions.
- Video Overviews support formats and steering prompts; Cinematic is more limited.
- Audio Overviews support Deep Dive, Brief, Critique, and Debate, with language and some length controls.
- Advanced NotebookLM artifact creation, code execution, charts, spreadsheets, documents, and PowerPoint are available only for eligible account plans and should be treated as optional.

## Source Links

- NotebookLM chat: https://support.google.com/notebooklm/answer/16179559
- Add or discover sources: https://support.google.com/notebooklm/answer/16215270
- Create a notebook and Studio outputs: https://support.google.com/notebooklm/answer/16206563
- Mind Maps: https://support.google.com/notebooklm/answer/16212283
- Flashcards or Quizzes: https://support.google.com/notebooklm/answer/16958963
- Slide Decks: https://support.google.com/notebooklm/answer/16757456
- Infographics: https://support.google.com/notebooklm/answer/16758265
- Audio Overviews: https://support.google.com/notebooklm/answer/16212820
- Video Overviews: https://support.google.com/notebooklm/answer/16454555
- Google NotebookLM research update, June 8, 2026: https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/
- NotebookLM Deep Research update, November 13, 2025: https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-deep-research-file-types/
- NotebookLM Data Tables update, December 18, 2025: https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-data-tables/
- NotebookLM Cinematic Video update, March 4, 2026: https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/
