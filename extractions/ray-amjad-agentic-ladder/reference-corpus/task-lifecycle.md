# Ray Amjad — Task Lifecycle (real artifact, transcribed from screen)

> Source: video XLA-sTSJ-Wc, ~12:00-15:30. Built live in his AgentStack repo's CLAUDE.md, then discussed as graduating to a `task-lifecycle` skill. This is his actual published artifact — corpus piece for blind-pass calibration.

```markdown
# Task Lifecycle

Input: Spec

1. When you're building out a feature, use a subagent for that.

2. Before verifying the changes, can you run /code-review at medium setting and /security-review if it's a small change (less than 100 lines) and at high setting if it's a change that's bigger than that. Do this in a subagent.

3. Pass any medium or high severity issues from the code review into another builder agent that would do those fixes.
   - For any plausible verdict, send me a message on Slack once you've opened up the PR, explaining that additional change and why it matters.

4. Repeat Step (3) up to 3 times.

5. Verify any changes, use the /verify skill inside the subagent.
   - Use the Playwright MCP for GUI changes.
   - Once the verification is done, send me a recording or multiple recordings if it's a big feature on Slack using the MCP server.

6. If any verification uncovers issues, can you pass it to another builder subagent to make those fixes and then repeat step 5 again until you're happy (cap of 3 times). If it fails because you don't have the right setup, pause and notify the user over Slack.

Output: Record + Open PR
```

Companion CLAUDE.md lines shown in the same session:
- "When verifying any changes, use the /verify skill inside the subagent. 1. Use the Playwright MCP for GUI changes. 2. Once the verification is done, send me a recording on Slack using the MCP server."
- "After notifying the user, monitor the PR for about 6 hours using the monitor tool — if they leave any comments you should fix those comments; if they merge it in you can end the session."
- Context-pull (Level 3): "When exploring in a subagent, look at the Notion product wiki via the MCP — we have a lot of information about the upcoming features there. If you find a contradiction between what the user told you and Notion, ask for clarification before continuing."
