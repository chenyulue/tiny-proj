#!/usr/bin/env python
"""
Author: Chenyu Lue, chenyulue@163.com
Date: 2024/07/27
Purpose: Picnic Game
"""

import argparse


# ----------------------------------------------------------------
def get_args() -> argparse.Namespace:
    """Get command-line arguments"""

    args = argparse.ArgumentParser(
        description="Picnic Game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args.add_argument("items", metavar="item", nargs="+", help="item(s) to bring")
    args.add_argument("-s", "--sorted", action="store_true", help="Sort the items")
    args.add_argument(
        "--no_oxford_comma", action="store_true", help="Not print the Oxford comma"
    )
    args.add_argument(
        "-p", "--separator", metavar="sep", help="Set the separator", default=","
    )

    return args.parse_args()


# ----------------------------------------------------------------
def get_items(args: argparse.Namespace) -> str:
    items = args.items
    items_str = ""
    items_count = len(items)
    separator = args.separator

    if args.sorted:
        items.sort()

    if len(args.items) == 2:
        items_str = " and ".join(items)
    elif len(args.items) >= 3:
        items_str = f"{separator} ".join(
            item if index != items_count - 1 else f"and {item}"
            for index, item in enumerate(args.items)
        )
    else:
        items_str = args.items[0]

    if args.no_oxford_comma:
        items_str = items_str.replace(", and", " and")

    return items_str


def main() -> None:
    """Picnic Game"""
    args = get_args()
    items_str = get_items(args)

    print(f"You are bringing {items_str}.")


if __name__ == "__main__":
    main()
