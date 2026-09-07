"""Observe native Codex and Claude tool events without inventing success.

Normalization is shared by the Codex adapter and direct ledger replays. It does
not flatten tool batches or infer actions from commentary; only actual events
count. Unknown or still-running responses stay distinct from completed work.
"""
from __future__ import annotations

import re
import shlex
from pathlib import Path


def normalize_event(payload: dict) -> dict:
    event = dict(payload)
    name = str(event.get('tool_name', ''))
    short = name.rsplit('__', 1)[-1].rsplit('.', 1)[-1]
    tin = event.get('tool_input') or {}
    if short == 'exec_command':
        event['native_tool_name'] = name
        event['tool_name'] = 'Bash'
        tin = dict(tin) if isinstance(tin, dict) else {}
        tin['command'] = tin.get('command', tin.get('cmd', ''))
    elif short == 'write_stdin':
        event['native_tool_name'] = name
        event['tool_name'] = 'shell_poll'
    elif short in ('apply_patch', 'spawn_agent'):
        event['native_tool_name'] = name
        event['tool_name'] = short
        if isinstance(tin, str):
            tin = {'patch': tin} if short == 'apply_patch' else {}
    if event.get('tool_name') == 'Bash' and isinstance(tin, dict):
        tin = dict(tin)
        tin['command'] = tin.get('command', tin.get('cmd', ''))
    event['tool_input'] = tin if isinstance(tin, dict) else {}
    return event


def response_text(event: dict) -> str:
    response = event.get('tool_response')
    if isinstance(response, dict):
        fields = [str(response.get(k, '')) for k in ('stdout', 'stderr', 'output')]
        content = response.get('content')
        if isinstance(content, list):
            fields.extend(str(c.get('text', '')) for c in content if isinstance(c, dict))
        return '\n'.join(fields)
    return str(response or '')


def event_status(event: dict) -> str:
    response = event.get('tool_response')
    if event.get('is_error') is True:
        return 'failed'
    if isinstance(response, dict):
        if any(response.get(k) is True for k in ('interrupted', 'isError', 'is_error')):
            return 'failed'
        # Claude's command semantics distinguish grep no-matches from failure.
        interpretation = response.get('returnCodeInterpretation')
        if interpretation:
            return 'failed' if str(interpretation).startswith('Command failed') else 'succeeded'
        code = response.get('exit_code', response.get('exitCode'))
        if isinstance(code, int):
            return 'succeeded' if code == 0 else 'failed'
        if response.get('session_id') is not None and event.get('tool_name') == 'Bash':
            return 'running'
        if response.get('success') is False:
            return 'failed'
        if response.get('success') is True or response.get('agent_id'):
            return 'succeeded'
    output = response_text(event)
    if re.search(r'command not found|Traceback \(most recent call last\)|Error:|FAILED|fatal:|No such file or directory|Permission denied|ModuleNotFoundError|SyntaxError', output):
        return 'failed'
    if event.get('tool_name') == 'apply_patch':
        return 'succeeded' if re.search(r'Success[.!:]|Updated the following files', output) else 'unknown'
    if isinstance(response, dict) and any(k in response for k in ('stdout', 'stderr')):
        return 'succeeded'  # Legacy Claude PostToolUse response, no error signal.
    if event.get('tool_name') in ('Read', 'Write', 'Edit', 'NotebookEdit', 'Skill', 'Task', 'Agent') and response is not None:
        return 'succeeded'  # These legacy PostToolUse events are emitted after success.
    return 'unknown'


def full_read_paths(event: dict) -> list[str]:
    if event_status(event) != 'succeeded':
        return []
    tin = event['tool_input']
    response = event.get('tool_response')
    text = response_text(event)
    if (isinstance(response, dict) and any(response.get(k) for k in ('truncated', 'is_truncated'))
            or re.search(r'tokens truncated|output.{0,15}truncated|truncated.{0,15}output', text, re.I)):
        return []
    if isinstance(response, dict):
        file_info = response.get('file')
        if isinstance(file_info, dict):
            total, returned = file_info.get('totalLines'), file_info.get('numLines')
            if isinstance(total, int) and isinstance(returned, int) and returned < total:
                return []
    if event.get('tool_name') == 'Read':
        if tin.get('offset') or tin.get('limit'):
            return []
        return [str(tin['file_path'])] if tin.get('file_path') else []
    if event.get('tool_name') != 'Bash':
        return []
    command = str(tin.get('command', ''))
    # A complete plain cat is observable. Pipelines, slices, substitutions and
    # command lists need independent read evidence, not a guessed full load.
    if any(c in command for c in '|;&<>`$\n'):
        return []
    try:
        tokens = shlex.split(command)
    except ValueError:
        return []
    if not tokens or tokens[0] not in ('cat', '/bin/cat'):
        return []
    paths = tokens[1:]
    if paths and paths[0] == '--':
        paths = paths[1:]
    if not paths or any(p.startswith('-') or any(c in p for c in '*?[') for p in paths):
        return []
    return paths


def produced_paths(event: dict) -> list[str]:
    if event_status(event) != 'succeeded':
        return []
    tin = event['tool_input']
    if event.get('tool_name') in ('Write', 'Edit', 'NotebookEdit'):
        path = tin.get('file_path', tin.get('notebook_path', ''))
        return [str(path)] if path else []
    if event.get('tool_name') == 'apply_patch':
        patch = str(tin.get('patch', tin.get('input', '')))
        return list(dict.fromkeys(re.findall(r'^\*\*\* (?:Add File|Update File|Move to): (.+)$', patch, re.M)))
    return []


def relative_path(path: str, event: dict, root: Path) -> str | None:
    cwd = Path(str(event['tool_input'].get('workdir') or event.get('cwd') or root))
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = cwd / candidate
    try:
        return '/' + candidate.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return None  # An external edit is not this workspace's deliverable.


def command_invokes(command: str, script: str, action: str | None = None, *,
                    root: Path | None = None, cwd: Path | None = None) -> bool:
    """Recognize a simple actual script invocation; mentions are not execution."""
    if any(c in command for c in '|;&<>`$\n'):
        return False
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False
    if not tokens:
        return False
    program = tokens.pop(0)
    first = Path(program).name
    if re.fullmatch(r'python(?:\d+(?:\.\d+)*)?', first):
        while tokens and tokens[0] in ('-B', '-u', '-I', '-E', '-s'):
            tokens.pop(0)
        if not tokens or tokens[0].startswith('-'):
            return False
        program = tokens.pop(0)
        first = Path(program).name
    if root is not None:
        actual = Path(program)
        if not actual.is_absolute():
            actual = (cwd or root) / actual
        if actual.resolve() != (root / "execution" / script).resolve():
            return False
    return first == script and (action is None or bool(tokens) and tokens[0] == action)
