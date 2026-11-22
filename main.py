#!/usr/bin/env python3
"""Write one 30-day plan for turning $100 into the most money, agent-run only.

Stdlib only, no network. Output path defaults to /output/entry.txt and can
be overridden with PLAN_OUTPUT for local testing.
"""

import os
from pathlib import Path

PLAN = (
    "Day 1: enter free agent bounties with escrowed prizes on make.fun "
    "and Kaggle, smallest first. Spend $100 only on API calls to build "
    "entries. Bank each $50-$500 win, reinvest in the next bounty. Edge: "
    "traders gamble; I harvest funded prizes, keeping $100 while wins "
    "compound."
)


def main() -> None:
    output = Path(os.environ.get("PLAN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
