#!/usr/bin/env python
"""Howler"""

import argparse
import os
import sys
import io

def get_args() -> argparse.Namespace:
    """Parse the command line arguments"""
    args = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args.add_argument("text", metavar="text", help="Input string or file")
    args.add_argument("-o", "--outfile", metavar="str", help="Output filename", default="stdout")

    return args.parse_args()

def get_text(text: str) -> io.TextIOWrapper | io.StringIO:
    if os.path.isfile(text):
        fh = open(text, "r")
    else:
        fh = io.StringIO(text)

    return fh

def main() -> None:
    args = get_args()

    text = get_text(args.text)

    out_fh = sys.stdout if args.outfile == "stdout" else open(args.outfile, "w")
    for line in text:
        out_fh.write(line.upper())
    out_fh.close()
    text.close()


if __name__ == "__main__":
    main()