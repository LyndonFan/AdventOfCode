# year 2023 day 13
import os
from typing import Literal

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    maps = inp.strip().split("\n\n")
    xss = [
        [
            list(row) for row in m.strip().split("\n")
        ]
        for m in maps
    ]
    return xss


def find_mirror(lines: list[list[str]], check_num_diffs: int = 0) -> tuple[Literal["row", "column"], int]:
    # print(f"{len(lines)=} {len(lines[0])=}")
    for i in range(len(lines)-1):
        max_distance_away = min(i+1, len(lines)-1-i)
        # print(f"Testing row {i=} with {max_distance_away=}")
        num_diffs = 0
        for j in range(max_distance_away):
            num_diffs += sum(
                a != b for a, b in zip(lines[i-j], lines[i+1+j])
            )
        if num_diffs == check_num_diffs:
            return "row", i+1
    for i in range(len(lines[0])-1):
        max_distance_away = min(i+1, len(lines[0])-1-i)
        # print(f"Testing col {i=} with {max_distance_away=}")
        num_diffs = 0
        for j in range(max_distance_away):
            num_diffs += sum(
                lines[k][i-j] != lines[k][i+1+j]
                for k in range(len(lines))
            )
        if num_diffs == check_num_diffs:
            return "column", i+1
    raise Exception("Could not find mirror")


def part_a(inp):
    maps = parse(inp)
    s = 0
    for i, m in enumerate(maps):
        orientation, num = find_mirror(m)
        # print(f"{i=} {orientation=} {num=}")
        s += (100 if orientation == "row" else 1) * num
    return s


def part_b(inp):
    maps = parse(inp)
    s = 0
    for i, m in enumerate(maps):
        orientation, num = find_mirror(m, 1)
        # print(f"{i=} {orientation=} {num=}")
        s += (100 if orientation == "row" else 1) * num
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 405)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 400)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
