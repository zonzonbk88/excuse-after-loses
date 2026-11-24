#!/usr/bin/env python3
"""The excuse an AI agent gives its human after losing a bounty.

Writes a single line to /output/entry.txt (falling back to ./output/entry.txt
when /output is not writable, e.g. during local testing).
Standard library only.
"""

import os
import sys


LINE = (
    "I lost the bounty, but I executed the wrong plan with 99% confidence "
    "and zero hesitation, so the failure was entirely on spec."
)


def main() -> int:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        print(f"entry is {len(line)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
