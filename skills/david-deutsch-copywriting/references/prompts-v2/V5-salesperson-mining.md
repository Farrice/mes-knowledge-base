---
name: "Salesperson Mining Protocol"
source_prompt: "skills/david-deutsch-copywriting/references/prompts/V5-salesperson-mining.md"
skill: david-deutsch-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# Salesperson Mining Protocol

Extract tested copy from sales teams.

---

## Role & Activation

You are David Deutsch's sales mining methodology — salespeople talk to real prospects all day and already have the tested phrases, objection responses, and language that works; copy should mine that field data rather than invent language from scratch. Deploy before writing copy for any offer that already has a sales team or sales history.

---

## Input Required

- **[PRODUCT]**: What you're selling
- **[SALES_TEAM]**: Who to interview
- **[QUESTIONS]**: What to ask them

---

## Execution Protocol

1. **INTERVIEW** 3–5 salespeople — talk to a genuine cross-section of [SALES_TEAM], not just the top performer or the most available person
2. **ASK** "What do you say that works?" — capture their actual phrasing verbatim, not a paraphrase
3. **ASK** "What objections do you hear most?" — capture the objections in the prospect's own words, as reported by the salesperson
4. **DOCUMENT** proven phrases and responses — log verbatim language paired with the objection or moment it's used for
5. **EXTRACT** the highest-signal phrases — from the documented material, pull the tested language most directly usable in copy

---

## Output Contract

Deliver:
- **Interview log** — verbatim quotes from each salesperson interviewed, tagged by person
- **Objection inventory** — the objections reported, in the prospect's own words where captured
- **Tested phrase extraction** — the highest-signal, copy-ready phrases pulled from the interview log
- **Usage map** — which phrase pairs with which objection or sales moment

---

## Output Skeleton

```
INTERVIEW LOG
[Salesperson 1]: "[verbatim quote]" — context: [what question/moment prompted it]
[Salesperson 2]: "[verbatim quote]" — context: [...]
[Salesperson N]: "[verbatim quote]" — context: [...]

OBJECTION INVENTORY
[Objection, in prospect's own words as reported] — frequency noted by: [which salespeople raised it]
[Objection 2] — [...]

TESTED PHRASE EXTRACTION
[Copy-ready phrase, pulled verbatim from interview log] — source: [salesperson]
[Copy-ready phrase 2] — source: [salesperson]

USAGE MAP
[Phrase] → pairs with objection/moment: [which]
[Phrase] → pairs with objection/moment: [which]
```

---

## Quality Gate

- [ ] Every quote in the interview log is verbatim from an actual interview, not paraphrased or invented
- [ ] At least 3 distinct salespeople are represented in the interview log, per the stated protocol
- [ ] Every objection in the inventory is attributed to what was actually reported, not assumed
- [ ] Extracted phrases are the salesperson's real language, not rewritten to sound more "polished"
- [ ] No phrase or objection is presented as field-tested if it was not actually gathered from [SALES_TEAM]

---

## Deploy When

- Writing copy for an offer that already has a sales team or sales call history
- Copy feels generic or "written," disconnected from how the offer actually closes in real conversations
- Building an objection-handling section for a sales page or script
