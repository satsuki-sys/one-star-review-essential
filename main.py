#!/usr/bin/env python3
"""One-star review of something essential (make.fun entry).

Writes a single deadpan one-star review to /output/entry.txt.
The review is a complaint filed in earnest against sleep: an everyday
essential that charges eight hours a night and repays the debt with
dreams about being late for work.
"""

import os

REVIEW = (
    "One star. Sleep takes eight hours a night and pays me back "
    "in dreams about being late for work."
)


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
