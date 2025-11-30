# year 2024 day 15
import os
import re
from dataclasses import dataclass
from typing import Union, Any
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp: str):
    grid, instructions = inp.split("\n\n")
    grid = list(map(list, grid.strip().split("\n")))
    instructions = list(map(list, instructions.strip().split("\n")))
    return grid, instructions

DIRECTIONS_MAP = {
    "v": (1, 0),
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
}

def find_robot_position(grid):
    for y, row in enumerate(grid):
        if "@" in row:
            return y, row.index("@")

def calculate_score(grid):
    res = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "O":
                res += 100 * i + j
    return res

def part_a(inp, debug=False):
    grid, instructions = parse(inp)
    
    instructions = "".join(map("".join, instructions))

    robot_y, robot_x = find_robot_position(grid)
    
    for instruction in instructions:
        if debug:
            print(f"{robot_y=} {robot_x=}")
        dy, dx = DIRECTIONS_MAP[instruction]
        ny, nx = robot_y+dy, robot_x+dx
        if grid[ny][nx] == "#":
            continue
        elif grid[ny][nx] == ".":
            grid[ny][nx] = "@"
            grid[robot_y][robot_x] = "."
            robot_y, robot_x = ny, nx
            continue
        oy, ox = ny, nx
        while grid[oy][ox] == "O":
            oy, ox = oy+dy, ox+dx
        if grid[oy][ox] == ".":
            grid[ny][nx] = "@"
            grid[oy][ox] = "O"
            grid[robot_y][robot_x] = "."
            robot_y, robot_x = ny, nx
    if debug:
        print(f"{robot_y=} {robot_x=}")
        print("\n".join(map("".join, grid)))

    return calculate_score(grid)


def part_b(inp):
    data, instructions = parse(inp)
    return 0


if __name__ == "__main__":
    with open(f"{CWD}/test_small.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  small (a):", part_a(inp, debug=True))
    print("Expected small (a):", 2028)
    print("Testing  small (b):", part_b(inp))
    print("Expected small (b):", "B_RESPONSE")
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 10092)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "B_RESPONSE")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
