#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a one-page newspaper
poster summing up the world news of Wednesday 18 November 2026. This
program copies it to /output/entry.png, deterministically and byte for
byte, so both grading runs write the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The grader runs the program twice; copying the same file guarantees both
# runs write identical bytes.
OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
