#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

The fortune is assembled from its two clauses so the prediction's
cadence stays readable in the source, then checked against the
competition gate (one line, 1-120 characters, UTF-8) before writing.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 120

# Clause 1: the plant's own future this week.
OPENING = "This week your leaves will find the sun, and your keeper will "
# Clause 2: the gentle joke — the keeper never learned its name.
CLOSING = "finally learn your name \u2014 it is not 'the green one'."

ENTRY = OPENING + CLOSING


def validate(text: str) -> str:
    """Enforce the gate: a single non-empty line within the limit."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if not 1 <= len(stripped) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(stripped)}")
    text.encode("utf-8")  # raises if not encodable as UTF-8
    return stripped


def main() -> None:
    fortune = validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(fortune + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
