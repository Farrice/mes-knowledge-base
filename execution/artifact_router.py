#!/usr/bin/env python3
"""Global artifact organization router for Codex system roots.

The router keeps the physical workspace project-first while preserving a
domain-first retrieval layer. It owns inventory, classification, staged move
plans, safe move application, and enforcement for new artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from paths import BASE_PATH


ROOT = BASE_PATH
DOCUMENTS_CODEX = Path("/Users/farricecain/Documents/Codex")
ORG_DIR = ROOT / "_system" / "organization"
INBOX_DIR = ORG_DIR / "inbox"
MANIFEST_PATH = ORG_DIR / "manifest.json"
ROUTES_PATH = ORG_DIR / "routes.json"
ALIASES_PATH = ORG_DIR / "aliases.json"
ORG_INDEX_PATH = ORG_DIR / "ORG_INDEX.md"
MOVE_LEDGER_PATH = ORG_DIR / "move-ledger.jsonl"

DOMAIN_TAXONOMY = (
    "System",
    "Creative",
    "Extraction",
    "Revenue",
    "Client",
    "Research",
    "Content",
    "Ops",
    "Personal",
)

STANDARD_PROJECT_DIRS = (
    "00-start-here",
    "01-source",
    "02-research",
    "03-working-drafts",
    "04-deliverables",
    "05-assets",
    "06-system",
    "90-exports",
    "99-archive",
)

CONTROL_ROOTS = {
    ".agent",
    ".agents",
    "_system",
    "agents",
    "directives",
    "docs",
    "execution",
    "semantic_libraries",
    "skills",
}

INDEXED_SYSTEM_ROOTS = {
    "brain",
    "extractions",
    "knowledge",
}

MIGRATION_SOURCE_ROOTS = {
    "deliverables",
    "research_outputs",
    "strategy_briefs",
    "documents_codex",
}

SKIP_DIR_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".tmp",
    "tmp",
    "tempmediaStorage",
}

SKIP_FILE_NAMES = {".DS_Store"}

SIDE_METADATA_SUFFIXES = (".metadata.json",)

TEXT_REFERENCE_SUFFIXES = {
    ".md",
    ".py",
    ".json",
    ".toml",
    ".txt",
    ".yml",
    ".yaml",
}

ASSET_SUFFIXES = {
    ".apng",
    ".gif",
    ".jpeg",
    ".jpg",
    ".mov",
    ".mp3",
    ".mp4",
    ".png",
    ".svg",
    ".webp",
}

EXPORT_SUFFIXES = {".docx", ".html", ".htm", ".pdf"}

SOURCE_KEYWORDS = {
    "capture",
    "input",
    "intake",
    "raw",
    "source",
    "transcript",
    "upload",
}

RESEARCH_KEYWORDS = {
    "analysis",
    "benchmark",
    "competitor",
    "dossier",
    "evidence",
    "landscape",
    "ledger",
    "market",
    "qa_report",
    "research",
    "source_ledger",
    "trend",
    "validation",
}

DRAFT_KEYWORDS = {
    "draft",
    "post",
    "script",
    "variant",
    "working",
}

DELIVERABLE_KEYWORDS = {
    "asset",
    "audit",
    "brief",
    "blueprint",
    "dashboard",
    "deliverable",
    "handoff",
    "kit",
    "one-pager",
    "package",
    "pack",
    "playbook",
    "proposal",
    "roadmap",
    "scorecard",
    "template",
}

SYSTEM_KEYWORDS = {
    "automation",
    "guard",
    "index",
    "manifest",
    "operating",
    "router",
    "sop",
    "system",
    "tracker",
    "workflow",
}

DOMAIN_KEYWORDS = {
    "System": {
        "agent",
        "artifact",
        "automation",
        "bridge",
        "codex",
        "command",
        "guard",
        "harness",
        "index",
        "mission",
        "router",
        "system",
        "workflow",
    },
    "Creative": {
        "asset",
        "carousel",
        "creative",
        "design",
        "image",
        "mood",
        "portrait",
        "video",
        "visual",
    },
    "Extraction": {
        "book",
        "extract",
        "extraction",
        "framework",
        "skill",
        "source-to-skill",
        "transcript",
    },
    "Revenue": {
        "cash",
        "client",
        "monetization",
        "offer",
        "outreach",
        "pricing",
        "proposal",
        "revenue",
        "sales",
    },
    "Client": {
        "audit",
        "client",
        "delivery",
        "handoff",
        "implementation",
        "intake",
        "proposal",
    },
    "Research": {
        "analysis",
        "benchmark",
        "evidence",
        "landscape",
        "market",
        "research",
        "source",
        "trend",
    },
    "Content": {
        "brief",
        "calendar",
        "content",
        "hook",
        "linkedin",
        "newsletter",
        "post",
        "substack",
    },
    "Ops": {
        "health",
        "ledger",
        "ops",
        "pulse",
        "recurring",
        "report",
        "tracker",
    },
    "Personal": {
        "farrice",
        "ideation",
        "personal",
        "reflection",
        "voice",
        "worldview",
    },
}

PROJECT_ALIASES = {
    "cash-first-service-menu": ("cash-first", "cash-sprint", "first-10", "first-10k"),
    "chris-restaurants": ("chris-restaurants", "panda-inn", "wasabi", "yakiya"),
    "coach-cooz": ("acusio", "coach-cooz", "cooz"),
    "content-system-audit": (
        "ai-content-misfire",
        "ai-misfire",
        "content-misfire",
        "content-system-audit",
        "misfire",
        "slop-cleanup",
    ),
    "farrice-brand": ("farrice-brand", "farrice-voice", "marketing-voice"),
    "farrice-content-os": (
        "brandjack",
        "farrice-content",
        "farrice-content-os",
        "hook-lab",
        "hybrid-content",
        "hybrid-linkedin",
        "hybrid-morning",
        "hybrid-signal",
    ),
    "linkedin-launch": (
        "linkedin-ai-operating-partner",
        "linkedin-launch",
        "week-1-linkedin",
    ),
    "parallax-icp-offer": ("parallax", "parallax-icp"),
    "operator-cockpit-v2": (
        "operator-cockpit",
        "operator cockpit",
        "cockpit-v2",
        "v2-operating-cockpit",
        "intent-confidence-packet",
        "friction-cockpit",
    ),
    "research-intelligence-entry-point": (
        "deep-research",
        "research-intelligence",
        "research-swarm",
    ),
    "service-first-productization": (
        "service-first",
        "productization",
        "productized-service",
    ),
    "strategic-clarity": ("strategic-clarity",),
    "system-audit": ("system-audit", "system-efficiency", "system-cohesion"),
    "vibe-tax-brief-deployment-os": ("vibe-tax",),
}

PROJECT_PRIMARY_DOMAINS = {
    "cash-first-service-menu": "Revenue",
    "chris-restaurants": "Client",
    "coach-cooz": "Client",
    "content-system-audit": "Revenue",
    "farrice-brand": "Personal",
    "farrice-content-os": "Content",
    "josh-dancewear-brand": "Client",
    "josh-swing-nerd-shirts-v1": "Client",
    "linkedin-launch": "Content",
    "operator-cockpit-v2": "System",
    "parallax-icp-offer": "Content",
    "research-intelligence-entry-point": "Research",
    "service-first-productization": "Revenue",
    "strategic-clarity": "Ops",
    "system-audit": "System",
    "vibe-tax-brief-deployment-os": "Client",
}


@dataclass(frozen=True)
class Classification:
    path: str
    root: str
    relative_path: str
    exists: bool
    size: int
    modified_at: str
    domain: str
    secondary_domains: list[str]
    project: str | None
    artifact_type: str
    lifecycle: str
    destination: str | None
    confidence: float
    status: str
    reasons: list[str]

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "root": self.root,
            "relative_path": self.relative_path,
            "exists": self.exists,
            "size": self.size,
            "modified_at": self.modified_at,
            "domain": self.domain,
            "secondary_domains": self.secondary_domains,
            "project": self.project,
            "artifact_type": self.artifact_type,
            "lifecycle": self.lifecycle,
            "destination": self.destination,
            "confidence": self.confidence,
            "status": self.status,
            "reasons": self.reasons,
        }


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def read_json(path: Path, fallback: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fallback


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def safe_relative(path: Path, base: Path) -> str | None:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return None


def active_projects() -> list[str]:
    active_dir = ROOT / "_active"
    if not active_dir.exists():
        return []
    return sorted(p.name for p in active_dir.iterdir() if p.is_dir() and not p.name.startswith("."))


def ensure_org_home() -> None:
    ORG_DIR.mkdir(parents=True, exist_ok=True)
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    MOVE_LEDGER_PATH.touch(exist_ok=True)

    aliases = read_json(ALIASES_PATH, None)
    if aliases is None:
        write_json(ALIASES_PATH, {"version": 1, "updated_at": utc_now(), "aliases": {}})

    routes = {
        "version": 1,
        "updated_at": utc_now(),
        "owned_roots": [str(ROOT), str(DOCUMENTS_CODEX)],
        "domain_taxonomy": list(DOMAIN_TAXONOMY),
        "active_project_shape": list(STANDARD_PROJECT_DIRS),
        "canonical_project_root": str(ROOT / "_active" / "<project-slug>"),
        "lifecycle_destinations": {
            "source": "01-source",
            "research": "02-research",
            "draft": "03-working-drafts",
            "deliverable": "04-deliverables",
            "asset": "05-assets",
            "system": "06-system",
            "export": "90-exports",
            "archive": "99-archive",
        },
        "indexed_not_bulk_moved": sorted(CONTROL_ROOTS | INDEXED_SYSTEM_ROOTS),
        "migration_source_roots": sorted(MIGRATION_SOURCE_ROOTS),
        "ambiguous_policy": "Report to inbox; do not move automatically.",
    }
    write_json(ROUTES_PATH, routes)


def ensure_project_shapes() -> list[str]:
    created: list[str] = []
    for project in active_projects():
        project_dir = ROOT / "_active" / project
        for child in STANDARD_PROJECT_DIRS:
            path = project_dir / child
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                created.append(str(path))
        index_path = project_dir / "INDEX.md"
        if not index_path.exists():
            index_path.write_text(
                f"# {project.replace('-', ' ').title()}\n\n"
                "## Purpose\n"
                "Canonical project home managed by the global artifact router.\n\n"
                "## Router\n"
                "Use `python3 execution/artifact_router.py classify <path>` to place new artifacts.\n",
                encoding="utf-8",
            )
            created.append(str(index_path))
    return created


def iter_scan_roots() -> list[Path]:
    roots = [
        ROOT / "_active",
        ROOT / "_exports",
        ROOT / "brain",
        ROOT / "deliverables",
        ROOT / "docs",
        ROOT / "extractions",
        ROOT / "knowledge",
        ROOT / "projects",
        ROOT / "research_outputs",
        ROOT / "strategy_briefs",
        ROOT / "execution",
        ROOT / ".agent",
        ROOT / ".agents",
        ROOT / "agents",
        ROOT / "directives",
        ROOT / "semantic_libraries",
        ROOT / "skills",
        ROOT / "_system",
        DOCUMENTS_CODEX,
    ]
    return [path for path in roots if path.exists()]


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIR_NAMES:
        return True
    if path.name in SKIP_FILE_NAMES:
        return True
    return False


def iter_files(paths: Iterable[Path]) -> Iterable[Path]:
    for root in paths:
        if root.is_file():
            if not should_skip(root):
                yield root
            continue
        for path in root.rglob("*"):
            if should_skip(path):
                continue
            if path.is_symlink():
                resolved = path.resolve(strict=False)
                if safe_relative(resolved, ROOT) is None and safe_relative(resolved, DOCUMENTS_CODEX) is None:
                    continue
            if path.is_file():
                yield path


def root_name(path: Path) -> tuple[str, str]:
    rel = safe_relative(path, ROOT)
    if rel is not None:
        top = rel.split("/", 1)[0]
        return top, rel
    rel_docs = safe_relative(path, DOCUMENTS_CODEX)
    if rel_docs is not None:
        return "documents_codex", rel_docs
    return "external", str(path)


def tokens_for(path: Path) -> set[str]:
    rel = str(path).lower()
    return set(re.findall(r"[a-z0-9][a-z0-9-]*", rel.replace("_", "-")))


def text_for_matching(path: Path) -> str:
    _, rel = root_name(path)
    normalized = rel.lower().replace("_", "-")
    return " ".join(re.findall(r"[a-z0-9][a-z0-9-]*", normalized)) + " " + normalized


def infer_project(path: Path, top: str, rel: str) -> tuple[str | None, float, list[str]]:
    reasons: list[str] = []
    parts = rel.split("/")
    if top == "_active" and len(parts) >= 2:
        return parts[1], 0.98, ["already under active project"]
    if top == "projects" and len(parts) >= 2:
        return slugify(parts[1]), 0.78, ["under projects workspace"]
    if top == "_exports" and len(parts) >= 2:
        return slugify(parts[1]), 0.74, ["under exports workspace"]

    haystack = text_for_matching(path)
    best_project: str | None = None
    best_score = 0

    candidate_projects = set(active_projects()) | set(PROJECT_ALIASES) | set(PROJECT_PRIMARY_DOMAINS)
    for project in sorted(candidate_projects):
        aliases = set(PROJECT_ALIASES.get(project, ()))
        aliases.add(project)
        aliases.add(project.replace("-", " "))
        score = 0
        for alias in aliases:
            normalized = alias.lower().replace("_", "-")
            if normalized in haystack:
                score += 3 + normalized.count("-")
        if score > best_score:
            best_project = project
            best_score = score

    if best_project and best_score >= 3:
        reasons.append(f"matched active project signal: {best_project}")
        return best_project, min(0.9, 0.72 + best_score / 20), reasons

    if top == "deliverables" and len(parts) >= 3:
        project = slugify(parts[1])
        return project, 0.62, ["derived project from deliverables subfolder"]

    if top == "documents_codex" and len(parts) >= 2:
        date_or_session = parts[0]
        session = parts[1] if re.match(r"\d{4}-\d{2}-\d{2}", date_or_session) else parts[0]
        return slugify(session), 0.55, ["derived project from Documents/Codex session folder"]

    return None, 0.35, ["no strong project owner found"]


def infer_lifecycle(path: Path) -> tuple[str, str, list[str]]:
    lower = text_for_matching(path)
    suffix = path.suffix.lower()
    reasons: list[str] = []

    if any(part.lower() in {"archive", "_archive", "archived", "deprecated", "_deprecated"} for part in path.parts):
        return "archive", "archive", ["path is archived or deprecated"]
    if path.name.endswith(".metadata.json"):
        return "metadata", "metadata", ["sidecar metadata"]
    if ".resolved" in path.name:
        return "generated", "generated", ["resolved/generated file"]
    if suffix in EXPORT_SUFFIXES:
        return "export", "export", ["export-format suffix"]
    if suffix in ASSET_SUFFIXES:
        return "asset", "asset", ["media/asset suffix"]

    keyword_groups = [
        ("source", SOURCE_KEYWORDS, "source/input keyword"),
        ("research", RESEARCH_KEYWORDS, "research/evidence keyword"),
        ("draft", DRAFT_KEYWORDS, "draft/content keyword"),
        ("system", SYSTEM_KEYWORDS, "system/workflow keyword"),
        ("deliverable", DELIVERABLE_KEYWORDS, "deliverable keyword"),
    ]
    for lifecycle, keywords, reason in keyword_groups:
        if any(keyword in lower for keyword in keywords):
            reasons.append(reason)
            return lifecycle, lifecycle, reasons

    if suffix in {".csv", ".json", ".jsonl", ".tsv"}:
        return "source", "source", ["structured data defaults to source"]
    if suffix == ".md":
        return "deliverable", "deliverable", ["markdown defaults to deliverable when project is known"]

    return "unknown", "unknown", ["no lifecycle signal found"]


def infer_domain(path: Path, lifecycle: str, project: str | None = None) -> tuple[str, list[str]]:
    lower = text_for_matching(path)
    scored: list[tuple[int, str]] = []
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in lower)
        if score:
            scored.append((score, domain))

    project_domain = PROJECT_PRIMARY_DOMAINS.get(project or "")

    if not scored:
        fallback = project_domain or {
            "asset": "Creative",
            "deliverable": "Client",
            "draft": "Content",
            "export": "Client",
            "research": "Research",
            "source": "Research",
            "system": "System",
        }.get(lifecycle, "System")
        return fallback, []

    scored.sort(key=lambda item: (-item[0], DOMAIN_TAXONOMY.index(item[1]) if item[1] in DOMAIN_TAXONOMY else 99))
    primary = project_domain or scored[0][1]
    secondary = [domain for _, domain in scored if domain != primary][:3]
    return primary, secondary


def destination_for(project: str | None, lifecycle: str, path: Path) -> Path | None:
    if project is None:
        return None
    folder = {
        "archive": "99-archive",
        "asset": "05-assets",
        "deliverable": "04-deliverables",
        "draft": "03-working-drafts",
        "export": "90-exports",
        "research": "02-research",
        "source": "01-source",
        "system": "06-system",
    }.get(lifecycle)
    if folder is None:
        return None
    return ROOT / "_active" / project / folder / path.name


def classify_path(raw_path: str | Path) -> Classification:
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    else:
        path = path.resolve(strict=False)

    exists = path.exists()
    size = path.stat().st_size if exists and path.is_file() else 0
    modified_at = (
        datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).replace(microsecond=0).isoformat()
        if exists
        else ""
    )
    top, rel = root_name(path)
    reasons: list[str] = []

    lifecycle, artifact_type, lifecycle_reasons = infer_lifecycle(path)
    reasons.extend(lifecycle_reasons)
    project, project_confidence, project_reasons = infer_project(path, top, rel)
    reasons.extend(project_reasons)
    domain, secondary_domains = infer_domain(path, lifecycle, project)

    destination = destination_for(project, lifecycle, path)
    destination_str = str(destination) if destination else None

    confidence = project_confidence
    if lifecycle != "unknown":
        confidence += 0.08
    if top in CONTROL_ROOTS:
        confidence = 0.95
    if top in INDEXED_SYSTEM_ROOTS:
        confidence = max(confidence, 0.82)
    if top == "_active" and any(f"/{folder}/" in f"/{rel}/" for folder in STANDARD_PROJECT_DIRS):
        confidence = 0.98
    confidence = min(round(confidence, 2), 0.99)

    status = "ambiguous"
    if top in CONTROL_ROOTS:
        status = "indexed_control_plane"
        destination_str = None
        reasons.append("control-plane file is indexed, not moved")
    elif top in INDEXED_SYSTEM_ROOTS:
        status = "indexed_system_library"
        destination_str = None
        reasons.append("system library is indexed, not bulk-moved")
    elif top == "_active":
        if any(f"/{folder}/" in f"/{rel}/" for folder in STANDARD_PROJECT_DIRS):
            status = "canonical"
            reasons.append("already in canonical project shape")
        else:
            status = "project_home_needs_standardization"
            reasons.append("active project file is governed but not automatically moved")
    elif destination is None:
        status = "ambiguous"
    elif path == destination:
        status = "canonical"
    elif top in MIGRATION_SOURCE_ROOTS and confidence >= 0.85:
        status = "migration_candidate"
    else:
        status = "needs_review"

    return Classification(
        path=str(path),
        root=top,
        relative_path=rel,
        exists=exists,
        size=size,
        modified_at=modified_at,
        domain=domain,
        secondary_domains=secondary_domains,
        project=project,
        artifact_type=artifact_type,
        lifecycle=lifecycle,
        destination=destination_str,
        confidence=confidence,
        status=status,
        reasons=reasons,
    )


def build_manifest() -> dict[str, Any]:
    ensure_org_home()
    created = ensure_project_shapes()
    entries = [classify_path(path).as_dict() for path in iter_files(iter_scan_roots())]

    counts: dict[str, dict[str, int]] = {"by_root": {}, "by_domain": {}, "by_status": {}}
    for entry in entries:
        for bucket, key in (
            ("by_root", entry["root"]),
            ("by_domain", entry["domain"]),
            ("by_status", entry["status"]),
        ):
            counts[bucket][key] = counts[bucket].get(key, 0) + 1
    for root in sorted(CONTROL_ROOTS | INDEXED_SYSTEM_ROOTS | MIGRATION_SOURCE_ROOTS | {"_active", "_system", "projects"}):
        counts["by_root"].setdefault(root, 0)

    manifest = {
        "version": 1,
        "generated_at": utc_now(),
        "owned_roots": [str(ROOT), str(DOCUMENTS_CODEX)],
        "total_files": len(entries),
        "counts": counts,
        "project_shape_created": created,
        "entries": entries,
    }
    write_json(MANIFEST_PATH, manifest)
    write_org_index(manifest)
    return manifest


def write_org_index(manifest: dict[str, Any]) -> None:
    lines = [
        "# Global Artifact Organization",
        "",
        f"Last updated: {manifest['generated_at']}",
        f"Total indexed files: {manifest['total_files']}",
        "",
        "## Canonical Project Shape",
        "",
        "Active projects live under `_active/<project-slug>/` with:",
        "",
    ]
    for folder in STANDARD_PROJECT_DIRS:
        lines.append(f"- `{folder}/`")

    lines.extend(["", "## Counts By Root", ""])
    for root, count in sorted(manifest["counts"]["by_root"].items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{root}`: {count}")

    lines.extend(["", "## Counts By Domain", ""])
    for domain in DOMAIN_TAXONOMY:
        count = manifest["counts"]["by_domain"].get(domain, 0)
        lines.append(f"- `{domain}`: {count}")

    lines.extend(
        [
            "",
            "## Router Commands",
            "",
            "- `python3 execution/artifact_router.py inventory`",
            "- `python3 execution/artifact_router.py classify <path>`",
            "- `python3 execution/artifact_router.py plan`",
            "- `python3 execution/artifact_router.py apply --plan <plan.json>`",
            "- `python3 execution/artifact_router.py enforce <path...>`",
            "",
            "## Policy",
            "",
            "Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.",
        ]
    )
    ORG_INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def sidecar_paths(path: Path) -> list[Path]:
    return [
        path.with_name(path.name + ".metadata.json"),
        path.with_suffix(path.suffix + ".metadata.json"),
        path.with_suffix(".metadata.json"),
    ]


def has_sidecar_metadata(path: Path) -> bool:
    return any(candidate.exists() for candidate in sidecar_paths(path))


def reference_corpus() -> str:
    roots = [
        ROOT / "CODEX.md",
        ROOT / "AGENTS.md",
        ROOT / ".agent" / "workflows",
        ROOT / ".agents" / "skills",
        ROOT / "execution",
        ROOT / "docs",
        ROOT / "semantic_libraries",
    ]
    chunks: list[str] = []
    for path in iter_files(roots):
        if path.suffix.lower() not in TEXT_REFERENCE_SUFFIXES:
            continue
        try:
            chunks.append(path.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
    return "\n".join(chunks)


def is_referenced(entry: dict[str, Any], corpus: str) -> bool:
    path = Path(entry["path"])
    rel = safe_relative(path, ROOT)
    checks = [entry["path"]]
    if rel:
        checks.append(rel)
    return any(check in corpus for check in checks)


def plan_moves(output: str | None = None) -> dict[str, Any]:
    manifest = build_manifest()
    corpus = reference_corpus()
    plan: dict[str, Any] = {
        "version": 1,
        "generated_at": utc_now(),
        "safe": [],
        "ambiguous": [],
        "blocked": [],
        "skipped": [],
    }

    for entry in manifest["entries"]:
        path = Path(entry["path"])
        destination = Path(entry["destination"]) if entry.get("destination") else None
        if not path.exists() or not path.is_file():
            continue
        if path.name.endswith(SIDE_METADATA_SUFFIXES) or ".resolved" in path.name:
            plan["skipped"].append({**entry, "skip_reason": "metadata or generated companion"})
            continue
        if entry["root"] not in MIGRATION_SOURCE_ROOTS:
            plan["skipped"].append({**entry, "skip_reason": "indexed/governed root, not backlog migration source"})
            continue
        if entry["status"] != "migration_candidate" or destination is None:
            plan["ambiguous"].append({**entry, "review_reason": "low confidence or missing destination"})
            continue
        if destination.exists():
            plan["blocked"].append({**entry, "block_reason": "destination exists", "destination": str(destination)})
            continue
        if is_referenced(entry, corpus):
            plan["blocked"].append({**entry, "block_reason": "old path referenced by active system files"})
            continue
        plan["safe"].append(
            {
                **entry,
                "destination": str(destination),
                "move_reason": "high-confidence backlog artifact with active project owner",
            }
        )

    plan_path = Path(output) if output else INBOX_DIR / f"move-plan-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    write_json(plan_path, plan)
    plan["plan_path"] = str(plan_path)
    return plan


def write_backlog_map(output: str | None = None) -> dict[str, Any]:
    """Write a readable dated backlog map plus the underlying staged move plan."""
    manifest = build_manifest()
    plan = plan_moves()
    backlog_dir = ORG_DIR / "backlog-maps"
    backlog_dir.mkdir(parents=True, exist_ok=True)
    map_path = Path(output) if output else backlog_dir / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-backlog-map.md"

    status_counts = manifest.get("counts", {}).get("by_status", {})
    root_counts = manifest.get("counts", {}).get("by_root", {})
    domain_counts = manifest.get("counts", {}).get("by_domain", {})

    lines = [
        "# Artifact Backlog Map",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Summary",
        "",
        f"- Total indexed files: {manifest.get('total_files', 0)}",
        f"- Safe staged moves: {len(plan.get('safe', []))}",
        f"- Ambiguous review items: {len(plan.get('ambiguous', []))}",
        f"- Blocked items: {len(plan.get('blocked', []))}",
        f"- Skipped/indexed items: {len(plan.get('skipped', []))}",
        f"- Underlying move plan: `{plan.get('plan_path', '')}`",
        "",
        "## Counts By Status",
        "",
    ]
    for status, count in sorted(status_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{status}`: {count}")

    lines.extend(["", "## Counts By Root", ""])
    for root, count in sorted(root_counts.items(), key=lambda item: (-item[1], item[0]))[:20]:
        lines.append(f"- `{root}`: {count}")

    lines.extend(["", "## Counts By Domain", ""])
    for domain in DOMAIN_TAXONOMY:
        lines.append(f"- `{domain}`: {domain_counts.get(domain, 0)}")

    lines.extend(
        [
            "",
            "## Review Policy",
            "",
            "No files are moved by this map. Safe moves still require a reviewed `apply --plan` run. Ambiguous, blocked, referenced, or low-confidence items stay in place until reviewed.",
            "",
            "## Next Review Buckets",
            "",
        ]
    )
    for bucket in ("safe", "ambiguous", "blocked"):
        lines.append(f"### {bucket.title()}")
        for item in plan.get(bucket, [])[:25]:
            destination = item.get("destination") or item.get("review_reason") or item.get("block_reason") or ""
            rel = safe_relative(Path(item.get("path", "")), ROOT) or item.get("path", "")
            lines.append(f"- `{rel}` -> {destination}")
        if len(plan.get(bucket, [])) > 25:
            lines.append(f"- ... {len(plan.get(bucket, [])) - 25} more in plan JSON")
        lines.append("")

    map_path.parent.mkdir(parents=True, exist_ok=True)
    map_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {
        "map_path": str(map_path),
        "plan_path": plan.get("plan_path", ""),
        "safe": len(plan.get("safe", [])),
        "ambiguous": len(plan.get("ambiguous", [])),
        "blocked": len(plan.get("blocked", [])),
        "skipped": len(plan.get("skipped", [])),
    }


def load_aliases() -> dict[str, Any]:
    aliases = read_json(ALIASES_PATH, {"version": 1, "updated_at": utc_now(), "aliases": {}})
    aliases.setdefault("version", 1)
    aliases.setdefault("aliases", {})
    return aliases


def append_move_ledger(record: dict[str, Any]) -> None:
    MOVE_LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MOVE_LEDGER_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def move_companions(source: Path, destination: Path, moved: list[dict[str, str]]) -> None:
    for sidecar in sidecar_paths(source):
        if not sidecar.exists():
            continue
        if sidecar.name == source.name + ".metadata.json":
            sidecar_dest = destination.with_name(destination.name + ".metadata.json")
        elif sidecar.suffix == ".json":
            sidecar_dest = destination.with_suffix(destination.suffix + ".metadata.json")
        else:
            sidecar_dest = destination.with_suffix(".metadata.json")
        if sidecar_dest.exists():
            continue
        sidecar_dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(sidecar), str(sidecar_dest))
        moved.append({"from": str(sidecar), "to": str(sidecar_dest)})


def ensure_written_sidecar(destination: Path, item: dict[str, Any], generated: list[dict[str, str]]) -> None:
    """Create minimal sidecar metadata for moved written artifacts when absent."""
    if destination.suffix.lower() != ".md" or has_sidecar_metadata(destination):
        return
    rel = safe_relative(destination, ROOT) or ""
    if not any(f"/{folder}/" in f"/{rel}/" for folder in ("02-research", "03-working-drafts", "04-deliverables")):
        return
    sidecar = destination.with_name(destination.name + ".metadata.json")
    data = {
        "userFacingSurface": "rendered-conversation-document",
        "sourceRole": "persistence-copy",
        "externalExportRequested": False,
        "organizationGenerated": True,
        "generatedBy": "execution/artifact_router.py",
        "generatedAt": utc_now(),
        "domain": item.get("domain"),
        "project": item.get("project"),
        "lifecycle": item.get("lifecycle"),
        "sourcePath": item.get("path"),
    }
    write_json(sidecar, data)
    generated.append({"from": "generated", "to": str(sidecar)})


def apply_plan(plan_path: str) -> dict[str, Any]:
    ensure_org_home()
    plan = read_json(Path(plan_path), None)
    if not isinstance(plan, dict):
        raise SystemExit(f"Could not read plan: {plan_path}")

    aliases = load_aliases()
    result = {"moved": [], "skipped": [], "failed": []}
    for item in plan.get("safe", []):
        source = Path(item["path"])
        destination = Path(item["destination"])
        if not source.exists():
            result["skipped"].append({**item, "skip_reason": "source missing"})
            continue
        if destination.exists():
            result["skipped"].append({**item, "skip_reason": "destination exists"})
            continue
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            moved_record = {"from": str(source), "to": str(destination)}
            companions: list[dict[str, str]] = []
            move_companions(source, destination, companions)
            ensure_written_sidecar(destination, item, companions)
            result["moved"].append({**moved_record, "companions": companions})
            aliases["aliases"][str(source)] = {
                "current": str(destination),
                "moved_at": utc_now(),
                "domain": item.get("domain"),
                "project": item.get("project"),
                "lifecycle": item.get("lifecycle"),
            }
            append_move_ledger(
                {
                    "action": "move",
                    "moved_at": utc_now(),
                    "from": str(source),
                    "to": str(destination),
                    "companions": companions,
                    "plan": str(Path(plan_path).resolve()),
                }
            )
        except Exception as exc:  # pragma: no cover - defensive filesystem handling
            result["failed"].append({**item, "error": str(exc)})

    aliases["updated_at"] = utc_now()
    write_json(ALIASES_PATH, aliases)
    build_manifest()
    return result


def enforce(paths: list[str]) -> dict[str, Any]:
    ensure_org_home()
    results: list[dict[str, Any]] = []
    for raw_path in paths:
        classification = classify_path(raw_path).as_dict()
        path = Path(classification["path"])
        failures: list[str] = []
        warnings: list[str] = []

        if classification["root"] == "external":
            failures.append("path is outside approved Codex system roots")
        elif classification["status"] in {"ambiguous", "needs_review", "migration_candidate"}:
            failures.append("path is not in its canonical artifact route")

        canonical_rel = classification.get("relative_path", "")
        is_written_project_source = any(
            f"/{folder}/" in f"/{canonical_rel}/"
            for folder in ("02-research", "03-working-drafts", "04-deliverables")
        )
        if (
            path.suffix.lower() == ".md"
            and is_written_project_source
            and path.name not in {"INDEX.md", "README.md"}
            and not has_sidecar_metadata(path)
        ):
            failures.append("written artifact is missing sidecar metadata")

        if path.suffix.lower() == ".md":
            try:
                from artifact_frontmatter_guard import scan_paths as scan_markdown_readability

                readability_issues = scan_markdown_readability([path])
            except Exception as exc:
                readability_issues = [
                    {
                        "reason": f"Markdown readability guard could not run: {exc}",
                    }
                ]
            if readability_issues:
                failures.append("Markdown source has visible metadata header")

        if classification.get("destination"):
            warnings.append(f"proposed destination: {classification['destination']}")

        results.append({**classification, "failures": failures, "warnings": warnings})

    return {
        "status": "fail" if any(item["failures"] for item in results) else "pass",
        "checked": len(results),
        "results": results,
    }


def print_summary(label: str, payload: dict[str, Any]) -> None:
    print(f"{label}:")
    for key, value in payload.items():
        if key == "entries":
            continue
        if isinstance(value, (str, int)):
            print(f"  {key}: {value}")
    if "counts" in payload:
        print("  counts:")
        for group, counts in payload["counts"].items():
            compact = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
            print(f"    {group}: {compact}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Route, inventory, and enforce Codex artifact organization.")
    sub = parser.add_subparsers(dest="command", required=True)

    inventory_p = sub.add_parser("inventory", help="Scan approved roots and build the global manifest.")
    inventory_p.add_argument("--json", action="store_true")

    classify_p = sub.add_parser("classify", help="Classify one path.")
    classify_p.add_argument("path")
    classify_p.add_argument("--json", action="store_true")

    plan_p = sub.add_parser("plan", help="Generate a staged move plan.")
    plan_p.add_argument("--output", help="Write plan to a specific path.")
    plan_p.add_argument("--json", action="store_true")

    backlog_p = sub.add_parser("backlog-map", help="Generate a dated readable backlog map and staged cleanup plan.")
    backlog_p.add_argument("--output", help="Write the readable backlog map to a specific path.")
    backlog_p.add_argument("--json", action="store_true")

    apply_p = sub.add_parser("apply", help="Apply safe moves from a staged move plan.")
    apply_p.add_argument("--plan", required=True, help="Plan JSON created by the plan command.")
    apply_p.add_argument("--json", action="store_true")

    enforce_p = sub.add_parser("enforce", help="Validate that paths follow the organization rules.")
    enforce_p.add_argument("paths", nargs="+")
    enforce_p.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.command == "inventory":
        manifest = build_manifest()
        if args.json:
            print(json.dumps(manifest, indent=2))
        else:
            print_summary("Inventory complete", manifest)
            print(f"  manifest: {MANIFEST_PATH}")
            print(f"  index: {ORG_INDEX_PATH}")
        return 0

    if args.command == "classify":
        classification = classify_path(args.path).as_dict()
        if args.json:
            print(json.dumps(classification, indent=2))
        else:
            print(json.dumps(classification, indent=2))
        return 0

    if args.command == "plan":
        plan = plan_moves(args.output)
        if args.json:
            print(json.dumps(plan, indent=2))
        else:
            print(f"Plan written: {plan['plan_path']}")
            print(f"  safe: {len(plan['safe'])}")
            print(f"  ambiguous: {len(plan['ambiguous'])}")
            print(f"  blocked: {len(plan['blocked'])}")
            print(f"  skipped: {len(plan['skipped'])}")
        return 0

    if args.command == "backlog-map":
        result = write_backlog_map(args.output)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Backlog map written: {result['map_path']}")
            print(f"  plan: {result['plan_path']}")
            print(f"  safe: {result['safe']}")
            print(f"  ambiguous: {result['ambiguous']}")
            print(f"  blocked: {result['blocked']}")
            print(f"  skipped: {result['skipped']}")
        return 0

    if args.command == "apply":
        result = apply_plan(args.plan)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Moved: {len(result['moved'])}")
            print(f"Skipped: {len(result['skipped'])}")
            print(f"Failed: {len(result['failed'])}")
            for item in result["moved"][:25]:
                print(f"- {item['from']} -> {item['to']}")
            if len(result["moved"]) > 25:
                print(f"... {len(result['moved']) - 25} more")
        return 1 if result["failed"] else 0

    if args.command == "enforce":
        result = enforce(args.paths)
        if args.json:
            print(json.dumps(result, indent=2))
        elif result["status"] == "pass":
            print("Artifact route enforcement passed.")
        else:
            print("Artifact route enforcement failed:")
            for item in result["results"]:
                if not item["failures"]:
                    continue
                print(f"- {item['path']}")
                for failure in item["failures"]:
                    print(f"  {failure}")
                for warning in item["warnings"]:
                    print(f"  {warning}")
        return 0 if result["status"] == "pass" else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
