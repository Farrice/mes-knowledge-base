# Operating Codex + Claude Code — Antigravity Harness

A plain-language guide to running both AI coding tools on one repo without breaking anything. You do not need to understand the internals to follow this. Read it once, then keep it open the first few times.

> **Setup status (repaired 2026-06-30):** The control plane is restored, `main` is canonical and green, and Codex's gates + tools are wired. **Three one-time steps are yours to do** (they need a browser login or a UI click I can't do for you) — see [§10 Finish Setup](#10-finish-setup-do-these-once). Everything else is done.

---

## 1. The Mental Model (read this first)

You have **one project folder** and **two AI assistants** that both work in it.

- **One canonical repo** — `/Users/farricecain/Google Antigravity`. The single source of truth. There is no "Codex copy" and no "Claude copy" anymore. Both tools read and write the same files, the same ~800 skills, the same git history.
- **Two front doors** — **Claude Code** and **Codex**. They are *peers*, not master/servant. Either can do almost any task. They share the same skills, the same "Chain" process, and the same finalize ledger.
- **Peer constitutions** — each tool reads its own rulebook at the repo root:
  - Claude Code reads **`CLAUDE.md`** (this is *canon* — the source of truth)
  - Codex reads **`AGENTS.md`**
  - (Gemini, if ever used, reads `GEMINI.md`)
  They are kept deliberately in sync and describe the *same* system from each tool's point of view.

One sentence: **same repo, same skills, same rules — two different brains you can pick from.**

---

## 2. How to START Each Tool (and confirm you're in the right place)

**Claude Code** — open it in `/Users/farricecain/Google Antigravity`. Ask it to run `pwd`; it should print exactly that path. It auto-loads `CLAUDE.md`.

**Codex** — open Codex (Desktop or `codex` CLI) and `cd` into `/Users/farricecain/Google Antigravity`. Run `pwd` (same path). It auto-loads `AGENTS.md`. Confirm tools with `codex mcp list` — you should see ~11 servers (the repo adds `playwright` on top of the global set).

**Why the folder matters:** Codex only turns on the repo's extra tools and hooks when you are *inside* this trusted folder. Start it anywhere else and you lose playwright and the repo gates.

---

## 3. THE GOLDEN RULE (the one thing you must never get wrong)

> **Never run Claude Code and Codex on this folder at the same time.**

Both tools edit the same files with no lock between them. If both work at once, one overwrites the other mid-edit and the tree corrupts — this is the exact "I fix one thing and another breaks" failure you hit (root-caused 2026-06-30: a background Codex session was rewriting files under an active repair). This rule is now written into the top of both `CLAUDE.md` and `AGENTS.md`.

**The safe workflow (memorize this):**

1. Pick ONE tool to "drive" the current piece of work.
2. Let it finish a clean unit of work — to a **commit**, or until **`git status` is clean**.
3. Only THEN open the other tool on this repo.
4. Hand off by committing. The next tool picks up from a clean tree. (`/handoff` writes a clean handoff doc; `/resume` picks it up.)

Think of it like a single steering wheel — one driver at a time.

*If you ever truly need both at once* (not recommended): give Codex its own checkout with `git worktree add ../ag-codex <branch>`, so each tool has its own folder but shares history through branches. Never two drivers in one folder.

---

## 4. How the Chain + Gates Work in Each Tool

Both tools follow **The Chain** — a 6-step process for every real deliverable (score intent → sharpen → route to an expert → load the expert → produce → verify facts → finalize and log). The difference is *how the gates are enforced*.

**Claude Code — gates are automatic (physical hooks).** You don't think about them:
- **Cost gate** — blocks paid-API spend (image/video/deep-research) before it happens.
- **Finalize gate** — won't let the turn end if you produced expert work but didn't log it.
- **Routing gate** — warns when you're about to use the wrong expert.
- **Dangerous-git guard** — blocks destructive git (`push --force`, `reset --hard`, `clean -fd`).
If a gate fires, **work WITH it** — never route around it.

**Codex — same gates via a "hook bridge," now enabled.** As of this repair all six hooks (cost-gate, dangerous-git, skill-router, session-ledger ×3) are trusted and on in `~/.codex/config.toml`. If Codex ever changes its `hooks.json` it will mark them untrusted until you re-approve in Codex Desktop → Hooks. When a gate is NOT firing, Codex's rulebook says it plainly: **"here YOU are the hook"** — sanity-check cost yourself before paid commands, confirm destructive git yourself, and run finalize yourself after expert work.

So: **Claude Code = the gates watch you. Codex = the gates watch you once enabled; until then, you watch yourself.**

---

## 5. The Hot Control-Plane Commands (and when to use each)

Type these as `/name` in either tool. The ones you'll reach for most:

- **`/autopilot`** — "just do it, don't stop to ask." Runs a whole mission end-to-end with only 3 taste checkpoints (intent, cost, final prose). Use when you trust the plan and want output, not a conversation.
- **`/mission`** — a multi-deliverable campaign with structure. For bigger jobs producing several artifacts.
- **`/system-audit`** — a full health check on the whole system. Run it when something **feels off**, or before/after a big change. Your "is the machine healthy?" button.
- **`/convene` · `/swarm` · `/supercomputer` · `/deploy`** — parallel multi-expert work (councils, swarms, parallel research). **Prefer Claude Code** for these — it runs experts truly in parallel; Codex runs them one at a time.
- **`/resume`** — pick up where you left off. Run it at the start of a session for a menu of unfinished work.
- **`/handoff`** — compress the current session into a clean handoff doc for the next session (or the other tool).

Rule of thumb: `/autopilot` to produce · `/mission` to campaign · `/system-audit` to diagnose · `/resume` to continue.

---

## 6. Which Tool to Prefer for Which Task

Same skills, same repo — but each tool has real strengths. Pick by the job:

| The job | Use | Why |
|---|---|---|
| Councils, swarms, parallel research/extract (`/convene`, `/swarm`, `/supercomputer`, `/deploy`) | **Claude Code** | Only it runs experts truly in parallel; Codex is serial |
| Anything paid/gated you don't want to babysit (image/video/deep-research; finalize discipline) | **Claude Code** | Its gates fire automatically |
| Single-expert content / copy / strategy (one expert, clear task) | **Either** — whoever's open | Same skills, same result |
| Deep single-thread reasoning, hard debugging, architecture calls | **Codex** | A different strong reasoner (gpt-5.5 high-effort) — a genuine "second brain" |
| Office docs (.docx / .xlsx / .pptx / PDF), Remotion video | **Codex** | Dedicated document + Remotion runtimes |
| GUI / desktop-app / computer-use automation | **Codex** | Native computer-use + bundled browser |
| GitHub-heavy or security-review work | **Codex** | Has github + security-review + an approvals reviewer |
| Visual generation (Higgsfield, Canva, Gamma, posters) | **Claude Code** | That visual surface is wired + cost-guarded here |

Simple version: **Claude Code is the factory** (parallel work, automatic gates, visuals). **Codex is the specialist** (deep reasoning, documents, computer control). When in doubt on ordinary content/copy, use whichever is already open.

---

## 7. MCP / Tools Available in Each

"MCP" = the external tools each assistant can call. The sets overlap but aren't identical.

- **Claude Code:** Higgsfield (image/video/3D/voice), Canva, Gamma, Notion, Gmail, Google Drive/Calendar, Playwright (headless), Perplexity, pencil, episodic-memory search, plus ~800 skills as first-class tools.
- **Codex:** its own document runtimes (.docx/.xlsx/.pptx/PDF), Remotion, computer-use + bundled browser/chrome, node REPL, github, security-review, Higgsfield, Playwright (inside the repo), Perplexity, recall, and the same skills read as files.

Two things to know:
- **Playwright on Codex only works inside this repo** (added by the repo config) — start Codex in the folder and it's there.
- **recall needs a one-time login** (see §10). Until then Codex's card-grounding is weaker than Claude Code's.

---

## 8. Troubleshooting

- **"Codex feels off / dumber / is ignoring rules."** → Run **`/system-audit`**. Most "feels off" issues are a stale/disabled gate; the audit names it.
- **"Routing picked the wrong expert."** → Run `python3 execution/codex_operator_preflight.py "<your prompt>" --plain`. It shows which expert the router would pick and why. If wrong, invoke the expert explicitly with its `/name`.
- **"A destructive git command went through without a block on Codex."** → Open **Codex Desktop → Hooks**, re-trust the repo's `hooks.json`, ensure **dangerous-git** is toggled **on**. Until then, **you are the hook** — double-check git yourself.
- **"recall isn't grounding."** → `codex mcp login recall`, sign in at getrecall.ai, approve. Verify with `codex mcp list --json` (recall `auth_status: o_auth`). Note: `codex doctor` shows green even when recall is unlogged — trust `codex mcp list --json`, not `doctor`.
- **"Perplexity research fails on Codex."** → Fixed in this repair (key set in `~/.codex/config.toml`). If it recurs, the key under `[shell_environment_policy.set]` was lost — re-add it from the repo `.env`.
- **"Did Codex or Claude Code ship this?"** → finalize now records a `--platform` field; CLAUDE.md sets `claude-code`, AGENTS.md sets `codex`.

---

## 9. Maintenance (keep the harness healthy)

- **After editing a constitution** (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`): run `python3 execution/platform_compiler.py sync` then `... lint --json` (expect `{"failures": []}`). This catches drift between the two rulebooks.
- **Weekly — verifier sweep** (the canonical baseline must stay green):
  ```bash
  python3 execution/verify_google_operator_core.py
  python3 execution/verify_codex_authority.py
  python3 execution/verify_autopilot_runtime_preflight.py
  python3 execution/verify_skill_system_contract.py
  python3 execution/verify_subagent_approval_language.py
  python3 execution/platform_compiler.py lint --json
  ```
  If one goes red after a change you made, fix the change. If one is red because it describes an *old* layout, that's a verifier to **adapt**, not a real failure — flag it rather than recreating old structure.
- **Weekly — memory sweep** (keeps shared memory current for both tools):
  ```bash
  python3 execution/episodic_ingest.py run && python3 execution/memory_embed.py && python3 execution/memory_distill.py preview && python3 execution/memory_review.py
  ```

---

## 10. Finish Setup (do these once)

These three need a browser login or a Desktop click — I can't do them headless:

1. **Log recall into Codex** *(highest value — restores 3,000+ card grounding for content/copy/brand work).*
   ```bash
   codex mcp login recall      # opens a browser → sign in at getrecall.ai → approve
   codex mcp list --json       # confirm recall shows auth_status: o_auth
   ```
   (If it says already-logged-but-broken: `codex mcp logout recall` first, then login.)

2. **Confirm the dangerous-git hook is ON in Codex Desktop.** I enabled it in config, but the guaranteed path is the UI: **Codex Desktop → Hooks →** find the dangerous-git hook under this repo's `hooks.json` → toggle **on**. (This protects you from accidental destructive git in Codex.)

3. **Open a fresh Codex session in the repo and sanity-check:** run `/system-audit` — it should come up green on the canonical baseline. Then try a tiny task to confirm hooks fire and routing lands.

4. **(Optional but recommended) Turn on the concurrent-tool warning.** A ready, tested guard exists at `execution/hooks/active_tool_lock.py`. It WARNS (never blocks) when the *other* tool was active in this repo in the last 10 minutes — a safety net for the GOLDEN RULE. Wiring it modifies agent config, so it's yours to enable:
   - **Claude Code** — add this block to the `PreToolUse` array in `.claude/settings.json`:
     ```json
     { "matcher": "Bash|Edit|Write|NotebookEdit",
       "hooks": [ { "type": "command",
         "command": "python3 \"$CLAUDE_PROJECT_DIR/execution/hooks/active_tool_lock.py\" claude-code",
         "timeout": 10 } ] }
     ```
   - **Codex** — add a third `PreToolUse` hook to `.codex/hooks.json` calling
     `python3 "/Users/farricecain/Google Antigravity/execution/hooks/active_tool_lock.py" codex`,
     then re-trust `hooks.json` in **Codex Desktop → Hooks** (the file hash changes).
   (Or just rely on the GOLDEN RULE discipline — the warning is a backstop, not a substitute.)

That's it — after these steps, both tools are fully operational and at parity.

---

## The 30-Second Version (stick this on a note)

1. **One folder, two assistants.** Same repo, same skills, same rules.
2. **Never run both at once.** Finish to a clean `git status` / commit before switching tools.
3. **Claude Code = factory** (parallel, auto-gates, visuals). **Codex = specialist** (deep reasoning, documents, computer-use).
4. **In Codex, if a gate isn't firing, YOU are the gate.**
5. **`/system-audit` when it feels off · `/resume` to continue · `/autopilot` to ship.**
6. **After editing a constitution → `platform_compiler.py sync`.**
