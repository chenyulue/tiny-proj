#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput
import pytest

from proj import CH02

prg = CH02 / 'crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'python {prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'python {prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'python {prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'python {prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())


# --------------------------------------------------
@pytest.mark.parametrize(
    "word,article",
    [("octopus", "an"), ("Octopus", "An"),
     ("cat", "a"), ("Cat", "A")]
)
def test_case_match(word, article):
    """an octopus, An Octopus"""
    out = getoutput(f"python {prg} {word}")
    assert out.strip() == template.format(article, word)


# --------------------------------------------------
def test_side_starboard():
    """change side to starboard"""
    out = getoutput(f"python {prg} octopus --starboard")
    assert out.strip() == template.replace("larboard", "starboard").format("an", "octopus")

# --------------------------------------------------
@pytest.mark.parametrize(
    "word",
    ["3octopus", ",uppbound"],
)
def test_start_with_non_letters(word):
    """words start with non-letters"""
    out = getoutput(f"python {prg} {word}")
    assert out.strip() == 'Ahoy, Captain, {} off the larboard bow!'.format(word)