# Free-First Research Mission Contract

## Purpose

Make deep, current research executable inside Codex without treating local
memory as current-world evidence and without silently reaching for paid or
quota-heavy accelerators.

This is a companion contract for `/deep-research-os`. It is not a new research
owner, hot command, expert persona, or automation.

## Authority Order

Use this order whenever a claim describes what is true now:

1. Current primary or official external sources opened during this run.
2. Multiple current independent external sources.
3. Current public community evidence or RSS items, labeled for what they can
   actually prove.
4. Tavily Search snippets and extracts as discovery or supporting evidence.
5. User-provided material, with its date and provenance stated.
6. Local harness context, memory, skills, and prior artifacts.

Local context may shape the question, constraints, skill selection,
interpretation, and downstream use. It may not establish a current-world fact.
If local context conflicts with current external evidence, the external evidence
wins for world-state claims. User-owned definitions, preferences, and project
decisions still control intent.

## Source Ladder

### 1. Codex native web research

Use the host-provided web search and page-open tools first. Search several
angles, open the strongest pages, prefer primary sources, inspect publication
dates, and run a counterevidence query. Search-result snippets are discovery,
not decision-grade proof.

The local Python backplane cannot call an app-only native web tool. It prepares
the mission and validates returned evidence; the active Codex thread performs
the native web calls.

### 2. Tavily Search and Extract

Use only the existing Search and Extract legs for bounded gap filling and page
recovery. Do not invoke Tavily Research from this mode. A Tavily search snippet
is `DIRECTIONAL`; a full-page extract may support analysis but is not promoted
to `VERIFIED` merely because extraction succeeded.

Pin Search and Extract to basic depth, cap the default call at two queries and
four extracts, and disclose estimated API credits in the receipt. Because the
runtime cannot inspect the Tavily plan or overage setting, its Tavily command
fails closed until the operator explicitly confirms that the account cannot
create a dollar charge. `$0.00` means no paid endpoint was intentionally
selected, not that an invisible account setting was guessed.

### 3. Public RSS or Atom

Pull public feeds on demand for dated releases, changelogs, publications, and
community signals. RSS is a source transport, not an automation. This contract
creates no schedule, daemon, launch agent, cron job, or recurring monitor.

### 4. Local context and relevant skills

Search the workspace after the live research question is locked. Load only the
context and skills that can change the questions, interpretation, or use of the
evidence. Keep local facts out of the external evidence ledger unless the claim
is explicitly about the local system.

## Blocked Paths

Free-first mode must not call or delegate to:

- Apify or any Apify actor, dataset, task, webhook, or client.
- Gemini Deep Research, Perplexity, NotebookLM, or another paid accelerator.
- Tavily Research. Tavily Search and Extract remain allowed only as bounded,
  disclosed credit usage under a zero-intended-dollar run cap; account-plan and
  overage status remain unverified unless separately inspected.
- Real subagents, research swarms, background workers, or parallel agent fan-out.
- Authenticated/private scraping or browser automation.
- Schedules, recurring automations, launch agents, cron jobs, or monitors.

The run receipt must show zero paid spend and an empty executed-blocked-paths
list. Mentioning a blocked provider in policy is not execution; importing or
calling its client is.

## Mission Contract

Every mission must name:

- the research objective;
- the decision it supports;
- the requested depth;
- the downstream consumer or use;
- the use-now artifact;
- the current-world authority rule;
- a current-world freshness window (72 hours by default) and a requirement that
  evidence be retrieved during this mission;
- the query plan, including official/current and counterevidence angles;
- relevant local context paths and skills, if any;
- source, domain, and full-page-read floors;
- the blocked paths;
- the validation and value receipt.

If no decision or downstream use can be named, the mission is not ready to
consume research quota. Clarify or stop.

## Finding Contract

Each finding is one JSON object with:

- `claim_id`
- `claim`
- `source_url`
- `source_title`
- `source_class`
- `retrieval_method`
- `evidence_type`
- `retrieved_at`
- `published_at` when time-sensitive source classes require it
- `query_id`
- `claim_label`
- `claim_scope`
- `stance`
- `excerpt`

Allowed claim labels are `VERIFIED`, `TRIANGULATED`, `DIRECTIONAL`, `INFERENCE`,
`UNVERIFIED`, and `CONTRADICTED`.

Rules:

- A current-world claim needs a public HTTP(S) source and a retrieval time.
- A current-world retrieval must occur during the mission and remain inside the
  declared freshness window. Reusing an older evidence file does not make it
  current.
- `VERIFIED` needs an opened page, document, direct quote, or dated official feed
  item. A search snippet cannot be `VERIFIED`.
- `TRIANGULATED` needs at least two independent source domains for the same
  `claim_id`.
- RSS/community current signals need a publication date.
- A local-context source cannot carry `claim_scope: current_world`.
- A direct quote needs a source URL and a non-empty excerpt.
- Invalid findings are quarantined and make the ingest fail closed until fixed.

## Execution Loop

1. Lock the decision, audience, freshness need, and use-now artifact.
2. Compile the local mission packet.
3. Execute native web research in the active Codex thread.
4. Use bounded Tavily Search/Extract and public RSS only for identified gaps.
5. Ingest findings through the deterministic validator.
6. Load relevant local context and skills for interpretation, never for current
   factual substitution.
7. Synthesize the decision brief with citations, contradictions, confidence,
   and explicit unknowns.
8. Run the research quality gate and write the value receipt.

## Completion Gate

A mission is `REAL` only when:

- at least one full page was opened through Codex native web research;
- the requested depth source and domain floors are met;
- the requested authoritative-claim floor is met; directional-only findings
  cannot earn a `REAL` receipt;
- snippets count at half weight and cannot carry the run alone;
- the counterevidence angle returned evidence or is explicitly reported as an
  unresolved gap;
- no invalid current-world claim survived;
- paid spend is `$0.00`;
- no blocked path executed;
- the output names a decision and a downstream use;
- the value receipt distinguishes data returned from data accepted or used.

Otherwise return `DEGRADED` or `FAILED`, never a confident deep-research label.

## Value Receipt

Every final artifact reports these states separately:

- `data_returned`
- `evidence_gate`
- `decision_supported`
- `artifact_produced`
- `downstream_use`
- `accepted_by_operator`
- `used_in_work`
- `commercial_event`

The final three remain `UNTESTED / NO EVENT` until an actual event is recorded.

## Reuse Hook

`/deep-research-os --free-first` is the explicit route. In Codex, free-first is
the default for current external research unless Farrice explicitly authorizes
another provider or execution mode.
