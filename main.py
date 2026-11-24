#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

The entry word is "Hermit": my Wi-Fi only exists in one corner of the
house, by the router, and refuses to venture anywhere else.
"""

import os

WORD = "Hermit"


def main() -> None:
    print(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
