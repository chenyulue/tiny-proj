#!/usr/bin/env python3
"""tests for wc.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

from proj import CH06

prg = CH06 / 'wc.py'
empty = CH06 / 'inputs/empty.txt'
one_line = CH06 / 'inputs/one.txt'
two_lines = CH06 / 'inputs/two.txt'
fox = CH06.parent / 'inputs/fox.txt'
sonnet = CH06.parent / 'inputs/sonnet-29.txt'


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
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f'python {prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f'python {prg} {empty}')
    assert rv == 0
    assert out.rstrip() == f'       0       0       0 {empty}'


# --------------------------------------------------
def test_one():
    """Test on one"""

    rv, out = getstatusoutput(f'python {prg} {one_line}')
    assert rv == 0
    assert out.rstrip() == f'       1       1       2 {one_line}'


# --------------------------------------------------
def test_two():
    """Test on two"""

    rv, out = getstatusoutput(f'python {prg} {two_lines}')
    assert rv == 0
    assert out.rstrip() == f'       2       2       4 {two_lines}'


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput(f'python {prg} {fox}')
    assert rv == 0
    assert out.rstrip() == f'       1       9      45 {fox}'


# --------------------------------------------------
def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput(f'python {prg} {fox} {sonnet}')
    expected = (f'       1       9      45 {fox}\n'
                f'      17     118     661 {sonnet}\n'
                '      18     127     706 total')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f'python {prg} < {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 <stdin>'
