# Prompts - Manus-To-Codex Replacement

## Reproduce An Existing External AI Result

```text
Analyze this external AI session as a repeatability case.

Source: [URL, transcript, screenshots, or pasted chat]
Goal: reproduce the final result locally in /Users/farricecain/Google Antigravity.
Mode: [faithful reproduction | improved version | audit only]

First extract the Run Map:
1. original user goal
2. prompt sequence
3. agent decisions
4. assets generated or changed
5. final artifact
6. verification loop
7. acceptance criteria

Then execute the equivalent or better result locally.
Preserve what made the result work.
Make the output editable, not just copied.
Download or recreate required assets locally when allowed.
Run browser checks at desktop and mobile.
Give me paths, verification proof, and the prompt I should use next time.

Ask only for credentials, paid tools, publishing, destructive changes, or taste decisions that would change the artifact.
```

## Harden A Local Reproduction

```text
Audit this local reproduction against the external AI original.

Original: [URL or transcript]
Local artifact: [path]

Find the one to three places where the local version feels less premium, less persuasive, less faithful, or less useful.
Patch those issues locally.
Do not invent factual claims.
Verify with desktop and mobile browser checks.
Write a hardening audit that explains what changed and what remains optional.
```

## Promote The Workflow Later

```text
Review this cold workflow packet and tell me whether it should become a hot slash command.

Workflow packet: deliverables/manus-to-codex-replacement-workflow/

Run route/discoverability checks, identify bridge files required, list risks, and stop before modifying production command indexes unless I explicitly approve promotion.
```
