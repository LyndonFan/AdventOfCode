# year 2023 day 16
import os
import re
from dataclasses import dataclass
from typing import Union, Any
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

NEW_DIRECTION_LOOKUP = {
    ".": {x: [x] for x in [UP, DOWN, LEFT, RIGHT]},
    "/": {
        UP: [RIGHT], DOWN: [LEFT], LEFT: [DOWN], RIGHT: [UP],
    },
    "\\": {
        UP: [LEFT], DOWN: [RIGHT], LEFT: [UP], RIGHT: [DOWN],
    },
    "|": {
        UP: [UP], DOWN: [DOWN], LEFT: [UP, DOWN], RIGHT: [UP, DOWN],
    },
    "-": {
        UP: [LEFT, RIGHT], DOWN: [LEFT, RIGHT], LEFT: [LEFT], RIGHT: [RIGHT],
    },
}


def part_a(inp):
    data = parse(inp)
    seen_positions = set()
    seen_config = set()
    beams = [((0,-1), RIGHT)]
    while beams:
        new_beams = []
        for pos, direction in beams:
            if (pos, direction) in seen_config:
                continue
            seen_config.add((pos, direction))
            seen_positions.add(pos)
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if (new_pos, direction) in seen_config:
                continue
            # skip if out of bounds
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            if new_pos[0] >= len(data) or new_pos[1] >= len(data[0]):
                continue
            tile = data[new_pos[0]][new_pos[1]]
            new_directions = NEW_DIRECTION_LOOKUP[tile][direction]
            for new_direction in new_directions:
                new_beams.append((new_pos, new_direction))
        beams = new_beams
    to_remove = set()
    for pos, direction in seen_config:
        if pos[0] < 0 or pos[1] < 0:
            to_remove.add((pos, direction))
        if pos[0] >= len(data) or pos[1] >= len(data[0]):
            to_remove.add((pos, direction))
    seen_config -= to_remove
    seen_positions.remove((0,-1))
    for pos in seen_positions:
        if pos[0] < 0 or pos[1] < 0:
            seen_positions.remove(pos)
        if pos[0] >= len(data) or pos[1] >= len(data[0]):
            seen_positions.remove(pos)
    
    print_data = [[x for x in line] for line in data]
    for pos, direction in seen_config:
        y, x = pos
        if data[y][x] != ".":
            continue
        if print_data[y][x] not in "234^<>v":
            print_data[y][x] = {
                UP: "^",
                DOWN: "v",
                LEFT: "<",
                RIGHT: ">",
            }[direction]
        elif print_data[y][x] in "^<>v":
            print_data[y][x] = "2"
        else:
            print_data[y][x] = str(int(print_data[y][x]) + 1)
    for row in print_data:
        print("".join(row))
    print("=" * len(data[0]))
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if (i,j) in seen_positions:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print("=" * len(data[0]))
    return len(seen_positions)


def part_b(inp):
    data = parse(inp)
    return 0


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 46)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "B_RESPONSE")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
