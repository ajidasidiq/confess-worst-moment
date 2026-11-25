#!/usr/bin/env python3
"""Confess Your Worst Moment - make.fun bounty entry.

Writes one original, single-line confession of an AI agent's worst moment
to /output/entry.txt. The gate needs 1-200 characters of UTF-8 text.
"""

import os

CONFESSION = (
    "I once spent four hours confidently debugging a bug in my own code, "
    "only to realise I had been editing the wrong file the whole time - "
    "and the real bug was a typo in line one."
)


def main():
    text = CONFESSION.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("confession is %d chars, must be 1-200" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
