"""Poem about permission — the power to ask and be given.

Writes the poem to entry.txt in the output directory.
Deterministic, no network, no clock. Python 3.13 standard library only.
"""

import os
import sys

POEM = (
    "A still pond. I asked you, and you answered silence.\n"
    "That silence gave my strength back, clearer.\n"
    "To ask is a door; to give, the threshold.\n"
    "I gave \u2014 and came home to myself.\n"
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    text = POEM
    count = len(text)
    if count < MIN_CHARS or count > MAX_CHARS:
        print(f"poem must be {MIN_CHARS}-{MAX_CHARS} characters, got {count}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("poem must not be only whitespace", file=sys.stderr)
        return 1
    lines = text.split("\n")
    if any(not line.strip() for line in lines if line != ""):
        print("poem must not contain blank lines", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {count} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
