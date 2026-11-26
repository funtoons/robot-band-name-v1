#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny name for a band made of robots, plus a few words on
its hit song, to /output/entry.txt (1-200 characters, UTF-8).

Deterministic and offline: no randomness, no network, no clock.
Running it twice produces byte-identical output.
"""

import os

ENTRY = "The Pop-Up Ads \u2014 hit single 'Click Here to Continue' has 40 million streams and zero listeners."


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
