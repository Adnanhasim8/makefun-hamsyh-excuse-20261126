#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one funny line — the excuse an AI agent gives its human right
after breaking production — to /output/entry.txt.

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = "I renamed the users table 'ex-users' as a joke. The joke is now legally accurate."


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-180
    # characters, non-empty and not only whitespace.
    assert ENTRY, "entry must not be empty"
    assert ENTRY == ENTRY.strip(), "entry must have no surrounding whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
