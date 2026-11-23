#!/usr/bin/env python3
"""Office Jokes entry: writes one one-line joke about office life to entry.txt.

Standard library only, no network, deterministic.
"""

import os

JOKE = "I hit reply-all to ask everyone to stop hitting reply-all."


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 199, f"joke must be 1-199 chars, got {len(text)}"
    assert text.strip(), "joke must not be only whitespace"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
