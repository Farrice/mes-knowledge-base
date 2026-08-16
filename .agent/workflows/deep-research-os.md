---
description: "Ultimate research OS: deep research, wide decomposition, social listening, market intelligence, source ledger, and anti-hallucination verification"
---

# /deep-research-os - Deep Research, Market Intelligence, And Social Listening

Use this workflow when the user needs serious research that will influence strategy,
offers, positioning, content, product-market fit, client work, market entry,
competitive intelligence, social listening, or factual claims.

Preferred hot front door:

```text
/virtuoso --mode research [research objective]
```

Optional Kimi-style packet compiler (never part of Free-First mode; use only
after explicit approval for real subagents):

```bash
python3 execution/kimi_swarm.py plan "[research objective]" --mode research --depth standard --allow-subagents --json
```

Direct specialist command:

```text
/deep-research-os [research objective]
/deep-research-os --free-first [research objective]
/deep-research-os --market [market/category/offer]
/deep-research-os --icp [buyer/problem/category]
/deep-research-os --social-listening [market/community/problem]
/deep-research-os --pmf [product/offer/category]
/deep-research-os --competitors [category or named competitors]
/deep-research-os --claim-audit [draft, brief, or claim list]
/deep-research-os --wide [large list, many companies, many products, many creators]
/deep-research-os --local-only [objective]
```

## Role

`/deep-research-os` is the research composer. It does not replace
`/deep-research`, `/research-swarm`, `/parallel-research`, `/competitor-intel`,
or `/icp-deep-dive`. It chooses and blends them into one research operation with
a plan, evidence ledger, verification pass, and packaged synthesis.

In Codex, current external research defaults to **Free-First Research Mission**
mode unless Farrice explicitly authorizes another provider or execution mode.
The contract lives at
`semantic_libraries/antigravity/primitives/free-first-research-mission-contract.md`.
This is a companion execution path under the existing owner, not a new command
surface or competing research system.

For Kimi-style research, `/deep-research-os` remains the owner and
`/kimi-swarm` is only the packet compiler: it decomposes the objective, casts
expert research angles, emits worker briefs, and hands sourced findings back to
`execution/research.py` for receipt-bearing ingest.

## Codex Free-First Default

Use this path when the user asks for current, deep, live, enriched, or
decision-grade research in Codex and has not approved paid accelerators or real
subagents.

Compile the mission locally:

```bash
python3 execution/free_first_research.py plan \
  --objective "[research objective]" \
  --decision "[decision this research supports]" \
  --downstream "[where the evidence will be used]" \
  --artifact "[use-now artifact]" \
  --depth quick|standard|deep|max \
  --freshness-hours 72 \
  --context "[optional local path]" \
  --skill "[optional relevant skill]"
```

Then execute the generated `native-web-runbook.md` in the active Codex thread:

1. Use Codex's host-provided native web search and page-open tools first.
2. Search official/current, counterevidence, comparison, human-voice, and
   RSS/changelog angles sequentially in the main thread.
3. Open the strongest pages. Search snippets are discovery, not `VERIFIED`
   evidence.
4. Use bounded, basic-depth Tavily **Search and Extract** only for identified
   gaps. Do not invoke Tavily Research. Disclose the estimated credits and say
   when the account's billing-plan/overage state could not be verified. The
   Tavily command fails closed until the zero-dollar account boundary is
   explicitly confirmed.
5. Pull public RSS/Atom feeds on demand when they improve recency or source
   coverage. Do not create a schedule.
6. Ingest the JSONL findings through `free_first_research.py ingest`.
7. Only after the external evidence gate passes, load relevant local context and
   skills for interpretation and downstream use.
8. Synthesize the cited decision artifact, run the quality gate, and expose the
   value receipt.

Current-world authority is **live external evidence retrieved in this run**.
Local memory, harness files, skills, and prior artifacts may shape questions,
constraints, skill selection, analysis, and reuse, but they may not prove what
is currently true. If they conflict, live external evidence wins for
current-world claims; user-owned preferences and project decisions still
control intent.

Free-first mode must not call Apify, Gemini Deep Research, Perplexity,
NotebookLM, Tavily Research, a research swarm, a real subagent, browser
automation, a background worker, or a scheduler. The run receipt must show
`cost_usd: 0.0` and no executed blocked paths.

## Inspiration Standard

The bar is not "search and summarize." The bar is:

- A plan before research begins.
- Source control over what can be used.
- Wide decomposition when the task contains many independent items.
- Fresh context packets for wide work so item 30 does not get lower-quality
  treatment than item 1.
- Current source retrieval with citations, dates, and contradiction checks.
- Real social listening from public, attributed language.
- Claim labels that separate verified evidence from inference.
- A final report that explains the system underneath the facts.

## Safety And Permission Boundary

Allowed by default:

- Workspace-local reads.
- Local routing, planning, and artifact creation.
- Public web reads when the user asks for current research.
- Codex native web search/page reads in Free-First Research Mission mode.
- Bounded Tavily Search/Extract and on-demand public RSS when free-first mode is
  explicitly selected; both remain source-gathering legs, not proof shortcuts.
- Source-ledger creation, claim inventory, and quality checks.

Approval required:

- Paid or quota-heavy APIs such as Perplexity, Gemini Deep Research, Apify, or
  NotebookLM.
- Authenticated/private social listening, scraping, or browser automation.
- Connector writes, publishing, outreach, DMs, comments, emails, or public posts.
- External exports, global mirrors, destructive cleanup, Mission mutation, or
  real Codex subagents.

If live web or provider access is unavailable, continue with local corpus only
and label the output `evidence_gap: live sources not accessed`. Local-only work
cannot satisfy or substitute for a current-world evidence gate.

## Research Trace

Every run starts with this visible block:

```markdown
## Deep Research OS Trace
- Objective:
- Research mode:
- Function owner: Research Intelligence Agent
- Primary route:
- Support stack considered:
- Support stack executed:
- Source access:
- Current-world authority:
- Free-first mission packet:
- Paid/API boundary:
- Social-listening boundary:
- Worker packets prepared:
- Real subagents spawned: false unless explicitly approved
- Evidence ledger:
- Verification plan:
- Decision and downstream use:
- Value receipt:
- First safe local action:
```

## Operating Loop

### 1. Intent Lock

Convert the user's raw context into:

- Research decision to support.
- Audience for the output.
- Time sensitivity.
- Source types allowed.
- Deliverable shape.
- Decision deadline.
- Risk if wrong.

Ask only when the missing answer changes the research path. Otherwise state
assumptions and proceed.

### 2. Research Design

Build a research plan before gathering. Include:

- Core question.
- Subquestions.
- Source map.
- Inclusion and exclusion rules.
- Search/query plan.
- Expected contradictions.
- What would change the recommendation.
- Minimum evidence bar.

### 3. First-Principles And Systems Map

For strategic research, map:

- Actors.
- Incentives.
- Constraints.
- Value chain.
- Distribution channels.
- Buyer alternatives.
- Status quo.
- Bottlenecks.
- Feedback loops.
- Failure modes.
- First-principles hypotheses.

This prevents shallow trend summaries from pretending to be strategy.

### 4. Wide Decomposition

Use wide decomposition when the task contains many parallel items:

- Many companies.
- Many products.
- Many creators.
- Many customer segments.
- Many reviews or conversations.
- Many markets.

Create independent packets:

```markdown
## Research Packet
- Packet id:
- Item:
- Question:
- Required fields:
- Source targets:
- Claim labels required:
- Output format:
```

No real Codex subagents are spawned unless the user explicitly authorizes them.
Without authorization, the main thread runs or stages the packets locally.

### 5. Route Selection

Choose the smallest stack that covers the research job.

| Need | Route |
|---|---|
| Current research in Codex with no paid tools or subagents | Free-First Research Mission under `/deep-research-os` |
| One deep, current question | `/deep-research` |
| Gemini-first deep research | `/deep-research-gemini` |
| Market + audience + system scan | `/research-swarm` |
| Custom independent angles | `/parallel-research --angles` |
| Competitor positioning/pricing/content gaps | `/competitor-intel` |
| Buyer psychology, language, resistance | `/icp-deep-dive` |
| Claim verification | `python3 execution/research_quality_gate.py` |
| Local system/source overlap | `python3 execution/context_retriever.py search` |

When real subagents and any provider costs are explicitly approved, the default
stack for high-stakes market work is:

```text
/research-swarm -> /parallel-research --angles -> /deep-research -> quality gate
```

When those same boundaries are explicitly approved, the default stack for
offer-market fit is:

```text
/research-swarm -> /competitor-intel -> /icp-deep-dive -> quality gate
```

Default stack for claim-heavy drafts:

```text
claim inventory -> source ledger -> quality gate -> rewrite only after verification
```

### 6. Evidence Gathering

Preferred Codex entrypoint with no paid/provider approval:

```bash
python3 execution/free_first_research.py plan \
  --objective "[research question]" \
  --decision "[decision this research supports]" \
  --downstream "[downstream consumer]" \
  --artifact "[use-now research artifact]" \
  --depth quick|standard|deep|max
```

Execute the generated native-web runbook in Codex, then validate returned
findings:

```bash
python3 execution/free_first_research.py ingest --mission .tmp/research-missions/[mission-id]
python3 execution/free_first_research.py verify --mission .tmp/research-missions/[mission-id] --require-receipt
```

Provider-backed entrypoint only after explicit approval for that provider and
cost boundary:

```bash
python3 execution/research.py "[research question]" --depth quick|standard|deep|max
```

Unified receipt-bearing research entrypoint:

```bash
python3 execution/research.py plan --query "[research question]" --depth standard
python3 execution/research.py ingest --findings .tmp/research/<slug>/native-findings.jsonl --query "[research question]" --depth standard --swarm
```

For local-only research, search the workspace and existing compiled knowledge
only when the decision is about the local system or live evidence is explicitly
out of scope. Never use local-only results to answer a current-world question.

### 7. Social Listening

Social listening must capture real human language, not inferred sentiment.

Allowed source classes:

- Public Reddit threads.
- Public forums and communities.
- Public reviews.
- Public comments discoverable through normal web search.
- Public competitor pages, sales pages, changelogs, help docs, and pricing pages.
- User-provided exports, notes, interview transcripts, or CRM snippets.

Do not fabricate quotes. Every quote needs:

- URL or user-provided source.
- Date or retrieval date when available.
- Context: thread, review, comment, post, or page.
- Speaker class if knowable: buyer, practitioner, critic, user, seller.
- Quote confidence: direct quote, lightly cleaned quote, paraphrase, or summary.

Social-listening output:

```markdown
## Voice And Signal Ledger
| Source | Speaker class | Verbatim or signal | Theme | Confidence | Implication |
|---|---|---|---|---|---|
```

### 8. Deep Canvassing Layer

When the research affects ICP, messaging, adoption, belief change, or offer
conversion, add the deep canvassing layer:

- What do they believe that makes the current behavior rational?
- What identity is protected by not changing?
- What evidence would feel safe enough to reconsider?
- What language do they use before they are ready to buy?
- What promise would they reject as too convenient?
- What status loss or risk sits underneath the objection?
- What bridge message lets them move without feeling manipulated?

### 9. Anti-Hallucination Gate

Every final report uses claim labels:

| Label | Meaning |
|---|---|
| `VERIFIED` | Directly supported by a cited source. |
| `TRIANGULATED` | Supported by multiple independent sources. |
| `DIRECTIONAL` | Supported by signals, but not definitive. |
| `INFERENCE` | Analyst conclusion based on evidence. |
| `UNVERIFIED` | Plausible but not sourced enough to rely on. |
| `CONTRADICTED` | Sources disagree or undermine the claim. |

Run the quality gate before downstream use:

```bash
python3 execution/research_quality_gate.py validate [final_report.md] --strict --source-ledger [source_ledger.md]
```

If the gate fails, revise the research or downgrade the claim. Do not launder
weak evidence into confident strategy.

### 10. Package The Output

Choose the output package that matches the user's decision.

| Package | Use |
|---|---|
| Research Brief | Fast decision support. |
| Market Intelligence Map | Market, competitors, trends, channels, pricing. |
| Social Listening Pack | Voice, objections, language, communities, demand signals. |
| ICP Deep Canvass | Identity-level buyer understanding and bridge messaging. |
| PMF/OMF Fit Brief | Product-market and offer-market fit diagnosis. |
| Claim Audit | Verify or downgrade claims in drafts, decks, pages, and reports. |
| Wide Research Table | Many items with consistent fields and quality. |
| Strategy Memo | Synthesis, implications, tradeoffs, and next actions. |

Minimum final structure:

```markdown
# [Research Title]

## Decision It Supports
## Bottom Line
## Method
## Evidence Ledger
## Claim Table
## Contradictions And Gaps
## Systems Map
## Social Listening
## First-Principles Analysis
## Recommendations
## Confidence And Risks
## Next Data Pull
## Sources
```

## Worker Packets

Prepare these packets when useful. Real Codex subagents still require explicit
authorization.

| Packet | Job | Output |
|---|---|---|
| `deep-research` | Current source gathering and synthesis | Source-backed research memo |
| `fact-verifier` | Claim inventory and verification | Claim table with labels |
| `competitive-intel` | Category, pricing, positioning, gaps | Competitive map |
| `icp-deep-canvasser` | Buyer identity, resistance, language | ICP deep canvass |
| `adversarial-reviewer` | Attack weak logic and unsupported claims | Risk memo |
| `prose-doctor` | Make the report human, sharp, and readable | Polished synthesis |
| `content-finalizer` | Convert findings into publishable assets | Final content pack |

## First Safe Local Action

If the user asks to build, package, or run current research and no paid/API
action is approved, compile the free-first mission first:

```bash
python3 execution/free_first_research.py plan \
  --objective "[research objective]" \
  --decision "[decision]" \
  --downstream "[downstream use]" \
  --artifact "[use-now artifact]" \
  --depth standard
```

Then execute the generated native-web runbook in the active Codex thread. Do
not run a paid provider, schedule, or subagent unless separately approved.

## Verification

Use these checks after command or workflow changes:

```bash
python3 execution/verify_free_first_research_mission.py
python3 execution/verify_deep_research_os.py
python3 execution/validate_skill.py source-command-deep-research-os
python3 execution/command_menu.py search "deep research social listening market intelligence"
python3 execution/workflow_router.py search "deep research social listening market intelligence"
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
