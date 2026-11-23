#!/usr/bin/env python3
"""Six Words, One Story.

Writes one complete story in exactly six words to /output/entry.txt.

The story: a homecoming that lands as an erasure. Three words set up
the return, three words undo it -- a whole life of absence is implied
in the gap between them, and the reader fills in why nobody remembers.
"""

import os

STORY = "He came home. Nobody remembered him."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"length {len(STORY)} outside 1-60"
    assert STORY.strip(), "story must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    # Verify the file round-trips exactly: what the judge reads is
    # byte-for-byte what we wrote, still six words, still in range.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == STORY, "round-trip mismatch"
    assert len(written.split()) == 6


if __name__ == "__main__":
    main()
