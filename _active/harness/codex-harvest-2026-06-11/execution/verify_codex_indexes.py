#!/usr/bin/env python3
"""Verify generated Codex Antigravity semantic indexes."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GENERATOR = ROOT / "execution" / "generate_codex_indexes.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_codex_indexes", GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {GENERATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    generator = load_generator()
    ok, failures = generator.verify()
    if not ok:
        print("Codex semantic index verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Codex semantic index verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
