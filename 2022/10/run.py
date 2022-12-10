# year 2022 day 10
import os

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data


def part_a(inp):
    data = parse(inp)
    ans = 0
    cycle = 1
    curr = 1
    for l in data:
        if l == "noop":
            if cycle % 40 == 20:
                ans += cycle * curr
            cycle += 1
        else:
            v = l.split(" ")[-1]
            v = int(v)
            if cycle % 40 == 20:
                ans += cycle * curr
            cycle += 1
            if cycle % 40 == 20:
                ans += cycle * curr
            cycle += 1
            curr += v
    return ans


def part_b(inp):
    data = parse(inp)
    cycle = 1
    x = 1
    lines = [[" " for _ in range(40)] for _ in range(6)]

    def render():
        draw = False
        for e in [-1, 0, 1]:
            i = (cycle - 1) % 40
            if x + e == i:
                r = (cycle - 1) // 40
                lines[r][i] = "#"

    for l in data:
        if l == "noop":
            render()
            cycle += 1
        else:
            v = l.split(" ")[-1]
            v = int(v)
            render()
            cycle += 1
            render()
            cycle += 1
            x += v
    res = "\n" + "\n".join("".join(r) for r in lines)
    return res


B_RESPONSE = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 13140)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", B_RESPONSE)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
