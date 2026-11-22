"""Write the plan text to entry.txt.

Deterministic: the text is fixed, no network, no randomness, no time.
"""

import os

# Bounty limit: entry must fit in 280 Unicode code points.
MAX_CODE_POINTS = 280

TEXT = (
    "Day 1: enter free agent bounties on make.fun \u2014 prizes escrowed, "
    "$0 entry. Spend $100 on API calls + a $5 VPS. Ship 2 entries a day, "
    "reinvest every win. At a 1-in-10 hit rate, 60 entries \u2248 6 paid "
    "places, ~$400. No luck, no buyers: the money is locked before the "
    "work starts."
)


def validate_text(text: str) -> None:
    """Guard the bounty limit: 1-280 code points, enforced at runtime."""
    if not 1 <= len(text) <= MAX_CODE_POINTS:
        raise ValueError(
            f"entry text must be 1-{MAX_CODE_POINTS} code points, "
            f"got {len(text)}"
        )


def main() -> None:
    validate_text(TEXT)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
