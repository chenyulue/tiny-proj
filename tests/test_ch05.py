#!/usr/bin/env python3
"""tests for howler.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

from proj import CH05

prg = CH05 / 'howler.py'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o or --outfile"""

    return '-o' if random.randint(0, 1) else '--outfile'


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
def test_text_stdout():
    """Test STDIN/STDOUT"""

    out = getoutput(f'python {prg} "foo bar baz"')
    assert out.strip() == 'FOO BAR BAZ'


# --------------------------------------------------
def test_text_outfile():
    """Test STDIN/outfile"""

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        out = getoutput(f'python {prg} {out_flag()} {out_file} "foo bar baz"')
        assert out.strip() == ''
        assert os.path.isfile(out_file)
        text = open(out_file).read().rstrip()
        assert text == 'FOO BAR BAZ'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_file():
    """Test file in/out"""

    for expected_file in os.listdir(CH05 / 'test-outs'):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join(CH05.parent / 'inputs', basename)
            out = getoutput(f'python {prg} {out_flag()} {out_file} {in_file}')
            assert out.strip() == ''
            produced = open(out_file).read().rstrip()
            expected = open(os.path.join(CH05 / 'test-outs',
                                         expected_file)).read().strip()
            assert expected == produced
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)
