import pytest
from run import RangeList

def test_init():
    ranges = [(1, 5), (10, 15), (30, 25)]
    rl = RangeList(ranges)
    assert rl.ranges == [(1, 6), (10, 25), (30, 55)]

def test_contains():
    ranges = [(1, 5), (10, 15), (20, 25)]
    rl = RangeList(ranges)
    assert 3 in rl
    assert 7 not in rl

def test_len():
    ranges = [(1, 5), (10, 15), (20, 25)]
    rl = RangeList(ranges)
    assert len(rl) == 5 + 15 + 25