#!/usr/bin/env python3
"""Keep one native Google Doc per living local source.

This is intentionally small: one ignored registry maps a local source and title
to its Google Doc ID. Exporters update that Doc on later runs and let Drive keep
the revision history. A separate Doc is an explicit milestone decision.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".agent" / "health" / "google-doc-living-registry.json"


def content_hash(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n"
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _key(source: str | Path, folder_id: str | None, title: str) -> str:
    identity = [str(Path(source).expanduser().resolve()), folder_id or "root", title]
    return hashlib.sha256(json.dumps(identity, ensure_ascii=False).encode("utf-8")).hexdigest()


def _load(path: Path = REGISTRY) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data.get("exports"), dict):
            return data
    except (OSError, json.JSONDecodeError, AttributeError):
        pass
    return {"schema_version": "google-doc-living-registry/v1", "exports": {}}


def lookup(source: str | Path, folder_id: str | None, title: str,
           path: Path = REGISTRY) -> dict[str, Any] | None:
    return _load(path)["exports"].get(_key(source, folder_id, title))


def record(source: str | Path, folder_id: str | None, title: str, doc_id: str,
           source_hash: str, link: str | None = None, path: Path = REGISTRY) -> dict[str, Any]:
    data = _load(path)
    row = {
        "source": str(Path(source).expanduser().resolve()),
        "folder_id": folder_id,
        "title": title,
        "doc_id": doc_id,
        "source_hash": source_hash,
        "link": link or f"https://docs.google.com/document/d/{doc_id}/edit",
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    data["exports"][_key(source, folder_id, title)] = row
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                     prefix=f".{path.name}.", delete=False) as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        temp_path = Path(handle.name)
    os.replace(temp_path, path)
    return row
