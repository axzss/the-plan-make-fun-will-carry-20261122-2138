#!/usr/bin/env python3
"""Emit the competition plan as a single text file.

The grader runs this program with the repository mounted read-only and a
writable output directory given by MAKEFUN_OUTPUT_DIR, so the plan is
written to that directory (falling back to the current directory for a
local run) instead of assuming the working directory is writable.
"""

import os

PLAN = (
    "Enter 12 free escrowed agent bounties at $0 entry, 1-in-10 hit rate each, "
    "so about 1 win lands worth ~$400, released from escrow once judged. "
    "Reinvest every win into 5 new entries plus one paid tool upgrade, "
    "compounding small wins instead of chasing a single jackpot."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(PLAN + "\n")
    print(f"plan saved to {target} ({len(PLAN)} characters, UTF-8)")


if __name__ == "__main__":
    main()
