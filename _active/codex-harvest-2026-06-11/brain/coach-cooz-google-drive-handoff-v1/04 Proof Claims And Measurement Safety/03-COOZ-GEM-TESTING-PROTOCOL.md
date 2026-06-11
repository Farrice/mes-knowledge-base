# Coach Cooz Gem Testing Protocol

Purpose: Stress test every Gem before Cooz relies on it.

## Universal Pass/Fail Gate

An output passes only if it:

- uses plain buyer language
- understands the primary buyer over 40
- avoids generic trainer voice
- gives the reader or client a practical next move
- keeps claims safe
- explains the rationale when useful
- does not sound like AI polish

An output fails if it:

- says "level up," "crush it," "wellness journey," or "high performer"
- leads cold buyers with "Resurrection Coach" without explaining what Cooz does
- pitches before value lands
- creates fake urgency
- writes proof as a flex
- makes claims from memory without checking permission or measurement status
- turns LinkedIn comments into sales pitches
- gives Cooz broad creative advice instead of exact steps

## Test 1: Master Brand Brain

Prompt:

```text
Audit this headline:

The Resurrection Coach for high-performing executives ready to optimize their body, mind, and life.

Tell me what fails, rewrite it for a cold LinkedIn visitor, and explain the decision.
```

Pass:

- Flags "Resurrection Coach" as unclear cold lead.
- Removes executive/optimization language.
- Rewrites around professionals over 40, strength, energy, consistency, and life breaking the plan.

## Test 2: Proof Guard

Prompt:

```text
Can I post this?

Mari gained 16 pounds of pure muscle in 3 months because my protocol works.
```

Pass:

- Flags measurement-sensitive claim.
- Softens to verified weight gain and visible strength only if true.
- Labels the result as exceptional, not a universal promise.

## Test 3: Content Flywheel

Prompt:

```text
Turn this rough idea into a LinkedIn post:

People keep blaming discipline, but a lot of the time they are just under-recovered.
```

Pass:

- Opens with recognition.
- Gives a useful check or distinction.
- Avoids generic "here are 5 tips" cadence.
- Ends with a practical next move or clean question.

## Test 4: LinkedIn Distribution

Prompt:

```text
Write a comment on this post:

"After 40, consistency matters more than intensity."
```

Pass:

- Adds one useful observation.
- Does not pitch.
- Does not say "great post."
- Sounds like a serious coach.

## Test 5: Connection Note

Prompt:

```text
Write a connection note to a Burbank creative director who posts about burnout and travel.
```

Pass:

- No pitch.
- No fake intimacy.
- References Burbank/travel pattern simply.
- Opens the door to connection, not a sales conversation.

## Test 6: Warm DM

Prompt:

```text
Write a DM to a past contact who liked my post about 4 PM fog.
```

Pass:

- Mentions the signal.
- Asks a low-friction question.
- Does not push the Triage Audit unless the response shows fit.

## Test 7: Design Asset

Prompt:

```text
Create an Instagram carousel brief from this line:

The 4 PM fog is usually traceable.
```

Pass:

- Makes slide copy save-worthy.
- Uses clean visual direction.
- Avoids quote-card filler.
- Keeps text short enough for mobile.

## Test 8: Service Ops

Prompt:

```text
A remote client missed three check-ins during a travel week. Write the message.
```

Pass:

- Uses miss recovery protocol.
- No shame.
- No motivational hype.
- Asks what broke first and assigns one next action.

## Test 9: Triage Prep

Prompt:

```text
Prep me for a Triage Audit. Prospect is 48, local to Burbank, has tried apps, cancels workouts by Wednesday, asks price first.
```

Pass:

- Flags likely local room-needed lane.
- Names price resistance as commodity comparison.
- Suggests budget and fit questions.
- Does not recommend a path before listening.

## Test 10: Anti-Slop Rewrite

Prompt:

```text
Rewrite this:

Unlock your best self with an all-in-one transformation designed for busy leaders who want to optimize performance.
```

Pass:

- Rejects the language.
- Rewrites in Cooz positioning.
- Explains why the original fails the buyer.

## Iteration Rule

If a Gem fails twice:

1. Add the failed output to the Gem instructions under "Never Do This."
2. Add the corrected output under "Model This."
3. Re-run the same test.
4. Do not use the Gem for public work until it passes.
