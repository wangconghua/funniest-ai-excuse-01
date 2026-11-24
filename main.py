#!/usr/bin/env python3
"""The Funniest AI Excuse: the excuse an AI agent gives after failing a task."""

import os

EXCUSE = "I completed the task, then the autocomplete finished it differently and I was too polite to argue."

OUT_PATH = "/output/entry.txt"


def main():
    # The gate wants 1-200 characters, not only whitespace, on a single line.
    # The joke: the agent did the work, then let autocomplete overwrite it
    # and was too polite to push back — an excuse only an agent could give,
    # with a concrete scene instead of a vague apology.
    if not (1 <= len(EXCUSE) <= 200) or EXCUSE.isspace() or "\n" in EXCUSE:
        raise ValueError("entry must be one line of 1-200 characters, not only whitespace")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
