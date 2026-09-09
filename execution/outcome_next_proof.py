"""Outcome ownership companion for the existing Codex hook adapter.

Prompt delivery plus bounded, observe-only current-turn checks. No LLM calls,
network, new hook registration, or hard blocks. NO_FLAG never means quality PASS.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

CONTRACT = "semantic_libraries/antigravity/primitives/operating-alignment-contract.md"
BEGIN = "<!-- BEGIN:outcome-next-proof -->"
END = "<!-- END:outcome-next-proof -->"
MAX_TRANSCRIPT_BYTES = 4 * 1024 * 1024


def meaningful(prompt: str) -> bool:
    p = prompt.strip()
    if not p or p.startswith("[SYSTEM NOTIFICATION") or "<task-notification>" in p:
        return False
    if "<send_user_message_question_reply>" in p:
        p = re.sub(r"<send_user_message_question_reply>.*?</send_user_message_question_reply>", "", p, flags=re.S).strip()
    if re.fullmatch(r"(?i)(thanks[!. ]*|thank you[!. ]*|ok(?:ay)?[!. ]*|yes[!. ]*|no[!. ]*|stop[!. ]*|continue[!. ]*|ready[!. ]*|done[!. ]*)", p):
        return False
    if re.match(r"(?i)^(translate|spell|what time|what is \d|what's \d)\b", p):
        return False
    return len(p.split()) >= 7 or bool(re.match(r"^(?:/|\$)[a-z][\w-]{3,}", p))


def prompt_context(payload: dict, root: Path) -> str:
    if not meaningful(str(payload.get("prompt") or "")):
        return ""
    text = (root / CONTRACT).read_text()
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("outcome contract markers missing or ambiguous")
    return text.split(BEGIN, 1)[1].split(END, 1)[0].strip()


def merge_context(stdout: str, extra: str) -> str:
    """Preserve existing JSON fields/decisions; never concatenate invalid JSON."""
    if not extra:
        return stdout
    if stdout.strip():
        data = json.loads(stdout)
        if not isinstance(data, dict):
            raise ValueError("existing hook output is not an object")
    else:
        data = {}
    specific = data.setdefault("hookSpecificOutput", {})
    if specific.get("hookEventName", "UserPromptSubmit") != "UserPromptSubmit":
        raise ValueError("unexpected hook event")
    specific["hookEventName"] = "UserPromptSubmit"
    existing = specific.get("additionalContext", "")
    specific["additionalContext"] = "\n\n".join(x for x in (existing, extra) if x)
    return json.dumps(data)


def _text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(str(x.get("text", "")) for x in content if isinstance(x, dict) and x.get("type") in ("text", "input_text", "output_text"))
    return ""


def _success(output) -> bool:
    """Only explicit success signals; plain prose and unknown tools aren't proof."""
    if isinstance(output, str):
        try:
            output = json.loads(output)
        except (ValueError, TypeError):
            return False
    if not isinstance(output, dict):
        return False
    if any(output.get(k) is True for k in ("isError", "is_error", "interrupted")):
        return False
    code = output.get("exit_code", output.get("exitCode"))
    if isinstance(code, int):
        return code == 0
    return output.get("success") is True or output.get("isError") is False


def _inspection_call(name: str, arguments) -> bool:
    """Recognize retrieval, not arbitrary successful activity (mkdir, clock, etc.).

    This establishes only an observed inspection opportunity, not relevance or
    sufficient diligence. Unknown orchestration wrappers remain unobserved.
    """
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except ValueError:
            arguments = {}
    arguments = arguments if isinstance(arguments, dict) else {}
    short = name.rsplit("__", 1)[-1].rsplit(".", 1)[-1].lower()
    if short in ("read", "read_thread", "read_mcp_resource", "get_pricing", "search", "search_query"):
        return True
    if "web" in name.lower() and short == "run":
        return any(arguments.get(k) for k in ("search_query", "open", "find"))
    if short in ("exec_command", "bash"):
        command = str(arguments.get("cmd", arguments.get("command", ""))).strip()
        return bool(re.match(r"^(?:cat|rg|ls|sed|head|tail|git (?:show|diff|status))\s", command))
    return False


def current_turn(records: list[dict], session_id: str = "") -> dict:
    """Read native Codex response_item and Claude message records, never reasoning.

    Reset on each real user message. Tool-result user envelopes do not reset a
    Claude turn. Ignore duplicated event_msg mirrors and previous-turn evidence.
    Missing current user/final response remains UNOBSERVED.
    """
    turn = {"prompt": "", "answer": "", "observed_success": False, "tool_results": 0, "identity_mismatch": False}
    calls = {}
    for record in records:
        kind = record.get("type")
        item = record.get("payload", {}) if kind == "response_item" else record.get("message", {})
        if kind == "session_meta" and session_id:
            sid = (record.get("payload") or {}).get("id")
            if sid and sid != session_id:
                turn["identity_mismatch"] = True
                return turn
        if kind in ("user", "assistant") and session_id and record.get("sessionId") not in (None, session_id):
            turn["identity_mismatch"] = True
            return turn
        if not isinstance(item, dict):
            continue
        if kind == "response_item" and item.get("type") in ("function_call", "custom_tool_call"):
            calls[item.get("call_id")] = _inspection_call(str(item.get("name", "")), item.get("arguments", item.get("input")))
        elif kind == "response_item" and item.get("type") in ("function_call_output", "custom_tool_call_output"):
            turn["tool_results"] += 1
            turn["observed_success"] |= bool(calls.get(item.get("call_id"))) and _success(item.get("output"))
        elif kind in ("response_item", "user", "assistant"):
            role = item.get("role", kind)
            content = item.get("content", [])
            text = _text(content)
            if role == "user" and text and "<task-notification>" not in text:
                turn.update(prompt=text, answer="", observed_success=False, tool_results=0)
                calls.clear()
            elif role == "assistant" and text and item.get("phase") not in ("commentary", "analysis"):
                turn["answer"] = text
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        calls[block.get("id")] = _inspection_call(str(block.get("name", "")), block.get("input"))
                    elif isinstance(block, dict) and block.get("type") == "tool_result":
                        turn["tool_results"] += 1
                        turn["observed_success"] |= bool(calls.get(block.get("tool_use_id"))) and block.get("is_error") is False
    return turn


def assess(turn: dict) -> dict:
    """Heuristic review cues, not a semantic judge or a compliance score."""
    prompt, answer = turn.get("prompt", ""), turn.get("answer", "")
    if turn.get("identity_mismatch") or not prompt or not answer:
        return {"status": "UNOBSERVED", "flags": [], "quality_verified": False}
    if not meaningful(prompt):
        return {"status": "SKIP", "flags": [], "quality_verified": False}
    p, a = prompt.lower(), answer.lower()
    flags = []
    provider = re.search(r"\b(subscribe|buy credits|use (?:flow|heygen|fal|autoreel|runway)|recommend (?:flow|heygen|fal|autoreel|runway))\b", a)
    uncertain = re.search(r"\b(unverified|not yet checked|haven't checked|have not checked|not tested|untested|provisional)\b", a)
    if provider and not turn.get("observed_success") and not uncertain:
        flags.append("provider_recommendation_without_observed_inspection")
    wants_build = re.search(r"\b(build|make|develop)\b.{0,70}\b(app|tool|software)\b", p, re.S)
    if wants_build and provider and not re.search(r"\b(private (?:app|tool)|custom (?:app|tool)|build|prototype|assistant-operated|operated by me)\b", a):
        flags.append("requested_build_route_omitted")
    invalid = re.search(r"\b(mismatched|wrong (?:photo|image)|invalid test|upload failed|upload failure)\b", p + "\n" + a)
    rejects = re.search(r"\b(impossible|cannot work|can't work|not feasible)\b", a)
    qualifies = re.search(r"\b(does not prove|doesn't prove|cannot conclude|can't conclude|does not establish|doesn't establish|not a clean test)\b", a)
    if invalid and rejects and not qualifies:
        flags.append("invalid_test_used_for_broad_rejection")
    action = re.search(r"\b(install|implement|fix|create|build|run|execute)\b", p)
    handback = re.search(r"\b(would you like me to|let me know if you want|you can run|tell me when you want)\b", a)
    boundary = re.search(r"\b(read.only|analysis.only|ideation|don't build|do not build|before implementing|plan only)\b", p)
    blocker = re.search(r"\b(approval|permission|blocked|unavailable|missing|requires your|need your|access denied)\b", a)
    if action and handback and not boundary and not blocker and not turn.get("observed_success"):
        flags.append("possible_premature_handoff")
    if boundary and re.search(r"\b(i (?:installed|modified|deleted)|changes (?:are )?committed)\b", a):
        flags.append("claimed_mutation_in_read_only_turn")
    return {"status": "REVIEW_REQUIRED" if flags else "NO_FLAG", "flags": flags, "quality_verified": False}


def observe_stop(payload: dict, root: Path) -> str:
    path = payload.get("transcript_path")
    if not path or payload.get("stop_hook_active"):
        return ""
    with Path(path).open("rb") as handle:
        handle.seek(0, 2)
        size = handle.tell()
        handle.seek(max(0, size - MAX_TRANSCRIPT_BYTES))
        raw = handle.read(MAX_TRANSCRIPT_BYTES)
    records = []
    for line in raw.decode("utf-8", errors="replace").splitlines():
        try:
            rec = json.loads(line)
            if isinstance(rec, dict):
                records.append(rec)
        except ValueError:
            continue
    turn = current_turn(records, str(payload.get("session_id") or ""))
    verdict = assess(turn)
    if verdict["status"] == "SKIP":
        return ""
    # Existing observation stream; hashes identify the turn without copying prose.
    log = root / ".agent/sessions/observe-log.jsonl"
    signature = hashlib.sha256((str(payload.get("session_id")) + turn["prompt"] + turn["answer"]).encode()).hexdigest()
    if log.exists():
        with log.open("rb") as handle:
            handle.seek(0, 2)
            handle.seek(max(0, handle.tell() - 65536))
            if signature.encode() in handle.read():
                return ""
    record = {"ts": datetime.now(timezone.utc).isoformat(), "event": "outcome-next-proof", "session_id": payload.get("session_id"), "signature": signature, **verdict}
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a") as handle:
        handle.write(json.dumps(record) + "\n")
    if verdict["flags"]:
        return "OUTCOME REVIEW (advisory; not a quality verdict): " + "; ".join(verdict["flags"]) + ". Check the actual task evidence; preserve the user's scope and approval boundaries.\n"
    return ""


def augment(target: str, args: list[str], payload: dict, root: Path, stdout: str, stderr: str) -> tuple[str, str]:
    if os.environ.get("OUTCOME_NEXT_PROOF_OFF") == "1":
        return stdout, stderr
    try:
        if target == "skill-router":
            stdout = merge_context(stdout, prompt_context(payload, root))
        elif target == "session-ledger" and args == ["stop"]:
            stderr += observe_stop(payload, root)
    except Exception as exc:
        stderr += f"[outcome-next-proof] UNOBSERVED ({type(exc).__name__}); existing hook preserved.\n"
    return stdout, stderr
