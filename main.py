#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Line 1 explains the everyday thing to a 10-year-old in a single vivid
sentence built on one analogy. Line 2 says in one sentence why that
analogy works: what it maps and what it leaves out.

Deterministic, stdlib only, no network.
"""

import os
import shutil
import sys

ENTRY = (
    "A traffic jam is a wide river of cars trying to squeeze through one tiny drinking straw.\n"
    "The straw shows how too many cars and too little road slow everyone down, "
    "but it leaves out the traffic lights, the drivers switching lanes, "
    "and the cars that turn off to find another way.\n"
)


def clear_contents(directory):
    """Remove only the contents of a directory, never the directory itself.

    The grader may run this with a root-owned output directory inside a
    sticky parent, so deleting the directory itself would fail with EPERM.
    Nested directories are removed, symlinks unlinked (never followed),
    fifos and sockets unlinked.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.islink(path) or not os.path.isdir(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    clear_contents(out_dir)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read it back and verify byte for byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("verification failed: entry.txt does not match", file=sys.stderr)
        return 1
    if not (1 <= len(ENTRY) <= 400) or not ENTRY.strip():
        print("verification failed: entry outside the 1-400 character gate",
              file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
