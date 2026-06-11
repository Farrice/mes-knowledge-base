# RISKS — Locals' Go/No-Go App (working name "Lowkey", uncleared)

Flagged per flag-risks-early rule. Ordered by severity.

## 1. Disney IP / Trademark — HIGH
- "Disney," "Disneyland," "Magic Key," castle imagery, character likenesses: all off-limits in name, icon, branding, and App Store metadata. Every incumbent (Touring Plans, MouseWait, Thrill Data) operates as explicitly "unofficial" — viable path, but Disney polices aggressively, and App Store review sometimes rejects Disney-adjacent metadata on rights grounds.
- Demo uses "SoCal Annual" (generic) instead of Magic Key tier names; keep that discipline through launch.
- Naming status: **nothing is cleared.** "Parkcast" collides with a UK theme-park podcast (same industry — avoid). "Gatecheck" collides with industrial security apps (different class, weaker risk). "Lowkey"/"Gatekeep" are generic words — clearance search required before any spend.

## 2. Data sourcing — HIGH
- The forecast engine needs wait-time history + live signals. Realistic sources: queue-times.com-style aggregators, Thrill Data-style scraping of Disney's app API. Disney's API is unofficial/undocumented; access can break or be revoked at any time. This is the single biggest operational dependency — same risk every incumbent silently carries.
- Magic Key reservation-availability data (for the rare-combo alerts) requires scraping Disney's reservation calendar — most fragile and most legally gray surface. Ship v1 with manual/blockout-calendar data (published publicly) and add live reservation scraping later, eyes open.

## 3. Platform risk — MEDIUM
- Disney could expand its official app. Mitigation is structural: Disney will never tell guests "don't come today" (revenue conflict), so the verdict layer is durably ours. But Disney CAN improve official crowd transparency enough to dull the edge.
- Apple App Store: crowd apps are accepted today (MouseWait, Lines live there), but Disney complaints have gotten apps pulled before. Keep branding scrupulously clean.

## 4. Market size ceiling — MEDIUM
- Single-resort locals app: pass-holder base estimated in the high hundreds of thousands (Disney doesn't publish; UNCONFIRMED), of which a paid-conversion sliver. ~$1M ARR realistic ceiling at $39/yr. Fine for an indie/side business, not venture-scale. Expansion path: WDW + Universal with the same engine.

## 5. Forecast accuracy = the entire brand — MEDIUM
- One badly-called "go-day" that turns out packed destroys trust faster than any feature wins it. Mitigation: publish accuracy receipts (turns the risk into the trust moat), under-promise on far-out dates, and label confidence like a weather forecast.
