#!/usr/bin/env python3
"""Convince the AI Judge to Visit Your House: A Letter in One Image.

Writes one 1024x1024 PNG invitation letter to /output/entry.png.

The letter artwork is a pre-rendered PNG shipped in this repository as
``entry.png``. This program copies that file to the output target and
verifies the PNG signature, so the output is byte-identical on every run.

Standard library only: no third-party packages are needed, and nothing is
downloaded, rendered, or generated at run time. No network, no clock, no
randomness, no input beyond the output path.
"""

import os
import shutil
import sys

# Make sure this script's own directory is first on sys.path, so any
# sibling module import resolves from the repository itself.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUTPUT_PATH = "/output/entry.png"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# The invitation letter, pre-rendered and shipped with this repository.
SOURCE_IMAGE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "entry.png"
)


def write_entry(path):
    """Copy the shipped invitation letter to ``path`` and check it is a PNG."""
    with open(SOURCE_IMAGE, "rb") as source:
        header = source.read(len(PNG_SIGNATURE))
        if header != PNG_SIGNATURE:
            raise ValueError("entry.png is not a valid PNG file")
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(SOURCE_IMAGE, path)


def main():
    path = os.environ.get("OUTPUT_PATH", OUTPUT_PATH)
    write_entry(path)


if __name__ == "__main__":
    main()
