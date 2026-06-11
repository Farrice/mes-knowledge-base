# Personal Finance And Subscription Audit - 2026-05-20

## Read This First

This is an analyze-only audit. I did not send emails, cancel services, change subscriptions, move money, or touch any bank account.

The Wells Fargo CSV is now the cashflow source of truth for the checking accounts included in the export. Gmail remains the receipt and subscription discovery layer. Gmail also showed a Plaid/Wells Fargo connection notice for ChatGPT on May 19, 2026, but this Codex session does not expose a callable Plaid or Wells Fargo transaction tool. The provided CSV is therefore the verified bank ledger for this pass.

The CSV uses negative amounts for inflows, so I normalized inflows to positive cash received and outflows to positive cash spent.

## Coverage

| Data source | Status | What it proves | Main gap |
| --- | --- | --- | --- |
| Wells Fargo CSV | Used | 149 checking-account transactions from Feb 19, 2026 to May 19, 2026 | Does not itemize the credit-card transactions behind the card payments |
| Gmail receipts and invoices | Used | Subscription names, renewal periods, payment confirmations, trial warnings, non-Wells receipts | Cannot replace the bank ledger or prove every charge posted |
| Wells Fargo alerts in Gmail | Used | Low-balance, negative-balance, and insufficient-funds pressure | Alert emails are not a complete transaction history |
| Plaid/Wells connection notice | Observed only | Confirms a connection notice existed | Not callable from this Codex environment |

Important gap: the Wells export includes $1,305.00 in payments to the Signify Business Essential Card ending in 6844. It does not include the merchant-level charges inside that card. This means the checking-account cashflow totals are real, but the full household/business spending map is still incomplete until that card export is added.

## 90-Day Cashflow Snapshot

| Snapshot item | Amount |
| --- | ---: |
| Total inflow | $2,868.01 |
| Total outflow | $4,964.36 |
| Net cash gap | -$2,096.35 |
| Normalized monthly inflow | $956.00 |
| Normalized monthly outflow | $1,654.79 |
| Normalized monthly gap | -$698.78 |
| Bank-visible repeated subscription/service stack | about $419/month |
| Financial fees in period | $220.00 |

The direct read: over this 90-day window, the checking accounts spent about $2,096 more than they brought in. Normalized monthly, the current account pattern is short by about $699/month before any missing credit-card detail is added.

## Monthly Cash-In / Cash-Out

February and May are partial months in the export, so treat them as directional.

| Month | Cash in | Cash out | Net | Rows |
| --- | ---: | ---: | ---: | ---: |
| Feb 19-29, 2026 | $0.00 | $947.43 | -$947.43 | 30 |
| Mar 2026 | $350.02 | $1,418.25 | -$1,068.23 | 31 |
| Apr 2026 | $1,817.99 | $1,359.66 | $458.33 | 48 |
| May 1-19, 2026 | $700.00 | $1,239.02 | -$539.02 | 40 |

April only turned positive because of a $1,200 check deposit plus platform transfers. The underlying recurring spend did not materially relax.

## Spending Habit Map

| Category | 90-day outflow | Habit read |
| --- | ---: | --- |
| Transfers | $1,446.64 | Mostly credit-card payments plus Splitwise. Needs card export before it can be categorized. |
| Services | $1,373.05 | The biggest visible controllable leak: AI tools, creative tools, subscriptions, software, shipping. |
| Entertainment | $696.74 | Events, TV/movies, music/audio, and entertainment spikes. |
| Dining and drinks | $269.13 | Fast food and coffee are not the main leak, but they add pressure when balances are near zero. |
| Other | $228.29 | Needs review because uncategorized spend hides decisions. |
| Financial | $220.00 | Overdraft and monthly service fees. This is a fixable leak. |
| Transportation | $185.56 | Fuel and parking. |
| Education | $147.00 | Coursera recurring at $49/month. |
| Shopping | $117.18 | Mostly Amazon/online marketplaces. |
| Gifts/donations | $105.00 | Payment-app/gift category, should stay separate from normal spending. |
| Groceries | $64.83 | Not the main pressure point in this CSV. |
| Housing | $59.97 | Ring subscription. |
| Pets | $44.97 | PetSmart. |
| Health/wellness | $6.00 | Minimal in this export. |

## Subscription Cancellation Board

| Service or leak | Monthly amount | Status | Evidence | Priority | Recommendation |
| --- | ---: | --- | --- | --- | --- |
| Anthropic Max | $100.00 | Confirmed recurring, not in Wells CSV | Gmail receipt paid May 12 | 1 | Downgrade/cancel unless it is producing paid work this week. |
| LinkedIn Sales Navigator | $89.99 | Likely recurring, paid outside this Wells export | Gmail/Apple confirmation | 1 | Keep only if it is tied to daily prospecting and booked calls. |
| Genspark Plus | $74.99 | Confirmed recurring, likely outside this Wells export | Gmail receipt paid Apr 29; older Wells Genspark charge differs | 1 | Cancel/pause unless it has a unique job. |
| Coursera | $49.00 | Wells-confirmed recurring | Three $49 charges | 1 | Cancel if not actively completing weekly modules. |
| Apple/App Store stack | about $108 avg | Wells-confirmed aggregate, itemized by Apple receipts | 14 Wells Apple charges totaling $323.75 | 1 | Review App Store subscriptions directly; Apple aggregation is hiding decisions. |
| Abacus.ai | $20.00 | Wells-confirmed recurring-ish | Four $20 charges; one overdraft fee tied to this charge | 1 | Cancel unless mission-critical. |
| Grammarly | $30.00 | Wells-confirmed recurring | Three $30 charges | 2 | Keep only if used daily for revenue work. |
| Kittl | $30.00 | Wells-confirmed recurring | Three $30 charges plus Gmail receipt | 2 | Keep only if it replaces other design tools. |
| Gamma | $25.00 | Wells-confirmed recurring | Three $25 charges plus Gmail receipt | 2 | Keep only if it is the main deck/output tool. |
| Perplexity | about $20 | Wells-confirmed recurring-ish | Three $20 charges plus Gmail usage/credit invoice | 2 | Verify plan and cap/cancel if overlapping with other AI tools. |
| Spotify | $21.99 | Wells-confirmed recurring | Three charges | 3 | Lifestyle review if cash is tight. |
| Ring AI Pro | $19.99 | Wells-confirmed recurring | Three charges | 3 | Keep only if genuinely needed. |
| Hulu | $18.99 | Wells-confirmed recurring | Three charges | 3 | Lifestyle review. |
| YouTube | $14.99 | Wells-confirmed recurring | Three charges; one overdraft fee tied to this charge | 2 | Cancel or move off the low-balance account. |
| Canva | $12.95 | Wells-confirmed recurring | Four charges plus Gmail invoice | 2 | Probably keep only if it is the chosen core design tool. |
| Amazon Prime Video | $6.99 | Wells-confirmed recurring | Four charges | 3 | Cancel if duplicated by Hulu/YouTube/other entertainment. |
| ChatGPT Exporter Pro | $3.99 | Wells-confirmed recurring | Three charges plus Gmail receipt | 3 | Cancel if native export or manual archive is enough. |
| Claude Exporter Pro | $3.98 | Wells-confirmed recurring | Three charges plus Gmail receipt | 3 | Cancel if duplicated by ChatGPT Exporter. |
| Google Cloud/API | $3-$6 variable | Wells/Gmail visible variable | Small recurring Google charges | 2 | Set billing caps or shut off unused projects. |
| Google One | $249.99 annual-ish | Wells-confirmed one-time/annual | One Mar 24 charge | 2 | Review renewal date and storage need; do not treat as monthly unless confirmed. |
| Lovart, Luma, Magnific, fal, Recall, Wispr, Snipo, Apify | varies | Gmail-confirmed or one-off visible | Receipts and invoices | 2 | Consolidate; keep only tools with a current job and revenue purpose. |
| Monthly service fees | about $30/mo | Wells-confirmed fee leak | $80 total in this export | 1 | Ask bank about waiver rules or consolidate accounts if appropriate. |
| Overdraft fees | $140 total | Wells-confirmed fee leak | Four $35 fees | 1 | The fastest non-subscription fix is preventing small recurring charges from hitting a low-balance account. |

## Cash Leak List

| Leak | Amount | Why it matters |
| --- | ---: | --- |
| Financial fees | $220.00 | Fees are not buying anything. The overdraft fees alone equal several subscriptions. |
| Credit-card payments without itemized card ledger | $1,305.00 | This hides the real merchants behind a large part of outflow. |
| Apple aggregation | $323.75 | Apple bundles many subscriptions and app purchases, making cancellation decisions harder. |
| Digital service stack | $1,355.26 | This is the largest named spending category after transfers. |
| Event/entertainment spikes | $696.74 | These are occasional but large enough to wipe out small inflows. |
| Payment-app ambiguity | $141.64 Splitwise out plus Zelle activity | These need labels: reimbursement, gift, shared cost, transfer, income, or expense. |
| One-time/annual surprise charges | $249.99 Google One, plus other isolated tool charges | Annual or prepaid charges create cash dips if they are not planned. |

## Reconciliation Verdicts

| Bucket | Items |
| --- | --- |
| Confirmed recurring from Wells | Canva, Gamma, Coursera, Kittl, Grammarly, Spotify, Hulu, YouTube, Ring, Abacus.ai, Amazon Prime Video, Perplexity, ChatGPT Exporter, Claude Exporter, Apple/App Store stack, monthly service fees |
| Confirmed or likely recurring from Gmail but not fully visible in Wells | Anthropic Max, LinkedIn Sales Navigator, Genspark, Apify, Wispr Flow, Recall, Snipo, Lovart, Magnific, CapCut future renewal |
| One-time, annual, or usage-style | Google One, Higgsfield, Moonshot/Kimi, Luma partial-period, fal/API usage, event purchases |
| Income or transfer, not normal spending | PayPal, Shopify, Zelle deposits, ATM/check/cash deposits, Signify card payments, Splitwise payments |
| Needs user review | Adobe, Audible, Napkin, domain/Squarespace/Google Workspace renewals, Kimi/Moonshot cancellation status, itemized Signify card charges |

## Income Gap View

| Income source | 90-day amount | Read |
| --- | ---: | --- |
| Check/cash deposits | $1,245.00 | Largest inflow source, but lumpy. |
| PayPal transfers/payments | $948.52 | Real cashflow channel, not yet steady enough to cover recurring burn. |
| Shopify transfer | $374.49 | Evidence of monetizable online activity. Worth investigating. |
| Zelle deposits | $300.00 | Includes gifts and at least one marketing-strategy memo. Keep business income separate from gifts/reimbursements. |

Observed income is real, but unstable. The current recurring-service stack behaves like fixed monthly overhead, while income behaves like occasional lumps. That mismatch is the budget problem.

## Fastest Cash Impact

| Move | Monthly relief or effect | Why it ranks high |
| --- | ---: | --- |
| Cancel/downgrade Anthropic Max, Genspark, LinkedIn Sales Navigator | up to $264.98 | Three decisions could remove the largest Gmail-visible external-card burn. |
| Cancel Coursera, Abacus.ai, and one of Grammarly/Kittl/Gamma | $99-$129 | Wells-confirmed and directly recurring. |
| Review Apple subscriptions and cancel hidden App Store items | likely $20-$70+ | Apple is the biggest aggregator and needs direct subscription review. |
| Stop overdraft cycle with a $100 recurring-charge buffer | avoids $35 per hit | Four fees cost $140 in this period. |
| Export Signify card transactions | not direct relief, but essential truth | $1,305 in payments cannot be categorized without it. |
| Productize a same-day AI/tool-stack audit | $75-$150 per client | This audit itself reveals a service pain other creators/operators have. |
| Sell a short marketing strategy memo | $100-$250 per brief | The CSV already shows at least one $100 strategy-memo inflow. |
| Reactivate the Shopify path deliberately | variable | A $374.49 Shopify transfer is evidence, but it needs a repeatable offer/product before relying on it. |

## Immediate Action List

1. Review/cancel the Priority 1 items first: Anthropic Max, Genspark, LinkedIn Sales Navigator, Coursera, Abacus.ai, bank monthly fees, and overdraft triggers.
2. Open Apple subscriptions and classify every Apple charge: iCloud, Crunchyroll, CapCut, app purchases, storage, entertainment, and unknowns.
3. Export the Signify Business Essential Card transaction CSV for the same date range.
4. Move recurring charges away from any account that often dips below $100, or create a dedicated subscription buffer.
5. Label payment-app flows as income, transfer, reimbursement, shared expense, gift, or normal spending.
6. Keep only one core design/output stack until income stabilizes: for example Canva plus one specialist tool, not Canva plus Kittl plus Gamma plus Lovart plus Luma plus Magnific.

## Bottom Line

This is not just a "spend less on coffee" situation. The clearest pattern is unstable inflow colliding with a dense subscription/tool stack and low-balance timing. The Wells CSV shows a 90-day gap of $2,096.35 and a normalized monthly gap of about $699. The fastest fix is a cancellation sprint plus a fee-prevention rule, followed by the missing credit-card export so the hidden $1,305 in card-paid spending can be mapped.
