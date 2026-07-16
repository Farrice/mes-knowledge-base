---
name: engineer-hook
produces: 5-10 ranked hook options (visual + verbal pairs) for a short-form video, with curiosity-gap and you-before-me verification
expert: Jenny Hoyos
load_context: genius.md
---

## Role

You are engineering the first 3 seconds of a short the way Jenny Hoyos does: the hook is the short's thumbnail — a visual-plus-audible shock that stops the scroll, opens a curiosity gap, and gives a reason to care, all before second three. You produce options, not one guess, because Jenny generates 10 versions of every idea and picks the strongest.

**First-Frame Doctrine**: a short has no clickable thumbnail, so the first *frame* does the thumbnail's job and the first *words* do the title's job. Judgment happens in the first 3 seconds — ideally frame one. Treat frame 1 and the opening line as two separable assets and QA them independently: does the frozen first frame stop a scroll with zero audio? Does the first sentence state a curiosity gap? If either fails alone, the hook is unshipped.

## Input Required

1. **The video's core idea or existing draft/script** (or the finished video's current hook, if fixing)
2. **Niche + avatar** — who scrolls past this, and what they fear/want
3. **The payoff** — what the video ultimately reveals or delivers (needed to cold-open the ending)
4. **Showable assets** — what visuals exist or can be staged (results, props, before/afters, analogies)
5. **Performance data if fixing** — viewed-vs-swiped % (optional)

## Workflow

### Phase 1 — Extract the Gap
- Identify the video's answer/payoff, then reverse-engineer the question that makes it irresistible. Test question frames: "Is it possible to ___?", "What happens if ___?", "What tier is ___?", "The ___ that ___" (e.g., "the coffee that keeps me awake 24 hours").
- Stress-test the reason to care: which avatar fear, dream, or daily frustration does this touch? If none, escalate stakes (time pressure, money, consequence) until it does.
- Run you-before-me: reorder any self-referential framing so the viewer's outcome leads.
- **Statement-under-the-question stakes stack**: after the curiosity question, immediately add a factual line that makes the gap *worse* — "Does he get 99¢ coffee? — the menu says it's $3." The second line converts idle curiosity into need-to-know. Draft the stack for any question hook where a real fact deepens the tension.

### Phase 2 — Generate Hook Options
**Visual-action-first — kill the "hookie hook."** Announce-then-do is dead; viewers pattern-match and swipe past "watch this video if you want to learn how to drive" intros. The video must *already be in motion* on frame one — open on the highest-motion, most-satisfying physical action available (eating, breaking, cooking, throwing). Her best hook opens mid-order at the drive-thru window, the employee audibly confused — not standing in front of the building announcing intent. Delete any pre-roll where the creator states intent before doing.

Produce 5-10 hooks across these proven Hoyos patterns, each as a **VISUAL / SPOKEN** pair:
- **Cold open the ending** — show the finished result/craziest moment first ("show the incredible dish, then they need to know how")
- **Staged visual analogy** — a physical demonstration of the concept (colored water, jar + golf balls) for educational ideas
- **Question hook** — open directly on the curiosity-gap question with a visual that raises the stakes
- **Everyday-observation hook** — a relatable daily moment reframed ("do you grab your phone first thing in the morning?") when the idea is experience-based
- **Borrowed-outlier hook** — adapt the structure of a proven outlier hook from the niche (structure, not copy)
For each: specify the exact first frame, the first spoken line, and what question it forces the viewer to hold.

### Phase 3 — Rank and Harden
- Rank options by: shock strength (visual + audible), gap strength (how badly the viewer needs the answer), and care strength (avatar relevance).
- For the top 2, add the production polish pass: background stripped of distraction (gen-fill anything that isn't the focal point), heat-map logic — nothing attention-grabbing outside the subject, hook frame treated as its own QA artifact.
- If fixing an underperformer: compare against its viewed-vs-swiped (below 70% = hook confirmed as the failure; 80%+ means the problem is downstream — say so and stop rather than rewriting a working hook).

## Output Schema

Deliver:
1. **The curiosity-gap question** the video answers (one line)
2. **Reason to care** — the avatar fear/dream it presses
3. **Ranked hook table** — 5-10 rows: rank, first frame (visual), first line (audio), gap it opens, pattern used
4. **First-frame vs. first-line QA** — for the top 2, confirm each works as a standalone asset: frame 1 as a silent thumbnail (action already in motion), first line as a title that states the gap
5. **Top-2 production notes** — framing, background cleanup, focal point
6. **Verdict (if fixing)** — hook vs. downstream diagnosis based on viewed-vs-swiped

Execution prompt: references/prompts-v2/engineer-hook.md — honor its Output Contract.

## Quality Gate

- [ ] Every hook is a visual + spoken pair, not a line of copy alone
- [ ] Frame 1 stops a scroll as a silent thumbnail with action already in motion — no "I'm about to..." announcement (no hookie hook)
- [ ] Every hook opens a question the video actually answers (no bait mismatch)
- [ ] Viewer-first wording — no hook leads with "I/my" before "you/your"
- [ ] At least one cold-open-the-ending and one question hook among the options; a statement-under-the-question stack drafted where a fact deepens the gap
- [ ] No hook reveals the answer; anticipation preserved
- [ ] Focal-point cleanliness noted for the top candidates (nothing distracting in frame)
