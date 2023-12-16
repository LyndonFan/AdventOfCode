from run import part_a

def test_splits():
    inp = r"""
..\..
.....
..-..
.....
"""
    assert part_a(inp.strip()) == 9
    inp = r"""
..\..
.....
..|..
.....
"""
    assert part_a(inp.strip()) == 6

    inp = r"""
\...
....
\.|.
....
....
"""
    assert part_a(inp.strip()) == 9
    inp = r"""
\...
....
\.-.
....
....
"""
    assert part_a(inp.strip()) == 6

def test_repeat_tile():
    inp = r"""
..\..
..-.\
.....
..\./
"""
    assert part_a(inp.strip()) == 13
    inp = r"""
...\...
./.....
/..-..\
\/..|./
"""
    expect_highlighted = r"""
#####..
.######
#######
##..###
"""
    assert part_a(inp.strip()) == expect_highlighted.count("#")