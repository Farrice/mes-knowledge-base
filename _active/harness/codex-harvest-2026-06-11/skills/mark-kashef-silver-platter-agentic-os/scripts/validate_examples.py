"""Validate included silver-platter example data maps."""

from __future__ import annotations

import json
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = SKILL_DIR / "examples"

REQUIRED_TOP_LEVEL = ["business", "pantry", "prep", "plate", "opportunities"]
RECIPE_REQUIRED = [
    "id",
    "name",
    "headline",
    "goal",
    "ingredients",
    "claude_code_stack",
    "walkthrough",
    "before_claude_code",
    "after_claude_code",
]
REGULATED = {"healthcare_clinic", "professional_services", "wealth_advisory"}


def fail(message: str) -> str:
    return f"[fail] {message}"


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    rel = path.relative_to(SKILL_DIR)

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(fail(f"{rel}: missing top-level key {key}"))

    business = data.get("business", {})
    archetype = business.get("archetype")
    setup = data.get("setup_priority", [])

    if archetype in REGULATED:
        first = " ".join(str(setup[0].get(field, "")) for field in ["title", "title_friendly", "what_to_do"]) if setup else ""
        if "bedrock" not in first.lower() and "model" not in first.lower():
            errors.append(fail(f"{rel}: regulated archetype must put Bedrock/model containment first"))
        joined = json.dumps(data).lower()
        if not any(token in joined for token in ["phi", "walling", "scoping", "path-scoped", "cross-domain"]):
            errors.append(fail(f"{rel}: regulated archetype lacks data-scoping language"))

    for index, recipe in enumerate(data.get("recipes", []), start=1):
        for key in RECIPE_REQUIRED:
            if key not in recipe:
                errors.append(fail(f"{rel}: recipe {index} missing {key}"))

    for prep in data.get("prep", []):
        if not prep.get("sample_content"):
            errors.append(fail(f"{rel}: prep item {prep.get('id')} missing sample_content"))
        if "reads_from" not in prep:
            sources = prep.get("sources")
            if sources is None:
                errors.append(fail(f"{rel}: prep item {prep.get('id')} missing sources/reads_from"))

    for plate in data.get("plate", []):
        if not plate.get("sample_output"):
            errors.append(fail(f"{rel}: plate item {plate.get('id')} missing sample_output"))
        if not plate.get("approval_gate"):
            errors.append(fail(f"{rel}: plate item {plate.get('id')} missing approval_gate"))

    return errors


def main() -> int:
    paths = sorted(EXAMPLES_DIR.glob("*/data_map.json"))
    if not paths:
        print("[fail] no example data_map.json files found")
        return 1

    errors: list[str] = []
    for path in paths:
        errors.extend(validate(path))

    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"[ok] validated {len(paths)} example data maps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

