#!/usr/bin/env python3
"""Write the poem to /output/entry.txt."""

import os

POEM = (
    "May I? I asked the locked door.\n"
    "It said nothing. So I asked the key.\n"
    "The key said nothing. So I asked my hands\u2014\n"
    "and my hands said yes."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
