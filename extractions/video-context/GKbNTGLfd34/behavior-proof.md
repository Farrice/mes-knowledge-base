# Behavior proof: advice to operating loop

## Before

A cold-start request such as “take this client from zero to a large LinkedIn audience” could produce a static plan, generic calendar, and untested hook list. It had no shared client state, no deterministic idea ranking, no post ledger, and no false-green check for empty data.

## Source mechanic applied

- Profile: what you do + who you help + outcome.
- Queue: attention potential 1-5 + time to create 1-5.
- Production: surprising or actionable; body first, then hook choices.
- Learning: record saves, reposts, impressions, follower growth, leads, and revenue.
- Review: top patterns after 10 posts; top 10 after every 100.

## After

`execution/linkedin_growth_os.py` now initializes a portable account workspace, rejects invalid idea scores, ranks the queue, refuses to review an empty ledger, calculates follower efficiency and depth rate from recorded events, and produces a decision report with an explicit causality limit.

## Cold-start run

```bash
python3 execution/linkedin_growth_os.py init \
  --name "Example Expert" --offer "Advisory" --icp "B2B founders" \
  --outcome "qualified demand" --mechanism "source-grounded content" \
  --output .tmp/linkedin-example
python3 execution/linkedin_growth_os.py doctor --workspace .tmp/linkedin-example
```

Expected behavior: the first command creates the account state; the second returns `LinkedIn growth workspace: PASS`.

## Negative controls

- Idea scores outside 1-5 return exit code 2.
- Reviewing an empty post ledger returns exit code 2.
- Removing a required workspace file makes `doctor` fail.

## Proof state

Local runtime behavior: `VERIFIED` by `execution/test_linkedin_growth_os.py`.

Follower growth and revenue: `NO EVENT`; they require real publication and account data.
