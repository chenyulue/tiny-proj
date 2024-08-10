#!/user/bin/env python
"""
Author: Chenyu Lue, chenyulue@163.com
Date: 2024/08/10
"""

from typing import TextIO
import argparse

from proj import CH07

def get_args() -> argparse.Namespace:
    """Get the arguments from the command line"""

    args = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args.add_argument("letter", type=str, help="Letter(s)", nargs="+")
    args.add_argument("-f", "--file", type=argparse.FileType("rt"), 
                      help="Input file", default=str(CH07 / "gashlycrumb.txt"))
    args.add_argument("-i", "--interactive", action="store_true",
                      help="Run the program interactively")

    return args.parse_args()

def create_mapping(fh: TextIO) -> dict[str, str]:
    return {line[0].lower(): line.rstrip() for line in fh}

def main() -> None:
    args = get_args()

    mapping = create_mapping(args.file)

    if args.interactive:
        print("Welcome to Gashlycrumb!")
        
    for letter in args.letter:
        line = mapping.get(letter.lower(), f'I do not know "{letter}".')
        print(line)

    if args.interactive:
        while ((letter := input("Please provide a letter [! to quit]: ")) != "!"):
            print(mapping.get(letter.lower(), f'I do not know "{letter}".'))

if __name__ == "__main__":
    main()
    