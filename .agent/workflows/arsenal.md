---
description: See what you already have — task-matched browse across every skill, workflow, agent, and front door. The anti-rebuild surface. Backed by execution/arsenal.py.
---

# /arsenal — What Do I Already Have For This?

The system builds faster than anyone can remember. 378 skills · 231 agents · ~2,500 skill
workflows · ~1,900 command workflows. `/recommend` names an expert and advises a path;
`/find-skill` names a skill. **`/arsenal` names the exact thing to fire** — and shows what you
built and forgot.

Reach for it *before* building anything, and any time you want a refresher on the arsenal.

## Invocation

```bash
python3 execution/arsenal.py "<what you're trying to do>"   # task-matched
python3 execution/arsenal.py --family <skill-name>          # one family, in full
python3 execution/arsenal.py --unused                       # forge-grade, no routing evidence
python3 execution/arsenal.py --new 14                       # built in the last 14 days
python3 execution/arsenal.py --stats                        # shape of the whole arsenal
```

// turbo
```bash
python3 execution/arsenal.py "$ARGUMENTS"
```

## Steps

1. **Run it** with whatever Farrice typed after `/arsenal`. No arguments → `--stats`.
2. **Read the output, don't re-list it.** The CLI output is already the deliverable. Add only
   what the listing cannot say: which two or three of these actually fit *this* situation, and
   why one beats the others.
3. **Name the anti-rebuild finding if there is one.** If something in the list already solves
   what Farrice was about to build, say so plainly and stop — that is the single highest-value
   thing this command does.
4. **Offer the next move, don't take it.** `/arsenal` is an advisor. Do not load experts or run
   workflows until Farrice picks.

## When to Use Which Door

| Question | Door |
|---|---|
| "What do I have for X?" | `/arsenal` |
| "What should I do about X?" (strategy, sequencing, gates) | `/recommend` |
| "Which skill covers X?" | `/find-skill` |
| "What did I work on last?" | `/resume` |
| "Is anything I built unfireable?" | `python3 execution/arsenal_index.py drift` |

## Notes

- **`--unused` is a memory jog, not an indictment.** The router log records *routed* calls only,
  so anything Farrice typed directly still shows as "no evidence". Never present it as "you never
  used this."
- Entries tagged `[not fireable]` are built but have no wrapper/shim yet. The parity surfaces
  mint those automatically (end-session spine, nightly 06:40 sweep); to force it now:
  `python3 execution/mint_menu_wrappers.py --scope skill <name> --apply`.
- Index: `.agent/arsenal-index.json`, rebuilt automatically when sources change.
  Spec: `directives/arsenal-loop.md`.
