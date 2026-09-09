# Angle Map source receipt · 2026-08-28

## Verdict

`REAL` research run. Fifteen market source URLs across fourteen domains were
accepted. Thirteen opened through native web. The two native failures were
recovered by direct public HTTP; Jina recovered one of those two and correctly
reported the other as blocked. No search snippet was promoted to verified
evidence.

## Acquisition summary

| Stage | Result | Cost |
|---|---:|---:|
| Market discovery | 15 queries | $0.00 |
| Native full-page reads | 13 PASS | $0.00 |
| Native failures | Google Help 429; The Grocer 405 | $0.00 |
| Direct HTTP fallback | 2/2 PASS | $0.00 |
| Jina fallback | 1 PASS; 1 BLOCKED | $0.00 |
| Tavily | NOT RUN | $0.00 |
| Accounts or dependencies created | 0 | $0.00 |

## Evidence accepted

| Source | Class | Acquisition | Grade | Use |
|---|---|---|---|---|
| [P&G 10-K](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm) | Primary filing | Native | VERIFIED | $3.8B Thorne agreement and closing boundary |
| [P&G rationale](https://us.pg.com/blogs/thorne/) | Official company | Native | VERIFIED | Trust, science, quality and practitioner credibility |
| [DIZZY product page](https://dizzysupps.com/shop) | Official product | Native | VERIFIED | One scoop, 12 ingredients, pricing and comparison |
| [DIZZY launch](https://www.thecheckout.eu/article/dizzy-launches-a-women-focused-daily-supplement) | Trade press | Native | VERIFIED | Launch date, audience and founder context |
| [NIQ consumer report](https://nielseniq.com/global/en/insights/analysis/2026/health-and-wellness-consumer-trends-the-rise-of-the-self-directed-health-consumer/) | Market research | Native | VERIFIED AS PUBLISHED | Self-directed, outcome-led health behavior |
| [PwC consumer report](https://www.pwc.com/gx/en/issues/c-suite-insights/voice-of-the-consumer-survey.html) | Market research | Native | VERIFIED AS PUBLISHED | Everyday health occasions across 21,808 consumers |
| [Current stack thread](https://www.reddit.com/r/Biohackers/comments/1vyldyx/rate_my_stack/) | Community | Native | VERIFIED AS BUYER TEXT | Current scene and 370-comment clarification |
| [All-in-one thread](https://www.reddit.com/r/Supplements/comments/1roe9a9/what_a_properly_dosed_allinone_actually_looks_like/) | Community | Native | VERIFIED AS BUYER TEXT | Counterevidence and buyer language |
| [Fool's Fix](https://foolsfix.com/) | Official product | Native | VERIFIED | Current recovery offer and pricing language |
| [Fool's Fix launch](https://www.thegrocer.co.uk/news/james-watt-unveils-fools-fix-detoxification-drink/722862.article) | Trade press | Direct after native 405 | VERIFIED | Launch reporting; Jina hit a security check |
| [Google GenAI report](https://support.google.com/webmasters/answer/16984139?hl=en) | Official documentation | Direct + Jina after native 429 | VERIFIED | AI Overview and AI Mode impression reporting |
| [Attaboy release](https://www.bevnet.com/pr/2026/08/06/attaboy-lab-continues-rapid-subscription-growth-adding-800000-in-monthly-arr-as-malar-expands-investment-ceo-joins-board) | Company release | Native | LIKELY, COMPANY-REPORTED | Subscription and multi-outcome positioning |
| [Isagenix WITHIN release](https://www.issuewire.com/isagenix-expands-microbiome-innovation-portfolio-with-within-a-5-in-1-daily-gut-immune-support-system-1873895632945060) | Company release | Native | LIKELY, COMPANY-REPORTED | Five-in-one launch pattern; no efficacy promotion |
| [Vogue longevity report](https://www.vogue.com/article/the-execs-guide-to-longevity-tech) | Editorial | Native | LIKELY | Longevity as identity and premium status |
| [GPO AI-search report](https://gpo.com/blog/august-2026-state-of-search-ai/) | Agency secondary | Native | DIRECTIONAL | Citation versus recommendation; excluded from public factual claims |

## What the routing proved

- Native web handled the primary sources and both Reddit threads, including the
  exact community language needed for the promises-not-kept receipt.
- Direct HTTP closed both named access gaps without another account or tool.
- Jina was useful on Google's large help page and failed honestly on The
  Grocer's security screen. It was not treated as a universal unlocker.
- Tavily had no unclosed gap to fill. Calling it would have consumed API credits
  without changing the research decision.

## Boundary receipt

- Paid calls: `0`
- Tavily calls: `0`
- New accounts: `0`
- Raw bodies persisted: `false`
- Login, cookies, CAPTCHA solving, proxies, authenticated scraping: `none`
- Publishing, outreach or contact: `none`
- Real subagents: `0`

The machine-readable receipt is
`daily/2026-08-28-angle-map-source-receipt.json`.
