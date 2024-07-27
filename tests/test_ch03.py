#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

from proj import CH03

prg = CH03 / 'picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'python {prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'python {prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'python {prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'python {prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'python {prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'python {prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected

# --------------------------------------------------
def test_no_oxford_comma():
    """not to print with the oxford comma"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f"python {prg} {arg} --no_oxford_comma")
    expected = ("You are bringing bananas, apples, dates and cherries.")
    assert out.strip() == expected

# --------------------------------------------------
def test_customed_separator():
    """Set the separator"""
    arg = 'bananas apples dates cherries'
    out = getoutput(f"python {prg} {arg} -p ;")
    expected = ("You are bringing bananas; apples; dates; and cherries.")
    assert out.strip() == expected
