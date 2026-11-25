"""One Line, One Laugh - make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Python standard library only; deterministic, no network, no input files.
"""

import os

LINE = "I asked AI to write my apology; it said sorry so well my girlfriend forgave the robot, not me."


def main():
    # Gate, checked locally before writing: one line, 1-200 characters.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
