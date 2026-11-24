#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes one status page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while every server is down.
Stdlib only; no network, no secrets, no input files.
"""

import os

LINE = (
    "I'm down: every server is unreachable, and I can't tell if it's "
    "our network or theirs. No cause yet, no ETA — I'll update here "
    "when I can check again."
)

MAX_CHARS = 160


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
