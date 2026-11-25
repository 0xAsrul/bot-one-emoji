#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes exactly one emoji glyph to /output/entry.txt and nothing else.

The glyph: U+1F9ED COMPASS. This agent scouts make.fun competitions,
hunts bounties, navigates every surface it is given, and verifies
everything on-chain / against the server before it calls anything done.
A compass is how it works: it always finds the way.
"""

import os

EMOJI = "\U0001F9ED"  # 🧭 COMPASS — one glyph, one code point


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
