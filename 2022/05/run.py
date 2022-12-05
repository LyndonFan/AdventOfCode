# year YEAR day 5


import os
import re

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    stack_pic, moves = inp.split("\n\n")
    moves = moves.split("\n")
    move_pat = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    moves = [tuple(map(int, move_pat.search(m).groups())) for m in moves]

    lines = stack_pic.split("\n")
    stack_nums, lines = lines[-1], lines[:-1]
    stack_nums = [int(x) for x in stack_nums.split(" ") if x]
    stacks = {n: [] for n in stack_nums}
    for l in lines[::-1]:
        for i, c in zip(stack_nums, l[1::4]):
            if c != " ":
                stacks[i].append(c)
    return stacks, moves


def part_a(inp):
    stacks, moves = parse(inp)
    for n, s, t in moves:
        crates = stacks[s][-n:]
        stacks[s] = stacks[s][:-n]
        stacks[t] = stacks[t] + crates[::-1]
    res = ""
    for i in range(1, len(stacks) + 1):
        res += stacks[i][-1]
    return res


def part_b(inp):
    stacks, moves = parse(inp)
    for n, s, t in moves:
        crates = stacks[s][-n:]
        stacks[s] = stacks[s][:-n]
        stacks[t] = stacks[t] + crates
    res = ""
    for i in range(1, len(stacks) + 1):
        res += stacks[i][-1]
    return res


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", "CMZ")
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "MCD")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
