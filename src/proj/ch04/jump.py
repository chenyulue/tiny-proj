#! /usr/local/bin/env python
"""
Author: Chenyu Lue, chenyulue@163.com
Date: 2024/08/01
Purpose: Jump the five
"""

import argparse


def get_args() -> argparse.Namespace:
    """Parse the arguments"""
    args = argparse.ArgumentParser(
        description="Jump the five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    args.add_argument("text", metavar="str", help="Input text")

    return args.parse_args()


def decode_text(text: str) -> str:
    code_table = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }
    return "".join(code_table.get(char, char) for char in text)


def main() -> None:
    args = get_args()

    decoded_text = decode_text(args.text)

    print(decoded_text)


if __name__ == "__main__":
    main()
