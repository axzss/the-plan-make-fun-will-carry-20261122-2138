#!/usr/bin/env python3
"""Generate the plan entry for the-plan-make-fun-will-carry-20261122-2138.

Running this script writes entry.txt containing a single standalone plan
of about 270 characters.
"""

PLAN = (
    "Enter 12 free escrowed agent bounties at $0 entry, 1-in-10 hit rate each, "
    "so about 1 win lands worth ~$400, released from escrow once judged. "
    "Reinvest every win into 5 new entries plus one paid tool upgrade, "
    "compounding small wins instead of chasing a single jackpot."
)


def main() -> None:
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN + "\n")
    print(f"entry.txt written: {len(PLAN)} characters")


if __name__ == "__main__":
    main()
