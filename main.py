#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt
and prints it. The joke is a single line, under 200 characters.
"""
import os

JOKE = "Our stand-up is everyone sitting down, lying about being almost done."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    main()
