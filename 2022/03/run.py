# year 2022 day 3
import os

CWD = os.path.dirname(os.path.abspath(__file__))

from string import ascii_lowercase as alpha
from string import ascii_uppercase as ALPHA


def parse(inp):
    data = inp.split("\n")
    return data


def conv(c: str):
    if c in alpha:
        return alpha.index(c) + 1
    return ALPHA.index(c) + 27


def split_pack(pack: str):
    m = len(pack) // 2
    return pack[:m], pack[m:]


def part_a(inp):
    data = parse(inp)
    s = 0
    for line in data:
        pa, pb = split_pack(line)
        overlap = set(pa).intersection(set(pb))
        s += sum(map(conv, overlap))
    return s


def part_b(inp):
    data = parse(inp)
    s = 0
    for i in range(0, len(data), 3):
        pa, pb, pc = data[i : i + 3]
        overlap = set(pa).intersection(set(pb)).intersection(set(pc))
        s += sum(map(conv, overlap))
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", "157")
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "70")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
