#!/usr/bin/env python3
"""One-star review of an everyday essential (gravity).

Writes a single deadpan one-star review, 160 characters or fewer,
to /output/entry.txt (or ./output/entry.txt when run locally).
Pure Python standard library only.
"""

import os
import sys

REVIEW = "One star. Gravity works fine until you drop your phone face-down. Then it works perfectly."


def main() -> int:
    text = REVIEW
    if not (1 <= len(text) <= 160):
        print(f"entry is {len(text)} characters, must be 1-160", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    out_dir = "/output" if os.path.isdir("/output") else os.path.join(os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
