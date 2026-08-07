# Evidence Analysis — hDBsQTK7VTc

## Source Role

Strategic/technical audit that turns crawl, analytics, search, content, citation, and competitor data into a prioritized work backlog.

## Timestamped Operational Mechanics

| Time | Mechanic | Evidence state | Operational use |
|---|---|---|---|
| 00:31-03:39 | Configure a lean Screaming Frog crawl, enable near-duplicate/spelling/semantic checks, and connect GA4, GSC, and PageSpeed data. | OBSERVED | Build one row-level audit table before prescribing work; V1 should import equivalent exports rather than require live APIs. |
| 03:40-06:01 | Flag indexable pages deeper than three clicks and pages with fewer than roughly five unique internal inlinks. | OBSERVED | Use thresholds as investigation triggers, then determine whether architecture or topic support is the cause. |
| 06:03-09:23 | Flag low performance scores (speaker uses below 80), then inspect representative pages on desktop and mobile. | OBSERVED | Prioritize sitewide fixes where a template issue affects many pages; keep the claimed LLM timeout mechanism UNCONFIRMED. |
| 09:24-11:31 | Distinguish intentional 404s from KPI-bearing accidental losses by joining status codes to traffic, impressions, clicks, events, and engagement. | OBSERVED | Redirect, restore, or consolidate only after preserving the page's measurable value. |
| 11:31-12:38 | Use fewer than 500 words as a thin-content flag, not an automatic command to add text. | OBSERVED | Route flagged pages to qualitative investigation, deletion, consolidation, or improvement. |
| 12:39-14:17 | Detect exact/near duplication with the crawl and a second scanner; investigate high-match pages while ignoring expected pagination. | OBSERVED | Separate structural duplication from genuinely competing assets. |
| 14:18-18:29 | Define cannibalization as same topic plus same intent; preserve commercial pages and buyer guides when their jobs differ. | OBSERVED | Require an intent comparison before merging or deleting similar-keyword pages. |
| 18:30-20:46 | Find off-topic assets, then preserve positive KPIs before pruning or reworking them. | OBSERVED | Keep the site's subject-matter boundary tight without destroying proven traffic value. |
| 20:47-22:49 | Evaluate cluster depth around priority topics; the example proposes 75-100 supporting assets around a pillar. | OBSERVED | Treat support depth as a hypothesis tied to importance/competition, not a universal publishing quota. |
| 22:50-25:35 | Let low impressions identify pages for qualitative review; established pages with no traffic, impressions, or backlinks become prune/rethink candidates. | OBSERVED | Use data to select the review set, then make a human quality decision. |
| 25:36-29:52 | Audit baseline placement and topic relevance; revisit aging pages against the current competitive corpus. | OBSERVED | Refresh when the live topic set changed; avoid chasing a tool score of 100. |
| 29:53-33:33 | Verify GSC positions 2-15 live, then test relevance, internal links, speed, and topic support before adding backlinks. | OBSERVED | Order low-hanging-fruit work from controlled/on-site levers to higher-cost authority work. |
| 33:34-36:14 | Treat established position-50-plus queries as potential missing-cluster demand, then build a dedicated relevant page if intent and demand hold. | OBSERVED | Convert impression evidence into a new-page hypothesis, not proof of future rank. |
| 36:15-40:28 | Pursue topic domination across own pages, YouTube, Reddit, and third-party pages already visible in the SERP. | OBSERVED | Choose surfaces from observed SERP presence; do not publish everywhere by default. |
| 40:29-42:39 | Run a commercial query across ChatGPT, Perplexity, Claude, and Grok; pool citation sources and locate brand-mention gaps. | OBSERVED | Create a citation opportunity ledger; external outreach remains outside V1. |
| 42:40-44:23 | Mine competitors' best-linked pages for repeatable formats, then transfer proven templates across industries. | OBSERVED | Preserve the framework while changing the subject and evidence. |
| 44:24-46:15 | Probe a model's static corpus without web access for brand knowledge, while explicitly accepting hallucination risk. | OBSERVED | Record only a rough observation; never treat model recall as ground truth. |

## Visual Ledger

| Time | Frame | What the frame proves | Boundary |
|---|---|---|---|
| 01:33 | `frames/cue_0000.jpg` | The audit begins inside Screaming Frog's configuration surface; the UI exposes crawl config plus analytics, search, speed, link, and AI integrations. | It does not show every checked crawl setting. |
| 02:29 | `frames/cue_0001.jpg` | Duplicate settings visibly enable near duplicates, restrict checking to indexable pages, and use a 90% near-duplicate threshold. | A 90% threshold is tool configuration, not a universal duplicate-content law. |
| 02:53 | `frames/cue_0002.jpg` | GA4, GSC, and PageSpeed are visibly connected in API Access; additional providers are listed separately. | V1 is import-first, so this proves desired fields—not authorization to add live connectors. |
| 10:26 | `frames/cue_0003.jpg` | The working sheet visibly joins crawl fields with GA4 sessions/views/engagement/key events, GSC clicks/impressions/CTR/position, and performance/core-vitals columns. | The frame does not isolate the 404 rows or independently total the five-million-impression claim. |
| 21:58 | `frames/cue_0004.jpg` | A live pillar asset titled `22 Best AI Search Rank Tracking Tools for 2025` is used as the cluster example. | The supporting-asset count and cluster performance are not visible in this frame. |
| 28:04 | `frames/cue_0005.jpg` | Rankability's optimizer list shows the `dashword alternatives` asset with score 45 and word count 957 before deeper review. | A tool score is a diagnostic state, not an observed rank lift. |
| 41:51 | `frames/cue_0006.jpg` | ChatGPT displays a sourced answer for SEO-book recommendations and exposes a sources control. | The specific citation list is not expanded; no outreach or coverage result is proven. |

## Contradictions, Drift, and Uncertainty

- The opening promises a complete battle plan and predictable results, while the workflow itself relies on personal thresholds, tool scores, and additional qualitative investigation. Preserve it as an audit protocol, not a result guarantee.
- The source uses live API connections; the approved system boundary is import-first. Reproduce the data contract and field mapping, not the connector behavior.
- The claim that LLM crawlers allow less than three seconds, the claim that relevance is the most important ranking factor, and the claimed two-to-four-position refresh lift are UNCONFIRMED by this source.
- The 75-100-asset cluster is a competitive-depth example, not a safe default for every project.
- Citation-gap outreach is an external action and must remain a recommended opportunity, not an automated V1 step.
- Screaming Frog, Rankability, model names, custom GPT availability, and citation behavior may drift from the 2025-09-22 publication context.
- Static-corpus probing is explicitly acknowledged by the speaker as hallucination-prone and only a rough ballpark.

## Cross-Source Corroboration Within This Creator Corpus

- `4tqCKkGilXI` expands the page-level crawl, intent, topic-coverage, and conversion checks used inside this sitewide audit.
- `lkFA-aBN_LM` expands topic domination and citation-source coverage into the larger search-everywhere architecture.
- This is same-creator repetition, not independent external validation.

