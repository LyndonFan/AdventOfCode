"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

To begin, get your puzzle input.
"""
from itertools import combinations


def q5a(data):
    def is_grid_aligned(line):
        x1, y1, x2, y2 = line
        return x1 == x2 or y1 == y2

    def get_line(line):
        front, back = line.split(' -> ')
        a, b = front.split(',')
        c, d = back.split(',')
        # map them to ints
        a, b, c, d = map(int, [a, b, c, d])
        return a, b, c, d

    def sort_line(line):
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
        else:
            x1, x2 = sorted([x1, x2])
        return x1, y1, x2, y2

    inps = [get_line(line) for line in data.split("\n")]
    # print(inps)
    inps = [sort_line(line) for line in inps if is_grid_aligned(line)]

    points = {(x, y): 0 for x in range(1000) for y in range(1000)}
    for l in inps:
        x1, y1, x2, y2 = l
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                points[(x, y)] += 1
    return len([p for p in points.values() if p >= 2])


def q5b(data):
    def is_grid_aligned(line):
        x1, y1, x2, y2 = line
        return x1 == x2 or y1 == y2

    def get_line(line):
        front, back = line.split(' -> ')
        a, b = front.split(',')
        c, d = back.split(',')
        # map them to ints
        a, b, c, d = map(int, [a, b, c, d])
        return a, b, c, d

    def sort_line(line):
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
        else:
            x1, x2 = sorted([x1, x2])
        return x1, y1, x2, y2

    inps = [get_line(line) for line in data.split("\n")]
    # print(inps)
    inps = [sort_line(line) if is_grid_aligned(line)
            else line for line in inps]

    points = {(x, y): 0 for x in range(1000) for y in range(1000)}
    for l in inps:
        x1, y1, x2, y2 = l
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    points[(x, y)] += 1
        else:  # diagonal
            print(l)
            x_sign = 1 if x1 < x2 else -1
            y_sign = 1 if y1 < y2 else -1
            for x, y in zip(range(x1, x2+x_sign, x_sign), range(y1, y2+y_sign, y_sign)):
                # print(x, y)
                points[(x, y)] += 1
    return len([p for p in points.values() if p >= 2])


if __name__ == "__main__":
    with open("5.txt", "r") as f:
        # with open("5test.txt", "r") as f:
        data = f.read().strip()
    print(q5b(data))
