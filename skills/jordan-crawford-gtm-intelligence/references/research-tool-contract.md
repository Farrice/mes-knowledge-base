# Research Tool Contract

This contract governs live research for every Jordan Crawford workflow. It keeps private strategy local, makes tool failures visible, and prevents public signals from being promoted into customer truth.

## 1. Partition the input before retrieval

Create two explicit blocks and show them for review in the Research Receipt:

- `PRIVATE_CONTEXT` — nonpublic offer names, pricing, target lists, hypotheses, customer records, internal metrics, and strategic reasoning. Keep this local unless the user explicitly authorizes disclosure to a named provider.
- `PUBLIC_QUERY` — the minimum generic question an external research tool needs. It may contain public category, company, role, behavior, regulation, or pricing terms, but no confidential combination of internal facts.

Do not paste the full working brief into an external engine. Before retrieval, inspect `PUBLIC_QUERY` for private offer names, exact nonpublic prices, named private targets, internal metrics, hypotheses, and combinations that reveal the strategy. If a useful public query cannot be formed without exposing private context, stop at `NO PERMISSION` and use local evidence or ask for authorization. This is a human-visible safety gate; tool availability is not permission.

## 2. Tool ladder

Use the cheapest method that can meet the answer contract:

1. Permissioned internal records and existing source receipts.
2. Free public first-party retrieval and authoritative web sources.
3. `python3 execution/research.py "<PUBLIC_QUERY>" --depth <quick|standard|deep|max> --json` for public-safe queries.
4. Approved quota- or cost-bearing actors such as Apify when ordinary retrieval cannot reach the required public evidence.
5. Permissioned customer interviews or manual market exposure.

Paid, quota-heavy, authenticated, outreach, CRM-write, and publishing actions remain approval-gated. A model or search tool judges nothing merely because it returned text.

## 3. Research status

Every run ends in one of these states:

- `VERIFIED RESEARCH EVENT` — successful retrieval with inspectable sources that meet the answer contract.
- `DEGRADED RESEARCH EVENT` — some sources were retrieved, but coverage, freshness, diversity, or tool failure limits the conclusion.
- `NO RESEARCH EVENT` — the engine failed, returned no inspectable sources, or the query was blocked. This is failure evidence about the route, not market evidence.
- `NO PERMISSION` — the next useful action would cross a privacy, cost, authentication, or external-action boundary.

Never silently replace a failed engine with model memory. Record the failed search and continue only through an allowed route.

## 4. Evidence floors

- A customer behavior, recurring pain, trigger, or language pattern needs three distinct cited sources, including at least one direct customer/action source, or it stays `MODELED`/`PROVISIONAL`.
- A price or competitor-scope claim needs a direct public offer page, proposal, invoice, or other inspectable primary source; otherwise use `UNKNOWN` or a clearly labeled range.
- A regulatory claim needs the governing or authoritative source.
- A Problem-Qualified Segment needs at least two independent evidence methods (for example observed behavior plus interview, purchase plus implementation record, or case-level action plus verbatim customer source). At least one must be case-level evidence tying the named action or language to the stated problem, consequence, and segment. An aggregate survey response alone does not qualify. Public company traces alone can produce only `PROVISIONAL`.
- Search-result snippets, model summaries, and repeated syndications are discovery aids, not independent corroboration.
- Absence is evidence only after the relevant sources, dates, and search terms are recorded.

## 5. Research Receipt

Attach this receipt to every externally researched deliverable:

```markdown
## Research Receipt
- Decision:
- PRIVATE_CONTEXT retained locally: [YES|NO + exception]
- PUBLIC_QUERY set:
- Tools/engines:
- Status: [VERIFIED RESEARCH EVENT|DEGRADED RESEARCH EVENT|NO RESEARCH EVENT|NO PERMISSION]
- Attempts and failures:
- Failed searches: [query/source checked + result]
- Sources: [count, domains, direct/indirect mix]
- Coverage dates:
- Cost/quota:
- Evidence floors met:
- Unresolved gaps:
```

For deep research artifacts, validate the report when available with:

```bash
python3 execution/research_quality_gate.py validate <report> --strict --depth deep --receipt
```

Validation proves structural and citation quality, not customer demand.
