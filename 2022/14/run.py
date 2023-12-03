# year 2022 day 14
import os
from dataclasses import dataclass
from collections import namedtuple
CWD = os.path.dirname(os.path.abspath(__file__))

Position = namedtuple("Position", ["x", "y"])

class SandBox:
    def __init__(self, source: Position, rocks: list[list[Position]], has_floor: bool = False):
        self.source = source
        self.rocks = rocks
        self.blocked = set()
        self.max_depth = 0
        self.has_floor = has_floor
        self._add_blocked(rocks)
    
    def _add_blocked(self, rocks: list[list[Position]]):
        for rock in rocks:
            for i in range(len(rock) - 1):
                if rock[i].x == rock[i + 1].x:
                    y_start, y_end = min(rock[i].y, rock[i + 1].y), max(rock[i].y, rock[i + 1].y)
                    for j in range(y_start, y_end + 1):
                        self.blocked.add(Position(rock[i].x, j))
                else:
                    x_start, x_end = min(rock[i].x, rock[i + 1].x), max(rock[i].x, rock[i + 1].x)
                    for j in range(x_start, x_end + 1):
                        self.blocked.add(Position(j, rock[i].y))
        self.max_depth = max(p.y for p in self.blocked)
    
    def add_sand(self) -> bool:
        sand_pos = self.source
        while sand_pos.y <= self.max_depth:
            if (sand_pos.x, sand_pos.y + 1) not in self.blocked:
                sand_pos = Position(sand_pos.x, sand_pos.y + 1)
            elif (sand_pos.x - 1, sand_pos.y + 1) not in self.blocked:
                sand_pos = Position(sand_pos.x - 1, sand_pos.y + 1)
            elif (sand_pos.x + 1, sand_pos.y + 1) not in self.blocked:
                sand_pos = Position(sand_pos.x + 1, sand_pos.y + 1)
            else:
                # print(sand_pos, "will stop")
                self.blocked.add(sand_pos)
                return True
        if self.has_floor:
            self.blocked.add(sand_pos)
            return True
        return False

def parse(inp):
    data = inp.split("\n")
    return data


def part_a(inp):
    data = parse(inp)
    source = Position(500, 0)
    rocks = []
    for line in data:
        rocks.append([Position(*map(int, p.split(","))) for p in line.split(" -> ")])
    sandbox = SandBox(source, rocks)
    count = 0
    original_blocked = set(sandbox.blocked)
    sand_will_stop = True
    while sand_will_stop:
        sand_will_stop = sandbox.add_sand()
        if not sand_will_stop:
            break
        count += 1
        # print(sandbox.blocked - original_blocked)
    return count


def part_b(inp):
    data = parse(inp)
    source = Position(500, 0)
    rocks = []
    for line in data:
        rocks.append([Position(*map(int, p.split(","))) for p in line.split(" -> ")])
    sandbox = SandBox(source, rocks, True)
    count = 0
    original_blocked = set(sandbox.blocked)
    while source not in sandbox.blocked:
        sandbox.add_sand()
        count += 1
    return count


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 24)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "93")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
