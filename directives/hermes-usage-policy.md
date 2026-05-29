# Hermes Agent — Usage Policy + Complete User Guide

> **Role**: Local agent CLI powered by Nous Research's Hermes models. Use for coding/agent tasks where Claude is overkill or rate-limited, or when an open-weights / multi-model second opinion is wanted.
> **Subscription**: Nous Portal Pro — $20/month flat | Auth via OAuth (`hermes auth add nous --type oauth`)
> **Not an MCP server.** Invoked via shell only.

---

## Part 1 — What Your $20/Month Includes

Confirmed via `hermes portal` + `hermes status` + Tool Gateway docs (https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway):

### Model Access (single OAuth, ~30 models)
Top tier:
- **Anthropic**: `anthropic/claude-opus-4.7-fast` (your default), `~anthropic/claude-sonnet-latest`, `~anthropic/claude-haiku-latest`
- **OpenAI**: `openai/gpt-5.5-pro`, `openai/gpt-5.5`, `~openai/gpt-mini-latest`, `~openai/gpt-latest`
- **Google**: `google/gemini-3.5-flash`, `google/gemini-3.1-flash-lite`, `~google/gemini-pro-latest`, `~google/gemini-flash-latest`
- **xAI**: `x-ai/grok-4.3`, `x-ai/grok-build-0.1`
- **DeepSeek**: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v4-flash:free`
- **Qwen**: `qwen/qwen3.7-max`, `qwen/qwen3.5-plus-20260420`, `qwen/qwen3.6-flash`
- **Mistral**: `mistralai/mistral-medium-3-5`
- **IBM**: `ibm-granite/granite-4.1-8b`
- **Moonshot**: `~moonshotai/kimi-latest`
- **Inclusion AI**: `inclusionai/ring-2.6-1t`, `inclusionai/ling-2.6-1t`
- **Tencent**: `tencent/hy3-preview`
- **OpenRouter relay**: `openrouter/owl-alpha`

Full live list anytime:
```bash
source "/Users/farricecain/Google Antigravity/.env"
curl -s -H "Authorization: Bearer $NOUS_API_KEY" https://inference-api.nousresearch.com/v1/models | jq -r '.data[].id'
```

### Tool Gateway (included free with subscription)
Routes through Nous infrastructure, NO separate signup needed for:
- **Web search & extraction** — Firecrawl-powered, "no rate limits to worry about"
- **Image generation** — 9 models including FLUX 2, Ideogram, Recraft
- **Text-to-speech** — OpenAI TTS voices (Edge TTS as default fallback)
- **Cloud browser automation** — Headless Chromium via Browser Use (navigate, click, type, vision)

Modal (serverless code execution) is an OPTIONAL add-on, not included by default.

### Billing Model
Pay-as-you-use against your $20/mo Nous subscription. **No explicit per-call quotas published** — Nous appears to throttle dynamically rather than hard-cap. Check usage anytime at `https://portal.nousresearch.com` (dashboard shows breakdown per tool).

### What's NOT included (separate keys required)
- Tavily (web search alt) — already in your Antigravity `.env`, Hermes auto-detected it
- xAI direct (`XAI_API_KEY`)
- ElevenLabs (`ELEVENLABS_API_KEY`)
- Browserbase / Browser Use direct (only the cloud version is free via Gateway)
- GitHub Models (`GITHUB_TOKEN`)
- Personal LLM keys (Anthropic, OpenAI direct) — you'd only need these if you don't want to route via Nous

---

## Part 2 — Daily Usage

### The 10 Commands You'll Actually Use

```bash
# 1. Interactive chat with default model (Opus 4.7 fast)
hermes

# 2. Same, but with the modern TUI (recommended)
hermes --tui

# 3. One-shot non-interactive prompt
hermes -z "your prompt here"

# 4. One-shot with a specific model
hermes -z "..." -m google/gemini-3.5-flash
hermes -z "..." -m x-ai/grok-4.3
hermes -z "..." -m openai/gpt-5.5-pro

# 5. Resume the most recent session
hermes --continue

# 6. List previous sessions
hermes sessions list

# 7. Auto-approve tool use (skip confirmation prompts)
hermes --yolo -z "..."

# 8. Check Nous subscription + Tool Gateway status
hermes portal

# 9. Diagnose any config/auth issues
hermes doctor

# 10. Update to the latest Hermes Agent version
hermes update
```

### Tool Use Mechanics
Inside a chat session, Hermes has access to three tool families:
- **Terminal execution** — runs shell commands, shows results
- **File operations** — reads/modifies local files
- **Web/external** — search, image gen, TTS, browser via Tool Gateway

Toggle which tools are available per platform:
```bash
hermes tools              # interactive UI
hermes tools list         # see what's enabled
hermes tools disable web  # turn off web tools for CLI
hermes tools enable browser  # enable browser tools
```

### Sessions & Continuity
- Each chat creates a session stored in `~/.hermes/sessions/`
- `hermes --continue` resumes the most recent
- `hermes --continue <session_name>` resumes a named session
- `hermes sessions list` shows all of them
- `hermes --resume <session_id>` jumps to a specific one

### Skills System (97 built-in workflows)
Categories include `apple` (Notes/Reminders/iMessage/FindMy), `autonomous-ai-agents` (claude-code/codex/opencode integration), `creative` (architecture-diagrams, ascii-art, manim-video, p5js, pixel-art, sketch, songwriting), `data-science` (jupyter-live-kernel), `devops` (kanban-orchestrator/worker), and dozens more.

```bash
hermes skills list                    # show all installed
hermes skills search kubernetes       # search by keyword
hermes skills install <skill-name>    # install one
# In chat: type /skills to invoke
```

---

## Part 3 — Telegram Bot Setup

This turns Hermes into a personal AI assistant you can message from anywhere.

### Step 1 — Create the bot
1. Open Telegram, message **@BotFather**
2. Send: `/newbot`
3. Choose a display name (e.g., "My Hermes")
4. Choose a username ending in `bot` (e.g., `farrice_hermes_bot`)
5. BotFather replies with your **bot token** (format `123456789:ABCdef...`)
6. **Save the token securely** — anyone with it can control your bot

### Step 2 — Get your Telegram user ID
1. In Telegram, message **@userinfobot** (or **@get_id_bot**)
2. It replies instantly with your numeric ID (e.g., `123456789`)
3. Save this — it's how Hermes knows you're allowed to use the bot

### Step 3 — Wire credentials into Hermes
Recommended (interactive wizard):
```bash
hermes gateway setup
```
Select Telegram when prompted; paste token + user ID when asked.

Manual (if wizard fails):
Add to `~/.hermes/.env`:
```
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
TELEGRAM_ALLOWED_USERS=123456789
```
Multiple users? Comma-separate: `TELEGRAM_ALLOWED_USERS=123456789,987654321`

### Step 4 — Start the gateway
```bash
hermes gateway              # foreground (good for first test)
# OR
hermes gateway install      # install as background launchd service on macOS
hermes gateway start        # start the installed service
hermes gateway status       # check if running
hermes gateway stop         # stop it
```

### Step 5 — First message
1. In Telegram, search your bot's username
2. Send any message ("hello")
3. Bot replies using your default model (Opus 4.7 fast)
4. If you get "unauthorized" → your user ID doesn't match `TELEGRAM_ALLOWED_USERS`

### Optional — cron delivery channel
If you want Hermes to send scheduled reports/digests, set:
```
TELEGRAM_HOME_CHANNEL=<chat_id>
```
The chat ID for a private bot conversation = your user ID. For a group, it's a negative number you can get from @get_id_bot inside the group.

---

## Part 4 — Cost Discipline & Usage Tracking

### Real-time usage check
```bash
hermes portal             # auth status + Tool Gateway routing
# Open https://portal.nousresearch.com in browser for dashboard
```

### Antigravity-side tracking
Log notable runs to `.agent/hermes-usage.json` so future-you can see patterns. If Nous adds usage caps later, this file is the precedent.

### Soft guidelines
- Flat $20/mo, no published hard caps — but Tool Gateway is pay-as-you-go
- Don't pipe Antigravity secrets into Hermes prompts (separate trust domain)
- Don't add Hermes to `.mcp.json` — it's a CLI, not an MCP server
- If subscription adds rate caps in the future, halt at 80% — update this directive when that happens

---

## Part 5 — Invocation Reference

- Binary: `~/.local/bin/hermes` (PATH already includes `~/.local/bin/`)
- Home: `~/.hermes/` — config, OAuth tokens, sessions, logs, skills, cloned repo
- Config: `~/.hermes/config.yaml` (model defaults, provider, base_url)
- Env vars: `~/.hermes/.env` (Telegram token, optional override keys)
- Provider: `nous` (set in `~/.hermes/config.yaml` under `model.provider`)
- Default model: `anthropic/claude-opus-4.7-fast`
- Tool Gateway: image gen + browser automation routed through Nous (free with subscription)

### Re-auth (if OAuth expires)
```bash
hermes auth add nous --type oauth
```
Or just `hermes login` for the same flow. Browser opens, sign in, done.

### Logout
```bash
hermes auth logout nous
```

### Full system diagnostic
```bash
hermes doctor             # check config + dependencies
hermes status             # full status with key/auth/provider info
hermes dump               # setup summary for support tickets
```

---

## When to Use Hermes vs Other Tools

| Tool | Use When |
|------|----------|
| Claude (in this Antigravity session) | Antigravity workflows, skill execution, anything involving directives |
| **Hermes interactive (`hermes`)** | Scratchpad coding tasks, second-opinion drafts, frontier-model variety (Grok, GPT-5.5, Gemini Pro, DeepSeek v4) |
| **Hermes Telegram bot** | On-the-go assistant from phone — no laptop required |
| **Hermes one-shot (`hermes -z`)** | Quick lookups, batch scripts, anything where you want a fast non-interactive answer with a non-Claude model |
| Gemini Deep Research (Antigravity) | Foundation research (unchanged) |
| Perplexity (Antigravity) | Fact verification, real-time web (unchanged) |

---

## Future / Optional Extensions

Already-disabled features you could enable later if needed:
- **Discord bot** — `hermes gateway setup` → select Discord (needs `DISCORD_BOT_TOKEN`)
- **WhatsApp bot** — `hermes whatsapp` (multi-step setup, mileage varies)
- **Slack bot** — `hermes slack` (manifest gen) + `SLACK_BOT_TOKEN`/`SLACK_APP_TOKEN`
- **Cron jobs** — `hermes cron` to schedule recurring agent tasks
- **Webhooks** — `hermes webhook` for inbound automation triggers
- **Skills Hub** — `hermes skills search/install` to add community workflows beyond the 97 built-ins
- **Kanban orchestrator** — `hermes kanban` for multi-profile collaboration (codex-lane, worker)
- **Modal serverless** — optional Tool Gateway add-on for sandboxed code execution

---

## Rotation Hygiene

If the API key in `Google Antigravity/.env` (`NOUS_API_KEY`) is ever exposed (transcript leak, accidental commit, etc.), rotate immediately from the Nous Research dashboard at `portal.nousresearch.com` and replace the value in the `.env`. The Hermes Agent itself uses OAuth and doesn't require the API key, but the env var is available for direct curl/script use.

OAuth tokens auto-refresh; no rotation needed unless compromised. To force re-auth: `hermes auth logout nous && hermes auth add nous --type oauth`.
