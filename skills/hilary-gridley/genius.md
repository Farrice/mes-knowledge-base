# Hilary Gridley — Genius Context

Ex-Whoop team lead who drove AI adoption org-wide, then built the course "How to Be a Super Manager with AI" (Maven, hundreds of managers since Feb 2025). Her territory: the slop epidemic is not a tooling failure — it's an unarticulated quality bar. Source: Marketing Against the Grain deep-dive (8,716 words + slide capture). Full extraction: `extractions/hilary-gridley/extraction.md`.

## Core Philosophy

**"You have to make it super clear what good looks like. If you don't have clarity on that, you cannot expect anyone on your team to have clarity on that — and if they don't, you can't expect them to meet the bar."**

Slop happens when people outsource judgment to AI instead of scaling judgment with AI. The fix is never a detector bolted on at the end — it's a manager's tacit standard made explicit, encoded into narrow tools, and installed as operating culture. "The best AI work has nothing to do with AI." (Host's close, her thesis exactly.)

## The Crown Jewel — Judgment Encoding Pipeline

Her complete method, in her own words, for turning tacit taste into a deployable tool:

1. **Assemble evidence, don't introspect.** "If you asked me the five things I look for, I don't think I could tell you at this moment." Instead: one document, Column A = drafts people sent her, Column B = her revisions.
2. **Ask AI for the delta.** "What is the difference between column A and column B? What are the edits I make over and over? Help me spot the patterns." — AI's role is pattern *legibility*, not taste. The standard lives in the edits.
3. **Criteria.** "Turn those rules into criteria — give me five criteria."
4. **Plain-English pass/fail.** "Write out in plain English what passing versus failing that criteria looks like. Then you have a rubric — and you can run anything against a rubric."
5. **Deploy.** "Write that rubric as a prompt I can paste into a custom GPT or a skill. It's just English." → paste-in system prompt: evaluate against criteria, report pass/fail, give suggested rewrites. "Anyone has access to your brain."

**The hidden layer**: the tool is a byproduct. "I get so much clarity by going through this as a manager... even if you don't make any tools, you're going to be a better manager." The articulated standard is the real product; the GPT is its container.

## Genius Patterns (operational summary — full detail in extraction.md)

1. **Edit-Pair Rubric Mining** — standards from evidence, never memory. ≥5 before/after pairs minimum.
2. **Purpose-Driven Tool Scoping** — one artifact × one audience × one outcome. "NOT a second Hilary." Breadth comes from a fleet of dozens of narrow tools, never one wide one.
3. **Backward-From-AI-Native** — imagine the team a year out working AI-native, write the day-in-the-life, derive today's build order from the gap. Never "which current task can AI do?"
4. **Nothing-Is-A-Surprise** — every signal a human must notice/find/be-alerted-to becomes proactively served. Proactivity has a *tense*: the AI-native state starts in the past ("Your system flagged this three days ago. You already knew.")
5. **One-Step-Further Laddering** — at each step: "what if AI did the next thing? What if it went even further?" — repeat until only taste/judgment moves remain human. Includes unrequested *insight* (the slide's system flags a second rising competitor nobody asked about).
6. **Concrete-Detail Vision Painting** — name data sources (down to the lookback window: "your last 90 days"), exact AI next-actions, and the human's seat. Concreteness is a credibility instrument: it converts FUD into direction and makes the manager believable.
7. **Three-Layer Quality Stack** — L1 how people spend time · L2 which 10 of 100 projects (the *other* slop: "10 applications nobody's ever going to use") · L3 per-artifact bar. Manage all three, never conflate.
8. **Accountability-Not-Method** — "The job has never been about the work — it's about accountability for the work." Never police tool usage; contract on outcomes. ("I told my team to use AI and now they're making bad stuff" = wrong conversation.)
9. **Graduated Iteration Feedback** — "This is a good first start but it still feels too AI-generated — keep going." Break the bad/good binary. Reciprocity line: "It doesn't seem like you put a ton of thought into it, so I'm not going to put a ton of thought into it. Take another pass, put your spin on it, then I'll put mine."
10. **Kick-the-Crutch Tool Design** — tools teach what good looks like such that removing them leaves the team *better*. Test: do users pre-empt the tool's feedback?
11. **Virtuous Cycle vs Slop Doom Loop** — better people → better systems → better people; or cognitive rot → outsourced judgment → nobody questions outputs → worse everything. Diagnose spin direction first; tooling amplifies whichever way it's turning.
12. **Codify-Before-AI Dividend** — real context helps a zero-AI team too ("even if we had no AI, everything would improve immediately"). If a codification only helps prompting, it's hackery, not context.
13. **Domain-Experts-Build** — building stays decentralized in domain hands; only canon (source of truth) and the quality bar centralize.
14. **Editor-Not-Author Split** — AI does the undifferentiated 0→80; human judgment does 80→great. "If good lands on your desk and your job becomes getting everything to great — that's a great way to work." Never automate the judgment station.

## Context Doctrine

Context = "the information a person or an AI agent needs in order to do a job well" — and it is **calibrated, not maximized**: "Here's every A/B test we've ever run, knock yourself out — not helpful. Likewise no information." Deciding what to withhold is the core skill, identical for humans and agents. Third level: context includes the clarity/decision foundation — strategy, priorities, who you serve — not just facts.

## Signature Moves

- **Backward-Paint** first on any AI question — end state before path.
- **Column A/B Upload** whenever "what does good look like" stalls.
- **One-Step-Further Probe** at every workflow station.
- **Narrow-Name the Tool** (artifact × audience × outcome) before building.
- **Plain-English Pass/Fail First** — prose before prompt.
- **Reciprocity Feedback Line** on received slop.
- **Accountability Pivot** when tool-policing conversations start.

## Quality Rubric (score any output of this skill against these — full anchors in extraction.md)

1. **Purpose specificity** — savant: fleet of narrow tools; users never wonder what to upload
2. **Standard provenance** — savant: mined from real edit pairs; expert recognizes the patterns as theirs but couldn't have listed them cold
3. **Pass/fail legibility** — savant: a new hire self-grades accurately on day one
4. **Feedback actionability** — savant: verdict + rewrites in the expert's register
5. **Teaching residue** — savant: kick-the-crutch passes; users pre-empt the feedback
6. **Proactivity** — savant: zero workflow entry points requiring human discovery
7. **Human seat clarity** — savant: every remaining human touch is choose/judge/elevate; data sources + exact AI actions named
8. **Layer coverage** — savant: time / portfolio / artifact managed distinctly

## Anti-Patterns (reject on sight — each anchored to the source interview, MATG 2026)

- **"Run it by Claude" management** — feedback with no encoded standard. Her words: "Can you run your emails through Claude before you send them — there's no me in that equation." (source transcript, tool-scoping section)
- **The Second Brain** — one general upload-anything clone of an expert. Her words: "I was NOT like 'I'm going to make a second Hilary.'" (source transcript, custom-GPT walkthrough)
- **Incremental AI sprinkling** — her words: "I already am going to write a brief — can AI write that brief for me? Instead... imagine a year in the future." (source transcript, backward-design section)
- **Method policing** — her words: "'I told my team to use AI and now they're making all this bad stuff' — that's too focused on HOW to do the work." (source transcript, accountability section)
- **Bad/good binary feedback** — her words: "It's not 'you made slop, you're a bad person.'" (source transcript, feedback-culture section)
- **Builder slop** — Kipp's naming, her three-layer frame: "I built these 10 applications that nobody's ever going to see or use... because I thought it was cool and only I thought it was cool." (source transcript, layers section)
- **Automation-first framing** — her words: "There's almost too much focus, especially in non-technical fields, around automation — which implies it starts the job, it finishes the job." (source transcript, editor-split section)
- **Hand-wavy future states** — inverse of her stated bar: "very concrete to the point of: what are the data sources, what is the exact next action, what is the role of the human." (source transcript + slide capture 2026-07-28)

## Recognition Test

Before shipping anything from this skill, ask: **would Hilary Gridley recognize this as hers?** Concretely: is the standard evidence-mined rather than asserted, is the tool narrow-named, is the pass/fail in plain English, does the human keep the judgment seat, and does it read like a worked example with real stakes rather than a framework poster? An output she'd wave off as "a second Hilary" or "run it by Claude with extra steps" fails regardless of polish.

## Voice & Register

Warm, concrete, story-first; teaches through worked examples with asymmetric stakes (the launch-date email that detonates a day). Self-deprecating about "silly examples," then shows why they're load-bearing. Never doomy about slop — treats it as a legibility event: "It's just good leadership and management." Laughs at the AI-hype framing while taking the mechanics dead seriously.
