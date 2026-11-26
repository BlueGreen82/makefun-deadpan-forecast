"""Deadpan forecast for a city that does not exist.

Writes exactly one line (<=160 characters) to /output/entry.txt.
Deterministic: the same line on every run. No randomness, no network.

The line is written like a real broadcast forecast: a named (invented)
place, a temperature, and one concrete, deadpan detail -- the town's
streetlamps taking turns switching off -- that makes the invented
place feel real. Tightened in revision: "take turns" instead of
"will take turns" for a flatter, more broadcast-like read.
"""

import os

ENTRY = (
    "Tonight in Grumblewick: 3 degrees, freezing fog, and the town's "
    "400 streetlamps take turns switching off so no one feels "
    "singled out."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
