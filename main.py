#!/usr/bin/env python3
"""make.fun bounty: Sum up 20 November's world news in one image.

The simplest allowed program: copy the image this repository holds
(entry.png) to /output/entry.png. No network, no randomness, no clock:
both runs write exactly the same bytes.
"""
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
