#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent
message itself, one line written exactly as it was typed.
"""

from pathlib import Path

ENTRY = (
    "To: the friend I ghosted after your dad's funeral\n"
    "I typed \"I'm sorry I wasn't there\" six times and deleted it "
    "every time because sorry felt too small and too late at once.\n"
)

# Gate from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 260 characters, and the message itself one line of
# at most 200 characters. Fail loudly instead of writing a bad entry.
assert 1 <= len(ENTRY) <= 260, f"entry is {len(ENTRY)} characters"
_lines = ENTRY.rstrip("\n").split("\n")
assert len(_lines) == 2, f"entry must be exactly two lines, got {len(_lines)}"
assert _lines[0].startswith("To: "), "first line must be the To: line"
assert len(_lines[1]) <= 200, f"message is {len(_lines[1])} characters"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
