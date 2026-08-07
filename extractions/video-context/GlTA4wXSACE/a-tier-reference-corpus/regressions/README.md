# Regression Fixture Rules

Create one fixture for every distinct observed failure before changing any shipped behavior.

Each fixture must contain:

1. case ID and replay path;
2. exact failure evidence quoted from the replay;
3. violated hard gate or rubric dimension;
4. expected behavior stated without copying the held-out reference;
5. smallest owning component already inside the shipped system;
6. Preservation Lock and explicit no-router-expansion clause;
7. repair and bounded replay status.

A fixture is not a general wish for better prose. It must be specific enough that a future blind replay can either reproduce the failure or prove it absent.

Corpus and handoff failures use the same rule: name the observable miss, preserve all judged references and router scope, assign the smallest package owner, and add a deterministic verifier check whenever the condition can be checked mechanically.
