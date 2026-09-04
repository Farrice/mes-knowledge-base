# First Home Valley Decision Check

Private browser prototype for the 6-3-2 buyer-routing hypothesis.

## What it does

- Collects five structured choices and one optional sentence.
- Routes by the buyer's current blocker, with one optional secondary blocker.
- Gives a useful result before asking whether Jen should help.
- Separates the buyer route from the service state: active conversation, nurture, or route out.
- Checks existing representation and follow-up consent.
- Flags safety/schools, financing, and legal/title language for a human boundary response. It never makes those decisions.
- Saves and transmits nothing.

## Private test

Open `index.html` in a browser and complete the flow. The prototype is not approved for public linking, lead collection, analytics, or automated decisions.

Run the deterministic journey test from this folder:

```bash
node test-decision-logic.mjs
```

Expected receipt: `PASS 12/12 diagnostic journeys`.

## Hold before public use

Jen and her broker must approve the buyer-facing wording, data handling, representation check, privacy notice, lender boundary, and fair-housing redirect. Choose the delivery and record system only after the manual conversation test shows repeated value.

