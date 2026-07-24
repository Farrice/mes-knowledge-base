---
description: "Riley Brown's ad factory — take a winning ad's proven STRUCTURE (never its copy or its people), swap in your brand, and mass-produce on-brand variations. Structure-theft not copy-theft; volume is the goal; never carry a real byline."
---

# /riley-template-steal-ads — Winning Ad → On-Brand Variant Batch

Riley's template-steal doctrine (Pattern 13, Exemplar 2): "we're basically just going to use them as templates for our own ads... You want to experiment a lot with ads... Would we ever do this word for word? We would change it more than this." The proven ad's *structure* is the reusable template; brand-swap + image-gen turns one winner into a test batch. **The named failure to never repeat** (Hidden Knowledge #10): Codex kept the competitor's real byline "Dr. Fahim Hussain" on the rebranded ad. Our gate bans any real name/person/byline carryover.

## Pre-Flight Gate

Load `genius.md` first. Proceed if:
- You have a winning ad to work from (ideally #1 longest-running from `/riley-ad-spy`).
- You have brand truth to swap in (a DESIGN.md, or run `/riley-brand-scrape` first).
- You accept the floor: **structure borrowed, brand native** — a cold viewer must not clock the source ad; and **zero real names/bylines/people** carried over.

## Skill Acquisition

- `genius.md` — Pattern 13, Exemplar 2, Hidden Knowledge #10
- `references/source-quotes.md` — Exemplar 2 regenerate prompts + the byline failure
- Live infra: `.agent/workflows/creative-from-winners.md` (the full structure-transfer + production routing)

## Execution

Run `/creative-from-winners` — it implements Riley's improvised pipeline on our creative stack (his was Paper.design; ours routes Dara / Fantastic Studio / Canva / Higgsfield):
1. **Ground the winner.** Pull the source ad from the Social Intelligence DB (`/riley-ad-spy` output). Extract its **skeleton only**: offer framing, hook mechanism, visual hierarchy (what you read 1st/2nd/3rd), CTA type, proof element — never its literal copy, and **never its people/bylines**.
2. **Ground the brand.** Load brand truth (client DESIGN.md or `/riley-brand-scrape` output; Farrice's own via `_active/farrice-brand/`). Never hand a bare prompt to a generator.
3. **Structure transfer, not clone.** Route by need: static concepts + test plan → `/dara-static-engine`; full art direction → Fantastic Studio; copy skeleton on the winner's structure → `/copy-engine` or Luke Iha hooks. Riley's line: "Change nothing else except the colors to match the [brand]" — but the *floor* is his other line: "we would change it more than this." One structure → **3+ divergent executions** (volume is the point).
4. **Produce.** Canva MCP (layout-true statics) / Higgsfield Soul (people; pre-flight `creative_router.py`) — cost/credit-gated; surface cost before batch generation, never auto-spend.
5. **Close the loop.** Write finished variants back to the source's Social Intelligence page (`Media`). Offer `/jam` on taste-bearing picks.

## Content Type Adaptations

| Winner type | Adaptation |
|---|---|
| Static image ad | Dara static engine — format swap + objection engine on the proven skeleton |
| Founder/person ad | **regenerate the person as your own** — never reuse the source's face or name |
| Comparison ad | keep the David/Goliath structure; swap both sides to your framing |
| Video ad | extract hook/beat structure; produce as new (don't re-cut theirs) |

## Output Requirements

- **3+ divergent** on-brand executions from one proven structure — a test batch, not one clone.
- Zero real names / bylines / faces from the source (hard gate).
- Copy passes `prose_classifier.py check` + reader-contract dials.
- Variants written back to the Notion source record.

Execution prompt: references/prompts-v2/on-brand-ad-variant-batch.md — honor its Output Contract.

## Quality Gate

A cold viewer can't clock the source ad? · **No real byline/person/name carried over (the Dr. Fahim Hussain check)?** · Structure borrowed, brand native? · 3+ divergent variants, not a single copy? · Generator cost surfaced before spend?
