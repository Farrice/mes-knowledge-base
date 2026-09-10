# /eli5 format ladder — condense, don't decorate

Farrice, 2026-09-10: not "draw a picture." Use whatever format lets him take the information in fastest, and only when that format condenses better than prose. The shape of the information picks the format. Nothing is rendered for its own sake.

Climb only when the rung below would be a wall of text. Never climb for a single item.

| information shape | format | rule |
|---|---|---|
| one thing, one state | prose, 1-2 sentences | the default |
| 3-8 things sharing the same fields (name · state · needs) | markdown table, three columns | replaces the "where each piece is" list |
| a sequence or dependency ("X waits on Y, then Z") | `flowchart LR`, at most 6 nodes | only when order or blocking matters; Codex prints `A → B → C` instead |
| a decision with two real options | two-column mini table: A vs B, rows = what it costs · what you get · my pick | never more than two options; proposal-options stay in prose |
| `all` with more than 8 pieces (Claude Code) | one inline widget, rows grouped by state, done collapsed to a count | the only rung with a widget; never a hosted page |

Counting rule: a table row is one line, a mermaid block is three lines, a widget is three lines. Total output stays at or under 20.

## One example per rung

**Prose (1-2 pieces)**

> 🔄 10 changed files not committed on this lane — working. Edits in progress.

**Table (3-8 pieces)**

| thing | state | what it needs |
|---|---|---|
| linkedin-daily | ⛔ stuck | your raw take, 79 days waiting |
| farrice-final-10 | 🙋 waiting on you | four calls, see below |
| system health | 🙋 waiting on you | 26 items need your judgment, first is constitution drift |

**Flowchart (a chain)**

```mermaid
flowchart LR
  A[your raw take] --> B[the cook runs] --> C[post goes live]
```

Codex prints: `your raw take → the cook runs → post goes live`

**Decision card (two real options)**

| | A) run the queued card | B) park it |
|---|---|---|
| what it costs | one skill-evolution session, about 20 minutes | nothing now |
| what you get | jen-santulan-listing-content scores climb back over 7 | the queue keeps flagging it |
| my pick | **A**, the three low scores are real | |

**Widget (`all`, more than 8 pieces, Claude Code only)**

Load `mcp__visualize__read_me` with `["diagram","interactive"]` first. One HTML card: three groups (stuck, waiting on you, working) with one row each, done rolled up into a single "N things done" row. CSS variables only, two font weights. Subtitles at most five words. Detail stays in the prose.
