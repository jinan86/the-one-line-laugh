#!/usr/bin/env python3
"""The One-Line Laugh — make.fun bounty entry.

Writes exactly one funny sentence to /output/entry.txt.

The line: folded laundry piled on "the chair" — the universal
dresser-chair that every home has — quietly promoted from a
temporary stack to a permanent, rent-free roommate.

Pure Python 3.13 standard library. Deterministic: no network,
no clock, no randomness. The same bytes are produced on every run.
"""

import os
from pathlib import Path

ENTRY = (
    "I folded my laundry, put it on the chair, and now it lives there "
    "rent-free like a tiny roommate who never does the dishes."
)

MAX_CHARS = 200


def build_entry() -> str:
    """Return the single funny line for this entry."""
    return ENTRY


def validate_entry(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def entry_stats(text: str) -> dict:
    """Return character and byte counts for the entry text."""
    encoded = text.encode("utf-8")
    return {"characters": len(text), "bytes": len(encoded)}


def main() -> None:
    """Write the validated entry to /output/entry.txt."""
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = build_entry()
    validate_entry(text)
    target = output_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    stats = entry_stats(text)
    print(
        f"Wrote {stats['characters']} characters "
        f"({stats['bytes']} bytes) to {target}"
    )


if __name__ == "__main__":
    main()
