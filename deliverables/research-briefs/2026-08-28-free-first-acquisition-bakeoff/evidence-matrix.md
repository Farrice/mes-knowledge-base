# Free-First Research Acquisition Bakeoff

- Fixture: `health-performance-real-corpus-30`
- URLs: 30
- Paid calls: 0
- Accounts created: 0
- Methods: direct public HTTP; Jina Reader public no-key endpoint
- Raw page bodies persisted: no
- Tavily: NOT RUN — account overage boundary not independently verified

## Method Summary

| Method | PASS | PARTIAL | BLOCKED | FAIL | Usable rate | Median latency | Cost |
|---|---:|---:|---:|---:|---:|---:|---:|
| direct_http | 24 | 0 | 0 | 6 | 80% | 435 ms | $0.00 |
| jina_reader | 24 | 0 | 6 | 0 | 80% | 562 ms | $0.00 |

## Evidence Matrix

PASS means usable content and at least one expected signal (or a valid PDF payload). PARTIAL means content arrived but was thin or missed the expected signal. BLOCKED and FAIL remain failures; the harness performs no CAPTCHA or authentication escalation.

| ID | Class | Domain | Direct HTTP | Jina Reader | Better zero-dollar path |
|---|---|---|---|---|---|
| official-01 | official_guidance | www.fda.gov | PASS (200) | PASS (200) | jina_reader (tie) |
| official-02 | official_guidance | www.fda.gov | PASS (200) | PASS (200) | direct_http (tie) |
| official-03 | official_guidance | www.ftc.gov | PASS (200) | PASS (200) | jina_reader (tie) |
| official-04 | official_guidance | www.ftc.gov | PASS (200) | PASS (200) | direct_http (tie) |
| official-05 | official_guidance | leginfo.legislature.ca.gov | PASS (200) | PASS (200) | direct_http (tie) |
| editorial-01 | editorial_legal | www.asa.org.uk | PASS (200) | PASS (200) | direct_http (tie) |
| editorial-02 | editorial_legal | www.nsf.org | PASS (200) | PASS (200) | direct_http (tie) |
| editorial-03 | editorial_legal | www.nutraingredients.com | PASS (200) | PASS (200) | jina_reader (tie) |
| editorial-04 | editorial_legal | www.nutraingredients.com | PASS (200) | PASS (200) | direct_http (tie) |
| editorial-05 | editorial_legal | www.nutraceuticalsworld.com | PASS (200) | PASS (200) | direct_http (tie) |
| editorial-06 | editorial_legal | topclassactions.com | PASS (200) | PASS (200) | jina_reader (tie) |
| editorial-07 | editorial_legal | athletechnews.com | PASS (200) | PASS (200) | jina_reader (tie) |
| editorial-08 | editorial_legal | www.nutritioninsight.com | PASS (200) | PASS (200) | jina_reader (tie) |
| editorial-09 | editorial_legal | www.nutritionaloutlook.com | PASS (200) | PASS (200) | direct_http (tie) |
| editorial-10 | editorial_legal | www.foodmanufacture.co.uk | PASS (200) | PASS (200) | jina_reader (tie) |
| brand-01 | brand_product | ritual.com | PASS (200) | PASS (200) | jina_reader (tie) |
| brand-02 | brand_product | ritual.com | PASS (200) | PASS (200) | jina_reader (tie) |
| brand-03 | brand_product | eightx.co | PASS (200) | PASS (200) | direct_http (tie) |
| brand-04 | brand_product | evolutagency.com | PASS (200) | PASS (200) | jina_reader (tie) |
| brand-05 | brand_product | segwise.ai | PASS (200) | PASS (200) | jina_reader (tie) |
| community-01 | community | www.reddit.com | FAIL (200) | BLOCKED (200) | none - use native web or mark gap |
| community-02 | community | www.reddit.com | FAIL (200) | BLOCKED (200) | none - use native web or mark gap |
| community-03 | community | www.reddit.com | FAIL (200) | BLOCKED (200) | none - use native web or mark gap |
| community-04 | community | www.reddit.com | FAIL (200) | BLOCKED (200) | none - use native web or mark gap |
| community-05 | community | www.reddit.com | FAIL (200) | BLOCKED (200) | none - use native web or mark gap |
| community-06 | community | www.reddit.com | FAIL (200) | BLOCKED (200) | none - use native web or mark gap |
| community-07 | community | sellercentral.amazon.com | PASS (200) | PASS (200) | direct_http (tie) |
| pdf-01 | pdf | www.ftc.gov | PASS (200) | PASS (200) | jina_reader (tie) |
| pdf-02 | pdf | ods.od.nih.gov | PASS (200) | PASS (200) | jina_reader (tie) |
| pdf-03 | pdf | ods.od.nih.gov | PASS (200) | PASS (200) | jina_reader (tie) |

## Class Breakdown

### brand_product

- `direct_http`: PASS=5, PARTIAL=0, BLOCKED=0, FAIL=0
- `jina_reader`: PASS=5, PARTIAL=0, BLOCKED=0, FAIL=0

### community

- `direct_http`: PASS=1, PARTIAL=0, BLOCKED=0, FAIL=6
- `jina_reader`: PASS=1, PARTIAL=0, BLOCKED=6, FAIL=0

### editorial_legal

- `direct_http`: PASS=10, PARTIAL=0, BLOCKED=0, FAIL=0
- `jina_reader`: PASS=10, PARTIAL=0, BLOCKED=0, FAIL=0

### official_guidance

- `direct_http`: PASS=5, PARTIAL=0, BLOCKED=0, FAIL=0
- `jina_reader`: PASS=5, PARTIAL=0, BLOCKED=0, FAIL=0

### pdf

- `direct_http`: PASS=3, PARTIAL=0, BLOCKED=0, FAIL=0
- `jina_reader`: PASS=3, PARTIAL=0, BLOCKED=0, FAIL=0

## Boundary Receipt

- Public URLs only.
- No login, cookies, private data, contact enrichment, CAPTCHA solving, or proxy rotation.
- No paid provider, new dependency, API key, account, scheduler, or background worker.
- This matrix measures acquisition, not truth. Evidence promotion still requires source and claim review.

## Native Web Reference Sample

The host-native reader was independently spot-checked on six sentinel URLs after
the automated matrix. This is a reference sample, not a claim of 30-URL native
coverage.

| ID | Class | Native web result | What it changed |
|---|---|---|---|
| official-01 | official_guidance | PASS | Confirmed ordinary official-page reading. |
| editorial-02 | editorial_legal | TIMEOUT | Native web is not universally more reliable. |
| brand-01 | brand_product | PASS | Confirmed product-page reading. |
| community-01 | community | PASS | Recovered a Reddit page both automated transports missed. |
| community-07 | community | PASS | Confirmed public forum reading. |
| pdf-01 | pdf | PASS | Opened the 42-page FTC PDF for page-level reading. |

Reference sample: 5/6 readable, including the unique Reddit recovery. Therefore
native web stays first; direct HTTP handles ordinary known URLs; Jina is a
conditional text/PDF fallback; failed community URLs become explicit gaps when
native web is unavailable.

## Dependency Decision

**Recommendation after the evidence matrix: install nothing.** Existing tools
cover 24/30 URLs through either zero-dollar transport, all 23 non-community
pages, the Amazon seller forum, and all three PDFs. The remaining six failures
are source-specific Reddit access, and the native reader recovered the sampled
Reddit page. A new dependency would add maintenance before proving incremental
coverage.
