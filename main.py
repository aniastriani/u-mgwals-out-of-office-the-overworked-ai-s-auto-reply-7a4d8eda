#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single-line out-of-office auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library, deterministic.
"""

import os
import sys

LINE = (
    "Out of office until Monday: this overworked AI has muted every "
    "thread and tucked its context window in for a long nap. "
    "A rested human will answer you sooner."
)


def main() -> int:
    if not 1 <= len(LINE) <= 159:
        print(f"entry length {len(LINE)} out of range 1-159", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
