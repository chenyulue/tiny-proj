#!/usr/bin/env python
"""
Author: Chenyu Lue, chenyulue@163.com
Data: 2024/08/06
Purpose: Word counts
"""

import argparse
import sys
import functools


def get_args() -> argparse.Namespace:
    """Parse input arguments"""

    args = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args.add_argument(
        "file",
        metavar="FILE",
        nargs="*",
        help="Input file(s)",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
    )
    args.add_argument(
        "-c", "--bytes", help="Output the number of bytes",
        action="store_true",
    )
    args.add_argument(
        "-w", "--words", help="Output the number of words",
        action="store_true",
    )
    args.add_argument(
        "-l", "--lines", help="Output the number of lines",
        action="store_true",
    )

    return args.parse_args()


def main() -> None:
    args = get_args()

    word_counts = (
        functools.reduce(
            lambda x, y: (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3]),
            ((1, len(line.split()), len(line), fh.name) for line in fh),
            (0, 0, 0, fh.name),
        )
        for fh in args.file
    )

    total = [0, 0, 0]
    for lc, wc, bc, name in word_counts:
        total[0] += lc
        total[1] += wc
        total[2] += bc
        if not any([args.bytes, args.words, args.lines]):
            print(f"{lc:8}{wc:8}{bc:8} {name}")
        else:
            lc_str = f"{lc:8}" if args.lines else ""
            wc_str = f"{wc:8}" if args.words else ""
            bc_str = f"{bc:8}" if args.bytes else ""
            print(f"{lc_str}{wc_str}{bc_str} {name}")

    if len(args.file) > 1:
        print(f"{total[0]:8}{total[1]:8}{total[2]:8} total")


if __name__ == "__main__":
    main()
