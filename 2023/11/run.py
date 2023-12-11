# year 2023 day 11
import os
import re
from dataclasses import dataclass
from typing import Union, Any
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))

class GalaxyMap:
    def __init__(self, lines: list[str], empty_line_factor: int) -> None:
        self.lines = [list(line) for line in lines]
        self.empty_line_factor = empty_line_factor
        self.star_locations = []
        self.width = len(self.lines[0])
        self.height = len(self.lines)
        for i, row in enumerate(self.lines):
            for j, cell in enumerate(row):
                if cell == "#":
                    self.star_locations.append((i, j))
        self.empty_rows = []
        for i, row in enumerate(self.lines):
            if all(cell == "." for cell in row):
                self.empty_rows.append(i)
        self.empty_columns = []
        for j in range(self.width):
            if all(row[j] == "." for row in self.lines):
                self.empty_columns.append(j)
    
    def distance(self, start: tuple[int, int], end: tuple[int, int]) -> int:
        distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
        distance += sum(
            (start[0] < x and x < end[0]) or (end[0] < x and x < start[0])
            for x in self.empty_rows
        ) * (self.empty_line_factor - 1)
        distance += sum(
            (start[1] < y and y < end[1]) or (end[1] < y and y < start[1])
            for y in self.empty_columns
        ) * (self.empty_line_factor - 1)
        return distance

def parse(inp):
    data = inp.split("\n")
    return data


def part_a(inp):
    data = parse(inp)
    galaxy_map = GalaxyMap(data, 2)
    s = 0
    for i, start in enumerate(galaxy_map.star_locations):
        for j, end in enumerate(galaxy_map.star_locations[i+1:], i+1):
            d = galaxy_map.distance(start, end)
            # print(f"{i+1: 2} -> {j+1: 2} = {d}")
            s += d
    return s


def part_b(inp, factor: int = 1000000):
    data = parse(inp)
    galaxy_map = GalaxyMap(data, factor)
    s = 0
    for i, start in enumerate(galaxy_map.star_locations):
        for j, end in enumerate(galaxy_map.star_locations[i+1:], i+1):
            d = galaxy_map.distance(start, end)
            s += d
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 374)
    print("Testing  (b):", part_b(inp, 100))
    print("Expected (b):", 8410)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
