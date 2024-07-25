#!/usr/bin/env python
"""Crow's Nest"""

import argparse


# ----------------------------------------------------------------
def get_args() -> argparse.Namespace:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("word", metavar="word", help="A word")
    parser.add_argument("--starboard", action=argparse.BooleanOptionalAction,
                        help="change the side to 'starboard'")

    return parser.parse_args()


# ----------------------------------------------------------------
def did_start_with_vowel(word: str) -> bool:
    return word[0].lower() in "aeiou"


def cry_out(word: str, side: str) -> str:
    article = ""
    if word[0].isalpha():
        article = "an" if did_start_with_vowel(word) else "a"
        if word[0].isupper():
            article = article.title()
    space = " " if article else ""
    
    return f"Ahoy, Captain, {article}{space}{word} off the {side} bow!"


def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = "starboard" if args.starboard else "larboard"

    print(cry_out(word, side))


if __name__ == "__main__":
    main()
