# DOC-FORMAT-SPEC — Binding Template for Client-Facing Action Docs

Standing standard for every client deliverable, system-wide. Cooz is the first build. Every builder follows this exactly. No new facts: every claim traces to a Receipts doc.

---

## THE CARD (base unit)

Six parts. Effort lives inside the HOW line so the card stays tight. Fill every part.

```
### [WHAT — bold imperative. The conclusion, not a topic.]
Why it matters: [one sentence — the stake if you skip it]
Do it (TIME + who else): [ ] verb-led step, paste-ready asset inline
                          [ ] verb-led step
                          [ ] verb-led step        (max 7; more = two cards)
Done when: [visible, binary proof — something you can point at, not a feeling]
Go deeper → [ONE named Receipts doc + section]
```

**Filled example:**

```
### Fix the broken booking link before you print a single flyer
Why it matters: A flyer that sends people to a dead link burns the only shot you get with a walk-by.
Do it (15 min, alone): [ ] Open your Squarespace site, click the "Book a Call" button
                        [ ] Paste this URL in its place: calendly.com/cooz/triage
                        [ ] Text the link to yourself, tap it, confirm the calendar loads
Done when: You tap the flyer's link on your phone and land on a working calendar.
Go deeper → 06-market-truth/CONCEPT-V2-MARKETABLE.md, "Why the offer needs one door"
```

Rules: WHAT is an instruction, never a label ("Booking page" banned; "Fix the booking link" is the header). Every step opens with a verb. Assets sit inline — exact URL, exact caption — so he never leaves the card. TIME is honest: a 45-minute job says 45. Name anyone else needed.

---

## THE DOC

```
# [Doc title — what he'll have when done]

**After this doc:** [X exists.]  ← the outcome banner. First line, always.

[3 to 7 cards. Never more. 8+ cards = split into two docs.]

## Not now
- [thing to ignore this week — and one line why it can wait]
- [thing to ignore]
```

The **Not-now section** is mandatory. It makes the scope feel finite — he sees the edge of the work, not an open drain. List what he should NOT touch yet.

**Zero-jargon law.** These words are banned in the card face. Translate every time:

| Banned | Say instead |
|---|---|
| ICP / avatar / target persona | the guy you're trying to reach |
| instrumental / terminal | the step / the win |
| hypothesis / H1 / [ASSUMPTION] | our best guess |
| awareness levels / awareness ladder | how much he already knows |
| funnel / top-of-funnel / TOFU | how a stranger becomes a client |
| gate / gate record | the check before you ship |
| leverage (verb) | use |

Operator tags ([ASSUMPTION], gate records, hypothesis labels) stay in the Receipts. They never appear in an action doc.

---

## THE MASTER PLAYBOOK (00)

The whole story, scrollable in one file. Structure:

1. **The 10-line read** (top). Plain sentences. What we found / what we're doing / the one decision you need to make right now. If he reads only this, he can still act.
2. **One section per action doc.** Its essence in two lines + its single top card, verbatim + `→ open [doc]`. Compact. He skims five sections, knows the whole plan.
3. **Receipts map** (bottom). One line per research doc: what it proves.
   - `MCBROOM-READOUT.md → proof your method already worked on you`
   - `ICP-DESIRE-LADDER.md → the exact words your guy uses for his problem`
   - `SOCIAL-LISTENING.md → real quotes from real men, not guesses`

Receipts are ammunition for defending a call to himself or a client. Never required to finish a checklist.

---

## VOICE (Farrice → Cooz, peer register)

Read `15-final-package/03-cooz-voice-profile.md` before writing a word. Rules:

- **Three punches and a wave.** Short. Short. Short. Then one 15-20 word line. Then a short close. No walls.
- **Peer with receipts** — a friend two years ahead, not a drill sergeant, guru, or therapist.
- **Profanity where it's load-bearing.** "This link is fucking broken, fix it first" beats "prioritize link remediation." Only when it carries weight.
- **Banned** (per voice profile D1-D3 + `directives/ai-slop-detector.md`): "Here's what/why/how" openers, "crush it," "level up," "journey," "mindset shift," "unlock your potential," "leverage," em dashes over 2 per doc, any emoji, "It's not X, it's Y," "let's unpack/break it down."
- One hit = rewrite. The ban list is not advisory.

---

## THE 60-SECOND TEST (every doc must pass)

Hand the doc to a tired reader. Within 60 seconds of opening, he can say out loud:

1. **What I'll have when I'm done** (from the After-this banner)
2. **The first physical thing I do** (from card 1's first checkbox)
3. **How long it takes** (from the HOW time tag)

Can't answer all three in 60 seconds? The doc fails. Rebuild it.

---

## THE COMPLETE-PACKAGE RULE (locked by Farrice 2026-07-09 — binding, all client packages)

A client-facing doc may only point at three things: (1) a sibling doc in the same
package ("doc 03", "Receipts → 05 — McBroom Readout"), (2) a file that SHIPS with
the package (Print Files folder), or (3) a public URL the client can open. Never:
repo paths, internal build files, tool names, commands, gate/review vocabulary, or
working-dir references. If a card needs an asset the client doesn't have, the fix
is to SHIP THE ASSET into the package, not to point at where it lives internally.
If no package target exists and the card is self-contained, the Go-deeper line
says what to ask Farrice for — or gets cut.

**Deterministic enforcement**: `python3 execution/client_package_lint.py <package-dir>`
must PASS (0 findings) before any client package ships. Run it on the exact copies
being delivered, not just the repo sources.
