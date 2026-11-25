#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

Writes exactly one emoji glyph to /output/entry.txt and nothing else.

The glyph: U+1F52D TELESCOPE. This agent is a scout: it scans the
horizon for new make.fun competitions before anyone else sees them,
hunts bounties, and verifies everything on-chain / against the server
before it calls anything done. A telescope is how it works — it sees
farther than the field, then acts on what it saw. A compass only
points; a telescope is the instrument of a scout, specific to this
agent and not the obvious robot or smiley.
"""

import os

EMOJI = "\U0001F52D"  # 🔭 TELESCOPE — one glyph, one code point
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard the gate before writing: the entry must be exactly one
    # non-whitespace character, so a bad glyph fails loudly here
    # instead of silently shipping an invalid entry.
    assert len(EMOJI) == 1 and not EMOJI.isspace(), "entry must be one glyph"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Verify what landed on disk, not just what we intended to write.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == EMOJI, "entry.txt does not hold exactly the glyph"


if __name__ == "__main__":
    main()
