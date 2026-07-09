#!/usr/bin/env python3
"""Small dummy app for preonboarding exercises."""

from __future__ import annotations

import argparse
import sys


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Dummy preonboarding CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="Print a greeting")
    greet_parser.add_argument("name", help="Name to greet")

    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First number")
    add_parser.add_argument("b", type=float, help="Second number")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "greet":
        print(greet(args.name))
        return 0

    if args.command == "add":
        print(add(args.a, args.b))
        return 0

    parser.error(f"unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
