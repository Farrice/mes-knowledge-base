#!/usr/bin/env python3
"""Known-good fixture — the code floor predicate must accept this file."""


def greet(name: str) -> str:
    return f"hello, {name}"


def main() -> int:
    print(greet("floor"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
