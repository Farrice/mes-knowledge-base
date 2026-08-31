# Frozen Kallaway → Growth Blueprint Run Receipt

- **Client fixture:** `fixture-bravo@example.com` — $89/month mobility cohort for desk workers.
- **Source:** `extractions/kallaway/validation/fixtures/fixture-pack.json` — six synthetic YouTube rows, generated 2026-08-27.
- **Cost:** $0. No web fetch, API, paid enrichment, connector write, publishing, or outreach.
- **Route:** `/ai-topic-mining` → Growth Blueprint state chain → `/gb-blueprint` → client render → PDF.
- **Evidence behavior:** one row qualified for topic use; three were format-only; two were excluded for wrong-buyer topics. Forty-four missing top-50 rows were not fabricated.
- **Human boundary:** clinical opinion, prescription, contraindications, story, voice, final approval, and publishing remain human-owned.
- **Produced outputs:** client HTML, five-page PDF, eight state artifacts, manifest, render source, context pack, and this receipt.

## Acceptance checks

| Check | Result | Proof |
|---|---|---|
| Client HTML contains no operator-only language | **PASS** | `client_package_lint.py`: 0 findings |
| PDF is readable and larger than 1 KB | **PASS** | 5 pages; 230,820 bytes; 823 extracted words |
| Reader-facing prose clears the anti-slop gate | **PASS WITH STRUCTURAL WARNING** | Main headings and paragraphs scored 2.0/10; the only hit was the required `source ledger` heading. Full-page UI labels were excluded from the prose sample. |
| Every client-facing number is fixture-backed or labeled as a proposed threshold | **PASS** | Source ledger, bet register, and money-map labels are present in HTML and PDF. |
| Synthetic attention is not described as demand, conversion, clinical, or revenue proof | **PASS** | The limitations section survives PDF extraction and explicitly names each unsupported proof class. |
| Human creative ownership is visible | **PASS** | Clinical judgment, exercise choice, contraindications, story, voice, approval, and publishing are assigned to the founder. |
| Literal `/ai-topic-mining` route resolves without hijacking broader routing | **PASS** | Kallaway verifier positive and negative controls passed. |
| Signal-pack v2 and Kallaway skill system remain complete | **PASS** | 22/22 completion checks; signal-pack sabotage suite 14/14; lead-magnet suite 43/43. |
| JSON and repository whitespace validation | **PASS** | Four JSON artifacts parsed; `git diff --check` returned clean. |

## Client deliverables

- `exports/fixture-bravo-mobility-growth-blueprint/fixture-bravo-mobility-growth-blueprint-brief-client.html`
- `exports/fixture-bravo-mobility-growth-blueprint/fixture-bravo-mobility-growth-blueprint.pdf`

## Honest proof boundary

This run proves that the frozen Kallaway evidence can flow through the connected skill system into a client-readable Growth Blueprint without spending money, inventing missing research, or laundering AI output into a clinician's judgment. It does not prove live market demand or business results. Those require a current scan plus first-party publication and conversion receipts.
