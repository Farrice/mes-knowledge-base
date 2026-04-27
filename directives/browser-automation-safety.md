# Browser Automation Safety Protocol

**Fires when**: Playwright MCP (or any browser-driving tool) is invoked.

**Why this exists**: A browser-driving agent has high blast radius. It can post to LinkedIn, send messages, submit forms, accept invites, click "Buy" — actions that are visible to others, often irreversible, and tied directly to Farrice's reputation and accounts.

---

## The Two-Tier Action Model

### Tier 1 — Read-only (no confirmation required)

Free to execute without checking in:
- `navigate`, `goto`, `reload`
- `screenshot`, `snapshot` (accessibility tree)
- `extract`, `evaluate` (read-only JS — no DOM mutations, no XHR submits)
- `wait_for_selector`, `get_text`, `get_attribute`
- Scrolling, hovering (when not triggering side effects)

These cannot leak state into Farrice's accounts or the world. Just do them.

### Tier 2 — State-changing (CONFIRM FIRST, every time)

Pause and get explicit one-shot approval before:
- **Posting / publishing**: LinkedIn posts, Substack publish, tweet, comment, reply
- **Messaging**: DMs, connection requests, emails sent via webmail UI
- **Submissions**: Form submits, checkout, "apply now," "send proposal"
- **Account changes**: Settings, profile edits, password changes, billing
- **Acceptance / rejection**: Connection accept, calendar invite respond, friend request
- **Purchases / commitments**: Any "Buy," "Subscribe," "Confirm order"
- **Destructive**: Delete a post, leave a group, archive/trash items
- **Anything that produces a notification on the other side**

Confirmation format (one line, blocking):
```
🛑 ABOUT TO: [exact action] on [site] as [account if known]
   Visible result: [what others will see]
   Reversible: [yes/no — how to undo]
   Proceed? (y / n / modify)
```

Wait for explicit `y` or equivalent. `n` aborts. `modify` opens a one-round revision.

---

## Credentials — Never Type Them

Playwright's persistent profile (default user data dir) carries Farrice's logins across sessions. **Never enter passwords, OAuth codes, 2FA codes, or API keys via Playwright's `fill` or `type` actions.**

If a site requires login and the profile isn't authenticated:
1. Stop.
2. Tell Farrice: "Site X needs login. The persistent profile at [path] isn't authenticated. Please open the browser and log in manually, then I'll resume."
3. Resume only after he confirms.

This rule has zero exceptions, including when "it would be faster" or "it's just a test account."

---

## Audit Trail

Every Tier 2 action is logged to `.agent/browser-actions-log.jsonl` with:
- `timestamp` (ISO 8601)
- `site` (domain)
- `account` (if identifiable)
- `action` (verb + target, e.g., "posted to LinkedIn feed")
- `content_hash` (SHA-256 of submitted content if applicable)
- `confirmed_by_user` (always `true` — Tier 2 cannot fire without confirmation)
- `result` (success / error message)

This log gives Farrice a permanent audit trail. He can review what was done, when, where, and as whom. If something looks wrong, the log identifies it within minutes.

---

## Persistent Profile Hygiene

Playwright MCP defaults to a persistent profile that stays logged in across sessions. This is desirable — it makes the agent useful — but means **the browser holds real credentials at rest**.

- Default profile lives in Playwright's user data dir (system-determined)
- For sensitive contexts (banking, healthcare, employer accounts), prefer `--isolated` mode (fresh session, no persistence)
- If a profile gets compromised or borrowed, log out of all sessions in that profile rather than deleting the dir

---

## Multi-Step Tasks ("End to End")

When Farrice asks for end-to-end automation ("post this everywhere," "apply to these 10 jobs," "schedule these meetings"):

1. **Plan first**: List every Tier 2 action the chain will fire. Show the full plan.
2. **Get one umbrella approval**: "I'll execute steps 1-7 above. Tier 2 actions: [list]. Approve the whole batch, or want per-action confirmation?"
3. **Execute with telemetry**: Report progress as it runs. On any unexpected state (login wall, captcha, error page), pause and report — never improvise.
4. **Halt on first error**: If step 3 fails, stop. Don't continue assuming success.

Umbrella approval can be revoked mid-run by Farrice saying "stop." That command halts immediately.

---

## What This Protocol Is NOT

- It is NOT a friction tax on legitimate use. Read-only browsing should feel frictionless.
- It is NOT a substitute for judgment. If a Tier 1 action smells off (scraping a paywalled site, hitting rate limits, evading detection), pause and ask anyway.
- It is NOT a license to ignore other directives. Quality gate, factual grounding, and verification still apply to any deliverable produced via browser automation.

---

## Integration With The Chain

Browser automation typically slots into Step 5 (PRODUCE) or Step 5.5 (VERIFY — for live fact-checks). The chain still runs:

- Tier 1 reads can be a verification source (Step 5.5)
- Tier 2 actions are usually the final delivery mechanism (post the polished draft, submit the verified application)
- Finalize (Step 6) still fires after the action — log composite quality + the browser action result together

---

## Quick Reference Card

| Situation | Action |
|---|---|
| User says "go to X.com and read Y" | Just do it — Tier 1 |
| User says "post this to LinkedIn" | Show post → confirm → execute → log |
| Site needs login, no profile auth | Stop, ask user to log in manually |
| Multi-step pipeline (5+ Tier 2 actions) | Show full plan → umbrella approval → execute with progress |
| Anything triggers captcha / 2FA | Stop. Surface to user. Never solve. |
| Error mid-pipeline | Halt. Report. Wait. |
