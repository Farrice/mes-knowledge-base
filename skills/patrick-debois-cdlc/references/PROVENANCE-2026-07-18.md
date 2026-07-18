# Provenance — patrick-debois-cdlc repair

Single source file: `extractions/Patrick Debois/transcript.txt` (22,885 bytes, 4,276 words, one
continuous keynote + Q&A transcript — read in full for this repair). All anchors below are exact
substrings of that file, confirmed with `python3` string search before being written into
`genius.md`.

| Anchor added in genius.md | Location | Verbatim in source? |
|---|---|---|
| "you cannot say, 'Well, run it once, and then if it passes or not.' ... in for a treat" | Anti-Patterns — Single-run eval theatre | Yes — Test section, transcript body |
| "Simple analogy, simple linter that you can run." | Anti-Patterns — Lint-only confidence; also `### Test` stage body | Yes |
| "99.9, and I mean that in a very sincere way, of the skills is crap" | Anti-Patterns — Default-A skill classification (already present pre-repair, kept) | Yes |
| "immediately it's loaded. So, you can't filter that with sandboxes. You need to have another way." | Anti-Patterns — Sandbox-as-only-defense (already present pre-repair, kept) | Yes |
| "These pieces of code were changed and were failing... Can we create a test case for this?" | Anti-Patterns — Static eval suites | Yes |
| "Generate. It's probably the one that you're all most familiar with. Because you're all prompting." | Anti-Patterns — Generate-only thinking | Yes |
| "you can kind of keep arguing on the PR, or you can just say, 'Let's improve the context.'" | Anti-Patterns — Argue-the-PR reflex (already present pre-repair as Hidden Knowledge Insight, added anchor to the anti-pattern bullet line) | Yes |
| "That's why I like to voice code... way more elaborate voice coding than typing" | `### Generate` stage body | Yes |
| "with context we're going to have dependency hell" | `### Distribute` stage body | Yes |
| "I can optimize my context uh and that's I think the message uh doing this more in an engineered way..." | `### Adapt` stage body | Yes |
| "In 2009, I don't know if there is any DevOps people in the room. It was kind of me saying like what if ops looked more like dev?" | Pattern 2 — The Lifecycle Loop Reflex | Yes |
| "is it actually can the agent understand what you're writing" | Pattern 3 — Lint → Grammarly → Eval Ladder | Yes |
| "the ability to create consistency as a form of context or as a form of eval... if they're all the same, then it's probably a pretty good definition" | Pattern 5 — Consistency-as-Eval (provenance correction) | Yes — spoken by the **audience questioner**, not Patrick |
| "I don't have maybe a a specific answer to your like exotic case" | Pattern 5 — Consistency-as-Eval (provenance correction) | Yes — Patrick's actual reply, a hedge not an endorsement |
| "if we have a software development life cycle how does a context development life cycle look like?" | `## The CDLC — 5 Stages` intro sentence | Yes |

## What was NOT invented
No quote in genius.md after this repair is fabricated or paraphrased-as-verbatim. The one
correction made is a **provenance downgrade**, not an addition of new unverified authority: Pattern
5 ("Consistency-as-Eval") was previously presented as an undifferentiated Debois genius pattern; it
is actually a technique proposed by an audience member in the Q&A, which Patrick explicitly
declined to claim expertise on. This is now flagged in-line in `genius.md` and in
`references/source-ledger.md` row 26, per the envelope's rule that a false claim of "this is the
expert's own move" is itself a provenance failure worth catching, not just inventing quotes from
nothing.

## What was left UNCONFIRMED (honestly, not silently)
- YouTube URL `bSG9wUYaHWU` (SKILL.md `source_url`) — not checked against the live video this
  session; no web fetch performed. See source-ledger.md row 5.
- Exact event name "AI Engineering Summit" — the transcript only self-identifies generically as
  "the AI engineering [conference]" with an "architect track"; the specific proper noun is not
  self-confirming from the transcript alone. See source-ledger.md row 4.
- "DevOpsDays Ghent" as the specific first-DevOpsDays location — well-known public biography, not
  stated in this transcript. See source-ledger.md row 6.
