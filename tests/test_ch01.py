#!/usr/bin/env python3
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput
import pytest

from proj import CH01

prg = CH01 / 'hello.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""
    cmd = 'python' if os.name == 'nt' else 'python3'
    out = getoutput(f'{cmd} {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
@pytest.mark.skipif(os.name=='nt', reason="Skip executable test for win os")
def test_executable():
    """Says 'Hello, World!' by default"""

    out = getoutput(str(prg))
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{"python " if os.name=="nt" else ""}{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{"python " if os.name=="nt" else ""}{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
