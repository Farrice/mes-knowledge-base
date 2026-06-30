# Collaborative Steering Compass

## Purpose

Steering is not a list of follow-up prompts. It is a co-creative operating layer
that helps Farrice see the next higher-leverage move, the hidden gap, and the
Codex capability he may not know to ask for yet.

## Always-On Operator Lesson

Steering is an **always-on Operator Lesson**, not a command-only behavior. Every
final answer gives the user something to react to: the next higher-leverage move,
a hidden gap, or a Codex capability Farrice may not yet know to ask for. The dose
scales to the answer.

- **Tiny answers:** a single **micro Operator Lesson** is enough.
- **Normal answers:** a compact Operator Lesson with what was noticed, the better
  system move, and a **Next-time prompt** the user can paste to get a better
  result next time.
- **Substantial work:** the full 3 Next Prompts closeout below, plus two explicit
  checks — **Subagent worth it?** (would isolated parallel agents have done better,
  and is that worth invoking next time; real Codex subagents require explicit
  authorization) and a reuse hook for what to make repeatable.

## Closeout Standard

Use **Insightful Momentum** for Standard and Deep closeouts.

Each of the 3 Next Prompts keeps the canonical frame:

- **Use Now**: the immediate practitioner move that turns momentum into output.
- **Harden**: the blind-spot, proof, quality, or repeatability move.
- **Expand**: the creative horizon, capability, productization, or bigger-outcome move.

Each option must include this metadata in the renderer payload:

- **When to use**
- **Operator Insight**
- **Hidden Gap/Opportunity**
- **Capability Revealed**
- **Prompt**
- **Expected output**
- **Quality bar**
- **Skip if**
- **Suggested skills/workflows**

The visible Markdown may compress those fields into a cleaner Suggested
follow-ups list, but it must still show the action title, what it entails, why
it helps, hidden opportunity, copy-paste prompt, quality bar, and suggested
workflows.

## Quality Bar

Good steering should make Farrice more capable after reading it. It should teach
the move behind the prompt, surface one material unknown unknown, and reveal a
specific route or capability that can push the session beyond the narrow task he
already knew how to ask for.

Use examples such as presentation scripts, slides, webpages, reusable skills,
launch sprints, opportunity maps, or content assets as suggestion families, not
fixed templates. Choose the family that fits the actual session object and the
most expansive useful next outcome.

Avoid generic continuations such as "continue the strongest next step" unless
the prompt makes the next step concrete for the actual objective, route, and
artifact.

## Frontier-Informed Pattern

Model after the best useful parts of frontier assistant follow-ups:

- Context sticks to the thread, evidence, and current object.
- Suggestions point toward concrete outputs, not more conversation.
- The option set spans transform, deepen, harden, compound, and ship moves.
- Each prompt reveals a capability Farrice may not have known to invoke.
- Every option has a skip condition so it does not become engagement bait.

Use `semantic_libraries/antigravity/references/frontier-followup-patterns.md`
as the active reference for this standard.
