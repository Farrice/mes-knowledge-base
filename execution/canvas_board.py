#!/usr/bin/env python3
"""canvas_board.py — the board file + DAG context walk + chat seat (2026-09-10).

The Poppy.ai idea, locally: nodes on a whiteboard, edges between them, and a
chat node that reads EVERYTHING upstream of it as context. One JSON file per
board on disk, so a board is also grep-able context for any later session.

    .agent/canvas/boards/<slug>.json
        nodes[]  {id, type: source|chat|note|profile, x, y, w, h, title, text,
                  source, kind, tokens, model, effort, turns[], status, error}
        edges[]  {from, to}

Context rule (stolen from canvas-chat, the one good idea there): walk the DAG
backward from the chat node, collect every ancestor, order by creation, dedupe
(a diamond graph contributes each node once). Source/note ancestors contribute
their text; chat ancestors contribute their turns. The chat node's own prior
turns are the conversation history.

Model seats (Farrice's ruling 2026-09-10: Claude rides the subscription):
    sonnet / opus / fable  → `claude -p` headless, cwd OUTSIDE the repo so no
                             CLAUDE.md, hooks or skills load — a pure model call;
                             cost is MEASURED from --output-format json
    gemini-flash / -pro    → execution/gemini_client.py (metered, cents, ledgered)
    gpt / gpt-mini         → `codex exec` headless on the ChatGPT subscription

Nothing here calls the Anthropic or OpenAI API directly (directives/model-notes.md).

CLI:
    python3 execution/canvas_board.py demo                       # seed a demo board
    python3 execution/canvas_board.py list
    python3 execution/canvas_board.py context <slug> <chat_id>   # show what a chat node sees
    python3 execution/canvas_board.py run <slug> <chat_id> "<prompt>"
    python3 execution/canvas_board.py add <slug> <url-or-text> [--x N --y N]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
BOARDS = ROOT / ".agent" / "canvas" / "boards"
SCRATCH = Path(os.environ.get("CANVAS_SCRATCH") or "~/.cache/antigravity-canvas").expanduser()
PY = sys.executable or "python3"
sys.path.insert(0, str(EXEC))

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
ID_RE = re.compile(r"^[a-z]{1,8}_[0-9a-f]{8}$")

# label → (seat, model-arg, default effort, effort choices)
MODELS = {
    "sonnet":       ("claude", "sonnet",  "medium", ["low", "medium", "high", "xhigh"]),
    "opus":         ("claude", "opus",    "medium", ["low", "medium", "high", "xhigh"]),
    "fable":        ("claude", "claude-fable-5-1", "medium", ["low", "medium", "high", "xhigh"]),
    "gemini-flash": ("gemini", "flash",   "low",    ["low", "high"]),
    "gemini-pro":   ("gemini", "pro",     "high",   ["low", "high"]),
    "gpt":          ("codex",  None,      "medium", ["low", "medium", "high", "xhigh"]),
}
DEFAULT_MODEL = "sonnet"
CLAUDE_TIMEOUT_S = 900
NODE_W, NODE_H = 300, 180
CHAT_W, CHAT_H = 420, 320

SYSTEM = (
    "You are a chat node on Farrice Cain's canvas. Everything under SOURCES was "
    "placed on the board and wired to you on purpose; treat it as the working "
    "material and cite it by [S#] when you draw on it. Do not invent facts that "
    "are not in the sources or the conversation. Answer directly, in plain "
    "English, at the length the question needs. No preamble, no closing offer."
)


# ----------------------------------------------------------------------------
# board io
# ----------------------------------------------------------------------------

def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def _nid(kind: str) -> str:
    return f"{kind}_{uuid.uuid4().hex[:8]}"


def board_path(slug: str) -> Path:
    if not SLUG_RE.match(slug or ""):
        raise ValueError(f"bad board slug: {slug!r}")
    return BOARDS / f"{slug}.json"


def list_boards() -> list[dict]:
    BOARDS.mkdir(parents=True, exist_ok=True)
    out = []
    for p in sorted(BOARDS.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
        try:
            b = json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            continue
        out.append({"slug": b.get("slug", p.stem), "title": b.get("title", p.stem),
                    "nodes": len(b.get("nodes", [])), "updated": b.get("updated")})
    return out


def new_board(slug: str, title: str | None = None) -> dict:
    return {"slug": slug, "title": title or slug.replace("-", " "), "created": _now(),
            "updated": _now(), "seq": 0, "view": {"x": 0, "y": 0, "k": 1},
            "nodes": [], "edges": []}


def load(slug: str, create: bool = False) -> dict:
    p = board_path(slug)
    if not p.exists():
        if create:
            b = new_board(slug)
            save(b)
            return b
        raise FileNotFoundError(f"no board: {slug}")
    return _migrate(json.loads(p.read_text(encoding="utf-8")))


def _migrate(board: dict) -> dict:
    """v1 chat nodes kept one `turns` list; Poppy-form chats hold several
    conversations. Wrap the old list once; `chat_turns()` is the accessor."""
    for n in board.get("nodes", []):
        if n.get("type") == "chat" and "convos" not in n:
            n["convos"] = [{"id": _nid("cv"), "title": "Conversation 1",
                            "turns": n.pop("turns", []) or [], "created": n.get("created", _now())}]
            n["active"] = n["convos"][0]["id"]
    return board


def active_convo(n: dict) -> dict:
    if "convos" not in n:
        _migrate({"nodes": [n]})
    for c in n["convos"]:
        if c["id"] == n.get("active"):
            return c
    n["active"] = n["convos"][0]["id"]
    return n["convos"][0]


def chat_turns(n: dict) -> list:
    return active_convo(n)["turns"]


def add_convo(board: dict, nid: str, title: str | None = None) -> dict:
    n = _node(board, nid)
    active_convo(n)
    c = {"id": _nid("cv"), "title": title or f"Conversation {len(n['convos']) + 1}",
         "turns": [], "created": _now()}
    n["convos"].append(c)
    n["active"] = c["id"]
    n["status"] = "idle"
    n["error"] = None
    return c


def convo_op(board: dict, nid: str, op: str, cid: str = "", title: str | None = None) -> dict:
    n = _node(board, nid)
    active_convo(n)
    if op == "new":
        return add_convo(board, nid, title)
    c = next((c for c in n["convos"] if c["id"] == cid), None)
    if c is None:
        raise KeyError(f"no conversation {cid}")
    if op == "switch":
        n["active"] = c["id"]
    elif op == "rename":
        c["title"] = (title or c["title"])[:120]
    elif op == "delete":
        if len(n["convos"]) == 1:
            c["turns"] = []
        else:
            n["convos"] = [x for x in n["convos"] if x["id"] != cid]
            if n["active"] == cid:
                n["active"] = n["convos"][-1]["id"]
    else:
        raise ValueError(f"unknown convo op {op!r}")
    return active_convo(n)


def save(board: dict) -> Path:
    board["updated"] = _now()
    p = board_path(board["slug"])
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(board, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, p)
    return p


def _node(board: dict, nid: str) -> dict:
    for n in board["nodes"]:
        if n["id"] == nid:
            return n
    raise KeyError(f"no node {nid}")


def _next_seq(board: dict) -> int:
    board["seq"] = int(board.get("seq", 0)) + 1
    return board["seq"]


# ----------------------------------------------------------------------------
# mutations (cheap; the server calls these in-process)
# ----------------------------------------------------------------------------

def add_source(board: dict, source: str, x: float = 40, y: float = 40, force: bool = False) -> dict:
    """Ingest a URL/path/text and drop it on the board as a source node.
    Ingestion is the slow part (seconds to minutes for whisper); callers that
    must not block spawn `canvas_board.py add` detached and poll the file."""
    import ingest_url
    rec = ingest_url.ingest(source, force=force)
    n = {"id": _nid("src"), "type": "source", "seq": _next_seq(board),
         "x": x, "y": y, "w": NODE_W, "h": NODE_H,
         "title": rec["title"], "kind": rec["kind"], "source": source[:500],
         "text": rec["text"], "tokens": rec["meta"].get("tokens_est", 0),
         "meta": {k: v for k, v in rec["meta"].items() if k not in ("source",)},
         "created": _now(), "status": "idle"}
    board["nodes"].append(n)
    return n


def add_pending_source(board: dict, source: str, x: float = 40, y: float = 40) -> dict:
    """Placeholder the UI can show immediately; `fill_source` completes it."""
    n = {"id": _nid("src"), "type": "source", "seq": _next_seq(board),
         "x": x, "y": y, "w": NODE_W, "h": NODE_H,
         "title": source[:80], "kind": "pending", "source": source[:500],
         "text": "", "tokens": 0, "meta": {}, "created": _now(), "status": "running"}
    board["nodes"].append(n)
    return n


def fill_source(slug: str, nid: str, force: bool = False) -> dict:
    """Run ingestion for a pending node and write the result back (reloads the
    board file first so concurrent moves are not clobbered)."""
    import ingest_url
    board = load(slug)
    n = _node(board, nid)
    try:
        rec = ingest_url.ingest(n["source"], force=force)
        n.update(title=rec["title"], kind=rec["kind"], text=rec["text"],
                 tokens=rec["meta"].get("tokens_est", 0),
                 meta={k: v for k, v in rec["meta"].items() if k != "source"},
                 status="idle", error=None)
    except Exception as e:
        n.update(status="error", error=str(e)[:300], kind="error")
    save(board)
    return n


def add_chat(board: dict, x: float = 420, y: float = 40, model: str = DEFAULT_MODEL,
             title: str = "chat") -> dict:
    if model not in MODELS:
        raise ValueError(f"unknown model {model!r}; choose from {', '.join(MODELS)}")
    cid = _nid("cv")
    n = {"id": _nid("chat"), "type": "chat", "seq": _next_seq(board),
         "x": x, "y": y, "w": CHAT_W, "h": CHAT_H, "title": title,
         "model": model, "effort": MODELS[model][2],
         "convos": [{"id": cid, "title": "Conversation 1", "turns": [], "created": _now()}],
         "active": cid, "created": _now(), "status": "idle"}
    board["nodes"].append(n)
    return n


def list_profile(url: str, limit: int = 10) -> list[dict]:
    """A creator's latest posts, free: yt-dlp --flat-playlist (YouTube channels,
    TikTok profiles; ~1-3 s). Instagram is login-walled here — vidIQ path later."""
    import ingest_url
    if "instagram.com" in url:
        raise ValueError("Instagram profiles need the vidIQ connector (not wired yet); paste single reel URLs instead")
    u = url.rstrip("/")
    if "youtube.com" in u and not u.endswith("/videos") and "/playlist" not in u:
        u += "/videos"
    ytdlp = shutil.which("yt-dlp", path=ingest_url._env().get("PATH")) or "yt-dlp"
    fmt = "%(url)s\t%(id)s\t%(title)s\t%(view_count)s\t%(duration)s\t%(upload_date)s"
    r = subprocess.run([ytdlp, "--flat-playlist", "-I", f"1:{int(limit)}", "--print", fmt, "--", u],
                       capture_output=True, text=True, timeout=60, env=ingest_url._env())
    posts = []
    for line in (r.stdout or "").splitlines():
        p = line.split("\t")
        if len(p) < 6 or not p[0].startswith("http"):
            continue
        def _n(v):
            try:
                return int(float(v))
            except (TypeError, ValueError):
                return None
        vid = p[1]
        thumb = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg" if "youtube.com" in p[0] or "youtu.be" in p[0] else ""
        posts.append({"url": p[0], "id": vid, "title": p[2], "views": _n(p[3]),
                      "duration_s": _n(p[4]), "date": p[5] if p[5] != "NA" else "", "thumb": thumb})
    if not posts:
        raise RuntimeError((r.stderr or "no posts found")[-300:].strip())
    return posts


def add_profile(board: dict, url: str, x: float = 40, y: float = 40, limit: int = 10) -> dict:
    """Poppy's profile card: handle → latest posts with views. The listing text
    is also context (a chat wired to it knows what the creator posts)."""
    posts = list_profile(url, limit)
    handle = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
    lines = [f"- {p['title']} · {p['views'] or '?'} views · {p['duration_s'] or '?'} s · {p['url']}" for p in posts]
    text = f"{handle} — latest {len(posts)} posts (yt-dlp flat listing)\n" + "\n".join(lines)
    n = {"id": _nid("prof"), "type": "profile", "seq": _next_seq(board),
         "x": x, "y": y, "w": NODE_W, "h": 360, "title": handle, "kind": "profile",
         "source": url[:500], "text": text, "tokens": max(0, len(text) // 4), "posts": posts,
         "meta": {"fetched": _now()}, "created": _now(), "status": "idle"}
    board["nodes"].append(n)
    return n


def add_note(board: dict, text: str, x: float = 40, y: float = 260, title: str = "note") -> dict:
    n = {"id": _nid("note"), "type": "note", "seq": _next_seq(board),
         "x": x, "y": y, "w": NODE_W, "h": 140, "title": title, "text": text,
         "tokens": max(1, len(text) // 4), "created": _now(), "status": "idle"}
    board["nodes"].append(n)
    return n


def add_edge(board: dict, src: str, dst: str) -> bool:
    if src == dst:
        return False
    _node(board, src)
    _node(board, dst)
    if any(e["from"] == src and e["to"] == dst for e in board["edges"]):
        return True
    # refuse a cycle: dst must not already be upstream of src
    if dst in ancestors(board, src):
        return False
    board["edges"].append({"from": src, "to": dst})
    return True


def remove_edge(board: dict, src: str, dst: str) -> None:
    board["edges"] = [e for e in board["edges"] if not (e["from"] == src and e["to"] == dst)]


def remove_node(board: dict, nid: str) -> None:
    board["nodes"] = [n for n in board["nodes"] if n["id"] != nid]
    board["edges"] = [e for e in board["edges"] if nid not in (e["from"], e["to"])]


def move(board: dict, nid: str, x=None, y=None, w=None, h=None) -> dict:
    n = _node(board, nid)
    for k, v in (("x", x), ("y", y), ("w", w), ("h", h)):
        if v is not None:
            n[k] = float(v)
    return n


def set_model(board: dict, nid: str, model: str | None = None, effort: str | None = None,
              research: bool | None = None) -> dict:
    n = _node(board, nid)
    if research is not None:
        n["research"] = bool(research)  # web tools for the Claude seat only (see _seat_claude)
    if model:
        if model not in MODELS:
            raise ValueError(f"unknown model {model!r}")
        n["model"] = model
        if effort is None and n.get("effort") not in MODELS[model][3]:
            n["effort"] = MODELS[model][2]
    if effort:
        if effort not in MODELS[n["model"]][3]:
            raise ValueError(f"effort {effort!r} not valid for {n['model']}")
        n["effort"] = effort
    return n


def edit_text(board: dict, nid: str, text: str | None = None, title: str | None = None) -> dict:
    n = _node(board, nid)
    if title is not None:
        n["title"] = title[:200]
    if text is not None and n["type"] in ("note", "source"):
        n["text"] = text
        n["tokens"] = max(1, len(text) // 4)
    return n


# ----------------------------------------------------------------------------
# the DAG walk
# ----------------------------------------------------------------------------

def ancestors(board: dict, nid: str) -> list[str]:
    """Every node upstream of nid, deduped, ordered by creation seq."""
    parents: dict[str, list[str]] = {}
    for e in board["edges"]:
        parents.setdefault(e["to"], []).append(e["from"])
    seen: set[str] = set()
    stack = list(parents.get(nid, []))
    while stack:
        cur = stack.pop()
        if cur in seen or cur == nid:
            continue
        seen.add(cur)
        stack.extend(parents.get(cur, []))
    order = {n["id"]: n.get("seq", 0) for n in board["nodes"]}
    return sorted(seen, key=lambda i: (order.get(i, 0), i))


def context_for(board: dict, chat_id: str) -> dict:
    """What this chat node sees: numbered source blocks + upstream chat turns."""
    chat = _node(board, chat_id)
    blocks, upstream_turns = [], []
    idx = 0
    for aid in ancestors(board, chat_id):
        n = _node(board, aid)
        if n["type"] in ("source", "note", "profile"):
            if not (n.get("text") or "").strip():
                continue
            idx += 1
            head = f"[S{idx}] {n.get('title', '')}".strip()
            src = n.get("source") or ""
            if src and n["type"] != "note" and not src.startswith(n.get("text", "")[:20]):
                head += f"\n{src}"
            blocks.append(f"{head}\n\n{n['text'].strip()}")
        elif n["type"] == "chat":
            for t in chat_turns(n):
                upstream_turns.append(f"[{n.get('title', 'chat')} · {t['role']}] {t['text']}")
    ctx = ""
    if blocks:
        ctx += "SOURCES\n=======\n\n" + "\n\n----\n\n".join(blocks)
    if upstream_turns:
        ctx += ("\n\n" if ctx else "") + "UPSTREAM CONVERSATION\n=====================\n\n" + "\n\n".join(upstream_turns)
    return {"context": ctx, "sources": idx, "upstream_turns": len(upstream_turns),
            "ancestors": ancestors(board, chat_id), "tokens_est": max(0, len(ctx) // 4),
            "history_turns": len(chat_turns(chat))}


def build_prompt(board: dict, chat_id: str, prompt: str) -> tuple[str, dict]:
    chat = _node(board, chat_id)
    ctx = context_for(board, chat_id)
    parts = []
    if ctx["context"]:
        parts.append(ctx["context"])
    hist = chat_turns(chat)
    if hist:
        lines = [f"{t['role'].upper()}: {t['text']}" for t in hist]
        parts.append("CONVERSATION SO FAR\n===================\n\n" + "\n\n".join(lines))
    parts.append(f"USER: {prompt.strip()}")
    return "\n\n\n".join(parts), ctx


# ----------------------------------------------------------------------------
# model seats
# ----------------------------------------------------------------------------

def _scratch_dir() -> Path:
    """A cwd OUTSIDE the repo so `claude -p` / `codex exec` load no CLAUDE.md,
    hooks, skills or agents — a pure model call, nothing else."""
    SCRATCH.mkdir(parents=True, exist_ok=True)
    return SCRATCH


RESEARCH_TOOLS = "WebSearch,WebFetch"
RESEARCH_SYSTEM = (
    " Research is ON for this node: before you state a current number, price, "
    "limit, date or program status, check it on the live web with WebSearch/WebFetch "
    "and put the source URL beside it. Mark anything you could not verify UNCONFIRMED."
)


def _seat_claude(model_arg: str, effort: str, full_prompt: str, research: bool = False) -> dict:
    if not shutil.which("claude"):
        raise RuntimeError("claude CLI not on PATH")
    # --tools "": no tool calls at all; scratch cwd: no CLAUDE.md/hooks. Pure model.
    # research=True opens exactly the two web tools (still no file/shell tools).
    # (--bare would also skip the login keychain → "Not logged in"; do not add it.)
    cmd = ["claude", "-p", "--tools", RESEARCH_TOOLS if research else "",
           "--model", model_arg, "--effort", effort,
           "--output-format", "json", "--no-session-persistence",
           "--append-system-prompt", SYSTEM + (RESEARCH_SYSTEM if research else "")]
    # One-shot call: nothing to compact. The user's settings.json sets
    # CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50, which made a 77K-token prompt at
    # --effort high "thrash" (2026-09-10, Jen board). Disable it for the seat.
    env = dict(os.environ, DISABLE_AUTO_COMPACT="1")
    env.pop("CLAUDE_AUTOCOMPACT_PCT_OVERRIDE", None)
    r = subprocess.run(cmd, input=full_prompt, capture_output=True, text=True,
                       timeout=CLAUDE_TIMEOUT_S, cwd=_scratch_dir(), env=env)
    out = r.stdout or ""
    try:
        j = json.loads(out)
    except ValueError:
        if r.returncode != 0:
            raise RuntimeError((r.stderr or out)[-400:].strip() or f"claude exit {r.returncode}")
        return {"text": out.strip(), "cost_usd": None, "raw": None}
    if j.get("is_error") or r.returncode != 0:
        raise RuntimeError(str(j.get("result") or r.stderr or "claude error")[-400:])
    return {"text": (j.get("result") or "").strip(), "cost_usd": j.get("total_cost_usd"),
            "duration_ms": j.get("duration_ms"), "raw_model": (j.get("modelUsage") or {})}


def _seat_gemini(tier: str, effort: str, full_prompt: str) -> dict:
    import gemini_client
    gemini_client.load_env()
    client = gemini_client.GeminiClient()
    # 2.5-era models take a thinking BUDGET, not a level; low = off, high = 8k.
    budget = {"low": None, "high": 8192}.get(effort)
    text, meta = client.generate_sync(full_prompt, system_instruction=SYSTEM, model=tier,
                                      max_output_tokens=8192, thinking_budget=budget)
    cost = getattr(meta, "cost_usd", None)
    if cost is None:
        cost = getattr(meta, "estimated_cost_usd", None)
    return {"text": (text or "").strip(), "cost_usd": cost,
            "raw_model": getattr(meta, "model", tier)}


def _seat_codex(model_arg, effort: str, full_prompt: str) -> dict:
    if not shutil.which("codex"):
        raise RuntimeError("codex CLI not on PATH")
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, dir=_scratch_dir()) as f:
        out_path = f.name
    cmd = ["codex", "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only",
           "-C", str(_scratch_dir()), "-c", f"model_reasoning_effort={effort}",
           "-o", out_path]
    if model_arg:
        cmd += ["-m", model_arg]
    cmd.append("-")  # prompt from stdin
    r = subprocess.run(cmd, input=f"{SYSTEM}\n\n{full_prompt}", capture_output=True,
                       text=True, timeout=CLAUDE_TIMEOUT_S)
    text = ""
    try:
        text = Path(out_path).read_text(encoding="utf-8").strip()
    finally:
        Path(out_path).unlink(missing_ok=True)
    if not text:
        err = (r.stderr or r.stdout or f"codex exit {r.returncode}").strip()
        if "requires a newer version of Codex" in err:
            raise RuntimeError("the installed codex CLI is too old for its default model; "
                               "upgrading codex is Farrice's call, then retry")
        if "not supported when using Codex with a ChatGPT account" in err:
            raise RuntimeError("that GPT model is not available on the ChatGPT plan through codex")
        raise RuntimeError(err[-400:])
    return {"text": text, "cost_usd": None, "raw_model": model_arg or "codex-default"}


def run_chat(slug: str, chat_id: str, prompt: str) -> dict:
    """Assemble context, call the seat, append the turn. Reloads the board at
    each write so a concurrent drag does not lose the reply."""
    board = load(slug)
    chat = _node(board, chat_id)
    if chat["type"] != "chat":
        raise ValueError("not a chat node")
    model = chat.get("model") or DEFAULT_MODEL
    seat, model_arg, default_effort, choices = MODELS[model]
    effort = chat.get("effort") if chat.get("effort") in choices else default_effort
    full_prompt, ctx = build_prompt(board, chat_id, prompt)

    convo_id = active_convo(chat)["id"]
    chat_turns(chat).append({"role": "user", "text": prompt.strip(), "ts": _now()})
    chat["status"] = "running"
    chat["error"] = None
    save(board)

    t0 = time.time()
    try:
        if seat == "claude":
            res = _seat_claude(model_arg, effort, full_prompt, research=bool(chat.get("research")))
        elif seat == "gemini":
            res = _seat_gemini(model_arg, effort, full_prompt)
        else:
            res = _seat_codex(model_arg, effort, full_prompt)
        turn = {"role": "assistant", "text": res["text"], "model": model, "seat": seat,
                "effort": effort, "research": bool(chat.get("research")) and seat == "claude",
                "cost_usd": res.get("cost_usd"), "seconds": round(time.time() - t0, 1),
                "context_tokens": ctx["tokens_est"], "sources": ctx["sources"], "ts": _now()}
        board = load(slug)
        chat = _node(board, chat_id)
        convo = next((c for c in chat["convos"] if c["id"] == convo_id), None) or active_convo(chat)
        convo["turns"].append(turn)
        if convo["title"].startswith("Conversation ") and len(convo["turns"]) == 2:
            convo["title"] = prompt.strip().replace("\n", " ")[:48]  # Poppy names the thread by its first ask
        chat["status"] = "idle"
        save(board)
        return turn
    except Exception as e:
        board = load(slug)
        chat = _node(board, chat_id)
        convo = next((c for c in chat["convos"] if c["id"] == convo_id), None) or active_convo(chat)
        turns = convo["turns"]
        if turns and turns[-1].get("role") == "user" and turns[-1].get("text") == prompt.strip():
            turns.pop()  # the ask did not land; keep the board honest so a retry is not doubled
        chat["status"] = "error"
        chat["error"] = str(e)[:400]
        save(board)
        raise


# ----------------------------------------------------------------------------
# demo + CLI
# ----------------------------------------------------------------------------

def demo(force: bool = False) -> dict:
    slug = "demo"
    if board_path(slug).exists() and not force:
        return load(slug)
    b = new_board(slug, "demo · diamond graph")
    a = add_note(b, "Farrice's rule: nothing is a cage. Two things may block work: the cost gate and the factual veto. Everything else nudges.", 40, 40, "compass doctrine")
    c = add_note(b, "Poppy.ai: paste a URL, a transcript node appears; wire it to a chat; the chat reads every upstream node. $399/yr wall was pricing posture, not infrastructure.", 40, 240, "poppy mechanics")
    mid = add_chat(b, 420, 40, "sonnet", "synthesis")
    top = add_chat(b, 900, 40, "sonnet", "final")
    add_edge(b, a["id"], mid["id"])
    add_edge(b, c["id"], mid["id"])
    add_edge(b, mid["id"], top["id"])
    add_edge(b, a["id"], top["id"])  # diamond: a reaches top twice, must count once
    save(b)
    return b


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    d = sub.add_parser("demo")
    d.add_argument("--force", action="store_true")
    c = sub.add_parser("context")
    c.add_argument("slug")
    c.add_argument("chat_id")
    r = sub.add_parser("run")
    r.add_argument("slug")
    r.add_argument("chat_id")
    r.add_argument("prompt")
    a = sub.add_parser("add")
    a.add_argument("slug")
    a.add_argument("source")
    a.add_argument("--x", type=float, default=40)
    a.add_argument("--y", type=float, default=40)
    a.add_argument("--force", action="store_true")
    f = sub.add_parser("fill")
    f.add_argument("slug")
    f.add_argument("node_id")
    f.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if args.cmd == "list":
        for b in list_boards():
            print(f"{b['slug']:<24} {b['nodes']:>3} nodes  {b['updated']}  {b['title']}")
        return 0
    if args.cmd == "demo":
        b = demo(force=args.force)
        print(f"demo board → {board_path('demo')}  ({len(b['nodes'])} nodes, {len(b['edges'])} edges)")
        for n in b["nodes"]:
            print(f"  {n['id']:<16} {n['type']:<7} {n.get('title')}")
        return 0
    if args.cmd == "context":
        ctx = context_for(load(args.slug), args.chat_id)
        print(f"sources={ctx['sources']} upstream_turns={ctx['upstream_turns']} "
              f"~{ctx['tokens_est']:,} tokens · ancestors={ctx['ancestors']}\n")
        print(ctx["context"])
        return 0
    if args.cmd == "run":
        turn = run_chat(args.slug, args.chat_id, args.prompt)
        cost = turn.get("cost_usd")
        print(f"[{turn['model']}/{turn['effort']} · {turn['seconds']}s · "
              f"{'$%.4f' % cost if isinstance(cost, (int, float)) else 'subscription'} · "
              f"{turn['context_tokens']:,} ctx tokens]\n")
        print(turn["text"])
        return 0
    if args.cmd == "add":
        b = load(args.slug, create=True)
        n = add_source(b, args.source, args.x, args.y, force=args.force)
        save(b)
        print(f"{n['id']}  {n['kind']} · {n['title']} · ~{n['tokens']:,} tokens")
        return 0
    if args.cmd == "fill":
        n = fill_source(args.slug, args.node_id, force=args.force)
        print(f"{n['id']}  {n['status']} · {n.get('kind')} · {n.get('title')} · ~{n.get('tokens', 0):,} tokens"
              + (f"\n  error: {n.get('error')}" if n.get("error") else ""))
        return 0 if n["status"] != "error" else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
