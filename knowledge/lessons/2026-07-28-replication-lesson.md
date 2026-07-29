# How to Order This Again — The Replication Lesson (2026-07-28)

What produced the cash-launch package Farrice rated "what I've been begging for," written as instructions to the operator, not theory. Companion memory: `feedback_cash-launch-session-recipe.md`.

---

## 1. What you actually did that worked (keep doing these)

**You dumped raw and let /go compile.** Your opening message was a messy, honest brain-dump with the felt standard inside it ("$500 to $2,000 cash collected in my bank account within the next 7 to 14 days"). That verbatim sentence became the binding constraint every artifact was tested against — the wargame even priced bank-clear lag because of it. **Always state the outcome, the number, and the deadline in your own words. Never pre-polish the ask.**

**You used the plan review as a veto, not a rubber stamp.** The single highest-leverage moment of the session was your rejection note: "yes, but do fresh research — ours was flawed." One sentence, and the whole output upgraded from stale-hypothesis to 146-source receipts. **When the mission card comes back, read it looking for the one assumption you don't trust, and say it in one sentence.** Approve fast otherwise.

**You let the system assemble instead of regenerate.** The About takes, teardowns, and offer OS came from prior sessions. This session refused to rebuild them and instead stress-tested them. That's why nothing broke.

## 2. The five-move shape (what the system does when it's working)

1. **Inventory before generate** — sweep `_active/` and the mission log; treat prior work as the asset base.
2. **Fresh receipts before judgment** — Gemini Deep runs ($0 under Ultra) demote old research to hypothesis.
3. **Adversarial wargame in an isolated context** — named attack surfaces, receipts-only rule, word ceiling. The skeptic burned 141k tokens of its own context; none of it polluted the conductor's window. Delegation IS context engineering.
4. **Felt standard as the test** — every artifact survives contact with your verbatim goal or gets fixed.
5. **Decisions, not homework** — close-out hands you only what the system cannot decide (taste picks, personal facts, sends).

If a session's output feels flat, one of these five was skipped — usually #1 (regenerating what existed) or #3 (no independent skeptic).

## 3. Session doctrine — the answer to "too many sessions"

The unit is the **mission**, not the task. One session = one mission = one deliverable-shaped outcome (a launch package, a content batch, a client doc). Everything inside that mission — follow-ups, adjustments, "also add X" — stays in the same session. You are not supposed to open a session per little thing.

- **Open fresh** when: new mission, new work type, or the prior mission hit its close-out (verdict logged, work committed).
- **Stay** when: you're refining or extending the mission that's still open.
- **Close well**: the close IS the product — commit to main, one-tap verdict, `/end-session`. A closed mission resumes cleanly with `/resume`; an unclosed one is a debt the next /go has to dig up.
- **One live writer per tree.** Before a big run, close idle sessions. Two writers on this directory at once is the one way to actually ruin things.

Sessions are cheap because continuity is on disk: missions.jsonl, handoffs, pinned chains, memory. Closing a session loses nothing that was committed.

## 4. Context budget — what this mission cost, roughly

A session starts with ~35–45k tokens of fixed overhead (system prompt, CLAUDE.md, memory index, hooks) before the first word. This mission then spent approximately: ~25k reading the existing asset base, ~30k collecting and reading the research, ~20k on planning/edits/close-out, and only ~5k on the wargame — because the skeptic's 141k tokens ran in its own isolated window. Total: roughly 120–150k of a ~200k window by close-out.

**Practical rules:**
- A mission of this size fits one session comfortably. Don't ration.
- The harness compacts long sessions automatically and `session-state.md` survives it — degradation is gradual, not a cliff. Fresh sessions are about *focus*, not fear.
- Big research artifacts get READ selectively and live on disk — never paste a 70k-char report into chat.
- Heavy parallel work (reviews, fleets, extractions) goes to subagents/workflows precisely so it doesn't spend your conductor's window.

## 5. Seating

Strongest available model conducts (Fable today); Opus 5 = heavy executor with its dialect card damping the run-long/expand-scope drift; degrade a tier, never stall. The engines, hooks, and this recipe are model-independent — the conducting judgment is the variable.
