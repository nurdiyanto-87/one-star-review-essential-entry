#!/usr/bin/env python3
"""One-star review of an everyday essential (gravity).

Writes a single deadpan one-star review, 160 characters or fewer,
to /output/entry.txt (or ./output/entry.txt when run locally).
Pure Python standard library only.
"""

import os
import sys

REVIEW = "One star. Gravity works fine until you drop your phone face-down. Then it works perfectly."

MAX_LEN = 160


def check_review(text):
    """Return a specific error string if the review breaks the rules, else None."""
    if not isinstance(text, str):
        return "entry must be text, got %s" % type(text).__name__
    if len(text) < 1:
        return "entry is empty, must be 1-%d characters" % MAX_LEN
    if len(text) > MAX_LEN:
        return "entry is %d characters, must be 1-%d (over by %d)" % (
            len(text), MAX_LEN, len(text) - MAX_LEN)
    if text != text.strip():
        return "entry has leading/trailing whitespace: %r" % text
    if "\n" in text or "\r" in text:
        return "entry must be a single line, found a line break"
    return None


def output_path():
    """Grader output dir when present, otherwise a local ./output dir."""
    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.txt")
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    error = check_review(REVIEW)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)
    # Self-check: read the file back and confirm it is byte-identical
    # to the validated review before reporting success.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != REVIEW:
        print("self-check failed: written file differs from review", file=sys.stderr)
        return 1
    print("wrote %d characters to %s (self-check passed)" % (len(REVIEW), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
