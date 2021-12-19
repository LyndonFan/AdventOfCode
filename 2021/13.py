# day 13 solutions

"""
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........
Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

How many dots are visible after completing just the first fold instruction on your transparent paper?

To begin, get your puzzle input.
"""


def q13a(inp):
    coors, folds = inp.split("\n\n")
    coors = coors.split("\n")
    folds = folds.split("\n")
    folds = folds[:1]
    coors = [list(map(int, c.split(","))) for c in coors]
    folds = [f.split(" ")[-1].split("=") for f in folds]
    folds = [[d, int(v)] for d, v in folds]

    # find the bounds of the paper
    x_min = 0
    x_max = max([c[0] for c in coors])
    y_min = 0
    y_max = max([c[1] for c in coors])

    dots = set(map(tuple, coors))

    if len(coors) <= 20:
        print("\n".join(["".join(["." if (x, y) not in dots else "#" for x in range(
            x_min, x_max + 1)]) for y in range(y_min, y_max + 1)]))

    # perform fold
    for d, v in folds:
        if d == "x":
            new_x_min = min(x_min, x_max - 2*(x_max-v))
            new_x_max = v
            print(f"folding along x={v}")
            new_dots = set()
            for x, y in dots:
                if v <= x <= x_max:
                    new_dots.add((x-2*(x-v), y))
                else:
                    new_dots.add((x, y))
            x_min = new_x_min
            x_max = new_x_max
        elif d == "y":
            new_y_min = min(y_min, y_max - 2*(y_max-v))
            new_y_max = v
            print(f"folding along y={v}")
            new_dots = set()
            for x, y in dots:
                if v <= y <= y_max:
                    new_dots.add((x, y-2*(y-v)))
                else:
                    new_dots.add((x, y))
            y_min = new_y_min
            y_max = new_y_max
        else:
            raise Exception("bad fold")
        dots = new_dots.copy()

        if len(coors) <= 20:
            print("\n".join(["".join(["." if (x, y) not in dots else "#" for x in range(
                x_min, x_max + 1)]) for y in range(y_min, y_max + 1)]))
    return len(dots)


def q13b(inp):
    coors, folds = inp.split("\n\n")
    coors = coors.split("\n")
    folds = folds.split("\n")
    coors = [list(map(int, c.split(","))) for c in coors]
    folds = [f.split(" ")[-1].split("=") for f in folds]
    folds = [[d, int(v)] for d, v in folds]

    # find the bounds of the paper
    x_min = 0
    x_max = max([c[0] for c in coors])
    y_min = 0
    y_max = max([c[1] for c in coors])

    dots = set(map(tuple, coors))

    if len(coors) <= 20:
        print("\n".join(["".join(["." if (x, y) not in dots else "#" for x in range(
            x_min, x_max + 1)]) for y in range(y_min, y_max + 1)]))

    # perform fold
    for d, v in folds:
        if d == "x":
            new_x_min = min(x_min, x_max - 2*(x_max-v))
            new_x_max = v
            print(f"folding along x={v}")
            new_dots = set()
            for x, y in dots:
                if v <= x <= x_max:
                    new_dots.add((x-2*(x-v), y))
                else:
                    new_dots.add((x, y))
            x_min = new_x_min
            x_max = new_x_max
        elif d == "y":
            new_y_min = min(y_min, y_max - 2*(y_max-v))
            new_y_max = v
            print(f"folding along y={v}")
            new_dots = set()
            for x, y in dots:
                if v <= y <= y_max:
                    new_dots.add((x, y-2*(y-v)))
                else:
                    new_dots.add((x, y))
            y_min = new_y_min
            y_max = new_y_max
        else:
            raise Exception("bad fold")
        dots = new_dots.copy()

        if len(coors) <= 20:
            print("\n".join(["".join(["." if (x, y) not in dots else "#" for x in range(
                x_min, x_max + 1)]) for y in range(y_min, y_max + 1)]))

    print("\n".join(["".join(["." if (x, y) not in dots else "#" for x in range(
        x_min, x_max + 1)]) for y in range(y_min, y_max + 1)]))
    return 0


if __name__ == "__main__":
    with open("13test.txt", "r") as f:
        data = f.read().strip()
    print("Testing  (a):", q13a(data))
    print("Expected (a):", 17)
    print("Testing  (b):", q13b(data))
    print("Expected (b):", 'B_RESPONSE')
    with open("13.txt", "r") as f:
        data = f.read().strip()
    print("Actual   (a): ", q13a(data))
    print("Actual   (b): ", q13b(data))
