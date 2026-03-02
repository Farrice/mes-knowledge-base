import os
import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

CHECKPOINT_DIR = ".agent/checkpoints"
SESSION_STATE_PATH = ".agent/session-state.md"

def _get_checkpoint_path(workflow_name: str) -> str:
    """Returns the absolute path to the checkpoint file for a given workflow."""
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in workflow_name)
    return os.path.join(CHECKPOINT_DIR, f"{safe_name}.json")

def save_checkpoint(workflow_name: str, step: str, data: Any) -> None:
    """
    Persist state after each successful step in a workflow.
    
    Args:
        workflow_name: A unique identifier for the workflow execution.
        step: The name or identifier of the completed step.
        data: JSON-serializable context or data to save.
    """
    checkpoint_path = _get_checkpoint_path(workflow_name)
    
    checkpoint_data: Dict[str, Any] = {"step": step, "data": data}
    
    with open(checkpoint_path, 'w', encoding='utf-8') as f:
        json.dump(checkpoint_data, f, indent=2)

def load_checkpoint(workflow_name: str) -> Optional[Dict[str, Any]]:
    """
    Resume from the last successful step.
    
    Args:
        workflow_name: A unique identifier for the workflow execution.
        
    Returns:
        A dictionary containing the last completed 'step' and its 'data',
        or None if no checkpoint exists.
    """
    checkpoint_path = _get_checkpoint_path(workflow_name)
    
    if not os.path.exists(checkpoint_path):
        return None
        
    try:
        with open(checkpoint_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Corrupt or unreadable checkpoint
        return None

def clear_checkpoint(workflow_name: str) -> bool:
    """
    Clean up after successful completion of a workflow.
    
    Args:
        workflow_name: A unique identifier for the workflow execution.
        
    Returns:
        True if the checkpoint was found and deleted, False otherwise.
    """
    checkpoint_path = _get_checkpoint_path(workflow_name)
    
    if os.path.exists(checkpoint_path):
        try:
            os.remove(checkpoint_path)
            return True
        except OSError:
            pass
    return False


# --- Session State Anchors (Anti-Drift) ---
# Protocol: directives/session-state-protocol.md

def save_session_state(
    active_task: str,
    decisions: Optional[List[Dict[str, str]]] = None,
    experts_deployed: Optional[List[Dict[str, str]]] = None,
    key_findings: Optional[List[str]] = None,
    files_modified: Optional[List[Dict[str, str]]] = None,
    current_phase: str = "",
    next_steps: Optional[List[str]] = None,
    intent: Optional[Dict[str, str]] = None,
) -> str:
    """
    Write a session state anchor to survive context compaction.

    Args:
        active_task: 1-2 sentence description of current work.
        decisions: List of {"decision": ..., "choice": ..., "rationale": ...}.
        experts_deployed: List of {"name": ..., "contribution": ...}.
        key_findings: List of 1-line finding strings.
        files_modified: List of {"path": ..., "description": ...}.
        current_phase: Where we are in the workflow.
        next_steps: List of next action strings.
        intent: Optional {"deliverable": ..., "audience": ..., "success_criteria": ...}.

    Returns:
        The path to the written state file.
    """
    os.makedirs(os.path.dirname(SESSION_STATE_PATH), exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# Session State Anchor",
        f"> Last updated: {timestamp}",
        "",
        "## Active Task",
        active_task,
        "",
    ]

    if intent:
        lines.extend([
            "## Intent (Validated)",
            f"- **Deliverable**: {intent.get('deliverable', 'TBD')}",
            f"- **Audience**: {intent.get('audience', 'TBD')}",
            f"- **Success criteria**: {intent.get('success_criteria', 'TBD')}",
            "",
        ])

    if decisions:
        lines.append("## Decisions Made")
        for d in decisions:
            lines.append(f"- **{d['decision']}**: {d['choice']} — {d.get('rationale', '')}")
        lines.append("")

    if experts_deployed:
        lines.append("## Experts Deployed")
        for e in experts_deployed:
            lines.append(f"- **{e['name']}**: {e['contribution']}")
        lines.append("")

    if key_findings:
        lines.append("## Key Findings (Compressed)")
        for f in key_findings:
            lines.append(f"- {f}")
        lines.append("")

    if files_modified:
        lines.append("## Files Created/Modified This Session")
        for fm in files_modified:
            lines.append(f"- `{fm['path']}`: {fm['description']}")
        lines.append("")

    if current_phase:
        lines.extend(["## Current Phase", current_phase, ""])

    if next_steps:
        lines.append("## Next Steps")
        for i, step in enumerate(next_steps, 1):
            lines.append(f"{i}. {step}")
        lines.append("")

    content = "\n".join(lines)
    with open(SESSION_STATE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return SESSION_STATE_PATH


def load_session_state() -> Optional[str]:
    """
    Read the session state anchor file.

    Returns:
        The contents of the state file as a string, or None if it doesn't exist.
    """
    if not os.path.exists(SESSION_STATE_PATH):
        return None

    try:
        with open(SESSION_STATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except IOError:
        return None


def clear_session_state() -> bool:
    """
    Remove the session state file (e.g., when a session completes cleanly).

    Returns:
        True if removed, False if it didn't exist or couldn't be removed.
    """
    if os.path.exists(SESSION_STATE_PATH):
        try:
            os.remove(SESSION_STATE_PATH)
            return True
        except OSError:
            pass
    return False
