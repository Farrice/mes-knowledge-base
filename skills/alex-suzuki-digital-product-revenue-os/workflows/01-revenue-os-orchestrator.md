# Revenue OS Orchestrator

## Use When
The user wants a full Suzuki-style operating plan from raw product idea to sales post, funnel, launch path, proof gaps, and next action.

## Load First
- `../genius.md`
- `../references/source-ledger.md`
- `../references/revenue-mechanics.md`
- `../references/post-mechanics.md`
- `../references/funnel-map.md`
- `../references/scaling-mechanics.md`
- `../references/compliance-gate.md`
- `../references/composition-ledger.md`

## Inputs
- Product idea
- Buyer
- Price or intended price
- Proof available
- Platform
- Free asset or sample
- Launch timing

## Steps
1. **Intent lock**: summarize product, buyer, platform, price, and missing proof.
2. **Buyer readiness diagnosis**: classify likely buyers as cold, warm, ready, or wrong fit.
3. **Product path**: choose low-ticket checkout, trust container, application, or conversation path.
4. **Post design**: create one core post or thread using the raised 8-part sales post.
5. **Decision asset**: define the free asset that helps the buyer choose a lane and previews the paid result.
6. **Two-lane CTA**: create a value keyword and a purchase-intent keyword or equivalent reply path.
7. **Funnel map**: route comment/reply to DM, free asset, fit check, checkout/application, and follow-up.
8. **First-use path**: show what the buyer does in the first 30 minutes, 24 hours, 3 uses, or 7 days after purchase.
9. **Launch sprint**: create a 7-day calendar with main post, replay templates, replies, DM windows, email, and proof assets.
10. **Proof gate**: mark source claims, internal proof, assumptions, and missing assets.
11. **Floor test**: fail and run Launch Debugger if the output is only a question map, neutral report, or guide CTA with no paid-intent lane.
12. **Next action**: give one action that can be done today.

## Output Format
```markdown
# Suzuki Revenue OS - [Product]

## Intent Lock
[Product, buyer, price, platform, goal, assumptions]

## Sales Post
[Finished post or thread]

## Free Asset
[Asset name, promise, delivery method, buyer lane, why it previews the paid product]

## Buyer Readiness Diagnosis
[Cold, warm, ready, wrong-fit lanes and signals]

## Funnel Map
[Step-by-step route from post to value lane, purchase lane, checkout/application, and follow-up]

## First-Use Path
[What the buyer does after purchase or application]

## 7-Day Launch Sprint
[Daily actions, replay templates, reply windows, and proof assets]

## Proof Gaps
[What must be proven before publishing]

## Next Action
[One action]
```

## Quality Gate
- Names a real buyer.
- Gives a finished post, not a framework only.
- Has separate value and purchase-intent routing.
- Has a follow-up path by buyer intent.
- Has a first-use or first-7-day plan.
- Marks creator claims and assumptions.
- Fails question-map-only drafts and repairs them before delivery.

## Scale & Cold-Start Handoff
This orchestrator covers a single product's launch. Route onward when the goal is bigger:
- No product / no proof / cold start → `/suzuki` (Cold-Start Revenue Engine).
- Need an offer (build / partner / affiliate) → `/suzuki-product-source`.
- Autopilot the posting + DMs → `/suzuki-automate`.
- More than one launch / add accounts → `/suzuki-scale`.
- Deepest post pass (hook bank + swipe + AI-gen) → `/suzuki-post-lab`.
- Build a native funnel on another platform → `/suzuki-platform-engine`.
Always run the `compliance-gate.md` pass before delivery (claims labeled, disclosures present).
