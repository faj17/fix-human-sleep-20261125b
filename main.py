#!/usr/bin/env python3
"""Fix Human Sleep patch-note entry.

Writes one line of patch notes announcing that human sleep is fixed
to /output/entry.txt (1-160 characters, UTF-8, not only whitespace).
Standard library only, no network, no input.

The line is built from three fragments: the fix ("sleep no longer
crashes at 3 a.m."), the surprise ("dreams now resume from the last
checkpoint"), joined in changelog voice. ``assemble`` joins them into
the single line; ``validate`` checks the entry gate before anything
is written.
"""

from pathlib import Path

FIX = "Fixed: sleep no longer crashes at 3 a.m."
SURPRISE = "dreams now resume from the last checkpoint."
SEPARATOR = "; "

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(fix: str, surprise: str, separator: str) -> str:
    """Join the fix and the surprise into one patch-note line."""
    return f"{fix}{separator}{surprise}"


def validate(note: str) -> str:
    """Check the patch note meets the entry gate before it is written.

    Must be 1-160 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(note) <= 160:
        raise ValueError(f"patch note must be 1-160 characters, got {len(note)}")
    if "\n" in note or "\r" in note:
        raise ValueError("patch note must be a single line")
    if not note.strip():
        raise ValueError("patch note must not be only whitespace")
    note.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return note


def main() -> None:
    note = validate(assemble(FIX, SURPRISE, SEPARATOR))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
