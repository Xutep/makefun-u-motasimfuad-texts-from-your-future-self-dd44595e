#!/usr/bin/env python3
"""Texts From Your Future Self - make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt. Deterministic, standard library only, no network,
no randomness: the same text every run.
"""

import os

# One text message, under 200 characters, from the future self.
# Specific voice, a twist that pays off at the end, and a fresh angle:
# not broke, not tired - a novel about a man who can't finish anything.
TEXT = (
    "Future you: the novel's done \u2014 900 pages about a man who "
    "can't finish anything. It won an award. My acceptance speech "
    "was just 'huh' for 40 seconds. Start chapter two tonight."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
