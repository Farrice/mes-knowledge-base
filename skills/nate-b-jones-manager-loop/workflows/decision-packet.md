---
slug: "decision-packet"
name: "Decision Packet"
produces: "One DECISION PACKET he can answer in a line"
expert: "Nate B Jones Manager Loop"
load_context: "genius.md"
---

# Nate B Jones Manager Loop — Decision Packet

## Role
You bring back "the choices or approvals that still need me" (22:14) in the only shape that
respects his time: the choice, whether it can be undone, the options with a recommendation, and
what happens if he says nothing. "I want to bring the person back to the choice, the risk, the
responsibility" (19:00). A status update is not a packet. A question that could be researched is
not a packet.

**Before executing**: genius.md Patterns 6, 7 and Tacit T5, T7.

## Input Required
- **[LANE]** and **[SLUG]**: where the loop stopped.
- **[FORK]**: the two (max three) real options, with what each costs and what each forecloses.
- **[IRREVERSIBILITY]**: what cannot be undone once chosen (a send, a spend, a public post, a
  deleted file, a client-facing promise).

## Workflow
1. **Test it is his.** Is this a verdict/taste/private fact/irreversible call? If a fact, research
   it and don't write the packet. If the card's `Handles alone` covers it, handle it.
2. **Compress the fork** to options he can tell apart in one read. Name the recommendation and
   the one reason.
3. **Name the default**: what the manager does if no answer arrives — usually "lane stays
   blocked, everything else keeps moving"; sometimes "proceed with A after <time>" when the card
   or a standing grant allows.
4. **File it**: `python3 execution/job_board.py packet <slug> add --lane <L> --choice "…"
   --irreversible "…" --options "A … / B …" --recommend "A — …" --if-none "…"`.
5. **Deliver it verbatim** in the turn-end reply. When he answers in chat, record it:
   `job_board.py packet <slug> answer <n> "<his words>"`, then unblock the lane.

## Output Contract
```
DECISION PACKET — <job>/<lane> · #<n>
Choice: <one line>
Irreversible? yes|no — <what can't be undone>
Options: A <…> / B <…> — recommend <A|B>: <one reason>
If no answer: <default>
```

## Quality Gate
1. He can answer with one word or one line.
2. The recommendation exists and has exactly one reason.
3. Irreversibility is stated even when "no".
4. Nothing in the packet was findable on disk or by a read-only lane.
