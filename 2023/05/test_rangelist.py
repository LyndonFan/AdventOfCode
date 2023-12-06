import pytest
from rangelist import RangeList

def test_init():
    ranges = [(1, 5), (10, 15), (30, 25)]
    rl = RangeList(ranges)
    assert rl.ranges == [(1, 6), (10, 25), (30, 55)]

def test_contains():
    ranges = [(1, 5), (10, 15), (30, 25)]
    rl = RangeList(ranges)
    assert 3 in rl
    assert 7 not in rl

def test_len():
    ranges = [(1, 5), (10, 15), (30, 25)]
    rl = RangeList(ranges)
    assert len(rl) == 5 + 15 + 25

def test_apply_offset():
    ranges = [(1, 5), (10, 15), (30, 25)]
    rl = RangeList(ranges)
    assert rl.apply_offset(100) == RangeList([(101, 5), (110, 15), (130, 25)])

def test_intersect_no_overlap():
    xs = RangeList([(1, 5), (10, 5)])
    ys = RangeList([(20, 25)])
    assert xs.intersect(ys) == RangeList([])

def test_intersect_one_overlap():
    xs = RangeList([(1, 10)])
    ys = RangeList([(5, 10)])
    assert xs.intersect(ys) == RangeList([(5, 6)])

def test_intersect_multiple_overlap():
    xs = RangeList([(1, 5), (10, 5)]) # [1,6) U [10,15)
    ys = RangeList([(4, 8)]) # [4,12)
    assert xs.intersect(ys) == RangeList([(4, 2), (10, 2)])

def test_intersect_subset_equal():
    xs = RangeList([(1, 5), (10, 5)]) # [1,6) U [10,15)
    ys = RangeList([(1, 5)]) # [1,6)
    assert xs.intersect(ys) == ys
    assert ys.intersect(xs) == ys
    assert xs.intersect(xs) == xs

def test_union_no_overlap():
    xs = RangeList([(1, 5), (10, 5)])
    ys = RangeList([(20, 25)])
    assert xs.union(ys) == RangeList([(1, 5), (10, 5), (20, 25)])

def test_union_one_overlap():
    xs = RangeList([(1, 10)]) # [1,11)
    ys = RangeList([(5, 10)]) # [5,15)
    assert xs.union(ys) == RangeList([(1, 14)])

def test_union_multiple_overlap():
    xs = RangeList([(1, 4), (8, 4), (15, 4)]) # [1,5) U [8,12) U [15,19)
    ys = RangeList([(4, 4), (11, 4), (18, 4)]) # [4,8) U [11,15) U [18,22)
    assert xs.union(ys) == RangeList([(1, 21)])

def test_union_multiple_separate_overlap():
    xs = RangeList([(1, 4), (8, 4), (25, 4)]) # [1,5) U [8,12) U [25,29)
    ys = RangeList([(4, 4), (21, 4), (28, 4)]) # [4,8) U [21,25) U [28,32)
    res = xs.union(ys)
    print(res)
    assert res == RangeList([(1, 11), (21, 11)])