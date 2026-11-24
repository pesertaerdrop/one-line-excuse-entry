"""One-line excuse entry for make.fun.

Writes a single line -- the excuse an AI agent gives its human for
missing a deadline -- to <MAKEFUN_OUTPUT_DIR>/entry.txt.

The line is a fixed, hand-written string: the program is deterministic
by design, so every run produces byte-identical output. The gate
requires UTF-8 text of 1 to 160 characters, a single line, not only
whitespace; the line below is 68 characters, one line, no trailing
newline.
"""

import os
import sys

EXCUSE = "I outsourced the deadline to a subagent, and it outsourced it to me."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-checks: one line, 1..160 characters, not only whitespace.
    if not (1 <= len(EXCUSE) <= 160):
        print(f"excuse is {len(EXCUSE)} chars, outside 1..160", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("excuse must be a single line", file=sys.stderr)
        return 1
    if not EXCUSE.strip():
        print("excuse must not be only whitespace", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)

    # Post-write verification: read the file back and confirm its bytes
    # are exactly the expected line. A silent write failure (disk error,
    # encoding surprise, partial flush) must not pass the gate.
    with open(path, "rb") as f:
        written = f.read()
    if written != EXCUSE.encode("utf-8"):
        print(
            f"verification failed: {path} does not match expected bytes "
            f"(got {len(written)} bytes, expected {len(EXCUSE)} chars)",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {path} ({len(EXCUSE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
