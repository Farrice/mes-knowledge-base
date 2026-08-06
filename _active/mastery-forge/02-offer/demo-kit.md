# The 10-Minute Demo Kit — showing the God Agent + Oracle to a real person

**Audience:** the interested friend, Chris, the restaurant owner, anyone warm. **Rule:** never demo from the terminal. Two visual surfaces carry the whole pitch, and both run at $0.

## Surface 1 — The Oracle dashboard (the proof the system grades itself)

Open before they arrive: `python3 execution/oracle_dashboard.py --open` (or `/oracle-board`).

**The 3-minute walk:**
1. "This is an AI I built that's learning to beat betting markets. It is not allowed to touch real money yet." Point at the NO-GO badge. "It has to pass a four-part exam first. No override exists."
2. Point at the integrity strip: "It found 226 of its own historical bets were reconstructed after the fact, so it disqualified them. It grades itself harder than I would."
3. Point at the red C5 bar: "When its own confidence scores turned out to be wrong, it flagged itself. That's the difference between this and every AI demo you've seen: it can fail, visibly."

The pitch inside the demo: *every business system I install carries this same property. Checked work, not vibes.*

## Surface 2 — The Agent Inbox (the magic trick)

1. Before the meeting, drop a note or screenshot into the Desktop "Agent Inbox" folder while they watch. "Anything I drop here becomes a task my system works overnight."
2. Show `.agent/inbox/processed/` with a prior night's `.result.md` next to its source. "I dropped this yesterday. This result was waiting at breakfast."
3. Phone buzz (ntfy notification) if configured: "It tells me when it picks work up."

## Do not say
God agent. Orchestration. LLM. The system's internal names. Say: AI employee, exam, checked work.

## The close (one breath)

"I run this on my own business as client zero. What I install for you is the same thing trained on YOUR operation: it watches your market at night, drafts your responses, and hands you finished work every morning. Everything it produces gets checked before you see it. Want me to run a two-week proof on [their business]?"

## Prep checklist
- [ ] Re-render the dashboard same-day (`/oracle-board`) so the timestamp is fresh
- [ ] One real processed inbox item from the last 48h to show
- [ ] The positioning one-liner memorized (`positioning-plain-terms.md` §2, conversation variant)
