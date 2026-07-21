# Generated for blind pass — task-lifecycle-forge output (BakeMargin web app)
# Judged side-by-side against reference-corpus/task-lifecycle.md

```markdown
# Task Lifecycle

Input: Spec

1. When you're building out a feature, use a subagent for that.

2. Before verifying the changes, run /code-review at medium setting and /security-review if it's a small change (less than 100 lines) and at high setting if it's bigger than that. Do this in a subagent.

3. Pass any medium or high severity issues from the code review into another builder agent that would do those fixes.
   - For any plausible verdict, don't fix it — send me a message on Slack once the PR is open explaining that change and why it matters.

4. Repeat step (3) up to 3 times.

5. Verify the changes with the /verify skill inside a subagent.
   - GUI changes: use the Playwright MCP — check both the desktop and mobile breakpoints, we've had margin calculator layouts break on mobile before.
   - Pricing math changes: also hit the calculator with 3 known recipes and capture the numbers next to the expected ones.
   - Once verification is done, send me a recording on Slack (multiple recordings if it's a big feature).

6. If verification uncovers issues, pass them to another builder subagent to make the fixes and repeat step 5 until you're happy (cap of 3 times). If it fails because you don't have the right setup — no seeded recipes, no test account — pause and notify me over Slack instead of retrying.

7. After notifying me, monitor the PR for about 6 hours with the monitor tool. Fix any comments I leave; if I merge it, end the session.

Output: Recording + Open PR
```

Vessel: CLAUDE.md block for now — graduate to a task-lifecycle skill once it's survived a few runs unchanged.
Trust: run this manually on the next 2-3 features and refine before letting it run unattended.
